English | [한국어](README.ko.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [Español](README.es.md)

# oh-my-claudecode

[![npm version](https://img.shields.io/npm/v/oh-my-claude-sisyphus?color=cb3837)](https://www.npmjs.com/package/oh-my-claude-sisyphus)
[![npm downloads](https://img.shields.io/npm/dm/oh-my-claude-sisyphus?color=blue)](https://www.npmjs.com/package/oh-my-claude-sisyphus)
[![GitHub stars](https://img.shields.io/github/stars/Yeachan-Heo/oh-my-claudecode?style=flat&color=yellow)](https://github.com/Yeachan-Heo/oh-my-claudecode/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Sponsor](https://img.shields.io/badge/Sponsor-❤️-red?style=flat&logo=github)](https://github.com/sponsors/Yeachan-Heo)

**Multi-agent orchestration for Claude Code. Zero learning curve.**

*Don't learn Claude Code. Just use OMC.*

[Get Started](#quick-start) • [Documentation](https://yeachan-heo.github.io/oh-my-claudecode-website) • [Migration Guide](docs/MIGRATION.md)

---

## Quick Start

**Step 1: Install**
```bash
/plugin marketplace add https://github.com/Yeachan-Heo/oh-my-claudecode
/plugin install oh-my-claudecode
```

**Step 2: Setup**
```bash
/oh-my-claudecode:omc-setup
```

**Step 3: Build something**
```
autopilot: build a REST API for managing tasks
```

That's it. Everything else is automatic.

### Updating

```bash
# 1. Update the plugin
/plugin install oh-my-claudecode

# 2. Re-run setup to refresh configuration
/oh-my-claudecode:omc-setup
```

If you experience issues after updating, clear the old plugin cache:

```bash
/oh-my-claudecode:doctor
```

<h1 align="center">Your Claude Just Have been Steroided.</h1>

<p align="center">
  <img src="assets/omc-character.jpg" alt="oh-my-claudecode" width="400" />
</p>

---

## Why oh-my-claudecode?

- **Zero configuration required** - Works out of the box with intelligent defaults
- **Natural language interface** - No commands to memorize, just describe what you want
- **Automatic parallelization** - Complex tasks distributed across specialized agents
- **Persistent execution** - Won't give up until the job is verified complete
- **Cost optimization** - Smart model routing saves 30-50% on tokens
- **Learn from experience** - Automatically extracts and reuses problem-solving patterns
- **Real-time visibility** - HUD statusline shows what's happening under the hood

---

## Features

### Execution Modes
Multiple strategies for different use cases - from fully autonomous builds to token-efficient refactoring. [Learn more →](https://yeachan-heo.github.io/oh-my-claudecode-website/docs.html#execution-modes)

| Mode | Speed | Use For |
|------|-------|---------|
| **Autopilot** | Fast | Full autonomous workflows |
| **Ultrawork** | Parallel | Maximum parallelism for any task |
| **Ralph** | Persistent | Tasks that must complete fully |
| **Ultrapilot** | 3-5x faster | Multi-component systems |
| **Ecomode** | Fast + 30-50% cheaper | Budget-conscious projects |
| **Swarm** | Coordinated | Parallel independent tasks |
| **Pipeline** | Sequential | Multi-stage processing |

### Intelligent Orchestration

- **32 specialized agents** for architecture, research, design, testing, data science
- **Smart model routing** - Haiku for simple tasks, Opus for complex reasoning
- **Automatic delegation** - Right agent for the job, every time

### Developer Experience

- **Magic keywords** - `ralph`, `ulw`, `eco`, `plan` for explicit control
- **HUD statusline** - Real-time orchestration metrics in your status bar
- **Skill learning** - Extract reusable patterns from your sessions
- **Analytics & cost tracking** - Understand token usage across all sessions

[Full feature list →](docs/REFERENCE.md)

---

## Magic Keywords

Optional shortcuts for power users. Natural language works fine without them.

| Keyword | Effect | Example |
|---------|--------|---------|
| `autopilot` | Full autonomous execution | `autopilot: build a todo app` |
| `ralph` | Persistence mode | `ralph: refactor auth` |
| `ulw` | Maximum parallelism | `ulw fix all errors` |
| `eco` | Token-efficient execution | `eco: migrate database` |
| `plan` | Planning interview | `plan the API` |
| `ralplan` | Iterative planning consensus | `ralplan this feature` |

**ralph includes ultrawork:** When you activate ralph mode, it automatically includes ultrawork's parallel execution. No need to combine keywords.

---

## Utilities

### Rate Limit Wait

Auto-resume Claude Code sessions when rate limits reset.

```bash
omc wait          # Check status, get guidance
omc wait --start  # Enable auto-resume daemon
omc wait --stop   # Disable daemon
```

**Requires:** tmux (for session detection)

---

## Documentation

- **[Full Reference](docs/REFERENCE.md)** - Complete feature documentation
- **[Performance Monitoring](docs/PERFORMANCE-MONITORING.md)** - Agent tracking, debugging, and optimization
- **[Website](https://yeachan-heo.github.io/oh-my-claudecode-website