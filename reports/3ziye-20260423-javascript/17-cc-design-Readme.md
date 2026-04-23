# cc-design

**[Demo](https://cc-design-demo.vercel.app)**

A Claude Code skill for high-fidelity HTML design and prototype creation — slide decks, interactive prototypes, landing pages, UI mockups, animations, and visual design explorations.

## Screenshots

**Demo Gallery**

[![Demo Gallery](./screenshots/previews/cc-design-home-preview.png)](./screenshots/previews/cc-design-home-preview.png)

<p align="center">
  <a href="./screenshots/previews/cc-design-enterprise-preview.png"><img src="./screenshots/previews/cc-design-enterprise-preview.png" alt="Enterprise Hero" width="32%"></a>
  <a href="./screenshots/previews/cc-design-scifi-preview.png"><img src="./screenshots/previews/cc-design-scifi-preview.png" alt="Sci-Fi Website" width="32%"></a>
  <a href="./screenshots/previews/cc-design-tesla-preview.png"><img src="./screenshots/previews/cc-design-tesla-preview.png" alt="Tesla 3D" width="32%"></a>
</p>
<p align="center">
  <a href="./screenshots/previews/cc-design-aether-preview.png"><img src="./screenshots/previews/cc-design-aether-preview.png" alt="AETHER" width="32%"></a>
  <a href="./screenshots/previews/cc-design-glass-preview.png"><img src="./screenshots/previews/cc-design-glass-preview.png" alt="Glass Dashboard" width="32%"></a>
  <a href="./screenshots/previews/cc-design-banking-preview.png"><img src="./screenshots/previews/cc-design-banking-preview.png" alt="Banking App" width="32%"></a>
</p>

## Overview

cc-design embeds a structured design workflow into Claude Code, enabling it to operate as an expert product designer. Five core principles guide every task:

- **Fact verification (P0)** — Never guess. Verify claims about design trends, brand aesthetics, or technology. Wrong facts are worse than no facts.
- **Gather enough context first (P1)** — Resolve or explicitly assume the blocking fields before any full build: audience, output shape, scope, hard constraints, reference source, and success criteria.
- **Visible plan before build (P1.5)** — Once blocking uncertainty is resolved, produce a short execution plan and wait for approval before starting the full build.
- **Anti-AI slop (P2)** — Aggressive gradients, emoji (unless brand), generic SaaS hero sections, and overused fonts are banned. Full rules in `references/content-guidelines.md`.
- **Audible loading (P3)** — Runtime bundles are never loaded silently. cc-design announces every reference/template bundle with `Load: because=... loaded=...` before using it.

Progressive disclosure keeps the main skill definition concise while 27+ technical references load on demand.
`load-manifest.json` is the machine-readable source of truth for bundle contents, `scripts/generate-bundle-catalog.mjs` generates the bundle catalog for AI matching, and `scripts/lint-load-manifest.mjs` checks that every reference/template is accounted for. Routing prefers a semantic-matching subagent when the platform provides one, and falls back to `scripts/resolve-load-bundles.mjs` when it does not.

Runtime bundles are organized into three groups:
- **Base-required bundles (`基础必载`)** — always loaded for every design task, including typography, layout patterns, and visual/color theory
- **Conditionally required bundles (`条件命中后必载`)** — loaded when a task type or checkpoint is triggered
- **Truly optional inspirations (`真正可选`)** — case studies and reference material only

The core product promise is behavioral, not just feature breadth:
- every design task starts with the base-required bundle
- new ambiguous tasks start with structured step-by-step confirmation
- new tasks use a short route-shaping question batch before loading additional task bundles
- richly specified briefs can skip most clarification, but still require a visible plan before build
- explicit speed requests compress clarification, but still produce a mini-plan unless the user explicitly says to skip planning
- first-pass work stops for approval after the plan
- small edits and follow-up iterations do not reopen the full discovery flow
- existing `DESIGN.md` files are never silently rewritten; the user confirms append / merge / overwrite first

## Features

| Category | Capabilities |
|---|---|
| **Output formats** | Interactive prototypes, slide decks, landing pages, UI mockups, animated motion studies, wireframes, design systems |
| **Design philosophies** | 20 design philosophy schools organized in 5 schools: Information Architects, Motion Poets, Minimalists, Experimental Vanguard, Eastern Philosophy. See `references/design-styles.md` |
| **Design thinking** | 8-layer design framework (Goal→Information→Structure→Interaction→Visual→Brand→System→Validation), 10 core design principles, theory foundations for each layer |
| **Brand style cloning** | Progressive loading of 68+ brand design systems from [getdesign.md](https://getdesign.md) |
| **Design patterns** | Curated catalog of proven layout patterns with case studies |
| **Design review** | 5-dimension scoring framework (Philosophy Alignment, Visual Hier