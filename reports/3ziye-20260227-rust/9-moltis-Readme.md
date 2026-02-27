<div align="center">

<a href="https://moltis.org"><img src="https://raw.githubusercontent.com/moltis-org/moltis-website/main/favicon.svg" alt="Moltis" width="64"></a>

# Moltis — A Rust-native claw you can trust

One binary — sandboxed, secure, yours.

[![CI](https://github.com/moltis-org/moltis/actions/workflows/ci.yml/badge.svg)](https://github.com/moltis-org/moltis/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/moltis-org/moltis/graph/badge.svg)](https://codecov.io/gh/moltis-org/moltis)
[![CodSpeed](https://img.shields.io/endpoint?url=https://codspeed.io/badge.json&style=flat&label=CodSpeed)](https://codspeed.io/moltis-org/moltis)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Rust](https://img.shields.io/badge/Rust-1.91%2B-orange.svg)](https://www.rust-lang.org)
[![Discord](https://img.shields.io/discord/1469505370169933837?color=5865F2&label=Discord&logo=discord&logoColor=white)](https://discord.gg/XnmrepsXp5)

[Installation](#installation) • [Comparison](#comparison) • [Architecture](#architecture--crate-map) • [Security](#security) • [Features](#features) • [How It Works](#how-it-works) • [Contributing](CONTRIBUTING.md)

</div>

---

Moltis recently hit [the front page of Hacker News](https://news.ycombinator.com/item?id=46993587). Please [open an issue](https://github.com/moltis-org/moltis/issues) for any friction at all. I'm focused on making Moltis excellent.

**Secure by design** — Your keys never leave your machine. Every command runs in a sandboxed container, never on your host.

**Your hardware** — Runs on a Mac Mini, a Raspberry Pi, or any server you own. One Rust binary, no Node.js, no npm, no runtime.

**Full-featured** — Voice, memory, scheduling, Telegram, browser automation, MCP servers — all built-in. No plugin marketplace to get supply-chain attacked through.

**Auditable** — The agent loop + provider model fits in ~5K lines. The core (excluding the optional web UI) is ~121K lines across modular crates you can audit independently, with 2,300+ tests and zero `unsafe` code\*.

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

## Comparison

| | OpenClaw | PicoClaw | NanoClaw | ZeroClaw | **Moltis** |
|---|---|---|---|---|---|
| Language | TypeScript | Go | TypeScript | Rust | **Rust** |
| Agent loop | ~430K LoC | Small | ~500 LoC | ~3.4K LoC | **~5K LoC** (`runner.rs` + `model.rs`) |
| Full codebase | — | — | — | 1,000+ tests | **~124K LoC** (2,300+ tests) |
| Runtime | Node.js + npm | Single binary | Node.js | Single binary (3.4 MB) | **Single binary (44 MB)** |
| Sandbox | App-level | — | Docker | Docker | **Docker + Apple Container** |
| Memory safety | GC | GC | GC | Ownership | **Ownership, zero `unsafe`\*** |
| Auth | Basic | API keys | None | Token + OAuth | **Password + Passkey + API keys + Vault** |
| Voice I/O | Plugin | — | — | — | **Built-in (15+ providers)** |
| MCP | Yes | — | — | — | **Yes (stdio + HTTP/SSE)** |
| Hooks | Yes (limited) | — | — | — | **15 event types** |
| Skills | Yes (store) | Yes | Yes | Yes | **Yes (+ OpenClaw Store)** |
| Memory/RAG | Plugin | — | Per-group | SQLite + FTS | **SQLite + FTS + vector** |

\* `unsafe` is denied workspace-wide. The only exceptions are opt-in FFI wrappers behind the `local-embeddings` feature flag, not part of the core.

> [Full comparison with benchmarks →](https://docs.moltis.org/comparison.html)

## Architecture — Crate Map

**Core** (always compiled):

| Crate | LoC | Role |
|-------|-----|------|
| `moltis` (cli) | 2.4K | Entry point, CLI commands |
| `moltis-agents` | 20.1K | LLM providers, agent loop, streaming |
| `moltis-gateway` | 29.2K | HTTP/WS server, RPC, auth |
| `moltis-chat` | 10.2K | Chat engine, agent orchestration |
| `moltis-tools` | 13.4K | Tool execution, sandbox |
| `moltis-config` | 5.1K | Configuration, validation |
| `moltis-sessions` | 2.7K | Session persistence |
| `moltis-plugins` | 1.4K | Hook dispatch, plugin formats |
| `moltis-common` | 0.8K | Shared utilities |

**Optional** (feature-gated or additive):

| Category | Crates | Combined LoC |
|----------|--------|-------------|
| Web UI | `moltis-web` | 4.3K |
| Voice | `moltis-voice` | 4.7K |
| Memory | `moltis-memory`, `moltis-qmd` | 5.8K |
| Channels | `moltis-telegram`, `moltis-msteams`, `moltis-channels` | 6.4K |
| Browser | `moltis-browser` | 4.8K |
| Scheduling | `moltis-cron` | 3.8K |
| Extensibility | `moltis-mcp`, `moltis-skills` | 7.4K |
| Auth/OAuth | `moltis-oauth`, `moltis-onboarding`, `moltis-vault` | 2.8K |
| Metrics | `moltis-metrics` | 1.7K |
| Other | `moltis-projects`, `moltis-routing`, `moltis-protocol`, `moltis-media`, `moltis-canvas`, `moltis-auto-reply` | 2.4K |

Use `--