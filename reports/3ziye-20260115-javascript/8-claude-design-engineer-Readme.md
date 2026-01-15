# Design Engineer

<p align="center">
  <strong>Craft · Memory · Enforcement</strong>
</p>

<p align="center">
  Build interfaces with intention. Remember decisions across sessions. Maintain systematic consistency.
</p>

<p align="center">
  <a href="#installation">Install</a> ·
  <a href="#how-it-works">How It Works</a> ·
  <a href="#examples">Examples</a> ·
  <a href="https://dashboard-v4-eta.vercel.app">Demo</a>
</p>

---

## What This Does

When you build UI with Claude, design decisions get made: spacing values, colors, depth strategy, button heights. Without structure, those decisions drift across sessions.

**Design Engineer helps you:**

1. **Craft** — Smart direction inference (dashboard → precision, marketing → bold)
2. **Memory** — Save decisions to `.design-engineer/system.md`, load automatically
3. **Enforcement** — Validate UI code against your system, catch violations before you see them

Make choices once. Enforce them automatically.

## Before & After

**Without design-engineer:**
- Every session starts from scratch
- Button heights drift (36px, 38px, 40px...)
- Random spacing values (14px, 17px, 22px...)
- No consistency across components

**With design-engineer:**
- System loads automatically each session
- Patterns reused (Button: 36px, Card: 16px pad)
- Spacing on grid (4px, 8px, 12px, 16px)
- Violations caught before finishing

See the difference: **[dashboard-v4-eta.vercel.app](https://dashboard-v4-eta.vercel.app)**

---

## Installation

### Plugin (Recommended - Full Features)

```bash
/plugin install oakinleye/design-engineer
```

Gets you:
- ✅ Smart workflows (APPLY, ESTABLISH, EXTEND modes)
- ✅ Automatic system.md loading every session
- ✅ Post-write validation hooks
- ✅ Commands (/design-engineer status, audit, extract)

### Manual (Advanced)

```bash
git clone https://github.com/Dammyjay93/design-engineer.git
cd design-engineer
cp -r . ~/.claude/plugins/design-engineer
```

Restart Claude Code.

---

## How It Works

### Smart Dispatcher

When you build UI, design-engineer automatically detects which mode to use:

**APPLY MODE** (system exists)
```
✓ Loads .design-engineer/system.md
✓ Uses established patterns
✓ Validates before finishing
✓ Updates system if new patterns emerge
```

**ESTABLISH MODE** (real project, no system)
```
1. Scans project (package.json, framework, file structure)
2. Infers product type (dashboard? marketing? docs?)
3. Suggests direction based on context
4. Asks ONE smart question with default
5. Builds components
6. Offers to save system
```

**PRINCIPLES ONLY** (quick prototype)
```
✓ Just applies craft principles
✓ No questions, no system.md
```

### Example: First Session

```
You: "Build a user dashboard with metrics cards"

Claude (via design-engineer):
Detected: Dashboard with data visualization
Suggests: Precision & Density, Cool (slate), Borders-only

Does this direction fit? (y/n/customize)

[You: y]

[Builds dashboard with tight spacing, borders, clean layout]

Created foundations:
- Direction: Precision & Density
- Depth: Borders-only
- Patterns: MetricCard (border, 16px pad, 8px gap)

Save to .design-engineer/system.md? (y)

✓ System saved
```

### Example: Second Session

```
You: "Add a settings page"

Claude (via design-engineer):
✓ Loaded system (Precision & Density, Borders-only)
✓ Reusing MetricCard pattern
✓ Building with established spacing grid

[Builds settings page matching existing design]

✓ Self-validation passed
```

The system **remembers** and **enforces** automatically.

---

## System File

After establishing direction, your decisions live in `.design-engineer/system.md`:

```markdown
# Design System

## Direction
Personality: Precision & Density
Foundation: Cool (slate)
Depth: Borders-only

## Tokens
### Spacing
Base: 4px
Scale: 4, 8, 12, 16, 24, 32

### Colors
--foreground: slate-900
--secondary: slate-600
--accent: blue-600

## Patterns
### Button Primary
- Height: 36px
- Padding: 12px 16px
- Radius: 6px
- Usage: Primary actions

### Card Default
- Border: 0.5px solid
- Padding: 16px
- Radius: 8px
```

This file loads automatically at session start. Claude sees it and maintains consistency.

---

## Commands

```bash
/design-engineer              # Smart status/suggestions
/design-engineer status       # Show current system
/design-engineer audit <path> # Check code against system
/design-engineer extract      # Extract patterns from existing code
```

---

## Design Directions

The skill infers direction from project context, but you can customize:

| Direction | Feel | Best For |
|-----------|------|----------|
| **Precision & Density** | Tight, technical, monochrome | Developer tools, admin dashboards |
| **Warmth & Approachability** | Generous spacing, soft shadows | Collaborative tools, consumer apps |
| **Sophistication & Trust** | Cool tones, layered depth | Finance, enterprise B2B |
| **Boldness & Clarity** | High contrast, dramatic space | Marketing sites, modern dashboards |
| **Utility & Function** | Muted, 