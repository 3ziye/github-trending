# grepai

[![Go](https://github.com/yoanbernabeu/grepai/actions/workflows/ci.yml/badge.svg)](https://github.com/yoanbernabeu/grepai/actions/workflows/ci.yml)
[![Go Report Card](https://goreportcard.com/badge/github.com/yoanbernabeu/grepai)](https://goreportcard.com/report/github.com/yoanbernabeu/grepai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**A privacy-first, CLI-native way to semantically search your codebase.**

Search code by *what it does*, not just what it's called. `grepai` indexes the meaning of your code using vector embeddings, enabling natural language queries that find conceptually related code—even when naming conventions vary.

## Why grepai?

`grep` was built in 1973 for exact text matching. Modern codebases need semantic understanding.

|                      | `grep` / `ripgrep`           | `grepai`                          |
|----------------------|------------------------------|-----------------------------------|
| **Search type**      | Exact text / regex           | Semantic understanding            |
| **Query**            | `"func.*Login"`              | `"user authentication flow"`      |
| **Finds**            | Exact pattern matches        | Conceptually related code         |
| **AI Agent context** | Requires many searches       | Fewer, more relevant results      |

### Built for AI Agents

grepai is designed to provide **high-quality context** to AI coding assistants. By returning semantically relevant code chunks, your agents spend less time searching and more time coding.

## Getting Started

### Installation

```bash
curl -sSL https://raw.githubusercontent.com/yoanbernabeu/grepai/main/install.sh | sh
```

Or download from [Releases](https://github.com/yoanbernabeu/grepai/releases).

### Quick Start

```bash
grepai init                        # Initialize in your project
grepai watch                       # Start background indexing daemon
grepai search "error handling"     # Search semantically
grepai trace callers "Login"       # Find who calls a function
```

## Commands

| Command                  | Description                            |
|--------------------------|----------------------------------------|
| `grepai init`            | Initialize grepai in current directory |
| `grepai watch`           | Start real-time file watcher daemon    |
| `grepai search <query>`  | Search codebase with natural language  |
| `grepai trace <cmd>`     | Analyze call graph (callers/callees)   |
| `grepai status`          | Browse index state interactively       |
| `grepai agent-setup`     | Configure AI agents integration        |
| `grepai update`          | Update grepai to the latest version    |

```bash
grepai search "authentication" -n 5       # Limit results (default: 10)
grepai search "authentication" --json     # JSON output for AI agents
grepai search "authentication" --json -c  # Compact JSON (~80% fewer tokens)
```

### Background Daemon

Run the watcher as a background process:

```bash
grepai watch --background    # Start in background
grepai watch --status        # Check if running
grepai watch --stop          # Stop gracefully
```

Logs are stored in OS-specific directories:

| Platform | Log Directory |
|----------|---------------|
| Linux    | `~/.local/state/grepai/logs/` |
| macOS    | `~/Library/Logs/grepai/` |
| Windows  | `%LOCALAPPDATA%\grepai\logs\` |

Use `--log-dir /custom/path` to override (must be passed to all commands):

```bash
grepai watch --background --log-dir /custom/path    # Start in background
grepai watch --status --log-dir /custom/path        # Check if running
grepai watch --stop --log-dir /custom/path          # Stop gracefully
```

### Self-Update

Keep grepai up to date:

```bash
grepai update --check    # Check for available updates
grepai update            # Download and install latest version
grepai update --force    # Force update even if already on latest
```

The update command:
- Fetches the latest release from GitHub
- Verifies checksum integrity
- Replaces the binary automatically
- Works on all supported platforms (Linux, macOS, Windows)

### Call Graph Analysis

Find function relationships in your codebase:

```bash
grepai trace callers "Login"           # Who calls Login?
grepai trace callees "HandleRequest"   # What does HandleRequest call?
grepai trace graph "ProcessOrder" --depth 3  # Full call graph
```

Output as JSON for AI agents:
```bash
grepai trace callers "Login" --json
```

## AI Agent Integration

grepai integrates natively with popular AI coding assistants. Run `grepai agent-setup` to auto-configure.

| Agent        | Configuration File                     |
|--------------|----------------------------------------|
| Cursor       | `.cursorrules`                         |
| Windsurf     | `.windsurfrules`                       |
| Claude Code  | `CLAUDE.md` / `.claude/settings.md`    |
| Gemini CLI   | `GEMINI.md`                            |
| OpenAI Codex | `AGENTS.md` 