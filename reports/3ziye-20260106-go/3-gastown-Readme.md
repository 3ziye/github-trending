# Gas Town

Multi-agent orchestrator for Claude Code. Track work with convoys; sling to agents.

## Why Gas Town?

| Without | With Gas Town |
|---------|---------------|
| Agents forget work after restart | Work persists on hooks - survives crashes, compaction, restarts |
| Manual coordination | Agents have mailboxes, identities, and structured handoffs |
| 4-10 agents is chaotic | Comfortably scale to 20-30 agents |
| Work state in agent memory | Work state in Beads (git-backed ledger) |

## Prerequisites

- **Go 1.23+** - [go.dev/dl](https://go.dev/dl/)
- **Git 2.25+** - for worktree support
- **beads (bd)** - [github.com/steveyegge/beads](https://github.com/steveyegge/beads) - required for issue tracking
- **tmux 3.0+** - recommended for the full experience (the Mayor session is the primary interface)
- **Claude Code CLI** - [claude.ai/code](https://claude.ai/code)

## Quick Start

```bash
# Install
go install github.com/steveyegge/gastown/cmd/gt@latest

# Ensure Go binaries are in your PATH (add to ~/.zshrc or ~/.bashrc)
export PATH="$PATH:$HOME/go/bin"

# Create workspace (--git auto-initializes git repository)
gt install ~/gt --git
cd ~/gt

# Add a project
gt rig add myproject https://github.com/you/repo.git

# Create your personal workspace
gt crew add <yourname> --rig myproject

# Start working
cd myproject/crew/<yourname>
```

For advanced multi-agent coordination, use the Mayor session:

```bash
gt mayor attach                        # Enter the Mayor's office
```

Inside the Mayor session, you're talking to Claude with full town context:

> "Help me fix the authentication bug in myproject"

The Mayor will create convoys, dispatch workers, and coordinate everything. You can also run CLI commands directly:

```bash
# Create a convoy and sling work (CLI workflow)
gt convoy create "Feature X" issue-123 issue-456 --notify --human
gt sling issue-123 myproject

# Track progress
gt convoy list

# Switch between agent sessions
gt agents
```

## Core Concepts

**The Mayor** is your AI coordinator. It's Claude Code with full context about your workspace, projects, and agents. The Mayor session (`gt prime`) is the primary way to interact with Gas Town - just tell it what you want to accomplish.

```
Town (~/gt/)              Your workspace
├── Mayor                 Your AI coordinator (start here)
├── Rig (project)         Container for a git project + its agents
│   ├── Polecats          Workers (ephemeral, spawn → work → disappear)
│   ├── Witness           Monitors workers, handles lifecycle
│   └── Refinery          Merge queue processor
```

**Hook**: Each agent has a hook where work hangs. On wake, run what's on your hook.

**Beads**: Git-backed issue tracker. All work state lives here. [github.com/steveyegge/beads](https://github.com/steveyegge/beads)

## Workflows

### Full Stack (Recommended)

The primary Gas Town experience. Agents run in tmux sessions with the Mayor as your interface.

```bash
gt start                               # Start Gas Town (daemon + Mayor session)
gt mayor attach                        # Enter Mayor session

# Inside Mayor session, just ask:
# "Create a convoy for issues 123 and 456 in myproject"
# "What's the status of my work?"
# "Show me what the witness is doing"

# Or use CLI commands:
gt convoy create "Feature X" issue-123 issue-456
gt sling issue-123 myproject           # Spawns polecat automatically
gt convoy list                         # Dashboard view
gt agents                              # Navigate between sessions
```

### Minimal (No Tmux)

Run individual Claude Code instances manually. Gas Town just tracks state.

```bash
gt convoy create "Fix bugs" issue-123  # Create convoy (sling auto-creates if skipped)
gt sling issue-123 myproject           # Assign to worker
claude --resume                        # Agent reads mail, runs work
gt convoy list                         # Check progress
```

### Pick Your Roles

Gas Town is modular. Run what you need:

- **Polecats only**: Manual spawning, no monitoring
- **+ Witness**: Automatic worker lifecycle, stuck detection
- **+ Refinery**: Merge queue, code review
- **+ Mayor**: Cross-project coordination

## Cooking Formulas

Formulas define structured workflows. Cook them, sling them to agents.

### Basic Example

```toml
# .beads/formulas/shiny.formula.toml
formula = "shiny"
description = "Design before code, review before ship"

[[steps]]
id = "design"
description = "Think about architecture"

[[steps]]
id = "implement"
needs = ["design"]

[[steps]]
id = "test"
needs = ["implement"]

[[steps]]
id = "submit"
needs = ["test"]
```

### Using Formulas

```bash
bd formula list                    # See available formulas
bd cook shiny                      # Cook into a protomolecule
bd mol pour shiny --var feature=auth   # Create runnable molecule
gt convoy create "Auth feature" gt-xyz  # Track with convoy
gt sling gt-xyz myproject          # Assign to worker
gt convoy list                     # Monitor progress
```