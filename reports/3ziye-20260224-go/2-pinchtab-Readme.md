<p align="center">
  <img src="assets/pinchtab-headless.png" alt="pinchtab" width="200"/>
</p>

<p align="center">
  <strong>Browser control for AI agents.</strong><br/>
  12MB Go binary. Zero config. Accessibility-first.<br/><br/>
  🦀 <em>PINCH! PINCH!</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/lang-Go-00ADD8?style=flat-square" alt="Go"/>
  <img src="https://img.shields.io/badge/binary-12MB-FFD700?style=flat-square" alt="12MB"/>
  <img src="https://img.shields.io/badge/interface-HTTP-00ff88?style=flat-square" alt="HTTP"/>
  <img src="https://img.shields.io/badge/license-MIT-888?style=flat-square" alt="MIT"/>
</p>

---

## Why

Most agent browser tools (OpenClaw, Playwright MCP, Browser Use) are tightly coupled — they only work inside their own framework. If you switch agents or want to script something in bash, you're out of luck.

Pinchtab is a standalone HTTP server. Any agent, any language, even `curl`:

```bash
# Read a page — 800 tokens instead of 10,000
curl localhost:9867/text?tabId=X

# Click a button by ref from the last snapshot
curl -X POST localhost:9867/action -d '{"kind":"click","ref":"e5"}'
```

| | Pinchtab | OpenClaw Browser |
|---|---|---|
| **Tokens per page** | **~800** (`/text`) / ~3,600 (interactive) | ~10,000+ (full snapshot) |
| Interface | HTTP — any agent, any language | Internal only |
| A11y snapshots | ✅ | ✅ |
| Element interaction | ✅ | ✅ |
| Stealth mode | ✅ | ❌ |
| Session persistence | ✅ | ❌ |
| Self-contained binary | ✅ 12MB | ❌ |

- **5-13x cheaper** than screenshots or full snapshots for read-heavy tasks ([real measurements](#token-efficiency--real-numbers))
- **Plain HTTP API** — not locked to any agent framework
- **Self-contained** — 12MB binary, launches its own Chrome, zero config
- **Stealth mode** — bypasses bot detection on major sites
- **Persistent sessions** — log in once, stays logged in across restarts

## Quick Start

### Docker (easiest)

```bash
docker run -d -p 9867:9867 --security-opt seccomp=unconfined pinchtab/pinchtab
curl http://localhost:9867/health
```

### With your AI agent

> Install Pinchtab and set it up for browser automation.

Your agent can clone, build, and configure Pinchtab using the [OpenClaw skill](skill/pinchtab/SKILL.md). Just ask.

### Manual

```bash
# Build
go build -o pinchtab ./cmd/pinchtab

# Headless mode (default) — no window, pure automation (best for token-efficient API flows)
./pinchtab

# Headed mode — visible window for operator-in-the-loop flows
BRIDGE_HEADLESS=false ./pinchtab
```

### Run Modes

| Mode | Command | Notes |
|---|---|---|
| Headless (default) | `./pinchtab` | Launches managed Chrome without UI |
| Headed | `BRIDGE_HEADLESS=false ./pinchtab` | Launches managed Chrome with visible window |
| Dashboard / orchestrator | `./pinchtab dashboard` | Runs control plane only (profiles + instances), no browser in dashboard process |
| Remote CDP | `CDP_URL=http://localhost:9222 ./pinchtab` | Connects to an existing Chrome instead of launching one |

Common runtime options:

```bash
# Custom port
BRIDGE_PORT=9870 ./pinchtab

# Custom profile directory
BRIDGE_PROFILE=/path/to/profile ./pinchtab

# Enable API auth
BRIDGE_TOKEN=your-secret-token ./pinchtab
```

### Headless Mode

<img src="assets/pinchtab-headless.png" width="64" alt="Pinchtab" />

Chrome runs invisibly in the background — no window, pure API. Best for servers, CI, Docker, and unattended automation. Token savings come from using `/text` and filtered snapshot formats (`/snapshot?filter=interactive&format=compact`) rather than vision/screenshot-heavy flows.

```bash
./pinchtab
```

All core API flows are validated in headless mode.

### Remote Chrome via CDP_URL

Instead of launching your own Chrome, connect to an existing instance:

```bash
# Start Chrome with debugging enabled (localhost only)
chrome --remote-debugging-port=9222 &

# Get the WebSocket URL
CDP_URL=$(curl http://localhost:9222/json/version | jq -r '.webSocketDebuggerUrl')

# Connect Pinchtab to it
export CDP_URL
./pinchtab
```

**Use cases:**
- 🤝 **Multi-agent resource sharing** — All agents share one Chrome (save 1.3GB per agent)
- 🧪 **Integration testing** — Multiple test scripts use the same browser and session
- 🐳 **Docker/containers** — Chrome in one container, Pinchtab in another

**⚠️ Security:** Chrome's DevTools Protocol has no authentication. Only expose the CDP port locally or via SSH tunnel. See **[docs/cdp-url-shared-chrome.md#security](docs/cdp-url-shared-chrome.md#security)** for details.

See **[docs/cdp-url-shared-chrome.md](docs/cdp-url-shared-chrome.md)** for detailed setup and use cases.

### Headed Mode (operator-in-the-loop)

<img src="assets/pinchtab-headed.png" width="128" alt="Pinchtab headed mode" />

Headed mode is for mixed human + agent workflows:

- Human signs in, solves captchas/2FA, validates page state
- Agent continues through HTTP API against the same profile
- Team can watch automation behavior in real time

See **[docs/hea