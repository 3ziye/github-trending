# cc-connect

[![Discord](https://img.shields.io/discord/1478978944567869652?logo=discord&label=Discord)](https://discord.gg/kHpwgaM4kq)
[![Telegram](https://img.shields.io/badge/Telegram-Group-26A5E4?logo=telegram)](https://t.me/+odGNDhCjbjdmMmZl)
[![GitHub release](https://img.shields.io/github/v/release/chenhg5/cc-connect?include_prereleases)](https://github.com/chenhg5/cc-connect/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

English | [中文](./README.zh-CN.md)

**Control your local AI agents from any chat app. Anywhere, anytime.**

cc-connect bridges AI agents running on your machine to the messaging platforms you already use. Code review, research, automation, data analysis — anything an AI agent can do, now accessible from your phone, tablet, or any device with a chat app.

```
         You (Phone / Laptop / Tablet)
                    │
    ┌───────────────┼───────────────┐
    ▼               ▼               ▼
 Feishu          Slack          Telegram  ...9 platforms
    │               │               │
    └───────────────┼───────────────┘
                    ▼
              ┌────────────┐
              │ cc-connect │  ← your dev machine
              └────────────┘
              ┌─────┼─────┐
              ▼     ▼     ▼
         Claude  Gemini  Codex  ...7 agents
          Code    CLI   OpenCode / iFlow
```

### Why cc-connect?

> Time to uninstall OpenClaw — cc-connect gives you access to the most powerful AI agents available, not just one.

- **7 AI Agents** — Claude Code, Codex, Cursor Agent, Qoder CLI, Gemini CLI, OpenCode, iFlow CLI. Use whichever fits your workflow, or all of them at once.
- **9 Chat Platforms** — Feishu, DingTalk, Slack, Telegram, Discord, WeChat Work, LINE, QQ, QQ Bot (Official). Most need zero public IP.
- **Multi-Bot Relay** — Bind multiple bots in a group chat and let them communicate with each other. Ask Claude, get insights from Gemini — all in one conversation.
- **Full Control from Chat** — Switch models (`/model`), change permission modes (`/mode`), manage sessions, all via slash commands.
- **Agent Memory** — Read and write agent instruction files (`/memory`) without touching the terminal.
- **Scheduled Tasks** — Set up cron jobs in natural language. "Every day at 6am, summarize GitHub trending" just works.
- **Voice & Images** — Send voice messages or screenshots; cc-connect handles STT/TTS and multimodal forwarding.
- **Multi-Project** — One process, multiple projects, each with its own agent + platform combo.

<p align="center">
  <img src="docs/images/screenshot/cc-connect-lark.JPG" alt="飞书" width="32%" />
  <img src="docs/images/screenshot/cc-connect-telegram.JPG" alt="Telegram" width="32%" />
  <img src="docs/images/screenshot/cc-connect-wechat.JPG" alt="微信" width="32%" />
</p>
<p align="center">
  <em>Left：Lark &nbsp;|&nbsp; Telegram &nbsp;|&nbsp; Right：Wechat</em>
</p>

## Support Matrix

| Component | Type | Status |
|-----------|------|--------|
| Agent | Claude Code | ✅ Supported |
| Agent | Codex (OpenAI) | ✅ Supported |
| Agent | Cursor Agent | ✅ Supported |
| Agent | Gemini CLI (Google) | ✅ Supported |
| Agent | Qoder CLI | ✅ Supported |
| Agent | OpenCode (Crush) | ✅ Supported |
| Agent | iFlow CLI | ✅ Supported |
| Agent | Goose (Block) | 🔜 Planned |
| Agent | Aider | 🔜 Planned |
| Agent | Kimi Code (Moonshot) | 🔭 Exploring |
| Agent | GLM Code / CodeGeeX (ZhipuAI) | 🔭 Exploring |
| Agent | MiniMax Code | 🔭 Exploring |
| Platform | Feishu (Lark) | ✅ WebSocket — no public IP needed |
| Platform | DingTalk | ✅ Stream — no public IP needed |
| Platform | Telegram | ✅ Long Polling — no public IP needed |
| Platform | Slack | ✅ Socket Mode — no public IP needed |
| Platform | Discord | ✅ Gateway — no public IP needed |
| Platform | LINE | ✅ Webhook — public URL required |
| Platform | WeChat Work (企业微信) | ✅ Webhook — public URL required |
| Platform | QQ (via NapCat/OneBot) | ✅ WebSocket, no public IP needed — **Beta** |
| Platform | QQ Bot (Official) | ✅ WebSocket — no public IP needed |
| Platform | WhatsApp | 🔜 Planned (Business Cloud API) |
| Platform | Microsoft Teams | 🔜 Planned (Bot Framework) |
| Platform | Google Chat | 🔜 Planned (Chat API) |
| Platform | Mattermost | 🔜 Planned (Webhook + Bot) |
| Platform | Matrix (Element) | 🔜 Planned (Client-Server API) |
| Feature | Voice Messages (STT) | ✅ Whisper API (OpenAI / Groq / Qwen) + ffmpeg |
| Feature | Voice Reply (TTS) | ✅ Qwen TTS / OpenAI TTS + ffmpeg |
| Feature | Image Messages | ✅ Multimodal (Claude Code) |
| Feature | API Provider Management | ✅ Runtime provider switching |
| Feature | CLI Send (`cc-connect send`) | ✅ Send messages to sessions via CLI |
| Feature | Multi-Bot Relay | ✅ Cross-platform bot communication & group chat binding |

## Quick Start

### Prerequisites

- **Claude Code**: [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code) installed and configured, OR
- **Codex**: [Codex CLI](https:/