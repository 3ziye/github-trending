<p align="center">
  <img src="pi_agent_rust_illustration.webp" alt="Pi Agent Rust" width="600"/>
</p>

<h1 align="center">pi_agent_rust</h1>

<p align="center">
  <strong>pi_agent_rust - High-performance AI coding agent CLI written in Rust</strong>
</p>

<p align="center">
  <a href="#why-should-you-care">Why Should You Care?</a> •
  <a href="#tldr-piopenclaw-users">TL;DR</a> •
  <a href="#benchmark-methodology-and-claim-integrity">Methodology</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="#features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#commands">Commands</a> •
  <a href="#configuration">Configuration</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/rust-2024%20edition-orange?logo=rust" alt="Rust 2024">
  <img src="https://img.shields.io/badge/license-MIT%20%2B%20Rider-blue" alt="License: MIT + Rider">
  <img src="https://img.shields.io/badge/unsafe-forbidden-brightgreen" alt="No Unsafe Code">
  <a href="https://github.com/Dicklesworthstone/pi_agent_rust/actions/workflows/ci.yml">
    <img src="https://github.com/Dicklesworthstone/pi_agent_rust/actions/workflows/ci.yml/badge.svg?branch=main" alt="CI">
  </a>
  <a href="https://github.com/Dicklesworthstone/pi_agent_rust/actions/workflows/bench.yml">
    <img src="https://github.com/Dicklesworthstone/pi_agent_rust/actions/workflows/bench.yml/badge.svg?branch=main" alt="Bench">
  </a>
</p>

```bash
# Install latest release
curl -fsSL "https://raw.githubusercontent.com/Dicklesworthstone/pi_agent_rust/main/install.sh?$(date +%s)" | bash
```

---

## The Problem

You want an AI coding assistant in your terminal, but existing tools are:
- **Slow to start**: Node.js/Python runtimes add 500ms+ before you can type
- **Memory hungry**: Electron apps or heavy runtimes eat gigabytes
- **Unreliable**: Streaming breaks, sessions corrupt, tools fail silently
- **Hard to extend**: Closed ecosystems or complex plugin systems

## The Solution

**pi_agent_rust** is a from-scratch Rust port of [Pi Agent](https://github.com/badlogic/pi) by [Mario Zechner](https://github.com/badlogic) (made with his blessing!). Single binary, instant startup, stable streaming, and 7 built-in tools.

Rather than a direct line-by-line translation, this port builds on two purpose-built Rust libraries:
- **[asupersync](https://github.com/Dicklesworthstone/asupersync)**: A structured concurrency async runtime with built-in HTTP, TLS, and SQLite
- **[rich_rust](https://github.com/Dicklesworthstone/rich_rust)**: A Rust port of [Rich](https://github.com/Textualize/rich) by [Will McGugan](https://github.com/willmcgugan), providing beautiful terminal output with markup syntax

```bash
# Start a session
pi "Help me refactor this function to use async/await"

# Continue a previous session
pi --continue

# Single-shot mode (no session)
pi -p "What does this error mean?" < error.log
```

## Why Should You Care?

If you already use Pi Agent, especially through OpenClaw, this project keeps the core workflow while upgrading the engine under the hood:

- **Substantially faster in realistic end-to-end flows** (not synthetic microbenchmarks)
- **Dramatically smaller memory footprint** in long-running sessions
- **Materially stronger security model** for extension/tool execution, including command-level blocking of dangerous extension shell patterns

Security is a first-class design goal here, not a bolt-on:

- Capability-gated hostcalls (`tool`/`exec`/`http`/`session`/`ui`/`events`)
- Two-stage extension `exec` enforcement: capability gate first, then command mediation that blocks critical shell classes by default (for example recursive delete, disk/device writes, reverse shell) and can tighten to block high-tier classes in strict/safe policy
- Policy + runtime risk + quota enforcement on the execution path
- Per-extension trust lifecycle (`pending` -> `acknowledged` -> `trusted` -> `killed`) with kill-switch audit logs and explicit operator provenance
- Hostcall-lane emergency controls that can force compatibility-lane execution globally or for one extension when fast-lane behavior needs immediate containment
- Structured concurrency via `asupersync` for more predictable cancellation/lifecycle behavior
- Auditable runtime signals/ledgers and redacted security alerts for extension behavior

## TL;DR (Pi/OpenClaw Users)

These are the realistic secure-path numbers that matter most (large-session, end-to-end behavior):

| Scenario | Rust total | Legacy Node total | Legacy Bun total | Rust advantage |
|---|---:|---:|---:|---:|
| Realistic 1M session | 250.29 ms | 1,238.67 ms | 700.52 ms | `4.95x` faster than Node, `2.80x` faster than Bun |
| Realistic 5M session | 1,382.12 ms | 5,974.67 ms | 2,959.42 ms | `4.32x` faster than Node, `2.14x` faster than Bun |

| Scenario | Rust RSS | Legacy Node RSS | Legacy Bun RSS | Rust memory advantage |
|---|---:|---:|---:|---:|
| Realistic 1M session | 67,572 KB | 820,380 KB | 875,092 KB | `12.14x` lower than Node