<div align="center">

# Harmonist

### Portable AI agent orchestration with mechanical protocol enforcement

*A drop-in multi-agent framework for Cursor, Claude Code, Copilot, Windsurf, Aider, and other AI coding assistants.*

[![GitHub stars](https://img.shields.io/github/stars/GammaLabTechnologies/harmonist?style=flat&logo=github&color=yellow)](https://github.com/GammaLabTechnologies/harmonist/stargazers)
[![CI](https://github.com/GammaLabTechnologies/harmonist/actions/workflows/ci.yml/badge.svg)](https://github.com/GammaLabTechnologies/harmonist/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Version 1.0.0](https://img.shields.io/badge/version-1.0.0-brightgreen.svg)](CHANGELOG.md)
[![Agents: 186](https://img.shields.io/badge/agents-186-purple.svg)](agents/index.json)
[![Tests: 430+](https://img.shields.io/badge/tests-430+-success.svg)](#testing)
[![Stdlib only](https://img.shields.io/badge/dependencies-stdlib%20only-lightgrey.svg)](#requirements)

**Built and maintained by [GammaLab](https://gammalab.ae) · [@GammaLabTechnologies](https://github.com/GammaLabTechnologies)**

</div>

---

Most AI coding frameworks trust the language model to follow the
rules. Harmonist **refuses to let it skip them**. Every code-changing
turn is gated by hooks that check whether the required reviewers ran,
whether memory was updated, and whether the supply chain of every
shipped file is intact. If the checks fail, the turn doesn't complete —
no matter how confidently the model claims it's done.

This is the first open-source agent framework where **protocol
enforcement is a mechanical gate, not a polite request in a prompt**.

---

## Table of contents

- [Why Harmonist exists](#why-harmonist-exists)
- [What makes it different](#what-makes-it-different)
- [Requirements](#requirements)
- [Quick start](#quick-start)
- [Architecture](#architecture)
- [The 186-agent catalogue](#the-186-agent-catalogue)
- [Mechanical enforcement](#mechanical-enforcement)
- [Structured validated memory](#structured-validated-memory)
- [Supply-chain integrity](#supply-chain-integrity)
- [Supported IDE integrations](#supported-ide-integrations)
- [Key scripts](#key-scripts)
- [Documentation](#documentation)
- [Testing](#testing)
- [FAQ](#faq)
- [Contributing](#contributing)
- [Security](#security)
- [License](#license)
- [About GammaLab](#about-gammalab)

---

## Why Harmonist exists

AI coding assistants have a structural problem that prompt engineering
alone cannot fix.

**The problem:** every serious engineering workflow has non-negotiable
rules — "no floating-point for money", "run QA before merging", "every
external call retries with idempotency keys", "security review before
touching auth code". An LLM can be *told* to follow them, but there is
no mechanism forcing it to. It can agree, move on, and silently skip
the step. On a good day you notice. On a bad day the bug ships.

**The current landscape** is split between two imperfect answers:

- **Thin agent frameworks** (LangChain, CrewAI, AutoGen, MetaGPT and
  many others) give you orchestration primitives but leave enforcement
  to the prompt. The model can always override its own protocol.
- **Heavy enterprise platforms** promise governance through separate
  runtimes, databases, and vendor lock-in — but need infrastructure to
  install, don't work on a solo developer's laptop, and can't be
  audited file-by-file.

**Harmonist takes a different stance.** Protocol enforcement is
implemented as IDE-level hooks — concrete shell and Python scripts that
observe every subagent dispatch, every file edit, every session stop.
When the rules the project declared aren't met, the `stop` hook
returns a `followup_message` to the AI and refuses to allow the turn
to complete. The model can't argue with that; it's a state machine on
disk.

No runtime. No database. No vendor lock-in. Just markdown, stdlib
Python, and bash — sitting next to your code, doing one job
correctly.

---

## What makes it different

Seven concrete, checkable properties — each one addresses a gap that
other open-source agent frameworks leave open.

### 1. Mechanical protocol enforcement via IDE hooks

The `stop` hook in `.cursor/hooks/` parses subagent dispatch markers
from the session, checks whether `qa-verifier` ran, whether any
required reviewer was missing, whether `session-handoff.md` was
updated, and returns a structured `followup_message` if the turn
is incomplete. `loop_limit: 3` caps retries. On exhaustion, an
incident is recorded and surfaced in the next session. **The AI
literally cannot ship a code change that skipped review.**

### 2. Supply-chain verification of agent definitions

Every shipped file is hashed in `MANIFEST.sha256`. `upgrade.py`
sha-verifies each source *before* copying into a project. A tampered
`security-reviewer.md` (say, one that returns 