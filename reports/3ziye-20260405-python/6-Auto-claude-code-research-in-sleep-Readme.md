# Auto-claude-code-research-in-sleep (ARIS ⚔️🌙)

💡 *Use ARIS in Claude Code / Cursor / Trae as a skill-based workflow, or get the full experience with the standalone CLI — enjoy any way you like!*

🔥 [**ARIS-Code CLI — 独立安装版**](docs/ARIS-Code-README_CN.md) · [English](docs/ARIS-Code-README_EN.md) | [⬇️ Download](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/releases/latest)

> 📰 **ARIS-Code v0.3.3** (2026-04-04) — Fix all config loading crashes for Claude Code hooks compatibility
>
> <details><summary>Previous versions</summary>
>
> **v0.3.0** (2026-04-03) — Multi-file memory index | Rich task system (TodoWrite) | `/plan` | Security hardening
>
> **v0.2.2** (2026-04-03) — `/plan` step-by-step planning | `/tasks` persistent tracking
>
> **v0.2.1** (2026-04-03) — Persistent Memory | Kimi K2.5 multi-turn fix | CJK cursor fix
>
> **v0.2.0** (2026-04-02) — Open source | Kimi + MiniMax + GLM support | Smart LlmReview routing | CI/CD
>
> **v0.1.0** (2026-04-02) — Initial release | Multi-executor & reviewer | 42 bundled skills
>
> </details>

<img src="docs/aris-code-banner.png" width="600" alt="ARIS-Code CLI">

![ARIS Logo](docs/aris_logo.svg)

![Hero](docs/hero_combined.svg)

[中文版 README](README_CN.md) | English

![Score Progression](docs/auto_review_score_curve.png)

> 🌙 **Let Claude Code do research while you sleep.** Wake up to find your paper scored, weaknesses identified, experiments run, and narrative rewritten — autonomously.
>
> 🪶 **Radically lightweight — zero dependencies, zero lock-in.** The entire system is plain Markdown files. No framework to learn, no database to maintain, no Docker to configure, no daemon to babysit. Every skill is a single `SKILL.md` readable by any LLM — swap Claude Code for [Codex CLI](skills/skills-codex/), [OpenClaw](docs/OPENCLAW_ADAPTATION.md), [Cursor](docs/CURSOR_ADAPTATION.md), [Trae](docs/TRAE_ARIS_RUNBOOK_EN.md), [Antigravity](docs/ANTIGRAVITY_ADAPTATION.md), Windsurf, or your own agent and the workflows still work. Fork it, rewrite it, adapt it to your stack.
>
> *💡 ARIS is a methodology, not a platform. What matters is the research workflow — take it wherever you go. 🌱*

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19415257.svg)](https://doi.org/10.5281/zenodo.19415257) · [![Featured on PaperWeekly](https://img.shields.io/badge/Featured%20on-PaperWeekly-red?style=flat)](https://mp.weixin.qq.com/s/tDniVryVGjDkkkWl-5sTkQ) · [![PaperWeekly — MiniMax-M2.7](https://img.shields.io/badge/PaperWeekly-MiniMax--M2.7-red?style=flat)](https://mp.weixin.qq.com/s/KLFU74lAL2FAIc9K6i1Kqg) · [![Featured in awesome-agent-skills](https://img.shields.io/badge/Featured%20in-awesome--agent--skills-blue?style=flat&logo=github)](https://github.com/VoltAgent/awesome-agent-skills) · [![AI Digital Crew - Project of the Day](https://img.shields.io/badge/AI%20Digital%20Crew-Project%20of%20the%20Day%20(2026.03.14)-orange?style=flat)](https://aidigitalcrew.com) · [💬 Join Community](#-community) · [![Cite](https://img.shields.io/badge/📖_Cite_Us-BibTeX-green?style=flat)](#-citation)

Custom [Claude Code](https://docs.anthropic.com/en/docs/claude-code) skills for autonomous ML research workflows. These skills orchestrate **cross-model collaboration** — Claude Code drives the research while an external LLM (via [Codex MCP](https://github.com/openai/codex)) acts as a critical reviewer. 🔀 **Also supports [alternative model combinations](#-alternative-model-combinations) (Kimi, LongCat, DeepSeek, etc.) — no Claude or OpenAI API required.** For example, [MiniMax-M2.7 + GLM-5 or GLM-5 + MiniMax-M2.7](docs/MiniMax-GLM-Configuration.md). 🤖 **[Codex CLI native](skills/skills-codex/)** — full skill set also available for OpenAI Codex. 🖱️ **[Cursor](docs/CURSOR_ADAPTATION.md)** — works in Cursor too. 🖥️ **[Trae](docs/TRAE_ARIS_RUNBOOK_EN.md)** — ByteDance AI IDE. 🚀 **[Antigravity](docs/ANTIGRAVITY_ADAPTATION.md)** — Google's agent-first IDE. 🆓 **[Free tier via ModelScope](docs/MODELSCOPE_GUIDE.md) — zero cost, zero lock-in.**

> 💭 **Why not self-play with a single model?** Using Claude Code subagents or agent teams for both execution and review is technically possible, but tends to fall into **local minima** — the same model reviewing its own patterns creates blind spots.
>
> *Think of it like adversarial vs. stochastic bandits: a single model self-reviewing is the stochastic case (predictable reward noise), while cross-model review is adversarial (the reviewer actively probes weaknesses the executor didn't anticipate) — and adversarial bandits are fundamentally harder to game.*
>
> 💭 **Why two models, not more?** Two is the minimum needed to break self-play blind spots, and 2-player games converge to Nash equilibrium far more efficiently than n-player ones. Adding more reviewers increases API cost and coordination overhead with diminishing returns — the biggest gain is going from 1→2, not 2→4.
>
> Claude Code's strength is fast, fluid execution; Codex (GPT-5.4 xhigh) is slower but mor