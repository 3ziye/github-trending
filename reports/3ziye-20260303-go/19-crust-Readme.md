<p align="center">
  <img src="docs/banner.png" alt="Crust Banner" width="100%" />
</p>

<h1 align="center">Crust</h1>

<p align="center">
  <strong>Your agents should never <del>(try to)</del> read your secrets.</strong>
</p>

<p align="center">
  <a href="https://getcrust.io">Website</a> •
  <a href="#how-it-works">How It Works</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="#agent-setup">Agent Setup</a> •
  <a href="#protection">Protection</a> •
  <a href="#documentation">Docs</a> •
  <a href="https://github.com/BakeLens/crust/issues">Issues</a> •
  <a href="https://github.com/BakeLens/crust/discussions">Discussions</a>
</p>

<p align="center">
  <a href="https://github.com/BakeLens/crust/actions/workflows/ci.yml"><img src="https://github.com/BakeLens/crust/actions/workflows/ci.yml/badge.svg" alt="CI" /></a>
  <a href="https://codecov.io/gh/BakeLens/crust"><img src="https://codecov.io/gh/BakeLens/crust/graph/badge.svg" alt="Coverage" /></a>
  <a href="https://goreportcard.com/report/github.com/BakeLens/crust"><img src="https://goreportcard.com/badge/github.com/BakeLens/crust" alt="Go Report Card" /></a>
  <a href="https://github.com/BakeLens/crust/releases"><img src="https://img.shields.io/github/v/release/BakeLens/crust" alt="Release" /></a>
  <img src="https://img.shields.io/github/go-mod/go-version/BakeLens/crust" alt="Go Version" />
  <img src="https://img.shields.io/badge/License-Elastic%202.0-blue.svg" alt="License" />
  <img src="https://img.shields.io/badge/Platform-macOS%20%7C%20Linux%20%7C%20Windows%20%7C%20FreeBSD-lightgrey" alt="Platform" />
</p>

<p align="center">
  <a href="https://github.com/BakeLens/crust/blob/main/SECURITY.md"><img src="https://img.shields.io/badge/Security%20Policy-Responsible%20Disclosure-green" alt="Security Policy" /></a>
  <img src="https://img.shields.io/badge/SAST-gosec%20%7C%20semgrep-blueviolet" alt="SAST" />
  <img src="https://img.shields.io/badge/Fuzz%20Tested-32%20targets-orange" alt="Fuzz Tested" />
  <img src="https://img.shields.io/badge/Secrets-govulncheck%20%7C%20gitleaks-critical" alt="Secret Scanning" />
</p>

## What is Crust?

Crust is a transparent, local gateway between your AI agents and LLM providers. It intercepts every tool call — file reads, shell commands, network requests — and blocks dangerous actions before they execute. No code changes required.

**100% local. Your data never leaves your machine.**

<p align="center">
  <img src="docs/demo.gif" alt="Crust in action" width="800" />
</p>

## How It Works

<p align="center">
  <img src="docs/crust.png" alt="Crust architecture" width="90%" />
</p>

Crust inspects tool calls at multiple layers:

1. **Layer 0 (Request Scan)**: Scans tool calls in conversation history before they reach the LLM — catches agents replaying dangerous actions.
2. **Layer 1 (Response Scan)**: Scans tool calls in the LLM's response before they execute — blocks new dangerous actions in real-time.
3. **Stdio Proxy** ([MCP](docs/mcp.md) / [ACP](docs/acp.md)): Wraps MCP servers or ACP agents as a stdio proxy, intercepting security-relevant JSON-RPC messages in both directions — including DLP scanning of server responses for leaked secrets.

All modes apply a [15-step evaluation pipeline](docs/how-it-works.md) with a self-protection pre-filter — input sanitization, Unicode normalization, obfuscation detection, DLP secret scanning, path-based rules, and fallback content matching — each step in microseconds.

All activity is logged locally to encrypted storage.

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
docker compose up -d        # uses the included docker-compose.yml
# or manually:
docker build -t crust https://github.com/BakeLens/crust.git
docker run -p 9090:9090 crust
```

Then start the gateway:

```bash
crust start --auto
```

Auto mode detects your LLM provider from the model name — no endpoint URL or API key configuration needed. Your agent's existing auth is passed through.

## Agent Setup

### HTTP Proxy

Point your agent to Crust:

| Agent | Configuration |
|-------|---------------|
| **[Claude Code](https://github.com/anthropics/claude-code)** | `ANTHROPIC_BASE_URL=http://localhost:9090` |
| **[Codex CLI](https://github.com/openai/codex)** | `OPENAI_BASE_URL=http://localhost:9090/v1` |
| **[Cursor](https://cursor.com)** | Settings → Models → Override OpenAI Base URL → `http://localhost:9090/v1` |
| **[Cline](https://github.com/cline/cline)** | Settings → API Configuration → Base URL → `http://localhost:9090/v1` |
| **[Windsurf](https://windsurf.com)** | Settings → AI → Provider Base URL → `http://localhost:9090/v1` |
| **[JetBrains AI](https://www.jetbrains.com/ai/)** | Settings → AI Assistant → Providers & API keys → Base URL → `http://localhost:9090/v1` |
| **[C