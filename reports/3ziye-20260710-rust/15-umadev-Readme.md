# umadev

<div align="center">

<img src="docs/assets/umadev-logo-en.png" alt="umadev" width="760">

### UmaDev: A coding agent that works like a real dev team, commanding the Claude Code / Codex / OpenCode you already use.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Rust](https://img.shields.io/badge/Rust-1.87%2B-orange)](https://www.rust-lang.org/)
[![Spec](https://img.shields.io/badge/Spec-UMADEV__HOST__SPEC__V1-blue)](spec/UMADEV_HOST_SPEC_V1.md)
[![Version](https://img.shields.io/badge/Version-1.0.x-success)](CHANGELOG.md)

English | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md)

</div>

---

umadev is **a coding agent that works like a real dev team**. It drives an AI coding CLI you already have — Claude Code, Codex, or OpenCode — as one continuous session, and owns no model of its own: the model your base is connected to is the brain.

What you get is **a whole AI development team**. Eight specialists — product manager, architect, UI/UX designer, frontend engineer, backend engineer, QA, security, and DevOps — plan, build, review, and sign off the way a real team does, borrowing your already-logged-in base as their shared brain. You describe what you want in plain language, and the team turns it into runnable, shippable, auditable software: it researches, writes the PRD, architecture, and UI/UX, builds the frontend and backend, runs the quality and governance checks, and hands back the code plus a delivery proof. It sizes itself to the task — a small edit stays a small edit; a full project convenes the full roster.

A ninth seat, the **coordinator** (the team's technical lead), routes the request, owns a visible plan, schedules the team, enforces the gates, and leaves the audit trail. It doesn't write code; the base — the AI coding CLI — is the engineer that does that. The roles coordinate through shared artifact files and structured verdicts, never by chatting to each other.

It's a single Rust binary. npm is just the delivery shell.

---

## Table of Contents

- [Install](#install)
- [Quickstart](#quickstart)
- [Project Origin](#project-origin)
- [What Problem It Solves](#what-problem-it-solves)
- [Features](#features)
- [How It Works](#how-it-works)
- [The Team](#the-team)
- [Why You Can Trust the Output](#why-you-can-trust-the-output)
- [Runtime Modes](#runtime-modes)
- [The Full Delivery Flow](#the-full-delivery-flow)
- [Quality Gate](#quality-gate)
- [Governance](#governance)
- [Knowledge Base](#knowledge-base)
- [Deliverables](#deliverables)
- [Commands](#commands)
- [Configuration](#configuration)
- [Rust Architecture](#rust-architecture)
- [Development](#development)
- [License](#license)

---

## Install

```bash
npm install -g umadev
```

The npm package is a distribution shim. The actual program is a Rust binary. Prebuilt binaries ship for macOS (Apple Silicon and Intel), Linux (x86_64 and ARM64), and Windows (x86_64).

The binary and the curated knowledge corpus install from npm and work fully offline. The optional local embedding model (`multilingual-e5-small`, f16, ~224 MB) is **not** bundled in the npm package — it is fetched on first run to `~/.umadev/embed-model` (a one-time download), then powers offline vector search locally with no API key and no runtime network. If that first-run download is unavailable (offline install, restricted network), umadev still works: retrieval falls back to BM25-only until the model is present, and it self-heals — a later run re-downloads it (a corrupt cache is re-fetched, not trusted).

Build from source:

```bash
git clone https://github.com/umacloud/umadev.git
cd umadev && cargo build --release --features vector-local
./target/release/umadev --version
```

> **Building from source? The embedding model is not in the repo (it's too large for git, ~224 MB).** A plain `cargo build --release` gives a **BM25-only** binary; the local vector channel needs the `--features vector-local` flag **and** the model on disk. The prebuilt binaries and `npm i` bundle both automatically — for a source build, download `multilingual-e5-small` into `~/.umadev/embed-model/` once:
>
> ```bash
> mkdir -p ~/.umadev/embed-model && cd ~/.umadev/embed-model
> for f in config.json tokenizer.json model.safetensors; do
>   curl -fsSL "https://huggingface.co/intfloat/multilingual-e5-small/resolve/main/$f" -o "$f"
> done
> ```
>
> umadev auto-discovers it there (or point `UMADEV_EMBED_MODEL_DIR` at any directory with those three files). Without the model, umadev still works — retrieval just falls back to BM25-only.

You also need one AI coding CLI installed and logged in — that's the brain umadev drives:

| Base | Install | Log in |
|---|---|---|
| Claude Code | `npm i -g @anthropic-ai/claude-code` | `claude auth login` |
| Codex | `npm i -g @openai/codex` | `codex login` |
| OpenCode | see opencode.ai | `opencode auth login` |

umadev injects nothing into the base. Whatever your base is configured with — an official login or your own third