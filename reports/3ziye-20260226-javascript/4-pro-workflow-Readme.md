# Pro Workflow

[![GitHub stars](https://img.shields.io/github/stars/rohitg00/pro-workflow?style=social)](https://github.com/rohitg00/pro-workflow)
[![npm version](https://img.shields.io/npm/v/pro-workflow)](https://www.npmjs.com/package/pro-workflow)

Battle-tested AI coding workflows from power users. Self-correcting memory, parallel worktrees, wrap-up rituals, and the 80/20 AI coding ratio. Works with **Claude Code** and **Cursor**.

## The Core Idea

> "80% of my code is written by AI, 20% is spent reviewing and correcting it." — Karpathy

This skill optimizes for that ratio. Every pattern reduces correction cycles.

## Patterns

| Pattern | What It Does |
|---------|--------------|
| **Self-Correction Loop** | Claude learns from your corrections automatically |
| **Parallel Worktrees** | Zero dead time - native `claude -w` worktrees |
| **Wrap-Up Ritual** | End sessions with intention, capture learnings |
| **Split Memory** | Modular CLAUDE.md for complex projects |
| **80/20 Review** | Batch reviews at checkpoints |
| **Model Selection** | Opus 4.6 adaptive thinking, Sonnet 4.6 (1M context) |
| **Context Discipline** | Manage your 200k token budget |
| **Learning Log** | Auto-document insights |

## Installation

### Cursor (Recommended)

```bash
/add-plugin pro-workflow
```

The plugin includes 9 skills, 3 agents, and 6 rules that load automatically.

### Claude Code — One-Click Plugin Install

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

### Claude Code — Build with SQLite Support

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

## Skills (Cursor)

| Skill | Description |
|:------|:------------|
| `pro-workflow` | Core 8 workflow patterns for AI-assisted coding |
| `smart-commit` | Quality gates, staged review, and conventional commits |
| `wrap-up` | End-of-session ritual with change audit and learning capture |
| `learn-rule` | Capture corrections as persistent learning rules |
| `parallel-worktrees` | Set up git worktrees for zero dead time |
| `replay-learnings` | Surface past learnings relevant to the current task |
| `session-handoff` | Generate handoff documents for session continuity |
| `insights` | Session analytics, correction trends, and productivity metrics |
| `deslop` | Remove AI-generated code slop and clean up style |

## Rules (Cursor)

| Rule | Applies To | Description |
|:-----|:-----------|:------------|
| `quality-gates` | Always | Lint, typecheck, and test before commits |
| `atomic-commits` | Always | Conventional format, feature branches, specific staging |
| `context-discipline` | Always | Read before edit, plan before multi-file changes |
| `self-correction` | Always | Capture mistakes as compounding learnings |
| `no-debug-statements` | `*.{ts,tsx,js,jsx,py,go,rs}` | Remove console.log, debugger, print before committing |
| `communication-style` | Always | Concise, action-oriented, no over-engineering |

## Commands (Claude Code)

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
/search "file paths"      # Exact phrase s