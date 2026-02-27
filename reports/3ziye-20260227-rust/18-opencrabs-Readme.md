[![Rust](https://img.shields.io/badge/rust-%23000000.svg?style=for-the-badge&logo=rust&logoColor=white)](https://www.rust-lang.org)
[![Rust Edition](https://img.shields.io/badge/rust-2024_edition-orange.svg)](https://www.rust-lang.org/)
[![Ratatui](https://img.shields.io/badge/ratatui-%23000000.svg?style=for-the-badge&logo=rust&logoColor=white)](https://ratatui.rs)
[![Docker](https://img.shields.io/badge/docker-%23000000.svg?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE.md)
[![CI](https://github.com/adolfousier/opencrabs/actions/workflows/ci.yml/badge.svg)](https://github.com/adolfousier/opencrabs/actions/workflows/ci.yml)
[![GitHub Stars](https://img.shields.io/github/stars/adolfousier/opencrabs?style=social)](https://github.com/adolfousier/opencrabs)

# 🦀 OpenCrabs

**Rust-based open-claw inspired orchestration layer for software development.**

> A terminal-native AI orchestration agent written in Rust with Ratatui. Inspired by [Open Claw](https://github.com/openclaw/openclaw).

```
    ___                    ___           _
   / _ \ _ __  ___ _ _    / __|_ _ __ _| |__  ___
  | (_) | '_ \/ -_) ' \  | (__| '_/ _` | '_ \(_-<
   \___/| .__/\___|_||_|  \___|_| \__,_|_.__//__/
        |_|

 🦀 Shell Yeah! AI Orchestration at Rust Speed.

```

**Author:** [Adolfo Usier](https://github.com/adolfousier)

⭐ Star us on [GitHub](https://github.com/adolfousier/opencrabs) if you like what you see!

---

## Table of Contents

- [Screenshots](#-screenshots)
- [Core Features](#-core-features)
- [Supported AI Providers](#-supported-ai-providers)
- [Agent-to-Agent (A2A) Protocol](#-agent-to-agent-a2a-protocol)
- [Quick Start](#-quick-start)
- [Onboarding Wizard](#-onboarding-wizard)
- [API Keys (keys.toml)](#-api-keys-keystoml)
- [Using Local LLMs](#-using-local-llms)
- [Configuration](#-configuration)
- [Tool System](#-tool-system)
- [Plan Mode](#-plan-mode)
- [Keyboard Shortcuts](#-keyboard-shortcuts)
- [Debug and Logging](#-debug-and-logging)
- [Architecture](#-architecture)
- [Project Structure](#-project-structure)
- [Development](#-development)
- [Platform Notes](#-platform-notes)
- [Troubleshooting](#-troubleshooting)
- [Disclaimers](#-disclaimers)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)

---

## 📸 Screenshots

[![Demo](src/screenshots/opencrabs-demo.gif)](https://github.com/user-attachments/assets/dfc44f70-52e1-44f7-8aef-b57faf453761)

![Splash](src/screenshots/splash.png)

![Onboarding](src/screenshots/onboard1.png)

![Provider Auth](src/screenshots/onboard2.png)

![Workspace](src/screenshots/onboard3.png)

![Home Base](src/screenshots/onboard4.png)

![Chat](src/screenshots/opencrabs-ui.png)

![Session Usage](src/screenshots/session-usage.png)

![Rebuild Complete](src/screenshots/rebuild-dialog.png)

---

## 🎯 Core Features

### AI & Providers
| Feature | Description |
|---------|-------------|
| **Multi-Provider** | Anthropic Claude, OpenAI, OpenRouter (400+ models), MiniMax, and any OpenAI-compatible API (Ollama, LM Studio, LocalAI). Model lists fetched live from provider APIs — new models available instantly |
| **Real-time Streaming** | Character-by-character response streaming with animated spinner showing model name and live text |
| **Local LLM Support** | Run with LM Studio, Ollama, or any OpenAI-compatible endpoint — 100% private, zero-cost |
| **Cost Tracking** | Per-message token count and cost displayed in header; `/usage` shows all-time breakdown grouped by model with real costs + estimates for historical sessions |
| **Context Awareness** | Live context usage indicator showing actual token counts (e.g. `ctx: 45K/200K (23%)`); auto-compaction at 70% with tool overhead budgeting; accurate tiktoken-based counting calibrated against API actuals |
| **3-Tier Memory** | (1) **Brain MEMORY.md** — user-curated durable memory loaded every turn, (2) **Daily Logs** — auto-compaction summaries at `~/.opencrabs/memory/YYYY-MM-DD.md`, (3) **Hybrid Memory Search** — FTS5 keyword search + local vector embeddings (embeddinggemma-300M, 768-dim) combined via Reciprocal Rank Fusion. Runs entirely local — no API key, no cost, works offline |
| **Dynamic Brain System** | System brain assembled from workspace MD files (SOUL, IDENTITY, USER, AGENTS, TOOLS, MEMORY) — all editable live between turns |

### Multimodal Input
| Feature | Description |
|---------|-------------|
| **Image Attachments** | Paste image paths or URLs into the input — auto-detected and attached as vision content blocks for multimodal models |
| **PDF Support** | Attach PDF files by path — native Anthropic PDF support; for other providers, text is extracted locally via `pdf-extract` |
| **Document Parsing** | Built-in `parse_document` tool extracts text from PDF, DOCX, HTML, TXT, MD, JSON, XML |
| **Voice (STT)** | Telegram voice notes transcribed via Groq Whisper (`whisper-large-v3-turbo`) and processed 