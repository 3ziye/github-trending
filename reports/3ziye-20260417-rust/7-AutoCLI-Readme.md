# AutoCLI
> Formerly known as **opencli-rs**. Renamed to **AutoCLI** starting from v0.2.4.

**[English](README.md) | [中文](README.zh.md) | [日本語](README.ja.md)**

<p align="center">
  <img src="assets/title_screen.jpg" alt="autocli" width="800" />
</p>

<p align="center">
  <a href="https://autocli.ai"><b>https://autocli.ai</b></a> — AI-powered adapter marketplace & cloud API
</p>

---

## What's New

### v0.3.2
- **Chrome Extension Selector Tool** — Just select the core data you need, visually pick elements from any page and build precise CSS selectors to target specific content
- **AI-Powered Generation via AutoCLI.ai** — Based on your selected data, AI automatically expands and discovers related fields, generating complete scraping rules
- **Seamless Local + Cloud Sync** — Generated adapters are saved locally and synced to AutoCLI.ai, ready to use immediately

---

Blazing fast, memory-safe command-line tool — **Fetch information from any website with a single command**. Covers Twitter/X, Reddit, YouTube, HackerNews, Bilibili, Zhihu, Xiaohongshu, and [55+ sites](#built-in-commands), with support for controlling Electron desktop apps, integrating local CLI tools (`gh`, `docker`, `kubectl`), powered by browser session reuse and AI-native discovery capabilities.

A **complete rewrite in pure Rust** based on [OpenCLI](https://github.com/jackwener/opencli) (TypeScript). Feature-equivalent, **up to 12x faster**, **10x less memory**, **single 4.7MB binary**, zero runtime dependencies.

**The perfect companion for OpenClaw/Agent** — Give your AI Agent the ability to reach information across the entire web, fetching real-time data from 55+ sites with a single command.
**Built for AI Agents:** Configure `autocli list` in `AGENT.md` or `.cursorrules`, and AI can automatically discover all available tools. Register your local CLI (`autocli register mycli`), and AI can seamlessly invoke all your tools.


## 🚀 Performance Comparison

| Metric | 🦀 autocli (Rust) | 📦 opencli (Node.js) | Improvement |
|------|:-----------------:|:-----------------:|:----:|
| 💾 **Memory Usage (Public Commands)** | 15 MB | 99 MB | **6.6x** |
| 💾 **Memory Usage (Browser Commands)** | 9 MB | 95 MB | **10.6x** |
| 📏 **Binary Size** | 4.7 MB | ~50 MB (node_modules) | **10x** |
| 🔗 **Runtime Dependencies** | None | Node.js 20+ | **Zero deps** |
| ✅ **Test Pass Rate** | 103/122 (84%) | 104/122 (85%) | Near parity |

**⚡ Real-world Command Timing Comparison:**

| Command | 🦀 autocli | 📦 opencli | Speedup |
|------|:----------:|:-------:|:------:|
| `bilibili hot` | **1.66s** | 20.1s | 🔥 **12x** |
| `zhihu hot` | **1.77s** | 20.5s | 🔥 **11.6x** |
| `xueqiu search 茅台` | **1.82s** | 9.2s | ⚡ **5x** |
| `xiaohongshu search` | **5.1s** | 14s | ⚡ **2.7x** |

> Based on automated testing of 122 commands (55 sites), macOS Apple Silicon environment.

## Features

- **55 sites, 333 commands** — Covers Bilibili, Twitter, Reddit, Zhihu, Xiaohongshu, YouTube, Hacker News, and more
- **Browser session reuse** — Reuse logged-in sessions via Chrome extension, no need to manage tokens
- **Declarative YAML Pipeline** — Describe data scraping workflows in YAML, add new adapters with zero code
- **AI-native discovery** — `explore` analyzes website APIs, `generate` auto-creates adapters with one command, `cascade` probes authentication strategies
- **AI-powered generation** — `generate --ai` uses LLM to analyze any website and create working adapters automatically, with cloud sharing via [autocli.ai](https://autocli.ai)
- **Download media & articles** — Download videos (via yt-dlp), articles as Markdown with images localized
- **External CLI passthrough** — Integrate GitHub CLI, Docker, Kubernetes, and other tools
- **Multi-format output** — table, JSON, YAML, CSV, Markdown
- **Single binary** — Compiles to a 4MB static binary with zero runtime dependencies

## Installation
> **Just one file, download and use.** No Node.js, Python, or any runtime needed — just put it in your PATH and go.

### One-line Install Script (macOS / Linux)

```bash
curl -fsSL https://raw.githubusercontent.com/nashsu/autocli/main/scripts/install.sh | sh
```

Automatically detects your system and architecture, downloads the corresponding binary, and installs to `/usr/local/bin/`.

### Windows (PowerShell)

```powershell
Invoke-WebRequest -Uri "https://github.com/nashsu/autocli/releases/latest/download/autocli-x86_64-pc-windows-msvc.zip" -OutFile autocli.zip
Expand-Archive autocli.zip -DestinationPath .
Move-Item autocli.exe "$env:LOCALAPPDATA\Microsoft\WindowsApps\"
```


### Manual Download (Simplest)

Download the file for your platform from [GitHub Releases](https://github.com/nashsu/autocli/releases/latest):

| Platform | File |
|------|------|
| macOS (Apple Silicon) | `autocli-aarch64-apple-darwin.tar.gz` |
| macOS (Intel) | `autocli-x86_64-apple-darwin.tar.gz` |
| Linux (x86_64) | `autocli-x86_64-unknown-linux-musl.tar.gz` |
| Linux (ARM64) | `autocli-aarch64-unknown-linux-musl.tar.gz` |
