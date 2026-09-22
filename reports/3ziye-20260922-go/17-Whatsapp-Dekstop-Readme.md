<p align="center">
  <img src="screenshots/hero-banner.png" width="100%" alt="WhatsApp Desk - Native, Ultra-Light, Private Desktop Client">
</p>

<p align="center">
  <a href="https://github.com/vianziro/Whatsapp-Dekstop/releases/latest"><img src="https://img.shields.io/github/v/release/vianziro/Whatsapp-Dekstop?label=release&color=18c77b&style=flat-square" alt="Latest Release"></a>
  <a href="https://github.com/vianziro/Whatsapp-Dekstop/releases"><img src="https://img.shields.io/badge/platform-macOS%20%7C%20Windows%20%7C%20Linux-0b1713?style=flat-square" alt="Platforms"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-18c77b?style=flat-square" alt="License: MIT"></a>
  <a href="https://go.dev/"><img src="https://img.shields.io/badge/go-1.26+-00ADD8?style=flat-square&logo=go&logoColor=white" alt="Go Version"></a>
  <a href="https://github.com/vianziro/Whatsapp-Dekstop/releases/latest"><img src="https://img.shields.io/badge/architecture-Universal%20%7C%20x64-555?style=flat-square" alt="Architecture"></a>
</p>

<p align="center">
  <strong>WhatsApp Desk</strong> is a fast, ultra-lightweight, privacy-respecting desktop client for <a href="https://web.whatsapp.com">WhatsApp Web</a>.<br>
  Built with native operating system web engines — <strong>WebKit</strong> on macOS, <strong>WebView2</strong> on Windows, and <strong>WebKitGTK</strong> on Linux.<br>
  <em>Zero Electron bloat • Zero telemetry • Zero message relay servers • Complete local privacy.</em>
</p>

---

## ⚡ Downloads

Get the latest stable release for your operating system (updated automatically):

| Platform | Recommended Installer | Portable / Archive | Requirements |
| :--- | :--- | :--- | :--- |
| **macOS** | [**Universal DMG**](https://github.com/vianziro/Whatsapp-Dekstop/releases/latest/download/WhatsApp-Desk-macOS-Universal.dmg) | [Universal ZIP](https://github.com/vianziro/Whatsapp-Dekstop/releases/latest/download/WhatsApp-Desk-macOS-Universal.zip) | macOS 11.0+ (Apple Silicon & Intel) |
| **Windows 10 / 11** | [**Setup Wizard (.exe)**](https://github.com/vianziro/Whatsapp-Dekstop/releases/latest/download/WhatsApp-Desk-Windows-x64-Setup.exe) | [Portable EXE](https://github.com/vianziro/Whatsapp-Dekstop/releases/latest/download/WhatsAppDesk.exe) | Windows 10/11 x64 (WebView2 runtime) |
| **Linux** | [**Build from source**](#️-building--releasing) | [older releases (≤ v1.5.9.2)](https://github.com/vianziro/Whatsapp-Dekstop/releases) | GTK 3 & WebKitGTK 4.0 / 4.1 |

> [!TIP]
> Download links point automatically to the latest release assets. You can also view all past versions and architectures on the [Releases](https://github.com/vianziro/Whatsapp-Dekstop/releases) page.

---

## ✨ Key Features

* 🚀 **Ultra-Lightweight Engine:** Built directly on native OS webviews (WebKit on macOS, WebView2 on Windows, WebKitGTK on Linux). Minimal RAM and battery footprint compared to Chromium/Electron apps.
* 🛡️ **Zero Telemetry & Private by Design:** Communicates straight with `https://web.whatsapp.com`. No analytics tracking, no user profiling, and no proxy or relay servers.
* 👁️ **Instant Privacy Mode & Auto-Lock:** Quickly redact chat previews, sender names, and media thumbnails with a shortcut (`Ctrl+Shift+P` / `Cmd+Shift+P`) or automatic lock on idle.
* 📄 **Built-in Document & Office Preview:** Instant in-app previews for PDFs, Word docs, Excel spreadsheets, PowerPoint slides, and text attachments without cluttering your drive with duplicate files.
* 🛠️ **Windows Setup Wizard:** Per-user installer with branded artwork, Start Menu and desktop shortcuts, and clean uninstallation in Windows Apps & Features.
* ⚙️ **Unified Settings & Module Guard:** Single accessible settings control (`Ctrl+,` / `Cmd+,`) protected by runtime module isolation (`waRunModule`) against unexpected DOM changes.
* 🔄 **Built-in Self Updater:** Automatic update notifications with cryptographic `SHA256SUMS` validation before applying updates.
* 🖥️ **Per-Monitor Window Memory:** Automatically remembers window position and dimension across multi-monitor setups.

---

## 📸 Application Preview

<p align="center">
  <img src="screenshots/app-dark.png" width="900" alt="WhatsApp Desk Main Chat Window">
</p>

<p align="center">
  <img src="screenshots/macos-menu.png" width="620" alt="WhatsApp Desk Settings and Customization Panel">
</p>

*Note: Screenshots use blurred chat content to protect personal information.*

---

## ⌨️ Keyboard Shortcuts

| Feature | macOS | Windows & Linux |
| :--- | :--- | :--- |
| **Open Settings** | <kbd>Cmd</kbd> + <kbd>,</kbd> | <kbd>Ctrl</kbd> + <kbd>,</kbd> |
| **Toggle Privacy Mode** | <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> |
| **Toggle Always on Top** | <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>T</kbd> | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>T</kbd> |
| **Mute / Unmute Audio** | <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>M</kbd> | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kb