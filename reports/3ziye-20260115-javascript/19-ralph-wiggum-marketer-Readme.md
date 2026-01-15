# Ralph Wiggum Marketer

A **Claude Code Plugin** that provides an autonomous AI copywriter for SaaS content marketing.

Uses the [Ralph Wiggum pattern](https://ghuntley.com/ralph/) - an iterative AI loop that ships content while you sleep.

## Installation

### Option 1: Add as Marketplace (Recommended)

```bash
# In Claude Code, add the repo as a marketplace:
/plugin marketplace add muratcankoylan/ralph-wiggum-marketer

# Then install the plugin:
/plugin install ralph-wiggum-marketer@muratcankoylan-ralph-wiggum-marketer
```

### Option 2: Test Locally (For Development)

```bash
# Clone the repo
git clone https://github.com/muratcankoylan/ralph-wiggum-marketer.git

# Run Claude Code with the plugin directory
claude --plugin-dir ./ralph-wiggum-marketer
```

### Option 3: Interactive Plugin Manager

```bash
# Open the plugin manager:
/plugin

# Browse, search, and install from the interactive UI
```

## Quick Start

```bash
# 1. Initialize a new content project
/ralph-init

# 2. Check progress anytime
/ralph-status

# 3. Cancel if needed
/ralph-cancel
```

## Commands

| Command | Description |
|---------|-------------|
| `/ralph-init` | Initialize a new content project in current directory |
| `/ralph-marketer` | Start the autonomous copywriter loop |
| `/ralph-status` | Check content pipeline and progress |
| `/ralph-cancel` | Cancel the active loop |

## How It Works

```
┌──────────────────────────────────────────────────────────────────┐
│                     MULTI-AGENT ECOSYSTEM                        │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─────────────┐   ┌─────────────┐   ┌─────────────┐             │
│  │ TrendScout  │   │  Research   │   │  Product/   │             │
│  │   Agent     │   │   Agent     │   │  Marketing  │             │
│  └──────┬──────┘   └──────┬──────┘   └──────┬──────┘             │
│         │                 │                 │                    │
│         ▼                 ▼                 ▼                    │
│  ┌────────────────────────────────────────────────────┐          │
│  │              SQLite Content Database               │          │
│  │  • trends     • research     • communications      │          │
│  └────────────────────────┬───────────────────────────┘          │
│                           │                                      │
│                           ▼                                      │
│  ┌────────────────────────────────────────────────────┐          │
│  │           RALPH THE COPYWRITER                     │          │
│  │                                                     │         │
│  │   Reads inputs → Plans content → Writes drafts     │          │
│  │   → Reviews & iterates → Publishes                 │          │
│  │                                                     │         │
│  │   Memory: git commits + progress.txt + prd.json    │          │
│  └────────────────────────────────────────────────────┘          │
│                           │                                      │
│                           ▼                                      │
│                    Published Content                             │
│              (blogs, case studies, social, newsletters)          │
└──────────────────────────────────────────────────────────────────┘
```

### The Ralph Loop

1. **Read PRD**: Check `scripts/ralph/prd.json` for tasks
2. **Check Progress**: Read `scripts/ralph/progress.txt` for learnings
3. **Pick Task**: Find highest priority story where `passes: false`
4. **Execute**: Complete the task following acceptance criteria
5. **Verify**: Run tests to ensure quality
6. **Commit**: Save progress to git
7. **Update**: Mark task done, log learnings
8. **Repeat**: Loop until all tasks complete

Each iteration is a fresh context window. Memory persists through files.

## Plugin Structure

```
ralph-wiggum-marketer/
├── .claude-plugin/
│   └── plugin.json          # Plugin manifest
├── commands/
│   ├── ralph-marketer.md    # Main loop command
│   ├── ralph-init.md        # Project initialization
│   ├── ralph-status.md      # Status check
│   └── ralph-cancel.md      # Cancel loop
├── skills/
│   └── copywriter/
│       └── SKILL.md         # Copywriter skill
├── hooks/
│   ├── hooks.json           # Hook configuration
│   └── stop-hook.sh         # Loop continuation hook
├── scripts/
│   └── src/                 # Database & utility scripts
├── templates/
│   ├── prd.json             # Task template
│   ├── progress.txt         # Progress log template
│   ├── prompt.md            # Agent instructions template
│   └── package.json         # Project package.json template
└── README.md
```

## Database Schema

### Input Tables (from other agents)

```sql
-- Trends from TrendScout
trends (topic, description, source, relevance_score, status)

-- Research from Research Agent
research (title, summary, key_findings, data_point