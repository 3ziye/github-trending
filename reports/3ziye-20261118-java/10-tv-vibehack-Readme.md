# tv-vibehack 📺✨

> **Transform any ad-bloated Android TV or Google TV into a lightning-fast, tvOS-inspired, fail-safe experience — without root, without bootloop risks, and without losing access to stock features.**

[![Android 14 Ready](https://img.shields.io/badge/Android-14%20(API%2034)-green.svg)](https://developer.android.com/about/versions/14)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Root Required: No](https://img.shields.io/badge/Root-Not%20Required-brightgreen.svg)](#)
[![Zero Bootloop Architecture](https://img.shields.io/badge/Architecture-100%25%20Fail--Safe-orange.svg)](#the-100-fail-safe-architecture)

---

## 📐 Architecture & Transformation Overview

```text
[ STOCK GOOGLE TV ]                             [ NLRC TV VIBEHACK ]
┌──────────────────────────────────────┐        ┌──────────────────────────────────────┐
│  Sponsored Ad Banner (70% Screen)    │        │  NLRC Home · Ambient Clock & Date    │
│  [Trending Shows] [Paid Promotions]  │        │                                      │
│  50+ Bloatware OTT Apps              │   ➔    │                                      │
│  Remote Buttons Lock You In Paywalls │        │  Dock: [HDMI 2 (Cable)] [Media Vault]│
└──────────────────────────────────────┘        └──────────────────────────────────────┘
   • 2.5 GB RAM used                               • 120 MB RAM used
   • Heavy telemetry & tracking                    • 0 Ads · 0 Telemetry · 100% Fail-Safe
```

---

## 🎯 The Motivation

Modern Smart TVs ship with:
- **Sponsored ads covering 70% of the screen**.
- **Sluggish bloatware** and 50+ pre-installed background apps consuming memory and tracking habits.
- **Unremappable sponsored remote buttons** (Netflix, Prime Video) that elderly family members hit by mistake, throwing them into subscription walls.
- **Overly complicated navigation** that makes switching to Cable/HDMI or playing personal home videos a headache.

**tv-vibehack** solves this permanently. Originally built to give aging parents a distraction-free, one-touch TV experience, it provides a universal blueprint for taking back control of any Android TV without root.

---

## ⚡ What Makes This Different?

### 1. 🛡️ The 100% Fail-Safe Architecture (Zero Bootloops)
On Android 14 Google TV, disabling the stock launcher (`com.google.android.apps.tv.launcherx`) breaks Direct Boot, tripping Android's `RescueParty` service and bricking the TV into a black-screen recovery state.

**tv-vibehack never disables `launcherx`.** Instead:
- The custom launcher is **`directBootAware="true"`**.
- A lightweight native **Accessibility Service** (`HomeKeyService`) intercepts Home key events and window transitions in under 10ms.
- If the custom launcher is ever uninstalled or crashes, Google TV seamlessly takes over. **Zero chance of bricking your TV.**

### 2. 🔀 Hardware Passthrough (Direct HDMI Switching)
No more opening 4 nested TV menus just to watch cable. Through reverse-engineered Realtek RTD `TvContract` passthrough URIs, the launcher switches directly to HDMI inputs programmatically:
```java
Uri uri = TvContract.buildChannelUriForPassthroughInput(
    "com.realtek.tv.passthrough/.hdmiinput.HDMITvInputService/HW151519744" // HDMI 2
);
context.startActivity(new Intent(Intent.ACTION_VIEW, uri));
```

### 3. 🎮 Sponsored Remote Key Remapping (No Root)
`HomeKeyService` intercepts hardcoded hardware remote buttons (`KEYCODE_BUTTON_3` for Netflix, `KEYCODE_BUTTON_4` for Prime Video, `KEYCODE_PROG_RED`/`GREEN`) and redirects them straight to HDMI 2 / Set-Top Box in <150ms without root.

### 4. 🎞️ Offline TV Media Vault & Legacy Transcoding
Many families have legacy home videos or recordings stored on USB drives encoded in older formats (e.g., DVD MPEG-2) that native modern Smart TV chipsets cannot decode inside standard MP4 containers.

#### How to Add Your Own Media:
1. **Transcode to Hardware-Accelerated H.264:**
   ```bash
   ffmpeg -i "MyVideo_Part_1.mp4" -c:v libx264 -preset faster -crf 23 -c:a aac -b:a 192k "Part_1.mp4"
   ```
2. **Push Directly into TV Internal Storage:**
   ```bash
   adb shell mkdir -p /sdcard/Movies/NLRC
   adb push Part_1.mp4 /sdcard/Movies/NLRC/Part_1.mp4
   adb push Part_2.mp4 /sdcard/Movies/NLRC/Part_2.mp4
   adb push Part_3.mp4 /sdcard/Movies/NLRC/Part_3.mp4
   ```
3. **Instant D-pad Remote Navigation:**
   Launch **PenDrive / Media Viewer** directly from the dock. No USB stick needs to remain plugged in; videos play natively at 60fps with intuitive remote controls:
   - ◄ / ►: Seek -10s / +10s with real-time HUD.
   - ▲ / ▼ or CH+ / CH-: Switch to Next / Previous part.
   - OK: Play / Pause toggle.

---

## 🚀 Quick Start

### 1. Enable ADB on your Android TV
1. On the TV: **Settings** → **System** → **About** → Click **Build** 7 times to enable Developer Options.
2. Go to **Settings** → **System** → **Developer Options** → Turn on **USB Debugging** (and Network Debugging if available).
3. Connect your computer to the same Wi-Fi 