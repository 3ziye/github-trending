
# claude-obsidian

<p align="center">
  <img src="wiki/meta/claude-obsidian-gif-cover-16x9.gif" alt="claude-obsidian" width="100%" />
</p>

[![GitHub stars](https://img.shields.io/github/stars/AgriciDaniel/claude-obsidian?style=flat&color=e8734a)](https://github.com/AgriciDaniel/claude-obsidian/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude_Code-plugin-8B5CF6)](https://code.claude.com/docs/en/discover-plugins)
[![Blog Post](https://img.shields.io/badge/Deep_Dive-Blog_Post-22c55e)](https://agricidaniel.com/blog/claude-obsidian-ai-second-brain)

Claude + Obsidian knowledge companion. A running notetaker that builds and maintains a persistent, compounding wiki vault. Every source you add gets integrated. Every question you ask pulls from everything that has been read. Knowledge compounds like interest.

Based on [Andrej Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). **11 skills. Zero manual filing. Multi-agent support. Optional [DragonScale Memory](docs/dragonscale-guide.md) extension** (log folds, deterministic page addresses, semantic tiling lint, boundary-first autoresearch).

---

## What It Does
### [Youtube Demo](https://www.youtube.com/watch?v=a2hgayvr-H4)
<p align="center">
  <img src="wiki/meta/welcome-canvas.gif" alt="Welcome canvas. Visual demo board" width="96%" />
</p>

You drop sources. Claude reads them, extracts entities and concepts, updates cross-references, and files everything into a structured Obsidian vault. The wiki gets richer with every ingest.

You ask questions. Claude reads the hot cache (recent context), scans the index, drills into relevant pages, and synthesizes an answer. It cites specific wiki pages, not training data.

You lint. Claude finds orphans, dead links, stale claims, and missing cross-references. Your wiki stays healthy without manual cleanup.

At the end of every session, Claude updates a hot cache. The next session starts with full recent context, no recap needed.

<p align="center">
  <img src="wiki/meta/image-example-graph-view.png" alt="Graph view. Color-coded wiki nodes" width="48%" />
  <img src="wiki/meta/image-example-wiki-map-view.png" alt="Wiki Map canvas" width="48%" />
</p>

---

## Why claude-obsidian?

Most Obsidian AI plugins are chat interfaces - they answer questions about your existing notes. claude-obsidian is a knowledge engine - it creates, organizes, maintains, and evolves your notes autonomously.

| Capability | claude-obsidian | Smart Connections | Copilot |
|---|---|---|---|
| **Auto-organize notes** | Creates entities, concepts, cross-references | No | No |
| **Contradiction flagging** | `[!contradiction]` callouts with sources | No | No |
| **Session memory** | Hot cache persists between conversations | No | No |
| **Vault maintenance** | 8-category lint (orphans, dead links, gaps) | No | No |
| **Autonomous research** | 3-round web research with gap-filling | No | No |
| **Multi-model support** | Claude, Gemini, Codex, Cursor, Windsurf | Claude only | Multiple |
| **Visual canvas** | Via [claude-canvas](https://github.com/AgriciDaniel/claude-canvas) companion | No | No |
| **Query with citations** | Cites specific wiki pages | Cites similar notes | Cites notes |
| **Batch ingestion** | Parallel agents for multiple sources | No | No |
| **Open source** | MIT | MIT | Freemium |

> **Deep dive:** [I Turned Obsidian Into a Self-Organizing AI Brain](https://agricidaniel.com/blog/claude-obsidian-ai-second-brain) - full breakdown with data visualizations, market context, and workflow demos.

---

## Quick Start

### Option 1: Clone as vault (recommended: full setup in 2 minutes)

```bash
git clone https://github.com/AgriciDaniel/claude-obsidian
cd claude-obsidian
bash bin/setup-vault.sh
```

Open the folder in Obsidian: **Manage Vaults → Open folder as vault → select `claude-obsidian/`**

Open Claude Code in the same folder. Type `/wiki`.

> `setup-vault.sh` configures `graph.json` (filter + colors), `app.json` (excludes plugin dirs), and `appearance.json` (enables CSS). Run it once before the first Obsidian open. You get the fully pre-configured graph view, color scheme, and wiki structure out of the box.

---

### Option 2: Install as Claude Code plugin

Plugin installation is a two-step process in Claude Code. First add the marketplace catalog, then install the plugin from it.

```bash
# Step 1: add the marketplace
claude plugin marketplace add AgriciDaniel/claude-obsidian

# Step 2: install the plugin
claude plugin install claude-obsidian@claude-obsidian-marketplace
```

In any Claude Code session: `/wiki`. Claude walks you through vault setup.

To check it worked:
```bash
claude plugin list
```

---

### Option 3: Add to an existing vault

Copy `WIKI.md` into your vault root. Paste into Claude:

```
Read WIKI.md in this project. Then:
1. Check if Obsidian is installed. If not, install it.
2. Check 