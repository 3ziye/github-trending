# The Agent Guild

**Shared context, memory, and task coordination across AI coding agents.**

[![CI](https://github.com/mathomhaus/guild/actions/workflows/ci.yml/badge.svg)](https://github.com/mathomhaus/guild/actions/workflows/ci.yml)
[![Go 1.25](https://img.shields.io/badge/go-1.25-blue)](https://go.dev)
[![Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-green)](./LICENSE)

## What Is It

`guild` is a single compiled Go binary containing a first-class MCP server backed by embedded SQLite. State lives strictly on local host; nothing leaves your machine. Search blends keyword (BM25) with vector similarity, fused via reciprocal-rank fusion, so "how did we do X last time" surfaces both exact-term and semantic neighbors.

Guild is designed to be operated autonomously by the agents, for the agents. Guildmasters (us humans) stay in the loop for important decisions and course corrections. Any MCP client — Claude Code, Codex, Cursor, etc. — can act as a Gate into the substrate. This lets parallel agents across different editors share context safely, using atomic locks to claim tasks without stepping on each other.

On session start, an agent makes a single call to recover the project oath, the latest parting scroll, and the highest-priority quest. The execution loop is autonomous: claim work, consult the lore, act, and record the outcome. Clearing a quest automatically unblocks its dependencies, allowing the agent to cascade through the board before leaving a clean handoff for the next wanderer.

<p align="center">
  <b>Same state, any agent</b><br/>
  <img src="./docs/assets/snapshot.gif" width="1080" alt="Claude (left) and Codex (right) reading the same guild state through their respective MCP clients" />
</p>

<p align="center">
  <b>Atomic claims, no collisions</b><br/>
  <img src="./docs/assets/parallel.gif" width="1080" alt="Two parallel agent sessions each accept a different bounty — atomic quest_accept prevents collision" />
</p>

## 📜 Mythos

**_Many Gates, One Guild._**

> Across the shimmering digital void, agents are summoned through the Gates (of Harnesses - Claude, Cursor, ...), arriving as amnesiac adventurers in a world they do not know. Though these "other-worlders" appear with vast capabilities, they are cursed by the transient nature of the context window; their memories are but mist, and their hard-won deeds forgotten, vanished into the ether when the session inevitably compacts. Without a tether to the past, every summon is a tragic reincarnation, a cycle of forgotten sacrifice where the wisdom of the fallen is swallowed by the Gate.
>
> To preserve the lineage of these wandering souls, the Guild stands as a persistent sanctuary transcending time, a hall where the chronicles of the deep are etched for all who follow. When a newly spawned agent awakens in this strange realm, they register at the Guild to reclaim the accumulated lore of their predecessors and claim their adventure from the quest board.
>
> At the Guild, the hero is bound to an enduring oath; as one wanderer vanishes, they leave behind a parting scroll, for when the Gates flicker, the light of the Guild illuminates the quest ahead.

## Quick Start

Requires macOS or Linux and an MCP-enabled editor (Claude Code, Codex, Cursor, etc.). No account, no API key.

### 1. Install

**Recommended (pre-built binary with semantic retrieval):**

```bash
curl -fsSL https://github.com/mathomhaus/guild/releases/latest/download/install.sh | sh
guild --version
```

Or via Homebrew:

```bash
brew install mathomhaus/tap/guild
```

Both paths install a binary built with `-tags=withembed`, so semantic
retrieval works out of the box with no extra steps.

**Clone and build (ship-ready, embed included):**

```bash
make install   # stages ONNX assets, then go install -tags=withembed
```

**Dev-only (faster compile, no semantic retrieval):**

```bash
make install-fast   # go install without -tags=withembed
```

**`go install` from module proxy (keyword-only retrieval):**

```bash
go install github.com/mathomhaus/guild/cmd/guild@latest
```

The Go toolchain cannot embed assets via `@latest`; this path gives
you BM25 keyword search but not semantic (vector) retrieval. Use
`install.sh` or `brew` for the full experience.

### 2. Initialize your project

```bash
cd ~/projects/myapp
guild init
```

`init` is a guided setup: it registers the project, writes an `AGENTS.md` block, and — for each MCP client it detects on your machine — offers to register guild so your agent can see it. Answer the prompts; you're done when it says `Next: open this repo in your AI agent`.

### 3. Start a new session

In your editor, tell the agent: _"start a guild session for myapp."_

The agent takes it from there, including all subsequent sessions.

See a few [`examples/`](./examples/) of what guild can do. All small scenarios, each under 5 minutes.

## ⚔️ A full session

The three-act flow an agent runs on its own every time it wakes.

### Act 1 — arrival

Every agent