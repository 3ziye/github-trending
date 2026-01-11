# AutoCoder

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-FFDD00?style=flat&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/leonvanzyl)

A long-running autonomous coding agent powered by the Claude Agent SDK. This tool can build complete applications over multiple sessions using a two-agent pattern (initializer + coding agent). Includes a React-based UI for monitoring progress in real-time.

## Video Tutorial

[![Watch the tutorial](https://img.youtube.com/vi/lGWFlpffWk4/hqdefault.jpg)](https://youtu.be/lGWFlpffWk4)

> **[Watch the setup and usage guide →](https://youtu.be/lGWFlpffWk4)**

---

## Prerequisites

### Claude Code CLI (Required)

This project requires the Claude Code CLI to be installed. Install it using one of these methods:

**macOS / Linux:**
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows (PowerShell):**
```powershell
irm https://claude.ai/install.ps1 | iex
```

### Authentication

You need one of the following:

- **Claude Pro/Max Subscription** - Use `claude login` to authenticate (recommended)
- **Anthropic API Key** - Pay-per-use from https://console.anthropic.com/

---

## Quick Start

### Option 1: Web UI (Recommended)

**Windows:**
```cmd
start_ui.bat
```

**macOS / Linux:**
```bash
./start_ui.sh
```

This launches the React-based web UI at `http://localhost:5173` with:
- Project selection and creation
- Kanban board view of features
- Real-time agent output streaming
- Start/pause/stop controls

### Option 2: CLI Mode

**Windows:**
```cmd
start.bat
```

**macOS / Linux:**
```bash
./start.sh
```

The start script will:
1. Check if Claude CLI is installed
2. Check if you're authenticated (prompt to run `claude login` if not)
3. Create a Python virtual environment
4. Install dependencies
5. Launch the main menu

### Creating or Continuing a Project

You'll see options to:
- **Create new project** - Start a fresh project with AI-assisted spec generation
- **Continue existing project** - Resume work on a previous project

For new projects, you can use the built-in `/create-spec` command to interactively create your app specification with Claude's help.

---

## How It Works

### Two-Agent Pattern

1. **Initializer Agent (First Session):** Reads your app specification, creates features in a SQLite database (`features.db`), sets up the project structure, and initializes git.

2. **Coding Agent (Subsequent Sessions):** Picks up where the previous session left off, implements features one by one, and marks them as passing in the database.

### Feature Management

Features are stored in SQLite via SQLAlchemy and managed through an MCP server that exposes tools to the agent:
- `feature_get_stats` - Progress statistics
- `feature_get_next` - Get highest-priority pending feature
- `feature_get_for_regression` - Random passing features for regression testing
- `feature_mark_passing` - Mark feature complete
- `feature_skip` - Move feature to end of queue
- `feature_create_bulk` - Initialize all features (used by initializer)

### Session Management

- Each session runs with a fresh context window
- Progress is persisted via SQLite database and git commits
- The agent auto-continues between sessions (3 second delay)
- Press `Ctrl+C` to pause; run the start script again to resume

---

## Important Timing Expectations

> **Note: Building complete applications takes time!**

- **First session (initialization):** The agent generates feature test cases. This takes several minutes and may appear to hang - this is normal.

- **Subsequent sessions:** Each coding iteration can take **5-15 minutes** depending on complexity.

- **Full app:** Building all features typically requires **many hours** of total runtime across multiple sessions.

**Tip:** The feature count in the prompts determines scope. For faster demos, you can modify your app spec to target fewer features (e.g., 20-50 features for a quick demo).

---

## Project Structure

```
autonomous-coding/
├── start.bat                 # Windows CLI start script
├── start.sh                  # macOS/Linux CLI start script
├── start_ui.bat              # Windows Web UI start script
├── start_ui.sh               # macOS/Linux Web UI start script
├── start.py                  # CLI menu and project management
├── start_ui.py               # Web UI backend (FastAPI server launcher)
├── autonomous_agent_demo.py  # Agent entry point
├── agent.py                  # Agent session logic
├── client.py                 # Claude SDK client configuration
├── security.py               # Bash command allowlist and validation
├── progress.py               # Progress tracking utilities
├── prompts.py                # Prompt loading utilities
├── api/
│   └── database.py           # SQLAlchemy models (Feature table)
├── mcp_server/
│   └── feature_mcp.py        # MCP server for feature management tools
├── server/
│   ├── main.py               # FastAPI REST API server
│   ├── websocket.py          # WebSoc