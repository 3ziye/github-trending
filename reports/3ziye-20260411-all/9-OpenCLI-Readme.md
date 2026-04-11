# OpenCLI

> **Turn websites, browser sessions, Electron apps, and local tools into deterministic interfaces for humans and AI agents.**
> Reuse your logged-in browser, automate live workflows, and crystallize repeated actions into reusable CLI commands.

[![中文文档](https://img.shields.io/badge/docs-%E4%B8%AD%E6%96%87-0F766E?style=flat-square)](./README.zh-CN.md)
[![npm](https://img.shields.io/npm/v/@jackwener/opencli?style=flat-square)](https://www.npmjs.com/package/@jackwener/opencli)
[![Node.js Version](https://img.shields.io/node/v/@jackwener/opencli?style=flat-square)](https://nodejs.org)
[![License](https://img.shields.io/npm/l/@jackwener/opencli?style=flat-square)](./LICENSE)

OpenCLI gives you one surface for three different kinds of automation:

- **Use built-in adapters** for sites like Bilibili, Zhihu, Xiaohongshu, Reddit, HackerNews, Twitter/X, and [many more](#built-in-commands).
- **Drive a live browser directly** with `opencli browser` when an AI agent needs to click, type, extract, or inspect a page in real time.
- **Generate new adapters** from real browser behavior with `explore`, `synthesize`, `generate`, and `cascade`.

It also works as a **CLI hub** for local tools such as `gh`, `docker`, and other binaries you register yourself, plus **desktop app adapters** for Electron apps like Cursor, Codex, Antigravity, ChatGPT, and Notion.

## Why OpenCLI

---

## Highlights

- **CLI All Electron** — CLI-ify apps like Antigravity Ultra! Now AI can control itself natively.
- **Browser Automation** — `browser` gives AI agents direct browser control: click, type, extract, screenshot — any interaction, fully scriptable.
- **Website → CLI** — Turn any website into a deterministic CLI: 70+ pre-built adapters, or crystallize your own with `opencli record`.
- **Account-safe** — Reuses Chrome/Chromium logged-in state; your credentials never leave the browser.
- **Anti-detection built-in** — Patches `navigator.webdriver`, stubs `window.chrome`, fakes plugin lists, cleans ChromeDriver/Playwright globals, and strips CDP frames from Error stack traces. Extensive anti-fingerprinting and risk-control evasion measures baked in at every layer.
- **AI Agent ready** — `explore` discovers APIs, `synthesize` generates adapters, `cascade` finds auth strategies, `browser` controls the browser directly.
- **External CLI Hub** — Discover, auto-install, and passthrough commands to any external CLI (gh, obsidian, docker, etc). Zero setup.
- **Self-healing setup** — `opencli doctor` diagnoses and auto-starts the daemon, extension, and live browser connectivity.
- **Dynamic Loader** — Simply drop `.js` adapters into the `clis/` folder for auto-registration.
- **Zero LLM cost** — No tokens consumed at runtime. Run 10,000 times and pay nothing.
- **Deterministic** — Same command, same output schema, every time. Pipeable, scriptable, CI-friendly.
- **Broad coverage** — 87+ sites across global and Chinese platforms (Bilibili, Zhihu, Xiaohongshu, Reddit, HackerNews, and more), plus desktop Electron apps via CDP.

---

## Quick Start

### 1. Install OpenCLI

```bash
npm install -g @jackwener/opencli
```

### 2. Install the Browser Bridge Extension

OpenCLI connects to Chrome/Chromium through a lightweight Browser Bridge extension plus a small local daemon. The daemon auto-starts when needed.

1. Download the latest `opencli-extension.zip` from the GitHub [Releases page](https://github.com/jackwener/opencli/releases).
2. Unzip it, open `chrome://extensions`, and enable **Developer mode**.
3. Click **Load unpacked** and select the unzipped folder.

### 3. Verify the setup

```bash
opencli doctor
```

### 4. Run your first commands

```bash
opencli list
opencli hackernews top --limit 5
opencli bilibili hot --limit 5
```

## For Humans

Use OpenCLI directly when you want a reliable command instead of a live browser session:

- `opencli list` shows every registered command.
- `opencli <site> <command>` runs a built-in or generated adapter.
- `opencli register mycli` exposes a local CLI through the same discovery surface.
- `opencli doctor` helps diagnose browser connectivity.

## For AI Agents

Use two different entry points depending on the task:

- [`skills/opencli-explorer/SKILL.md`](./skills/opencli-explorer/SKILL.md): the entry point for creating new adapters — supports both fully automated generation (`opencli generate <url>`) and manual exploration workflows.
- [`skills/opencli-browser/SKILL.md`](./skills/opencli-browser/SKILL.md): the low-level control surface for live browsing, debugging, and manual intervention.

Install the packaged skills with:

```bash
npx skills add jackwener/opencli
```

Or install only what you need:

```bash
npx skills add jackwener/opencli --skill opencli-usage
npx skills add jackwener/opencli --skill opencli-browser
npx skills add jackwener/opencli --skill opencli-explorer
npx skills add jackwener/opencli --skill opencli-oneshot
```

In practice:

- start with `opencli-explorer` when the agent needs a 