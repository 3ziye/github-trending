<p align="center">
  <img src="logo.png" alt="Picobot" width="250" height="150">
  <h1 align="center">Picobot</h1>
  <p align="center"><strong>The AI agent that runs anywhere — even on a $5 VPS.</strong></p>
  <p align="center">
    <img src="https://img.shields.io/badge/binary-~9MB-brightgreen" alt="Binary Size">
    <img src="https://img.shields.io/badge/docker-~29MB-blue" alt="Docker Size">
    <img src="https://img.shields.io/badge/built_with-Go-00ADD8?logo=go" alt="Go">
    <img src="https://img.shields.io/badge/RAM-~10MB-orange" alt="Memory Usage">
    <img src="https://img.shields.io/badge/license-MIT-yellow" alt="License">
    <img src="https://github.com/louisho5/picobot/actions/workflows/docker-publish.yml/badge.svg" alt="Workflow">
  </p>
</p>

---

Love the idea of open-source AI agents like [OpenClaw](https://github.com/openclaw/openclaw) but tired of the bloat? **Picobot** gives you the same power — persistent memory, tool calling, skills, Telegram and Discord integration — in a single ~9MB binary that boots in milliseconds.

No Python. No Node. No 500MB container. Just one Go binary and a config file.

## Why Picobot?

| | Picobot | Typical Agent Frameworks |
|---|---|---|
| **Binary size** | ~9MB | 200MB+ (Python + deps) |
| **Docker image** | ~29MB (Alpine) | 500MB–1GB+ |
| **Cold start** | Instant | 5–30 seconds |
| **RAM usage** | ~10MB idle | 200MB–1GB |
| **Dependencies** | Zero (single binary) | Python, pip, venv, Node… |

Picobot runs happily on a **$5/mo VPS**, a Raspberry Pi, or even an old Android phone via Termux.

## Quick Start — 30 seconds

### Docker Run

```sh
docker run -d --name picobot \
  -e OPENAI_API_KEY="your-key" \
  -e OPENAI_API_BASE="https://openrouter.ai/api/v1" \
  -e PICOBOT_MODEL="openrouter/free" \
  -e TELEGRAM_BOT_TOKEN="your-telegram-token" \
  -v ./picobot-data:/home/picobot/.picobot \
  --restart unless-stopped \
  louisho5/picobot:latest
```

All config, memory, and skills are persisted in `./picobot-data` on your host.

### Docker Compose

Create a `docker-compose.yml`:

```yaml
services:
  picobot:
    image: louisho5/picobot:latest
    container_name: picobot
    restart: unless-stopped
    environment:
      - OPENAI_API_KEY=your-key
      - OPENAI_API_BASE=https://openrouter.ai/api/v1
      - PICOBOT_MODEL=openrouter/free
      - TELEGRAM_BOT_TOKEN=your-telegram-token
      - TELEGRAM_ALLOW_FROM=your-user-id
    volumes:
      - ./picobot-data:/home/picobot/.picobot
```

Then run:

```sh
docker compose up -d
```

### From Source

```sh
go build -o picobot ./cmd/picobot
./picobot onboard                     # creates ~/.picobot config + workspace
./picobot agent -m "Hello!"           # single-shot query
./picobot gateway                     # long-running mode with Telegram
```

## Architecture

Actually the logic is simple and straightforward. Messages flow through a **Chat Hub** (inbound/outbound channels) into the **Agent Loop**, which builds context from memory/sessions/skills, calls the LLM via OpenAI-compatible API, and executes tools (filesystem, exec, web, etc.) before sending replies back through the hub.

<p>
  <img src="how-it-works.png" alt="How Picobot Works" width="600">
</p>

Notes: Channel refers to communication channels (e.g., Telegram, Discord, WhatsApp, etc.).

## Features

### 11 Built-in Tools

The agent can take real actions — not just chat:

| Tool | What it does |
|------|-------------|
| `filesystem` | Read, write, list files |
| `exec` | Run shell commands |
| `web` | Fetch web pages and APIs |
| `message` | Send messages to channels |
| `spawn` | Launch background subagents |
| `cron` | Schedule recurring tasks |
| `write_memory` | Persist information across sessions |
| `create_skill` | Create reusable skill packages |
| `list_skills` | List available skills |
| `read_skill` | Read a skill's content |
| `delete_skill` | Remove a skill |

### Persistent Memory

Picobot remembers things between conversations:

- **Daily notes** — auto-organized by date
- **Long-term memory** — survives restarts
- **Ranked recall** — retrieves the most relevant memories for each query

```sh
picobot memory recent --days 7     # what happened this week?
picobot memory rank -q "meeting"   # find relevant memories
```

### Skills System

Teach your agent new tricks. Skills are modular knowledge packages that extend the agent:

```sh
You: "Create a skill for checking weather using curl wttr.in"
Agent: Created skill "weather" — I'll use it from now on.
```

Skills are just markdown files in `~/.picobot/workspace/skills/`. Create them via the agent or manually.

### Telegram Integration

Chat with your agent from your phone. Set up in 2 minutes:

1. Message [@BotFather](https://t.me/BotFather) — `/newbot` — copy the token
2. Add the token to config or pass as `TELEGRAM_BOT_TOKEN` env var
3. Start the commu