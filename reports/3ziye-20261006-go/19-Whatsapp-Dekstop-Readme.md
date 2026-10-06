<p align="center">
  <img src="screenshots/hero-banner.png" width="100%" alt="WhatsApp Desk - Native, Ultra-Light, Private Desktop Client">
</p>

<p align="center">
  <a href="https://github.com/vianziro/Whatsapp-Dekstop/releases/latest"><img src="https://img.shields.io/github/v/release/vianziro/Whatsapp-Dekstop?label=release&color=18c77b&style=flat-square" alt="Latest Release"></a>
  <a href="https://github.com/vianziro/Whatsapp-Dekstop/releases"><img src="https://img.shields.io/badge/platform-macOS%20%7C%20Windows%20%7C%20Linux-0b1713?style=flat-square" alt="Platforms"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-18c77b?style=flat-square" alt="License: MIT"></a>
  <a href="https://go.dev/"><img src="https://img.shields.io/badge/go-1.26+-00ADD8?style=flat-square&logo=go&logoColor=white" alt="Go Version"></a>
  <a href="https://github.com/vianziro/Whatsapp-Dekstop/releases/latest"><img src="https://img.shields.io/badge/architecture-Universal%20%7C%20x64-555?style=flat-square" alt="Architecture"></a>
  <a href="https://github.com/vianziro/Whatsapp-Dekstop"><img src="https://komarev.com/ghpvc/?username=vianziro&repo=Whatsapp-Dekstop&style=flat-square&color=18c77b&label=visitors" alt="Visitors"></a>
</p>

<p align="center">
  <strong>WhatsApp Desk</strong> is a fast, ultra-lightweight, privacy-respecting desktop client for <a href="https://web.whatsapp.com">WhatsApp Web</a>.<br>
  Built with native operating system web engines — <strong>WebKit</strong> on macOS, <strong>WebView2</strong> on Windows, and <strong>WebKitGTK</strong> on Linux.<br>
  <em>Zero Electron bloat • Zero telemetry • Zero message relay servers • Complete local privacy.</em>
</p>

---

## Downloads

Get the latest stable release for your operating system (updated automatically):

| Platform | Recommended Installer | Portable / Archive | Requirements |
| :--- | :--- | :--- | :--- |
| **macOS** | [**Universal DMG**](https://github.com/vianziro/Whatsapp-Dekstop/releases/latest/download/WhatsApp-Desk-macOS-Universal.dmg) | [Universal ZIP](https://github.com/vianziro/Whatsapp-Dekstop/releases/latest/download/WhatsApp-Desk-macOS-Universal.zip) | macOS 12.0+ (Apple Silicon & Intel) |
| **Windows 10 / 11** | [**Setup Wizard (.exe)**](https://github.com/vianziro/Whatsapp-Dekstop/releases/latest/download/WhatsApp-Desk-Windows-x64-Setup.exe) | [Portable EXE](https://github.com/vianziro/Whatsapp-Dekstop/releases/latest/download/WhatsAppDesk.exe) | Windows 10/11 x64 (WebView2 runtime) |
| **Linux (x64)** — via [v1.5.9.9](https://github.com/vianziro/Whatsapp-Dekstop/releases/tag/v1.5.9.9) | [**DEB (WebKitGTK 4.0, Ubuntu 22.04)**](https://github.com/vianziro/Whatsapp-Dekstop/releases/download/v1.5.9.9/WhatsApp-Desk-Linux-amd64.deb) · [**DEB (WebKitGTK 4.1, Ubuntu 24.04+)**](https://github.com/vianziro/Whatsapp-Dekstop/releases/download/v1.5.9.9/WhatsApp-Desk-Linux-amd64-webkit4.1.deb) | [tar.gz 4.0](https://github.com/vianziro/Whatsapp-Dekstop/releases/download/v1.5.9.9/WhatsApp-Desk-Linux-x64.tar.gz) · [tar.gz 4.1](https://github.com/vianziro/Whatsapp-Dekstop/releases/download/v1.5.9.9/WhatsApp-Desk-Linux-x64-webkit4.1.tar.gz) | GTK 3 & WebKitGTK 4.0 / 4.1 |

> [!TIP]
> Download links point automatically to the latest release assets. You can also view all past versions and architectures on the [Releases](https://github.com/vianziro/Whatsapp-Dekstop/releases) page.
>
> **Linux note:** the 1.6.3 pipeline builds macOS and Windows only. Linux packages keep
> riding with [v1.5.9.9](https://github.com/vianziro/Whatsapp-Dekstop/releases/tag/v1.5.9.9)
> until the next Linux build; their fixed links above always resolve.

---

## Key Features

* **Two Accounts, One Window:** Link a second WhatsApp account with a fully isolated browser profile and switch from the account dock (`Ctrl+Shift+1/2` / `Cmd+Shift+1/2`) — with per-account unread badges and a seamless, blink-free swap. One live engine at a time keeps memory low.
* **Ultra-Lightweight Engine:** Built directly on native OS webviews (WebKit on macOS, WebView2 on Windows, WebKitGTK on Linux) instead of bundling a whole browser, so the app's own process stays around 100 MB.
* **Frees Memory While Hidden (macOS):** WhatsApp Web keeps every image and video it has displayed alive in the renderer, which reaches a couple of gigabytes over a long session. Once the window has been off screen for 15 minutes the page reloads and that memory comes back — only while hidden, at most every 30 minutes, and never during an upload or an open preview. Toggle it under Settings → Maintenance.
* **Zero Telemetry & Private by Design:** Communicates straight with `https://web.whatsapp.com`. No analytics tracking, no user profiling, and no proxy or relay servers.
* **Instant Privacy Mode & Auto-Lock:** Quickly redact chat previews, sender names, and media thumbnails with a shortcut (`Ctrl+Shift+P` / `Cmd+Shift+P`) or automatic lock on idle.
* **Built-in Document & Office Preview:** Instant in-app previe