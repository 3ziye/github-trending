# Planning with Files

> **Work like Manus** — the AI agent company Meta acquired for **$2 billion**.

## Thank You

To everyone who starred, forked, and shared this skill — thank you. This project blew up in less than 24 hours, and the support from the community has been incredible.

If this skill helps you work smarter, that's all I wanted.

---

A Claude Code plugin containing an [Agent Skill](https://code.claude.com/docs/en/skills) that transforms your workflow to use persistent markdown files for planning, progress tracking, and knowledge storage — the exact pattern that made Manus worth billions.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-Plugin-blue)](https://code.claude.com/docs/en/plugins)
[![Claude Code Skill](https://img.shields.io/badge/Claude%20Code-Skill-green)](https://code.claude.com/docs/en/skills)
[![Cursor Rules](https://img.shields.io/badge/Cursor-Rules-purple)](https://docs.cursor.com/context/rules-for-ai)
[![Version](https://img.shields.io/badge/version-2.0.1-brightgreen)](https://github.com/OthmanAdi/planning-with-files/releases)

## Versions

| Version | Branch | Features | Install |
|---------|--------|----------|---------|
| **v2.0.0** (current) | `master` | Hooks, templates, scripts | `/plugin install planning-with-files@planning-with-files` |
| **v1.0.0** (legacy) | `legacy` | Core 3-file pattern | `git clone -b legacy https://github.com/OthmanAdi/planning-with-files.git` |

## What's New in v2.0.0

- **Hooks Integration** — Automatic plan re-reading and completion verification
- **Templates** — Structured templates for task_plan.md, findings.md, progress.md
- **Scripts** — Helper scripts for initialization and completion checks
- **Enhanced Documentation** — 2-Action Rule, 3-Strike Protocol, 5-Question Reboot Test

See [CHANGELOG.md](CHANGELOG.md) for details. Upgrading from v1.x? See [MIGRATION.md](MIGRATION.md).

## Why This Skill?

On December 29, 2025, [Meta acquired Manus for $2 billion](https://techcrunch.com/2025/12/29/meta-just-bought-manus-an-ai-startup-everyone-has-been-talking-about/). In just 8 months, Manus went from launch to $100M+ revenue. Their secret? **Context engineering**.

This skill implements Manus's core workflow pattern:

> "Markdown is my 'working memory' on disk. Since I process information iteratively and my active context has limits, Markdown files serve as scratch pads for notes, checkpoints for progress, building blocks for final deliverables."
> — Manus AI

## The Problem

Claude Code (and most AI agents) suffer from:

- **Volatile memory** — TodoWrite tool disappears on context reset
- **Goal drift** — After 50+ tool calls, original goals get forgotten
- **Hidden errors** — Failures aren't tracked, so the same mistakes repeat
- **Context stuffing** — Everything crammed into context instead of stored

## The Solution: 3-File Pattern

For every complex task, create THREE files:

```
task_plan.md      → Track phases and progress
findings.md       → Store research and findings
progress.md       → Session log and test results
```

### The Core Principle

```
Context Window = RAM (volatile, limited)
Filesystem = Disk (persistent, unlimited)

→ Anything important gets written to disk.
```

<details>
<summary><strong>Workflow Diagram</strong> (click to expand)</summary>

This diagram shows how the three files work together and how hooks interact with them:

```
┌─────────────────────────────────────────────────────────────────┐
│                    TASK START                                    │
│  User requests a complex task (>5 tool calls expected)          │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
         ┌───────────────────────────────┐
         │  STEP 1: Create task_plan.md │
         │  (NEVER skip this step!)      │
         └───────────────┬───────────────┘
                         │
                         ▼
         ┌───────────────────────────────┐
         │  STEP 2: Create findings.md   │
         │  STEP 3: Create progress.md   │
         └───────────────┬───────────────┘
                         │
                         ▼
    ┌────────────────────────────────────────────┐
    │         WORK LOOP (Iterative)              │
    │                                            │
    │  ┌──────────────────────────────────────┐ │
    │  │  PreToolUse Hook (Automatic)         │ │
    │  │  → Reads task_plan.md before        │ │
    │  │    Write/Edit/Bash operations       │ │
    │  │  → Refreshes goals in attention      │ │
    │  └──────────────┬───────────────────────┘ │
    │                 │                          │
    │                 ▼                          │
    │  ┌──────────────────────────────────────┐ │
    │  │  Perform work (tool calls)          │ │
    │  │  - Research → Update findings.md    │ │
    │  │  - 