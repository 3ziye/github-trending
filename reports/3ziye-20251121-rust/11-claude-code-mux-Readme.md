# Claude Code Mux

[![CI](https://github.com/9j/claude-code-mux/workflows/CI/badge.svg)](https://github.com/9j/claude-code-mux/actions)
[![Latest Release](https://img.shields.io/github/v/release/9j/claude-code-mux)](https://github.com/9j/claude-code-mux/releases/latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Rust](https://img.shields.io/badge/rust-1.70%2B-orange.svg)](https://www.rust-lang.org/)
[![GitHub Stars](https://img.shields.io/github/stars/9j/claude-code-mux?style=social)](https://github.com/9j/claude-code-mux)
[![GitHub Forks](https://img.shields.io/github/forks/9j/claude-code-mux?style=social)](https://github.com/9j/claude-code-mux/fork)

OpenRouter met Claude Code Router. They had a baby.

---

Now your coding assistant can use GLM 4.6 for one task, Kimi K2 Thinking for another, and Minimax M2 for a third. All in the same session. When your primary provider goes down, it falls back to your backup automatically.

⚡️ **Multi-model intelligence with provider resilience**

A lightweight, Rust-powered proxy that provides intelligent model routing, provider failover, streaming support, and full Anthropic API compatibility for Claude Code.

```
Claude Code → Claude Code Mux → Multiple AI Providers
              (Anthropic API)    (OpenAI/Anthropic APIs + Streaming)
```

## Table of Contents

- [Key Features](#key-features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Screenshots](#screenshots)
- [Usage Guide](#usage-guide)
- [Routing Logic](#routing-logic)
- [Configuration Examples](#configuration-examples)
- [Supported Providers](#supported-providers)
- [Advanced Features](#advanced-features)
- [CLI Usage](#cli-usage)
- [Troubleshooting](#troubleshooting)
- [FAQ](#faq)
- [Performance](#performance)
- [Why Choose Claude Code Mux?](#why-choose-claude-code-mux)
- [Documentation](#documentation)
- [Changelog](#changelog)
- [Contributing](#contributing)
- [License](#license)

## Key Features

### 🎯 Core Features
- ✨ **Modern Admin UI** - Beautiful web interface with auto-save and URL-based navigation
- 🔐 **OAuth 2.0 Support** - FREE access for Claude Pro/Max, ChatGPT Plus/Pro, and Google AI Pro/Ultra
- 🧠 **Intelligent Routing** - Auto-route by task type (websearch, reasoning, background, default)
- 🔄 **Provider Failover** - Automatic fallback to backup providers with priority-based routing
- 🌊 **Streaming Support** - Full Server-Sent Events (SSE) streaming for real-time responses
- 🌐 **Multi-Provider Support** - 18+ providers including OpenAI, Anthropic, Google Gemini/Vertex AI, Groq, ZenMux, etc.
- ⚡️ **High Performance** - ~5MB RAM, <1ms routing overhead (Rust powered)
- 🎯 **Unified API** - Full Anthropic Messages API compatibility

### 🚀 Advanced Features
- 🔀 **Auto-mapping** - Regex-based model name transformation before routing (e.g., transform all `claude-*` to default model)
- 🎯 **Background Detection** - Configurable regex patterns for background task detection
- 🤖 **Multi-Agent Support** - Dynamic model switching via `CCM-SUBAGENT-MODEL` tags
- 📊 **Live Testing** - Built-in test interface to verify routing and responses
- ⚙️ **Centralized Settings** - Dedicated Settings tab for regex pattern management

## Screenshots

<details>
<summary>📸 Click to view screenshots (5 images)</summary>

### Overview Dashboard
![Dashboard showing router configuration, providers, and models summary](docs/images/dashboard.png)
*Main dashboard with router configuration and provider management*

### Provider Management
![Provider management interface with add/edit capabilities](docs/images/providers.png)
*Add and manage multiple AI providers with automatic format translation*

### Model Mappings with Fallback
![Model configuration with priority-based fallback routing](docs/images/models.png)
*Configure models with priority-based fallback routing*

### Router Configuration
![Router configuration interface for intelligent routing rules](docs/images/routing.png)
*Set up intelligent routing rules for different task types*

### Live Testing Interface
![Testing interface for verifying configuration with real API calls](docs/images/testing.png)
*Test your configuration with live API requests and responses*

</details>

## Supported Providers

**18+ AI providers with automatic format translation, streaming, and failover:**

- **Anthropic-compatible**: Anthropic (API Key/OAuth), ZenMux, z.ai, Minimax, Kimi
- **OpenAI-compatible**: OpenAI, OpenRouter, Groq, Together, Fireworks, Deepinfra, Cerebras, Moonshot, Nebius, NovitaAI, Baseten
- **Google AI**: Gemini (OAuth/API Key), Vertex AI (GCP ADC)

<details>
<summary>📋 View full provider details</summary>

### Anthropic-Compatible (Native Format)
- **Anthropic** - Official Claude API provider (supports both API Key and OAuth)
- **Anthropic (OAuth)** - 🆓 **FREE for Claude Pro/Max subscribers** via OAuth 2.0
- **ZenMux** - Unified API gateway (Sunnyvale, CA)
- **z.ai** - China-based, GLM models
