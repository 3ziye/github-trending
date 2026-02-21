<div align="center">

# beautiful-mermaid

**Render Mermaid diagrams as beautiful SVGs or ASCII art**

Ultra-fast, fully themeable, zero DOM dependencies. Built for the AI era.

![beautiful-mermaid sequence diagram example](hero.png)

[![npm version](https://img.shields.io/npm/v/beautiful-mermaid.svg)](https://www.npmjs.com/package/beautiful-mermaid)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

[**Live Demo & Samples**](https://agents.craft.do/mermaid)

**[→ Use it live in Craft Agents](https://agents.craft.do)**

</div>

---

## Why We Built This

Diagrams are essential for AI-assisted programming. When you're working with an AI coding assistant, being able to visualize data flows, state machines, and system architecture—directly in your terminal or chat interface—makes complex concepts instantly graspable.

[Mermaid](https://mermaid.js.org/) is the de facto standard for text-based diagrams. It's brilliant. But the default renderer has problems:

- **Aesthetics** — Might be personal preference, but wished they looked more professional
- **Complex theming** — Customizing colors requires wrestling with CSS classes
- **No terminal output** — Can't render to ASCII for CLI tools
- **Heavy dependencies** — Pulls in a lot of code for simple diagrams

We built `beautiful-mermaid` at [Craft](https://craft.do) to power diagrams in [Craft Agents](https://agents.craft.do). It's fast, beautiful, and works everywhere—from rich UIs to plain terminals.


The ASCII rendering engine is based on [mermaid-ascii](https://github.com/AlexanderGrooff/mermaid-ascii) by Alexander Grooff. We ported it from Go to TypeScript and extended it Thank you Alexander for the excellent foundation! (And inspiration that this was possible.)

## Features

- **5 diagram types** — Flowcharts, State, Sequence, Class, and ER diagrams
- **Dual output** — SVG for rich UIs, ASCII/Unicode for terminals
- **15 built-in themes** — And dead simple to add your own
- **Full Shiki compatibility** — Use any VS Code theme directly
- **Live theme switching** — CSS custom properties, no re-render needed
- **Mono mode** — Beautiful diagrams from just 2 colors
- **Zero DOM dependencies** — Pure TypeScript, works everywhere
- **Ultra-fast** — Renders 100+ diagrams in under 500ms

## Installation

```bash
npm install beautiful-mermaid
# or
bun add beautiful-mermaid
# or
pnpm add beautiful-mermaid
```

## Quick Start

### SVG Output

```typescript
import { renderMermaid } from 'beautiful-mermaid'

const svg = await renderMermaid(`
  graph TD
    A[Start] --> B{Decision}
    B -->|Yes| C[Action]
    B -->|No| D[End]
`)
```

### ASCII Output

```typescript
import { renderMermaidAscii } from 'beautiful-mermaid'

const ascii = renderMermaidAscii(`graph LR; A --> B --> C`)
```

```
┌───┐     ┌───┐     ┌───┐
│   │     │   │     │   │
│ A │────►│ B │────►│ C │
│   │     │   │     │   │
└───┘     └───┘     └───┘
```

### Browser (Script Tag)

For non-bundled environments, include via CDN:

```html
<script src="https://unpkg.com/beautiful-mermaid/dist/beautiful-mermaid.browser.global.js"></script>
<script>
  const { renderMermaid, THEMES } = beautifulMermaid;
  renderMermaid('graph TD; A-->B').then(svg => { ... });
</script>
```

Also available via [jsDelivr](https://cdn.jsdelivr.net/npm/beautiful-mermaid/dist/beautiful-mermaid.browser.global.js). The bundle exposes `renderMermaid`, `renderMermaidAscii`, `THEMES`, `DEFAULTS`, and `fromShikiTheme` on the global `beautifulMermaid` object.

---

## Theming

The theming system is the heart of `beautiful-mermaid`. It's designed to be both powerful and dead simple.

### The Two-Color Foundation

Every diagram needs just two colors: **background** (`bg`) and **foreground** (`fg`). That's it. From these two colors, the entire diagram is derived using `color-mix()`:

```typescript
const svg = await renderMermaid(diagram, {
  bg: '#1a1b26',  // Background
  fg: '#a9b1d6',  // Foreground
})
```

This is **Mono Mode**—a coherent, beautiful diagram from just two colors. The system automatically derives:

| Element | Derivation |
|---------|------------|
| Text | `--fg` at 100% |
| Secondary text | `--fg` at 60% into `--bg` |
| Edge labels | `--fg` at 40% into `--bg` |
| Connectors | `--fg` at 30% into `--bg` |
| Arrow heads | `--fg` at 50% into `--bg` |
| Node fill | `--fg` at 3% into `--bg` |
| Node stroke | `--fg` at 20% into `--bg` |

### Enriched Mode

For richer themes, you can provide optional "enrichment" colors that override specific derivations:

```typescript
const svg = await renderMermaid(diagram, {
  bg: '#1a1b26',
  fg: '#a9b1d6',
  // Optional enrichment:
  line: '#3d59a1',    // Edge/connector color
  accent: '#7aa2f7',  // Arrow heads, highlights
  muted: '#565f89',   // Secondary text, labels
  surface: '#292e42', // Node fill tint
  border: '#3d59a1',  // Node stroke
})
```

If an enrichment color isn't provided, it falls back to the `color-mix()` derivation. This means you can provide just t