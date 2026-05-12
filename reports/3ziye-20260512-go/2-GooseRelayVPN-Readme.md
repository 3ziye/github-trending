# GooseRelayVPN

[![GitHub](https://img.shields.io/badge/GitHub-GooseRelayVPN-blue?logo=github)](https://github.com/kianmhz/GooseRelayVPN)

**[🇮🇷 راهنمای فارسی (Persian)](README_FA.md)**

A SOCKS5 VPN that tunnels **raw TCP** through a Google Apps Script web app to your own small VPS exit server. To anything on the network path your client only ever talks TLS to a Google IP with `SNI=www.google.com`. Everything in flight is AES-256-GCM encrypted end-to-end — Google never sees plaintext and never holds the key.

> **How it works in simple terms:** Your browser/app talks SOCKS5 to this tool on your computer. The tool wraps every TCP byte in AES-GCM frames and posts them through a Google-facing HTTPS connection to a free Apps Script web app you control. The Apps Script forwards those bytes verbatim to your own VPS, which decrypts and opens the real connection. To the firewall/filter it looks like you're just talking to Google.

> ⚠️ **You need a small VPS for the exit server.** Unlike pure-Apps-Script proxies, this project tunnels raw TCP — anything SOCKS5 can carry — so a real `net.Dial` has to happen somewhere. A small $4/month VPS is plenty. In exchange you can tunnel SSH, IMAP, custom protocols, anything — not just HTTP.

## Support This Project

If you like this project, please consider starring it on GitHub (⭐). It helps the project get discovered.

You can also support the project financially:

- TRX / USDT TRC20:
  `TSxg2WAXYnkoR2UiUTzCxbmqNARAt91aqB`
- BNB / USDT BEP20:
  `0xe7b48d8fd5fbbb4e3fa9a06723a62a88585139ea`
- TON:
  `UQDBzJqzJ5e7uZFPrmarTRSGGbD1UoFK2q5_jWh4D2nnNdUB`

## Important Notes

- Never share `tunnel_key` with anyone. Anyone with this key can use your tunnel/VPS as if they are you.
- A server with public internet access is required. Your exit server must be reachable from Google Apps Script.
- Each Google Apps Script deployment ID has a quota of about 20,000 executions per day, and the quota resets around 10:30 AM Iran time (GMT+3:30).
- You do not need to install a local MITM certificate in this project. The certificate setup in `MasterHttpRelayVPN` is for that project's architecture and is not required here.
- This project was inspired by the idea in the main repository: https://github.com/masterking32/MasterHttpRelayVPN

---

## Disclaimer

GooseRelayVPN is provided for educational, testing, and research purposes only.

- **Provided without warranty:** This software is provided "AS IS", without express or implied warranty, including merchantability, fitness for a particular purpose, and non-infringement.
- **Limitation of liability:** The developers and contributors are not responsible for any direct, indirect, incidental, consequential, or other damages resulting from the use of this project.
- **User responsibility:** Running this project outside controlled test environments may affect networks, accounts, or connected systems. You are solely responsible for installation, configuration, and use.
- **Legal compliance:** You are responsible for complying with all local, national, and international laws and regulations before using this software.
- **Google services compliance:** If you use Google Apps Script with this project, you are responsible for complying with Google's Terms of Service, acceptable-use rules, quotas, and platform policies. Misuse may lead to suspension of your Google account or deployment.
- **License terms:** Use, copying, distribution, and modification are governed by the repository license. Any use outside those terms is prohibited.

---

## How It Works

```
Browser/App
  -> SOCKS5  (127.0.0.1:1080)
  -> Zstd-compressed + AES-256-GCM frame batches
  -> HTTPS to a Google edge IP   (SNI=www.google.com, Host=script.google.com)
  -> Apps Script doPost()        (dumb forwarder, never sees plaintext)
  -> Your VPS :8443/tunnel       (decrypts, demuxes by session_id, dials target)
  <- Same path in reverse via long-polling
```

Your application sends TCP bytes through the SOCKS5 listener on your computer. The client groups them into batches of frames, **Zstandard-compresses** each batch (for compressible traffic such as plain HTTP or JSON APIs this reduces the body size by up to 65%, keeping you further from Apps Script's daily quota limits), then seals the whole batch under a single **AES-256-GCM** envelope and POSTs it over a domain-fronted HTTPS connection to your Apps Script web app. The Apps Script is a ~30-line script that forwards the body verbatim to your VPS — it never decrypts and the AES key never touches Google. Your VPS decrypts, dials the real target, and pumps bytes back along the same path. The filter sees only TLS to Google.

---

## Step-by-Step Setup Guide

### Step 1: Get an VPS

You need a Linux VPS with a public IP. Any provider works.

### Step 2: Get the binaries

You need two separate programs:
- **`goose-client`** — runs on **your own computer**. This is what you run every day.
- **`goose-server`** — runs on **your VPS**. You set it up onc