# awesome-slash

[![npm version](https://img.shields.io/npm/v/awesome-slash.svg)](https://www.npmjs.com/package/awesome-slash)
[![CI](https://github.com/avifenesh/awesome-slash/actions/workflows/ci.yml/badge.svg)](https://github.com/avifenesh/awesome-slash/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

AI models can write code. That's not the hard part anymore. The hard part is everything else—picking what to work on, managing branches, reviewing output, cleaning up artifacts, handling CI, addressing comments, deploying. **awesome-slash automates the entire workflow**, not just the coding.

**Works with:** Claude Code | OpenCode | Codex CLI

---

## Quick Navigation

| Section | What's there |
|---------|--------------|
| [Commands](#commands) | All 8 commands with jump links |
| [What This Does](#what-this-project-does) | The problem and how this solves it |
| [What's Different](#what-makes-this-different) | Why this isn't just another AI tool |
| [Design Philosophy](#design-philosophy) | The thinking behind the architecture |
| [Command Details](#command-details) | Deep dive into each command |
| [Installation](#installation) | Get started in 2 commands |
| [Documentation](#documentation) | Links to detailed docs |

---

## Commands

| Command | What it does | Details |
|---------|--------------|---------|
| [`/next-task`](#next-task) | Picks a task, implements it, reviews it, ships it | [→](#next-task) |
| [`/ship`](#ship) | Creates PR, monitors CI, addresses reviews, merges | [→](#ship) |
| [`/deslop`](#deslop) | Finds and removes debug code, TODOs, AI artifacts | [→](#deslop) |
| [`/audit-project`](#audit-project) | Multi-agent code review until issues resolved | [→](#audit-project) |
| [`/drift-detect`](#drift-detect) | Compares your docs to actual code state | [→](#drift-detect) |
| [`/repo-map`](#repo-map) | Builds a cached AST repo map for fast analysis | [→](#repo-map) |
| [`/enhance`](#enhance) | Analyzes prompts, plugins, docs for improvements | [→](#enhance) |
| [`/sync-docs`](#sync-docs) | Syncs documentation with code changes | [→](#sync-docs) |

---

## What This Project Does

You have AI coding assistants. They can write code. But the full workflow—picking what to work on, setting up branches, implementing, reviewing, fixing issues, creating PRs, monitoring CI, addressing reviewer comments, merging—still requires you to babysit every step.

**awesome-slash automates the entire workflow.** Not just code generation, but the complete process from "I have 50 issues" to "PR merged and deployed."

### The Core Idea

Most AI tools generate code and stop. You still have to:
- Decide what to work on
- Create branches
- Run the implementation
- Review the output
- Clean up AI artifacts
- Create PRs
- Wait for CI
- Address review comments
- Merge and deploy

This plugin handles all of that. You approve a plan, then it runs autonomously until there's a merged PR (or until something genuinely needs your input).

---

## What Makes This Different

### 1. Certainty-Based Detection

Every finding is tagged with a certainty level:
- **HIGH** - Definitely a problem. Safe to auto-fix.
- **MEDIUM** - Probably a problem. Needs context.
- **LOW** - Might be a problem. Needs human judgment.

This means you can run `/deslop apply` and trust that it won't break things.

### 2. Review Loops With Safeguards

The Phase 9 review loop spawns parallel reviewer agents (code quality, security, performance, test coverage) plus conditional specialists, iterating until no open issues remain. It runs deslop-work after each iteration to catch any AI artifacts.

### 3. Workflow Enforcement

A SubagentStop hook prevents agents from skipping phases. You can't push to remote before `/ship` is invoked. You can't skip the review loop. The workflow literally enforces the quality gates.

### 4. Resume From Any Point

State is tracked in two files:
- `tasks.json` - Which task you're working on (in your main repo)
- `flow.json` - Which phase you're in (in your worktree)

If your session dies, `/next-task --resume` picks up exactly where you left off.

### 5. Token Efficiency

- Compact output modes reduce tokens by 60-70%
- `/drift-detect` uses JavaScript collectors + a single LLM call (77% reduction vs multi-agent approaches)
- Pre-indexed pattern maps give O(1) lookups instead of scanning

### 6. Cross-Platform

Same workflows work on Claude Code, OpenCode, and Codex CLI. State directories adapt automatically (`.claude/`, `.opencode/`, `.codex/`).

---

## Design Philosophy

<details>
<summary><strong>Why build this? What's the thinking?</strong> (click to expand)</summary>

### The Actual Problem

Frontier models write good code. That's solved. What's not solved:

- **Context management** - Models forget what they're doing mid-session
- **Compaction amnesia** - Long sessions get summarized, losing critical state
- **Task drift** - Without structure