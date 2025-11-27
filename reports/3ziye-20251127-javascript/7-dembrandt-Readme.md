# 🎨 Dembrandt

[![npm version](https://img.shields.io/npm/v/dembrandt.svg)](https://www.npmjs.com/package/dembrandt)
[![npm downloads](https://img.shields.io/npm/dm/dembrandt.svg)](https://www.npmjs.com/package/dembrandt)
[![license](https://img.shields.io/npm/l/dembrandt.svg)](https://github.com/thevangelist/dembrandt/blob/main/LICENSE)

A CLI tool for extracting design tokens and brand assets from any website. Powered by Playwright with advanced bot detection avoidance.

![Dembrandt Demo](showcase.png)

## Quick Start

```bash
npx dembrandt stripe.com
```

No installation required! Extract design tokens from any website in seconds. Or install globally with `npm install -g dembrandt`.

## What It Does

Dembrandt analyzes live websites and extracts their complete design system:

- **Logo** — Logo detection (img/svg) with dimensions and source URL
- **Favicons** — All favicon variants with sizes and types
- **Colors** — Semantic colors, color palette with confidence scoring, CSS variables (both hex and RGB formats)
- **Typography** — Font families, sizes, weights, line heights, font sources (Google Fonts, Adobe Fonts, custom)
- **Spacing** — Margin and padding scales with grid system detection (4px/8px/custom)
- **Border Radius** — Corner radius patterns with usage frequency
- **Borders** — Border widths, styles (solid, dashed, dotted), and colors with confidence scoring
- **Shadows** — Box shadow values for elevation systems
- **Buttons** — Component styles with variants and states
- **Inputs** — Form field styles (input, textarea, select)
- **Links** — Link styles with hover states and decorations
- **Breakpoints** — Responsive design breakpoints from media queries
- **Icons** — Icon system detection (Font Awesome, Material Icons, SVG)
- **Frameworks** — CSS framework detection (Tailwind, Bootstrap, Material-UI, Chakra)

Perfect for competitive analysis, brand audits, or rebuilding a brand when you don't have design guidelines.

## Why It Matters

**Designers** — Analyze competitor systems, document production tokens, audit brand consistency

**Developers** — Migrate design tokens, reverse engineer components, validate implementations

**Product Managers** — Track competitor evolution, quantify design debt, evaluate vendors

**Marketing** — Audit competitor brands, plan rebrands, monitor brand compliance

**Engineering Leaders** — Measure technical debt, plan migrations, assess acquisition targets

## How It Works

Uses Playwright to render the page, extracts computed styles from the DOM, analyzes color usage and confidence, groups similar typography, detects spacing patterns, and returns actionable design tokens.

### Extraction Process

1. **Browser Launch** - Launches Chromium with stealth configuration
2. **Anti-Detection** - Injects scripts to bypass bot detection
3. **Navigation** - Navigates to target URL with retry logic
4. **Hydration** - Waits for SPAs to fully load (8s initial + 4s stabilization)
5. **Content Validation** - Verifies page content is substantial (>500 chars)
6. **Parallel Extraction** - Runs all extractors concurrently for speed
7. **Analysis** - Analyzes computed styles, DOM structure, and CSS variables
8. **Scoring** - Assigns confidence scores based on context and usage

### Color Confidence

- **High** — Logo, brand elements, primary buttons
- **Medium** — Interactive elements, icons, navigation
- **Low** — Generic UI components (filtered from display)

Only shows high and medium confidence colors in terminal. Full palette in JSON.

### Typography Detection

Samples all heading levels (h1-h6), body text, buttons, links. Groups by font family, size, and weight. Detects Google Fonts, Adobe Fonts, custom @font-face.

### Framework Detection

Recognizes Tailwind CSS, Bootstrap, Material-UI, and others by class patterns and CDN links.

## Installation

### Using npx (Recommended)

No installation needed! Run directly with `npx`:

```bash
npx dembrandt stripe.com
```

The first run will automatically install Chromium (~170MB).

### Global Installation

Install globally for repeated use:

```bash
npm install -g dembrandt
dembrandt stripe.com
```

### Prerequisites

- Node.js 18 or higher

### Development Setup

For contributors who want to work on dembrandt:

```bash
git clone https://github.com/thevangelist/dembrandt.git
cd dembrandt
npm install
npm link
```

## Usage

### Basic Usage

```bash
# Using npx (no installation)
npx dembrandt <url>

# Or if installed globally
dembrandt <url>

# Examples
dembrandt stripe.com
dembrandt https://github.com
dembrandt tailwindcss.com
```

### Options

**`--json-only`** - Output raw JSON to stdout instead of formatted terminal display

```bash
dembrandt stripe.com --json-only > tokens.json
```

Note: JSON is automatically saved to `output/domain.com/` regardless of this flag.

**`-d, --debug`** - Run with visible browser and detailed logs

```bash
dembrandt stripe.com --debug
```

Useful for troubleshooting bot detection, timeouts, or extraction