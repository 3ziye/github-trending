# OpenAB — Open Agent Broker

[![Stars](https://img.shields.io/github/stars/openabdev/openab?style=flat-square)](https://github.com/openabdev/openab) [![GitHub Release](https://img.shields.io/github/v/release/openabdev/openab?style=flat-square&logo=github)](https://github.com/openabdev/openab/releases/latest) ![License](https://img.shields.io/badge/license-MIT-A374ED?style=flat-square)

![OpenAB banner](images/banner.jpg)

A lightweight, secure, cloud-native ACP harness that bridges **Discord, Slack**, and any [Agent Client Protocol](https://github.com/anthropics/agent-protocol)-compatible coding CLI (Kiro CLI, Claude Code, Codex, Gemini, OpenCode, Copilot CLI, etc.) over stdio JSON-RPC — delivering the next-generation development experience. **Telegram, LINE**, and other webhook-based platforms are supported via the standalone [Custom Gateway](gateway/).

🪼 **Join our community!** Come say hi on Discord — we'd love to have you: **[🪼 OpenAB — Official](https://discord.gg/DmbhfDZjQS)** 🎉

```
┌──────────────┐  Gateway WS   ┌──────────────┐  ACP stdio    ┌──────────────┐
│   Discord    │◄─────────────►│              │──────────────►│  coding CLI  │
│   User       │               │    openab    │◄── JSON-RPC ──│  (acp mode)  │
├──────────────┤  Socket Mode  │    (Rust)    │               └──────────────┘
│   Slack      │◄─────────────►│              │
│   User       │               └──────┬───────┘
├──────────────┤                      │ WebSocket (outbound)
│   Telegram   │◄──webhook──┐         │
│   User       │            │         │
├──────────────┤            ▼         ▼
│   LINE       │◄──webhook──┌──────────────────┐
│   User       │            │  Custom Gateway  │
└──────────────┘            │  (standalone)    │
                            └──────────────────┘
```

## Demo

![openab demo](images/demo.png)

## Features

- **Multi-platform** — supports Discord and Slack, run one or both simultaneously
- **Pluggable agent backend** — swap between Kiro CLI, Claude Code, Codex, Gemini, OpenCode, Copilot CLI via config
- **@mention trigger** — mention the bot in an allowed channel to start a conversation
- **Thread-based multi-turn** — auto-creates threads; no @mention needed for follow-ups
- **Edit-streaming** — live-updates the Discord message every 1.5s as tokens arrive
- **Emoji status reactions** — 👀→🤔→🔥/👨‍💻/⚡→👍+random mood face
- **Session pool** — one CLI process per thread, auto-managed lifecycle
- **ACP protocol** — JSON-RPC over stdio with tool call, thinking, and permission auto-reply support
- **Kubernetes-ready** — Dockerfile + k8s manifests with PVC for auth persistence
- **Voice message STT** — auto-transcribes Discord voice messages via Groq, OpenAI, or local Whisper server ([docs/stt.md](docs/stt.md))

## Quick Start

### 1. Create a Bot

<details>
<summary><strong>Discord</strong></summary>

See [docs/discord.md](docs/discord.md) for a detailed step-by-step guide.

</details>

<details>
<summary><strong>Slack</strong></summary>

See [docs/slack-bot-howto.md](docs/slack-bot-howto.md) for a detailed step-by-step guide.

</details>

<details>
<summary><strong>Telegram</strong> (via Custom Gateway)</summary>

See [docs/telegram.md](docs/telegram.md) for the full setup guide. Requires the standalone [Custom Gateway](gateway/) service.

</details>

<details>
<summary><strong>LINE</strong> (via Custom Gateway)</summary>

See [docs/line.md](docs/line.md) for the full setup guide. Requires the standalone [Custom Gateway](gateway/) service.

</details>

### 2. Install with Helm (Kiro CLI — default)

```bash
helm repo add openab https://openabdev.github.io/openab
helm repo update

helm install openab openab/openab \
  --set agents.kiro.discord.botToken="$DISCORD_BOT_TOKEN" \
  --set-string 'agents.kiro.discord.allowedChannels[0]=YOUR_CHANNEL_ID'

# Slack
helm install openab openab/openab \
  --set agents.kiro.slack.enabled=true \
  --set agents.kiro.slack.botToken="$SLACK_BOT_TOKEN" \
  --set agents.kiro.slack.appToken="$SLACK_APP_TOKEN" \
  --set-string 'agents.kiro.slack.allowedChannels[0]=C0123456789'
```

### 3. Authenticate (first time only)

```bash
kubectl exec -it deployment/openab-kiro -- kiro-cli login --use-device-flow
kubectl rollout restart deployment/openab-kiro
```

### 4. Use

In your Discord channel:
```
@YourBot explain this code
```

The bot creates a thread. After that, just type in the thread — no @mention needed.

**Slack:** `@YourBot explain this code` in a channel — same thread-based workflow as Discord.

## Other Agents

| Agent | CLI | ACP Adapter | Guide |
|-------|-----|-------------|-------|
| Kiro (default) | `kiro-cli acp` | Native | [docs/kiro.md](docs/kiro.md) |
| Claude Code | `claude-agent-acp` | [@agentclientprotocol/claude-agent-acp](https://github.com/agentclientprotocol/claude-agent-acp) | [docs/claude-code.md](docs/claude-code.md) |
| Codex | `codex-acp` | [@zed-industries/codex-acp](https://github.com/zed-industries/codex-acp) | [docs/codex.md](docs/codex.md) |