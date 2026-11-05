<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/logo-dark.png">
  <img src="docs/images/logo-light.png" alt="Floorplan logo" height="88">
</picture>

# Floorplan

**See how your app actually fits together.**

Claude or Codex reads your codebase and draws an interactive map of it. Every part, file and web request gets a plain-English name, and every connection between them is shown.

[![Claude Code plugin](https://img.shields.io/badge/Claude%20Code-plugin-D97757?style=flat-square)](https://code.claude.com/docs/en/overview)
[![Codex plugin](https://img.shields.io/badge/Codex-plugin-111?style=flat-square)](docs/codex.md)
[![Tests](https://img.shields.io/github/actions/workflow/status/haydenschmitty/floorplan/test.yml?branch=main&style=flat-square&label=tests)](https://github.com/haydenschmitty/floorplan/actions/workflows/test.yml)
[![Version](https://img.shields.io/badge/version-0.6.3-111?style=flat-square)](CHANGELOG.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-111?style=flat-square)](LICENSE)
[![Node 18+](https://img.shields.io/badge/node-%E2%89%A518-111?style=flat-square)](https://nodejs.org)
[![Zero dependencies](https://img.shields.io/badge/dependencies-0-111?style=flat-square)](#how-it-works)

<a href="https://trendshift.io/repositories/322616"><img src="https://trendshift.io/api/badge/trendshift/repositories/322616/daily?language=JavaScript" alt="Floorplan on Trendshift" width="250" height="55"></a>

**[Try the live demo](https://haydenschmitty.github.io/floorplan-demo/)** · [Watch the video](https://youtu.be/NTUUzC7L_NQ) · [Install](#install) · [Quick start](#quick-start) · [Compared](#floorplan-archify-or-understand-anything) · [Features](#features) · [See it in action](#see-it-in-action) · [How it works](#how-it-works) · [Docs](docs/README.md) · [FAQ](#faq)

</div>

<p align="center">
  <a href="https://youtu.be/NTUUzC7L_NQ"><img src="docs/images/video.jpg" alt="Watch the walkthrough on YouTube: installing Floorplan, then a tour of the map of Brewline, a coffee subscription app" width="100%"></a>
</p>
<p align="center"><sub>▶ <a href="https://youtu.be/NTUUzC7L_NQ">Watch the walkthrough</a>: installing Floorplan, then a tour of Brewline, a demo coffee-subscription app built across four repos.</sub></p>
<p align="center"><b><a href="https://haydenschmitty.github.io/floorplan-demo/">Try the live demo →</a></b> Explore the Brewline map in your browser, no install needed.</p>

## Why Floorplan?

You built an app, probably with a lot of help from AI, and it works. But ask "what happens when someone checks out?" or "what breaks if I change this?" and the honest answer is *no idea*.

Floorplan gives you the diagram nobody drew. Ask Claude Code or Codex for a floorplan and a few minutes later you have a map you can explore, ask questions on, and keep up to date as you work.

- **For builders:** understand the app you made, in your own words, without reading the code.
- **For teams:** onboard someone in minutes, from the big picture down to the exact file.
- **For working with AI:** after every change Claude or Codex makes, see exactly which parts it touched and why.

## Floorplan, Archify or Understand Anything?

All three turn code into something you can see, and all three are worth knowing. They answer different questions:

| | **Floorplan** | **[Archify](https://github.com/tt-a1i/archify)** | **[Understand Anything](https://github.com/Egonex-AI/Understand-Anything)** |
|---|---|---|---|
| **The question it answers** | How does the app I built actually work, and what should I worry about? | How do I show this clearly? | How does this big codebase work, down to the functions? |
| **Made for** | People who build with AI and don't read the code | Anyone explaining a system, a process or an idea | Developers getting to know a large codebase |
| **What you get** | A zoomable map of your whole app: parts, files and endpoints, the screens, the requests between frontend and backend (even across repos), and outside services | A polished diagram in one of 10 types (architecture, sequence, ERD…) or a one-page explainer, from a repo or just a description | A knowledge graph of every file, function and class, with layers, a business-domain view and guided tours |
| **Only here** | **Health check** (keys in code, open Supabase tables and Firebase rules, fakeable Stripe webhooks, endpoints anyone can use), **Recent work** (what your AI just changed, and why), blueprints from a PRD | 10 diagram types, image and video exports, diagrams of things that aren't code | Diff impact, a dashboard that adapts to your role, knowledge-base graphs |
| **Runs in** | Claude Code, Codex | Claude Code, Codex, Cursor, OpenCode and more | Claude Code, Codex, Cursor, Copilot, Gemini CLI and more |

**Pick Floorplan** to understand and check an app you own. **Pick Archify** to draw a diagram for a doc, a talk or a decision. **Pick Understand Anything** to study a large codebas