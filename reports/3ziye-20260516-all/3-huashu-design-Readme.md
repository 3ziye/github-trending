<sub><b>🌐 English</b> · <a href="README.zh.md">中文</a></sub>

<div align="center">

# Huashu Design

> *"Type. Hit enter. A finished design lands in your lap."*
> *「打字。回车。一份能交付的设计。」*

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Agent-Agnostic](https://img.shields.io/badge/Agent-Agnostic-blueviolet)](https://skills.sh)
[![Skills](https://img.shields.io/badge/skills.sh-Compatible-green)](https://skills.sh)

<br>

**Say one sentence to your agent — Claude Code, Cursor, Codex, OpenClaw, Hermes all work.**

<br>

3 to 30 minutes — you ship a **product launch animation**, a clickable App prototype, an editable PPT deck, a print-grade infographic.

Not "decent for AI" quality — it looks like a real design team made it. Give the skill your brand assets (logo, colors, UI screenshots) and it reads your brand's voice; give it nothing and the built-in 20 design vocabularies still keep you out of AI slop territory.

**Every animation in this README was made by huashu-design itself.** No Figma, no After Effects — just a sentence + skill run. Next product launch needs a promo video? You can make it too.

```
npx skills add alchaincyf/huashu-design
```

> 📣 **Now MIT-licensed.** As of 2026-05-14 this skill is fully open-source under the [MIT License](LICENSE) — free for personal **and** commercial use, no authorization required. ([what changed](#license))

[See it work](#demo-gallery) · [Install](#install) · [What it does](#what-it-does) · [How it works](#core-mechanics) · [vs. Claude Design](#vs-claude-design)

> 📖 **Note for English readers**: this skill is built by a Chinese-speaking developer. The skill's agent prompts (`SKILL.md`, `references/*.md`) are in Chinese but the agent is bilingual — works fine with English tasks. The demos below are the English parallel versions; the Chinese ones are in the default-named files (see the [Chinese README](README.zh.md)).
>
> 📖 **致中文读者**：这个 skill 由花叔（@AlchainHust）开发。一句话能让 agent 在 3–30 分钟内交付**产品发布动画 / 可点击 App 原型 / 可编辑 PPT / 印刷级信息图**。完整中文介绍见 [README.zh.md](README.zh.md)。

</div>

---

<p align="center">
  <video src="https://github.com/alchaincyf/huashu-design/releases/download/v2.0/hero-animation-v10-en.mp4" autoplay muted loop playsinline width="100%">
    Your browser doesn't support inline video. <a href="https://github.com/alchaincyf/huashu-design/releases/download/v2.0/hero-animation-v10-en.mp4">Download MP4</a>.
  </video>
</p>

<p align="center"><sub>▲ 10-second hero animation showing what huashu-design does (<a href="https://github.com/alchaincyf/huashu-design/releases/download/v2.0/hero-animation-v10-en.mp4">download MP4</a> if autoplay doesn't work)</sub></p>

---

## Install

```bash
npx skills add alchaincyf/huashu-design
```

Then just talk to Claude Code:

```
"Make a keynote for AI psychology. Give me 3 style directions to pick from."
"Build an iOS prototype for a Pomodoro app — 4 screens, actually clickable."
"Turn this logic into a 60-second animation. Export MP4 and GIF."
"Run a 5-dimension expert review on this design."
```

No buttons, no panels, no Figma plugin. Agent-agnostic — drops into Claude Code, Cursor, Trae, Hermes, OpenClaw, or any markdown-skill-capable agent.

---

## Star History

<p align="center">
  <a href="https://star-history.com/#alchaincyf/huashu-design&Date">
    <img src="https://api.star-history.com/svg?repos=alchaincyf/huashu-design&type=Date" alt="huashu-design Star History" width="80%">
  </a>
</p>

---

## What it does

| Capability | Deliverable | Typical time |
|---|---|---|
| Interactive prototype (App / Web) | Single-file HTML · real iPhone bezel · clickable · Playwright-verified | 10–15 min |
| Slide decks | HTML deck (browser presentation) + editable PPTX (text frames preserved) | 15–25 min |
| Motion design | MP4 (25fps / 60fps interpolation) + GIF (palette-optimized) + BGM | 8–12 min |
| Design variations | 3+ side-by-side · Tweaks live params · cross-dimension exploration | 10 min |
| Infographic / data viz | Print-quality typography · exports to PDF/PNG/SVG | 10 min |
| Design direction advisor | 5 schools × 20 philosophies · 3 directions recommended · Demos generated in parallel | 5 min |
| 5-dimension expert critique | Radar chart + Keep/Fix/Quick Wins · actionable punch list | 3 min |

---

## Demo Gallery

> English parallel versions of the demos. Chinese versions live at the default filenames (see the Chinese README).

### Design Direction Advisor

The fallback for vague briefs: pick 3 differentiated directions from 5 schools × 20 philosophies, generate all 3 demos in parallel, let the user choose.

<p align="center"><img src="https://github.com/alchaincyf/huashu-design/releases/download/v2.0/w3-fallback-advisor-en.gif" width="100%"></p>

### iOS App Prototype

Pixel-accurate iPhone 15 Pro body (Dynamic Island / status bar / Home Indicator) · state-driven multi-screen navigation · real images pulled from Wikimedia/Met/Unsplash · Playwright click tests before delivery.

<p align="center">