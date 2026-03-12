# Context Mode

**The other half of the context problem.**

[![users](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fmksglu%2Fcontext-mode%40main%2Fstats.json&query=%24.message&label=users&color=brightgreen)](https://www.npmjs.com/package/context-mode) [![npm](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fmksglu%2Fcontext-mode%40main%2Fstats.json&query=%24.npm&label=npm&color=blue)](https://www.npmjs.com/package/context-mode) [![marketplace](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fmksglu%2Fcontext-mode%40main%2Fstats.json&query=%24.marketplace&label=marketplace&color=blue)](https://github.com/mksglu/context-mode) [![GitHub stars](https://img.shields.io/github/stars/mksglu/context-mode?style=flat&color=yellow)](https://github.com/mksglu/context-mode/stargazers) [![GitHub forks](https://img.shields.io/github/forks/mksglu/context-mode?style=flat&color=blue)](https://github.com/mksglu/context-mode/network/members) [![Last commit](https://img.shields.io/github/last-commit/mksglu/context-mode?color=green)](https://github.com/mksglu/context-mode/commits) [![License: ELv2](https://img.shields.io/badge/License-ELv2-blue.svg)](LICENSE)
[![Discord](https://img.shields.io/discord/1478479412700909750?label=Discord&logo=discord&color=5865f2)](https://discord.gg/DCN9jUgN5v)

## The Problem

Every MCP tool call dumps raw data into your context window. A Playwright snapshot costs 56 KB. Twenty GitHub issues cost 59 KB. One access log — 45 KB. After 30 minutes, 40% of your context is gone. And when the agent compacts the conversation to free space, it forgets which files it was editing, what tasks are in progress, and what you last asked for.

Context Mode is an MCP server that solves both halves of this problem:

1. **Context Saving** — Sandbox tools keep raw data out of the context window. 315 KB becomes 5.4 KB. 98% reduction.
2. **Session Continuity** — Every file edit, git operation, task, error, and user decision is tracked in SQLite. When the conversation compacts, context-mode doesn't dump this data back into context — it indexes events into FTS5 and retrieves only what's relevant via BM25 search. The model picks up exactly where you left off. If you don't `--continue`, previous session data is deleted immediately — a fresh session means a clean slate.

https://github.com/user-attachments/assets/07013dbf-07c0-4ef1-974a-33ea1207637b

## Install

<details open>
<summary><strong>Claude Code</strong></summary>

**Step 1 — Install the plugin:**

```bash
/plugin marketplace add mksglu/context-mode
/plugin install context-mode@context-mode
```

**Step 2 — Restart Claude Code.**

That's it. The plugin installs everything automatically:
- MCP server with 6 sandbox tools (`ctx_batch_execute`, `ctx_execute`, `ctx_execute_file`, `ctx_index`, `ctx_search`, `ctx_fetch_and_index`)
- PreToolUse hooks that intercept Bash, Read, WebFetch, Grep, and Task calls — nudging them toward sandbox execution
- PostToolUse, PreCompact, and SessionStart hooks for session tracking and context injection
- A `CLAUDE.md` routing instructions file auto-created in your project root
- Slash commands for diagnostics and upgrades (Claude Code only)

| Command | What it does |
|---|---|
| `/context-mode:ctx-stats` | Context savings — per-tool breakdown, tokens consumed, savings ratio. |
| `/context-mode:ctx-doctor` | Diagnostics — runtimes, hooks, FTS5, plugin registration, versions. |
| `/context-mode:ctx-upgrade` | Pull latest, rebuild, migrate cache, fix hooks. |

> **Note:** Slash commands are a Claude Code plugin feature. On other platforms, all three utility commands (`ctx stats`, `ctx doctor`, `ctx upgrade`) work as MCP tools — just type the command name and the model will invoke it. See [Utility Commands](#utility-commands).

**Alternative — MCP-only install** (no hooks or slash commands):

```bash
claude mcp add context-mode -- npx -y context-mode
```

This gives you the 6 sandbox tools but without automatic routing. The model can still use them — it just won't be nudged to prefer them over raw Bash/Read/WebFetch. Good for trying it out before committing to the full plugin.

</details>

<details>
<summary><strong>Gemini CLI</strong> <sup>(Beta)</sup></summary>

**Step 1 — Install globally:**

```bash
npm install -g context-mode
```

**Step 2 — Register the MCP server.** Add to `~/.gemini/settings.json`:

```json
{
  "mcpServers": {
    "context-mode": {
      "command": "context-mode"
    }
  }
}
```

**Step 3 — Add hooks.** Without hooks, the model can ignore routing instructions and dump raw output into your context window. Hooks intercept every tool call and enforce sandbox routing programmatically — blocking `curl`, `wget`, and other data-heavy commands before they execute. Add to the same `~/.gemini/settings.json`:

```json
{
  "hooks": {
    "BeforeTool": [
      {
        "matcher": "",
        "hooks": [{ "type": "command",