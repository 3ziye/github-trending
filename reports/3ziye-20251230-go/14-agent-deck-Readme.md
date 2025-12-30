<div align="center">

<!-- Status Grid Logo -->
<img src="site/logo.svg" alt="Agent Deck Logo" width="120">

# Agent Deck

**Your AI agent command center**

[![GitHub Stars](https://img.shields.io/github/stars/asheshgoplani/agent-deck?style=for-the-badge&logo=github&color=yellow&labelColor=1a1b26)](https://github.com/asheshgoplani/agent-deck/stargazers)
[![Go Version](https://img.shields.io/badge/Go-1.24+-00ADD8?style=for-the-badge&logo=go&labelColor=1a1b26)](https://go.dev)
[![License](https://img.shields.io/badge/License-MIT-9ece6a?style=for-the-badge&labelColor=1a1b26)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-macOS%20%7C%20Linux%20%7C%20WSL-7aa2f7?style=for-the-badge&labelColor=1a1b26)](https://github.com/asheshgoplani/agent-deck)
[![Latest Release](https://img.shields.io/github/v/release/asheshgoplani/agent-deck?style=for-the-badge&color=e0af68&labelColor=1a1b26)](https://github.com/asheshgoplani/agent-deck/releases)

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [CLI Commands](#cli-commands) • [Documentation](#documentation)

</div>

---

https://github.com/user-attachments/assets/e4f55917-435c-45ba-92cc-89737d0d1401

## The Problem

Running Claude Code on 10 projects? OpenCode on 5 more? Another agent somewhere in the background?

**Managing multiple AI sessions gets messy fast.** Too many terminal tabs. Hard to track what's running, what's waiting, what's done. Switching between projects means hunting through windows.

## The Solution

**Agent Deck is mission control for your AI coding agents.**

One terminal. All your agents. Complete visibility.

- 🎯 **See everything at a glance** - Running, waiting, or idle - know the status of every agent instantly
- ⚡ **Switch in milliseconds** - Jump between any session with a single keystroke
- 🔍 **Never lose track** - Search across all conversations, filter by status, find anything in seconds
- 🌳 **Stay organized** - Group sessions by project, client, or experiment with collapsible hierarchies
- 🔌 **Zero config switching** - Built on tmux - sessions persist through disconnects and reboots

## Features

### 🍴 Explore Multiple Solutions in Parallel

**Try different approaches without losing context.** Fork any Claude conversation instantly. Each fork inherits the full conversation history - perfect for comparing solutions or experimenting without risk.

![Fork Session Demo](demos/fork-session.gif)

- Press `f` for quick fork, `F` to customize name/group
- Fork your forks - explore as many branches as you need
- Session IDs auto-detected even after restarts

**Why this matters:** Ever wished you could try two different approaches to the same problem? Now you can. Fork, experiment, compare results, keep what works.

### 🔌 Add Superpowers On-Demand

**Attach MCP servers without touching config files.** Need web search? Browser automation? GitHub integration? Toggle them on per project or globally - Agent Deck handles the restart automatically.

https://github.com/user-attachments/assets/6a4af5ba-bacb-4234-ac72-a019d424d593

- Press `M` to open, `Space` to toggle any MCP server
- **LOCAL** scope (just this project) or **GLOBAL** (everywhere)
- Session auto-restarts with new capabilities loaded

**Why this matters:** Stop editing TOML files. Stop remembering restart commands. Just toggle what you need - Agent Deck takes care of the rest.

**Adding Available MCPs:**

Define your MCPs once in `~/.agent-deck/config.toml`, then toggle them per project:

```toml
# Web search
[mcps.exa]
command = "npx"
args = ["-y", "exa-mcp-server"]
env = { EXA_API_KEY = "your-api-key" }
description = "Web search via Exa AI"

# GitHub integration
[mcps.github]
command = "npx"
args = ["-y", "@modelcontextprotocol/server-github"]
env = { GITHUB_PERSONAL_ACCESS_TOKEN = "ghp_your_token" }
description = "GitHub repos, issues, PRs"

# Browser automation
[mcps.playwright]
command = "npx"
args = ["-y", "@playwright/mcp@latest"]
description = "Browser automation & testing"

# Memory across sessions
[mcps.memory]
command = "npx"
args = ["-y", "@modelcontextprotocol/server-memory"]
description = "Persistent memory via knowledge graph"
```

<details>
<summary>More MCP examples</summary>

```toml
# YouTube transcripts
[mcps.youtube-transcript]
command = "npx"
args = ["-y", "@kimtaeyoon83/mcp-server-youtube-transcript"]
description = "Get YouTube transcripts"

# Web scraping
[mcps.firecrawl]
command = "npx"
args = ["-y", "firecrawl-mcp"]
env = { FIRECRAWL_API_KEY = "your-key" }
description = "Web scraping and crawling"

# Notion
[mcps.notion]
command = "npx"
args = ["-y", "@notionhq/notion-mcp-server"]
env = { NOTION_TOKEN = "your-token" }
description = "Notion workspace access"

# Sequential thinking
[mcps.sequential-thinking]
command = "npx"
args = ["-y", "@modelcontextprotocol/server-sequential-thinking"]
description = "Step-by-step reasoning"

# Context7 - code docs
[mcps.context7]
command = "npx"
args = ["-y", "@upstash/context7-mcp@latest"]
descrip