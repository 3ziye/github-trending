# Loop Engineering


<p align="center">
  <a href="https://cobusgreyling.github.io/loop-engineering/">
    <img src="https://img.shields.io/badge/✨_Explore_the_Showcase-Design_systems_that_prompt_your_agents-0d1117?style=for-the-badge&labelColor=111a28&color=3ee8c5" alt="Explore the Showcase" />
  </a>
</p>

<p align="center">
  <a href="https://github.com/cobusgreyling/loop-engineering/stargazers"><img src="https://img.shields.io/github/stars/cobusgreyling/loop-engineering?style=social" alt="GitHub stars"></a>
  <a href="https://github.com/cobusgreyling/loop-engineering/actions/workflows/audit.yml"><img src="https://img.shields.io/github/actions/workflow/status/cobusgreyling/loop-engineering/audit.yml?label=loop-audit%20dogfood" alt="loop-audit dogfood"></a>
  <a href="https://www.npmjs.com/package/@cobusgreyling/loop-audit"><img src="https://img.shields.io/npm/v/@cobusgreyling/loop-audit?label=loop-audit" alt="loop-audit npm"></a>
  <a href="https://www.npmjs.com/package/@cobusgreyling/loop-init"><img src="https://img.shields.io/npm/v/@cobusgreyling/loop-init?label=loop-init" alt="loop-init npm"></a>
  <a href="https://www.npmjs.com/package/@cobusgreyling/loop-cost"><img src="https://img.shields.io/npm/v/@cobusgreyling/loop-cost?label=loop-cost" alt="loop-cost npm"></a>
  <a href="https://github.com/cobusgreyling/loop-engineering/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT"></a>
  <a href="https://cobusgreyling.github.io/loop-engineering/"><img src="https://img.shields.io/badge/GitHub_Pages-live%20%7C%20interactive-3ee8c5" alt="Pages"></a>
</p>


<p align="center">
  <img src="assets/visuals/loop-engineering-logo.jpg" alt="Loop Engineering" width="96" />
</p>

**Loop engineering is replacing yourself as the person who prompts the agent. You design the system that does it instead.**

For developers using Grok, Claude Code, Codex, Cursor, and other AI coding agents.

A loop is a recursive goal: you define a purpose and the AI iterates (often with sub-agents, verification, and external state) until the goal is complete or the loop decides to hand off to you.



<p align="center">
  <img src="assets/visuals/loop-engineering-social-banner.jpg" alt="Loop Engineering — Design the system that prompts your agents" width="100%" />
</p>

<p align="center">
  <strong><a href="https://cobusgreyling.github.io/loop-engineering/">→ Interactive showcase + pattern picker</a></strong>
  <br>
  <strong><a href="https://cobusgreyling.substack.com/p/loop-engineering">→ Loop Engineering essay (Substack)</a></strong>
  <br>
  <a href="https://addyosmani.com/blog/loop-engineering/">Canonical essay by Addy Osmani</a>
</p>

## Contents

- [Quick Links](#quick-links)
- [Why This Matters](#why-this-matters)
- [The Five Building Blocks + Memory](#the-five-building-blocks--memory)
- [Patterns](#patterns)
- [Getting Started (5 minutes)](#getting-started-5-minutes)
- [Examples by Tool](#examples-by-tool)
- [Operating & Safety](#operating--safety)
- [Caveats](#caveats)
- [Contributing](#contributing)
- [Sources](#sources)
- [License](#license)

## Quick Links

| Start here | Description |
|------------|-------------|
| [Loop Engineering essay](https://cobusgreyling.substack.com/p/loop-engineering) | The concept, primitives, and Grok mapping — **read this first** |
| [Pattern Picker](docs/pattern-picker.md) | Which loop to run first — **start here if unsure** |
| [Primitives Matrix](docs/primitives-matrix.md) | Grok vs Claude Code vs Codex — bookmark this |
| [Loop Design Checklist](docs/loop-design-checklist.md) | Ship readiness rubric |
| [Patterns](patterns/README.md) | 7 production patterns + [interactive picker](https://cobusgreyling.github.io/loop-engineering/#interactive) |
| [Starters](starters/) | Clone-and-run kits (Grok, Claude Code, Codex) |
| [loop-audit](tools/loop-audit/) | Loop Readiness Score CLI (v1.4 + activity detection) — `npx @cobusgreyling/loop-audit . --suggest` |
| [loop-init](tools/loop-init/) | Scaffold starters + budget/run-log (v1.2) — `npx @cobusgreyling/loop-init . --pattern daily-triage --tool grok` |
| [loop-cost](tools/loop-cost/) | Token spend estimator — `npx @cobusgreyling/loop-cost` |
| [Goal Engineering](https://github.com/cobusgreyling/goal-engineering) | Companion: Grok Build `/goal` — run-until-done objectives (`npx @cobusgreyling/goal-audit`) |
| [Stories](stories/) | Real wins and honest failures |

## Why This Matters

Peter Steinberger:
> “You shouldn’t be prompting coding agents anymore. You should be designing loops that prompt your agents.”

Boris Cherny (Head of Claude Code at Anthropic):
> “I don’t prompt Claude anymore. I have loops running that prompt Claude and figuring out what to do. My job is to write loops.”

The leverage point has moved from crafting individual prompts to designing the control systems that orchestrate agents over time.

## The Five Building Blocks + Memory

| Primitive | Job in the Loop |
|-----------|-----------------|
