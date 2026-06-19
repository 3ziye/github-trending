<div align="center">

# Vigils

### A local-first control plane for AI agents — see what they do, approve what matters, keep secrets out.

[![CI](https://github.com/duncatzat/vigils/actions/workflows/ci.yml/badge.svg)](https://github.com/duncatzat/vigils/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/duncatzat/vigils?sort=semver&color=blue)](https://github.com/duncatzat/vigils/releases)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](./LICENSE)
[![Platforms](https://img.shields.io/badge/platforms-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](#installation)

[Website](https://vigils.ai) · [▶ Watch the 20s demo](https://duncatzat.github.io/vigils/demo.html) · [Quick Start](#quick-start) · [Architecture](#architecture) · [Security Model](#security-model) · [Documentation](#documentation)

**English** | [简体中文](./README.zh-CN.md)

</div>

---

AI agents (Claude Code, Cursor, Zed, MCP clients, browser assistants) call tools, read
files, hit APIs, and paste into web UIs on your behalf. That power is useful — and risky.
**Vigils sits between your agents and the tools/data they touch**, and it is *local-first*:
your prompts, secrets, and audit trail never leave your machine.

```
   AI agent ──▶  ┌─────────────────── Vigils ───────────────────┐  ──▶  tools / data
 (MCP client)    │  redact → firewall → approve → sandbox → audit │       (MCP servers,
                 └───────────────────────────────────────────────┘        files, APIs, web)
```

## Why Vigils

Four guarantees, enforced locally:

| Guarantee | How |
|---|---|
| **See what the agent did** | Every tool call is recorded in a tamper-evident **SHA-256 hash-chained ledger** with full-text search. |
| **Approve risky actions first** | Destructive / sensitive calls pause for human review in an **Approval Queue**, with per-agent policy and scoped grants. |
| **Keep credentials out of prompts / logs / UI** | A **redaction engine** strips secrets and PII (hard-fingerprint rules + an optional ML ensemble) *before* text reaches a model, a log, or the screen. |
| **Contain & roll back** | The ledger is traceable end-to-end and the **sandbox runner is fail-closed by default** (Wasm + native + Linux Landlock). |

## Features

- **🔒 Tamper-evident audit ledger** — SQLite + SHA-256 hash chain; every event links to the
  previous one, so tampering is detectable. FTS5 full-text search over the redacted trail.
- **🛡️ Default-deny firewall** — tool calls are gated by a Rust policy DSL; per-agent rules;
  OAuth scope allow-lists for remote MCP. Nothing runs unless allowed.
- **✅ Human-in-the-loop approval** — risky effects (file writes, network, destructive ops)
  pause for review. Grants can be scoped (once / this-session).
- **🙈 Secret & PII redaction** — hard-fingerprint detection for 13+ credential classes
  (GitHub PAT, Stripe keys, Google/GitLab tokens, DB URLs, …) plus an optional multilingual
  ML ensemble; a fail-closed merge layer decides what to mask.
- **🎟️ Secret lease broker** — short-lived credential leases injected only into the child
  process that needs them; plaintext is never persisted.
- **📦 Sandbox runner** — one-shot tool execution in Wasm (Wasmtime) or native processes,
  with **Linux Landlock LSM** filesystem isolation and `env_clear` so children don't inherit
  your environment. Fail-closed by default.
- **🔌 MCP gateway** — sits in front of MCP servers over **stdio and HTTP**; descriptor
  pinning with drift detection (alerts when a tool's definition changes); bare-command stdio
  upstreams (`npx`/`node`/`python`) resolve via host PATH before sandboxing.
- **🖥️ Desktop app** (Tauri 2 + Vue 3) — Approval Queue, Activity Feed, Server Registry,
  Session Replay, Privacy Findings; keyboard shortcuts, light/dark/system theme, real-time
  updates, bilingual (zh / en) UI.
- **🌐 Browser extension** (Chrome MV3) — redacts secrets/PII *before* paste or submit on AI
  sites (ChatGPT, Claude, Gemini, Perplexity).

## Architecture

Vigils is a Rust workspace of focused crates plus three apps. Each layer is independently
testable and composed by the **Hub** (the MCP gateway).

| Layer | Crate | Responsibility |
|---|---|---|
| **Audit** | `vigil-audit` | SQLite ledger, SHA-256 hash chain, FTS5 search, redaction-scan records |
| **Policy** | `vigil-policy` | Rust policy DSL + rule engine (default-deny) |
| **Firewall** | `vigil-firewall` | Tool gating, per-agent rules, OAuth scope allow-lists |
| **Approval** | `vigil-mcp` (broker) | Human-in-the-loop, scoped grants, cross-process resolution |
| **Redaction** | `vigil-redaction` | Secret/PII detection (hard fingerprints + ML ensemble), fail-closed merge |
| **Leases** | `vigil-lease` | Short-lived credential leases, prepared child env (RAII revoke) |
| **Runner** | `vigil-runner` / `vigil-runner-types` | Native + Wasm execution, env policy, fail-closed |
| **Sandbox** | `vigil-sandbox-linux` | Linux Landlock LSM filesystem isolation |
| **Gat