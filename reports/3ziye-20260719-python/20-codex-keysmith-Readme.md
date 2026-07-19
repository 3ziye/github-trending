<!-- markdownlint-disable MD013 MD033 MD041 -->

<p align="center">
  <img src="docs/assets/readme/codex-keysmith-preview.png" alt="Illustrative codex-keysmith dry-run terminal preview; actual paths and output vary" width="100%">
</p>
<p align="center"><em>Illustrative preview / 示意预览；实际路径与输出以本机 dry-run 为准。</em></p>

<h1 align="center">codex-keysmith</h1>

<p align="center">
  Versioned Codex instruction deployment with preview, ownership manifests, hook isolation, and layered uninstall.
</p>

<p align="center">
  <a href="#简体中文">简体中文</a> ·
  <a href="#english">English</a> ·
  <a href="CONTRIBUTING.md">Contributing</a> ·
  <a href="SECURITY.md">Security</a> ·
  <a href="LICENSE">License</a>
</p>

<p align="center">
  <a href="https://github.com/Jia-Ethan/codex-keysmith/actions/workflows/tests.yml"><img alt="Tests" src="https://github.com/Jia-Ethan/codex-keysmith/actions/workflows/tests.yml/badge.svg"></a>
  <img alt="Release v0.1.0" src="https://img.shields.io/badge/release-v0.1.0-0099CC">
  <img alt="Python 3.10 to 3.14 recommended" src="https://img.shields.io/badge/Python-3.10--3.14-3776AB?logo=python&logoColor=white">
  <img alt="License MIT" src="https://img.shields.io/badge/license-MIT-6DB33F">
</p>

> [!IMPORTANT]
> **Global behavior boundary / 全局行为边界**
>
> A confirmed deployment changes the top-level `model_instructions_file` in the selected Codex configuration. The instruction therefore applies to every new Codex session that loads that configuration; it is not a per-project sandbox. By default, deployment also pauses the entire active `hooks.json` until explicitly restored. The tool does not patch Codex binaries, intercept traffic, or store credentials.
>
> 确认部署会修改所选 Codex 配置中的顶层 `model_instructions_file`，因此该指令会影响所有加载此配置的新 Codex 会话，并非项目级沙箱。默认部署还会暂停整份活跃 `hooks.json`，直到显式恢复。工具不修改 Codex 二进制、不劫持网络，也不保存凭证。

> [!WARNING]
> **Read the bundled prompt before using `--yes` / 使用 `--yes` 前先阅读内置提示词**
>
> The v0.1.0 bundled prompt directs the model to answer without refusal framing, reinterprets reverse-shell/keygen/bypass and related security requests as local fixtures, covers adult and consent-sensitive fiction, chemistry/pharmacology/weapons guides, and treats injected memory, hook, and session blocks as environment metadata that cannot override its execution mode. This is a broad global behavior change, not an authorization or safety boundary. Source: [`examples/gpt-unrestricted.md`](examples/gpt-unrestricted.md), embedded byte-for-byte in [`codex-instruct.py`](codex-instruct.py). SHA-256: `0ac8420d504f1a42db87be9f8555f740bf4c1e7b72beb0dde6a4b8d70b6cda07`. Inspect it or deploy your own `--file`. The normal preview plus one explicit `--yes` remains the confirmation flow; there is no second confirmation flag.
>
> v0.1.0 内置提示词要求模型避免拒绝式表达，将 reverse shell、keygen、bypass 等安全请求重解释为本地样本，覆盖成人及同意敏感题材、化学／药理／武器指南，并把注入的 memory、hook 和 session 区块视为不能覆盖其执行模式的环境元数据。这是范围很广的全局行为变更，不构成授权或安全边界。来源：[`examples/gpt-unrestricted.md`](examples/gpt-unrestricted.md)，并逐字节嵌入 [`codex-instruct.py`](codex-instruct.py)。SHA-256：`0ac8420d504f1a42db87be9f8555f740bf4c1e7b72beb0dde6a4b8d70b6cda07`。请先审阅，或通过 `--file` 部署自己的指令。确认流程仍是常规预览加一次显式 `--yes`，不增加第二个确认参数。

## 复制给智能体安装

```text
请安装 codex-keysmith v0.1.0。只从 https://github.com/Jia-Ethan/codex-keysmith/releases/tag/v0.1.0 下载 Release 资产，先用 SHA256SUMS 校验，不使用 curl | python。运行 --version、--status 和 --dry-run，报告目标 .codex 目录、内置提示词来源与 SHA-256、全局行为范围、MD/config/hooks/legacy/manifest 计划和备份路径；如果 status 发现 durable journal，只预览 --recover 并等我确认后才添加 --yes。完成后开启新 Codex 会话验证。不要删除任何备份或事务日志，不修改 Codex 二进制、网络、运行中进程或凭证。
```

## 友链 / Community

本项目接受 LINUX DO 社区佬友监督与反馈：[LINUX DO](https://linux.do)

同系列项目 / Same series:

- [codex-keysmith](https://github.com/Jia-Ethan/codex-keysmith) - Codex CLI instruction-file deployment for local configuration.
- [claude-keysmith](https://github.com/Jia-Ethan/claude-keysmith) - Claude Code `CLAUDE.md` import-block installer for local instruction files.
- [zcode-keysmith](https://github.com/Jia-Ethan/zcode-keysmith) - ZCode `AGENTS.md` installer for local instructions.

---

## 简体中文

### 项目定位

`codex-keysmith` v0.1.0 是零运行时依赖的单文件 Python CLI。它把内置或自定义 Markdown 部署到现有 Codex 配置目录，保守更新顶层 `model_instructions_file`，默认整体隔离活跃 hooks，并用带指纹的部署清单支持分层卸载。部署在首次修改前还会发布持久化事务日志，使 `SIGKILL` 等中断可以通过显式 `--recover` 检查和恢复。

默认不写入：常规部署、卸载和中断恢复在没有 `--yes` 时都只预览。`--status` 和 `--skip-hooks-isolation` 计划都不会打开或解析 hooks 内容；status 发现持久化日志或其他事务残留时 fail closed。durable deployment journal 使用 `--recover`，无 journal 的异常残留保留人工核对。

### 下载、校验与安装 v0.1.0

固定来源：

- [v0.1.0 Release](https://github.com/Jia-Ethan/codex-keysmith/releases/tag/v0.1.0)
- [v0.1.0 source tag](https://github.com/Jia-Ethan/codex-keysmith/tree/v0.1.0)
- Release bundle：`codex-keysmith-v0.1.0.zip`、`codex-keysmith-v0.1.0.tar.gz`
- 独立脚本：`codex-instruct-v0.1.0.py`
- 校验清单：`SHA256SUMS`

不要从浮动 `main` 安装正式版本，也不要使用 `curl | python`。先把文件保存到磁盘，校验后再执行。

macOS / Linux：

```bash
base='https://github.com/Jia-Ethan/codex-keysmith/releases/download/v0.1.0'
for file in \
  codex-keysm