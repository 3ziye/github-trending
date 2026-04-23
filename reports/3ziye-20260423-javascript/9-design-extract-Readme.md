<p align="center">
  <img src="website/public/logo-specimen.svg" alt="designlang — reads a website the way a developer reads a stylesheet" width="900">
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/designlang"><img src="https://img.shields.io/npm/v/designlang?color=0A0908&labelColor=F3F1EA&label=npm" alt="npm version"></a>
  <a href="https://github.com/Manavarya09/design-extract/blob/main/LICENSE"><img src="https://img.shields.io/github/license/Manavarya09/design-extract?color=0A0908&labelColor=F3F1EA" alt="license"></a>
  <a href="https://nodejs.org"><img src="https://img.shields.io/node/v/designlang?color=0A0908&labelColor=F3F1EA" alt="node version"></a>
  <a href="https://designlang.manavaryasingh.com/"><img src="https://img.shields.io/badge/website-live-FF4800?labelColor=F3F1EA" alt="website"></a>
[![SafeSkill 77/100](https://img.shields.io/badge/SafeSkill-77%2F100_Passes%20with%20Notes-yellow)](https://safeskill.dev/scan/manavarya09-design-extract)
</p>

---

<p align="center">
  <img src="designlang.png" alt="designlang in action" width="100%">
</p>

[![designlang on npm](https://pkgfolio.vercel.app/embed/pkg/designlang?v=2)](https://www.npmjs.com/package/designlang)

**designlang** crawls any website with a headless browser, extracts every computed style from the live DOM, and generates **17+ output files** — including an AI-optimized markdown file, visual HTML preview, Tailwind config, React theme, shadcn/ui theme, Figma variables, W3C design tokens, CSS custom properties, motion tokens, typed component anatomy stubs, a brand voice summary, **page intent + section roles**, **visual DNA** (material language + imagery style), **component library detection**, a **logo file**, a **multi-page consistency report**, and a **prompt pack** of ready-to-paste prompts for v0, Lovable, Cursor, and Claude Artifacts.

But unlike every other tool out there, it also extracts **layout patterns** (grids, flexbox, containers), **motion language** (durations, easings, springs, scroll-linked animations), **component anatomy** (slots, variant × size × state matrices), **brand voice** (tone, CTA verbs, heading style), captures **responsive behavior** across 4 breakpoints, records **interaction states** (hover, focus, active), scores **WCAG accessibility**, lints your own token files, and lets you **drift-check a codebase against a live site**, **visual-diff two URLs**, **compare multiple brands**, or **sync live sites to local tokens**.

## What's New in v10 — The Intent Release

Everything else captures *how* a site looks. v10 captures *what it is* — the semantic signal an LLM needs to rebuild a site faithfully instead of restyling a generic scaffold.

- **Page Intent** — classifier labels the URL as `landing` / `pricing` / `docs` / `blog` / `blog-post` / `product` / `about` / `dashboard` / `auth` / `legal`, with a confidence score and rival alternates. URL + title + meta + DOM-shape signals. Heuristic-only by default; opt into `--smart` for LLM refinement.
- **Section Roles** — every semantic region gets a role (`hero`, `feature-grid`, `logo-wall`, `stats`, `testimonial`, `pricing-table`, `faq`, `steps`, `comparison`, `gallery`, `bento`, `cta`, `footer`), plus reading order and extracted slot copy (headings, lede, CTA counts).
- **Multi-Page Crawl** — `--full` (or `--pages <n>`) auto-discovers the site's own canonical pages from its nav (pricing/docs/blog/about/product) and runs the full pipeline on each, then emits a cross-page consistency report — shared tokens, per-page uniques, and pairwise Jaccard scores. LLMs get a real design language, not just a homepage snapshot.
- **Material Language** — classifies the visual vocabulary as `glassmorphism` / `neumorphism` / `flat` / `brutalist` / `skeuomorphic` / `material-you` / `soft-ui` / `mixed` from shadow complexity, backdrop-filter usage, saturation, and geometry.
- **Imagery Style** — fingerprints the images: `photography` / `3d-render` / `isometric` / `flat-illustration` / `gradient-mesh` / `icon-only` / `screenshot` / `mixed`, plus dominant aspect ratio and image-radius profile.
- **Component Library Detection** — identifies `shadcn/ui`, `radix-ui`, `headlessui`, `mui`, `chakra-ui`, `mantine`, `ant-design`, `bootstrap`, `heroui`, `tailwind-ui`, `vuetify`, or plain `tailwindcss`, with evidence and alternates.
- **Logo Extraction** — `--full` writes `*-logo.svg` (or `.png`) plus `*-logo.json` with dimensions, aspect, and sampled clearspace.
- **Prompt Pack** — a `*-prompts/` directory with `v0.txt`, `lovable.txt`, `cursor.md`, `claude-artifacts.md`, and atomic `recipe-<component>.md` cards — tokens, section order, voice, and library inlined so one paste is enough.
- **`--smart` mode** — when a heuristic classifier returns low confidence, fall back to a small LLM call (uses `OPENAI_API_KEY` or `ANTHROPIC_API_KEY` from env). Completely optional — no key, no behavior change.

## What's New in v9 — The Motion & Voice Release

- **Motion Language** — durat