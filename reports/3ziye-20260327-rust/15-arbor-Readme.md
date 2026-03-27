<p align="center">
  <a href="assets/screenshot.png">
    <img src="assets/screenshot.png" alt="Arbor UI screenshot" width="1100" />
  </a>
</p>

# Arbor

[![CI](https://github.com/penso/arbor/actions/workflows/ci.yml/badge.svg)](https://github.com/penso/arbor/actions/workflows/ci.yml)
[![Rust Nightly](https://img.shields.io/badge/rust-nightly--2025--11--30-orange?logo=rust)](https://rust-lang.org)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![GitHub Release](https://img.shields.io/github/v/release/penso/arbor?label=release)](https://github.com/penso/arbor/releases)
[![macOS](https://img.shields.io/badge/macOS-supported-brightgreen)](#install)
[![Linux](https://img.shields.io/badge/Linux-supported-brightgreen)](#install)
[![Windows](https://img.shields.io/badge/Windows-supported-brightgreen)](#install)
[![CodSpeed](https://img.shields.io/endpoint?url=https://codspeed.io/badge.json)](https://codspeed.io/penso/arbor?utm_source=badge)

Arbor is a **fully native app for agentic coding** built with Rust and [GPUI](https://gpui.rs).
It gives you one place to manage repositories, issue-driven worktrees, embedded terminals, managed processes, diffs, PR context, AI coding agent activity, and a shared daemon that also powers Arbor's web UI, CLI, and MCP server.

## Why Arbor

- Fully native desktop app, UI and terminal stack included, optimized for long-running local workflows
- One daemon-backed model for the desktop app, web UI, CLI, and MCP server
- Built for parallel coding sessions across local repos, issue queues, and remote outposts

## Core Capabilities

### Repositories, Worktrees, and Issues
- List, create, and delete worktrees across multiple repositories
- Create managed worktrees directly from GitHub or GitLab issues
- Preview sanitized worktree names, branch names, and target paths before creation
- Repo-local branch naming rules via `[branch]` in `arbor.toml`
- Delete confirmation with unpushed commit detection
- Optional branch cleanup on worktree deletion
- Worktree navigation history (back/forward)
- Last git activity timestamp per worktree
- Automatic issue linking to existing branches and open PRs / MRs

### Embedded Terminal, Processes, and Tasks
- Built-in PTY terminal with truecolor and `xterm-256color` support
- Multiple terminal tabs per worktree
- Experimental embedded `libghostty-vt` engine behind a compile-time feature flag, used by default when available
- Persistent daemon-based sessions (survive app restarts)
- Session attach/detach and signals (interrupt/terminate/kill)
- Managed processes from both `Procfile` and `arbor.toml`
- Process restart state, memory metrics, and terminal-session linkage
- Scheduled `[[tasks]]` from `arbor.toml`, with optional Claude or Codex triggers
- Bell-aware terminal activity and completion notifications

### Diff, PR, and Review Context
- Side-by-side diff display with addition/deletion line counts
- Changed file listing per worktree
- File tree browsing with directory expand/collapse
- Multi-tab diff sessions
- PR summary and detail cards in the changes pane
- Native inline PR comment actions and review-comment refresh support

### Agent Chat
- Interactive chat sessions with ACP agents (Claude, Codex, Pi, Gemini, and more via acpx)
- OpenAI-compatible provider support: Ollama, LM Studio, OpenRouter, OpenAI, and any `/v1/chat/completions` endpoint
- Streaming responses via SSE for OpenAI-compatible providers and JSONL for ACP agents
- Automatic model discovery: probes `/v1/models` at startup for configured providers
- Model selector with per-provider sections and distinct icons (ACP vs API)
- Provider configuration via `~/.config/arbor/config.toml` `[[providers]]` sections
- Session persistence across daemon restarts
- Token usage tracking and display

### AI Agent Visibility
- Detects running coding agents: Claude Code, Codex, OpenCode
- Working/waiting state indicators with color-coded dots
- Real-time updates over WebSocket streaming in both the desktop and web UI
- Legacy session compatibility and targeted clear events for long-lived daemon sessions

### Remote Daemon and Companion Binaries
- `arbor-httpd` serves the remote daemon API and bundled web UI
- `arbor-cli` exposes daemon-backed health, repo, worktree, terminal, process, and task commands
- Dedicated `arbor-mcp` binary backed by Arbor's daemon API
- Structured MCP tools for repositories, worktrees, terminals, processes, tasks, and agent activity
- MCP resources for daemon snapshots and prompts for common Arbor workflows
- Supports `ARBOR_DAEMON_URL` and `ARBOR_DAEMON_AUTH_TOKEN` for remote authenticated daemons
- Create and manage remote worktrees over SSH
- Multi-host configuration with custom ports and identity files
- Mosh support for better connectivity
- Remote terminal sessions via `arbor-httpd`
- Outpost status tracking (available, unreachable, provisioning)
- Optional Symphony runtime endpoints when the feature is enabled

### UI and Config
- Autom