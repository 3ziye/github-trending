# Continuous Claude

> A persistent, learning, multi-agent development environment built on Claude Code

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude-Code-orange.svg)](https://claude.ai/code)
[![Skills](https://img.shields.io/badge/Skills-109-green.svg)](#skills-system)
[![Agents](https://img.shields.io/badge/Agents-32-purple.svg)](#agents-system)
[![Hooks](https://img.shields.io/badge/Hooks-30-blue.svg)](#hooks-system)

**Continuous Claude** transforms Claude Code into a continuously learning system that maintains context across sessions, orchestrates specialized agents, and eliminates wasting tokens through intelligent code analysis.

## Table of Contents

- [Why Continuous Claude?](#why-continuous-claude)
- [Design Principles](#design-principles)
- [How to Talk to Claude](#how-to-talk-to-claude)
- [Quick Start](#quick-start)
- [Architecture](#architecture)
- [Core Systems](#core-systems)
  - [Skills (109)](#skills-system)
  - [Agents (32)](#agents-system)
  - [Hooks (30)](#hooks-system)
  - [TLDR Code Analysis](#tldr-code-analysis)
  - [Memory System](#memory-system)
  - [Continuity System](#continuity-system)
  - [Math System](#math-system)
- [Workflows](#workflows)
- [Installation](#installation)
- [Updating](#updating)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

---

## Why Continuous Claude?

Claude Code has a **compaction problem**: when context fills up, the system compacts your conversation, losing nuanced understanding and decisions made during the session.

**Continuous Claude solves this with:**

| Problem | Solution |
|---------|----------|
| Context loss on compaction | YAML handoffs - more token-efficient transfer |
| Starting fresh each session | Memory system recalls + daemon auto-extracts learnings |
| Reading entire files burns tokens | 5-layer code analysis + semantic index |
| Complex tasks need coordination | Meta-skills orchestrate agent workflows |
| Repeating workflows manually | 109 skills with natural language triggers |

**The mantra: Compound, don't compact.** Extract learnings automatically, then start fresh with full context.

### Why "Continuous"? Why "Compounding"?

The name is a pun. **Continuous** because Claude maintains state across sessions. **Compounding** because each session makes the system smarter—learnings accumulate like compound interest.

---

## Design Principles

An agent is five things: **Prompt + Tools + Context + Memory + Model**.

| Component | What We Optimize |
|-----------|------------------|
| **Prompt** | Skills inject relevant context; hooks add system reminders |
| **Tools** | TLDR reduces tokens; agents parallelize work |
| **Context** | Not just *what* Claude knows, but *how* it's provided |
| **Memory** | Daemon extracts learnings; recall surfaces them |
| **Model** | Becomes swappable when the other four are solid |

### Anti-Complexity

We resist plugin sprawl. Every MCP, subscription, and tool you add promises improvement but risks breaking context, tools, or prompts through clashes.

**Our approach:**
- **Time, not money** — No required paid services. Perplexity and NIA are optional, high-value-per-token.
- **Learn, don't accumulate** — A system that learns handles edge cases better than one that collects plugins.
- **Shift-left validation** — Hooks run pyright/ruff after edits, catching errors before tests.

The failure modes of complex systems are structurally invisible until they happen. A learning, context-efficient system doesn't prevent all failures—but it recovers and improves.

---

## How to Talk to Claude

**You don't need to memorize slash commands.** Just describe what you want naturally.

### The Skill Activation System

When you send a message, a hook injects context that tells **Claude** which skills and agents are relevant. Claude infers from a rule-based system and decides which tools to use.

```
> "Fix the login bug in auth.py"

🎯 SKILL ACTIVATION CHECK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ CRITICAL SKILLS (REQUIRED):
  → create_handoff

📚 RECOMMENDED SKILLS:
  → fix
  → debug

🤖 RECOMMENDED AGENTS (token-efficient):
  → debug-agent
  → scout

ACTION: Use Skill tool BEFORE responding
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Priority Levels

| Level | Meaning |
|-------|---------|
| ⚠️ **CRITICAL** | Must use (e.g., handoffs before ending session) |
| 📚 **RECOMMENDED** | Should use (e.g., workflow skills) |
| 💡 **SUGGESTED** | Consider using (e.g., optimization tools) |
| 📌 **OPTIONAL** | Nice to have (e.g., documentation helpers) |

### Natural Language Examples

| What You Say | What Activates |
|--------------|----------------|
| "Fix the broken login" | `/fix` workflow → debug-agent, scout |
| "Build a user dashboard" | `/build` workflow → plan-agent, kraken |
| "I want to understand this codebase" | `/explore` + scout agent |
| "What could go wrong with this plan?" | `/premort