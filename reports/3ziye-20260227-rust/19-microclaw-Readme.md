# MicroClaw
<img src="icon.png" alt="MicroClaw logo" width="56" align="right" />

[English](README.md) | [中文](README_CN.md)

[![Website](https://img.shields.io/badge/Website-microclaw.ai-blue)](https://microclaw.ai)
[![Discord](https://img.shields.io/badge/Discord-Join-5865F2?logo=discord&logoColor=white)](https://discord.gg/pvmezwkAk5)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)


<p align="center">
  <img src="screenshots/headline.png" alt="MicroClaw headline logo" width="92%" />
</p>


> **Note:** This project is under active development. Features may change, and contributions are welcome!


An agentic AI assistant for chat surfaces, inspired by [nanoclaw](https://github.com/gavrielc/nanoclaw/) and incorporating some of its design ideas. MicroClaw uses a channel-agnostic core with platform adapters: it currently supports Telegram, Discord, Slack, Feishu/Lark, Matrix, WhatsApp, iMessage, Email, Nostr, Signal, DingTalk, QQ, IRC, and Web, and is designed to add more platforms over time. It works with multiple LLM providers (Anthropic + OpenAI-compatible APIs) and supports full tool execution: run shell commands, read/write/edit files, search codebases, browse the web, schedule tasks, and maintain persistent memory across conversations.


<p align="center">
  <img src="screenshots/screenshot1.png" width="45%" />
  &nbsp;&nbsp;
  <img src="screenshots/screenshot2.png" width="45%" />
</p>

## Table of contents

- [How it works](#how-it-works)
- [Install](#install)
- [Features](#features)
- [Tools](#tools)
- [Memory](#memory)
- [Skills](#skills)
- [Plugins](#plugins)
- [MCP](#mcp)
- [Plan & Execute](#plan--execute)
- [Scheduling](#scheduling)
- [Local Web UI (cross-channel history)](#local-web-ui-cross-channel-history)
- [Release](#release)
- [Setup](#setup)
- [Configuration](#configuration)
- [Docker Sandbox](#docker-sandbox)
- [Platform behavior](#platform-behavior)
- [Multi-chat permission model](#multi-chat-permission-model)
- [Usage examples](#usage-examples)
- [Architecture](#architecture)
- [Adding a New Platform Adapter](#adding-a-new-platform-adapter)
- [Documentation](#documentation)

## Install

### One-line installer (recommended)

```sh
curl -fsSL https://microclaw.ai/install.sh | bash
```

### Windows PowerShell installer

```powershell
iwr https://microclaw.ai/install.ps1 -UseBasicParsing | iex
```

This installer only does one thing:
- Download and install the matching prebuilt binary from the latest GitHub release
- It does not fallback to Homebrew/Cargo inside `install.sh` (use separate methods below)

### Preflight diagnostics

Run cross-platform diagnostics before first start (or when troubleshooting):

```sh
microclaw doctor
```

Machine-readable output for support tickets:

```sh
microclaw doctor --json
```

Checks include PATH, shell runtime, `agent-browser`, PowerShell policy (Windows), and MCP command dependencies from `<data_dir>/mcp.json` plus `<data_dir>/mcp.d/*.json`.

Sandbox-only diagnostics:

```sh
microclaw doctor sandbox
```

### Uninstall (script)

macOS/Linux:

```sh
curl -fsSL https://microclaw.ai/uninstall.sh | bash
```

Windows PowerShell:

```powershell
iwr https://microclaw.ai/uninstall.ps1 -UseBasicParsing | iex
```

### Homebrew (macOS)

```sh
brew tap microclaw/tap
brew install microclaw
```

### From source

```sh
git clone https://github.com/microclaw/microclaw.git
cd microclaw
cargo build --release
cp target/release/microclaw /usr/local/bin/
```

Optional semantic-memory build (sqlite-vec disabled by default):

```sh
cargo build --release --features sqlite-vec
```

First-time sqlite-vec quickstart (3 commands):

```sh
cargo run --features sqlite-vec -- setup
cargo run --features sqlite-vec -- start
sqlite3 <data_dir>/runtime/microclaw.db "SELECT id, chat_id, chat_channel, external_chat_id, category, embedding_model FROM memories ORDER BY id DESC LIMIT 20;"
```

In `setup`, set:
- `embedding_provider` = `openai` or `ollama`
- provider credentials/base URL/model as needed

## How it works

Every message triggers an **agentic loop**: the model can call tools, inspect the results, call more tools, and reason through multi-step tasks before responding. Up to 100 iterations per request by default.

<p align="center">
  <img src="docs/assets/readme/microclaw-architecture.svg" alt="MicroClaw architecture overview" width="96%" />
</p>

## Blog post

For a deeper dive into the architecture and design decisions, read: **[Building MicroClaw: An Agentic AI Assistant in Rust That Lives in Your Chats](https://microclaw.ai/blog/building-microclaw)**

## Features

- **Agentic tool use** -- bash commands, file read/write/edit, glob search, regex grep, persistent memory
- **Session resume** -- full conversation state (including tool interactions) persisted between messages; the agent keeps tool-call state across invocations
- **Context compaction** -- when sessions grow too large, older messages are automatically summarized to stay within context li