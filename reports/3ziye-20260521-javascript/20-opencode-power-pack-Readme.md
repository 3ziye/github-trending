<p align="center">
  <img src="assets/logo.svg" alt="opencode-power-pack" width="100%" />
</p>

<p align="center">
  <i>Eleven Claude Code skills, ported to OpenCode.<br/>
  Code review, security audit, feature dev, frontend design, and the rest of the kit — installable in one line.</i>
</p>

<p align="center">
  <a href="https://github.com/waybarrios/opencode-power-pack/blob/main/LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-brightgreen?style=flat-square"></a>
  <a href="https://github.com/waybarrios/opencode-power-pack/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/waybarrios/opencode-power-pack?style=flat-square&color=FFD60A"></a>
  <a href="https://github.com/waybarrios/opencode-power-pack/commits/main"><img alt="Last commit" src="https://img.shields.io/github/last-commit/waybarrios/opencode-power-pack?style=flat-square"></a>
  <a href="https://github.com/waybarrios/opencode-power-pack/issues"><img alt="Issues" src="https://img.shields.io/github/issues/waybarrios/opencode-power-pack?style=flat-square"></a>
  <img alt="Skills" src="https://img.shields.io/badge/skills-11-FFD60A?style=flat-square&labelColor=0B0F14">
  <img alt="OpenCode" src="https://img.shields.io/badge/opencode-compatible-0B0F14?style=flat-square&labelColor=FFD60A">
  <img alt="Claude Code compat" src="https://img.shields.io/badge/claude--code-skills_format-D97706?style=flat-square">
</p>

<p align="center">
  <a href="#installation"><b>Install</b></a> ·
  <a href="#whats-inside"><b>Skills</b></a> ·
  <a href="#slash-commands"><b>Commands</b></a> ·
  <a href="#how-it-works"><b>How it works</b></a> ·
  <a href="#acknowledgments"><b>Credits</b></a> ·
  <a href="LICENSE"><b>License</b></a>
</p>

<p align="center">
  <i>Built on top of <a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a>,
  <a href="https://github.com/anthropics/skills">anthropics/skills</a>,
  <a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a>,
  and <a href="https://github.com/obra/superpowers">obra/superpowers</a>. See <a href="#acknowledgments">Acknowledgments</a>.</i>
</p>

---

## Why this exists

OpenCode reads Claude Code's `SKILL.md` format natively, but **most of Anthropic's official Claude Code plugins put their value in `commands/` and `agents/`** — and those are Claude-Code-only. So if you want `/code-review`, `/security-review`, or `/feature-dev` in OpenCode, copy-paste won't get you there.

This pack does the **translation**: the multi-agent workflows from those plugins are rewritten as OpenCode-compatible skills, so the methodology survives the platform jump. Plus a few direct ports of skills that already lived in Anthropic's `skills/` repo.

It pairs nicely with **[obra/superpowers](https://github.com/obra/superpowers)**, which provides the meta-workflow skills (brainstorming, TDD, executing-plans). This pack adds the domain-specific muscle.

---

## What's inside

<table>
<tr>
<th align="left">Category</th>
<th align="left">Skill</th>
<th align="left">Source</th>
<th align="left">Purpose</th>
</tr>

<tr><td rowspan="2"><b>Review</b></td>
<td><code>code-review</code></td>
<td>translated · plugins/code-review</td>
<td>Multi-agent PR review with confidence-filtered cross-checks and reproduction scenarios</td></tr>
<tr><td><code>security-review</code></td>
<td>translated · claude-code-security-review</td>
<td>OWASP-bucketed, three-stage filtering, requires concrete attack PoC per finding</td></tr>

<tr><td rowspan="4"><b>Feature dev</b></td>
<td><code>feature-dev</code></td>
<td>translated · plugins/feature-dev</td>
<td>Seven-phase guided workflow: discovery → exploration → questions → architecture → impl → review → summary</td></tr>
<tr><td><code>code-explorer</code></td>
<td>translated · feature-dev/agents</td>
<td>Deep codebase analysis sub-task — traces a feature end-to-end</td></tr>
<tr><td><code>code-architect</code></td>
<td>translated · feature-dev/agents</td>
<td>Decisive architecture blueprint sub-task with file-level implementation map</td></tr>
<tr><td><code>code-reviewer</code></td>
<td>translated · feature-dev/agents</td>
<td>Two-pass adversarial review sub-task with explicit edge-case checklist</td></tr>

<tr><td><b>Design</b></td>
<td><code>frontend-design</code></td>
<td>copied · plugins/frontend-design</td>
<td>Distinctive, production-grade UI generation that avoids generic AI aesthetics</td></tr>

<tr><td rowspan="2"><b>Authoring</b></td>
<td><code>mcp-builder</code></td>
<td>copied · skills/mcp-builder</td>
<td>Build high-quality MCP servers (Python or TypeScript)</td></tr>
<tr><td><code>skill-creator</code></td>
<td>adapted · skills/skill-creator</td>
<td>Author new SKILL.md files with progressive-disclosure structure</td></tr>

<tr><td rowspan="2"><b>Project memory</b></td>
<td><code>agents-md-improver</code></td>
<td>adapted · plugins/claude-md-management</td>
<td>Audit and update <code>AGENT