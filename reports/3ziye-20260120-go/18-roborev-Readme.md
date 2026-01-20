# roborev

Automatic code review for git commits using AI agents (Claude Code, Codex, Gemini, Copilot, OpenCode).

![TUI Queue View](docs/screenshots/tui-queue.png)

## Installation

```bash
curl -fsSL https://raw.githubusercontent.com/wesm/roborev/main/scripts/install.sh | bash
```

Or with Go:

```bash
go install github.com/wesm/roborev/cmd/roborev@latest
go install github.com/wesm/roborev/cmd/roborevd@latest
```

Ensure `$GOPATH/bin` is in your PATH:

```bash
export PATH="$PATH:$(go env GOPATH)/bin"
```

## Quick Start

```bash
cd your-repo
roborev init          # Install post-commit hook
git commit -m "..."   # Reviews happen automatically
roborev tui           # View reviews in interactive UI
```

**Note**: Hook installation automatically detects your git hook manager (Husky, etc.) via `core.hooksPath`.

## Commands

| Command | Description |
|---------|-------------|
| `roborev init` | Initialize roborev in current repo |
| `roborev status` | Show daemon and queue status |
| `roborev tui` | Interactive terminal UI |
| `roborev show [sha]` | Display review for commit |
| `roborev show --job <id>` | Display review by job ID |
| `roborev review <sha>` | Queue a commit for review |
| `roborev review <start> <end>` | Queue a commit range (inclusive) |
| `roborev review --branch` | Review all commits on current branch |
| `roborev review --since <commit>` | Review commits since a specific commit |
| `roborev review --dirty` | Review uncommitted changes |
| `roborev review --reasoning <level>` | Set reasoning depth (thorough/standard/fast) |
| `roborev prompt "<text>"` | Run ad-hoc prompt with AI agent |
| `roborev respond <id> [msg]` | Add a response/note to a review |
| `roborev address <id>` | Mark review as addressed |
| `roborev refine` | Auto-fix failed reviews using AI |
| `roborev repo list` | List tracked repositories |
| `roborev repo rename <old> <new>` | Rename a repository's display name |
| `roborev stream` | Stream review events (JSONL) |
| `roborev daemon start\|stop\|restart` | Manage the daemon |
| `roborev install-hook` | Install git post-commit hook |
| `roborev uninstall-hook` | Remove git post-commit hook |
| `roborev update` | Update roborev to latest version |
| `roborev skills install` | Install agent skills (Claude Code, Codex) |
| `roborev version` | Show version information |

## Reviewing Branches

Use `--branch` to review all commits since your branch diverged from main:

```bash
roborev review --branch              # Review branch vs auto-detected main/master
roborev review --branch --base dev   # Review branch vs specific base
roborev review --branch --wait       # Wait for review and show result
```

This is useful for pre-merge reviews of entire feature branches.

## Reviewing Specific Commits

Use `--since` to review commits since a specific point:

```bash
roborev review --since HEAD~5       # Review last 5 commits
roborev review --since abc123       # Review commits since abc123 (exclusive)
roborev review --since v1.0.0       # Review commits since a tag
```

The range is exclusive of the starting commit (like git's `..` range syntax). Unlike `--branch`, this works on any branch including main.

## Reviewing Uncommitted Changes

Use `--dirty` to review working tree changes before committing:

```bash
roborev review --dirty           # Queue review of uncommitted changes
roborev review --dirty --wait    # Wait for review and show result
```

Includes staged changes, unstaged changes to tracked files, and untracked files.

The `--wait` flag exits with code 0 for passing reviews and code 1 for failing reviews, useful for CI:

```bash
if ! roborev review --dirty --wait --quiet; then
    echo "Review failed - please address findings"
    exit 1
fi
```

## Ad-Hoc Prompts

Use `prompt` to run arbitrary prompts with AI agents for tasks beyond code review:

```bash
roborev prompt "Explain the architecture of this codebase"
roborev prompt --wait "What does the main function do?"
roborev prompt --agent claude-code "Refactor error handling in main.go"
roborev prompt --reasoning thorough "Find potential security issues"
roborev prompt --agentic "Add error handling to main.go"
cat instructions.txt | roborev prompt --wait
```

**Flags:**

| Flag | Description |
|------|-------------|
| `--wait` | Wait for job to complete and show result |
| `--agent` | Agent to use (default: from config) |
| `--reasoning` | Reasoning level: fast, standard, or thorough |
| `--no-context` | Don't include repository context in prompt |
| `--agentic` | Enable agentic mode (allow file edits and commands) |
| `--yolo` | Alias for `--agentic` |
| `--quiet` | Suppress output (just enqueue) |

By default, prompts run in **review mode** (read-only). Use `--agentic` (or `--yolo`) to enable write operations (file edits, bash commands) for tasks that need to modify your codebase.

By default, prompts include context about the repository (name, path, and any project guidelines from `.roborev.toml`). Use `--no-context