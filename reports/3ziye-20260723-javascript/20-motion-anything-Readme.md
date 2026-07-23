# motion-anything

<p align="center"><sub>A project in the <a href="https://github.com/nexu-io/open-design"><b>nexu.io · Open Design</b></a> family — the same team's take on motion. If motion-anything clicks for you, <a href="https://github.com/nexu-io/open-design">Open Design</a> is where the full agent-era design studio lives.</sub></p>

> **Describe the feeling — your AI ships the animation.** The agentic motion layer: a local-first, chat-native motion engine. Generate animated pages and launch videos from one sentence, then edit motion **on the running page, component by component** — 4 triggers, 13 motion verbs, spring easing, a full keyframe editor. Driven by **8 coding-agent engines + BYOK** (Claude Code · Codex · Cursor · OpenCode · Grok Build · Hermes · Gemini · Open Design Cloud), armed with **403 curated motion recipes**, wired into the **Open Design ecosystem** (59 `DESIGN.md` brand packs · 58 HyperFrames video templates · 112 HTML prototype templates · 2,680 icons), and exported to anything: JSON · CSS · React · Lottie · MP4 · GIF · portable skills. Zero npm dependencies. No watermark. No per-render fees.

<p align="center">
  <img src="docs/assets/hero.jpg" alt="motion-anything — Anything becomes motion, on your laptop. Editorial dark banner with light-mode app windows: the component-motion workbench and the launch-video compositor, plus a stats row — 403 motion recipes, 230 portable skills, 2,680 icons, 59 design systems." width="100%" />
</p>

<p align="center">
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/license-Apache%202.0-blue.svg?style=flat-square" /></a>
  <a href="#engines"><img alt="Engines" src="https://img.shields.io/badge/engines-8%20CLIs%20%2B%20BYOK-111?style=flat-square" /></a>
  <a href="#the-library"><img alt="Recipes" src="https://img.shields.io/badge/motion%20recipes-403-8b7cf6?style=flat-square" /></a>
  <a href="#export-anything"><img alt="Export" src="https://img.shields.io/badge/export-JSON%20%C2%B7%20CSS%20%C2%B7%20React%20%C2%B7%20Lottie%20%C2%B7%20MP4%20%C2%B7%20GIF-9b59b6?style=flat-square" /></a>
  <a href="#quickstart"><img alt="Quickstart" src="https://img.shields.io/badge/quickstart-1%20command-green?style=flat-square" /></a>
  <a href="#architecture"><img alt="Zero deps" src="https://img.shields.io/badge/npm%20dependencies-0-ff6b35?style=flat-square" /></a>
</p>

<p align="center">
  <a href="#the-library"><img alt="Design systems" src="https://img.shields.io/badge/design%20systems-59-1abc9c?style=flat-square" /></a>
  <a href="#the-library"><img alt="Video templates" src="https://img.shields.io/badge/HyperFrames%20video%20templates-58-e67e22?style=flat-square" /></a>
  <a href="#the-library"><img alt="HTML templates" src="https://img.shields.io/badge/HTML%20prototype%20templates-112-3498db?style=flat-square" /></a>
  <a href="#the-library"><img alt="Icons" src="https://img.shields.io/badge/icons-2680-f39c12?style=flat-square" /></a>
  <a href="#open-design-ecosystem"><img alt="Portable skills" src="https://img.shields.io/badge/portable%20skills-230-8b7cf6?style=flat-square" /></a>
</p>

<p align="center">
  <a href="https://github.com/nexu-io/open-design"><img alt="Family" src="https://img.shields.io/badge/family-nexu--io%2Fopen--design-ff7043?style=flat-square&logo=github&logoColor=white" /></a>
  <a href="https://x.com/OpenDesignHQ"><img alt="Follow on X" src="https://img.shields.io/badge/follow-%40OpenDesignHQ-000000?style=flat-square&logo=x&logoColor=white" /></a>
</p>

<p align="center"><b>English</b> · <a href="README.zh-CN.md">简体中文</a></p>

---

## Showcase

Every tile below is a **live, dependency-free recipe** from the library — real GPU shaders, canvas engines and kinetic text, faithfully ported so they run with two `<script>` tags on any page (no React, no three.js, no build step). All tiles are animated GIFs recorded from the actual previews.

<table>
<tr>
<td width="50%"><a href="recipes/slides/fx-typewriter-multi/"><img src="docs/assets/effects/typewriter-multi.gif" alt="Typewriter multi — terminal-style lines typing in sequence" /></a></td>
<td width="50%"><a href="recipes/web/shiny-text/"><img src="docs/assets/effects/shiny-text.gif" alt="Shiny text — a highlight band sweeps across the label" /></a></td>
</tr>
<tr>
<td><b><a href="recipes/slides/fx-typewriter-multi/">typewriter-multi</a></b> · kinetic text<br/><sub>Terminal-style multi-line typing with live cursors — agent-boot energy.</sub></td>
<td><b><a href="recipes/web/shiny-text/">shiny-text</a></b> · kinetic text<br/><sub>A sheen sweeps across text-clipped gradient type. One class to use.</sub></td>
</tr>
<tr>
<td width="50%"><a href="recipes/web/star-border/"><img src="docs/assets/effects/star-border.gif" alt="Star border — a slow light circles the button border" /></a></td>
<td width="50%"><a href="recipes/web/rotating-text/"><img src="docs/assets/effects/rotating-text.gif" alt="Rotating text — words cycle in place" /></a></td>
</tr>
<tr>
<td><b><a href="re