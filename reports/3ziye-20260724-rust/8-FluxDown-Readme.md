<div align="center">

<img src="assets/logo/fluxdown_logo.png" alt="FluxDown Logo" width="128" />

# FluxDown

### Downloads, Supercharged.

*A blazing fast, multi-protocol download manager — the free & open-source IDM alternative.*

[![Latest Release](https://img.shields.io/github/v/release/zerx-lab/FluxDown?style=flat-square&color=06b6d4&label=release)](https://github.com/zerx-lab/FluxDown/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/zerx-lab/FluxDown/total?style=flat-square&color=22c55e)](https://github.com/zerx-lab/FluxDown/releases)
[![License: AGPL-3.0](https://img.shields.io/badge/license-AGPL--3.0-blue?style=flat-square)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux%20%7C%20NAS%20%7C%20Android-8b5cf6?style=flat-square)](#installation)
[![Rust](https://img.shields.io/badge/engine-Rust-f74c00?style=flat-square&logo=rust)](native/engine)
[![Flutter](https://img.shields.io/badge/UI-Flutter-02569B?style=flat-square&logo=flutter)](lib)
[![MCP Server](https://img.shields.io/badge/MCP-Glama-8b5cf6?style=flat-square)](https://glama.ai/mcp/servers/zerx-lab/FluxDown)

[**Website**](https://fluxdown.zerx.dev) · [**Download**](https://fluxdown.zerx.dev/#download) · [**Changelog**](https://fluxdown.zerx.dev/changelog) · [**FAQ**](https://fluxdown.zerx.dev/faq) · [**Feedback**](https://fluxdown.zerx.dev/feedback)

**English** | [简体中文](README.zh-CN.md)

</div>

---

## Highlights

- **Up to 10x faster** — Rust + Tokio engine with IDM-style dynamic segmentation
- **Multi-protocol** — HTTP/HTTPS, FTP, BitTorrent, eD2K, HLS & DASH streaming
- **Browser integration** — Chrome / Edge / Firefox extension with a 3-layer interception engine
- **AI-agent ready** — built-in MCP (Model Context Protocol) server: let Claude, Cursor & other AI clients manage your downloads
- **Resume anywhere** — full download state persisted in SQLite; survive crashes and reboots
- **Beautiful UI** — light/dark themes, 13 color schemes, responsive three-pane layout
- **Clean & private** — free and open source, no ads, no tracking, no account required, local-first

## Features

| Feature | Description |
|---|---|
| **Rust-Powered Engine** | Built on Rust and Tokio with zero-cost abstractions — memory-safe concurrency at maximum throughput |
| **Smart Segmentation** | Segments split dynamically at runtime; idle threads rescue slow segments, just like IDM — but smarter |
| **Multi-Protocol** | Dedicated engines for HTTP/HTTPS, FTP, BitTorrent (DHT/UPnP/magnet), eD2K (server + Kad DHT source finding, MD4 verification), HLS (AES-decrypt) and DASH |
| **Speed Control** | Token-bucket global rate limiting — download in the background without killing your browsing |
| **Resume Anywhere** | Every byte tracked in SQLite with WAL; power loss never costs you progress |
| **Browser Integration** | Three-layer download interception, streaming media sniffing, Alt+Click bypass, right-click send |
| **MCP Server** | Built-in Model Context Protocol endpoint (Streamable HTTP) with 9 tools — AI agents can add, monitor and control downloads |
| **Beautiful Interface** | shadcn-style widgets, IDM-style segment visualization, named queues, system tray |
| **Clean & Private** | Zero ads, zero telemetry lock-in, zero accounts — your data never leaves your machine |

## FluxDown vs. IDM

| | FluxDown | IDM |
|---|:---:|:---:|
| Price | **Free & open source** | $24.95 + renewals |
| Open source | Yes (AGPL-3.0) | No |
| Platforms | Windows / macOS / Linux / NAS / Android | Windows only |
| BitTorrent & magnet | Yes | No |
| eD2K / eMule links | Yes | No |
| HLS / DASH streaming | Yes | Partial |
| Dynamic segmentation | Yes | Yes |
| Browser extension | Chrome / Edge / Firefox | Yes |
| Ads & tracking | **None** | — |

## Installation

Grab the latest build from [**GitHub Releases**](https://github.com/zerx-lab/FluxDown/releases/latest) or [**fluxdown.zerx.dev**](https://fluxdown.zerx.dev/#download):

| Platform | Packages |
|---|---|
| **Windows** (x64 / ARM64) | `setup.exe` installer · portable `.zip` |
| **macOS** (Intel / Apple Silicon) | `.dmg` · portable `.tar.gz` |
| **Linux** (x64) | `.AppImage` · `.deb` · Arch `.pkg.tar.zst` · portable `.tar.gz` |
| **Android** (arm64-v8a / armeabi-v7a / x86_64) | per-ABI `.apk` · universal `.apk` |
| **NAS / Server** (headless, x64 / ARM64) | [Docker](https://ghcr.io/zerx-lab/fluxdown-server) · Synology DSM 6/7 `.spk` · QNAP `.qpkg` · OpenWrt `.ipk` · Unraid CA template · CasaOS / ZimaOS app store |

### Browser Extension

Install the extension so FluxDown takes over browser downloads automatically:

[<img src="https://img.shields.io/badge/Chrome-Web%20Store-4285F4?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Chrome Web Store" />](https://chromewebstore.google.com/detail/fluxdown/meleenglfggcmcajknpeeeiobnpfmahc)
[<img src="https://img.shields.io/badge/Edge-Add--ons-0078D4?style=for-the-badge&logo=microsoftedge&logoColor=white" alt="Edge