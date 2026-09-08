# freebuff-proxy: No ads, no CLI, just /v1/chat/completions

[![CI](https://img.shields.io/github/actions/workflow/status/trefeon/freebuff-proxy/ci.yml)](https://github.com/trefeon/freebuff-proxy/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/trefeon/freebuff-proxy)](https://github.com/trefeon/freebuff-proxy/releases)
[![License](https://img.shields.io/github/license/trefeon/freebuff-proxy)](https://github.com/trefeon/freebuff-proxy/blob/main/LICENSE)

`freebuff-proxy` is a local gateway that makes the AI coding models behind Codebuff/FreeBuff available to **any** tool that speaks the OpenAI API: OpenCode, pi, 9router, LiteLLM, or your own scripts.

Your coding tools expect an OpenAI-style endpoint (`/v1/chat/completions`). The upstream service is not OpenAI-shaped: it is a CLI coding agent with its own session protocol, and its free-tier access is tied to per-account tokens that carry individual daily quotas and can be rate-limited or banned. `freebuff-proxy` sits between the two and absorbs that friction:

- **Translates**: rewrites standard OpenAI requests into the upstream session protocol (CLI request envelope, model-bound agent runs, tool-schema normalization) and streams the SSE response back as OpenAI `chat.completion.chunk` events.
- **Pools**: routes requests across multiple tokens (hot-session-first with round-robin start and failover), so a busy client or router rides out per-account quotas instead of failing.
- **Stealths**: makes egress look like a real browser (TLS fingerprints, header sanitization, request jitter) so upstream abuse detection is less likely to flag your account (see the ToS warning below).

> **⚠️ Terms-of-service risk.** Using your FreeBuff token through this proxy conflicts with FreeBuff/Codebuff terms of service; upstream abuse detection can suspend or permanently ban accounts. Use `SAFE_MODE=true`, keep usage modest, and do not run unattended 24/7. See [Getting Started](docs/getting-started.md).

> **⚠️ Honest expectations.** FreeBuff's servers are strict, and this proxy **reduces** ban risk; it does not eliminate it. Nothing here can guarantee your account is never flagged or banned. Upstream detection is documented in the open-source FreeBuff client: per-request IP scoring (VPN/proxy/Tor/hosting egress → limited tier or terminal `country_blocked`), per-account trust levels with sticky caps (third-party-client flag, shared signup network, shared mailbox), daily spend ceilings ($0.50/day for restricted cohorts), and mass sweeps against known farm shapes (6,699 of 7,129 disposable-email accounts were already banned when the blocklist was compiled). This project is a local adapter that exposes FreeBuff's models as an OpenAI-compatible API for other coding agents (OpenCode, pi, hermes, openclaw, or any client that supports a custom endpoint). Your auth tokens are handled automatically by the gateway, which reimplements the official CLI's wire protocol (~99% parity); it is not the official client, and upstream changes can break it until adapted. Keep usage modest and follow the hygiene rules below; further improvements to session handling and ban avoidance are planned.

---

## Table of Contents

- [New here? Start here](#new-here-start-here)
- [Requirements](#requirements)
- [Features](#features)
- [How It Works](#how-it-works)
- [Key Concepts](#key-concepts)
- [Quick Start](#quick-start)
- [Command-Line Interface](#command-line-interface)
- [Configuration Reference](#configuration-reference)
- [Deployment](#deployment)
- [Guides](#guides)
- [Contributing & Security](#contributing--security)
- [Contact & Support](#contact--support)
- [License](#license)

---

## New here? Start here (30-Second Quick Start)

Freebuff-proxy makes the free AI models behind the FreeBuff/Codebuff CLI available to any OpenAI-compatible tool (Cursor, VS Code Continue/Cline, OpenCode, pi, 9router, Chatbox, LibreChat).

If you are a beginner, you don't need to write code or compile anything:

1. **Download the pre-built Release**: Go to [**Releases**](https://github.com/trefeon/freebuff-proxy/releases) and download the ZIP for your OS (e.g. `freebuff-proxy_..._windows_amd64.zip`). *(Do not use the green "Code -> Download ZIP" button, which is raw source code)*.
2. **Extract & Double-Click**: Unzip the folder.
   - **Windows**: Double-click `start-proxy.cmd`.
   - **Linux / macOS**: Open terminal in the extracted folder and run `./start-proxy.sh`.
3. **Log in**: When prompted, press Enter to open your browser and sign in with your FreeBuff/GitHub account. Your token is saved automatically!
4. **Open Web Dashboard**: Open [**http://localhost:3457/admin**](http://localhost:3457/admin) in your browser to view your live status, test chat, and manage tokens visually.
5. **Connect your tool**: In Cursor, VS Code Continue/Cline, Chatbox, or OpenCode, set:
   - **Base URL**: `http://localhost:3457/v1`
   - **API Key**: `not-needed`
   - **Model**: `deepseek/deepseek-v4-flash` (f