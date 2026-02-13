<p align="center">
  <img src="ironclaw.png" alt="IronClaw" width="200"/>
</p>

<h1 align="center">IronClaw</h1>

<p align="center">
  <strong>Your secure personal AI assistant, always on your side</strong>
</p>

<p align="center">
  <a href="#philosophy">Philosophy</a> •
  <a href="#features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#configuration">Configuration</a> •
  <a href="#security">Security</a> •
  <a href="#architecture">Architecture</a>
</p>

---

## Philosophy

IronClaw is built on a simple principle: **your AI assistant should work for you, not against you**.

In a world where AI systems are increasingly opaque about data handling and aligned with corporate interests, IronClaw takes a different approach:

- **Your data stays yours** - All information is stored locally, encrypted, and never leaves your control
- **Transparency by design** - Open source, auditable, no hidden telemetry or data harvesting
- **Self-expanding capabilities** - Build new tools on the fly without waiting for vendor updates
- **Defense in depth** - Multiple security layers protect against prompt injection and data exfiltration

IronClaw is the AI assistant you can actually trust with your personal and professional life.

## Features

### Security First

- **WASM Sandbox** - Untrusted tools run in isolated WebAssembly containers with capability-based permissions
- **Credential Protection** - Secrets are never exposed to tools; injected at the host boundary with leak detection
- **Prompt Injection Defense** - Pattern detection, content sanitization, and policy enforcement
- **Endpoint Allowlisting** - HTTP requests only to explicitly approved hosts and paths

### Always Available

- **Multi-channel** - REPL, HTTP webhooks, WASM channels (Telegram, Slack), and web gateway
- **Docker Sandbox** - Isolated container execution with per-job tokens and orchestrator/worker pattern
- **Web Gateway** - Browser UI with real-time SSE/WebSocket streaming
- **Routines** - Cron schedules, event triggers, webhook handlers for background automation
- **Heartbeat System** - Proactive background execution for monitoring and maintenance tasks
- **Parallel Jobs** - Handle multiple requests concurrently with isolated contexts
- **Self-repair** - Automatic detection and recovery of stuck operations

### Self-Expanding

- **Dynamic Tool Building** - Describe what you need, and IronClaw builds it as a WASM tool
- **MCP Protocol** - Connect to Model Context Protocol servers for additional capabilities
- **Plugin Architecture** - Drop in new WASM tools and channels without restarting

### Persistent Memory

- **Hybrid Search** - Full-text + vector search using Reciprocal Rank Fusion
- **Workspace Filesystem** - Flexible path-based storage for notes, logs, and context
- **Identity Files** - Maintain consistent personality and preferences across sessions

## Installation

### Prerequisites

- Rust 1.85+
- PostgreSQL 15+ with [pgvector](https://github.com/pgvector/pgvector) extension
- NEAR AI account (authentication handled via setup wizard)

## Download or Build

Visit [Releases page](https://github.com/nearai/ironclaw/releases/) to see the latest updates.

<details>
  <summary>Install via Windows Installer (Windows)</summary>

Download the [Windows Installer](https://github.com/nearai/ironclaw/releases/latest/download/ironclaw-x86_64-pc-windows-msvc.msi) and run it.

</details>

<details>
  <summary>Install via powershell script (Windows)</summary>

```sh
irm https://github.com/nearai/ironclaw/releases/latest/download/ironclaw-installer.ps1 | iex
```

</details>

<details>
  <summary>Install via shell script (macOS, Linux, Windows/WSL)</summary>

```sh
curl --proto '=https' --tlsv1.2 -LsSf https://github.com/nearai/ironclaw/releases/latest/download/ironclaw-installer.sh | sh
```
</details>

<details>
  <summary>Compile the source code (Cargo on Windows, Linux, macOS)</summary>

Install it with `cargo`, just make sure you have [Rust](https://rustup.rs) installed on your computer.

```bash
# Clone the repository
git clone https://github.com/nearai/ironclaw.git
cd ironclaw

# Build
cargo build --release

# Run tests
cargo test
```

For **full release** (after modifying channel sources), run `./scripts/build-all.sh` to rebuild channels first.

</details>

### Database Setup

```bash
# Create database
createdb ironclaw

# Enable pgvector
psql ironclaw -c "CREATE EXTENSION IF NOT EXISTS vector;"
```

## Configuration

Run the setup wizard to configure IronClaw:

```bash
ironclaw onboard
```

The wizard handles database connection, NEAR AI authentication (via browser OAuth),
and secrets encryption (using your system keychain). All settings are saved to
`~/.ironclaw/settings.toml`.

## Security

IronClaw implements defense in depth to protect your data and prevent misuse.

### WASM Sandbox

All untrusted tools run in isolated WebAssembly containers:

- **Capability-based permissions** - Explicit opt-in for HTTP, secrets, tool i