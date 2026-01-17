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
[![Version](https://img.shields.io/badge/version-2.1.2-brightgreen)](https://github.com/OthmanAdi/planning-with-files/releases)

## Quick Install

```bash
/plugin marketplace add OthmanAdi/planning-with-files
/plugin install planning-with-files@planning-with-files
```

See [docs/installation.md](docs/installation.md) for all installation methods.

## Documentation

| Document | Description |
|----------|-------------|
| [Installation Guide](docs/installation.md) | All installation methods (plugin, manual, Cursor, Windows) |
| [Quick Start](docs/quickstart.md) | 5-step guide to using the pattern |
| [Workflow Diagram](docs/workflow.md) | Visual diagram of how files and hooks interact |
| [Troubleshooting](docs/troubleshooting.md) | Common issues and solutions |
| [Cursor Setup](docs/cursor.md) | Cursor IDE-specific instructions |
| [Windows Setup](docs/windows.md) | Windows-specific notes |

## Versions

| Version | Features | Install |
|---------|----------|---------|
| **v2.1.2** (current) | Fix template cache issue (Issue #18) | `/plugin install planning-with-files@planning-with-files` |
| **v2.1.1** | Fix plugin template paths | See [releases](https://github.com/OthmanAdi/planning-with-files/releases) |
| **v2.1.0** | Claude Code v2.1 compatible, SessionStart hook, PostToolUse hook, user-invocable | See [releases](https://github.com/OthmanAdi/planning-with-files/releases) |
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
Filesystem = Disk (persistent, unlimited)

→ Anything important gets written to disk.
```

## Usage

Once installed, Claude will automatically:

1. **Create `task_plan.md`** before starting complex tasks
2. **Re-read plan** before major decisions (via PreToolUse hook)
3. **Remind you** to update status after file writes (via PostToolUse hook)
4. **Store findings** in `findings.md` instead of stuffing context
5. **Log errors** for future reference
6. **Verify completion** before stopping (via Stop hook)

Or invoke manually with `/planning-with-files`.

See [docs/quickstart.md](docs/quickstart.md) for the full 5-step guide.

## Key Rules

1. **Create Plan First** — Never start without `task_plan.md`
2. **The 2-Action Rule** — Save findings after every 2 view/browser operations
3. **Log ALL Errors** — They help avoid repetition
4. **Never Repeat Failures** — Track attempts, mutate approach

## File Structure

```
planning-with-files/
├── templates/               # Root-level templates (for CLAUDE_PLUGIN_ROOT)
├── scripts/                 # Root-level scripts (for CLAUDE_PLUGIN_ROOT)
├── docs/                    # Documentation
│   ├── installation.md
│   ├── qu