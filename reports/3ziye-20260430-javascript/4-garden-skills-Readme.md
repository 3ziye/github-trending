<div align="center">

# Garden Skills

**A curated collection of production-ready [Agent Skills](https://support.claude.com/en/articles/12512176-what-are-skills) for Claude Code, Cursor, Codex, and other AI coding agents.**

[![License: MIT](https://img.shields.io/github/license/ConardLi/web-design-skill?style=flat-square&color=blue)](./LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/ConardLi/web-design-skill?style=flat-square)](https://github.com/ConardLi/web-design-skill/stargazers)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](#contributing)
[![Skills count](https://img.shields.io/badge/skills-3-orange?style=flat-square)](#whats-inside)
[![Spec](https://img.shields.io/badge/spec-SKILL.md-black?style=flat-square)](https://agentskills.io)

[English](./README.md) · [中文文档](./README.zh-CN.md)

</div>

---

## Table of contents

- [What's inside](#whats-inside)
- [Install](#install)
  - [Option A · Claude Code plugin marketplace](#option-a--claude-code-plugin-marketplace)
  - [Option B · Manual copy into your project](#option-b--manual-copy-into-your-project)
  - [Option C · Git submodule](#option-c--git-submodule)
- [Compatibility](#compatibility)
- [Anatomy of a Skill](#anatomy-of-a-skill)
- [Repository layout](#repository-layout)
- [Acknowledgments](#acknowledgments)
- [License](#license)

---

## What's inside

<table>
<tr>
<th width="22%">Skill</th>
<th width="14%">Category</th>
<th>Highlights</th>
<th width="14%">Docs</th>
</tr>

<tr>
<td>

**[`web-design-engineer`](./skills/web-design-engineer)**

</td>
<td>

Design&nbsp;/&nbsp;Frontend

</td>
<td>

Turns AI-generated web pages from "functional" into "stunning."

- Anti-cliché blocklist (no purple-pink gradients, no Inter, no emoji icons)
- `oklch` color theory + 6 curated color × font pairings
- Six-step workflow: requirements → context → design system → v0 → build → verify
- ~520-line advanced patterns library

</td>
<td>

[README](./skills/web-design-engineer/README.md) · [SKILL](./skills/web-design-engineer/SKILL.md) · [Demo](./demo/web-design-demo)

</td>
</tr>

<tr>
<td>

**[`gpt-image-2`](./skills/gpt-image-2)**

</td>
<td>

Image&nbsp;Gen&nbsp;/&nbsp;Prompting

</td>
<td>

A focused image-gen skill for GPT Image 2 (and OpenAI-compatible image APIs).

- **Three runtime modes**: A&nbsp;Garden local · B&nbsp;Host-native delegate · C&nbsp;Advisor-only
- 18 categories, 70+ structured prompt templates
- Auto prompt + image archival under `garden-gpt-image-2/`
- Mode-detection script so the skill never silently fails

</td>
<td>

[README](./skills/gpt-image-2/README.md) · [SKILL](./skills/gpt-image-2/SKILL.md)

</td>
</tr>

<tr>
<td>

**[`rag-skill`](./skills/rag-skill)**
<br/><sub>frontmatter `name: kb-retriever`</sub>

</td>
<td>

Retrieval&nbsp;/&nbsp;Docs

</td>
<td>

A local knowledge-base retriever that never loads whole files into context.

- Hierarchical `data_structure.md` index navigation
- Mandatory **learn-before-process** for PDF / Excel
- Progressive `grep` + windowed reads, bounded to 5 rounds
- Reference docs for `pdftotext` / `pdfplumber` / `pandas` workflows

</td>
<td>

[README](./skills/rag-skill/README.md) · [SKILL](./skills/rag-skill/SKILL.md)

</td>
</tr>

</table>

---

## Install

### Option A · Claude Code plugin marketplace

The fastest path if you use [Claude Code](https://docs.anthropic.com/en/docs/claude-code):

```bash
/plugin marketplace add ConardLi/garden-skills
/plugin install web-design-skills@garden-skills
/plugin install knowledge-base-skills@garden-skills
/plugin install image-generation-skills@garden-skills
```

Plugin packs are declared in [`.claude-plugin/marketplace.json`](./.claude-plugin/marketplace.json):

| Plugin pack | Skills included |
|---|---|
| `web-design-skills` | `web-design-engineer` |
| `knowledge-base-skills` | `rag-skill` |
| `image-generation-skills` | `gpt-image-2` |

### Option B · Manual copy into your project

Each skill folder is self-contained — copy the one(s) you want into your project's skills directory:

```bash
# Claude Code / Claude.ai
cp -r skills/web-design-engineer  your-project/.claude/skills/

# Cursor / generic agent
cp -r skills/web-design-engineer  your-project/.agents/skills/
```

The agent will discover the skill the next time it scans the workspace.

### Option C · Git submodule

If you want to track upstream updates inside a larger project:

```bash
git submodule add https://github.com/ConardLi/web-design-skill.git vendor/garden-skills
ln -s ../../vendor/garden-skills/skills/web-design-engineer .claude/skills/web-design-engineer
```

---

## Compatibility

| Agent / Runtime | Skill location | Status |
|---|---|---|
| **Claude Code** | `.claude/skills/<name>/` or via plugin marketplace | ✅ Tested |
| **Claude.ai** (web) | Settings → Capabilities → Skills | ✅ Tested |
| **Cursor** | `.agents/skills/<name>/` | ✅ Tested |
| **Codex CLI** | `.codex/skills/<name>/` | ✅ Tested |
| **Gemini CLI** | extension manifest | ✅