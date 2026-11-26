<p align="center"><img src="agent/PhoneBox.Agent/phonebox.ico" width="72" alt="PhoneBox icon"></p>

<h1 align="center">PhoneBox</h1>

<p align="center">
  <b>English</b> ·
  <a href="docs/README.tr.md">Türkçe</a> ·
  <a href="docs/README.de.md">Deutsch</a> ·
  <a href="docs/README.fr.md">Français</a> ·
  <a href="docs/README.es.md">Español</a> ·
  <a href="docs/README.it.md">Italiano</a> ·
  <a href="docs/README.pt.md">Português</a> ·
  <a href="docs/README.pt-BR.md">Português (Brasil)</a> ·
  <a href="docs/README.nl.md">Nederlands</a> ·
  <a href="docs/README.pl.md">Polski</a> ·
  <a href="docs/README.ru.md">Русский</a> ·
  <a href="docs/README.el.md">Ελληνικά</a> ·
  <a href="docs/README.vi.md">Tiếng Việt</a> ·
  <a href="docs/README.zh.md">中文 (简体)</a> ·
  <a href="docs/README.ja.md">日本語</a> ·
  <a href="docs/README.ko.md">한국어</a> ·
  <a href="docs/README.id.md">Bahasa Indonesia</a> ·
  <a href="docs/README.th.md">ไทย</a> ·
  <a href="docs/README.uk.md">Українська</a> ·
  <a href="docs/README.hi.md">हिन्दी</a> ·
  <a href="docs/README.cs.md">Čeština</a> ·
  <a href="docs/README.ar.md">العربية</a> ·
  <a href="docs/README.zh-Hant.md">中文（繁體）</a>
</p>

<p align="center"><b>Turn an old Android phone into a desk panel for your computer.</b><br>
PC stats, AI coding sessions, music and touch controls over USB or Wi-Fi.<br>
Windows, Linux and macOS. No root, PhoneBox account or cloud service required.</p>

<p align="center">
  <a href="https://ersinkoc.github.io/phonebox/"><b>Try the live demo</b></a> ·
  <a href="https://github.com/ersinkoc/phonebox/releases/latest"><b>Download</b></a> ·
  <a href="#quick-start"><b>Quick start</b></a>
</p>

<p align="center">
  <a href="https://github.com/ersinkoc/phonebox/actions/workflows/build.yml"><img src="https://github.com/ersinkoc/phonebox/actions/workflows/build.yml/badge.svg" alt="Build status"></a>
  <a href="https://github.com/ersinkoc/phonebox/releases/latest"><img src="https://img.shields.io/github/v/release/ersinkoc/phonebox?label=release" alt="Latest release"></a>
  <img src="https://img.shields.io/badge/Windows%20%C2%B7%20Linux%20%C2%B7%20macOS-.NET%2010-512bd4" alt="Windows, Linux, macOS; .NET 10">
  <img src="https://img.shields.io/badge/Android-5%2B-3ddc84" alt="Android 5+">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue" alt="MIT license"></a>
</p>

<p align="center"><img src="docs/hero-0.6.png" width="900" alt="PhoneBox on three phones showing automation, home and planner pages"><br>
<sub>Example layouts with demo data.</sub></p>

PhoneBox pairs a full-screen **Android app** with a small **desktop agent**. Build your panel in a browser-based
visual editor: **136 widgets**, **30 templates**, multiple pages and a live preview. Connect several phones with
their own layouts, or switch one phone between paired computers.

## What you can do

| Use it for | What appears on the phone |
|---|---|
| **PC monitoring** | CPU, GPU, RAM, disks, network and ping; charts, GPU details and process controls |
| **AI coding** | Claude, Codex and Antigravity quotas, reset times and burn-rate forecasts; local Claude Code, Codex and OpenCode sessions (native and inside WSL); GitHub reviews and CI status |
| **Touch controls** | App and URL shortcuts, key combinations and macros; application audio, microphone, media, OBS and system controls through [Control Deck](docs/CONTROL-DECK.md) |
| **Everyday use** | Now Playing, internet radio, clocks, weather, calendars, notes, checklists, pomodoro and timers |
| **Automation** | Webhook values and notifications, Home Assistant controls and rules that react to activity on the computer |

Tap an AI session for its model, timing and token details. Opt in to Codex, Claude Code or OpenCode permission prompts
to answer **Allow**, **Deny** (and **Always allow** for OpenCode) from the phone. Optional
[CodexBar integration](docs/GUIDE.md#widgets) adds quota providers and a cost overview.

<p align="center"><a href="docs/tour-0.6.mp4"><img src="docs/tour-0.6.gif" width="780" alt="PhoneBox tour showing notifications, a Claude Code permission prompt and automatic page switching"></a><br>
<sub>A tour with demo data: notifications, permission prompts and automatic page switching. <a href="docs/tour-0.6.mp4">Watch the MP4</a></sub></p>

## Quick start

You need an **Android 5+ phone** (Android 6 or later recommended) and a supported computer. USB uses a data cable and USB debugging; Wi-Fi pairing
works without either. Release agents include .NET, so you do not need to install the runtime.

### 1. Install the desktop agent

**Windows 10/11 x64 or Windows 11 ARM64** — paste into a normal PowerShell window:

```powershell
irm https://raw.githubusercontent.com/ersinkoc/phonebox/main/setup.ps1 | iex
```

**Linux or macOS** — run as your own user:

```sh
curl -fsSL https://raw.githubusercontent.com/ersinkoc/phonebox/main/setup.sh | bash
```

Setup downloads the latest release, checks its SHA-256 checksum, offers missing dependen