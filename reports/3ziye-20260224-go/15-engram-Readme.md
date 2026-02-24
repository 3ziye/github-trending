<p align="center">
  <img width="1024" height="340" alt="image" src="https://github.com/user-attachments/assets/32ed8985-841d-49c3-81f7-2aabc7c7c564" />
</p>

<p align="center">
  <strong>Persistent memory for AI coding agents</strong><br>
  <em>Agent-agnostic. Single binary. Zero dependencies.</em>
</p>

<p align="center">
  <a href="#quick-start">Quick Start</a> &bull;
  <a href="#how-it-works">How It Works</a> &bull;
  <a href="#agent-setup">Agent Setup</a> &bull;
  <a href="CONTRIBUTING.md">Contributing</a> &bull;
  <a href="#why-not-claude-mem">Why Not claude-mem?</a> &bull;
  <a href="#tui">Terminal UI</a> &bull;
  <a href="DOCS.md">Full Docs</a>
</p>

---

> **engram** `/ˈen.ɡræm/` — *neuroscience*: the physical trace of a memory in the brain.

Your AI coding agent forgets everything when the session ends. Engram gives it a brain.

A **Go binary** with SQLite + FTS5 full-text search, exposed via CLI, HTTP API, MCP server, and an interactive TUI. Works with **any agent** that supports MCP — OpenCode, Claude Code, Cursor, Windsurf, or anything else.

```
Agent (OpenCode / Claude Code / Cursor / Windsurf / ...)
    ↓ MCP stdio
Engram (single Go binary)
    ↓
SQLite + FTS5 (~/.engram/engram.db)
```

## Quick Start

### Install via Homebrew (recommended)

```bash
brew install gentleman-programming/tap/engram
```

Upgrade to latest:

```bash
brew update && brew upgrade engram
```

> **Migrating from Cask?** If you installed engram before v1.0.1, it was distributed as a Cask. Uninstall first, then reinstall:
> ```bash
> brew uninstall --cask engram 2>/dev/null; brew install gentleman-programming/tap/engram
> ```

### Install from source

```bash
git clone https://github.com/Gentleman-Programming/engram.git
cd engram
go install ./cmd/engram
```

### Download binary

Grab the latest release for your platform from [GitHub Releases](https://github.com/Gentleman-Programming/engram/releases).

Then set up your agent's plugin:

```bash
# Claude Code — via marketplace
claude plugin marketplace add Gentleman-Programming/engram
claude plugin install engram

# OpenCode — via engram setup
engram setup opencode

# Gemini CLI — MCP auto-registration
engram setup gemini-cli

# Codex — MCP auto-registration
engram setup codex

# Or interactive (asks which agent)
engram setup
```

See [Agent Setup](#agent-setup) for manual configuration or other agents (Cursor, Windsurf, Gemini, Codex).

That's it. No Node.js, no Python, no Bun, no Docker, no ChromaDB, no vector database, no worker processes. **One binary, one SQLite file.**

## How It Works

<p align="center">
  <img src="assets/agent-save.png" alt="Agent saving a memory via mem_save" width="800" />
  <br />
  <em>The agent proactively calls <code>mem_save</code> after significant work — structured, searchable, no noise.</em>
</p>

Engram trusts the **agent** to decide what's worth remembering — not a firehose of raw tool calls.

### The Agent Saves, Engram Stores

```
1. Agent completes significant work (bugfix, architecture decision, etc.)
2. Agent calls mem_save with a structured summary:
   - title: "Fixed N+1 query in user list"
   - type: "bugfix"
   - content: What/Why/Where/Learned format
3. Engram persists to SQLite with FTS5 indexing
4. Next session: agent searches memory, gets relevant context
```

### Session Lifecycle

```
Session starts → Agent works → Agent saves memories proactively
                                    ↓
Session ends → Agent writes session summary (Goal/Discoveries/Accomplished/Files)
                                    ↓
Next session starts → Previous session context is injected automatically
```

### 13 MCP Tools

| Tool | Purpose |
|------|---------|
| `mem_save` | Save a structured observation (decision, bugfix, pattern, etc.) |
| `mem_update` | Update an existing observation by ID |
| `mem_delete` | Delete an observation (soft-delete by default, hard-delete optional) |
| `mem_suggest_topic_key` | Suggest a stable `topic_key` for evolving topics before saving |
| `mem_search` | Full-text search across all memories |
| `mem_session_summary` | Save end-of-session summary |
| `mem_context` | Get recent context from previous sessions |
| `mem_timeline` | Chronological context around a specific observation |
| `mem_get_observation` | Get full content of a specific memory |
| `mem_save_prompt` | Save a user prompt for future context |
| `mem_stats` | Memory system statistics |
| `mem_session_start` | Register a session start |
| `mem_session_end` | Mark a session as completed |

### Progressive Disclosure (3-Layer Pattern)

Token-efficient memory retrieval — don't dump everything, drill in:

```
1. mem_search "auth middleware"     → compact results with IDs (~100 tokens each)
2. mem_timeline observation_id=42  → what happened before/after in that session
3. mem_get_observation id=42       → full untruncated content
```

### Memory Hygiene

- `mem_save` now supports `scope` (`project` default, `personal` optional)
- `mem_save` also supports `to