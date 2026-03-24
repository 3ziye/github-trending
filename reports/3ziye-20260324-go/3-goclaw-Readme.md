<p align="center">
  <img src="_statics/goclaw-logo.svg" alt="GoClaw" height="200" />
</p>

<p align="center"><strong>Multi-Tenant AI Agent Platform</strong></p>

<p align="center">
Multi-agent AI gateway built in Go. 20+ LLM providers. 7 channels. Multi-tenant PostgreSQL.<br/>
Single binary. Production-tested. Agents that orchestrate for you.
</p>

<p align="center">
  <a href="https://docs.goclaw.sh">Documentation</a> •
  <a href="https://docs.goclaw.sh/#quick-start">Quick Start</a> •
  <a href="https://x.com/nlb_io">Twitter / X</a>
</p>

<p align="center">
  <a href="https://go.dev/"><img src="https://img.shields.io/badge/Go_1.26-00ADD8?style=flat-square&logo=go&logoColor=white" alt="Go" /></a>
  <a href="https://www.postgresql.org/"><img src="https://img.shields.io/badge/PostgreSQL_18-316192?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL" /></a>
  <a href="https://www.docker.com/"><img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker" /></a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/API/WebSocket"><img src="https://img.shields.io/badge/WebSocket-010101?style=flat-square&logo=socket.io&logoColor=white" alt="WebSocket" /></a>
  <a href="https://opentelemetry.io/"><img src="https://img.shields.io/badge/OpenTelemetry-000000?style=flat-square&logo=opentelemetry&logoColor=white" alt="OpenTelemetry" /></a>
  <a href="https://www.anthropic.com/"><img src="https://img.shields.io/badge/Anthropic-191919?style=flat-square&logo=anthropic&logoColor=white" alt="Anthropic" /></a>
  <a href="https://openai.com/"><img src="https://img.shields.io/badge/OpenAI_Compatible-412991?style=flat-square&logo=openai&logoColor=white" alt="OpenAI" /></a>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" alt="License: MIT" />
</p>

A Go port of [OpenClaw](https://github.com/openclaw/openclaw) with enhanced security, multi-tenant PostgreSQL, and production-grade observability.

🌐 **Languages:**
[🇨🇳 简体中文](_readmes/README.zh-CN.md) ·
[🇯🇵 日本語](_readmes/README.ja.md) ·
[🇰🇷 한국어](_readmes/README.ko.md) ·
[🇻🇳 Tiếng Việt](_readmes/README.vi.md) ·
[🇵🇭 Tagalog](_readmes/README.tl.md) ·
[🇪🇸 Español](_readmes/README.es.md) ·
[🇧🇷 Português](_readmes/README.pt.md) ·
[🇮🇹 Italiano](_readmes/README.it.md) ·
[🇩🇪 Deutsch](_readmes/README.de.md) ·
[🇫🇷 Français](_readmes/README.fr.md) ·
[🇸🇦 العربية](_readmes/README.ar.md) ·
[🇮🇳 हिन्दी](_readmes/README.hi.md) ·
[🇷🇺 Русский](_readmes/README.ru.md) ·
[🇧🇩 বাংলা](_readmes/README.bn.md) ·
[🇮🇱 עברית](_readmes/README.he.md) ·
[🇵🇱 Polski](_readmes/README.pl.md) ·
[🇨🇿 Čeština](_readmes/README.cs.md) ·
[🇳🇱 Nederlands](_readmes/README.nl.md) ·
[🇹🇷 Türkçe](_readmes/README.tr.md) ·
[🇺🇦 Українська](_readmes/README.uk.md) ·
[🇮🇩 Bahasa Indonesia](_readmes/README.id.md) ·
[🇹🇭 ไทย](_readmes/README.th.md) ·
[🇵🇰 اردو](_readmes/README.ur.md) ·
[🇷🇴 Română](_readmes/README.ro.md) ·
[🇸🇪 Svenska](_readmes/README.sv.md) ·
[🇬🇷 Ελληνικά](_readmes/README.el.md) ·
[🇭🇺 Magyar](_readmes/README.hu.md) ·
[🇫🇮 Suomi](_readmes/README.fi.md) ·
[🇩🇰 Dansk](_readmes/README.da.md) ·
[🇳🇴 Norsk](_readmes/README.nb.md)

## What Makes It Different

- **Agent Teams & Orchestration** — Teams with shared task boards, inter-agent delegation (sync/async), and hybrid agent discovery
- **Multi-Tenant PostgreSQL** — Per-user workspaces, per-user context files, encrypted API keys (AES-256-GCM), isolated sessions
- **Single Binary** — ~25 MB static Go binary, no Node.js runtime, <1s startup, runs on a $5 VPS
- **Production Security** — 5-layer permission system (gateway auth → global tool policy → per-agent → per-channel → owner-only) plus rate limiting, prompt injection detection, SSRF protection, shell deny patterns, and AES-256-GCM encryption
- **20+ LLM Providers** — Anthropic (native HTTP+SSE with prompt caching), OpenAI, OpenRouter, Groq, DeepSeek, Gemini, Mistral, xAI, MiniMax, Cohere, Perplexity, DashScope, Bailian, Zai, Ollama, Ollama Cloud, Claude CLI, Codex, ACP, and any OpenAI-compatible endpoint
- **7 Messaging Channels** — Telegram, Discord, Slack, Zalo OA, Zalo Personal, Feishu/Lark, WhatsApp
- **Extended Thinking** — Per-provider thinking mode (Anthropic budget tokens, OpenAI reasoning effort, DashScope thinking budget) with streaming support
- **Heartbeat System** — Periodic agent check-ins via HEARTBEAT.md checklists with suppress-on-OK, active hours, retry logic, and channel delivery
- **Scheduling & Cron** — `at`, `every`, and cron expressions for automated agent tasks with lane-based concurrency
- **Observability** — Built-in LLM call tracing with spans and prompt cache metrics, optional OpenTelemetry OTLP export

## Claw Ecosystem

|                 | OpenClaw        | ZeroClaw | PicoClaw | **GoClaw**                              |
| --------------- | --------------- | -------- | -------- | --------------------------------------- |
| Language        | TypeScript      | Rust     | Go       | **Go**                         