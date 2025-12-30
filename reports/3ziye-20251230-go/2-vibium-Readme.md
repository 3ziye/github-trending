# Vibium

**Browser automation without the drama.**

Vibium is browser automation infrastructure built for AI agents. A single binary handles browser lifecycle, WebDriver BiDi protocol, and exposes an MCP server — so Claude Code (or any MCP client) can drive a browser with zero setup. Works great for AI agents, test automation, and anything else that needs a browser.

**New here?** [Getting Started Tutorial](docs/tutorials/getting-started.md) — zero to hello world in 5 minutes.

---

## Quick Reference

| Component | Purpose | Interface |
|-----------|---------|-----------|
| **Clicker** | Browser automation, BiDi proxy, MCP server | CLI / stdio / WebSocket :9515 |
| **JS Client** | Developer-facing API | npm package |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                         LLM / Agent                         │
│          (Claude Code, Codex, Gemini, Local Models)         │
└─────────────────────────────────────────────────────────────┘
                      ▲
                      │ MCP Protocol (stdio)
                      ▼
           ┌─────────────────────┐         
           │   Vibium Clicker    │
           │                     │
           │  ┌───────────────┐  │
           │  │  MCP Server   │  │
           │  └───────▲───────┘  │         ┌──────────────────┐
           │          │          │         │                  │
           │  ┌───────▼───────┐  │WebSocket│                  │
           │  │  BiDi Proxy   │  │◄───────►│  Chrome Browser  │
           │  └───────────────┘  │  BiDi   │                  │
           │                     │         │                  │
           └─────────────────────┘         └──────────────────┘
                      ▲
                      │ WebSocket BiDi :9515
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                        JS/TS Client                         │
│                     npm install vibium                      │
│                                                             │
│    ┌─────────────────┐               ┌─────────────────┐    │
│    │ Async API       │               │    Sync API     │    │
│    │ await vibe.go() │               │    vibe.go()    │    │
│    │                 │               │                 │    │
│    └─────────────────┘               └─────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

---

## Components

### Clicker

A single Go binary (~10MB) that does everything:

- **Browser Management:** Detects/launches Chrome with BiDi enabled
- **BiDi Proxy:** WebSocket server that routes commands to browser
- **MCP Server:** stdio interface for LLM agents
- **Auto-Wait:** Polls for elements before interacting
- **Screenshots:** Viewport capture as PNG

**Design goal:** The binary is invisible. JS developers just `npm install vibium` and it works.

### JS/TS Client

```javascript
// Option 1: require (REPL-friendly)
const { browserSync } = require('vibium')

// Option 2: dynamic import (REPL with --experimental-repl-await)
const { browser } = await import('vibium')

// Option 3: static import (in .mjs or .ts files)
import { browser, browserSync } from 'vibium'
```

**Sync API:**
```javascript
const fs = require('fs')
const { browserSync } = require('vibium')

const vibe = browserSync.launch()
vibe.go('https://example.com')

const png = vibe.screenshot()
fs.writeFileSync('screenshot.png', png)

const link = vibe.find('a')
link.click()
vibe.quit()
```

**Async API:**
```javascript
const fs = await import('fs/promises')
const { browser } = await import('vibium')

const vibe = await browser.launch()
await vibe.go('https://example.com')

const png = await vibe.screenshot()
await fs.writeFile('screenshot.png', png)

const link = await vibe.find('a')
await link.click()
await vibe.quit()
```

---

## For Agents

One command to add browser control to Claude Code:

```bash
claude mcp add vibium -- npx -y vibium
```

That's it. No manual steps needed. Chrome downloads automatically during setup.

| Tool | Description |
|------|-------------|
| `browser_launch` | Start browser (visible by default) |
| `browser_navigate` | Go to URL |
| `browser_find` | Find element by CSS selector |
| `browser_click` | Click an element |
| `browser_type` | Type text into an element |
| `browser_screenshot` | Capture viewport (base64 or save to file with `--screenshot-dir`) |
| `browser_quit` | Close browser |

---

## For Humans

```bash
npm install vibium
```

This automatically:
1. Installs the Clicker binary for your platform
2. Downloads Chrome for Testing + chromedriver to platform cache:
   - Linux: `~/.cache/vibium/`
   - macOS: `~/Library/Caches/vibium/`
   - Windows: `%LOCALAPPDATA%\vibium\`

No manual browser setup required.

**Skip browser download** (if you manage browsers separately):
```bash
VIBIUM_SKIP_BROWSER_DOWNLOAD=1 npm install vibium
```

---

## Platform Support

| Platform | A