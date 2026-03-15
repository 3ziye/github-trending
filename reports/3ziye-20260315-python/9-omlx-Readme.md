<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/images/icon-rounded-dark.svg" width="140">
    <source media="(prefers-color-scheme: light)" srcset="docs/images/icon-rounded-light.svg" width="140">
    <img alt="oMLX" src="docs/images/icon-rounded-light.svg" width="140">
  </picture>
</p>

<h1 align="center">oMLX</h1>
<p align="center"><b>LLM inference, optimized for your Mac</b><br>Continuous batching and tiered KV caching, managed directly from your menu bar.</p>

<p align="center">
  <img src="https://img.shields.io/badge/license-Apache%202.0-blue" alt="License">
  <img src="https://img.shields.io/badge/python-3.10+-green" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/platform-Apple%20Silicon-black?logo=apple" alt="Apple Silicon">
  <a href="https://buymeacoffee.com/jundot"><img src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?logo=buy-me-a-coffee&logoColor=black" alt="Buy Me a Coffee"></a>
</p>

<p align="center">
  <a href="mailto:junkim.dot@gmail.com">junkim.dot@gmail.com</a> · <a href="https://omlx.ai/me">https://omlx.ai/me</a>
</p>

<p align="center">
  <a href="#install">Install</a> ·
  <a href="#quickstart">Quickstart</a> ·
  <a href="#features">Features</a> ·
  <a href="#models">Models</a> ·
  <a href="#cli-configuration">CLI Configuration</a> ·
  <a href="https://omlx.ai/benchmarks">Benchmarks</a> ·
  <a href="https://omlx.ai">oMLX.ai</a>
</p>

<p align="center">
  <b>English</b> ·
  <a href="README.zh.md">中文</a> ·
  <a href="README.ko.md">한국어</a> ·
  <a href="README.ja.md">日本語</a>
</p>

---

<p align="center">
  <img src="docs/images/omlx_dashboard.png" alt="oMLX Admin Dashboard" width="800">
</p>

> *Every LLM server I tried made me choose between convenience and control. I wanted to pin everyday models in memory, auto-swap heavier ones on demand, set context limits - and manage it all from a menu bar.*
>
> *oMLX persists KV cache across a hot in-memory tier and cold SSD tier - even when context changes mid-conversation, all past context stays cached and reusable across requests, making local LLMs practical for real coding work with tools like Claude Code. That's why I built it.*

## Install

### macOS App

Download the `.dmg` from [Releases](https://github.com/jundot/omlx/releases), drag to Applications, done. The app includes in-app auto-update, so future upgrades are just one click.

### Homebrew

```bash
brew tap jundot/omlx https://github.com/jundot/omlx
brew install omlx

# Upgrade to the latest version
brew update && brew upgrade omlx

# Run as a background service (auto-restarts on crash)
brew services start omlx

# Optional: MCP (Model Context Protocol) support
/opt/homebrew/opt/omlx/libexec/bin/pip install mcp
```

### From Source

```bash
git clone https://github.com/jundot/omlx.git
cd omlx
pip install -e .          # Core only
pip install -e ".[mcp]"   # With MCP (Model Context Protocol) support
```

Requires macOS 15.0+ (Sequoia), Python 3.10+, and Apple Silicon (M1/M2/M3/M4).

## Quickstart

### macOS App

Launch oMLX from your Applications folder. The Welcome screen guides you through three steps - model directory, server start, and first model download. That's it. To connect OpenClaw, OpenCode, or Codex, see [Integrations](#integrations).

<p align="center">
  <img src="docs/images/Screenshot 2026-02-10 at 00.36.32.png" alt="oMLX Welcome Screen" width="360">
  <img src="docs/images/Screenshot 2026-02-10 at 00.34.30.png" alt="oMLX Menubar" width="240">
</p>

### CLI

```bash
omlx serve --model-dir ~/models
```

The server discovers LLMs, VLMs, embedding models, and rerankers from subdirectories automatically. Any OpenAI-compatible client can connect to `http://localhost:8000/v1`. A built-in chat UI is also available at `http://localhost:8000/admin/chat`.

### Homebrew Service

If you installed via Homebrew, you can run oMLX as a managed background service:

```bash
brew services start omlx    # Start (auto-restarts on crash)
brew services stop omlx     # Stop
brew services restart omlx  # Restart
brew services info omlx     # Check status
```

The service runs `omlx serve` with zero-config defaults (`~/.omlx/models`, port 8000). To customize, either set environment variables (`OMLX_MODEL_DIR`, `OMLX_PORT`, etc.) or run `omlx serve --model-dir /your/path` once to persist settings to `~/.omlx/settings.json`.

Logs are written to two locations:
- **Service log**: `$(brew --prefix)/var/log/omlx.log` (stdout/stderr)
- **Server log**: `~/.omlx/logs/server.log` (structured application log)

## Features

Supports text LLMs, vision-language models (VLM), OCR models, embeddings, and rerankers on Apple Silicon.

### Admin Dashboard

Web UI at `/admin` for real-time monitoring, model management, chat, benchmark, and per-model settings. Supports English, Korean, Japanese, and Chinese. All CDN dependencies are vendored for fully offline operation.

<p align="center">
  <img src="docs/images/Screenshot 2026-02-10 at 00.4