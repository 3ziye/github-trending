# agentic-stack

**Keep one portable memory-and-skills layer across coding-agent harnesses, so switching tools doesn't reset how your agent works.**

A portable `.agent/` folder (memory + skills + protocols) that plugs into Claude Code, Cursor, Windsurf, OpenCode, OpenClaw, Hermes, Pi Coding Agent, Codex, Antigravity, or a DIY Python loop — and keeps its knowledge when you switch.

It also includes a local data layer so you can monitor the whole suite of
agents from one place: harness activity, cron runs, active agents, token/cost
estimates, KPI summaries, user-defined resource categories, and
screenshot-ready daily dashboards.

<p align="center">
  <img src="docs/data-layer.svg" alt="agentic-stack data layer dashboard flow" width="880"/>
</p>

And it can turn approved, redacted runs into local flywheel artifacts:
trace records, context cards, eval cases, training-ready JSONL, and readiness
metrics without training a model or sending telemetry.

<p align="center">
  <img src="docs/demo.gif" alt="agentic-stack demo" width="880"/>
</p>

<p align="center">
  <img src="docs/diagram.svg" alt="agentic-stack architecture" width="880"/>
</p>

### New in v0.13.0 — transfer wizard

Minor release. Adds an onboarding-style `agentic-stack transfer` wizard for
moving a project brain into Codex, Cursor, Windsurf, or a terminal-only
`AGENTS.md` setup.

- **Natural-language transfer plans.** Say things like `move my memory into
  Codex`; the wizard detects targets, memory scopes, and whether to generate a
  curl command, apply locally, or both.
- **Portable memory bundles.** Transfers preferences, accepted lessons,
  skills, working memory, episodic/history logs, and candidate lessons, with
  SHA-256 verification and secret-like content blocking.
- **One-line import.** Generated curl/PowerShell bootstraps import the bundle
  into another project and install the selected adapter files.
- **Modern Windsurf rules.** Windsurf now gets `.windsurf/rules/agentic-stack.md`
  while keeping legacy `.windsurfrules` compatibility.

See [CHANGELOG.md](CHANGELOG.md) for the full list.

### v0.12.0 — tldraw visual canvas

Minor release. Adds an opt-in `tldraw` seed skill for live canvas diagrams and
a skill-local snapshot store. It is beta and off by default.

- **`tldraw` seed skill.** Draw, diagram, sketch, wireframe, flowchart, and
  whiteboard on a live canvas at `http://localhost:3030` through an MCP server.
- **Skill-local snapshots.** Save worthwhile canvases with
  `.agent/skills/tldraw/store.py snapshot`; list, load, and archive them later
  without treating them as a fifth memory layer.
- **Opt-in beta.** Onboarding writes `tldraw.enabled: false` by default. After
  enabling it, users manually merge `adapters/_shared/tldraw-mcp.json` into
  their harness MCP config.

### v0.11.0 — data layer + data flywheel

Added two local-first data capabilities for teams running multiple agent
harnesses against the same `.agent/` brain.

- **`data-layer` seed skill.** Generate local dashboard exports across Claude
  Code, Hermes, OpenClaw, Codex, Cursor, OpenCode, and custom loops:
  harness events, cron timelines, KPI summaries, token/cost estimates,
  categories, `dashboard.html`, and `daily-report.md`. The skill also acts as
  the injected natural-language surface for showing the terminal dashboard.
- **`data-flywheel` seed skill.** Export approved, redacted runs into trace
  records, context cards, eval cases, training-ready JSONL, and flywheel
  metrics. It is local-only and model-agnostic; it prepares artifacts but
  does not train models or call external APIs.

### v0.10.0 — design-md skill + Python 3.9 fix

Added the `design-md` seed skill for root `DESIGN.md` / Google Stitch
workflows, and fixed the Python 3.9 crash that hit macOS-default brew users
on first run.

### v0.9.1 — pi adapter fixes + tz correctness

Closed the gap between v0.9.0 and a working pi adapter, plus a timezone
sweep across every Python writer/reader so the dream cycle stops drifting
against the UTC decay window.

### v0.9.0 — harness manager

<p align="center">
  <img src="docs/harness-manager.svg" alt="harness manager v0.9.0" width="880"/>
</p>

Manifest-driven adapter system: every harness is now declared by an
`adapter.json`, applied by a shared Python backend, and managed via
verb subcommands or an interactive TUI. Cross-platform (POSIX +
Windows) with concurrent-write protection, pre-v0.9 migration via
`./install.sh doctor`, and shared-file ownership tracking so removing
one adapter never orphans another.

[![GitHub release](https://img.shields.io/github/v/release/codejunkie99/agentic-stack)](https://github.com/codejunkie99/agentic-stack/releases)
[![License: Apache 2.0](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
Made by https://x.com/Av1dlive

## Quickstart

### macOS / Linux

```bash
# tap + install (one-time — both lines required)
brew tap codejunkie99/agentic-stack https://github.com/codejunkie99/agentic-stack
brew install age