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
npx designlang https://stripe.com           # extract everything
npx designlang grade https://stripe.com     # shareable HTML report card  ← v12.1
npx designlang clone https://stripe.com     # working Next.js starter
npx designlang --full https://stripe.com    # screenshots + responsive + interactions
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

Multi-platform (`--platforms web,ios,android,flutter,wordpress,all`) adds `ios/`, `android/`, `flutter/`, and a WordPress block theme. `--emit-agent-rules` adds Cursor / Claude Code / generic agent rule files.

## Why designlang vs anything else

Other tools give you the paint. designlang reads the architecture:

- **Layout system** — grids, flex containers, container widths, gaps — not just tokens.
- **Responsive** — crawls 4 breakpoints and reports what changes (`--responsive`).
- **Interaction states** — programmatically hovers and focuses, captures the deltas (`--interactions`, `--deep-interact`).
- **Motion language** — durations, easing families, spring detection, scroll-linked flag, `feel` fingerprint (springy / smooth / mechanical / mixed).
- **Component anatomy** — slot trees with variant × size × state matrices, emitted as typed `.tsx`.
- **Brand voice** — tone, pronoun posture, heading style, CTA verb inventory.
- **Page intent + section roles** — `landing` / `pricing` / `docs` etc., with semantic regions (`hero`, `feature-grid`, `pricing-table`, `cta`…).
- **Multi-page consistency** — auto-discovers canonical pages, reconciles shared vs per-route tokens.
- **WCAG** — every fg/bg pair scored, with a remediation palette suggesting nearest passing colors.
- **Drift + lint + visual-diff** — `designlang drift`, `lint`, `visual-diff` all CI-ready, exit non-zero on failure.
- **Live-site sync** — treat the deployed site as source of truth (`designlang sync`).
- **MCP server** — `designlang mcp` exposes tokens, regions, components, and contrast pairs to any MCP-aware agent.

```bash
designlang grade https://stripe.com         # ← v12.1: shareable report card
designlang clone https://stripe.com         # → working Next.js app
designlang apply https://stripe.com -d ./app   # auto-detect framework, write to