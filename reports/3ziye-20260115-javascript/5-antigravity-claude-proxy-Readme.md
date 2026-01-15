# Antigravity Claude Proxy

[![npm version](https://img.shields.io/npm/v/antigravity-claude-proxy.svg)](https://www.npmjs.com/package/antigravity-claude-proxy)
[![npm downloads](https://img.shields.io/npm/dm/antigravity-claude-proxy.svg)](https://www.npmjs.com/package/antigravity-claude-proxy)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<a href="https://buymeacoffee.com/badrinarayanans" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" height="50"></a>

A proxy server that exposes an **Anthropic-compatible API** backed by **Antigravity's Cloud Code**, letting you use Claude and Gemini models with **Claude Code CLI**.

![Antigravity Claude Proxy Banner](images/banner.png)

## How It Works

```
┌──────────────────┐     ┌─────────────────────┐     ┌────────────────────────────┐
│   Claude Code    │────▶│  This Proxy Server  │────▶│  Antigravity Cloud Code    │
│   (Anthropic     │     │  (Anthropic → Google│     │  (daily-cloudcode-pa.      │
│    API format)   │     │   Generative AI)    │     │   sandbox.googleapis.com)  │
└──────────────────┘     └─────────────────────┘     └────────────────────────────┘
```

1. Receives requests in **Anthropic Messages API format**
2. Uses OAuth tokens from added Google accounts (or Antigravity's local database)
3. Transforms to **Google Generative AI format** with Cloud Code wrapping
4. Sends to Antigravity's Cloud Code API
5. Converts responses back to **Anthropic format** with full thinking/streaming support

## Prerequisites

- **Node.js** 18 or later
- **Antigravity** installed (for single-account mode) OR Google account(s) for multi-account mode

---

## Installation

### Option 1: npm (Recommended)

```bash
# Run directly with npx (no install needed)
npx antigravity-claude-proxy@latest start

# Or install globally
npm install -g antigravity-claude-proxy@latest
antigravity-claude-proxy start
```

### Option 2: Clone Repository

```bash
git clone https://github.com/badri-s2001/antigravity-claude-proxy.git
cd antigravity-claude-proxy
npm install
npm start
```

---

## Quick Start

### 1. Start the Proxy Server

```bash
# If installed via npm
antigravity-claude-proxy start

# If using npx
npx antigravity-claude-proxy@latest start

# If cloned locally
npm start
```

The server runs on `http://localhost:8080` by default.

### 2. Link Account(s)

Choose one of the following methods to authorize the proxy:

#### **Method A: Web Dashboard (Recommended)**

1. With the proxy running, open `http://localhost:8080` in your browser.
2. Navigate to the **Accounts** tab and click **Add Account**.
3. Complete the Google OAuth authorization in the popup window.

#### **Method B: CLI (Desktop or Headless)**

If you prefer the terminal or are on a remote server:

```bash
# Desktop (opens browser)
antigravity-claude-proxy accounts add

# Headless (Docker/SSH)
antigravity-claude-proxy accounts add --no-browser
```

> For full CLI account management options, run `antigravity-claude-proxy accounts --help`.

#### **Method C: Automatic (Antigravity Users)**

If you have the **Antigravity** app installed and logged in, the proxy will automatically detect your local session. No additional setup is required.

To use a custom port:

```bash
PORT=3001 antigravity-claude-proxy start
```

### 3. Verify It's Working

```bash
# Health check
curl http://localhost:8080/health

# Check account status and quota limits
curl "http://localhost:8080/account-limits?format=table"
```

---

## Using with Claude Code CLI

### Configure Claude Code

You can configure these settings in two ways:

#### **Via Web Console (Recommended)**

1. Open the WebUI at `http://localhost:8080`.
2. Go to **Settings** → **Claude CLI**.
3. Select your preferred models and click **Apply to Claude CLI**.

> [!TIP] > **Configuration Precedence**: System environment variables (set in shell profile like `.zshrc`) take precedence over the `settings.json` file. If you use the Web Console to manage settings, ensure you haven't manually exported conflicting variables in your terminal.

#### **Manual Configuration**

Create or edit the Claude Code settings file:

**macOS:** `~/.claude/settings.json`
**Linux:** `~/.claude/settings.json`
**Windows:** `%USERPROFILE%\.claude\settings.json`

Add this configuration:

```json
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "test",
    "ANTHROPIC_BASE_URL": "http://localhost:8080",
    "ANTHROPIC_MODEL": "claude-opus-4-5-thinking",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "claude-opus-4-5-thinking",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "claude-sonnet-4-5-thinking",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "gemini-2.5-flash-lite[1m]",
    "CLAUDE_CODE_SUBAGENT_MODEL": "claude-sonnet-4-5-thinking",
    "ENABLE_EXPERIMENTAL_MCP_CLI": "true"
  }
}
```

(Please use **gemini-2.5-flash-lite** as the default haiku model, even if others are claude, as claude code makes several calls via the haiku model