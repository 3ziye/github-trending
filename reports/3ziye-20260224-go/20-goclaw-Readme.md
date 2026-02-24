# goclaw (🐾 狗爪)

Go 语言版本的 OpenClaw - 一个功能强大的 AI Agent 框架。

[![License](https://img.shields.io/:license-MIT-blue.svg)](https://opensource.org/licenses/MIT) [![go.dev reference](https://img.shields.io/badge/go.dev-reference-007d9c?logo=go&logoColor=white&style=flat-square)](https://pkg.go.dev/github.com/smallnest/goclaw) [![github actions](https://github.com/smallnest/goclaw/actions/workflows/go.yaml/badge.svg)](https://github.com/smallnest/goclaw/actions) [![Go Report Card](https://goreportcard.com/badge/github.com/smallnest/goclaw)](https://goreportcard.com/report/github.com/smallnest/goclaw) [![Coverage Status](https://coveralls.io/repos/github/smallnest/goclaw/badge.svg?branch=master)](https://coveralls.io/github/smallnest/goclaw?branch=master)


![](docs/goclaw.png)

## 功能特性

- 🛠️ **完整的工具系统**：FileSystem、Shell、Web、Browser，支持 Docker 沙箱与权限控制
- 📚 **技能系统 (Skills)**：兼容 [OpenClaw](https://github.com/openclaw/openclaw) 和 [AgentSkills](https://agentskills.io) 规范，支持自动发现与环境准入控制 (Gating)
- 💾 **持久化会话**：基于 JSONL 的会话存储，支持完整的工具调用链 (Tool Calls) 记录与恢复
- 📢 **多渠道支持**：Telegram、WhatsApp、飞书 (Feishu)、QQ、企业微信 (WeWork)
- 🔧 **灵活配置**：支持 YAML/JSON 配置，热加载
- 🎯 **多 LLM 提供商**：OpenAI (兼容接口)、Anthropic、OpenRouter，支持故障转移
- 🌐 **WebSocket Gateway**：内置网关服务，支持实时通信
- ⏰ **Cron 调度**：内置定时任务调度器
- 🖥️ **Browser 自动化**：基于 Chrome DevTools Protocol 的浏览器控制

## 技能系统 (New!)

goclaw 引入了先进的技能系统，允许用户通过编写 Markdown 文档 (`SKILL.md`) 来扩展 Agent 的能力。

### 特性
*   **Prompt-Driven**: 技能本质上是注入到 System Prompt 中的指令集，指导 LLM 使用现有工具 (exec, read_file 等) 完成任务。
*   **OpenClaw 兼容**: 完全兼容 OpenClaw 的技能生态。您可以直接将 `openclaw/skills` 目录下的技能复制过来使用。
*   **自动准入 (Gating)**: 智能检测系统环境。例如，只有当系统安装了 `curl` 时，`weather` 技能才会生效；只有安装了 `git` 时，`git-helper` 才会加载。

### 使用方法

#### 配置文件加载优先级

goclaw 按以下顺序查找配置文件（找到第一个即使用）：

1. `~/.goclaw/config.json` (用户全局目录，**最高优先级**)
2. `./config.json` (当前目录)

可通过 `--config` 参数指定配置文件路径覆盖默认行为。

#### Skills 加载顺序

技能按以下顺序加载，**同名技能后面的会覆盖前面的**：

| 顺序 | 路径 | 说明 |
|-----|------|------|
| 1 | `传入的自定义目录` | 通过 `NewSkillsLoader()` 指定 |
| 2 | `workspace/skills/` | 工作区目录 |
| 3 | `workspace/.goclaw/skills/` | 工作区隐藏目录 |
| 4 | `<可执行文件路径>/skills/` | 可执行文件同级目录 |
| 5 | `./skills/` (当前目录) | **最后加载，优先级最高** |

默认 `workspace` 为 `~/.goclaw/workspace`。

1.  **列出可用技能**
    ```bash
    ./goclaw skills list
    ```

2.  **安装技能**
    将技能文件夹放入以下任一位置：
    *   `./skills/` (当前目录，最高优先级)
    *   `${WORKSPACE}/skills/` (工作区目录)
    *   `~/.goclaw/skills/` (用户全局目录)

3.  **编写技能**
    创建一个目录 `my-skill`，并在其中创建 `SKILL.md`：
    ```yaml
    ---
    name: my-skill
    description: A custom skill description.
    metadata:
      openclaw:
        requires:
          bins: ["python3"] # 仅当 python3 存在时加载
    ---
    # My Skill Instructions
    When the user asks for X, use `exec` to run `python3 script.py`.
    ```

## 项目结构

```
goclaw/
├── agent/              # Agent 核心逻辑
│   ├── loop.go         # Agent 循环
│   ├── context.go      # 上下文构建器
│   ├── memory.go       # 记忆系统
│   ├── skills.go       # 技能加载器
│   ├── subagent.go     # 子代理管理器
│   └── tools/          # 工具系统
│       ├── filesystem.go   # 文件系统工具
│       ├── shell.go        # Shell 工具
│       ├── web.go          # Web 工具
│       ├── browser.go      # 浏览器工具
│       └── message.go      # 消息工具
├── channels/           # 消息通道
│   ├── base.go         # 通道接口
│   ├── manager.go      # 通道管理器
│   ├── telegram.go     # Telegram 实现
│   ├── whatsapp.go     # WhatsApp 实现
│   ├── feishu.go       # 飞书实现
│   ├── qq.go           # QQ 实现
│   ├── wework.go       # 企业微信实现
│   ├── googlechat.go   # Google Chat 实现
│   └── teams.go        # Microsoft Teams 实现
├── bus/                # 消息总线
│   ├── events.go       # 消息事件
│   └── queue.go        # 消息队列
├── config/             # 配置管理
│   ├── schema.go       # 配置结构
│   └── loader.go       # 配置加载器
├── providers/          # LLM 提供商
│   ├── base.go         # 提供商接口
│   ├── factory.go      # 提供商工厂
│   ├── openai.go       # OpenAI 实现
│   ├── anthropic.go    # Anthropic 实现
│   └── openrouter.go   # OpenRouter 实现
├── gateway/            # WebSocket 网关
│   ├── server.go       # 网关服务器
│   ├── handler.go      # 消息处理器
│   └── protocol.go     # 协议定义
├── cron/               # 定时任务调度
│   ├── scheduler.go    # 调度器
│   └── cron.go         # Cron 任务
├── session/            # 会话管理
│   └── manager.go      # 会话管理器
├── cli/                # 命令行界面
│   ├── root.go         # 根命令
│   ├── agent.go        # Agent 命令
│   ├── agents.go       # Agents 管理命令
│   ├── sessions.go     # 会话命令
│   ├── cron_cli.go     # Cron 命令
│   ├── approvals.go    # 审批命令
│   ├── system.go       # 系统命令
│   └── commands/       # 子命令
│       ├── tui.go      # TUI 命令
│       ├── gateway.go  # Gateway 命令
│       ├── browser.go  # Browser 命令
│       ├── health.go   # 健康检查
│       ├── status.go   # 状态查询
│       ├── memory.go   # 记忆管理
│       └── logs.go     # 日志查询
├── internal/           # 内部包
│   ├── logger/         # 日志
│   └── utils/          # 工具函数
├── docs/               # 文档
│   ├── cli.md          # CLI 详细文档
│   └── INTRODUCTION.md # 项目介绍
└── main.go             # 主入口
```

## 快速开始

### 安装

``