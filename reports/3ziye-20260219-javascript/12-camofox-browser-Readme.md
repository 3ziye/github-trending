<div align="center">
  <img src="fox.png" alt="camofox-browser" width="200" />
  <h1>camofox-browser</h1>
  <p><strong>Anti-detection browser server for AI agents, powered by Camoufox</strong></p>
  <p>
    <a href="https://github.com/jo-inc/camofox-browser/actions"><img src="https://img.shields.io/badge/build-passing-brightgreen" alt="Build" /></a>
    <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/license-MIT-blue" alt="License" /></a>
    <a href="https://camoufox.com"><img src="https://img.shields.io/badge/engine-Camoufox-red" alt="Camoufox" /></a>
    <a href="https://hub.docker.com"><img src="https://img.shields.io/badge/docker-ready-blue" alt="Docker" /></a>
  </p>
  <p>
    Standing on the mighty shoulders of <a href="https://camoufox.com">Camoufox</a> - a Firefox fork with fingerprint spoofing at the C++ level.
    <br/><br/>
    The same engine behind <a href="https://askjo.ai">askjo.ai</a>'s web browsing.
  </p>
</div>

<br/>

---

## Why

AI agents need to browse the real web. Playwright gets blocked. Headless Chrome gets fingerprinted. Stealth plugins become the fingerprint.

Camoufox patches Firefox at the **C++ implementation level** - `navigator.hardwareConcurrency`, WebGL renderers, AudioContext, screen geometry, WebRTC - all spoofed before JavaScript ever sees them. No shims, no wrappers, no tells.

This project wraps that engine in a REST API built for agents: accessibility snapshots instead of bloated HTML, stable element refs for clicking, and search macros for common sites.

## Features

- **C++ Anti-Detection** - bypasses Google, Cloudflare, and most bot detection
- **Element Refs** - stable `e1`, `e2`, `e3` identifiers for reliable interaction
- **Token-Efficient** - accessibility snapshots are ~90% smaller than raw HTML
- **Runs on Anything** - lazy browser launch + idle shutdown keeps memory at ~40MB when idle. Designed to share a box with the rest of your stack — Raspberry Pi, $5 VPS, shared Railway infra.
- **Session Isolation** - separate cookies/storage per user
- **Cookie Import** - inject Netscape-format cookie files for authenticated browsing
- **Proxy + GeoIP** - route traffic through residential proxies with automatic locale/timezone
- **Structured Logging** - JSON log lines with request IDs for production observability
- **Search Macros** - `@google_search`, `@youtube_search`, `@amazon_search`, `@reddit_subreddit`, and 10 more
- **Deploy Anywhere** - Docker, Fly.io, Railway

## Quick Start

### OpenClaw Plugin

```bash
openclaw plugins install @askjo/camofox-browser
```

**Tools:** `camofox_create_tab` · `camofox_snapshot` · `camofox_click` · `camofox_type` · `camofox_navigate` · `camofox_scroll` · `camofox_screenshot` · `camofox_close_tab` · `camofox_list_tabs` · `camofox_import_cookies`

### Standalone

```bash
git clone https://github.com/jo-inc/camofox-browser
cd camofox-browser
npm install
npm start  # downloads Camoufox on first run (~300MB)
```

Default port is `9377`. See [Environment Variables](#environment-variables) for all options.

### Docker

```bash
docker build -t camofox-browser .
docker run -p 9377:9377 camofox-browser
```

### Fly.io / Railway

`fly.toml` and `railway.toml` are included. Deploy with `fly deploy` or connect the repo to Railway.

## Usage

### Cookie Import

Import cookies from your browser into Camoufox to skip interactive login on sites like LinkedIn, Amazon, etc.

#### Setup

**1. Generate a secret key:**

```bash
# macOS / Linux
openssl rand -hex 32
```

**2. Set the environment variable before starting OpenClaw:**

```bash
export CAMOFOX_API_KEY="your-generated-key"
openclaw start
```

The same key is used by both the plugin (to authenticate requests) and the server (to verify them). Both run from the same environment — set it once.

> **Why an env var?** The key is a secret. Plugin config in `openclaw.json` is stored in plaintext, so secrets don't belong there. Set `CAMOFOX_API_KEY` in your shell profile, systemd unit, Docker env, or Fly.io secrets.

> **Cookie import is disabled by default.** If `CAMOFOX_API_KEY` is not set, the server rejects all cookie requests with 403.

**3. Export cookies from your browser:**

Install a browser extension that exports Netscape-format cookie files (e.g., "cookies.txt" for Chrome/Firefox). Export the cookies for the site you want to authenticate.

**4. Place the cookie file:**

```bash
mkdir -p ~/.camofox/cookies
cp ~/Downloads/linkedin_cookies.txt ~/.camofox/cookies/linkedin.txt
```

The default directory is `~/.camofox/cookies/`. Override with `CAMOFOX_COOKIES_DIR`.

**5. Ask your agent to import them:**

> Import my LinkedIn cookies from linkedin.txt

The agent calls `camofox_import_cookies` → reads the file → POSTs to the server with the Bearer token → cookies are injected into the browser session. Subsequent `camofox_create_tab` calls to linkedin.com will be authenticated.

#### How it works

```
~/.camofox/cookies/linkedin.txt          (Netscape format,