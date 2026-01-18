# Planning with Files

> **Work like Manus** — the AI agent company Meta acquired for **$2 billion**.

## Thank You

To everyone who starred, forked, and shared this skill — thank you. This project blew up in less than 24 hours, and the support from the community has been incredible.

If this skill helps you work smarter, that's all I wanted.

---

A Claude Code plugin that transforms your workflow to use persistent markdown files for planning, progress tracking, and knowledge storage — the exact pattern that made Manus worth billions.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-Plugin-blue)](https://code.claude.com/docs/en/plugins)
[![Claude Code Skill](https://img.shields.io/badge/Claude%20Code-Skill-green)](https://code.claude.com/docs/en/skills)
[![Cursor Rules](https://img.shields.io/badge/Cursor-Rules-purple)](https://docs.cursor.com/context/rules-for-ai)
[![Version](https://img.shields.io/badge/version-2.3.0-brightgreen)](https://github.com/OthmanAdi/planning-with-files/releases)

## Quick Install

```bash
/plugin marketplace add OthmanAdi/planning-with-files
/plugin install planning-with-files@planning-with-files
```

See [docs/installation.md](docs/installation.md) for all installation methods.

## Supported IDEs

| IDE | Status | Installation Guide | Format |
|-----|--------|-------------------|--------|
| Claude Code | ✅ Full Support | [Installation](docs/installation.md) | Plugin + SKILL.md |
| Cursor | ✅ Full Support | [Cursor Setup](docs/cursor.md) | Rules |
| Kilocode | ✅ Full Support | [Kilocode Setup](docs/kilocode.md) | Rules |
| OpenCode | ✅ Full Support | [OpenCode Setup](docs/opencode.md) | Personal/Project Skill |
| Codex | ✅ Full Support | [Codex Setup](docs/codex.md) | Personal Skill |

## Documentation

| Document | Description |
|----------|-------------|
| [Installation Guide](docs/installation.md) | All installation methods (plugin, manual, Cursor, Windows) |
| [Quick Start](docs/quickstart.md) | 5-step guide to using the pattern |
| [Workflow Diagram](docs/workflow.md) | Visual diagram of how files and hooks interact |
| [Troubleshooting](docs/troubleshooting.md) | Common issues and solutions |
| [Cursor Setup](docs/cursor.md) | Cursor IDE-specific instructions |
| [Windows Setup](docs/windows.md) | Windows-specific notes |
| [Kilo Code Support](docs/kilocode.md) | Kilo Code integration guide |
| [Codex Setup](docs/codex.md) | Codex IDE installation and usage |
| [OpenCode Setup](docs/opencode.md) | OpenCode IDE installation, oh-my-opencode config |

## Versions

| Version | Features | Install |
|---------|----------|---------|
| **v2.3.0** (current) | Codex & OpenCode IDE support | `/plugin install planning-with-files@planning-with-files` |
| **v2.2.2** | Restored skill activation language | See [releases](https://github.com/OthmanAdi/planning-with-files/releases) |
| **v2.2.1** | Session recovery after /clear, enhanced PreToolUse hook | See [releases](https://github.com/OthmanAdi/planning-with-files/releases) |
| **v2.2.0** | Kilo Code IDE support, Windows PowerShell support, OS-aware hooks | See [releases](https://github.com/OthmanAdi/planning-with-files/releases) |
| **v2.1.2** | Fix template cache issue (Issue #18) | See [releases](https://github.com/OthmanAdi/planning-with-files/releases) |
| **v2.1.0** | Claude Code v2.1 compatible, PostToolUse hook, user-invocable | See [releases](https://github.com/OthmanAdi/planning-with-files/releases) |
| **v2.0.x** | Hooks, templates, scripts | See [releases](https://github.com/OthmanAdi/planning-with-files/releases) |
| **v1.0.0** (legacy) | Core 3-file pattern | `git clone -b legacy` |

See [CHANGELOG.md](CHANGELOG.md) for details.

## Why This Skill?

On December 29, 2025, [Meta acquired Manus for $2 billion](https://techcrunch.com/2025/12/29/meta-just-bought-manus-an-ai-startup-everyone-has-been-talking-about/). In just 8 months, Manus went from launch to $100M+ revenue. Their secret? **Context engineering**.

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
Filesystem