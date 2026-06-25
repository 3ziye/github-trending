# baoyu-design

**Run Claude Design on your own local agent — Cursor, Claude Code, Claude Desktop, or any file‑capable coding agent.**

[English](README.md) · [简体中文](README.zh-CN.md) · [Changelog](CHANGELOG.md)

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg) ![Best with Opus 4.8](https://img.shields.io/badge/Best%20with-Opus%204.8-d97757) ![Harness](https://img.shields.io/badge/Cursor%20%C2%B7%20Claude%20Code%20%C2%B7%20Codex-supported-1f6feb)

`baoyu-design` packages **Claude Design** — the design engine behind [claude.ai/design](https://claude.ai/design) — as a portable **Agent Skill**. Drop it into a local agent and you get most of what the website does, right inside your editor: polished UI mockups, interactive prototypes, wireframes, landing pages, dashboards, mobile apps, and slide decks — all produced as self‑contained HTML.

No website, no separate subscription, no upload step. The agent already on your machine does the work, and every artifact stays in your repo.

---

## Screenshots

The same Reader Mac App prompt was used in Cursor, Codex, Claude, and Claude Design.

| Cursor | Codex | Claude | Claude Design |
|---|---|---|---|
| <img src="assets/screenshots/cursor-reader-mac-app.webp" alt="Cursor running baoyu-design" width="240"> | <img src="assets/screenshots/codex-reader-mac-app.webp" alt="Codex running baoyu-design" width="240"> | <img src="assets/screenshots/claude-reader-mac-app.webp" alt="Claude running baoyu-design" width="240"> | <img src="assets/screenshots/claude-design-reader-mac-app.webp" alt="Claude Design running the same Reader Mac App prompt" width="240"> |

<details>
<summary>Prompt used for all screenshots</summary>

```markdown
Build a Reader Mac app that helps me read and save articles better. All data is stored locally.

## Information collection

1. Manual adding
Support manually adding different types of information:
- URL: enter a URL and automatically fetch content and images
- Attachments: upload PDFs, videos, and images
- Markdown editing: like publishing a blog post, enter the title, body, and cover image
- Other

2. Automatic subscriptions
- RSS feeds
- Social media accounts: X, Weibo, YouTube
- Other

## Editing and organization

1. Tags
Every item can have tags.

2. Categories and folders
Create tree-structured folders and place content in different categories.

3. Favorites
Users can click to favorite an item.

4. Editing
Every item can be edited with a built-in Markdown editor.

## AI assistance

1. Automatic translation
Support translation across different languages.

2. Summaries and abstracts
Generate summaries for captured content.

3. Derivative creation
Create new work based on one or more pieces of content.

4. Integrated AI Chat
Use AI Chat to call AI Agents that help process content.
```

</details>

---

## Why run it locally

- **Free yourself from the website.** You get the vast majority of `claude.ai/design`'s capabilities without ever leaving your editor — same methodology, same craft standards, same output format.
- **Best with Opus 4.8.** The skill is a long, demanding design brief; the stronger the model, the better the result. Pair it with **Claude Opus 4.8** for the best output, and it still works well on other capable models.
- **Iterate by pointing, not describing.** Because the deliverable is plain HTML served on `localhost`, you can lean on your agent's built‑in browser preview and element‑annotation tools (Cursor Browser / DevTools, Claude Preview, or Codex Browser). Point at a button in the live preview, say what you want changed, and the agent edits the underlying source — a tight, visual second‑pass editing loop that's hard to get on a website.
- **Everything is yours.** Output lands in `designs/<project>/` as self‑contained HTML you can version, fork, export, or ship.

---

## What it can make

The skill drives a full design process — clarifying questions → gathering design context → producing one or more HTML deliverables → previewing and verifying. It ships a deep bench of **built‑in skills** and a set of ready‑made component scaffolds.

| Area | Built‑in skills |
|---|---|
| **Core design** | Hi‑fi design · Interactive prototype · Wireframe · Frontend aesthetic direction |
| **Decks** | Make a deck · Speaker notes |
| **Mobile & motion** | Mobile prototype · Animated video · Sound effects |
| **Design systems** | Create design system · Use design system · Design system preview · Design Components (`.dc.html`) · Make tweakable |
| **Import sources** | Figma `.fig` (offline decode) · GitHub repo · Existing HTML/CSS |
| **Export & handoff** | Standalone HTML · PDF · PPTX (editable) · PPTX (screenshots) · Video (MP4) · Send to Figma · Send to Canva · Handoff to Claude Code |
| **AI assets & integration** | Gemini image generation · Call Claude from prototypes · Read PDF |

**Starter components** (in [`starter-components/`](skills/baoyu-design/starter-components/)) save the agent from hand‑rolling the basics: iOS / A