<p align="center">
  <img src="assets/logo.svg" alt="Better Harness logo" width="56" height="56">
</p>

<h1 align="center">Better Harness</h1>

<p align="center">
  English · <a href="README.zh-CN.md">简体中文</a>
</p>

<p align="center">
  <strong>Delegate coding to agents. Improve the loop around them.</strong>
</p>

<p align="center">
  Better Harness provides open-source insights for the Agent Work Loop. It runs
  through your Coding Agent and turns project and session evidence into prioritized
  improvements and verifiable next steps. Missing evidence stays explicit.
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/@qoder-ai/better-harness"><img src="https://img.shields.io/npm/v/@qoder-ai/better-harness.svg" alt="npm version"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License"></a>
</p>

<p align="center">
  <a href="https://qoderai.github.io/better-harness/?utm_source=github&utm_medium=referral&utm_campaign=repository_landing&utm_content=readme_hero">Website</a> ·
  <a href="#quick-start">Choose your host</a> ·
  <a href="#see-it-in-action">Sample report</a> ·
  <a href="https://qoderai.github.io/better-harness/docs/introduction">Docs</a>
</p>

## Quick start

Analyze and improve your coding workflow with: [Claude Code](#claude-code), [Codex Desktop](#codex-desktop), [Codex CLI](#codex-cli), [Qoder Desktop/CLI](#qoder), [Cursor](#cursor), or [GitHub Copilot CLI](#github-copilot).

Choose the host you already use to get its exact installation, verification,
invocation, and report-output steps. Better Harness does not use one universal
entrypoint across every host.

This README shows inline setup for the most common hosts. Additional supported
hosts (Qwen Code, Pi, Kimi Code, WorkBuddy, and Grok) keep their steps and
boundaries in the [installation guide](docs/docs/installation.mdx) and the
[public Host Adapter Matrix](docs/docs/hosts/adapter-matrix.md); see
[More adapters](#more-adapters). README placement is a display choice, not a
support-level claim.

Better Harness scopes behavior claims to relevant Task Episodes and the
surrounding project mechanisms. Qoder and Cursor produce host-native Canvas
reports; Claude Code, Codex, Qwen Code, GitHub Copilot, and Kimi Code produce
self-contained HTML with paired Markdown. Missing or partial evidence remains
explicit. See the [Host Adapter Matrix](docs/adapters/README.md) for current
coverage and output differences.

## See it in action

The report keeps missing evidence explicit and turns supported gaps into
prioritized findings with an impact, expected output, scoped repair, and
acceptance checks.

<p align="center">
  <a href="https://qoderai.github.io/better-harness/demo/better-harness-report/"><img src="assets/demo/better-harness-findings-report.png" alt="Better Harness HTML report showing an evidence-bounded finding with its impact, expected output, scoped AI fix, and acceptance checks" width="900"></a>
</p>

<p align="center">
  <sub><a href="https://qoderai.github.io/better-harness/demo/better-harness-report/">Open the complete self-contained English HTML report</a>
  (<a href="assets/demo/better-harness-report.html">source</a>).</sub>
</p>

For delivery tracing, the interactive [Harness Inspector](https://qoderai.github.io/better-harness/inspector/)
follows product intent through agent activity, sessions, files, and commits in
a read-only workspace, keeping evidence strength and limitations visible:

<p align="center">
  <a href="https://qoderai.github.io/better-harness/inspector/"><img src="docs/assets/harness-inspector/session-view.png" alt="Harness Inspector session view: a synchronized timeline of prompts, tool calls, and commits with the Evidence Drawer explaining each link" width="900"></a>
</p>

<p align="center">
  <sub><a href="https://qoderai.github.io/better-harness/inspector/">Open the interactive Harness Inspector sample</a> (fictional English data; it never reads your workspace).</sub>
</p>

After you have comparable reports over time, the history view shows how the five
Agent Work Loop dimensions move:

<p align="center">
  <a href="dev/terminal-demo/README.md"><img src="assets/demo/twenty-history.png" alt="Static final frame of Better Harness report history showing five Agent Work Loop dimensions over time" width="900"></a>
</p>

The static final frame summarizes historical Harness reports. It shows recorded
trends, not causal proof of improvement. [See how the demo was recorded](dev/terminal-demo/README.md).

## Why Better Harness?

AI coding agents change code fast, but the workflow around them is often the
weak point:

- 🎯 **Fuzzy goals** — the agent confidently solves the wrong problem.
- 🧭 **Improvised steps** — work happens on paths nobody can reproduce.
- ✅ **"It works" without proof** — validation is incomplete or missing.
- 🚢 **Speed over safeguards** — review and delivery checks get bypassed.
- 🧠 **Lessons lost** — the same friction comes back on the next task