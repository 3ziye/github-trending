<p align="center">
  <img src="website/public/logo-specimen.svg" alt="designlang — reads a website the way a developer reads a stylesheet" width="900">
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/designlang"><img src="https://img.shields.io/npm/v/designlang?color=0A0908&labelColor=F3F1EA&label=npm" alt="npm version"></a>
  <a href="https://github.com/Manavarya09/design-extract/blob/main/LICENSE"><img src="https://img.shields.io/github/license/Manavarya09/design-extract?color=0A0908&labelColor=F3F1EA" alt="license"></a>
  <a href="https://nodejs.org"><img src="https://img.shields.io/node/v/designlang?color=0A0908&labelColor=F3F1EA" alt="node version"></a>
  <a href="https://designlang.manavaryasingh.com/"><img src="https://img.shields.io/badge/website-live-FF4800?labelColor=F3F1EA" alt="website"></a>

</p>

---

<p align="center">
  <img src="designlang.png" alt="designlang in action" width="100%">
</p>

[![designlang on npm](https://pkgfolio.vercel.app/embed/pkg/designlang?v=2)](https://www.npmjs.com/package/designlang)

**designlang** points a headless browser at any URL and reads the design system off the live DOM. One command emits 17+ files — DTCG tokens, Tailwind config, shadcn theme, Figma variables, motion tokens, typed component anatomy, brand voice, page-intent labels, and a paste-ready prompt pack for v0 / Lovable / Cursor / Claude Artifacts.

It also goes where extractors don't: **layout patterns**, **responsive behavior across 4 breakpoints**, **hover / focus / active states**, **WCAG contrast scoring**, **multi-page consistency**, **drift checks against a live source-of-truth**, **visual-diffs**, and a **shareable graded report card**.

## Quick start

```bash
npx designlang https://stripe.com                      # extract everything
npx designlang pair stripe.com linear.app              # fuse two designs (visuals A × voice B)    ← v12.8
npx designlang brand stripe.com                        # full brand-guidelines book (13 chapters)  ← v12.7
npx designlang theme-swap stripe.com --primary "#ff4800"  # recolour around your brand        ← v12.6
npx designlang pack stripe.com                         # one polished design-system directory ← v12.4
npx designlang remix stripe.com --as cyberpunk         # restyle in another vocabulary       ← v12.3
npx designlang remix stripe.com --all                  # emit all 6 vocabs at once           ← v12.3
npx designlang grade https://stripe.com --badge        # report card + SVG badge             ← v12.2
npx designlang battle stripe.com vercel.com            # head-to-head graded fight           ← v12.2
npx designlang clone https://stripe.com                # working Next.js starter
npx designlang --full https://stripe.com               # screenshots + responsive + interactions
```

Drop a live design-score badge in any README:

```markdown
![Design Score](https://designlang.app/badge/stripe.com.svg)
```

## Install

```bash
npm i -g designlang                         # global
npx skills add Manavarya09/design-extract   # as an agent skill (40+ agents)
```

## What you get

Each run writes 17+ files to `./design-extract-output/`. The headline outputs:

| File | What it is |
|---|---|
| `*-design-language.md` | 19-section markdown — feed any LLM to recreate the design |
| `*-design-tokens.json` | W3C DTCG tokens (primitive + semantic + composite layers) |
| `*-tailwind.config.js` | Drop-in Tailwind theme |
| `*-shadcn-theme.css` | shadcn/ui `globals.css` variables |
| `*-figma-variables.json` | Figma Variables import (light + dark) |
| `*-variables.css` | CSS custom properties |
| `*-anatomy.tsx` | Typed React stubs for every detected component + variants |
| `*-motion-tokens.json` | Durations, easings, springs, scroll-linked flag |
| `*-voice.json` | Brand voice — tone, pronoun posture, CTA verbs |
| `*-prompts/` | Paste-ready prompts for v0, Lovable, Cursor, Claude Artifacts |
| `*-mcp.json` | Disk-backed MCP server payload |
| `*-grade.html` | **v12.1** Shareable Design Report Card (letter grade + evidence) |
| `*-grade.svg` | **v12.2** Shields.io-style design-score badge (drop into any README) |
| `*-battle.html` | **v12.2** Head-to-head graded battle card from `designlang battle` |
| `*-remix.<vocab>.html` | **v12.3** Site restyled in another vocabulary — brutalist / swiss / art-deco / cyberpunk / soft-ui / editorial |

Multi-platform (`--platforms web,ios,android,flutter,wordpress,all`) adds `ios/`, `android/`, `flutter/`, and a WordPress block theme. `--emit-agent-rules` adds Cursor / Claude Code / generic agent rule files.

## Why designlang vs anything else

Other tools give you the paint. designlang reads the architecture:

- **Layout system** — grids, flex containers, container widths, gaps — not just tokens.
- **Responsive** — crawls 4 breakpoints and reports what changes (`--responsive`).
- **Interaction states** — programmatically hovers and focuses, captures the deltas (`--interactions`, `--deep-interact`).
- **Motion lan