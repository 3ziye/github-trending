<div align="center">
  <img src="clawlet.png" alt="clawlet" width="500">
  <h1>Clawlet</h1>
  <h3>Ultra-Lightweight&Efficient Personal AI Assistant</h3>
  <p>Single Binary · No CGO · No Runtime · No Dependencies</p>
</div>

**Clawlet** is a lightweight and efficient personal AI agent with built-in hybrid semantic memory search — and it still ships as a single, dependency-free binary.
Powered by bundled SQLite + sqlite-vec. No CGO, no runtime, no dependencies. Drop it on any machine and memory search just works.  

This project is inspired by **OpenClaw** and **nanobot**.

## Install

Download from [GitHub Releases](https://github.com/mosaxiv/clawlet/releases/latest).

macOS (Apple Silicon):
```bash
curl -L https://github.com/mosaxiv/clawlet/releases/latest/download/clawlet_Darwin_arm64.tar.gz | tar xz
mv clawlet ~/.local/bin/
```

## Quick Start

```bash
# Initialize
clawlet onboard \
  --openrouter-api-key "sk-or-..." \
  --model "openrouter/anthropic/claude-sonnet-4.5"

# Check effective configuration
clawlet status

# Chat
clawlet agent -m "What is 2+2?"
```

## Configuration (`~/.clawlet/config.json`)

Config file: `~/.clawlet/config.json`

### Supported providers

clawlet currently supports these LLM providers:

- **OpenAI** (`openai/<model>`, API key: `env.OPENAI_API_KEY`)
- **OpenRouter** (`openrouter/<provider>/<model>`, API key: `env.OPENROUTER_API_KEY`)
- **Anthropic** (`anthropic/<model>`, API key: `env.ANTHROPIC_API_KEY`)
- **Gemini** (`gemini/<model>`, API key: `env.GEMINI_API_KEY` or `env.GOOGLE_API_KEY`)
- **Local (Ollama / vLLM / OpenAI-compatible local endpoint)** (`ollama/<model>` or `local/<model>`, default base URL: `http://localhost:11434/v1`, API key optional)

Minimal config (OpenRouter):

```json
{
  "env": { "OPENROUTER_API_KEY": "sk-or-..." },
  "agents": { "defaults": { "model": "openrouter/anthropic/claude-sonnet-4-5" } }
}
```

Agent generation defaults are configurable:

```json
{
  "agents": {
    "defaults": {
      "model": "openrouter/anthropic/claude-sonnet-4-5",
      "maxTokens": 8192,
      "temperature": 0.7
    }
  }
}
```

Minimal config (Local via Ollama):

```json
{
  "agents": { "defaults": { "model": "ollama/qwen2.5:14b" } }
}
```

Minimal config (Local via vLLM using the same `ollama/` route):

```json
{
  "agents": { "defaults": { "model": "ollama/meta-llama/Llama-3.1-8B-Instruct" } },
  "llm": { "baseURL": "http://localhost:8000/v1" }
}
```

clawlet will fill in sensible defaults for missing sections (tools, gateway, cron, heartbeat, channels).

### Option: Memory search setup

To enable semantic memory search, add `memorySearch` to the agent defaults:

```json
{
  "env": {
    "OPENAI_API_KEY": "sk-..."
  },
  "agents": {
    "defaults": {
      "memorySearch": {
        "enabled": true,
        "provider": "openai",
        "model": "text-embedding-3-small"
      }
    }
  }
}
```

When enabled:
- The agent gains `memory_search` and `memory_get` tools for retrieving past context.
- clawlet indexes `MEMORY.md`, `memory.md`, and `memory/**/*.md` for retrieval.
- The index DB is created at `{workspace}/.memory/index.sqlite`.

When disabled (default):
- `memorySearch.enabled` defaults to `false`; the search tools are not exposed to the model.
- Memory files (`memory/MEMORY.md`, `memory/YYYY-MM-DD.md`) are still injected into context as usual.
- Normal chat behavior is otherwise unchanged.


### Safety defaults

clawlet is conservative by default:

- `tools.restrictToWorkspace` defaults to `true` (tools can only access files inside the workspace directory)

## Chat Apps

Chat app integrations are configured under `channels` (examples below).

<details>
<summary><b>Telegram</b></summary>

Uses **Telegram Bot API long polling** (`getUpdates`) so no public webhook endpoint is required.

1. Create a bot with `@BotFather` and copy the bot token.
2. (Optional but recommended) Restrict access with `allowFrom`.
   - Telegram numeric user ID works best.
   - Username is also supported (without `@`).

Example config (merge into `~/.clawlet/config.json`):

```json
{
  "channels": {
    "telegram": {
      "enabled": true,
      "token": "123456:ABCDEF...",
      "allowFrom": ["123456789"]
    }
  }
}
```

Then run:

```bash
clawlet gateway
```

</details>

<details>
<summary><b>WhatsApp</b></summary>

Uses **WhatsApp Web Multi-Device**. No Meta webhook/public endpoint is required.

1. Enable channel and (recommended) set `allowFrom`.
2. Run login once:
   - `clawlet channels login --channel whatsapp`
   - Scan the QR shown in terminal from WhatsApp `Linked devices`.
3. Start normal runtime with `clawlet gateway`.

Example config (merge into `~/.clawlet/config.json`):

```json
{
  "channels": {
    "whatsapp": {
      "enabled": true,
      "allowFrom": ["15551234567"]
    }
  }
}
```

Then run:

```bash
# one-time login (required before gateway)
clawlet channels login --channel whatsapp

# normal runtime
clawlet gateway
```

Notes:
- Send retries are applied for transient/r