<div align="center">

<img src="https://crew44.io/brand/mark44-rust-512.png" alt="Crew44" width="96" height="96" />

# Crew44

### A local-first orchestrator for running specialist AI agents on your own machine.

[![CI](https://github.com/getcrew44/crew44/actions/workflows/ci.yml/badge.svg)](https://github.com/getcrew44/crew44/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-c4644a.svg)](LICENSE)
![Platforms](https://img.shields.io/badge/platforms-macOS%20·%20Windows%20·%20Linux-1c1a17)
![Free](https://img.shields.io/badge/price-free-5b9c5f.svg)


[**Download**](https://crew44.io/download) · [Website](https://crew44.io) · [What's new](CHANGELOG.md)


<a href="https://www.producthunt.com/products/crew44?embed=true&amp;utm_source=badge-featured&amp;utm_medium=badge&amp;utm_campaign=badge-crew44" target="_blank" rel="noopener noreferrer"><img alt="Crew44 - Turn coding agents into specialist teams | Product Hunt" width="250" height="54" src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=1156940&amp;theme=light&amp;t=1779982023946"></a>
</div>


---

Crew44 turns the AI agents you already run — Claude Code, Codex, Gemini, Cursor, and more — into a coordinated team. Instead of one generalist agent re-explaining context to itself all day, you assemble specialists, bind each to the model that wins at its job, and let them hand work off to each other inside one shared workspace.

Everything runs on your machine. State is plain files under `~/.crew44/`. No cloud account, no subscription, no telemetry — the only network traffic is whatever your underlying coding agent already makes.

https://github.com/user-attachments/assets/ce6e5293-6c58-4c37-8e00-74d654d2277c

## Download

Grab a signed desktop build for your platform — **free, no account required:**

| Platform | Format |
|----------|--------|
| **macOS** (Apple Silicon) | `.dmg` |
| **Windows** (x64) | `.exe` installer |
| **Linux** (ARM64) | `.AppImage` / `.deb` |

→ **[crew44.io/download](https://crew44.io/download)**

Prefer to build it yourself? See [Getting started](#getting-started).

## Why Crew44

| The old way — one agent | With Crew44 — a crew of specialists |
|-------------------------|----------------------|
| A new contractor every morning: never seen your repo, never learned your conventions. | **Per-project memory.** Monday's fix is in the crew's muscle memory by Thursday. |
| Skills never compound — whatever it figured out is gone by next task. | **Skills that compound.** Capture a workflow once as `SKILL.md`; every agent you attach it to gets it on every turn, across providers. |
| One generalist plans, builds, and reviews — no deep expertise in any role. | **Specialists in parallel.** Planner drafts while builder codes while reviewer checks. Handovers ship the baton, not the whole context. |
| Locked to a single model: pays Opus rates for a rename, runs a fast model on a hard call. | **The right model per role.** Opus plans, GPT-5.5 codes, a local model reviews — swap per task, not per app. |




## Supported runtimes

Crew44 detects and routes to any of these installed on your machine:

**Claude Code · Codex · Cursor Agent · Gemini CLI · Hermes · Kimi · OpenCode · OpenClaw · Pi · Qoder · Qwen Code**

The same skills folder runs across every provider, so you're never locked in. Have another CLI? The runtime layer is a small Go interface — add an adapter under `daemon/internal/backendagent/` and it shows up in the picker.

## Core concepts

| Concept   | What it is                                                                                              |
|-----------|---------------------------------------------------------------------------------------------------------|
| Runtime   | A coding-agent CLI on disk (Claude, Codex, Cursor, …) discovered by scanning.                           |
| Agent     | A named persona bound to one runtime + model, with an instruction and attached skills.                  |
| Skill     | A file-based capability (`SKILL.md` + assets) injected into the runtime session when its agent runs.    |
| Project   | A working directory plus the chats that belong to it. Stored under `Documents/Crew44/` or a folder you pick. |
| Chat      | A turn-by-turn thread. One in-flight response at a time; events are an append-only `events.jsonl`.      |
| Worktree  | An optional isolated git checkout for a chat. Toggle it on a new task and the crew works on its own `crew/…` branch without touching your working tree. |
| Handover  | A marker an agent emits to pass the turn to a teammate, with a one-line brief.                          |

The default crew ships with a **Partner**, an **Engineer**, a **Product Lead**, and a **Designer** — each owning a role, a model, and its own skills folder.

## How it works

```
┌─────────────────┐  WebSocket JSON-RPC   ┌──────────────────┐    spawn    ┌─────────────────┐
│  Electron / UI  │ ◄───────────────────► │   Go daemon      │ ───