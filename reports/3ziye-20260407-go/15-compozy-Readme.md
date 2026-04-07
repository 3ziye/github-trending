<div align="center">
  <h1>Compozy</h1>
  <p><strong>Orchestrate AI coding agents from idea to shipped code — in a single pipeline.</strong></p>
  <p>
    <a href="https://github.com/compozy/compozy/actions/workflows/ci.yml">
      <img src="https://github.com/compozy/compozy/actions/workflows/ci.yml/badge.svg" alt="CI">
    </a>
    <a href="https://pkg.go.dev/github.com/compozy/compozy">
      <img src="https://pkg.go.dev/badge/github.com/compozy/compozy.svg" alt="Go Reference">
    </a>
    <a href="https://goreportcard.com/report/github.com/compozy/compozy">
      <img src="https://goreportcard.com/badge/github.com/compozy/compozy" alt="Go Report Card">
    </a>
    <a href="LICENSE">
      <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT">
    </a>
    <a href="https://github.com/compozy/compozy/releases">
      <img src="https://img.shields.io/github/v/release/compozy/compozy?include_prereleases" alt="Release">
    </a>
  </p>
</div>

One CLI to replace scattered prompts, manual task tracking, and copy-paste review cycles. Compozy drives the full lifecycle of AI-assisted development: product ideation, technical specification, task breakdown with codebase-informed enrichment, concurrent execution across agents, and automated PR review remediation.

<div align="center">
  <img src="imgs/screenshot.png" alt="Compozy Agent Loop" width="100%">
</div>

## ✨ Highlights

- **One command, 40+ agents.** Install bundled skills into Claude Code, Codex, Cursor, Droid, OpenCode, Pi, Gemini, and 40+ other agents and editors with `compozy setup`.
- **Idea to code in a structured pipeline.** Optional Idea → PRD → TechSpec → Tasks → Execution → Review. Each phase produces plain markdown artifacts that feed into the next. Start from an idea for full research and debate, or jump straight to PRD if you already have a clear scope.
- **Codebase-aware enrichment.** Tasks aren't generic prompts. Compozy spawns parallel agents to explore your codebase, discover patterns, and ground every task in real project context.
- **Multi-agent execution.** Run tasks through ACP-capable runtimes like Claude Code, Codex, Cursor, Droid, OpenCode, Pi, or Gemini — just change `--ide`. Concurrent batch processing with configurable timeouts, retries, and exponential backoff, all with a live terminal UI.
- **Workflow memory between runs.** Agents inherit context from every previous task — decisions, learnings, errors, and handoffs. Two-tier markdown memory with automatic compaction keeps context fresh without manual bookkeeping.
- **Provider-agnostic reviews.** Fetch review comments from CodeRabbit, GitHub, or run AI-powered reviews internally. All normalize to the same format. Provider threads resolve automatically after fixes.
- **Markdown everywhere.** PRDs, specs, tasks, reviews, and ADRs are human-readable markdown files. Version-controlled, diffable, editable between steps. No vendor lock-in.
- **Frontmatter for machine-readable metadata.** Tasks and review issues keep parseable metadata in standard YAML frontmatter instead of custom XML tags.
- **Single binary, local-first.** Compiles to one Go binary with zero runtime dependencies. Your code and data stay on your machine.
- **Embeddable.** Use as a standalone CLI or import as a Go package into your own tools.

## 📦 Installation

#### Homebrew

```bash
brew tap compozy/compozy
brew install --cask compozy
```

#### NPM

```bash
npm install -g @compozy/cli
```

#### Go

```bash
go install github.com/compozy/compozy/cmd/compozy@latest
```

#### From Source

```bash
git clone git@github.com:compozy/compozy.git
cd compozy && make verify && go build ./cmd/compozy
```

Then install bundled skills into your AI agents:

```bash
compozy setup          # interactive — pick agents and skills
compozy setup --all    # install everything to every detected agent
```

Execution runtimes are separate from skill installation. To run `compozy exec`, `compozy start`, or `compozy fix-reviews`, install an ACP-capable runtime or adapter on `PATH` for the `--ide` you choose:

| Runtime      | `--ide` flag   | Expected ACP command             |
| ------------ | -------------- | -------------------------------- |
| Claude Agent | `claude`       | `claude-agent-acp`               |
| Codex CLI    | `codex`        | `codex-acp`                      |
| GitHub Copilot CLI | `copilot` | `copilot --acp`                  |
| Cursor       | `cursor-agent` | `cursor-agent acp`               |
| Droid        | `droid`        | `droid exec --output-format acp` |
| OpenCode     | `opencode`     | `opencode acp`                   |
| pi ACP       | `pi`           | `pi-acp`                         |
| Gemini CLI   | `gemini`       | `gemini --acp`                   |

When the direct ACP command is not installed, Compozy can also fall back to supported launchers such as `npx @zed-industries/codex-acp` when the launcher is available locally.

## 🔄 How It Works

<div align="center">
  <img src="imgs