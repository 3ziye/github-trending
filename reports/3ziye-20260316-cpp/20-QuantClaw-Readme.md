<p align="center">
  <img src="assets/quantclaw-logo-transparent.png" alt="QuantClaw" width="180" />
</p>

<h1 align="center">QuantClaw</h1>

<p align="center">
  <strong>High-performance personal AI assistant in C++17</strong>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="License"></a>
  <a href="https://github.com/QuantClaw/QuantClaw/actions/workflows/github-actions.yml"><img src="https://github.com/QuantClaw/QuantClaw/actions/workflows/github-actions.yml/badge.svg" alt="CI"></a>
  <img src="https://img.shields.io/badge/C%2B%2B-17-00599C.svg?logo=cplusplus&logoColor=white" alt="C++17">
  <img src="https://img.shields.io/badge/tests-886%20passing-brightgreen.svg" alt="886 tests passing">
  <img src="https://img.shields.io/badge/platform-Linux%20%7C%20Windows-lightgrey.svg" alt="Linux | Windows">
  <a href="https://github.com/openclaw/openclaw"><img src="https://img.shields.io/badge/OpenClaw-compatible-orange.svg" alt="OpenClaw Compatible"></a>
</p>

<p align="center">
  <a href="README_CN.md">中文文档</a>
</p>

---

QuantClaw is a native C++ implementation of the [OpenClaw](https://github.com/openclaw/openclaw) ecosystem — built for performance and low memory footprint while staying fully compatible with OpenClaw workspace files, skills, and the WebSocket RPC protocol.

## Features

- **Blazing Fast**: C++17 native performance with minimal overhead
- **Memory Efficient**: Small memory footprint, suitable for resource-constrained environments
- **OpenClaw Compatible**: Works with OpenClaw workspace files, skills, and configuration
- **Dual Protocol**: WebSocket RPC gateway + HTTP REST API
- **Multi-Provider LLM**: OpenAI-compatible and Anthropic APIs with `provider/model` prefix routing
- **Model Failover**: Multi-key rotation with exponential backoff cooldowns and automatic model fallback chains
- **Command Queue**: Per-session serialization with collect/followup/steer/interrupt modes and global concurrency control
- **Context Management**: Auto-compaction, tool result pruning, and BM25 memory search
- **Channel Adapters**: Connect Discord, Telegram, or custom bots to the gateway
- **Session Persistence**: Full conversation history with tool call context preserved in JSONL
- **Skill System**: Compatible with OpenClaw SKILL.md format (both OpenClaw and QuantClaw manifest formats)
- **Plugin Ecosystem**: Full OpenClaw plugin compatibility via Node.js sidecar — tools, hooks, services, providers, commands, HTTP routes, and gateway methods
- **MCP Support**: Model Context Protocol for external tool integration
- **File System First**: No database dependencies — everything stored in your workspace

## 📖 Documentation

Full documentation available at: **[https://quantclaw.github.io/](https://quantclaw.github.io/)**

Includes:
- [Getting Started Guide](https://quantclaw.github.io/guide/getting-started)
- [Installation Instructions](https://quantclaw.github.io/guide/installation)
- [Architecture Overview](https://quantclaw.github.io/guide/architecture)
- [Plugin Development Guide](https://quantclaw.github.io/guide/plugins)
- [CLI Reference](https://quantclaw.github.io/guide/cli-reference)

## Quick Start

### 1. Build QuantClaw

```bash
git clone https://github.com/QuantClaw/QuantClaw.git
cd QuantClaw
mkdir build && cd build
cmake ..
make -j$(nproc)

# Run tests
./quantclaw_tests

# Install (optional)
sudo make install
```

### 2. Run Onboarding Wizard

```bash
# Interactive setup wizard (recommended)
quantclaw onboard

# Or with automatic daemon installation
quantclaw onboard --install-daemon

# Or quick setup without prompts
quantclaw onboard --quick
```

The onboarding wizard guides you through:
- Configuration setup (gateway port, AI model, etc.)
- Workspace creation (SOUL.md, skills directory, etc.)
- Optional daemon installation as system service
- Skills initialization
- Setup verification

### 3. Start the Gateway

```bash
# If installed as service
quantclaw gateway start

# Or run in foreground
quantclaw gateway
```

### 4. Open Dashboard

```bash
quantclaw dashboard
```

This opens the web UI at `http://127.0.0.1:18801`

## Port Configuration

QuantClaw uses dedicated ports to avoid conflicts with OpenClaw and other services:

| Service | Port | Purpose |
|---------|------|---------|
| WebSocket RPC Gateway | `18800` | Main gateway for client connections |
| HTTP REST API / Dashboard | `18801` | Control UI and REST API endpoints |
| Sidecar IPC (TCP loopback) | `18802-18899` | Node.js Sidecar process communication |

**Note**: QuantClaw uses ports `18800-18801` (different from OpenClaw's `18789-18790`), allowing both to run simultaneously.

To use custom ports, edit `~/.quantclaw/quantclaw.json`:

```json
{
  "gateway": {
    "port": 18800,
    "controlUi": {
      "port": 18801
    }
  }
}
```

## Architecture

```
~/.quantclaw/
├── quantclaw.json              # Configuration (OpenClaw format)
├── skills/                     # Installe