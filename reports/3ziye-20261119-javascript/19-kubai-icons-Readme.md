<p align="center">
  <img src="site/src/app/icon.svg" width="72" height="72" alt="" />
</p>

<h1 align="center">Kubai Icons</h1>

<p align="center">
  <strong>An agent skill that draws animated icons in one consistent style.</strong><br />
  Plus 2,800+ open-source icons drawn with it, for React, Vue and the web.
</p>

<p align="center">
  <a href="#install-the-skill">Install the skill</a> ·
  <a href="https://icons.kubai.design/icons/">Browse the icons</a> ·
  <a href="#use-the-icons">Use them in code</a> ·
  <a href="https://icons.kubai.design/docs/">Docs</a>
</p>

<p align="center">
  <img src="assets/hover.webp" alt="Sixteen icons opening one after another on hover: a folder opens, an envelope unseals, a calendar turns a page, a lock springs open, a gear turns" />
</p>

## What's included

| Part | What you get |
| --- | --- |
| **Agent skill** | The rules, engine and self-check that draw every icon in one hand. Give Claude Code, Codex or another coding agent a product, and it draws the icons that product needs. |
| **Icon library** | 2,800+ icons: nearly 900 objects, plus badged and slashed "off" versions. For React, Vue, plain JavaScript, web components and static SVG. MIT licensed. |
| **Website** | [icons.kubai.design](https://icons.kubai.design/), in 16 languages. Search every icon by name, shape or meaning, recolor it, copy its code or a prompt for your agent, download it as SVG or PNG, and save a collection as a ZIP. |

## Install the skill

Copy this into your agent and send it:

```text
Install the Kubai Icons skill for me:
clone https://github.com/kubai087/kubai-icons into your skills folder as kubai-icons
(~/.claude/skills in Claude Code, ~/.agents/skills in Codex;
if it's already there, pull the latest version instead),
make sure SKILL.md exists in that folder, and tell me when it's ready.
```

Restart your agent, and the skill is ready. An agent without skill support can read `SKILL.md` from the cloned folder and follow it.

> [!TIP]
> The skill asks for careful geometry and several rounds of looking at its own screenshots, so use a capable model that can read images. It was developed and blind-tested with **Claude Opus 5.5**, which we recommend. Other models, such as GPT in Codex, can use the same skill. In Claude Code, run `claude --model claude-opus-5-5`.

<details>
<summary><strong>Install it yourself</strong></summary>

<br />

Clone the repository into your skills folder. In Codex, use `~/.agents/skills` instead.

```bash
git clone https://github.com/kubai087/kubai-icons.git ~/.claude/skills/kubai-icons
```

Or download `kubai-icons-v*.zip` from the [latest release](https://github.com/kubai087/kubai-icons/releases/latest) and unzip it there:

```bash
unzip kubai-icons-v*.zip -d ~/.claude/skills/
```

The agent picks the skill up the next time it starts.

Publishing to a skill marketplace that asks for a version and display names in `SKILL.md`? Upload `kubai-icons-v*-platform.zip` from the same release. It carries those fields at the top of the frontmatter.

</details>

## Ask for icons

Describe what you need in plain words. The skill triggers on requests about icons, so you don't need to name it.

- "Read this repository and draw dynamic icons for its main features."
- "Add a scissors icon and a map icon to this set."
- "We need an icon for Export that matches the others."
- "Give me static SVG files I can drop into Figma."

The agent then:

1. Reads the rules and writes one line per feature: an everyday object and what it does on hover ("a folder opens", "a lock springs open").
2. Draws each icon after the closest existing one, reusing the engine.
3. Runs the self-check beside existing icons, compares sizes, outlines, layers and colors, and repeats until every item on the checklist passes.

To start a set for your own product, the skill copies the engine, gallery and self-check into your project and works there.

<p align="center">
  <img src="assets/skill.webp" alt="Six icons on hover: an alarm clock rings, a notebook opens, a scan line sweeps a QR code, a door opens to an exit arrow, a calculator key presses, a compass needle settles north" />
</p>

<p align="center"><sub>Drawn by a fresh Claude session that had nothing but <code>SKILL.md</code> and <code>PROMPT.md</code>. Each blind test closes the gaps it finds in the rules.</sub></p>

## Use the icons

| Package | For |
| --- | --- |
| [`kubai-icons-react`](packages/react) | React 18+ and Next.js, server rendering included |
| [`kubai-icons-vue`](packages/vue) | Vue 3 and Nuxt |
| [`kubai-icons`](packages/core) | Any page: a framework-free API and the `<kubai-icon>` web component |
| [`kubai-icons-static`](packages/static) | Standalone SVG files for `<img>`, design tools, native apps and CDNs |

```bash
npm i kubai-icons-react
```

```tsx
import { Folder, CalendarCheck } from "kubai-icons-react";

// 24px, follows the text color
<Folder />

// Any CSS color, the soft look, a green badge
<CalendarCheck size={32} color="#22C55E" 