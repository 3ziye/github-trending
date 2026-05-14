# cc-design

**High-fidelity HTML design for Claude Code & Codex.**

Slide decks, landing pages, interactive prototypes, interactive explainers, animations, design systems, and more — powered by structured design thinking and built-in quality guardrails.

[Demo](https://cc-design-demo.vercel.app) · [Examples](./EXAMPLES.md) · [Report Bug](https://github.com/ZeroZ-lab/cc-design/issues)

---

## Quick Start

### Claude Code

```bash
# 1. Add the cc-design marketplace
/plugin marketplace add ZeroZ-lab/cc-design

# 2. Install the plugin
/plugin install cc-design@cc-design

# 3. Reload plugins to activate
/reload-plugins
```

After installation, cc-design activates via `/cc-design:design` command.

### Codex

```bash
# 1. Add the cc-design marketplace from GitHub
/plugin marketplace add ZeroZ-lab/cc-design

# 2. Install the plugin
/plugin install cc-design@cc-design

# 3. Reload plugins to activate
/reload-plugins
```

After installation, cc-design activates via `$cc-design` reference.

### Example prompts

```
"Design a landing page for our SaaS product"
"Create a 10-slide pitch deck for the Q3 board meeting"
"Build an interactive prototype of the checkout flow"
"Create an interactive explainer showing how our RAG pipeline works"
"Make a comparison explainer for React vs Vue"
"Build a decision tree for tech stack selection"
"Animate this logo reveal with the Pentagram style"
"Export the deck as editable PPTX"
```

cc-design handles context gathering, design planning, quality checks, and verification — you approve the plan, it builds.

## Showcase

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

## Capabilities

| Category | What you get |
|---|---|
| **Design outputs** | Landing pages, slide decks, interactive prototypes, interactive explainers (flow, compare, decision tree), wireframes, animations, design systems, motion studies |
| **Design thinking** | 8-layer framework (Goal → Validation), 10 core principles, 20 philosophy schools |
| **Brand cloning** | Progressive loading of 68+ brand design systems from [getdesign.md](https://getdesign.md) |
| **Quality guardrails** | Anti-AI slop rules, typography system, spacing scale, mandatory screenshot verification |
| **Variations** | 3+ design directions across layout, interaction, visual intensity, and motion |
| **Export** | PDF (multi-file + single-file), PPTX (image + editable), MP4 video, inline HTML |
| **Audio** | Dual-track audio (SFX + BGM), 37 SFX catalog, ffmpeg mixing |
| **Design review** | 5-dimension scoring: philosophy, hierarchy, craft, functionality, originality |
| **Animation** | Stage+Sprite timeline engine, easing library, signal protocol, pitfall guardrails |
| **Prototyping** | React + Babel inline JSX, device frames (iOS, Android, macOS, browser) |

## Design Styles

Mention a philosophy school to set the direction:

```
"Use the Pentagram style for this infographic"
"Apply Experimental Jetset minimalism to this poster"
"Mix Takram restraint with Locomotive motion for the hero"
```

20 schools across 5 traditions — Information Architects, Motion Poets, Minimalists, Experimental Vanguard, Eastern Philosophy. See `references/design-styles.md`.

### Brand Style Cloning

Mention a brand name to load its design system:

```
"Create a pricing page with Stripe's aesthetic"
"Notion-style kanban board"
"Mix Vercel's minimalism with Linear's purple accents"
```

## How It Works

```
Understand → Route → Plan → Approve → Build → Verify → Deliver
```

1. **Understand** — cc-design asks targeted questions to lock the output type, audience, and constraints
2. **Plan** — presents a visible execution plan with goals, facts, and assumptions
3. **Approve** — you approve before any code is written
4. **Build** — per-section preview pattern; you approve section by section
5. **Verify** — three-phase self-check (structural, visual, design excellence)
6. **Deliver** — screenshot-v