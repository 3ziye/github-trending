# Pro Workflow

[![GitHub stars](https://img.shields.io/github/stars/rohitg00/pro-workflow?style=social)](https://github.com/rohitg00/pro-workflow)
[![npm version](https://img.shields.io/npm/v/pro-workflow)](https://www.npmjs.com/package/pro-workflow)

Battle-tested Claude Code workflows from power users. Self-correcting memory, parallel worktrees, wrap-up rituals, and the 80/20 AI coding ratio.

**v1.2.0: Scout agent, /replay, /handoff, drift detection, adaptive quality gates, and correction heatmap!**

**If this helps your workflow, please give it a star!**

## What's New in v1.2.0

- **Scout Agent**: Confidence-gated exploration — scores readiness (0-100) before implementation, auto-gathers missing context
- **`/replay`**: Surface relevant past learnings before starting a task — your SQLite-powered coding muscle memory
- **`/handoff`**: Generate structured session handoff documents for seamless continuation in the next session
- **Drift Detection**: Hook that tracks your original intent and warns when you've strayed from the goal
- **Adaptive Quality Gates**: Gates adjust based on your correction history — high correction rate = tighter gates, low rate = relaxed gates
- **Correction Heatmap**: `/insights heatmap` shows which categories and projects get corrected most, with hot/cold learning analysis

### Previous: v1.1.0

- Smart `/commit` with quality gates, `/insights` analytics, agent teams, persistent SQLite storage with FTS5

## The Core Idea

> "80% of my code is written by AI, 20% is spent reviewing and correcting it." — Karpathy

This skill optimizes for that ratio. Every pattern reduces correction cycles.

## Patterns

| Pattern | What It Does |
|---------|--------------|
| **Self-Correction Loop** | Claude learns from your corrections automatically |
| **Parallel Worktrees** | Zero dead time - work while Claude thinks |
| **Wrap-Up Ritual** | End sessions with intention, capture learnings |
| **Split Memory** | Modular CLAUDE.md for complex projects |
| **80/20 Review** | Batch reviews at checkpoints |
| **Model Selection** | Opus+Thinking for one-shot accuracy |
| **Context Discipline** | Manage your 200k token budget |
| **Learning Log** | Auto-document insights |

## Installation

### One-Click Plugin Install (Recommended)

```bash
# Add marketplace
/plugin marketplace add rohitg00/pro-workflow

# Install plugin
/plugin install pro-workflow@pro-workflow
```

Or via CLI:

```bash
claude plugin marketplace add rohitg00/pro-workflow
claude plugin install pro-workflow@pro-workflow
```

### Build with SQLite Support

After installation, build the TypeScript for persistent storage:

```bash
cd ~/.claude/plugins/*/pro-workflow  # Navigate to plugin directory
npm install && npm run build
```

This creates the SQLite database at `~/.pro-workflow/data.db`.

### Or load directly

```bash
claude --plugin-dir /path/to/pro-workflow
```

### Manual Setup

```bash
git clone https://github.com/rohitg00/pro-workflow.git /tmp/pw
cp -r /tmp/pw/templates/split-claude-md/* ./.claude/
cp -r /tmp/pw/commands/* ~/.claude/commands/
cp -r /tmp/pw/hooks/* ~/.claude/
```

### Minimal (Just add to CLAUDE.md)

```markdown
## Pro Workflow

### Self-Correction
When corrected, propose rule → add to LEARNED after approval.

### Planning
Multi-file: plan first, wait for "proceed".

### Quality
After edits: lint, typecheck, test.

### LEARNED
```

## Commands

After plugin install, commands are namespaced:

| Command | Purpose |
|---------|---------|
| `/pro-workflow:wrap-up` | End-of-session checklist |
| `/pro-workflow:learn-rule` | Extract correction to memory (file-based) |
| `/pro-workflow:parallel` | Worktree setup guide |
| `/pro-workflow:learn` |Claude Code best practices & save learnings |
| `/pro-workflow:search` |Search learnings by keyword |
| `/pro-workflow:list` |List all stored learnings |
| `/pro-workflow:commit` | Smart commit with quality gates and code review |
| `/pro-workflow:insights` | Session analytics, learning patterns, and correction heatmap |
| `/pro-workflow:replay` |Surface past learnings for current task |
| `/pro-workflow:handoff` |Generate session handoff document for next session |

## Database Features

### Persistent Learnings

Learnings are stored in SQLite with FTS5 full-text search:

```
~/.pro-workflow/
└── data.db    # SQLite database with learnings and sessions
```

### Search Examples

```
/search testing           # Find all testing-related learnings
/search "file paths"      # Exact phrase search
/search git commit        # Multiple terms
```

### Learning Categories

- Navigation (file paths, finding code)
- Editing (code changes, patterns)
- Testing (test approaches)
- Git (commits, branches)
- Quality (lint, types, style)
- Context (when to clarify)
- Architecture (design decisions)
- Performance (optimization)
- Claude-Code (sessions, modes, CLAUDE.md, skills, subagents, hooks, MCP)
- Prompting (scope, constraints, acceptance criteria)

## Hooks

Automated enforcement of workflow