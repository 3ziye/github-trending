# Context Mode

**The other half of the context problem.**

[![users](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fmksglu%2Fclaude-context-mode%40main%2Fstats.json&query=%24.message&label=users&color=brightgreen)](https://www.npmjs.com/package/context-mode) [![npm](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fmksglu%2Fclaude-context-mode%40main%2Fstats.json&query=%24.npm&label=npm&color=blue)](https://www.npmjs.com/package/context-mode) [![marketplace](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fmksglu%2Fclaude-context-mode%40main%2Fstats.json&query=%24.marketplace&label=marketplace&color=blue)](https://github.com/mksglu/claude-context-mode) [![GitHub stars](https://img.shields.io/github/stars/mksglu/claude-context-mode?style=flat&color=yellow)](https://github.com/mksglu/claude-context-mode/stargazers) [![GitHub forks](https://img.shields.io/github/forks/mksglu/claude-context-mode?style=flat&color=blue)](https://github.com/mksglu/claude-context-mode/network/members) [![Last commit](https://img.shields.io/github/last-commit/mksglu/claude-context-mode?color=green)](https://github.com/mksglu/claude-context-mode/commits) [![License: ELv2](https://img.shields.io/badge/License-ELv2-blue.svg)](LICENSE)
[![Discord](https://img.shields.io/discord/1478479412700909750?label=Discord&logo=discord&color=5865f2)](https://discord.gg/DCN9jUgN5v)

Every MCP tool call in Claude Code dumps raw data into your 200K context window. A Playwright snapshot costs 56 KB. Twenty GitHub issues cost 59 KB. One access log — 45 KB. After 30 minutes, 40% of your context is gone.

Inspired by Cloudflare's [Code Mode](https://blog.cloudflare.com/code-mode-mcp/) — which compresses tool definitions from millions of tokens into ~1,000 — we asked: what about the other direction?

Context Mode is an MCP server that sits between Claude Code and these outputs. **315 KB becomes 5.4 KB. 98% reduction.**

https://github.com/user-attachments/assets/07013dbf-07c0-4ef1-974a-33ea1207637b

## Install

```bash
/plugin marketplace add mksglu/claude-context-mode
/plugin install context-mode@claude-context-mode
```

Restart Claude Code. Done. This installs the MCP server + a PreToolUse hook that automatically routes tool outputs through the sandbox + slash commands for diagnostics and upgrades.

| Command | What it does |
|---|---|
| `/context-mode:ctx-stats` | Show context savings for the current session — per-tool breakdown, tokens consumed, savings ratio. |
| `/context-mode:ctx-doctor` | Run diagnostics — checks runtimes, hooks, FTS5, plugin registration, npm and marketplace versions. |
| `/context-mode:ctx-upgrade` | Pull latest from GitHub, rebuild, migrate cache, fix hooks. |

<details>
<summary><strong>MCP-only install</strong> (no hooks or slash commands)</summary>

```bash
claude mcp add context-mode -- npx -y context-mode
```

</details>

<details>
<summary><strong>Local development</strong></summary>

```bash
claude --plugin-dir ./path/to/context-mode
```

</details>

## The Problem

MCP has become the standard way for AI agents to use external tools. But there is a tension at its core: every tool interaction fills the context window from both sides — definitions on the way in, raw output on the way out.

With [81+ tools active, 143K tokens (72%) get consumed before your first message](https://scottspence.com/posts/optimising-mcp-server-context-usage-in-claude-code). And then the tools start returning data. A single Playwright snapshot burns 56 KB. A `gh issue list` dumps 59 KB. Run a test suite, read a log file, fetch documentation — each response eats into what remains.

Code Mode showed that tool definitions can be compressed by 99.9%. Context Mode applies the same principle to tool outputs — processing them in sandboxes so only summaries reach the model.

## Tools

| Tool | What it does | Context saved |
|---|---|---|
| `batch_execute` | Run multiple commands + search multiple queries in ONE call. | 986 KB → 62 KB |
| `execute` | Run code in 10 languages. Only stdout enters context. | 56 KB → 299 B |
| `execute_file` | Process files in sandbox. Raw content never leaves. | 45 KB → 155 B |
| `index` | Chunk markdown into FTS5 with BM25 ranking. | 60 KB → 40 B |
| `search` | Query indexed content with multiple queries in one call. | On-demand retrieval |
| `fetch_and_index` | Fetch URL, detect content type (HTML/JSON/text), chunk and index. | 60 KB → 40 B |

## How the Sandbox Works

Each `execute` call spawns an isolated subprocess with its own process boundary. Scripts can't access each other's memory or state. The subprocess runs your code, captures stdout, and only that stdout enters the conversation context. The raw data — log files, API responses, snapshots — never leaves the sandbox.

Eleven language runtimes are available: JavaScript, TypeScript, Python, Shell, Ruby, Go, Rust, PHP, Perl, R, and Elixir. Bun is auto-detected fo