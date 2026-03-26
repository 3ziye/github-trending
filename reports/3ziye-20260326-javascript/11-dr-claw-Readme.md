<div align="center">
  <img src="public/dr-claw.png" alt="Dr. Claw" width="128" height="128">
  <h1>Dr. Claw: Your AI Research Assistant</h1>
  <p><strong>Full-stack research workspace.</strong></p>
</div>

<p align="center">
<a href="https://openlair.github.io/dr-claw">
<img src="https://img.shields.io/badge/%F0%9F%8C%90-Homepage-CB2B3E?style=for-the-badge" alt="Homepage" />
</a>
<a href="https://github.com/OpenLAIR/dr-claw">
<img src="https://img.shields.io/badge/%F0%9F%A6%9E-Dr.%20Claw-CB2B3E?style=for-the-badge" alt="Dr. Claw" />
</a>
<a href="https://github.com/OpenLAIR/dr-claw/blob/main/LICENSE">
<img src="https://img.shields.io/badge/License-GPL--3.0%20%2B%20AGPL--3.0-blue?style=for-the-badge" alt="License: GPL-3.0 + AGPL-3.0" />
</a>
<a href="https://join.slack.com/t/vibe-lab-group/shared_invite/zt-3r4bkcx5t-iGyRMI~r09zt7p_ND2eP9A">
<img src="https://img.shields.io/badge/Join-Slack-4A154B?style=for-the-badge&logo=slack" alt="Join Slack" />
</a>
<a href="https://x.com/Vibe2038004">
<img src="https://img.shields.io/badge/Follow-on%20X-black?style=for-the-badge&logo=x" alt="Follow on X" />
</a>
<a href="./public/wechat-group-qr.jpg">
<img src="https://img.shields.io/badge/Join-WeChat-07C160?style=for-the-badge&logo=wechat&logoColor=white" alt="Join WeChat" />
</a>
</p>

<p align="center">
  <a href="./README.md">English</a> | <a href="./README.zh-CN.md">中文</a>
</p>

## Table of Contents

- [Overview](#overview)
- [Highlights](#highlights)
- [Quick Start](#quick-start)
- [Configuration](#configuration)
- [OpenClaw Integration](#openclaw-integration)
- [Research Lab - Quick Example](#research-lab-quick-example)
- [Usage Guide](#usage-guide)
- [Additional Details](#additional-details)
- [Contributing](#contributing)
- [FAQ](./docs/faq.md)
- [License](#license)
- [Citation](#citation)
- [Acknowledgments](#acknowledgments)
- [Support & Community](#support--community)

## Overview

Dr. Claw is a general-purpose AI research assistant designed to help researchers and builders execute end-to-end projects across different domains. From shaping an initial idea to running experiments and preparing publication-ready outputs, Dr. Claw keeps the full workflow in one place so teams can focus on research quality and iteration speed.

## Product Screenshot

<p align="center">
  <img src="public/screenshots/chat.png" alt="Dr. Claw chat interface" width="1000">
</p>

<details>
<summary><strong>The Philosophy: Leveraged Cognition</strong></summary>

<p align="center">
  <img src="public/leveraged-cognition.png" alt="Leveraged Cognition" width="900">
</p>

**Manual work is too slow. Fully automated AI is too generic. Vibe Researching is the new frontier.** Dr. Claw turns your **Research Taste** into outsized outcomes with **Agentic Execution**--so you can move faster, think bigger, and still hold the line on scientific rigor.

</details>

## Highlights

- **🔬 Research Lab** — Structured dashboard for end-to-end research: define your brief, generate a pipeline of tasks, track progress across Survey → Ideation → Experiment → Publication → Promotion, and inspect source papers, ideas (rendered with LaTeX math), and cache artifacts — all at a glance
- **⚡ Auto Research** — Start one-click sequential task execution directly from the Project Dashboard, open the generated session live, and receive an email when the run completes
- **📚 100+ Research Skills** — A curated library spanning idea generation, code survey, experiment development & analysis, paper writing, review response, and delivery — automatically discovered by agents and applied as task-level assistance
- **🗂️ Chat-Driven Pipeline** — Describe your research idea in Chat; the agent uses the `inno-pipeline-planner` skill to interactively generate a structured research brief and task list — no manual templates needed
- **🤖 Multi-Agent Backend** — Seamlessly switch between Claude Code, Gemini CLI, and Codex as your execution engines

### What the Pipeline Produces

| | Artifact | Location | Description |
|---|---|---|---|
| 📚 | Survey reports | `Survey/reports/` | Literature reviews with citations from arXiv, Semantic Scholar, and web sources |
| 💡 | Research ideas | `Ideation/ideas/` | Brainstorming outputs with multi-persona evaluation scores |
| 🔬 | Experiment code | `Experiment/core_code/` | Implementation from the plan → implement → judge loop |
| 📊 | Analysis results | `Experiment/analysis/` | Statistical analysis, tables, and paper-ready figures |
| 📝 | Paper draft | `Publication/paper/` | Academic manuscript (IEEE/ACM format) with citations and LaTeX math |
| 🎞️ | Presentation | `Promotion/slides/` | Slide deck, TTS narration audio, and demo video |

> See [docs/pipeline-outputs.md](docs/pipeline-outputs.md) for the full artifact list and project directory structure.

<details>
<summary><span style="font-size: 1.17em; font-weight: 600;">More Features</span></summary>

- **💬 Interactive Chat + Shell** — Chat with your agent or drop into a full terminal — side by sid