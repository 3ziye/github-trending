# OpenCLI

> **Make any website, Electron App, or Local Tool your CLI.**
> Zero risk · Reuse Chrome/Chromium login · AI-powered discovery · Universal CLI Hub

[![中文文档](https://img.shields.io/badge/docs-%E4%B8%AD%E6%96%87-0F766E?style=flat-square)](./README.zh-CN.md)
[![npm](https://img.shields.io/npm/v/@jackwener/opencli?style=flat-square)](https://www.npmjs.com/package/@jackwener/opencli)
[![Node.js Version](https://img.shields.io/node/v/@jackwener/opencli?style=flat-square)](https://nodejs.org)
[![License](https://img.shields.io/npm/l/@jackwener/opencli?style=flat-square)](./LICENSE)

A CLI tool that turns **any website**, **Electron app**, or **local CLI tool** into a command-line interface — Bilibili, Zhihu, 小红书, Twitter/X, Reddit, YouTube, Antigravity, `gh`, `docker`, and [many more](#built-in-commands) — powered by browser session reuse and AI-native discovery.

**Built for AI Agents** — Load the [`opencli-operate` skill](./skills/opencli-operate/SKILL.md) to give any AI agent (Claude Code, Cursor) direct browser control. Operate any website, then crystallize those interactions into reusable CLI commands. Configure `opencli list` in your `AGENT.md` or `.cursorrules` so the AI auto-discovers all available tools.

**CLI Hub** — Register any local CLI (`opencli register mycli`) so AI agents can discover and call it alongside built-in commands. Auto-installs missing tools via your package manager (e.g. if `gh` isn't installed, `opencli gh ...` runs `brew install gh` first then re-executes seamlessly).

**CLI for Electron Apps** — Turn any Electron application into a CLI tool. Recombine, script, and extend apps like Antigravity Ultra from the terminal. AI agents can now control other AI apps natively.

---

## Highlights

- **CLI All Electron** — CLI-ify apps like Antigravity Ultra! Now AI can control itself natively.
- **Browser Automation** — `operate` gives AI agents direct browser control: click, type, extract, screenshot — any interaction, fully scriptable.
- **Website → CLI** — Turn any website into a deterministic CLI: 70+ pre-built adapters, or crystallize your own with `opencli record`.
- **Account-safe** — Reuses Chrome/Chromium logged-in state; your credentials never leave the browser.
- **Anti-detection built-in** — Patches `navigator.webdriver`, stubs `window.chrome`, fakes plugin lists, cleans ChromeDriver/Playwright globals, and strips CDP frames from Error stack traces. Extensive anti-fingerprinting and risk-control evasion measures baked in at every layer.
- **AI Agent ready** — `explore` discovers APIs, `synthesize` generates adapters, `cascade` finds auth strategies, `operate` controls the browser directly.
- **External CLI Hub** — Discover, auto-install, and passthrough commands to any external CLI (gh, obsidian, docker, etc). Zero setup.
- **Self-healing setup** — `opencli doctor` diagnoses and auto-starts the daemon, extension, and live browser connectivity.
- **Dynamic Loader** — Simply drop `.ts` or `.yaml` adapters into the `clis/` folder for auto-registration.
- **Zero LLM cost** — No tokens consumed at runtime. Run 10,000 times and pay nothing.
- **Deterministic** — Same command, same output schema, every time. Pipeable, scriptable, CI-friendly.
- **Broad coverage** — 73+ sites across global and Chinese platforms (Bilibili, Zhihu, Xiaohongshu, Reddit, HackerNews, and more), plus desktop Electron apps via CDP.

---

## Quick Start

### 1. Install Browser Bridge Extension

> OpenCLI connects to your browser through a lightweight **Browser Bridge** Chrome/Chromium extension + micro-daemon (zero config, auto-start).

1. Go to the GitHub [Releases page](https://github.com/jackwener/opencli/releases) and download the latest `opencli-extension.zip`.
2. Unzip the file and open `chrome://extensions`, enable **Developer mode** (top-right toggle).
3. Click **Load unpacked** and select the unzipped folder.

### 2. Install OpenCLI

**Install via npm (recommended)**

```bash
npm install -g @jackwener/opencli
```

### 3. Verify & Try

```bash
opencli doctor          # Check extension + daemon connectivity
opencli daemon status   # Check daemon state (PID, uptime, memory)
```

**Try it out:**

```bash
opencli list                           # See all commands
opencli hackernews top --limit 5       # Public API, no browser needed
opencli bilibili hot --limit 5         # Browser command (requires Extension)
```

### 4. Browser Automation — Make Websites Accessible for AI Agents

Point your AI agent (Claude Code, Cursor) to [`skills/opencli-operate/SKILL.md`](./skills/opencli-operate/SKILL.md). It has everything needed — full command reference, examples, and workflow.

Available commands: `open`, `state`, `click`, `type`, `select`, `keys`, `wait`, `get`, `screenshot`, `scroll`, `back`, `eval`, `network`, `init`, `verify`, `close`.

### Update

```bash
npm install -g @jackwener/opencli@latest
```

### Install AI Skills

OpenCLI provides [skills](./skills/) for AI agents (Claude Code, etc.):

```bash
