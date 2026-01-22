# zeroshot CLI

> **🎉 New in v5.4:** Now supports **OpenCode** CLI! Use Claude, Codex, Gemini, or OpenCode as your AI provider. Also supports **GitHub, GitLab, Jira, and Azure DevOps** as issue backends. See [Providers](#providers) and [Multi-Platform Issue Support](#multi-platform-issue-support).

<!-- install-placeholder -->
<p align="center">
  <code>npm install -g @covibes/zeroshot</code>
</p>

<p align="center">
  <img src="./docs/assets/zeroshot-demo.gif" alt="Demo" width="700">
  <br>
  <em>Demo (100x speed, 90-minute run, 5 iterations to approval)</em>
</p>

[![CI](https://github.com/covibes/zeroshot/actions/workflows/ci.yml/badge.svg)](https://github.com/covibes/zeroshot/actions/workflows/ci.yml)
[![npm version](https://img.shields.io/npm/v/@covibes/zeroshot.svg)](https://www.npmjs.com/package/@covibes/zeroshot)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Node 18+](https://img.shields.io/badge/node-18%2B-brightgreen.svg)](https://nodejs.org/)
![Platform: Linux | macOS](https://img.shields.io/badge/platform-Linux%20%7C%20macOS-blue.svg)

<!-- discord-placeholder -->

[![Discord](https://img.shields.io/badge/Discord-Join-5865F2?logo=discord&logoColor=white)](https://discord.gg/PdZ3UEXB)

Zeroshot is an open-source AI coding agent orchestration CLI that runs multi-agent workflows to autonomously implement, review, test, and verify code changes.

It runs a **planner**, an **implementer**, and independent **validators** in isolated environments, looping until changes are **verified** or **rejected** with actionable, reproducible failures.

Built for tasks where correctness matters more than speed.

## How It Works

- Plan: translate a task into concrete acceptance criteria
- Implement: make changes in an isolated workspace (local, worktree, or Docker)
- Validate: run automated checks with independent validators
- Iterate: repeat until verified, or return actionable failures
- Resume: crash-safe state persisted for recovery

## Quick Start

```bash
zeroshot run 123                    # GitHub issue number
zeroshot run feature.md             # Markdown file
zeroshot run "Add dark mode"        # Inline text
```

Or describe a complex task inline:

```bash
zeroshot run "Add optimistic locking with automatic retry: when updating a user,
retry with exponential backoff up to 3 times, merge non-conflicting field changes,
and surface conflicts with details. Handle the ABA problem where version goes A->B->A."
```

## Why Not Just Use a Single AI Agent?

| Approach                   | Writes Code | Runs Tests | Blind Validation | Iterates Until Verified |
| -------------------------- | ----------- | ---------- | ---------------- | ----------------------- |
| Chat-based assistant       | ✅          | ⚠️         | ❌               | ❌                      |
| Single coding agent        | ✅          | ⚠️         | ❌               | ⚠️                      |
| **Zeroshot (multi-agent)** | ✅          | ✅         | ✅               | ✅                      |

## Use Cases

- Autonomous AI code refactoring
- AI-powered pull request automation
- Automated bug fixing with validation
- Multi-agent code generation for software engineering
- Agentic coding workflows with blind validation

## Who Is This For?

- Senior engineers who care about correctness and reproducibility
- Teams automating PR workflows and code review gates
- Infra/platform teams standardizing agentic workflows
- Open-source maintainers working through issue backlogs
- AI power users who want verification, not vibes

## Install and Requirements

**Platforms**: Linux, macOS (Windows WSL not yet supported)

```bash
npm install -g @covibes/zeroshot
```

**Requires**: Node 18+, at least one provider CLI (Claude Code, Codex, Gemini, Opencode).

```bash
# Install one or more providers
npm i -g @anthropic-ai/claude-code
npm i -g @openai/codex
npm i -g @google/gemini-cli
# Opencode: see https://opencode.ai

# Authenticate with the provider CLI
claude login        # Claude
codex login         # Codex
gemini auth login   # Gemini
opencode auth login # Opencode

# GitHub auth (for issue numbers)
gh auth login
```

## Providers

Zeroshot shells out to provider CLIs. Pick a default and override per run:

```bash
zeroshot providers
zeroshot providers set-default codex
zeroshot run 123 --provider gemini
```

See `docs/providers.md` for setup, model levels, and Docker mounts.

## Why Multiple Agents?

Single-agent sessions degrade. Context gets buried under thousands of tokens. The model optimizes for "done" over "correct."

Zeroshot fixes this with isolated agents that check each other's work. Validators can't lie about code they didn't write. Fail the check? Fix and retry until it actually works.

## What Makes It Different

- **Blind validation** - Validators never see the worker's context or code history
- **Repeatable workflows** - Task complexity determines agent count and model selection
- **Accept/reject loop** - Rejections inc