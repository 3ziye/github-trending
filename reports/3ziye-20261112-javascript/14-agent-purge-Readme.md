<div align="center">

# agent-purge

**一份人设，统一管理多个 coding agent。**

[English](README.en.md) | [日本語](README.ja.md) | 简体中文

[![npm](https://img.shields.io/npm/v/agent-purge)](https://www.npmjs.com/package/agent-purge)
[![stars](https://img.shields.io/github/stars/ZiChuanLan/agent-purge)](https://github.com/ZiChuanLan/agent-purge/stargazers)
[![license](https://img.shields.io/npm/l/agent-purge)](LICENSE)

<p>
  <a href="https://trendshift.io/repositories/321425?utm_source=trendshift-badge&amp;utm_medium=badge&amp;utm_campaign=badge-trendshift-321425" target="_blank" rel="noopener noreferrer">
    <img src="https://trendshift.io/api/badge/trendshift/repositories/321425/daily?language=JavaScript" alt="ZiChuanLan/agent-purge | Trendshift" width="250" height="55"/>
  </a>
</p>

[快速开始](#快速开始) · [人设与模式](#人设与模式) · [应用范围](#应用范围) · [支持情况](#支持情况) · [暂停与卸载](#暂停与卸载) · [免责与合规声明](#免责与合规声明)

</div>

agent-purge 是一个本地提示词配置工具，为 Codex、Claude Code、OpenCode、pi 等执行器提供统一的人设管理入口。你可以在 Web 控制台中配置，也可以直接通过命令行启动；不同执行器仍保留自己的工具、模型和工作流程。

## 核心能力

- **一份配置，多种入口**：CLI 与 Web 共用人设和状态，支持单次启动、常驻配置、会话扩展与项目规则。
- **按执行器独立设置**：默认跟随全局，也能为某个执行器单独选择人设或模式。
- **支持热切，也说明边界**：具备每轮回调的动态通道可在下一轮读取变更；静态入口需要新会话。
- **变更可追溯、可撤销**：记录托管写入和恢复依据；外部修改会保留，恢复冲突明确报错。
- **本地优先、零生产依赖**：不需要额外云端配置服务，人设与程序分开保存，升级不覆盖用户数据。

## 快速开始

需要 **Node.js 20+**，并先安装你要使用的 coding agent。

```bash
npm install -g agent-purge
agent-purge web
```

也可以直接使用 `npx agent-purge web`，不进行全局安装。

1. 在「人设库」编辑起步模板，或新建自己的人设。
2. 回到「控制台」选择人设和模式，保存设置，再开启需要管理的执行器。
3. 按执行器详情中的提示，新建会话或重新加载插件。

控制台默认地址为 `http://127.0.0.1:7788`。首次打开不会自动接管所有执行器；默认启动项与应用范围分别配置。

![agent-purge 控制台](docs/images/console-desktop.png)

[查看窄屏布局](docs/images/console-mobile.png)

<details>
<summary>其他安装方式：Windows 安装器、便携包与无桌面环境</summary>

| 形式 | 运行要求 | 适用场景 |
|---|---|---|
| npm | Node.js 20+ | 用 npm 安装与升级 |
| `agent-purge-<版本>-setup.exe` | Windows，外部 Node.js 20+ | 图形安装和卸载 |
| `agent-purge-<版本>.zip` | Windows，外部 Node.js 20+ | 解压后使用 |
| `agent-purge.exe` | Windows x64，自带运行时 | 无需另装 Node 的独立便携版 |

下载附件以实际 [GitHub Releases](https://github.com/ZiChuanLan/agent-purge/releases) 为准；未发布的版本没有附件。请核对 SHA-256 和签名状态，未签名程序可能出现系统提示。ZIP 中的 EXE 是薄启动器，不是自带运行时的独立版。

SSH / WSL 等无桌面环境使用 `agent-purge web --no-open`。Web 仅监听本机；Linux/macOS 使用 npm 或源码入口，不能运行 Windows EXE。平台验证范围见[兼容性说明](docs/compatibility.md)。

控制台右上角的版本角标点开就是升级入口，按安装形态自动选路：独立 EXE 下载并就地热替换、npm 全局安装调 `npm install -g`、**源码检出（`git clone` 后直接 `node bin/agent-purge.mjs`）在安装目录执行 `git pull --ff-only`**，不下载任何发布产物。源码检出的「有没有更新」按上游提交算，版本号没变也会提示；工作区有未提交改动、处于游离 HEAD 或分支没有上游时一律拒绝并说明原因。

</details>

## 人设与模式

人设正文决定要提供给执行器的提示词；名称和说明只用于管理。首次运行会生成 `neutral` 起步模板，你可以在 Web 中直接编辑，也可以创建自己的 Markdown 文件。

```bash
agent-purge ls                       # 查看人设
agent-purge use <id>                 # 切换并同步已选范围
agent-purge mode append              # 修改全局模式
agent-purge use <id> --for codex     # 只给 Codex 指定人设
agent-purge use follow --for codex   # 恢复跟随全局
```

### 四种处理模式

| 模式 | 行为 | 注意 |
|---|---|---|
| `replace`（默认） | 优先替换宿主身份行，尽量保留其他说明 | 身份识别是近似处理；无法读取宿主文本的启动入口按 strict 执行 |
| `strict` | 用人设替换可控入口中的宿主文本 | 该入口原有说明也会移除；宿主仍可能添加额外文本 |
| `append` | 保留宿主说明，另加一份人设 | 不替换原身份，需注意规则冲突 |
| `off` | 停止相应入口注入 | 全局暂停与单次启动参数的作用范围不同 |

**strict 不等于“模型只收到人设”。** 实际角色可能是 `system`、`developer` 或项目上下文，取决于宿主和通道。希望保留宿主说明时，可先试 `append`。

<details>
<summary>手写人设示例与存储位置</summary>

将以下内容保存为 `~/.agent-purge/personas/concise.md`，然后执行 `agent-purge use concise`：

```markdown
---
id: concise
name: 简洁协作
description: 中文、先结论、修改前先读代码
---

用简体中文协作。先给结论，再给依据。
修改代码前先阅读现有实现；不确定时明确说明。
```

只有正文进入提示词。`description` 用于列表说明，旧键 `desc` 仍兼容；Web 编辑会保留未涉及的元数据。高级匹配、排序与数据目录配置见[使用指南](docs/usage.md#人设文件)。

也可参考维护者的 [some-magic 人设仓库](https://github.com/ZiChuanLan/some-magic)。

</details>

## 应用范围

只想临时使用，可以通过 agent-purge 启动一次，不必登记常驻通道：

```bash
agent-purge codex --mode append
agent-purge pi --ask "解释这段代码"
agent-purge codex -- --help          # -- 后的参数交给宿主
```

要让其他启动入口也读取配置，再按需选择以下通道：

| 通道 | 做什么 | 生效时机 |
|---|---|---|
| `install` | 写入宿主的托管配置或插件 | 静态配置需新会话；已加载动态插件下一轮读取 |
| `shim` | 通过 PATH 中的同名命令转发启动 | 下一次从该命令启动 |
| `slash` | 安装会话内 `/purge` 扩展 | 取决于宿主扩展和启用状态 |
| `project` | 写入指定目录的项目规则文件 | 对应目录的新会话 |

```bash
agent-purge install codex
agent-purge arm pi --slash
agent-purge project on pi --dir /path/to/project
agent-purge status
```

`arm <h>` 会尝试开启该执行器可用的常驻、命令和 slash 通道，结果逐项报告；项目通道需单独选择。同一人设经多个入口提供时可能重复，建议只开启需要的范围。

**使用 magpie 网关？** 可选插件位于 `magpie-plugin/`，不是仓库根目录。安装方法和网关改写边界见 [magpie 插件说明](magpie-plugin/README.md)。

## 支持情况

以下为支持范围与当前验证程度；请求级验证只覆盖表中明确说明的宿主，不是对所有版本的兼容承诺。

| 执行器 | 已验证版本 | 同会话热切 |
|---|---|---|
| pi / omp | 1.4.0 / 18.14.1 | 已验证（动态扩展） |
| OpenCode 1.x / 2.x | 1.19.5 / 2.2.5 | 已验证 |
| DSH | 0.2.1-rc.5 | 已验证（SDK 同会话；headless/web/desktop 三形态四模式已抓） |
| Codex / Claude Code | 0.166.0 / 2.1.316 | 启动入口已验证；热切未验证 |
| CodeBuddy / Grok | 2.179.0 / 1.0.73 | 启动入口已验证；热切未验证 |
| Kilo Code | @kilocode/cli 7.8.18 | off/strict/replace/append 四模式真实抓包；system 层 marker=1 |
| Antigravity（App + CLI `agy`） | CLI 1.5.3 / 语言服务 1.23.x | off/strict/replace/append 四模式真实抓包；写 `~/.gemini/config/AGENTS.md`，落 