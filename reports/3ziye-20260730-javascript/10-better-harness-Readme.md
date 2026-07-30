<h1 align="center">Better Harness</h1>

<p align="center">
  English · <a href="README.zh-CN.md">简体中文</a>
</p>

<p align="center">
  <strong>See how your AI coding workflow works—and make it better, one step at a time.</strong>
</p>

<p align="center">
  Better Harness reviews how coding agents understand tasks, make changes, verify
  results, deliver safely, and learn—then shows what to improve next, with every
  finding tied to visible evidence.
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License"></a>
  <a href="package.json"><img src="https://img.shields.io/badge/node-%3E%3D22.20.0-brightgreen.svg" alt="Node.js >= 22.20.0"></a>
</p>

<p align="center">
  <a href="https://qoderai.github.io/better-harness/">Website</a> ·
  <a href="#quick-start">Quick Start</a> ·
  <a href="#see-it-in-action">Demo</a> ·
  <a href="#why-better-harness">Why</a> ·
  <a href="#what-is-open">What's open</a> ·
  <a href="#installation">Installation</a> ·
  <a href="docs/adapters/README.md">Host support</a> ·
  <a href="roadmap.md">Roadmap</a> ·
  <a href="docs/community.md">Contribute</a>
</p>

## See it in action

Ask `/better-harness` to review the current task and its surrounding project
Harness, then generate a durable report:

```text
/better-harness review this project's AI coding workflow and generate a report
```

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

After you have comparable reports over time, the history view shows how the five
Agent Work Loop dimensions move:

<p align="center">
  <a href="dev/terminal-demo/README.md"><img src="assets/demo/twenty-history.gif" alt="Better Harness terminal history demo showing five Agent Work Loop dimensions over time" width="900"></a>
</p>

The animation replays historical Harness reports. It shows recorded trends, not
causal proof of improvement. [See how the demo was recorded](dev/terminal-demo/README.md).

## Why Better Harness?

AI coding agents change code fast, but the workflow around them is often the
weak point:

- 🎯 **Fuzzy goals** — the agent confidently solves the wrong problem.
- 🧭 **Improvised steps** — work happens on paths nobody can reproduce.
- ✅ **"It works" without proof** — validation is incomplete or missing.
- 🚢 **Speed over safeguards** — review and delivery checks get bypassed.
- 🧠 **Lessons lost** — the same friction comes back on the next task.

Reviewing only the final diff misses these system-level problems. Better Harness
reviews the workflow itself: it gathers project evidence (and session evidence
where supported), evaluates five connected dimensions, and turns concrete gaps
into prioritized findings — each tied to its evidence, expected outcome, repair
boundary, and validation route, so a team can improve one issue at a time.

## How Better Harness works

Better Harness uses a
[feedforward-and-feedback](https://martinfowler.com/articles/harness-engineering.html#FeedforwardandFeedback)
loop that combines guidance available before work starts with signals available
after the agent acts:

- **Feedforward guides** — `AGENTS.md`, specs, Skills, and acceptance criteria
  steer the agent before it acts.
- **Feedback sensors** — linters, tests, Hooks, and review agents observe results
  and help the agent self-correct.

Across that loop, it evaluates five parts of delivery — the **Agent Work Loop**:

[![Agent Work Loop: five dimensions from task understanding through learning capture](assets/agent-work-loop-en.svg)](models/agent-work-loop.md)

| Dimension | The question it answers | Backed by |
| --- | --- | --- |
| **Task Understanding** | Does the agent know the goal and what "done" means? | Rules, `AGENTS.md`, specs, `DESIGN.md` |
| **Controlled Execution** | Is the work on supported, repeatable paths? | Skills, commands, MCP tools, sandbox boundaries |
| **Change Validation** | Is there evidence the change actually works? | Tests, lint, Hooks, observable diagnostics |
| **Reliable Delivery** | Does AI speed bypass quality checks or acceptance? | Human review, approvals, CI/CD, recovery paths |
| **Learning Capture** | Does the next task benefit from this one? | Loop Discovery, reusable SDLC Skills, Memory |

Running `/better-harness` establishes a task-bounded baseline and, depending on
the host, produces a visu