[![Rust](https://img.shields.io/badge/rust-%23000000.svg?style=for-the-badge&logo=rust&logoColor=white)](https://www.rust-lang.org)
[![Rust Edition](https://img.shields.io/badge/rust-2024_edition-orange.svg)](https://www.rust-lang.org/)
[![Ratatui](https://img.shields.io/badge/ratatui-%23000000.svg?style=for-the-badge&logo=rust&logoColor=white)](https://ratatui.rs)
[![Docker](https://img.shields.io/badge/docker-%23000000.svg?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
[![CI](https://github.com/adolfousier/opencrabs/actions/workflows/ci.yml/badge.svg)](https://github.com/adolfousier/opencrabs/actions/workflows/ci.yml)
[![GitHub Stars](https://img.shields.io/github/stars/adolfousier/opencrabs?style=social)](https://github.com/adolfousier/opencrabs)

# 🦀 OpenCrabs

**The autonomous AI agent. Single Rust binary. Every channel.**

> Autonomous multi-channel AI agent built in Rust. Inspired by [Open Claw](https://github.com/openclaw/openclaw).

```
    ___                    ___           _
   / _ \ _ __  ___ _ _    / __|_ _ __ _| |__  ___
  | (_) | '_ \/ -_) ' \  | (__| '_/ _` | '_ \(_-<
   \___/| .__/\___|_||_|  \___|_| \__,_|_.__//__/
        |_|

 🦀 The autonomous AI agent. Single Rust binary. Every channel.

```

**Author:** [Adolfo Usier](https://github.com/adolfousier)

⭐ Star us on [GitHub](https://github.com/adolfousier/opencrabs) if you like what you see!

---

## Why OpenCrabs?

OpenCrabs runs as a **single binary on your terminal** — no server, no gateway, no infrastructure. It makes direct HTTPS calls to LLM providers from your machine. Nothing else leaves your computer.

### OpenCrabs vs Node.js Agent Frameworks

| | **OpenCrabs** (Rust) | **Node.js Frameworks** (e.g. Open Claw) |
|---|---|---|
| **Binary size** | **17–22 MB** single binary, zero dependencies | **1 GB+** `node_modules` with hundreds of transitive packages |
| **Runtime** | None — runs natively | Requires Node.js runtime + npm install |
| **Attack surface** | Zero network listeners. Outbound HTTPS only | Server infrastructure: open ports, auth layers, middleware |
| **API key security** | Keys on your machine only. `zeroize` clears them from RAM on drop, `[REDACTED]` in all debug output | Keys in env vars or config. GC doesn't guarantee memory clearing. Heap dumps can leak secrets |
| **Data residency** | 100% local — SQLite DB, embeddings, brain files, all in `~/.opencrabs/` | Server-side storage, potential multi-tenant data, network transit |
| **Supply chain** | Single compiled binary. Rust's type system prevents buffer overflows, use-after-free, data races at compile time | npm ecosystem: typosquatting, dependency confusion, prototype pollution |
| **Memory safety** | Compile-time guarantees — no GC, no null pointers, no data races | GC-managed, prototype pollution, type coercion bugs |
| **Concurrency** | tokio async + Rust ownership = zero data races guaranteed | Single-threaded event loop, worker threads share memory unsafely |
| **Native TTS/STT** | Built-in local speech-to-text (whisper.cpp) and text-to-speech — ~130 MB total stack, fully offline | No native voice. Requires external APIs (Google, AWS, Azure) or heavy Python dependencies (PyTorch, ~5 GB+) |
| **Telemetry** | Zero. No analytics, no tracking, no remote logging | Server infra typically includes monitoring, logging pipelines, APM |

### What stays local (never leaves your machine)

- All chat sessions and messages (SQLite)
- Tool executions (bash, file reads/writes, git)
- Memory and embeddings (local vector search)
- Voice transcription in local STT mode (whisper.cpp, on-device)
- Brain files, config, API keys

### What goes out (only when you use it)

- Your messages to the LLM provider API (Anthropic, OpenAI, GitHub Copilot, etc.)
- Web search queries (optional tool)
- GitHub API via `gh` CLI (optional tool)

---

## Table of Contents

- [Screenshots](#-screenshots)
- [Why OpenCrabs?](#why-opencrabs)
- [Core Features](#-core-features)
- [Supported AI Providers](#-supported-ai-providers)
- [Agent-to-Agent (A2A) Protocol](#-agent-to-agent-a2a-protocol)
- [Quick Start](#-quick-start)
- [Onboarding Wizard](#-onboarding-wizard)
- [API Keys (keys.toml)](#-api-keys-keystoml)
- [Configuration (config.toml)](#-configuration-configtoml)
- [Commands (commands.toml)](#-commands-commandstoml)
- [Using Local LLMs](#-using-local-llms)
- [Configuration](#-configuration)
- [Tool System](#-tool-system)
- [Keyboard Shortcuts](#-keyboard-shortcuts)
- [Debug and Logging](#-debug-and-logging)
- [Cron Jobs & Heartbeats](#-cron-jobs--heartbeats)
- [Architecture](#-architecture)
- [Project Structure](#-project-structure)
- [Development](#-development)
- [Platform Notes](#-platform-notes)
- [Troubleshooting](#-troubleshooting)
- [Companion Tools](#-companion-tools)
- [Disclaimers](#-disclaimers)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)

---

## 📸 Screenshots

https://github.com/user-attachments/assets/7f45c