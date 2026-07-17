<div align="center">

# ⚡ Godcoder

### A local-first, open-source AI coding agent for your desktop.

**Bring your own LLM key. Your code never leaves your machine.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Built with Rust](https://img.shields.io/badge/Built%20with-Rust-orange?logo=rust)](https://www.rust-lang.org/)
[![Tauri 2](https://img.shields.io/badge/Tauri-2.0-blue?logo=tauri)](https://tauri.app/)
[![Stars](https://img.shields.io/github/stars/eli-labz/Godcoder?style=social)](https://github.com/eli-labz/Godcoder/stargazers)
[![Forks](https://img.shields.io/github/forks/eli-labz/Godcoder?style=social)](https://github.com/eli-labz/Godcoder/network/members)

[**Download**](#getting-started) · [**Features**](#what-godcoder-can-do) · [**Architecture**](ARCHITECTURE.md) · [**Contribute**](CONTRIBUTING.md)

</div>

---

## 🚀 What is Godcoder?

Godcoder is a **local-first, fully open-source AI coding agent** that runs as a native desktop app. Unlike cloud-based tools, your source code never transits a vendor backend — API requests go straight from your machine to whichever model provider you configure.

It goes beyond editing code: Godcoder can **build and continuously improve its own agent harness** (Harness mode) and **self-train to drive the Open Cowork desktop app**, even **executing human-action tasks** — clicking, typing, opening apps, sending email, e-signing — through GUI/OS automation (CoWork mode). Both modes run a self-optimizing loop that compounds lessons over time, so the agent gets measurably better with use.

```
Your Machine ──► Model Provider (OpenAI / Anthropic / Any OpenAI-compatible API)
     ▲
     │  (no middleman, no cloud backend, no data lock-in)
     │
  Your Code
```

> Reimagined from the ground up. The original 2024 autonomous-dev pipeline is frozen under `v1/` — preserved, not maintained.

---

## 🧬 The Agent Builds Its Own Harness — Live

> **Godcoder doesn't just use a harness. It writes one, improves it, and optimizes it — autonomously, in real time.**

This is the defining capability that sets Godcoder apart. Activate **Harness mode** and the agent takes over its own agent loop: it scaffolds a live sandbox, engineers its own tools and workflows, runs improvement cycles, measures what works, and compounds that knowledge — all without you writing a single prompt.

```
┌─────────────────────────────────────────────────────────────┐
│              HARNESS MODE  —  Real-Time Self-Build          │
│                                                             │
│  START                                                      │
│    │                                                        │
│    ▼                                                        │
│  🏗️  Scaffold  →  creates harness-build/ sandbox            │
│    │                                                        │
│    ▼                                                        │
│  🗺️  Route     →  selects the highest-value next change     │
│    │                                                        │
│    ▼                                                        │
│  📋  Plan      →  designs the improvement                   │
│    │                                                        │
│    ▼                                                        │
│  ⚙️  Execute   →  writes, edits, runs code                  │
│    │                                                        │
│    ▼                                                        │
│  ✅  Evaluate  →  verifies with the project's own checks    │
│    │                                                        │
│    ▼                                                        │
│  📝  Log       →  records outcome in persistent memory      │
│    │                                                        │
│    ▼                                                        │
│  🔁  Optimize  →  biases future iterations toward success   │
│    │                                                        │
│    └──────────────────────────────► repeat                  │
└─────────────────────────────────────────────────────────────┘
```

**How it works:**
- Pick **Harness** in the new-session composer and press start — no prompt to type, no folder to choose.
- The agent instantly creates a dedicated `harness-build/` workspace, opens it in your file explorer, and confines all new work there — reading the rest of the repo for reference but never rewriting it.
- Each iteration makes **one decisive, verifiable change**: keep it if it's an improvement, discard it otherwise.
- Results are stored in a **persistent memory store** (via the ResearchSwarm bridge) so lessons from past runs rank and steer future iterations — the harness compounds knowledge over time.
- Like Freestyle mode, every tool call is auto-approved after the first confirmation.

The loop is powered by the [`self-optimizing-harness`](./crates/agent/default-sk