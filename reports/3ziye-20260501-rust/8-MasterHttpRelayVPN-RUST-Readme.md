# MasterHttpRelayVPN-RUST

[![Latest release](https://img.shields.io/github/v/release/therealaleph/MasterHttpRelayVPN-RUST?sort=semver&display_name=tag&logo=github&label=release)](https://github.com/therealaleph/MasterHttpRelayVPN-RUST/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/therealaleph/MasterHttpRelayVPN-RUST/total?label=downloads&logo=github)](https://github.com/therealaleph/MasterHttpRelayVPN-RUST/releases)
[![CI](https://github.com/therealaleph/MasterHttpRelayVPN-RUST/actions/workflows/release.yml/badge.svg)](https://github.com/therealaleph/MasterHttpRelayVPN-RUST/actions/workflows/release.yml)
[![License: MIT](https://img.shields.io/github/license/therealaleph/MasterHttpRelayVPN-RUST?color=blue)](LICENSE)
[![Stars](https://img.shields.io/github/stars/therealaleph/MasterHttpRelayVPN-RUST?style=flat&logo=github)](https://github.com/therealaleph/MasterHttpRelayVPN-RUST/stargazers)
[![Support](https://img.shields.io/badge/❤️_Support-sh1n.org-red?style=flat)](https://sh1n.org/donate)

Rust port of [@masterking32's MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN). **All credit for the original idea and the Python implementation goes to [@masterking32](https://github.com/masterking32).** This is a faithful reimplementation of the `apps_script` mode, packaged as two tiny binaries (CLI + desktop UI) with no runtime dependencies.

Free DPI bypass via Google Apps Script as a remote relay, with TLS SNI concealment. Your ISP's censor sees traffic going to `www.google.com`; behind the scenes a free Google Apps Script that you deploy in your own Google account fetches the real website for you.

> **Heads up on authorship:** the bulk of this Rust port was written with [Anthropic's Claude](https://claude.com) driving, reviewed by a human on every commit. Bug reports, fixes, and contributions are all welcome — see the [issues page](https://github.com/therealaleph/MasterHttpRelayVPN-RUST/issues).

**[Quick Start (English)](SF_README.md#quick-start)** | **[English Guide](#setup-guide)** | **[راهنمای خلاصه فارسی](SF_README.md#راهنمای-خلاصه-فارسی)** | **[راهنمای کامل فارسی](#راهنمای-فارسی)**

> **New here?** The Quick Start versions are short, plain-language, and cover the most common questions. The full guides have everything else (config options, full tunnel mode, OpenWRT, security notes).

## Why this exists

The original Python project is excellent but requires Python + `pip install cryptography h2` + system deps. For users in hostile networks that install process is often itself broken (blocked PyPI, missing wheels, Windows without Python). This port is a single ~2.5 MB executable that you download and run. Nothing else.

## How it works

```
Browser / Telegram / xray
        |
        | HTTP proxy (8085)  or  SOCKS5 (8086)
        v
mhrv-rs (local)
        |
        | TLS to Google IP, SNI = www.google.com
        v                       ^
   DPI sees www.google.com      |
        |                       | Host: script.google.com (inside TLS)
        v                       |
  Google edge frontend ---------+
        |
        v
  Apps Script relay (your free Google account)
        |
        v
  Real destination
```

The censor's DPI sees `www.google.com` in the TLS SNI and lets it through. Google's frontend hosts both `www.google.com` and `script.google.com` on the same IP and routes by the HTTP `Host` header inside the encrypted stream.

For a handful of Google-owned domains (`google.com`, `youtube.com`, `fonts.googleapis.com`, …) the same tunnel is used directly instead of going through the Apps Script relay. This bypasses the per-fetch quota and fixes the "User-Agent is always `Google-Apps-Script`" problem for those domains. You can add more domains via the `hosts` map in config.

## Platforms

Linux (x86_64, aarch64), macOS (x86_64, aarch64), Windows (x86_64), **Android 7.0+** (universal APK covering arm64, armv7, x86_64, x86). Prebuilt binaries on the [releases page](https://github.com/therealaleph/MasterHttpRelayVPN-RUST/releases).

**Android users** — grab `mhrv-rs-android-universal-v*.apk` and follow the full walk-through in [docs/android.md](docs/android.md) (English) or [docs/android.fa.md](docs/android.fa.md) (فارسی). The Android build runs the exact same `mhrv-rs` crate as the desktop (via JNI) and adds a TUN bridge via `tun2proxy`, so every app on the device routes its IP traffic through the proxy without per-app configuration.

> **Important Android caveat (issues #74 / #81):** while TUN captures all IP traffic, _HTTPS_ traffic from third-party apps still only works for apps that trust user-installed CAs. From Android 7 onward (which covers all supported devices — `minSdk = 24`), apps must opt in via `networkSecurityConfig` to trust the MITM CA we install. **Chrome and Firefox do**; **Telegram, WhatsApp, Instagram, YouTube, banking apps, games** do not. For those apps, either use `PROXY_ONLY` mode and point their in-app proxy at `127.0.0.1:1081` (S