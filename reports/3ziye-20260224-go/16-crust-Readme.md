<p align="center">
  <img src="docs/banner.png" alt="Crust Banner" width="100%" />
</p>

<h1 align="center">Crust</h1>

<p align="center">
  <strong>Your agents should never <del>(try to)</del> read your secrets.</strong>
</p>

<p align="center">
  <a href="https://getcrust.io">Website</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="#built-in-protection">Protection</a> •
  <a href="#how-it-works">How It Works</a> •
  <a href="#documentation">Docs</a> •
  <a href="https://github.com/BakeLens/crust/issues">Issues</a> •
  <a href="https://github.com/BakeLens/crust/discussions">Discussions</a>
</p>

<p align="center">
  <a href="https://github.com/BakeLens/crust/actions/workflows/ci.yml"><img src="https://github.com/BakeLens/crust/actions/workflows/ci.yml/badge.svg" alt="CI" /></a>
  <a href="https://goreportcard.com/report/github.com/BakeLens/crust"><img src="https://goreportcard.com/badge/github.com/BakeLens/crust" alt="Go Report Card" /></a>
  <a href="https://github.com/BakeLens/crust/releases"><img src="https://img.shields.io/github/v/release/BakeLens/crust" alt="Release" /></a>
  <img src="https://img.shields.io/github/go-mod/go-version/BakeLens/crust" alt="Go Version" />
  <img src="https://img.shields.io/badge/License-Elastic%202.0-blue.svg" alt="License" />
  <img src="https://img.shields.io/badge/Platform-macOS%20%7C%20Linux%20%7C%20Windows%20%7C%20FreeBSD-lightgrey" alt="Platform" />
</p>

## What is Crust?

Crust is a transparent, local gateway between your AI agents and LLM providers. It intercepts every tool call — file reads, shell commands, network requests — and blocks dangerous actions before they execute. No code changes required.

**100% local. Your data never leaves your machine.**

<p align="center">
  <img src="docs/demo.gif" alt="Crust in action" width="800" />
</p>

## Quick Start

**macOS / Linux:**
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/BakeLens/crust/main/install.sh)"
```

**Windows (PowerShell):**
```powershell
irm https://raw.githubusercontent.com/BakeLens/crust/main/install.ps1 | iex
```

**Docker:**
```bash
docker build -t crust https://github.com/BakeLens/crust.git
docker run -p 9090:9090 crust
```

Then start the gateway:

```bash
crust start --auto
```

Auto mode detects your LLM provider from the model name — no endpoint URL or API key configuration needed. Your agent's existing auth is passed through.

Point your agent to Crust:

| Agent | Configuration |
|-------|---------------|
| **[Claude Code](https://github.com/anthropics/claude-code)** | `ANTHROPIC_BASE_URL=http://localhost:9090` |
| **[Codex CLI](https://github.com/openai/codex)** | `OPENAI_BASE_URL=http://localhost:9090/v1` |
| **[Cursor](https://cursor.com)** | Settings → Models → Override OpenAI Base URL → `http://localhost:9090/v1` |
| **[Cline](https://github.com/cline/cline)** | Settings → API Configuration → Base URL → `http://localhost:9090/v1` |
| **[Windsurf](https://windsurf.com)** | Settings → AI → Provider Base URL → `http://localhost:9090/v1` |
| **[JetBrains AI](https://www.jetbrains.com/ai/)** | Settings → AI Assistant → Providers & API keys → Base URL → `http://localhost:9090/v1` |
| **[Continue](https://github.com/continuedev/continue)** | Set `apiBase` to `http://localhost:9090/v1` in config |
| **[Aider](https://github.com/Aider-AI/aider)** | `OPENAI_API_BASE=http://localhost:9090/v1` |
| **[Zed](https://github.com/zed-industries/zed)** | Set `api_url` to `http://localhost:9090/v1` in settings |
| **[Tabby](https://github.com/TabbyML/tabby)** | Set `api_endpoint` to `http://localhost:9090/v1` in config |
| **[avante.nvim](https://github.com/yetone/avante.nvim)** | Set `endpoint` to `http://localhost:9090/v1` in config |
| **[codecompanion.nvim](https://github.com/olimorris/codecompanion.nvim)** | Set `url` to `http://localhost:9090/v1` in adapter config |
| **[CodeGPT](https://github.com/timkmecl/codegpt)** | Set custom provider URL to `http://localhost:9090/v1` |
| **[OpenClaw](https://github.com/openclaw/openclaw)** | Set `baseUrl` to `http://localhost:9090` in `~/.openclaw/openclaw.json` |
| **[OpenCode](https://github.com/opencode-ai/opencode)** | `OPENAI_BASE_URL=http://localhost:9090/v1` |
| **Any OpenAI-compatible agent** | Set your LLM base URL to `http://localhost:9090/v1` |

That's it. Crust auto-detects the provider from the model name and passes through your auth. Works with all major coding agents out of the box — each agent's tool names are recognized automatically. Clients that send `/api/v1/...` paths (e.g. some JetBrains configurations) are also supported — the `/api` prefix is stripped automatically.

For providers with non-standard base paths like [OpenRouter](https://openrouter.ai) (`https://openrouter.ai/api`), use `--endpoint` — Crust preserves the upstream base path when forwarding requests.

```bash
crust status     # Check if running
crust logs -f    # Follow logs
crust stop       # Stop crust
```

## Built-in Protection

Crust shi