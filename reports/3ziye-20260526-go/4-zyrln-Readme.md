# Zyrln

[راهنمای فارسی](README_FA.md)

Bypass internet censorship in Iran. Routes your traffic through Google's infrastructure — no VPN fingerprint, no blocked IP, no dedicated server to block.

---

## Table of Contents

- [How It Works](#how-it-works)
- [I just want Google services (Gmail, Drive, Maps)](#i-just-want-google-services-gmail-drive-maps)
- [I want to access everything](#i-want-to-access-everything)
  - [What you need](#what-you-need)
  - [Step 1 — Run the desktop app](#step-1--run-the-desktop-app)
  - [Step 2 — Deploy the exit relay](#step-2--deploy-the-exit-relay)
  - [Step 3 — Deploy the Apps Script relay](#step-3--deploy-the-apps-script-relay)
  - [Step 4 — Connect](#step-4--connect)
  - [Step 5 — Set up Android](#step-5--set-up-android)
- [Building from Source](#building-from-source)
- [Troubleshooting](#troubleshooting)
- [Security Notes](#security-notes)
- [Credits](#credits)

---

## How It Works

Iran's censorship system (SNDPI) blocks sites by inspecting traffic. Zyrln defeats it two ways:

**For Google services (Gmail, Drive, Maps, etc.):**
Traffic is sent directly to Google but with the TLS handshake split into tiny fragments. The censor's system can't reassemble them fast enough to read the SNI, so it lets the connection through. No server needed.

**For everything else (Instagram, Twitter, etc.):**
Traffic is routed through Google Apps Script — a free Google service. From the censor's perspective it looks like normal Google traffic. Apps Script then forwards it to an exit relay (your VPS or Cloudflare) which fetches the real site.

---

## I just want Google services (Gmail, Drive, Maps)

**No server needed. No setup. Just download and enable.**

1. Download the app for your platform from the [Releases](../../releases) page
2. Run it — the GUI opens in your browser automatically
   - **Windows:** double-click the `.exe` — the GUI opens automatically
   - **Linux / macOS:** run from terminal with the `-gui` flag:
     ```bash
     # Linux
     ./zyrln-VERSION-linux-amd64 -gui
     # macOS Apple Silicon
     ./zyrln-VERSION-darwin-arm64 -gui
     # macOS Intel
     ./zyrln-VERSION-darwin-amd64 -gui
     ```
3. Click the **⚡ lightning bolt** button in the top bar to enable Direct Mode
4. Set your browser to use HTTP proxy `127.0.0.1:8085`

That's it. Many Google services can use the faster direct path when the local network allows it.

> Direct Mode works for Google services that are SNI-filtered but not IP-blocked — Gmail, Drive, Maps, Google Docs, and similar. YouTube video streaming and Play Store downloads go through the relay instead. Filtering behavior varies by ISP, city, carrier, and time.

---

## I want to access everything

To access Instagram, Twitter, Telegram, and other non-Google sites, you need to set up a relay chain. This takes about 15 minutes.

### What you need

| | What | Cost |
|---|---|---|
| ✅ Required | Google account | Free |
| ✅ Required | A shared auth key (you generate it) | Free |
| ☁️ Pick one | VPS with a public IP | ~$5/mo |
| ☁️ Or this | Cloudflare account | Free tier is enough |

### Step 1 — Run the desktop app

1. Download the binary for your OS from [Releases](../../releases)
2. Run it — the GUI opens automatically in your browser
   - **Windows:** double-click the `.exe` — the GUI opens automatically
   - **Linux / macOS:** run from terminal with the `-gui` flag:
     ```bash
     # Linux
     ./zyrln-VERSION-linux-amd64 -gui
     # macOS Apple Silicon
     ./zyrln-VERSION-darwin-arm64 -gui
     # macOS Intel
     ./zyrln-VERSION-darwin-amd64 -gui
     ```
3. Go to **Security** → generate and install the CA certificate (needed for HTTPS sites)
4. Go to **Settings** → click **Generate Key** and copy the auth key — you'll need it in the next steps

**Configure your browser:**

| Browser | Where to set it |
|---|---|
| Chrome / Edge | Settings → System → Open proxy settings → Manual proxy → `127.0.0.1:8085` |
| Firefox | Settings → Network → Manual proxy → HTTP `127.0.0.1` port `8085` |
| System-wide (all apps) | Use SOCKS5 `127.0.0.1:1080` in your OS network settings |

**Install the CA certificate** (required for HTTPS):

- **Chrome/Edge**: Settings → Privacy → Security → Manage certificates → Authorities → Import `zyrln-ca.pem`
- **Firefox**: Settings → Privacy & Security → Certificates → View Certificates → Authorities → Import

### Step 2 — Deploy the exit relay

This is the exit node that fetches real websites. Pick one option:

#### Option A — Cloudflare Worker (recommended, free)

1. Go to [dash.cloudflare.com](https://dash.cloudflare.com) → **Workers & Pages → Create**
2. Paste the contents of [`relay/cloudflare/worker.js`](relay/cloudflare/worker.js)
3. Click **Deploy** and copy the Worker URL:
   `https://your-worker.your-subdomain.workers.dev`

#### Option B — VPS

See **[docs/vps-setup.md](docs/vps-setup.md)** for full instructions.

Short version — on your VPS:
```bash
# Build locally and copy to server
GOOS=linux GOARCH=amd64 go b