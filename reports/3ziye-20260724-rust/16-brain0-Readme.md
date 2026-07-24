<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/brain0-wordmark-dark.svg">
  <img alt="brain0" src="docs/assets/brain0-wordmark-light.svg" width="380">
</picture>

<br/>

**The black box for AI-written code.**

`git` tells you *what* changed. brain0 tells you *why*: which prompt wrote it,
what the agent **read** to write it, and whether you can trust it.

[![CI](https://github.com/Brain0-ai/brain0/actions/workflows/ci.yml/badge.svg)](https://github.com/Brain0-ai/brain0/actions/workflows/ci.yml)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](./LICENSE)
[![npm](https://img.shields.io/npm/v/brain0?color=cb3837&logo=npm)](https://www.npmjs.com/package/brain0)
[![Rust](https://img.shields.io/badge/core-Rust-e43717?logo=rust)](./crates)
[![TypeScript](https://img.shields.io/badge/gui-TypeScript-3178c6?logo=typescript&logoColor=white)](./packages)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-27a644.svg)](./CONTRIBUTING.md)

[Quickstart](#quickstart) · [What it answers](#the-questions-your-repo-cant-answer-today) ·
[Give your agent memory](#give-your-agent-the-why-layer-mcp) · [How it works](#how-it-works) ·
[Comparison](#how-it-compares) · [Docs](./docs)

<br/>

<img alt="brain0 — the decision graph of a repository: click any node to read its intent, risk and dated history" src="docs/assets/brain0-demo.gif" width="900">

</div>

---

Coding agents now write most of the diff: continuously, in parallel, and opaquely.
brain0 **passively** builds a decision graph of your repository: every **commit** linked to
the **agent intents** behind it, down to the single **function**, with dated history, drift
detection, a DLP audit of what agents *read*, and a two-dimensional **risk score** rendered
green → red. No hooks, no agent cooperation, no code changes: it reads git and the
transcripts your agents already write to disk.

> Dogfooded from day one: brain0's own development is tracked by brain0.

## Quickstart

```bash
npx brain0 up
```

That's it. From any repo, `up` infers the repo id from your git remote, indexes the git
history (the **facts**), passively ingests your coding-agent sessions (the **intents**,
with Codex and Claude Code auto-discovered), and opens the GUI at `http://localhost:8787`:
an explorable graph of your codebase, from repo to module, file and symbol, where clicking a
commit reveals the prompts behind it, per-file diffs, and risk at a glance.

Then make it a habit:

```bash
brain0 today             # morning triage: what agents did, riskiest first
brain0 report            # the accountability report (add --md to share it)
brain0 query "why did the parser break"   # root-cause debug over the graph
```

## What you need

The only hard requirement is **Node.js ≥ 20**. brain0 is offline-first: with nothing else
installed it still works end to end: deterministic summaries, local feature-hash embeddings,
zero egress. Local models make it *better*, never *required*.

| Piece | Needed for | Without it |
|---|---|---|
| **Node.js ≥ 20** | everything (`npx brain0 up`) | (required) |
| **git** | commit history (the facts side) | filesystem checkpoint mode (`brain0 watch`) |
| **A coding agent**: Codex (`~/.codex`) or Claude Code (`~/.claude/projects`), auto-discovered | the *why* layer: prompts, drift, reads/DLP | graph of commits + code only |
| **[Ollama](https://ollama.com)** + models (below) | model-written summaries · semantic search · GUI smart chat | deterministic summaries · feature-hash embeddings · retrieval-only answers |
| `ANTHROPIC_API_KEY` / `OPENAI_API_KEY` (opt-in) | a hosted LLM for the GUI smart chat | local Ollama (default) |

### Recommended local models

```bash
ollama pull qwen3:4b               # summarizer (default)
ollama pull qwen3-embedding:0.6b   # embeddings (default; nomic-embed-text is the auto-fallback)
```

Both run on modest hardware. On a small GPU (≈4 GB VRAM) use a lighter summarizer for the
first, cache-populating run. Summaries are content-cached in `~/.cache/brain0/`, so every
later rebuild costs zero model calls (and even an interrupted run keeps its work):

```bash
BRAIN0_SUMMARIZER_MODEL=qwen3:1.7b npx brain0 up
```

If a configured model is missing, brain0 tells you exactly what to pull and degrades
gracefully (embedder falls back to `nomic-embed-text`, then local). Every choice is
overridable: `BRAIN0_SUMMARIZER_{PROVIDER,MODEL,ENDPOINT}`, `BRAIN0_EMBED_{PROVIDER,MODEL,ENDPOINT,DIM}`,
`BRAIN0_LLM_PROVIDER`. Details in [`docs/models.md`](./docs/models.md).

## The questions your repo can't answer today

- *Which prompt introduced this bug?*
- *Who (agent or human) touched this function, when, and **why**?*
- *The agent claimed it "changed little." **Did it?***
- *Did any session read `.env` or a private key before pushing code?*
- *This change looked harmless. Did it later prove dangerous?*

brain0 answers all five, by construction. Three of those answers exist nowhere e