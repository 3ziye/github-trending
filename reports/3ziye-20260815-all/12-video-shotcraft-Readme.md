<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/brand/logo-mark-reverse.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/brand/logo-mark.svg">
  <img alt="video-shotcraft logo" src="./assets/brand/logo-mark.svg" width="112" height="112">
</picture>

<h1>video-shotcraft</h1>

[![GitHub stars](https://img.shields.io/github/stars/Vincentwei1021/video-shotcraft)](https://github.com/Vincentwei1021/video-shotcraft/stargazers)
[![AtomGit Star](https://atomgit.com/VincentWei/video-shotcraft/star/badge.svg)](https://atomgit.com/VincentWei/video-shotcraft)
[![Gallery](https://img.shields.io/badge/Gallery-live%20previews-d3923c)](https://vincentwei1021.github.io/video-shotcraft/)

<a href="https://trendshift.io/repositories/88911?utm_source=trendshift-badge&utm_medium=badge&utm_campaign=badge-trendshift-88911" target="_blank" rel="noopener noreferrer"><img src="https://trendshift.io/api/badge/trendshift/repositories/88911/daily?language=TypeScript" alt="Vincentwei1021%2Fvideo-shotcraft | Trendshift" width="250" height="55"/></a>
<a href="https://trendshift.io/repositories/88911?utm_source=trendshift-badge&utm_medium=badge&utm_campaign=badge-trendshift-88911" target="_blank" rel="noopener noreferrer"><img src="https://trendshift.io/api/badge/trendshift/repositories/88911/weekly?language=TypeScript" alt="Vincentwei1021%2Fvideo-shotcraft | Trendshift" width="250" height="55"/></a>

**An agent skill for crafting cinematic product videos: 152 shot recipe cards · 209 styles · 209 motion previews · a production-ready template**

[English](README.md) | [中文](README_CN.md) | [日本語](README_JA.md)

</div>

**video-shotcraft** is an AI agent skill that turns Claude Code or Codex into a
motion-design studio: point it at your product and it storyboards, animates, and
sound-designs a cinematic promo, marketing, launch, or demo video with
[Remotion](https://www.remotion.dev/) — real page captures, 2.5D camera moves,
beat-synced cuts, and film-grade SFX included.

🖼️ [**Browse all 209 motion previews in the live Gallery »**](https://vincentwei1021.github.io/video-shotcraft/)

## ✨ What's new

> [!IMPORTANT]
> ### 🆕 2026-08 · 48 new shot recipe cards
> The library grows from 104 to **152 cards / 209 previews**. Distilled from
> 209 candidate motions through eight rounds of frame-by-frame review against
> reference footage, then folded into the regular Gallery categories with full
> recipe cards, native Remotion components
> (`demos/<category>/<name>/<Component>.tsx`, deterministic and driven by the
> normalized progress `t` — see demos/README.md for the wiring snippet), and
> motion previews. All de-branded: neutral placeholder copy and a single
> swappable `ACCENT` color variable.

- **2026-08 · JianYing (CapCut CN) project export** — after final delivery the
  film can be exported as an editable JianYing draft: the plate is cut per
  shot (retime/reorder/grade), captions are rebuilt as native text tracks
  (content/size/color editable), SFX/BGM land on separate audio tracks.
  Verified on JianYing Pro 11.2 for macOS; see
  [references/jianying-export.md](references/jianying-export.md).
- **2026-07 · Audio library restructure** — `bgm/` + `sfx/<category>/` with 149
  SFX across 16 scene/material categories, md5-deduplicated with license URLs
  restored.
- **2026-07 · Gallery upgrades** — multi-category card tags, flat alphabetized
  All view, auto-deploy to GitHub Pages with preview mp4s served from a release.

## 🎬 Showcase

The 38-second Gallery intro below was itself produced with this skill —
storyboard, shot implementation, and sound design were all done by an agent
following the toolkit's methodology:

https://github.com/user-attachments/assets/cba2df8a-4b2e-4247-bace-d0b1dea9c2bd

▶️ [Watch in HD on YouTube](https://youtu.be/gcVvRM_P3SM)

> Browse every shot card and motion preview online: **[Gallery](https://vincentwei1021.github.io/video-shotcraft/)**
> — search, filter, switch between variants, and copy selected shot-card names.

## 🚀 Quick start

**The most direct way: hand the repo link to your agent.**
In Claude Code / Codex or a similar agent, just say:

```text
Install this skill for me: https://github.com/Vincentwei1021/video-shotcraft
```

The agent will clone the repo and link it into your skills directory. Or install
with the [skills](https://skills.sh/) CLI / manually:

```bash
npx skills add Vincentwei1021/video-shotcraft
```

```bash
git clone https://github.com/Vincentwei1021/video-shotcraft.git
cd video-shotcraft
ln -s "$(pwd)" ~/.claude/skills/video-shotcraft   # Claude Code
# or
ln -s "$(pwd)" ~/.codex/skills/video-shotcraft    # Codex
```

Then make requests like:

```text
Use video-shotcraft to create a promo for my desktop product.
Use the deck-deal-flyin and row-embed shot cards to present this feature.
Design a product close-up inspired by spotlight-hero-card.
```

If no shot card is specified, the skill introduces the built-in video tem