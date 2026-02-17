<p align="center">
  <img src="assets/ralphex-wordmark-split.png" alt="ralphex" width="400">
</p>

<p align="center">
  <a href="https://github.com/umputun/ralphex/actions/workflows/ci.yml"><img src="https://github.com/umputun/ralphex/actions/workflows/ci.yml/badge.svg" alt="build"></a>
  <a href="https://coveralls.io/github/umputun/ralphex?branch=master"><img src="https://coveralls.io/repos/github/umputun/ralphex/badge.svg?branch=master" alt="Coverage Status"></a>
  <a href="https://goreportcard.com/report/github.com/umputun/ralphex"><img src="https://goreportcard.com/badge/github.com/umputun/ralphex?v=2" alt="Go Report Card"></a>
</p>

<h2 align="center">Autonomous plan execution with Claude Code</h2>

*ralphex is a standalone CLI tool that runs in your terminal from the root of a git repository. It orchestrates Claude Code to execute implementation plans autonomously - no IDE plugins or cloud services required, just Claude Code and a single binary.*

Claude Code is powerful but interactive - it requires you to watch, approve, and guide each step. For complex features spanning multiple tasks, this means hours of babysitting. Worse, as context fills up during long sessions, the model's quality degrades - it starts making mistakes, forgetting earlier decisions, and producing worse code.

ralphex solves both problems. Each task executes in a fresh Claude Code session with minimal context, keeping the model sharp throughout the entire plan. Write a plan with tasks and validation commands, start ralphex, and walk away. Come back to find your feature implemented, reviewed, and committed - or check the progress log to see what it's doing.

<details markdown>
<summary>Task Execution Screenshot</summary>

![ralphex tasks](assets/ralphex-tasks.png)

</details>

<details markdown>
<summary>Review Mode Screenshot</summary>

![ralphex review](assets/ralphex-review.png)

</details>

<details markdown>
<summary>Web Dashboard Screenshot</summary>

![ralphex web dashboard](assets/ralphex-web.png)

</details>

## Features

- **Zero setup** - works out of the box with sensible defaults, no configuration required
- **Autonomous task execution** - executes plan tasks one at a time with automatic retry
- **Interactive plan creation** - create plans through dialogue with Claude via `--plan` flag
- **Multi-phase code review** - 5 agents → codex → 2 agents review pipeline
- **Custom review agents** - configurable agents with `{{agent:name}}` template system and user defined prompts
- **Automatic branch creation** - creates git branch from plan filename
- **Plan completion tracking** - moves completed plans to `completed/` folder
- **Automatic commits** - commits after each task and review fix
- **Real-time monitoring** - streaming output with timestamps, colors, and detailed logs
- **Web dashboard** - browser-based real-time view with `--serve` flag
- **Docker support** - run in isolated container for safer autonomous execution
- **Notifications** - optional alerts on completion/failure via Telegram, Email, Slack, Webhook, or custom script
- **Multiple modes** - full execution, tasks-only, review-only, external-only, or plan creation

## Quick Start

Make sure ralphex is [installed](#installation) and your project is a git repository. You need a plan file in `docs/plans/`, for example:

```markdown
# Plan: My Feature

## Validation Commands
- `go test ./...`

### Task 1: Implement feature
- [ ] Add the new functionality
- [ ] Add tests
```

Then run:

```bash
ralphex docs/plans/my-feature.md
```

ralphex will create a branch, execute tasks, commit results, run multi-phase reviews, and move the plan to `completed/` when done.

## How It Works

ralphex executes plans in four phases with automated code reviews, plus an optional finalize step.

<details markdown>
<summary>Execution Flow Diagram</summary>

![ralphex flow](assets/ralphex-flow.png)

</details>

### Phase 1: Task Execution

1. Reads plan file and finds first incomplete task (`### Task N:` with `- [ ]` checkboxes)
2. Sends task to Claude Code for execution
3. Runs validation commands (tests, linters) after each task
4. Marks checkboxes as done `[x]`, commits changes
5. Repeats until all tasks complete or max iterations reached

### Phase 2: First Code Review

Launches 5 review agents **in parallel** via Claude Code Task tool:

| Agent | Purpose |
|-------|---------|
| `quality` | bugs, security issues, race conditions |
| `implementation` | verifies code achieves stated goals |
| `testing` | test coverage and quality |
| `simplification` | detects over-engineering |
| `documentation` | checks if docs need updates |

Claude verifies findings, fixes confirmed issues, and commits.

*[Default agents](https://github.com/umputun/ralphex/tree/master/pkg/config/defaults/agents) provide common, language-agnostic review steps. They can be customized and tuned for your specific needs, languages, and workflows. See [Customization](#customization) for details.*

### Phase 3: External 