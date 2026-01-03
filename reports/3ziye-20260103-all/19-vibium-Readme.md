# Vibium

**Browser automation without the drama.**

Vibium is browser automation infrastructure built for AI agents. A single binary handles browser lifecycle, [WebDriver BiDi](docs/explanation/webdriver-bidi.md) protocol, and exposes an MCP server — so Claude Code (or any MCP client) can drive a browser with zero setup. Works great for AI agents, test automation, and anything else that needs a browser.

**New here?** [Getting Started Tutorial](docs/tutorials/getting-started.md) — zero to hello world in 5 minutes.

---

## Why Vibium?

**Browser automation for AI agents and humans.**

- **AI-native.** MCP server built-in. Claude Code can drive a browser out of the box.
- **Zero config.** One install, browser downloads automatically, visible by default.
- **Sync API.** No async/await ceremony. Perfect for scripts, REPLs, and agents.
- **Standards-based.** Built on [WebDriver BiDi](docs/explanation/webdriver-bidi.md), not proprietary protocols controlled by large corporations.
- **Lightweight.** Single ~10MB binary. No runtime dependencies.

---

## Quick Reference

| Component | Purpose | Interface |
|-----------|---------|-----------|
| **Clicker** | Browser automation, BiDi proxy, MCP server | CLI / stdio / WebSocket :9515 |
| **JS Client** | Developer-facing API | npm package |
| **Python Client** | Developer-facing API | pip package |

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
│                       Client Libraries                       │
│           npm install vibium  ·  pip install vibium          │
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

### Python Client

```python
from vibium import browser, browser_sync
```

**Sync API:**
```python
from vibium import browser_sync as browser

vibe = browser.launch()
vibe.go("https://example.com")

png = vibe.screenshot()
with open("screenshot.png", "wb") as f:
    f.write(png)

link = vibe.find("a")
link.click()
vibe.quit()
```

**Async API:**
```python
import asyncio
from vibium import browser

async def main():
    vibe = await browser.launch()
    await vibe.go("h