<p align="center">
  <img src="docs/assets/logo_banner.png" alt="MeowHub" width="560" />
</p>

<p align="center">
  <b>TUTU Smart Control · AI Phone Control Hub</b>
</p>

<p align="center">
  <img src="https://github.com/openclaw.png?size=200" alt="OpenClaw" width="88" />
  <br/>
  <code>SUB-BRAND · OpenClaw / MeowClaw</code>
  <br/>
  <b>Built-in Full OpenClaw Runtime (2026.3.24)</b>
  <br/>
  <span>The lobster way 🦞</span>
</p>

<p align="center">
  <b>AI Phone Avatar — Create Your Own Phone Automation Skills with AI</b>
</p>

<p align="center">
  <b>MeowHub × OpenClaw (The lobster way 🦞)</b><br/>
  Built-in Full OpenClaw, One-Tap Install on Android.
</p>

<p align="center">
  No manual Termux setup, no git clone on phone, no npm install, no fragile shell scripts.
</p>

<p align="center">
  <a href="https://tutuai.me">Official Website</a> •
  <a href="README_CN.md">中文文档</a> •
  <a href="docs/skill-development-guide.md">Skill Development Guide</a> •
  <a href="skills/">Skill Gallery</a> •
  <a href="CONTRIBUTING.md">Contributing</a>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-GPL%20v3-blue.svg" alt="License: GPL v3" /></a>
  <img src="https://img.shields.io/badge/Android-9%2B-green.svg" alt="Android 9+" />
  <img src="https://img.shields.io/badge/Kotlin-2.3-purple.svg" alt="Kotlin" />
  <img src="https://img.shields.io/badge/Jetpack%20Compose-Material%203-blue.svg" alt="Compose" />
  <a href="https://github.com/zhaojiaqi/MeowHub/stargazers"><img src="https://img.shields.io/github/stars/zhaojiaqi/MeowHub?style=social" alt="Stars" /></a>
  <a href="https://github.com/zhaojiaqi/MeowHub/network/members"><img src="https://img.shields.io/github/forks/zhaojiaqi/MeowHub?style=social" alt="Forks" /></a>
  <a href="https://github.com/zhaojiaqi/MeowHub/issues"><img src="https://img.shields.io/github/issues/zhaojiaqi/MeowHub" alt="Issues" /></a>
</p>

---

## What is MeowHub?

MeowHub is an open-source Android app that turns your phone into an **AI-powered automation agent**. It serves as **the hands and feet of AI in the physical world** — enabling AI to truly "see" your screen, "tap" buttons, and "swipe" through apps to accomplish any task on your phone. MeowHub runs entirely on your device, is fully open-source, and uses a declarative **Skill Engine** so you can create and share automation skills in JSON — no coding required.

### Built-in OpenClaw, Not a Separate DIY Install

MeowHub now ships with a **fully integrated OpenClaw runtime** inside the app. This is not a "go install Termux, then run a few commands, then hope npm works" experience. Instead, MeowHub bundles the **complete OpenClaw-based MeowClaw stack** and can install it for users with **one tap**.

- **Built-in full OpenClaw** — bundled runtime, workspace, terminal, console, and Android bridge
- **One-tap install** — bootstrap, Node.js, npm, OpenClaw, workspace assets, and gateway are prepared automatically
- **No phone-side dependency hell** — no manual `git clone`, `npm install`, or package chasing on-device
- **More stable in bad network conditions** — key runtime assets are pre-packaged in the APK instead of fetched during first launch
- **Ready-to-use AI console** — terminal + web console are embedded directly in MeowHub

This matters because phone-side package installs are often the most fragile part of mobile AI-agent deployment: flaky network, broken mirrors, missing binaries, Android linker quirks, and inconsistent shell environments. MeowHub hides that complexity and delivers a **near out-of-box OpenClaw experience on Android**.

**Our vision:** Everyone can create and share their own phone AI avatar skills — giving AI the power to interact with the physical world.

### Why MeowHub? — A Fundamental Difference from Accessibility-Based Solutions

Most phone automation tools (Auto.js, Hamibot, etc.) rely on Android's **AccessibilityService**. This approach has critical flaws. MeowHub uses the **system-level ADB protocol**, solving these problems by design:

> **System-Level, Undetectable**
> Accessibility-based solutions run at the application layer. Major apps like WeChat, TikTok, Taobao, and Alipay actively detect Accessibility Services — triggering risk controls or even **account bans**. MeowHub operates through ADB at the system level, completely transparent to target apps, equivalent to real finger touches, **undetectable by any application**.

> **Stable & Reliable, One-Time Pairing**
> Accessibility permissions are fragile — broken by OS updates, inconsistent across OEM ROMs, auto-revoked or interrupted by system prompts. MeowHub uses the standard ADB protocol for consistent and stable behavior. Pair once, use permanently — no repeated authorization needed.

> **No Blind Spots**
> Accessibility can only interact with UI elements that have Accessibility nodes — games, Canvas, and WebView are out of reach. MeowHub supports touch, swipe, and key input at any screen position, completely framewo