<a id="top"></a>
<div align="center">

<img src="docs/banner.svg" alt="V2RayEz — DPI Bypass & CDN Toolkit" width="100%">

<br>

[![Version](https://img.shields.io/badge/version-4.7.5-2dd4bf?style=for-the-badge)](#)
[![Go](https://img.shields.io/badge/Go-1.22+-00ADD8?style=for-the-badge&logo=go&logoColor=white)](https://go.dev)
[![Platform](https://img.shields.io/badge/Windows%20·%20macOS%20·%20Linux-1c2330?style=for-the-badge)](#)
[![Telegram](https://img.shields.io/badge/@EzAccess1-229ED9?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/EzAccess1)

**A single-binary local web panel to beat DPI filtering and work with CDN-fronted proxies.**

**🌐 Language / زبان —** [**English**](#english) · [**فارسی**](#persian)

</div>

> [!WARNING]
> **For education, testing, and research only.** You are responsible for obeying your
> local laws and the terms of any service you use it with (Google, Cloudflare, …).
> Provided **as is**, with no warranty.

---

<a id="english"></a>

## 🇬🇧 English

V2RayEz is a **single-binary local web control panel**. You run one executable, a clean
dashboard opens in your browser (or its own app window), and *everything* — an
SNI-spoofing tunnel, xray/sing-box engines, scanners, a config library, a
Google-fronted relay, and a client-side **domain-fronting** proxy — lives behind that one
page. No installer, no hidden services, no telemetry. It's Go with an embedded UI, so the
whole app is one portable file.

<div align="center">
<img src="docs/screenshots/dashboard2.png" alt="V2RayEz dashboard" width="92%">
</div>

### ✨ Features

| | Feature | What it does |
|---|---|---|
| ≋ | **SNI Tunnel** | Local TCP proxy that does the TLS handshake with a *fake* SNI while connecting to the real endpoint, with optional DPI-desync (fragmentation, fake packets, uTLS fingerprints). |
| ⚙ | **XRay Core** | Detect/download **xray** & **sing-box**; run any config as a local **SOCKS5** proxy or a system-wide **TUN VPN**. Start/stop, flip TUN, and **Set/Clear the system proxy** from the header. |
| ◉ | **Domain Fronting** | Fully client-side domain fronting — a local MITM proxy reads each request's real Host and reaches the site's CDN edge behind an allowed front SNI. Editable host→front rules, **fronted DoH** resolution (bypasses poisoned DNS) with Cloudflare/Google/Quad9 presets, Set/Clear system proxy, direct pass-through for unmatched hosts, and live request/error logging. |
| ☷ | **Config Library** | Groups, subscriptions, the built-in SNI/Spoof list, paste & drag-drop, a **full structured v2ray editor**, QR sharing, **bulk relay + speed tests**, right-click menu, shift/multi-select — all auto-saved. |
| ◎ | **Scanners** | SNI scan, Mass SNI, **Clean IP Scanner**, CDN Edge test, CDN Configs builder, **Mass URI** tester, and a rebuilt **Site Scanner** (live progress, Cloudflare-first, Connect/Save). |
| ◈ | **Google Tunnel (Fastly)** | Domain-fronted relay through a **Google Apps Script** + **Cloudflare Worker** you deploy. Both scripts are generated in-app — no external repo involved. |
| ☁ | **Extras** | Cloudflare Worker maker, WinDivert management, Psiphon & SPlus tunnels. |
| 🎨 | **Modern UI** | Light & dark themes, readable fonts, fully fluid layout (phone → ultra-wide), collapsible log console, English & Persian. |

### 🚀 Quick start

```bash
# run a release build
./v2rayez            # Linux / macOS
v2rayez.exe          # Windows
```

Listens on `0.0.0.0:8765` by default and opens the dashboard. If it doesn't, visit
**http://127.0.0.1:8765**.

<details>
<summary><b>Build from source</b> (Go 1.22+)</summary>

```bash
git clone <your-fork-url> v2rayez
cd v2rayez
go build -o v2rayez .
./v2rayez

# cross-compile
GOOS=windows GOARCH=amd64 go build -o v2rayez.exe .
GOOS=darwin  GOARCH=arm64 go build -o v2rayez-mac .
GOOS=linux   GOARCH=amd64 go build -o v2rayez .

# optional transports behind build tags — flags go BEFORE the dot:
go build -tags "psiphon livekit" .        # correct
# go build . -tags psiphon                 # WRONG: "malformed import path -tags"
# tagged builds fetch deps first:
#   go get github.com/Psiphon-Labs/psiphon-tunnel-core/ClientLibrary/clientlib@latest
#   go get github.com/livekit/server-sdk-go/v2@latest
```

**Build every platform at once** (output in `dist/`, Windows `.exe` gets the app icon):

```bash
build-all.bat              # Windows - interactive: pick a tag profile (Standard / Psiphon / LiveKit / All), it fetches deps and builds
./build-all.sh             # macOS / Linux - standard
./build-all.sh psiphon     # with a build tag (fetches its deps automatically)
```
</details>

<details>
<summary><b>Command-line flags</b></summary>

| Flag | Default | Meaning |
| --- | --- | --- |
| `-addr` | `0.0.0.0:8765` | Address the panel listens on |
| `-open` | `true` | Open the dashboard on start |
| `-window` | `true` | Use a dedicated app window if available |
| `-minimize` | `true` | Minimize the console window on Windows |

```bash
./v2rayez -addr 127.0.0.1: