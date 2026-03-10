<p align="center">
  <img src="assets/pinchtab-headless.png" alt="PinchTab" width="200"/>
</p>

<p align="center">
  <strong>PinchTab</strong><br/>
  <strong>Browser control for AI agents</strong><br/>
  12MB Go binary • HTTP API • Token-efficient
</p>


<table align="center">
  <tr>
    <td align="center" valign="middle">
      <a href="https://pinchtab.com/docs"><img src="assets/docs-no-background-256.png" alt="Full Documentation" width="92"/></a>
    </td>
    <td align="left" valign="middle">
      <a href="https://github.com/pinchtab/pinchtab/releases/latest"><img src="https://img.shields.io/github/v/release/pinchtab/pinchtab?style=flat-square&color=FFD700" alt="Release"/></a><br/>
      <a href="https://github.com/pinchtab/pinchtab/actions/workflows/go-verify.yml"><img src="https://img.shields.io/github/actions/workflow/status/pinchtab/pinchtab/go-verify.yml?branch=main&style=flat-square&label=Build" alt="Build"/></a><br/>
      <img src="https://img.shields.io/badge/Go-1.25+-00ADD8?style=flat-square&logo=go&logoColor=white" alt="Go 1.25+"/><br/>
      <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache%202.0-blue?style=flat-square" alt="License"/></a>
    </td>
  </tr>
</table>

---

## What is PinchTab?

PinchTab is a **standalone HTTP server** that gives AI agents direct control over Chrome.

It has two runtime roles:
- `pinchtab` or `pinchtab server` — the full control-plane server
- `pinchtab bridge` — a single-instance bridge runtime

Most users only need the full server. It manages profiles, instances, routing, and the web dashboard. The `bridge` mode is the thin per-instance runtime used behind the scenes for managed child instances.

### Process Model

PinchTab is server-first:
- start `pinchtab` for the full control plane
- let the server manage profiles and instances
- let each managed instance run behind a lightweight `pinchtab bridge` runtime

In practice:
- **Server** is the public product entrypoint
- **Bridge** is the per-instance runtime for one browser
- **Attach** is the advanced path for registering an externally managed Chrome

### Primary Usage

The primary user journey is:

1. install Pinchtab
2. run `pinchtab`
3. point your agent or tool at `http://localhost:9867`
4. let Pinchtab act as your local browser service

That is the default “replace the browser runtime” scenario.
Most users should not need to think about `pinchtab bridge` directly.

### Key Features

- **CLI or Curl** — Control via command-line or HTTP API
- **Token-efficient** — 800 tokens/page with text extraction (5-13x cheaper than screenshots)
- **Headless or Headed** — Run without a window or with visible Chrome
- **Multi-instance** — Run multiple parallel Chrome processes with isolated profiles
- **Self-contained** — 12MB binary, no external dependencies
- **Accessibility-first** — Stable element refs instead of fragile coordinates
- **ARM64-optimized** — First-class Raspberry Pi support with automatic Chromium detection

---

## Quick Start

### Installation

**macOS / Linux:**
```bash
curl -fsSL https://pinchtab.com/install.sh | bash
```

**npm:**
```bash
npm install -g pinchtab
```

**Docker:**
```bash
docker run -d -p 9867:9867 pinchtab/pinchtab
```

### Use It

**Terminal 1 — Start the server:**
```bash
pinchtab
```

**Terminal 2 — Control the browser:**
```bash
# Navigate
pinchtab nav https://pinchtab.com

# Get page structure
pinchtab snap -i -c

# Click an element
pinchtab click e5

# Extract text
pinchtab text
```

Or use the HTTP API directly:
```bash
# Create an instance (returns instance id)
INST=$(curl -s -X POST http://localhost:9867/instances/launch \
  -H "Content-Type: application/json" \
  -d '{"name":"work","mode":"headless"}' | jq -r '.id')

# Open a tab in that instance
TAB=$(curl -s -X POST http://localhost:9867/instances/$INST/tabs/open \
  -H "Content-Type: application/json" \
  -d '{"url":"https://pinchtab.com"}' | jq -r '.tabId')

# Get snapshot
curl "http://localhost:9867/tabs/$TAB/snapshot?filter=interactive"

# Click element
curl -X POST "http://localhost:9867/tabs/$TAB/action" \
  -H "Content-Type: application/json" \
  -d '{"kind":"click","ref":"e5"}'
```

---

## Core Concepts

**Server** — The main PinchTab process. It manages profiles, instances, routing, and the dashboard.

**Instance** — A running Chrome process. Each instance can have one profile.

**Profile** — Browser state (cookies, history, local storage). Log in once, stay logged in across restarts.

**Tab** — A single webpage. Each instance can have multiple tabs.

**Bridge** — The single-instance runtime behind a managed instance. Usually spawned by the server, not started manually.

Read more in the [Core Concepts](https://pinchtab.com/docs/core-concepts) guide.

---

## Why PinchTab?

| Aspect | PinchTab |
|--------|----------|
| **Tokens performance** | ✅ |
| **Headless and Headed** | ✅ |
| **Profile** | ✅ |
| **Stealth mode** | ✅ |
| **Persistent sessions** | ✅ |
| **Binary size** | ✅ |
| **Mul