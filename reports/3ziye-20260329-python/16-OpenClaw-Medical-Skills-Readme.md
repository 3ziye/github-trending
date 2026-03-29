# OpenClaw Medical Skills

<div align="center">

[![GitHub Stars](https://img.shields.io/github/stars/FreedomIntelligence/OpenClaw-Medical-Skills?style=for-the-badge&logo=github&color=gold)](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/FreedomIntelligence/OpenClaw-Medical-Skills?style=for-the-badge&logo=github&color=blue)](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills/network/members)
[![GitHub Issues](https://img.shields.io/github/issues/FreedomIntelligence/OpenClaw-Medical-Skills?style=for-the-badge&logo=github)](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills/issues)
[![Skills Count](https://img.shields.io/badge/Skills-869-brightgreen?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyQzYuNDggMiAyIDYuNDggMiAxMnM0LjQ4IDEwIDEwIDEwIDEwLTQuNDggMTAtMTBTMTcuNTIgMiAxMiAyem0tMiAxNWwtNS01IDEuNDEtMS40MUwxMCAxNC4xN2w3LjU5LTcuNTlMMTkgOGwtOSA5eiIvPjwvc3ZnPg==)](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills/tree/main/skills)
[![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-OpenClaw%20%7C%20NanoClaw-orange?style=for-the-badge)](https://github.com/openclaw/openclaw)

**The largest open-source medical AI skill library for OpenClaw.**

*869 curated skills · Clinical · Genomics · Drug Discovery · Bioinformatics · Medical Devices*

[English](#) | [中文](README_zh.md)

</div>

---

## What Is This?

**OpenClaw Medical Skills** is a curated collection of **869 AI agent skills** covering the full spectrum of biomedical and clinical research. These skills are designed for [OpenClaw](https://github.com/openclaw/openclaw) / [NanoClaw](https://github.com/qwibitai/nanoclaw) — Claude-based personal AI assistant frameworks — and transform a general-purpose AI agent into a powerful medical and scientific research companion.

Each skill is a self-contained module (a `SKILL.md` file) that:
- Teaches the agent specialized domain knowledge and workflows
- Connects to real databases, APIs, and computational tools
- Produces structured, clinically or scientifically relevant outputs

> We benefit from the open-source community. The full collection of resources can be found here: [Awesome LLM Resources](https://github.com/WangRongsheng/awesome-LLM-resources?tab=readme-ov-file#%E6%8A%80%E8%83%BD-Skills)

### Why This Collection Matters

| Without Skills | With OpenClaw Medical Skills |
|---|---|
| Generic AI responses about medicine | Real PubMed / ClinicalTrials.gov / FDA queries |
| No bioinformatics capability | RNA-seq, scRNA-seq, GWAS, variant calling pipelines |
| No drug intelligence | ChEMBL, DrugBank, DDI prediction, pharmacovigilance |
| No clinical documentation | SOAP notes, discharge summaries, prior auth decisions |
| No genomics support | VCF annotation, ACMG classification, PRS calculation |
| No regulatory guidance | FDA, CE mark, IEC 62304, ISO 14971 compliance |

This collection aggregates skills from **12+ open-source skill repositories** spanning academic research tools, clinical workflows, regulatory frameworks, and cutting-edge AI-driven protein design — giving your AI agent capabilities comparable to a team of specialized research scientists.

---

## Installation

### Requirements

- [OpenClaw](https://github.com/openclaw/openclaw) installed and running, **or** [NanoClaw](https://github.com/qwibitai/nanoclaw) as an alternative
- Git (for cloning this repo)

---

### For OpenClaw Users

OpenClaw loads skills from two locations:

| Priority | Path | Scope |
|---|---|---|
| High | `<workspace>/skills/` | Per-workspace (recommended) |
| Low | `~/.openclaw/skills/` | Global, shared across all agents |

#### Method 1 — Clone and Copy (Recommended)

```bash
# Clone this repository (skills only — skips large data files)
git clone --depth=1 --no-checkout https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills.git
cd OpenClaw-Medical-Skills
git sparse-checkout init --cone
git sparse-checkout set skills
git checkout main

# Install to your workspace skills directory
cp -r skills/* <your-workspace>/skills/

# Or install globally (available to all agents)
cp -r skills/* ~/.openclaw/skills/
```

> **Note:** Some skills bundle large data files (databases, datasets). The
> sparse-checkout method above avoids downloading them. If you need the full
> repo including all data, install [Git LFS](https://git-lfs.com) first, then
> run `git clone https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills.git`.

Skills are picked up automatically on the next session. No restart needed.

#### Method 2 — OpenClaw CLI

If you use the [OpenClaw plugin registry](https://clawhub.com), you can search and install individual skills from there. For bulk install from this collection, Method 1 is faster.

```ba