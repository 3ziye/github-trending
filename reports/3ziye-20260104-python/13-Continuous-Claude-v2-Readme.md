# Continuous Claude

Session continuity, token-efficient MCP execution, and agentic workflows for Claude Code.

---

## Table of Contents

- [Architecture Overview](#architecture-overview)
- [The Problem](#the-problem) / [The Solution](#the-solution)
- [Quick Start](#quick-start) (project or global install)
- [How to Talk to Claude](#how-to-talk-to-claude)
- [Skills vs Agents](#skills-vs-agents)
- [MCP Code Execution](#mcp-code-execution)
- [Continuity System](#continuity-system)
- [Hooks System](#hooks-system)
- [Reasoning History](#reasoning-history)
- [Braintrust Session Tracing](#braintrust-session-tracing-optional) + [Compound Learnings](#compound-learnings)
- [Artifact Index](#artifact-index) (handoff search, outcome tracking)
- [TDD Workflow](#tdd-workflow)
- [Code Quality (qlty)](#code-quality-qlty)
- [Directory Structure](#directory-structure)
- [Environment Variables](#environment-variables)
- [Glossary](#glossary)
- [Troubleshooting](#troubleshooting)
- [Acknowledgments](#acknowledgments)

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            CLAUDE CODE SESSION                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌────────────┐  │
│   │ SessionStart│───▶│   Working   │───▶│  PreCompact │───▶│ SessionEnd │  │
│   └──────┬──────┘    └──────┬──────┘    └──────┬──────┘    └─────┬──────┘  │
│          │                  │                  │                  │         │
│          ▼                  ▼                  ▼                  ▼         │
│   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌───────────┐   │
│   │Load Ledger   │   │PreToolUse    │   │Auto-Handoff  │   │Mark       │   │
│   │Load Handoff  │   │ TS Preflight │   │Block Manual  │   │Outcome    │   │
│   │Surface       │   │PostToolUse   │   │              │   │Cleanup    │   │
│   │Learnings     │   │UserPrompt    │   │              │   │Learn      │   │
│   └──────────────┘   └──────────────┘   └──────────────┘   └───────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
                │                │                │                │
                ▼                ▼                ▼                ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                              DATA LAYER                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  thoughts/                    .claude/cache/                                │
│  ├── ledgers/                 ├── artifact-index/                           │
│  │   └── CONTINUITY_*.md          └── context.db (SQLite+FTS5)             │
│  └── shared/                  ├── learnings/                                │
│      ├── handoffs/                └── <date>_<session>.md                   │
│      │   └── <session>/       └── braintrust_sessions/                      │
│      │       └── *.md             └── <session>.json                        │
│      └── plans/                                                             │
│          └── *.md             .git/claude/                                  │
│                               └── commits/                                  │
│                                   └── <hash>/reasoning.md                   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
                │                                        │
                ▼                                        ▼
┌───────────────────────────────────┐  ┌───────────────────────────────────┐
│          SKILLS                   │  │           AGENTS                   │
├───────────────────────────────────┤  ├───────────────────────────────────┤
│                                   │  │                                   │
│  ┌──────────────────┐             │  │  ┌──────────────────┐             │
│  │ continuity_ledger│ Save state  │  │  │ plan-agent       │ Create plan │
│  ├──────────────────┤             │  │  ├──────────────────┤             │
│  │ create_handoff   │ End session │  │  │ validate-agent   │ Check tech  │
│  ├──────────────────┤             │  │  ├──────────────────┤             │
│  │ resume_handoff   │ Resume work │  │  │ implement_plan   │ Execute     │
│  ├──────────────────┤             │  │  ├──────────────────┤             │
│  │ commit           │ Git commit  │  │  │ research-agent   │ Research    │
│  ├──────────────────┤             │  │  ├───────────────