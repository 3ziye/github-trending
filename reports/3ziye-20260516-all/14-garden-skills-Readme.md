<div align="center">

# Garden Skills

**A curated collection of production-ready [Agent Skills](https://support.claude.com/en/articles/12512176-what-are-skills) for Claude Code, Cursor, Codex, and other AI coding agents.**

<a id="skills-gallery"></a>

<table>
<tr>
<td width="50%" valign="top">
<a href="#web-video-presentation"><img src="./dist/imgs/web-video-presentation-skill.png" alt="Web Video Presentation Skill" width="100%"></a>
<br/><a href="#web-video-presentation"><strong>web-video-presentation</strong></a>
<br/><sub>Web video / presentation</sub>
</td>
<td width="50%" valign="top">
<a href="#web-design-engineer"><img src="./dist/imgs/web-design-skill.png" alt="Web Design Skill" width="100%"></a>
<br/><a href="#web-design-engineer"><strong>web-design-engineer</strong></a>
<br/><sub>Design / frontend</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="#gpt-image-2"><img src="./dist/imgs/gpt-image-2-skill.png" alt="GPT Image 2 Skill" width="100%"></a>
<br/><a href="#gpt-image-2"><strong>gpt-image-2</strong></a>
<br/><sub>Image generation / prompting</sub>
</td>
<td width="50%" valign="top">
<a href="#kb-retriever"><img src="./dist/imgs/kb-retriever-skill.png" alt="KB Retriever Skill" width="100%"></a>
<br/><a href="#kb-retriever"><strong>kb-retriever</strong></a>
<br/><sub>Local knowledge retrieval</sub>
</td>
</tr>
</table>

[![License: MIT](https://img.shields.io/github/license/ConardLi/garden-skills?style=flat-square&color=blue)](./LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/ConardLi/garden-skills?style=flat-square)](https://github.com/ConardLi/garden-skills/stargazers)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](#contributing)
[![Skills count](https://img.shields.io/badge/skills-4-orange?style=flat-square)](#skills-gallery)
[![Spec](https://img.shields.io/badge/spec-SKILL.md-black?style=flat-square)](https://agentskills.io)

[English](./README.md) · [中文文档](./README.zh-CN.md) · [日本語](./README.ja-JP.md)

</div>

---

## Table of contents

| Install | Use | Contribute |
|---|---|---|
| [Install](#install)<br>[`skills` CLI (npx)](#option-a--skills-cli-npx)<br>[Claude Code plugin marketplace](#option-b--claude-code-plugin-marketplace)<br>[Pinned `.zip` from Releases](#option-c--pinned-zip-from-releases)<br>[Manual copy](#option-d--manual-copy-into-your-project)<br>[Git submodule](#option-e--git-submodule) | [Compatibility](#compatibility)<br>[What is a Skill?](#what-is-a-skill) | [Contributing](#contributing)<br>[Acknowledgments](#acknowledgments)<br>[License](#license) |

---

### [`web-video-presentation`](./skills/web-video-presentation)

![Web Video Presentation Skill](./dist/imgs/web-video-presentation-skill.png)

**Category:** Web Video / Presentation Engineering  
**Best for:** turning scripts, articles, lessons, product demos, and talks into click-driven 16:9 web presentations that can be screen-recorded as cinematic videos.

`web-video-presentation` builds record-ready Vite + React + TypeScript presentations that behave like video production surfaces. The workflow turns raw articles into narration scripts, maps script beats to full-screen scenes, pauses at required checkpoints, and can optionally synthesize narration audio after the visual outline is approved.

Highlights:

- Fixed 1920×1080 stage that scales to the viewport for stable screen recording
- Click / keyboard driven `(chapter, step)` cursor, with one narration beat per visual step
- Hard collaboration checkpoints for script, theme, outline, implementation mode, and optional audio
- Hidden hover-only progress controls so the stage stays clean while recording
- Theme-token architecture with multiple visual languages, from `paper-press` to `terminal-green`
- Scaffolded Vite + React + TypeScript project with reusable stage primitives and recording guidance

Links: [README](./skills/web-video-presentation/README.md) · [SKILL.md](./skills/web-video-presentation/SKILL.md) · <!-- DOWNLOAD:web-video-presentation:start -->[Download v1.1.5 .zip](https://github.com/ConardLi/garden-skills/releases/download/web-video-presentation-v1.1.5/web-video-presentation-1.1.5.zip)<!-- DOWNLOAD:web-video-presentation:end -->

---

### [`web-design-engineer`](./skills/web-design-engineer)

![Web Design Skill](./dist/imgs/web-design-skill.png)

**Category:** Design / Frontend  
**Best for:** web pages, landing pages, dashboards, interactive prototypes, HTML slide decks, animations, UI mockups, data visualizations, and design-system explorations.

`web-design-engineer` turns AI-generated web artifacts from merely functional into polished, deliberate, and visually memorable front-end work. It treats the agent as a design engineer: first understanding product context, then declaring a design system, showing an early v0, building the full experience, and verifying the result.

Highlights:

- Defines a six-step design workflow: requirements → context → design system → v0 → full build → veri