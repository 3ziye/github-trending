# Skills for coding agents

Small, composable skills for coding agents.

### Quick install recommended skills

```sh
npx @agent-native/skills@latest add
```

The interactive picker puts `/visual-plan` and `/visual-recap` first and selects
only those by default. See the [full CLI docs below](#install).

## Skills At A Glance

- [`/visual-plan`](#visual-plan) - Turn text plans into rich visual plans.
- [`/visual-recap`](#visual-recap) - Turn diffs into interactive visual recaps.
- [`/agent-watchdog`](#agent-watchdog) - Audit another agent's work.
- [`/plan-arbiter`](#plan-arbiter) - Compare competing plans and choose a direction.
- [`/plow-ahead`](#plow-ahead) - Keep working through ordinary ambiguity.
- [`/efficient-fable`](#efficient-fable) - Orchestrate Fable with cheaper helper agents.
- [`/efficient-frontier`](#efficient-frontier) - Preserve high-cost models for judgment.
- [`/stay-within-limits`](#stay-within-limits) - Track usage limits before long-running work.
- [`/quick-recap`](#quick-recap) - End work with a clear status signal.
- [`/read-the-damn-docs`](#read-the-damn-docs) - Check authoritative docs before guessing.

## Skill Details

### [`/visual-plan`](skills/visual-plan/README.md)

Turn ordinary text plans into rich interactive visual plans with diagrams, file
maps, annotated code, open questions, and UI/prototype review when useful.

Solves for plans that are too important to bury in chat. The output is
scannable, commentable, and intuitive enough for a human to approve before code
changes start.

<picture>
  <img alt="Visual plan review surface" src="media/visual-plan.png">
</picture>

Visual plans are MDX, customizable with your own components, and are viewed with the [Agent-Native plans app](https://www.agent-native.com/docs/template-plan). [Source here](https://github.com/BuilderIO/agent-native/)

### [`/visual-recap`](skills/visual-recap/README.md)

Turn a branch, commit, or PR diff into an interactive visual recap with
annotated diffs, diagrams, API/schema summaries, file maps, UI state summaries,
and focused review notes.

Solves for diffs that hide the shape of the change. Reviewers can understand
contracts, architecture moves, schema changes, and UI impact before diving into
raw line-by-line review.

<picture>
  <img alt="Visual recap review surface animation" src="media/visual-recap.gif">
</picture>

Visual recaps are MDX, customizable with your own components, and are viewed with the [Agent-Native plans app](https://www.agent-native.com/docs/template-plan). [Source here](https://github.com/BuilderIO/agent-native/)

You can also install a GitHub action for these to be automatically generated for every PR with

```sh
npx @agent-native/skills@latest add
```

![Example of a visual plan posted to a PR](https://cdn.builder.io/api/v1/image/assets%2FYJIGb4i01jvw0SRdL5Bt%2Fcf9bac396cf24a4ba976fc331af6fc5d)

### [`/agent-watchdog`](skills/agent-watchdog/README.md)

Audit another agent's work from a Codex session, Claude Code transcript, PR,
branch, or run summary.

Solves for cross-agent handoffs: watch until done, reconstruct what was asked,
check what actually changed and verified, report gaps, and optionally make
narrow fixes.

### [`/plan-arbiter`](skills/plan-arbiter/README.md)

Compare competing agent plans and choose one executable direction.

Solves for multi-agent planning loops where Codex, Claude Code, or other agents
produce separate strategies. The output is a decision memo with the winning or
hybrid plan, rejected alternatives, verification gates, and executor
recommendation.

### [`/plow-ahead`](skills/plow-ahead/README.md)

Keep working through ordinary ambiguity and finish with a clear decision recap.

Solves for explicit autonomy requests: the agent converts routine questions into
assumptions, proceeds with conservative choices, validates the work, and recaps
the decisions it made without stopping.

### [`/efficient-fable`](skills/efficient-fable/README.md)

Use Claude Fable as the orchestrator, architect, synthesizer, and final judge
while lighter agents handle token-heavy research, coding, testing, and log
reduction.

Solves for expensive-model waste: Fable should spend tokens on judgment, not on
reading every file, reducing every log, or manually running every browser check.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="skills/efficient-fable/assets/fable-orchestrator-dark.png">
  <source media="(prefers-color-scheme: light)" srcset="skills/efficient-fable/assets/fable-orchestrator.png">
  <img alt="Fable orchestrator diagram" src="skills/efficient-fable/assets/fable-orchestrator.png">
</picture>

### [`/efficient-frontier`](skills/efficient-frontier/README.md)

Apply the same orchestration as `/efficient-fable` to any high-cost frontier
model: preserve the expensive model for planning, tradeoffs, integration,
validation strategy, and final review; use cheaper agents for bounded heavy
lifting.

Solves for broad work that can be parallelized without a