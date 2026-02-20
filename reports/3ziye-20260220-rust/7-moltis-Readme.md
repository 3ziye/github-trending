<div align="center">

<a href="https://moltis.org"><img src="https://raw.githubusercontent.com/moltis-org/moltis-website/main/favicon-512.svg" alt="Moltis" width="120"></a>

# Moltis

**A personal AI gateway written in Rust. One binary, no runtime, no npm.**

[![CI](https://github.com/moltis-org/moltis/actions/workflows/ci.yml/badge.svg)](https://github.com/moltis-org/moltis/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/moltis-org/moltis/graph/badge.svg)](https://codecov.io/gh/moltis-org/moltis)
[![CodSpeed](https://img.shields.io/endpoint?url=https://codspeed.io/badge.json&style=flat&label=CodSpeed)](https://codspeed.io/moltis-org/moltis)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Rust](https://img.shields.io/badge/Rust-1.91%2B-orange.svg)](https://www.rust-lang.org)
<!-- [![Discord](https://img.shields.io/discord/1469505370169933837?color=5865F2&label=Discord&logo=discord&logoColor=white)](https://discord.gg/XnmrepsXp5) -->

[Features](#features) • [Installation](#installation) • [Build](#build) • [Cloud Deployment](#cloud-deployment) • [How It Works](#how-it-works) • [Hooks](#hooks) • [Contributing](CONTRIBUTING.md) • [Discord](https://discord.gg/XnmrepsXp5)

</div>

---

Inspired by [OpenClaw](https://docs.openclaw.ai) — just build it and run it.

## Installation

```bash
# One-liner install script (macOS / Linux)
curl -fsSL https://www.moltis.org/install.sh | sh

# macOS / Linux via Homebrew
brew install moltis-org/tap/moltis

# Docker (multi-arch: amd64/arm64)
docker pull ghcr.io/moltis-org/moltis:latest

# Or build from source
cargo install moltis --git https://github.com/moltis-org/moltis
```

## Features

- **Multi-provider LLM support** — OpenAI Codex, GitHub Copilot, and Local
  LLM through a trait-based provider architecture
- **Streaming responses** — real-time token streaming for a responsive user
  experience, including when tools are enabled (tool calls stream argument
  deltas as they arrive)
- **Communication channels** — Telegram integration with an extensible channel
  abstraction for adding others
- **Web gateway** — HTTP and WebSocket server with a built-in web UI
- **Session persistence** — SQLite-backed conversation history, session
  management, and per-session run serialization to prevent history corruption
- **Agent-level timeout** — configurable wall-clock timeout for agent runs
  (default 600s) to prevent runaway executions
- **Sub-agent delegation** — `spawn_agent` tool lets the LLM delegate tasks to
  child agent loops with nesting depth limits and tool filtering
- **Message queue modes** — `followup` (default, replay each queued message as a
  separate run) or `collect` (concatenate and send once) when messages arrive
  during an active run
- **Tool result sanitization** — strips base64 data URIs and long hex blobs,
  truncates oversized results before feeding back to the LLM (configurable
  limit, default 50 KB)
- **Memory and knowledge base** — embeddings-powered long-term memory
- **Skills** — extensible skill system with support for existing repositories
- **Hook system** — lifecycle hooks with priority ordering, parallel dispatch
  for read-only events, circuit breaker, dry-run mode, HOOK.md-based discovery,
  eligibility checks, bundled hooks (boot-md, session-memory, command-logger),
  CLI management (`moltis hooks list/info`), and web UI for editing, enabling/disabling,
  and reloading hooks at runtime
- **Web browsing** — web search (Brave, Perplexity) and URL fetching with
  readability extraction and SSRF protection
- **Voice support** — Text-to-speech (TTS) and speech-to-text (STT) with
  multiple cloud and local providers. Configure and manage voice providers
  from the Settings UI.
- **Scheduled tasks** — cron-based task execution
- **OAuth flows** — built-in OAuth2 for provider authentication
- **TLS support** — automatic self-signed certificate generation
- **Observability** — OpenTelemetry tracing with OTLP export
- **MCP (Model Context Protocol) support** — connect to MCP tool servers over
  stdio or HTTP/SSE (remote servers), with health polling, automatic restart
  on crash (exponential backoff), and in-UI server config editing
- **Parallel tool execution** — when the LLM requests multiple tool calls in
  one turn, they run concurrently via `futures::join_all`, reducing latency
- **Sandboxed execution** — Docker and Apple Container backends with pre-built
  images, configurable packages, and per-session isolation
- **Authentication** — password and passkey (WebAuthn) authentication with
  session cookies, API key support, and a first-run setup code flow
- **Endpoint throttling** — built-in per-IP request throttling for
  unauthenticated traffic when auth is enforced, with strict limits for
  password login attempts and sensible caps for API/WS traffic (`429` +
  `Retry-After` on limit hit)
- **WebSocket security** — Origin validation to prevent Cross-Site WebSocket
  Hijacking (CSWSH)
- **Onboarding wizar