# Whale

<p align="center">
  <img src="docs/logo.svg" alt="Whale — DeepSeek-native coding agent for the terminal" width="640">
</p>

<p align="center">
  <a href="./README.zh.md">简体中文</a> · <strong>English</strong>
</p>

<p align="center">
  <a href="https://github.com/usewhale/DeepSeek-Code-Whale/releases"><img src="https://img.shields.io/github/v/release/usewhale/DeepSeek-Code-Whale?label=release" alt="release"></a>
  <a href="https://github.com/usewhale/DeepSeek-Code-Whale/actions/workflows/ci.yml"><img src="https://github.com/usewhale/DeepSeek-Code-Whale/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/github/license/usewhale/DeepSeek-Code-Whale" alt="license"></a>
  <a href="https://github.com/usewhale/DeepSeek-Code-Whale/stargazers"><img src="https://img.shields.io/github/stars/usewhale/DeepSeek-Code-Whale?style=flat&logo=github&label=stars" alt="GitHub stars"></a>
</p>

<p align="center">
  <strong>Whale is an unofficial DeepSeek CLI / DeepSeek coding agent for the terminal.</strong><br>
  It can read code, edit files, run commands, and extend the agent with MCP and Skills.
</p>

<p align="center">
  <strong>90% live prefix-cache hit</strong> · <strong>~30x cheaper per task vs Claude Code</strong> · terminal-first · open source
</p>

<p align="center"><a href="./ROADMAP.md">📋 Roadmap · View current direction and available tasks</a></p>

---

## Quick Start

Install with the script:

```bash
curl -fsSL https://raw.githubusercontent.com/usewhale/DeepSeek-Code-Whale/main/scripts/install.sh | sh
```

Install with Homebrew:

```bash
brew install usewhale/tap/whale
```

**Windows PowerShell:**

```powershell
irm https://raw.githubusercontent.com/usewhale/DeepSeek-Code-Whale/main/scripts/install.ps1 | iex
```

**Windows CMD (Command Prompt):**

```cmd
powershell -NoProfile -ExecutionPolicy Bypass -Command "irm https://raw.githubusercontent.com/usewhale/DeepSeek-Code-Whale/main/scripts/install.ps1 | iex"
```

The installer prefers the Windows x64 or ARM64 package for your system and adds `whale.exe` to the current user's `PATH`. If an older release does not include an ARM64 package, it falls back to x64 emulation. You can also download the matching Windows zip manually from [GitHub Releases](https://github.com/usewhale/DeepSeek-Code-Whale/releases).

First run:

```bash
whale setup
whale doctor
whale
```

Upgrade:

```bash
brew upgrade usewhale/tap/whale
# or rerun the install script
```

Whale currently uses the DeepSeek API. Before running Whale, create an API key in the [DeepSeek Platform](https://platform.deepseek.com/). See the [DeepSeek API docs](https://api-docs.deepseek.com/) for API details.

> **Platform support:** Whale currently supports **macOS**, **Linux**, and **Windows**.

You can also run a one-shot prompt:

```bash
whale exec "Explain what this repository does"
printf 'Summarize the current directory\n' | whale exec
```

---

## How It Compares

|                          | Whale | Claude Code | Codex CLI | Cursor | Aider |
|--------------------------|-------|-------------|-----------|--------|-------|
| Primary interface        | Terminal TUI/CLI | Terminal agent | Terminal agent | IDE | CLI |
| Default backend          | DeepSeek | Anthropic | OpenAI | Multi-model | Multi-model |
| DeepSeek optimized       | yes | no | no | no | limited |
| Prefix-cache friendly    | yes | n/a | n/a | model-dependent | limited |
| Local code read/write    | yes | yes | yes | yes | yes |
| Shell / test execution   | yes | yes | yes | partial | yes |
| `/ask` read-only mode    | yes | partial | partial | n/a | partial |
| `/plan` planning mode    | yes | yes | yes | n/a | partial |
| MCP                      | yes | yes | version-dependent | partial | partial |
| Skills / reusable workflows | yes | yes | yes | partial | limited |
| Open source              | yes | no | yes | no | yes |

Whale is not trying to support every model. Its focus is turning the DeepSeek API into a stable, low-cost local coding agent that can stay open for long development sessions.

<details>
<summary><strong>Why DeepSeek-only?</strong></summary>

DeepSeek's low token price is only part of the story. The real advantage for long-running coding agents is prefix caching.

DeepSeek's prefix cache is sensitive to byte stability. Whale's loop is designed around that constraint: append-only turns, stable context ordering, and recoverable session records help long tasks keep benefiting from cached prefixes.

That is why Whale is not rushing toward a generic provider abstraction. Claude, OpenAI, and DeepSeek differ in cache mechanics, tool-call behavior, and reasoning controls. A generic wrapper usually hides the DeepSeek-specific parts that matter most.

Whale includes DeepSeek-specific handling for:

| Generic agent assumption | What DeepSeek can do | Whale's handling |
|--------------------------|----------------------|------------------|
| Tool-call JSON is stable | Payloads can 