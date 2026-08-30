# FuXi

[English](README.md) | [简体中文](README.zh-CN.md)

[![GitHub stars](https://img.shields.io/github/stars/fuxicodex/Fuxi?style=flat-square&color=0a6fe7&label=stars)](https://github.com/fuxicodex/Fuxi/stargazers)
[![Release](https://img.shields.io/github/v/release/fuxicodex/Fuxi?style=flat-square&color=0a6fe7&label=release)](https://github.com/fuxicodex/Fuxi/releases)
[![Last commit](https://img.shields.io/github/last-commit/fuxicodex/Fuxi?style=flat-square&color=0a6fe7)](https://github.com/fuxicodex/Fuxi/commits/main)
[![License](https://img.shields.io/badge/license-Proprietary-0a6fe7?style=flat-square)](LICENSE)

> **An AI coding agent that lives in your terminal.**

FuXi is a fast, self-contained **terminal AI coding agent** — read code, edit
files, run commands, and drive tools from a rich TUI, with cost-aware routing
across LLM providers and automatic failover. Built in Go, it ships as one
static binary with no runtime dependencies. Think of it as a provider-agnostic
alternative to Claude Code: bring any OpenAI-compatible model and get an
agentic Think → Act → Verify loop on top of it.

**Terminal-first** · **Provider-agnostic** · **Bring your own key** · **MCP client** · **Self-updating**

Homepage: **https://www.fuxicode.com**

```bash
curl -fsSL https://releases.fuxicode.com/bootstrap.sh | bash   # install
fuxi                                                        # start
```

![FuXi in action](docs/fuxi-demo.gif)

---

### What FuXi does

Its agentic **Think → Act → Verify** loop and intelligent routing let any
OpenAPI-compatible model perform above its raw benchmark — verified against
another coding agent on a reproducible task set (see
[benchmark](benchmark/REPORT.md)).

---
## Contents

- [Highlights](#highlights)
- [How FuXi compares](#how-fuxi-compares)
- [Evaluation & benchmarks](#evaluation--benchmarks)
- [Install](#install)
- [Getting started](#getting-started)
- [Usage guide](docs/usage.md)
- [Keyboard shortcuts](docs/keybindings.md)
- [FAQ](docs/faq.md)
- [Security & privacy](security-privacy/README.md)
- [Changelog](CHANGELOG.md)
- [Support](SUPPORT.md)
- [Project layout](#project-layout)
- [License](#license)

## Highlights

**The model is the engine. FuXi is the vehicle.** A model alone answers
questions; FuXi turns it into a worker — reasoning, acting on your real
codebase, verifying results, and doing it affordably and under your control.

![FuXi architecture](docs/architecture.png)

![Think → Act → Verify loop](docs/loop.png)

![Intelligent routing](docs/routing.png)

![Elevating any model's capability](docs/elevation.png)

- **50+ built-in tools** — file read/write/edit, shell (`bash` / PowerShell),
  ripgrep search, web fetch, LSP diagnostics, Jupyter, browser use, background
  tasks, and parallel sub-agents — all in one binary.
- **Safety guardrails** — shell commands pass an AST safety classifier before
  execution; fine-grained permissions and audit logging keep autonomous work
  under your control.
- **Durable sessions & memory** — transcripts persist to disk; checkpoints let
  you resume, roll back, or fork; idle "dreaming" consolidates memory across
  sessions; long conversations auto-compact to save tokens.
- **Bring your own key, or log in** — any provider API key (OpenAPI-compatible,
  Gemini, Bedrock/Vertex), or sign in with FuXi OAuth.
- **Extensible** — MCP client, hooks, skills, plugins, and slash commands, all
  hot-reloadable.
- **Free forever** — one static binary, no runtime dependencies, no license
  cost for individuals, teams, or enterprises.
- **Self-updating** — a background version check and one-command `fuxi update`,
  with checksum verification before it replaces the running binary.

---

## How FuXi compares

FuXi is a terminal-first AI coding agent designed to be provider-agnostic.
Feature availability reflects each product's publicly documented positioning
as of mid-2026; details evolve quickly, so treat it as an orientation.

### Measured head-to-head

![FuXi vs Claude Code head-to-head](docs/headtohead.png)

Both systems were driven through their own native clients, on identical
baselines and the same objective scorer (pytest + coverage), across 15 micro
dimensions and 4 large-project dimensions. Full methodology, raw results,
environment versions, exact commands, and known limitations are in
[`benchmark/REPORT.md`](benchmark/REPORT.md) so you can verify or re-run it.

> An honest caveat: this is a small, self-run task set — not a third-party
> benchmark — and it measures the *agent loop*, not raw model scores. Treat it
> as a data point, not a headline.

---

## Evaluation & benchmarks

FuXi is built to be measured honestly. It currently ships without a published
score on third-party benchmarks (e.g. SWE-bench, Terminal-Bench, or the Aider
polyglot benchmark). We prefer reproducible, self-verifiable evaluation over
headline numbers — so here is how to evaluate FuXi yourself, on your own work.

**A practical evaluation checklist**

1. **Install & s