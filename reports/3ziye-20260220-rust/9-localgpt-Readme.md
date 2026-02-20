
# <img src="https://localgpt.app/logo/localgpt-icon-app.png" width="50" height="50" alt="LocalGPT" /> LocalGPT

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/localgpt-app/localgpt#license)
[![Crates.io](https://img.shields.io/crates/v/localgpt.svg)](https://crates.io/crates/localgpt)
[![Downloads](https://img.shields.io/crates/d/localgpt.svg)](https://crates.io/crates/localgpt)
[![Docs](https://docs.rs/localgpt/badge.svg)](https://docs.rs/localgpt/latest/localgpt)
[![CI](https://github.com/localgpt-app/localgpt/workflows/CI/badge.svg)](https://github.com/localgpt-app/localgpt/actions)
[![Discord](https://img.shields.io/discord/691052431525675048.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://discord.gg/yMQ8tfxG)

A local device focused AI assistant built in Rust — persistent memory, autonomous tasks. Inspired by and compatible with OpenClaw.

`cargo install localgpt`

## Why LocalGPT?

- **Single binary** — no Node.js, Docker, or Python required
- **Local device focused** — runs entirely on your machine, your memory data stays yours
- **Persistent memory** — markdown-based knowledge store with full-text and semantic search
- **Hybrid web search** — native provider search passthrough plus client-side fallback providers
- **Autonomous heartbeat** — delegate tasks and let it work in the background
- **Multiple interfaces** — CLI, web UI, desktop GUI, Telegram bot
- **Defense-in-depth security** — signed policy files, kernel-enforced sandbox, prompt injection defenses
- **Multiple LLM providers** — Anthropic (Claude), OpenAI, xAI (Grok), Ollama, GLM (Z.AI), OAuth subscriptions (Claude Pro/Max, Gemini)
- **OpenClaw compatible** — works with SOUL, MEMORY, HEARTBEAT markdown files and skills format

## Install

```bash
# From crates.io (includes desktop GUI)
cargo install localgpt

# Headless (no desktop GUI — for servers, Docker, CI)
cargo install localgpt --no-default-features

# From source checkout
cargo install --path crates/cli
```

## Quick Start

```bash
# Initialize configuration
localgpt config init

# Start interactive chat
localgpt chat

# Ask a single question
localgpt ask "What is the meaning of life?"

# Inspect resolved config/data/state/cache paths
localgpt paths

# Run as a daemon with heartbeat, HTTP API and web ui
localgpt daemon start
```

## How It Works

LocalGPT uses XDG-compliant directories (or platform equivalents) for config/data/state/cache. Run `localgpt paths` to see your resolved paths.

Workspace memory layout:

```
<data_dir>/workspace/
├── MEMORY.md            # Long-term knowledge (auto-loaded each session)
├── HEARTBEAT.md         # Autonomous task queue
├── SOUL.md              # Personality and behavioral guidance
└── knowledge/           # Structured knowledge bank (optional)
    ├── finance/
    ├── legal/
    └── tech/
```

Files are indexed with SQLite FTS5 for fast keyword search, and sqlite-vec for semantic search with local embeddings.

## Configuration

Stored at `<config_dir>/config.toml` (run `localgpt config path` or `localgpt paths`):

```toml
[agent]
default_model = "claude-cli/opus"

[providers.anthropic]
api_key = "${ANTHROPIC_API_KEY}"

[heartbeat]
enabled = true
interval = "30m"
active_hours = { start = "09:00", end = "22:00" }

[memory]
workspace = "~/.local/share/localgpt/workspace" # optional override

# Optional: Telegram bot
[telegram]
enabled = true
api_token = "${TELEGRAM_BOT_TOKEN}"
```

### Using a local OpenAI-compatible server (LM Studio, llamafile, etc.)

If you run a local server that speaks the OpenAI API (e.g., LM Studio, llamafile, vLLM), point LocalGPT at it and pick an `openai/*` model ID so it does **not** try to spawn the `claude` CLI:

1. Start your server (LM Studio default port: `1234`; llamafile default: `8080`) and note its model name.
2. Edit your config file (`localgpt config path`):
   ```toml
   [agent]
   default_model = "openai/<your-model-name>"

   [providers.openai]
   # Many local servers accept a dummy key
   api_key = "not-needed"
   base_url = "http://127.0.0.1:8080/v1" # or http://127.0.0.1:1234/v1 for LM Studio
   ```
3. Run `localgpt chat` (or `localgpt daemon start`) and requests will go to your local server.

Tip: If you see `Failed to spawn Claude CLI`, change `agent.default_model` away from `claude-cli/*` or install the `claude` CLI.

### Web Search

Configure web search providers under `[tools.web_search]` and validate with:

```bash
localgpt search test "rust async runtime"
localgpt search stats
```

Full setup guide: [`docs/web-search.md`](docs/web-search.md)

### OAuth Subscription Plans

Use Claude Pro/Max or Google Gemini subscription credentials via OAuth instead of pay-per-request API keys:

```toml
# Claude Pro/Max OAuth (preferred over api_key when configured)
[providers.anthropic_oauth]
access_token = "${ANTHROPIC_OAUTH_TOKEN}"
refresh_token = "${ANTHROPIC_OAUTH_REFRESH_TOKEN}"

# Google Gemini subscription OAuth
[providers