# opencli-rs
**[English](README.md) | [中文](README.zh.md) | [日本語](README.ja.md)**

<p align="center">
  <img src="title_screen.png" alt="opencli-rs" width="800" />
</p>

<p align="center">
  <a href="https://autocli.ai"><b>https://autocli.ai</b></a> — AI-powered adapter marketplace & cloud API
</p>

---

Blazing fast, memory-safe command-line tool — **Fetch information from any website with a single command**. Covers Twitter/X, Reddit, YouTube, HackerNews, Bilibili, Zhihu, Xiaohongshu, and [55+ sites](#built-in-commands), with support for controlling Electron desktop apps, integrating local CLI tools (`gh`, `docker`, `kubectl`), powered by browser session reuse and AI-native discovery capabilities.

A **complete rewrite in pure Rust** based on [OpenCLI](https://github.com/jackwener/opencli) (TypeScript). Feature-equivalent, **up to 12x faster**, **10x less memory**, **single 4.7MB binary**, zero runtime dependencies.

**The perfect companion for OpenClaw/Agent** — Give your AI Agent the ability to reach information across the entire web, fetching real-time data from 55+ sites with a single command.
**Built for AI Agents:** Configure `opencli-rs list` in `AGENT.md` or `.cursorrules`, and AI can automatically discover all available tools. Register your local CLI (`opencli-rs register mycli`), and AI can seamlessly invoke all your tools.

**CLI-fy All Desktop Apps!** Turn any Electron app into a command-line tool — Cursor, ChatGPT, Notion, Discord, and more. Reorganize, script, and extend desktop apps; AI can natively control itself — endless possibilities.

## 🚀 Performance Comparison

| Metric | 🦀 opencli-rs (Rust) | 📦 opencli (Node.js) | Improvement |
|------|:-----------------:|:-----------------:|:----:|
| 💾 **Memory Usage (Public Commands)** | 15 MB | 99 MB | **6.6x** |
| 💾 **Memory Usage (Browser Commands)** | 9 MB | 95 MB | **10.6x** |
| 📏 **Binary Size** | 4.7 MB | ~50 MB (node_modules) | **10x** |
| 🔗 **Runtime Dependencies** | None | Node.js 20+ | **Zero deps** |
| ✅ **Test Pass Rate** | 103/122 (84%) | 104/122 (85%) | Near parity |

**⚡ Real-world Command Timing Comparison:**

| Command | 🦀 opencli-rs | 📦 opencli | Speedup |
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
curl -fsSL https://raw.githubusercontent.com/nashsu/opencli-rs/main/scripts/install.sh | sh
```

Automatically detects your system and architecture, downloads the corresponding binary, and installs to `/usr/local/bin/`.

### Windows (PowerShell)

```powershell
Invoke-WebRequest -Uri "https://github.com/nashsu/opencli-rs/releases/latest/download/opencli-rs-x86_64-pc-windows-msvc.zip" -OutFile opencli-rs.zip
Expand-Archive opencli-rs.zip -DestinationPath .
Move-Item opencli-rs.exe "$env:LOCALAPPDATA\Microsoft\WindowsApps\"
```


### Manual Download (Simplest)

Download the file for your platform from [GitHub Releases](https://github.com/nashsu/opencli-rs/releases/latest):

| Platform | File |
|------|------|
| macOS (Apple Silicon) | `opencli-rs-aarch64-apple-darwin.tar.gz` |
| macOS (Intel) | `opencli-rs-x86_64-apple-darwin.tar.gz` |
| Linux (x86_64) | `opencli-rs-x86_64-unknown-linux-musl.tar.gz` |
| Linux (ARM64) | `opencli-rs-aarch64-unknown-linux-musl.tar.gz` |
| Windows (x64) | `opencli-rs-x86_64-pc-windows-msvc.zip` |

After extracting, place `opencli-rs` (or `opencli-rs.exe` on Windows) in your system PATH.

### Build from Source

```bash
git clone https://github.com/nashsu/opencli-rs.git
cd opencli-rs
cargo build --release
cp target/release/opencli-rs /usr/l