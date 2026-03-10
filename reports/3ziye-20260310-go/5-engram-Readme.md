<p align="center">
  <img width="1024" height="340" alt="image" src="https://github.com/user-attachments/assets/32ed8985-841d-49c3-81f7-2aabc7c7c564" />
</p>

<p align="center">
  <strong>Persistent memory for AI coding agents</strong><br>
  <em>Agent-agnostic. Single binary. Zero dependencies.</em>
</p>

<p align="center">
  <a href="#quick-start">Quick Start</a> &bull;
  <a href="#install-on-windows">Windows</a> &bull;
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

A **Go binary** with SQLite + FTS5 full-text search, exposed via CLI, HTTP API, MCP server, and an interactive TUI. Works with **any agent** that supports MCP — Claude Code, OpenCode, Gemini CLI, Codex, VS Code (Copilot), Antigravity, Cursor, Windsurf, or anything else.

```
Agent (Claude Code / OpenCode / Gemini CLI / Codex / VS Code / Antigravity / ...)
    ↓ MCP stdio
Engram (single Go binary)
    ↓
SQLite + FTS5 (~/.engram/engram.db)
```

## Quick Start

### Install via Homebrew (macOS / Linux)

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

### Install on Windows

**Option A: Download the binary (recommended)**

1. Go to [GitHub Releases](https://github.com/Gentleman-Programming/engram/releases)
2. Download `engram_<version>_windows_amd64.zip` (or `arm64` for ARM devices)
3. Extract `engram.exe` to a folder in your `PATH` (e.g. `C:\Users\<you>\bin\`)

```powershell
# Example: extract and add to PATH (PowerShell)
Expand-Archive engram_*_windows_amd64.zip -DestinationPath "$env:USERPROFILE\bin"
# Add to PATH permanently (run once):
[Environment]::SetEnvironmentVariable("Path", "$env:USERPROFILE\bin;" + [Environment]::GetEnvironmentVariable("Path", "User"), "User")
```

**Option B: Install from source**

```powershell
git clone https://github.com/Gentleman-Programming/engram.git
cd engram
go install ./cmd/engram
# Binary goes to %GOPATH%\bin\engram.exe (typically %USERPROFILE%\go\bin\)

# Optional: build with version stamp (otherwise `engram version` shows "dev")
$v = git describe --tags --always
go build -ldflags="-X main.version=local-$v" -o engram.exe ./cmd/engram
```

> **Windows notes:**
> - Data is stored in `%USERPROFILE%\.engram\engram.db`
> - Override with `ENGRAM_DATA_DIR` environment variable
> - All core features work natively: CLI, MCP server, TUI, HTTP API, Git Sync
> - No WSL required for the core binary — it's a native Windows executable

### Install from source (macOS / Linux)

```bash
git clone https://github.com/Gentleman-Programming/engram.git
cd engram
go install ./cmd/engram

# Optional: build with version stamp (otherwise `engram version` shows "dev")
go build -ldflags="-X main.version=local-$(git describe --tags --always)" -o engram ./cmd/engram
```

### Download binary (all platforms)

Grab the latest release for your platform from [GitHub Releases](https://github.com/Gentleman-Programming/engram/releases).

| Platform | File |
|----------|------|
| macOS (Apple Silicon) | `engram_<version>_darwin_arm64.tar.gz` |
| macOS (Intel) | `engram_<version>_darwin_amd64.tar.gz` |
| Linux (x86_64) | `engram_<version>_linux_amd64.tar.gz` |
| Linux (ARM64) | `engram_<version>_linux_arm64.tar.gz` |
| Windows (x86_64) | `engram_<version>_windows_amd64.zip` |
| Windows (ARM64) | `engram_<version>_windows_arm64.zip` |

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

# VS Code — add MCP server via CLI
code --add-mcp "{\"name\":\"engram\",\"command\":\"engram\",\"args\":[\"mcp\"]}"

# Antigravity — add via MCP Store (see Agent Setup below)

# Or interactive (asks which agent)
engram setup
```

See [Agent Setup](#agent-setup) for manual configuration or other agents (VS Code, Antigravity, Cursor, Windsurf).

That's it. No Node.js, no Python, no Bun, no Docker, no ChromaDB, no vector database, no worker processes. **One binary, one SQLite file.**

## How It Works

<p align="center">
  <img src="assets/agent-save.png" alt="Agent saving a memory via mem_save" width="800" />
  <br />
  <em>The agent proactively calls <code>mem_save<