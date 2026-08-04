# pigo

[![CI](https://github.com/smallnest/pigo/actions/workflows/ci.yml/badge.svg)](https://github.com/smallnest/pigo/actions/workflows/ci.yml)
[![Release](https://github.com/smallnest/pigo/actions/workflows/release.yml/badge.svg)](https://github.com/smallnest/pigo/actions/workflows/release.yml)

使用 Go 复刻的 [pi](https://pi.dev) AI Agent —— 一个面向命令行的编码智能体，同时支持**无头（headless）脚本模式**与**交互式 REPL**。

pigo 可以读写文件、执行命令、检索代码、抓取网页，并借助大模型完成从"读懂需求"到"改好代码"的闭环。它兼容 OpenAI / Anthropic 等多种协议网关，支持会话续跑、项目信任、技能（Skills）、插件与包管理。

> 模块路径：`github.com/smallnest/pigo` · Go 1.27+

> 📖 配套电子书《用 Go 编写 pi Agent》：[write_pi_agent_in_go.pdf](https://github.com/smallnest/ebooks/blob/master/write_pi_agent_in_go.pdf)

![](docs/pigo-tui.png)

---

## 目录

- [特性一览](#特性一览)
- [架构总览](#架构总览)
- [安装与构建](#安装与构建)
- [快速开始](#快速开始)
- [命令行参数](#命令行参数)
- [模型与 Provider](#模型与-provider)
- [内置工具](#内置工具)
- [运行模式](#运行模式)
- [系统提示词组装](#系统提示词组装)
- [项目信任](#项目信任)
- [技能 Skills](#技能-skills)
- [提示词模板](#提示词模板)
- [插件](#插件)
- [Hooks](#hooks)
- [包管理](#包管理)
- [自更新](#自更新)
- [发布release](#发布release)
- [目录与环境变量](#目录与环境变量)
- [安全说明](#安全说明)

---

## 特性一览

- **两种模式**：无头 `-p` 一次性执行（适合脚本 / CI），或直接进入交互式 REPL。
- **多 Provider**：OpenRouter（默认）、本地 Ollama、NVIDIA NIM、Anthropic、任意 OpenAI 兼容端点。
- **内置工具集**：`read` / `write` / `edit` / `grep` / `find` / `bash`（支持 `run_in_background` 后台执行，配套 `bash_output` / `kill_bash`）/ `todo` / `webfetch`。
- **会话续跑**：`--list-sessions` / `--resume` / `--continue`，无头与 REPL 均可续跑。
- **stream-json 输出**：逐行 JSON 事件，首个事件携带 `session_id`，便于调用方关联。
- **系统提示词分层组装**：base 指令 + 环境块 + `AGENTS.md`（general→specific）+ `--append-system-prompt`。
- **项目信任**：副作用工具（bash/write/edit）在未信任目录需确认，`--approve` 一次性授权。
- **技能与插件**：`~/.agents/skills` 下的 `/slash` 命令、`~/.pigo/plugins` 下的外部插件。
- **提示词模板**：`~/.pigo/prompts`、项目 `.pigo/prompts`（受信任时）、config `prompts`、`--prompt-template` 下的可复用 `/name` 模板，支持 `$1`/`$@`/`${1:-default}`/`${@:N}` 等参数语法。
- **上下文自动压缩**：接近上下文窗口上限时自动摘要，亦可 `/compact` 手动触发。
- **包管理**：`pigo install npm:<pkg>` 安装 pi 生态的 extension / skill / prompt / theme。
- **自更新**：无参 `pigo update` 将 pigo 二进制升级到最新 GitHub Release；进入 TUI 时后台检查新版本并在横幅提示。

---

## 架构总览

pigo 的运行时分层架构：请求路径从用户经 CLI、Agent 循环、Provider 层直达 LLM 网关；工具路径从循环经工具执行器与信任闸门抵达本地环境；辅以会话存储与上下文压缩，并标注信任边界与外部网络边界。

![pigo 架构总览](book/images/fig1-1.svg)

> 更多分层图解（事件骨架、统一 Provider、工具批量执行、子 Agent 委派等）见配套电子书。

### Agent 两层循环

运行时的核心是 `internal/runtime/loop.go` 的两层循环：**内层** turn 循环反复「流式回复 → 停止原因分派 → 执行工具 → 回填」，直到某次助手消息不再发起工具调用；**外层**在内层收敛后消费 `GetFollowUpMessages`，有后续消息则重跑内层，否则结束。所有终止路径（自然结束 / error / aborted / 停止钩子 / 无后续消息）都汇于唯一出口 `finish()`。

![pigo Agent 两层循环](book/images/agent-loop-flowchart.svg)

> 交互式版本（含摘要卡片）见 [`docs/agent-loop-flowchart.html`](docs/agent-loop-flowchart.html)。

---

## 安装与构建

需要 Go 1.27 或更高版本。

```bash
# 克隆仓库
git clone https://github.com/smallnest/pigo.git
cd pigo

# 构建二进制（生成 ./pigo）
go build ./cmd/pigo

# 或安装到 $GOPATH/bin
go install ./cmd/pigo

# 也可以不构建，直接运行
go run ./cmd/pigo -p "1+1=?"
```

构建后可查看版本信息（版本号在正式发布时由 goreleaser 注入，源码构建显示 `dev`）：

```bash
pigo --version
# pigo dev (commit none, built unknown)
```

### 一键安装脚本（Linux / macOS）

`install.sh` 会自动检测操作系统 / 架构，从 GitHub Releases 下载最新的预编译二进制并安装到常用的 PATH 目录：

```bash
curl -fsSL https://raw.githubusercontent.com/smallnest/pigo/master/install.sh | sh
```

可用环境变量覆盖默认行为：

| 变量 | 说明 |
|------|------|
| `PIGO_VERSION` | 指定安装版本（形如 `v0.2.0`），默认取最新 release |
| `PIGO_INSTALL_DIR` | 安装目录，默认 `/usr/local/bin`（无写权限时回退到 `~/.local/bin`） |
| `GITHUB_TOKEN` | 可选，用于提高 GitHub API 速率限制 |

```bash
# 指定版本与安装目录
PIGO_VERSION=v0.2.0 PIGO_INSTALL_DIR="$HOME/bin" \
  curl -fsSL https://raw.githubusercontent.com/smallnest/pigo/master/install.sh | sh
```

> Windows 请从 Releases 页面下载 `.zip` 手动解压。

### 下载预编译二进制

[Releases](https://github.com/smallnest/pigo/releases) 页面提供 Linux / macOS / Windows 的 amd64 与 arm64 预编译包（由 goreleaser 构建）。下载对应平台的压缩包解压即可使用。

---

## 快速开始

```bash
# 1. 配置默认 Provider（OpenRouter）的 API Key
export OPENROUTER_API_KEY=sk-or-...

# 2. 无头模式跑一个 prompt，打印最终回答
pigo -p "读取 README 并用三句话总结"

# 3. 进入交互式 REPL（不带 -p 且 stdout 是终端时自动进入）
pigo

# 4. 用本地 Ollama 模型，无需联网
pigo -m ollama/qwen2.5-coder -u http://localhost:11434/v1 -p "解释 main.go 做了什么"
```

---

## 命令行参数

| 长参数 | 短参数 | 默认值 | 说明 |
|--------|--------|--------|------|
| `--print` | `-p` | `""` | 无头打印模式的 prompt（也可用位置参数传入） |
| `--model` | `-m` | `openrouter/free` | 使用的模型 id |
| `--base-url` | `-u` | `""` | 覆盖 Provider 的 base URL（如本地 Ollama） |
| `--api-key` | `-k` | `""` | 指定 Provider 的 API Key（覆盖 env/config，否则读 `<PROVIDER>_API_KEY`） |
| `--protocol` | `-P` | `""` | 强制线路协议：`openai` \| `anthropic`（默认由 model id 推断） |
| `--output-format` | `-o` | `text` | 输出格式：`text` \| `stream-json` |
| `--no-tools` | `-n` | `false` | 禁用内置文件/shell 工具（同时跳过插件发现） |
| `--list-sessions` | `-l` | `false` | 列出已存储的会话并退出 |
| `--resume` | `-r` | `""` | 续跑指定 id 的会话 |
| `--continue` | `-c` | `false` | 续跑最近一次的会话 |
| `--approve` | `-a` | `false` | 为本次运行信任工作目录：跳过首次信任提示，副作用工具免逐次确认 |
| `--no-skills` | | `false` | 禁用技能发现（不加载 `~/.agents/skills` 为 `/skill-name` 命令） |
| `--no-prompt-templat