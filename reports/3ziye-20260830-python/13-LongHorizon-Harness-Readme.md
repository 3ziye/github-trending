<div align="center">

# LongHorizon-Harness

### Loop Engineering for Computer-Use Agents

**Give Claude Code, Codex, OpenCode, or DeepSeek Harness a goal once. Keep it working across desktop apps and the terminal for dozens of hours.**

**Plan → act → verify → checkpoint or recover → repeat — until the work is actually done.**

<p align="center">
<a href="https://lh-harness.pages.dev"><img src="https://img.shields.io/badge/🌐-Website-1f6feb.svg?style=flat-square" alt="Website" /></a>
<a href="https://arxiv.org/abs/2608.01964"><img src="https://img.shields.io/badge/arXiv-2608.01964-b31b1b.svg?style=flat-square" alt="arXiv 2608.01964" /></a>
<a href="https://github.com/AMAP-ML/LongHorizon-Harness"><img src="https://img.shields.io/badge/GitHub-Repository-181717.svg?style=flat-square&logo=github&logoColor=white" alt="GitHub repository" /></a>
<img src="https://img.shields.io/badge/🤗-Trajectory_Coming_Soon-ffce00.svg?style=flat-square" alt="Hugging Face trajectory" />
<a href="https://huggingface.co/papers/2608.01964"><img src="https://img.shields.io/badge/🤗_Daily_Papers-2608.01964-ff8800.svg?style=flat-square" alt="Hugging Face Daily Papers" /></a>
<a href="./LICENSE"><img src="https://img.shields.io/badge/License-MIT-2ea44f.svg?style=flat-square" alt="MIT License" /></a>
</p>

[![Python](https://img.shields.io/badge/python-≥3.10-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Agents](https://img.shields.io/badge/backends-Claude%20Code%20|%20Codex%20|%20OpenCode%20|%20DeepSeek-8A2BE2)](#any-model-any-agent-backend)
[![Benchmarks](https://img.shields.io/badge/benchmarks-WeaveBench%20|%20OSWorld%202.0%20|%20Terminal--Bench%202.1-orange)](#hundreds-of-real-tasks-measured-gains)

[Usage](#one-command-full-visibility) · [The Loop](#loop-engineering-for-real-computer-environments) · [Computer Use](#desktop-apps-and-cli-one-continuous-task) · [Results](#hundreds-of-real-tasks-measured-gains) · [Project Website](https://lh-harness.pages.dev) · [简体中文](README.zh-CN.md)

<br>
<img src="assets/quickstart.gif" alt="Install and run LongHorizon-Harness from the command line" width="720">

</div>

> **The model determines what an agent can do in one round. LongHorizon-Harness engineers the loop around it: what to do next, how to verify the result in the real computer, what progress to preserve, and how to continue after failure or context refresh.**

**A Loop Engineering system for Claude Code, Codex, OpenCode, and DeepSeek Harness. One-command install, ready to run.**

LongHorizon-Harness turns existing agents into long-running computer-use systems. Across desktop apps and the terminal CLI, it continuously recovers the goal and verified state, selects the next bounded step, executes it with a fresh context, checks the actual result, and then checkpoints accepted progress or feeds failure evidence into the next round. It does not train a new model or replace an existing agent; it provides the durable execution loop around one.

## ✨ News

- **[v0.1.7 · 2026-08-20]** A finished run is no longer a dead end: the workbench is now a conversation. Read the reply, type a follow-up, and the run continues on its own round ledger instead of replanning from scratch. A message you send mid-round is claimed by the very next round, so stopping and continuing never drops it. Also adds `--reasoning-effort` for every role (with `--manager-reasoning-effort` and friends to override one), forwarded to whichever backend exposes it. The transcript now reads in strict chronological order, and a graceful stop escalates to a force stop only when a worker ignores it.
- **[v0.1.6 · 2026-08-15]** Added [OpenCode](https://github.com/anomalyco/opencode) CLI support. LongHorizon-Harness can now run `opencode run prompt` as `--agent opencode`, with role-scoped read/write permissions, OpenCode API endpoint overrides, normalized JSON results, and CLI/config/doctor integration. The Web workbench can select OpenCode Harness and its model independently for each role.
- **[v0.1.5 · 2026-08-14]** Added phase-1 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) CLI support. LongHorizon-Harness can now run `dsh --profile headless` as `--agent deepseek_harness`, with an isolated `DSH_HOME`, role-scoped read/write permissions, DeepSeek API endpoint overrides, normalized JSONL results, and CLI/config/doctor integration. The Web workbench can select DeepSeek Harness and its model independently for each role. GUI computer-use and MCP support will follow in a later phase; see [the CLI setup](#5-or-run-a-task-from-the-command-line).
- **[v0.1.4 · 2026-08-11]** The new Dashboard has landed: a React/FastAPI workbench you can drive entirely from the browser. Start a task, choose a backend and model per role, answer approvals, send an instruction mid-run, and stop or restart a run. Launch it with `lh-harness web`; see [Run a task in the browser](#4-run-a-task-in-the-browser-recommended).
- **[2026-08-10]** Added the Terminal-Bench 2.1 evaluation.