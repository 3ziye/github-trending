<p align="center">
  <img src="docs/images/sprite-banner.png" alt="pixtuoid sprites" width="500" />
</p>

<h1 align="center">pixtuoid</h1>

<p align="center">
  <em>Your AI coding agents, visualized as pixel-art coworkers in a terminal office.</em>
</p>

<p align="center">
  <sub><em><b>pix</b>el + <b>tu</b>i + (agent-)<b>oid</b></em></sub>
</p>

<p align="center">
  <a href="https://github.com/IvanWng97/pixtuoid/stargazers"><img src="https://img.shields.io/github/stars/IvanWng97/pixtuoid?style=flat-square" alt="Stars" /></a>
  <a href="https://github.com/IvanWng97/pixtuoid/releases"><img src="https://img.shields.io/github/v/release/IvanWng97/pixtuoid?label=version&style=flat-square" alt="Version" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square" alt="License" /></a>
  <a href="https://github.com/IvanWng97/pixtuoid/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/IvanWng97/pixtuoid/ci.yml?style=flat-square&label=CI" alt="CI" /></a>
  <a href="https://codecov.io/gh/IvanWng97/pixtuoid"><img src="https://img.shields.io/codecov/c/github/IvanWng97/pixtuoid?style=flat-square" alt="Coverage" /></a>
  <a href="https://claude.ai/code"><img src="https://img.shields.io/badge/Built%20with-Claude%20Code-blueviolet?style=flat-square&logo=anthropic" alt="Built with Claude Code" /></a>
  <a href="https://buymeacoffee.com/IvanWng97"><img src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=flat-square&logo=buy-me-a-coffee&logoColor=black" alt="Buy Me a Coffee" /></a>
</p>

<p align="center">
  <img src="docs/images/demo.gif" alt="pixtuoid animated demo" width="800" />
</p>

<p align="center">
  <a href="https://ivanwng97.github.io/pixtuoid/"><strong>🖥&#xFE0E; Live demo ↗</strong></a>
  &nbsp;·&nbsp; <a href="https://ivanwng97.github.io/pixtuoid/architecture">Architecture</a>
  &nbsp;·&nbsp; <a href="https://ivanwng97.github.io/pixtuoid/config">Configuration</a>
  &nbsp;·&nbsp; <a href="https://ivanwng97.github.io/pixtuoid/contributing">Contributing</a>
</p>

---

## Why?

Running several coding agents means alt-tabbing between terminals to find out who's stuck, who's waiting on a permission prompt, and who finished ten minutes ago. **pixtuoid** puts them all in one tiny pixel-art office you can watch from above — every session is a character at a desk: typing while it works, raising a `?` when it needs you, dozing off when it's done.

A little bit *Black Mirror*, a little bit *The Sims* — and the most glanceable multi-agent dashboard you'll ever use.

## Quick Start

Pick one — Homebrew on macOS, or npm on any OS:

<!-- install:start · generated from site/src/install.json by `just gen-readme` — edit the JSON, not this block -->
**Homebrew** (macOS):

```bash
brew install IvanWng97/pixtuoid/pixtuoid
```

**npm** (any OS):

```bash
npm install -g pixtuoid
```
<!-- install:end -->

Then launch:

```bash
pixtuoid
```

Press `s` to open the **Sources** panel and connect your agent CLI (Claude Code, Codex, Antigravity, Reasonix, …) — pixtuoid wires up the integration for you, no separate install step. In another terminal, start that coding agent. A character walks in from the elevator within a second; disconnect in the same panel and it walks back out. The panel also flags a source whose hooks are connected but broken (run `pixtuoid doctor` for the full health report).

**Keyboard shortcuts:** `q` quit · `p` pause · `s` sources (connect / health) · `t` themes · `Tab` agent dashboard · `?` help · `↑↓/jk/PgUp/PgDn` floors · click to pin tooltip

**More ways to install** — Cargo, prebuilt binaries, and Debian `.deb`s — are on the **[install guide ↗](https://ivanwng97.github.io/pixtuoid/#install)**. Upgrading from `ascii-agents`? See [docs/MIGRATION.md](docs/MIGRATION.md).

## Features

<!-- features:start · generated from site/src/features.json by `just gen-readme` — edit the JSON, not this table -->
| | Feature | Description |
|---|---|---|
| 🏢 | **Multi-agent office** | Each agent session gets a desk; overflow agents auto-fill new floors |
| 🛗 | **Multi-floor office** | PageUp/PageDown/↑↓/jk to navigate floors with slide transition |
| 🎭 | **Animated characters** | Typing, waiting (`?`), sleeping (z's), walking with A\*-routed pathfinding |
| 💡 | **Per-tool monitor glow** | Edit = blue, Bash = orange, Read = cyan — scannable at a glance |
| 🎨 | **Per-agent identity** | Deterministic shirt/hair/skin palette from session hash, 16 curated outfits |
| 🦞 | **OpenClaw gateway mascot** | A live OpenClaw gateway shows up as a wandering lobster whose motion tracks gateway health |
| 🌧️ | **Weather effects** | Rain, storm, snow, fog, overcast, windy — cycles every 10 min + sunset golden hour |
| 🔎 | **Hover tooltips** | Hover an agent for session duration, tool-call count and active-time %; hover any furniture — desks, sofas, plants, vending machine, printer — for its name |
| 🐾 | **Office pets** | A cat or dog (one per floor) ro