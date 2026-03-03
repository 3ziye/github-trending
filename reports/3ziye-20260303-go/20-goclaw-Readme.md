<p align="center">
  <img src="_statics/goclaw.png" alt="GoClaw" />
</p>

# GoClaw

[![Go](https://img.shields.io/badge/Go_1.25-00ADD8?style=flat-square&logo=go&logoColor=white)](https://go.dev/) [![PostgreSQL](https://img.shields.io/badge/PostgreSQL_18-316192?style=flat-square&logo=postgresql&logoColor=white)](https://www.postgresql.org/) [![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)](https://www.docker.com/) [![WebSocket](https://img.shields.io/badge/WebSocket-010101?style=flat-square&logo=socket.io&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket) [![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-000000?style=flat-square&logo=opentelemetry&logoColor=white)](https://opentelemetry.io/) [![Anthropic](https://img.shields.io/badge/Anthropic-191919?style=flat-square&logo=anthropic&logoColor=white)](https://www.anthropic.com/) [![OpenAI](https://img.shields.io/badge/OpenAI_Compatible-412991?style=flat-square&logo=openai&logoColor=white)](https://openai.com/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

**GoClaw** is a multi-agent AI gateway that connects LLMs to your tools, channels, and data — deployed as a single Go binary with zero runtime dependencies. It orchestrates agent teams, inter-agent delegation, and quality-gated workflows across 13+ LLM providers with full multi-tenant isolation.

A Go port of [OpenClaw](https://github.com/openclaw/openclaw) with enhanced security, multi-tenant PostgreSQL, and production-grade observability.

## What Makes It Different

- **Agent Teams & Orchestration** — Teams with shared task boards, inter-agent delegation (sync/async), conversation handoff, evaluate-loop quality gates, and hybrid agent discovery
- **Multi-Tenant PostgreSQL** — Per-user workspaces, per-user context files, encrypted API keys (AES-256-GCM), isolated sessions — the only Claw project with DB-native multi-tenancy
- **Single Binary** — ~25 MB static Go binary, no Node.js runtime, <1s startup, runs on a $5 VPS
- **Production Security** — 5-layer defense: rate limiting, prompt injection detection, SSRF protection, shell deny patterns, AES-256-GCM encryption
- **13+ LLM Providers** — Anthropic (native HTTP+SSE with prompt caching), OpenAI, OpenRouter, Groq, DeepSeek, Gemini, Mistral, xAI, MiniMax, Cohere, Perplexity, DashScope (Qwen), Bailian Coding
- **5 Messaging Channels** — Telegram, Discord, Zalo, Feishu/Lark, WhatsApp with `/stop` and `/stopall` commands

## Claw Ecosystem

**Resource Footprint:**

|                 | OpenClaw        | ZeroClaw | PicoClaw | **GoClaw**                              |
| --------------- | --------------- | -------- | -------- | --------------------------------------- |
| Language        | TypeScript      | Rust     | Go       | **Go**                                  |
| Binary size     | 28 MB + Node.js | 3.4 MB   | ~8 MB    | **~25 MB** (base) / **~36 MB** (+ OTel) |
| Docker image    | —               | —        | —        | **~50 MB** (Alpine)                     |
| RAM (idle)      | > 1 GB          | < 5 MB   | < 10 MB  | **~35 MB**                              |
| Startup         | > 5 s           | < 10 ms  | < 1 s    | **< 1 s**                               |
| Target hardware | $599+ Mac Mini  | $10 edge | $10 edge | **$5 VPS+**                             |

**Feature Matrix:**

| Feature                    | OpenClaw                             | ZeroClaw                                     | PicoClaw                              | **GoClaw**                     |
| -------------------------- | ------------------------------------ | -------------------------------------------- | ------------------------------------- | ------------------------------ |
| Multi-tenant (PostgreSQL)  | —                                    | —                                            | —                                     | ✅                             |
| Custom tools (runtime API) | Config-based only                    | —                                            | —                                     | ✅                             |
| MCP integration            | — (uses ACP)                         | —                                            | —                                     | ✅ (stdio/SSE/streamable-http) |
| Agent teams                | —                                    | —                                            | —                                     | ✅ Task board + mailbox        |
| Agent handoff              | —                                    | —                                            | —                                     | ✅ Conversation transfer       |
| Evaluate loop              | —                                    | —                                            | —                                     | ✅ Generator-evaluator cycle   |
| Quality gates              | —                     