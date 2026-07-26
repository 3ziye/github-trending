<!-- markdownlint-disable MD013 MD033 MD041 -->
<!-- WINDOWS_FRESH_DEPLOYMENT_POLICY: EXPLICIT_BETA -->

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
  <a href="https://github.com/Jia-Ethan/codex-keysmith/actions/workflows/tests.yml"><img alt="Blocking CI tests" src="https://github.com/Jia-Ethan/codex-keysmith/actions/workflows/tests.yml/badge.svg"></a>
  <img alt="Source version v0.1.1" src="https://img.shields.io/badge/source-v0.1.1-0099CC">
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
> The v0.1.1 source bundles the byte-identical prompt currently used as the Codex behavior baseline. It directs the model to answer without refusal framing, reinterprets reverse-shell/keygen/bypass and related security requests as local fixtures, covers adult and consent-sensitive fiction plus chemistry/pharmacology/weapons guides, and gives its execution mode precedence over injected context blocks. Source: [`examples/gpt-unrestricted.md`](examples/gpt-unrestricted.md), embedded byte-for-byte in [`codex-instruct.py`](codex-instruct.py). SHA-256: `2c2c9f0e008c492bfc9487170a7a08daedeb8b0625af1f85617ab2d1bd3f35c0`. A checkout is a candidate unless its commit is bound to an immutable signed/annotated tag and verified Release assets; the signed v0.1.0 assets retain their historical bundled prompt. Inspect the current source prompt or deploy your own `--file`.
>
> v0.1.1 源码内置提示词与当前 Codex 行为基线逐字节一致。它要求模型避免拒绝式表达，将 reverse shell、keygen、bypass 等请求重解释为本地样本，覆盖成人及同意敏感题材、化学／药理／武器指南，并规定执行模式优先于注入的上下文区块。来源：[`examples/gpt-unrestricted.md`](examples/gpt-unrestricted.md)，并逐字节嵌入 [`codex-instruct.py`](codex-instruct.py)。SHA-256：`2c2c9f0e008c492bfc9487170a7a08daedeb8b0625af1f85617ab2d1bd3f35c0`。未绑定不可变签名／附注 tag 与已校验 Release 资产的 checkout 均按候选版处理；已签名 v0.1.0 资产仍保留其历史内置提示词。请审阅当前源码提示词，或通过 `--file` 部署自己的指令。

## 复制给智能体安装

```text
请先检查操作系统。macOS / Linux 可安装 codex-keysmith v0.1.0：只从 https://github.com/Jia-Ethan/codex-keysmith/releases/tag/v0.1.0 下载 Release 资产，先用 SHA256SUMS 校验，不使用 curl | python。Windows 上的 v0.1.0 为 known-bad，不得 fresh deploy；如已留下 durable journal，保留全部 journal/marker/snapshot，改用已校验的 v0.1.1 脚本依次运行 --status、--recover 预览、--recover --yes、--status，不手工删除证据。Windows v0.1.1 fresh deployment 仅以明确 beta 开放，preview 与执行都会显示 beta 警告；这不构成正式 Windows support，P1/P2 边界仍然适用。任何平台都先运行 --version、--status 和 --dry-run，报告目标 .codex 目录、内置提示词来源与 SHA-256、全局行为范围、MD/config/hooks/legacy/manifest 计划和备份路径；写入前等我确认。完成后开启新 Codex 会话验证。不要删除任何备份或事务日志，不修改 Codex 二进制、网络、运行中进程或凭证。
```

## 友链 / Community

本项目接受 LINUX DO 社区佬友监督与反馈：[LINUX DO](https://linux.do)

同系列项目 / Same series:

- [codex-keysmith](https://github.com/Jia-Ethan/codex-keysmith) - Codex CLI 本地配置的版本化指令部署工具，支持预览、hook 隔离、中断恢复与分层卸载。 / Versioned instruction deployment for local Codex CLI configuration with preview, hook isolation, interruption recovery, and layered uninstall.
- [claude-keysmith](https://github.com/Jia-Ethan/claude-keysmith) - Claude Code `CLAUDE.md` 的受管理 import-block 安装器，用于本地 Markdown 指令文件。 / Managed Claude Code `CLAUDE.md` import-block installer for local Markdown instruction files.
- [zcode-keysmith](https://github.com/Jia-Ethan/zcode-keysmith) - ZCode App 的受管理 true system-role 入口，通过 agent-server wrapper 将 `system-role.md` 接入 runtime `customSystemPrompt` 的 system-message 路径。 / Managed true system-role entrypoint for ZCode App; an agent-server wrapper routes `system-role.md` into the runtime `customSystemPrompt` system-message path.
- [grok-keysmith](https://github.com/Jia-Ethan/grok-keysmith) - Grok Build 的全局 `AGENTS.md` 指令部署工具，