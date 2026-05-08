# mhrv-rs — bypass censorship for free, with your own Google account

[![Latest release](https://img.shields.io/github/v/release/therealaleph/MasterHttpRelayVPN-RUST?display_name=tag&logo=github&label=release&color=blue&cacheSeconds=300)](https://github.com/therealaleph/MasterHttpRelayVPN-RUST/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/therealaleph/MasterHttpRelayVPN-RUST/total.svg?label=downloads&logo=github&cacheSeconds=300)](https://github.com/therealaleph/MasterHttpRelayVPN-RUST/releases)
[![CI](https://github.com/therealaleph/MasterHttpRelayVPN-RUST/actions/workflows/release.yml/badge.svg)](https://github.com/therealaleph/MasterHttpRelayVPN-RUST/actions/workflows/release.yml)
[![License: MIT](https://img.shields.io/github/license/therealaleph/MasterHttpRelayVPN-RUST?color=blue)](LICENSE)
[![Stars](https://img.shields.io/github/stars/therealaleph/MasterHttpRelayVPN-RUST?style=flat&logo=github)](https://github.com/therealaleph/MasterHttpRelayVPN-RUST/stargazers)
[![Support](https://img.shields.io/badge/❤️_Support-sh1n.org-red?style=flat)](https://sh1n.org/donate)

**A small program that runs on your computer and lets you visit blocked websites for free, using a Google Apps Script you deploy in your own free Google account. Your ISP only sees encrypted traffic to `www.google.com` — it can't tell what you're really visiting.**

🇬🇧 [English Quick Start](#quick-start) · [Full Guide (advanced topics)](docs/guide.md)
🇮🇷 [راه‌اندازی سریع فارسی](#راه‌اندازی-سریع) · [راهنمای کامل (مباحث پیشرفته)](docs/guide.fa.md)

<p align="center" dir="rtl">
  ۱. <a href="https://www.youtube.com/watch?v=voCwxgvWR5U" target="_blank" rel="noopener noreferrer">راهنمای تصویری راه اندازی به زبان فارسی</a> (YouTube)
  <br>
  ۲. <a href="https://kian-irani.github.io/mhrv-setup-full-tunell/" target="_blank" rel="noopener noreferrer">راهنمای جامع متنی راه اندازی به زبان فارسی</a> با تشکر از <a href="https://github.com/KIAN-IRANi" target="_blank" rel="noopener noreferrer">Kian Irani</a>
</p>

---

## What you get

- 🌐 **Bypasses DPI / SNI blocking** by using Google's edge as a relay
- 💯 **Completely free** — runs on your own Google account's free tier
- ⚡ **One small file** (~3 MB), no Python, no Node.js, no dependencies
- 🖥️ **Works on** Mac, Windows, Linux, Android, OpenWRT routers
- 🦊 **Any browser or app** that supports HTTP proxy or SOCKS5

## How it works (the simple picture)

```
   you  →  browser  →  mhrv-rs  ──┐
                                  │ ISP only sees:  www.google.com
                                  ▼
                          Google's network
                                  │
                                  ▼
              your free Apps Script  fetches  the real site
                                  │
                                  ▼
                Twitter / ChatGPT / blocked-site of your choice
```

ISPs can't read inside encrypted HTTPS. They only see the address — `www.google.com`. The actual page lookup happens inside Google's network, hidden in the encrypted tunnel.

## Quick Start

**About 5 minutes.** You need:

- A free Google account (any Gmail works)
- A computer (Mac, Windows, or Linux)
- Firefox or Chrome

### Step 1 — Make the Google Apps Script (one-time)

1. Go to **[script.google.com](https://script.google.com)**, sign in with your Google account
2. Click **New project** at the top left
3. Delete the default code in the editor
4. Open the file [`assets/apps_script/Code.gs`](assets/apps_script/Code.gs) in this repo, copy all of it, paste into the Apps Script editor (replacing what was there)
5. Find this line near the top:
   ```js
   const AUTH_KEY = "CHANGE_ME_TO_A_STRONG_SECRET";
   ```
   Change `CHANGE_ME_TO_A_STRONG_SECRET` to a long random string of your own. **Keep this string** — you'll paste it into the app in Step 3. Treat it like a password.
6. Click 💾 **Save** (or `Ctrl/Cmd+S`)
7. Click **Deploy** (top right) → **New deployment**
8. Click the gear icon ⚙ next to "Select type" → choose **Web app**
9. Set:
   - **Execute as:** *Me* (your Google account)
   - **Who has access:** *Anyone*
10. Click **Deploy**. Google may ask for permissions — click **Authorize access** and approve
11. Google shows a **Deployment ID** (a long random string). **Copy it** — you'll need it in Step 3.

> **Tip:** if you ever update `Code.gs` later, don't make a new deployment. Edit the code, then go to **Deploy → Manage deployments → ✏️ → Version: New version → Deploy**. The Deployment ID stays the same.

### Step 2 — Download mhrv-rs

Go to the [latest release page](https://github.com/therealaleph/MasterHttpRelayVPN-RUST/releases/latest) and download the file for your computer:

| You're on | Download this |
|---|---|
| Mac with Apple Silicon (M1 / M2 / M3 / M4 chip) | `mhrv-rs-macos-arm64-app.zip` |
| Mac with Intel chip | `mhrv-rs-macos-amd64-app.zip` |
| Windows | `mhrv-rs-windows-amd64.zip` |
| Linux (Ubuntu / Mint / Fedora / Debian / Arch) | `mhrv-rs-linux-amd64.tar.gz`