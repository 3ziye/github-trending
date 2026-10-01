<div align="center">

<img src="assets/banner.svg" alt="DSCODE" width="880">

# ❄ DSCODE

**Write code in your terminal. Plug scripts into a live session. Hand tasks between agents.**

![Watch the 90-second DSCODE demo](assets/demo.gif)

![macOS 14+](https://img.shields.io/badge/macOS-14%2B-111827?logo=apple&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-22.19%2B%20%7C%2024%2B-43853D?logo=node.js&logoColor=white)
![DSH](https://img.shields.io/badge/DSH-0.1.5--rc.2-2563EB)
![License](https://img.shields.io/badge/license-MIT-green)
[![npm](https://img.shields.io/npm/v/@toddzheng024/dscode)](https://www.npmjs.com/package/@toddzheng024/dscode)
[![Release](https://img.shields.io/github/v/release/qiz029/dscode?color=111827&label=release)](https://github.com/qiz029/dscode/releases)
[![Stars](https://img.shields.io/github/stars/qiz029/dscode?color=111827)](https://github.com/qiz029/dscode/stargazers)
[![Discussions](https://img.shields.io/github/discussions/qiz029/dscode?color=111827&label=discussions)](https://github.com/qiz029/dscode/discussions)

[English](README.md) · [简体中文](README.zh-CN.md)

[Core features](#-core-features) · [What's new](#-whats-new) · [Quick start](#-quick-start) · [Commands](#-commands) · [Changelog](docs/CHANGELOG.md) · [Docs](#-documentation)

</div>

DSCODE is a terminal coding agent for macOS, built on [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness). A persistent shell reads and writes code and runs tests; the TUI, the CLI and your scripts all share one session runtime instead of each starting their own. It installs as a pinned, reproducible harness—DSH dependencies, TUI and plugins are versioned and verified together.

Most coding agents work alone. DSCODE is built on the opposite assumption: sessions on your machine are **visible to each other**, so one can hand a task over, another can review the diff, and an independent reviewer decides approvals from **your instruction** rather than from a rule table.

**See it in 60 seconds.** Three things most coding agents cannot do, and where to look:

| In one terminal | What it shows |
|---|---|
| `/btw why is the cache cold on the first turn?` | A side question runs in its own read-only child session and answers in a panel; the exchange never enters the main conversation. |
| `dscode send <session-id> --steer "review the change in parser.ts and reply"` | Work handed to another session on this machine; it can read your transcript, answer, and hand the result back. |
| `/permission auto-review` · `/review-usage` | Approvals decided by an independent reviewer from your instruction, with what it allowed and what it cost. |

The [90-second demo script](docs/demo.md) has the shot list, the exact commands, and how to record it.

## 🧭 Core features

| Feature | What you get |
|---|---|
| **[Agentic coding loop](docs/dscode-ultra.md)** | A persistent shell that keeps cwd, environment and background jobs, plus file edits, search, patch application and tests. Project instructions, skills, plan, goal and hooks are wired in. |
| **[Session bridge](docs/session-bridge.md)** | Start a task in the TUI, then add requirements, read output or subscribe to progress from another terminal (`dscode sessions`, `send`, `read`, `watch`). Every source enters the same runtime and context, and readers never take the session write lock. |
| **[Agent-to-agent tasks](docs/session-communication.md)** | The agent finds, reads and messages other sessions with `list_sessions`, `read_session`, `send_session` and `reply_session`, choosing `queue`, `steer` or `defer`. A persisted mailbox, retry de-duplication and a finite budget bound message loss, double processing and wake-up loops. |
| **[Session cards](docs/session-cards.md)** | Each session advertises its project, workspace and the topics of its last five user requests—enough to pick the right collaborator without reading its transcript. Cards describe what the user asked for, not conclusions. |
| **[Cross-session memory](docs/memory.md)** | Reusable experience is extracted in the background and retrieved together with its workspace and source messages. Memory can be disabled per session or globally, and its model usage is tracked separately. |
| **[Effort and sub-agents](docs/dscode-ultra.md)** | Ultra uses the model's `max` reasoning and decides how far to investigate, delegate and verify; below Ultra the agent can still delegate, but only when a task clearly warrants it. Parents pick a separate effort per child, and children that edit can work in isolated Git worktrees created from a clean `HEAD`. |
| **[Independent review](docs/tui-commands.md)** | After a code change passes its relevant checks, the agent sends the Git diff—or, outside a repository, the changes since a snapshot taken when the task began—to a separate read-only model and fixes concrete findings before ending the turn. `/review` runs the same reviewer by hand, scoped to the staging area, a base branch, a commit or a pa