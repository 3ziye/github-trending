<p align="center">
  <img src="images/beacon-hero.png" alt="Beacon" width="860">
</p>

<h1 align="center">Asymptote Lab's Agent Beacon</h1>

<p align="center">
  <a href="https://github.com/asymptote-labs/agent-beacon/releases"><img src="https://img.shields.io/github/v/release/asymptote-labs/agent-beacon" alt="GitHub release"></a>
  <a href="https://github.com/asymptote-labs/homebrew-tap"><img src="https://img.shields.io/badge/homebrew-beacon-fbb040?logo=homebrew" alt="Homebrew"></a>
  <a href="https://github.com/asymptote-labs/agent-beacon/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/asymptote-labs/agent-beacon/ci.yml" alt="GitHub Workflow Status"></a>
  <a href="https://github.com/asymptote-labs/agent-beacon/blob/main/LICENSE"><img src="https://img.shields.io/github/license/asymptote-labs/agent-beacon" alt="MIT license"></a>
  <a href="https://docs.asymptotelabs.ai/cli"><img src="https://img.shields.io/badge/docs-asymptotelabs.ai-0369a1" alt="Docs"></a>
  <a href="https://discord.gg/zdNChS2fBu"><img src="https://img.shields.io/badge/discord-community-5865F2?logo=discord&logoColor=white" alt="Discord"></a>
</p>

<p align="center">
  <strong>Unified endpoint telemetry for AI agents.</strong>
</p>

<p align="center">
  <a href="https://docs.asymptotelabs.ai/cli">Docs</a>
  ·
  <a href="https://discord.gg/zdNChS2fBu">Discord</a>
  ·
  <a href="https://docs.asymptotelabs.ai/cli/installation">Install</a>
  ·
  <a href="https://docs.asymptotelabs.ai/cli/security-it-teams">For Security & IT Teams</a>
  ·
  <a href="https://docs.asymptotelabs.ai/cli/dashboard">Dashboard</a>
  ·
  <a href="https://docs.asymptotelabs.ai/cli/command-reference">Commands</a>
</p>

## What is Agent Beacon

Agent Beacon is [Asymptote's open-source endpoint agent](https://justindsouza.substack.com/p/introducing-beacon-endpoint-telemetry) for security and IT teams that
need visibility into local AI agent activity.

It runs locally, captures all agent activity (e.g. prompts, tool use, file edits, etc.) from
all the [major local agent harnesses](#agent-runtimes), then
normalizes that activity into endpoint events your team can inspect and retain
locally.

Beacon is built to be easy to deploy for Security and IT teams through
[MDM deployment](#mdm-deployment) and to
emit agent harness telemetry logs to
[all the major enterprise-grade SIEMs](#siem--output-destinations).

Learn more in the [Agent Beacon Documentation](https://docs.asymptotelabs.ai/cli).

## High-Level Architecture

Beacon keeps collection, processing, and inspection local to the endpoint while
leaving forwarding under customer control.

<p align="center">
  <img src="images/beacon-architecture.png" alt="Beacon endpoint architecture" width="860">
</p>

- **Agent runtime layer:** Local hooks and OpenTelemetry sources capture
  supported activity from AI agent harnesses on the endpoint.
- **Beacon endpoint layer:** Local processing normalizes events, applies
  retention and redaction settings, and writes durable endpoint telemetry.
- **Output layer:** Teams inspect events in the local dashboard, retain JSONL,
  or forward records into all the major enterprise-grade SIEMs.

## Supported Surfaces

Beacon captures supported agent harness activity locally and writes normalized
endpoint events that teams can inspect in place or forward into customer-managed
security pipelines.

### Agent Runtimes

Agent Beacon supports the most popular enterprise coding agent harnesses (e.g.
Claude Code, Codex, Cursor, etc.) and knowledge worker agent harnesses (e.g.
Claude Cowork, OpenClaw).

#### Coding Agent Harnesses

| Agent harness | Support path |
| --- | --- |
| [Antigravity CLI](https://docs.asymptotelabs.ai/cli/supported-runtimes-antigravity-cli) | Beacon hook adapter |
| [Claude Code](https://docs.asymptotelabs.ai/cli/supported-runtimes-claude-code) | Local OpenTelemetry configuration or Beacon hook adapter |
| [Codex CLI](https://docs.asymptotelabs.ai/cli/supported-runtimes-codex-cli) | Local OpenTelemetry configuration |
| [Cursor](https://docs.asymptotelabs.ai/cli/supported-runtimes-cursor) | Beacon hook adapter |
| [Devin CLI](https://docs.asymptotelabs.ai/cli/supported-runtimes-devin) | Beacon hook adapter |
| [Devin Desktop](https://docs.asymptotelabs.ai/cli/supported-runtimes-devin-desktop) | Beacon hook adapter via Cascade/Windsurf hooks |
| [Factory Droid](https://docs.asymptotelabs.ai/cli/supported-runtimes-factory-droid) | Local OpenTelemetry configuration and optional hook adapter |
| [Gemini CLI](https://docs.asymptotelabs.ai/cli/supported-runtimes-gemini-cli) | Opt-in local OpenTelemetry configuration |
| [GitHub Copilot CLI](https://docs.asymptotelabs.ai/cli/supported-runtimes-github-copilot-cli) | MDM-managed OpenTelemetry (OTLP HTTP) |
| [Grok Build](https://docs.asymptotelabs.ai/cli/supported-runtimes-grok-build) | Beacon hook adapter |
| [OpenCode](https://docs.asymptotelabs.ai/cli/supported-runtimes-opencode) | Beacon hook adap