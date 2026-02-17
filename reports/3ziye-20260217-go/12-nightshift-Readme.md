# Nightshift

> It finds what you forgot to look for.

**[nightshift.haplab.com](https://nightshift.haplab.com)** · [Docs](https://nightshift.haplab.com/docs/intro) · [Quick Start](https://nightshift.haplab.com/docs/quick-start) · [CLI Reference](https://nightshift.haplab.com/docs/cli-reference)

![Nightshift logo](logo.png)

Your tokens get reset every week, you might as well use them. Nightshift runs overnight to find dead code, doc drift, test gaps, security issues, and 20+ other things silently accumulating while you ship features. Like a Roomba for your codebase — runs overnight, worst case you close the PR.

Everything lands as a branch or PR. It never writes directly to your primary branch. Don't like something? Close it. That's the whole rollback plan.

## Features

- **Budget-aware**: Uses remaining daily allotment, never exceeds configurable max (default 75%)
- **Multi-project**: Point it at your repos, it already knows what to look for
- **Zero risk**: Everything is a PR — merge what surprises you, close the rest
- **Great DX**: Thoughtful CLI defaults with clear output and reports

## Installation

Full guide: [Installation docs](https://nightshift.haplab.com/docs/installation)

```bash
brew install marcus/tap/nightshift
```

Binary downloads are available on the GitHub releases page.

Manual install:

```bash
go install github.com/marcus/nightshift/cmd/nightshift@latest
```

## Getting Started

Full guide: [Quick Start docs](https://nightshift.haplab.com/docs/quick-start)

After installing, run the guided setup:

```bash
nightshift setup
```

This walks you through provider configuration, project selection, budget calibration, and daemon setup. Once complete you can preview what nightshift will do:

```bash
nightshift preview
nightshift budget
```

Or kick off a run immediately:

```bash
nightshift run
```

## Common CLI Usage

Full reference: [CLI Reference docs](https://nightshift.haplab.com/docs/cli-reference)

```bash
# Preview next scheduled runs with prompt previews
nightshift preview -n 3
nightshift preview --long
nightshift preview --explain
nightshift preview --plain
nightshift preview --json
nightshift preview --write ./nightshift-prompts

# Guided global setup
nightshift setup

# Check environment and config health
nightshift doctor

# Budget status and calibration
nightshift budget --provider claude
nightshift budget snapshot --local-only
nightshift budget history -n 10
nightshift budget calibrate

# Browse and inspect available tasks
nightshift task list
nightshift task list --category pr
nightshift task list --cost low --json

# Show task details and planning prompt
nightshift task show lint-fix
nightshift task show skill-groom
nightshift task show lint-fix --prompt-only

# Run a task immediately
nightshift task run lint-fix --provider claude
nightshift task run skill-groom --provider codex --dry-run
nightshift task run lint-fix --provider codex --dry-run
```

If `gum` is available, preview output is shown through the gum pager. Use `--plain` to disable.

### `nightshift run`

Before executing, `nightshift run` displays a **preflight summary** showing the
selected provider, budget status, projects, and planned tasks. In interactive
terminals you are prompted for confirmation; in non-TTY environments (cron,
daemon, CI) confirmation is auto-skipped.

| Flag | Default | Description |
|------|---------|-------------|
| `--dry-run` | `false` | Show preflight summary and exit without executing |
| `--project`, `-p` | _(all configured)_ | Target a single project directory |
| `--task`, `-t` | _(auto-select)_ | Run a specific task by name |
| `--max-projects` | `1` | Max projects to process (ignored when `--project` is set) |
| `--max-tasks` | `1` | Max tasks per project (ignored when `--task` is set) |
| `--random-task` | `false` | Pick a random task from eligible tasks instead of the highest-scored one |
| `--ignore-budget` | `false` | Bypass budget checks (use with caution) |
| `--yes`, `-y` | `false` | Skip the confirmation prompt |

```bash
# Interactive run with preflight summary + confirmation prompt
nightshift run

# Non-interactive: skip confirmation
nightshift run --yes

# Dry-run: show preflight summary and exit
nightshift run --dry-run

# Process up to 3 projects, 2 tasks each
nightshift run --max-projects 3 --max-tasks 2

# Pick a random eligible task
nightshift run --random-task

# Bypass budget limits (shows warning)
nightshift run --ignore-budget

# Target a specific project and task directly
nightshift run -p ./my-project -t lint-fix
```

Other useful flags:
- `nightshift status --today` to see today's activity summary
- `nightshift daemon start --foreground` for debug
- `--category` — filter tasks by category (pr, analysis, options, safe, map, emergency)
- `--cost` — filter by cost tier (low, medium, high, veryhigh)
- `--prompt-only` — output just the raw prompt text for piping
- `--provider` — required for `task run`, choose claude or codex
- `--dry-run` — preview the p