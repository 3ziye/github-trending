# OpenClaw on Android

<img src="docs/images/openclaw_android.jpg" alt="OpenClaw on Android">

![Android 7.0+](https://img.shields.io/badge/Android-7.0%2B-brightgreen)
![Termux](https://img.shields.io/badge/Termux-Required-orange)
![No proot](https://img.shields.io/badge/proot--distro-Not%20Required-blue)
![License MIT](https://img.shields.io/github/license/AidanPark/openclaw-android)
![GitHub Stars](https://img.shields.io/github/stars/AidanPark/openclaw-android)

Because Android deserves a shell.

## No Linux install required

The standard approach to running OpenClaw on Android requires installing proot-distro with Linux, adding 700MB-1GB of overhead. OpenClaw on Android eliminates this by installing just the glibc dynamic linker (ld.so), letting you run OpenClaw without a full Linux distribution.

**Standard approach**: Install a full Linux distribution in Termux via proot-distro.

```
┌───────────────────────────────────────────────────┐
│ Linux Kernel                                      │
│ ┌───────────────────────────────────────────────┐ │
│ │ Android · Bionic libc · Termux                │ │
│ │ ┌───────────────────────────────────────────┐ │ │
│ │ │ proot-distro · Debian/Ubuntu              │ │ │
│ │ │ ┌───────────────────────────────────────┐ │ │ │
│ │ │ │ GNU glibc                             │ │ │ │
│ │ │ │ Node.js → OpenClaw                    │ │ │ │
│ │ │ └───────────────────────────────────────┘ │ │ │
│ │ └───────────────────────────────────────────┘ │ │
│ └───────────────────────────────────────────────┘ │
└───────────────────────────────────────────────────┘
```

**This project**: No proot-distro — just the glibc dynamic linker.

```
┌───────────────────────────────────────────────────┐
│ Linux Kernel                                      │
│ ┌───────────────────────────────────────────────┐ │
│ │ Android · Bionic libc · Termux                │ │
│ │ ┌───────────────────────────────────────────┐ │ │
│ │ │ glibc ld.so (linker only)                 │ │ │
│ │ │ ld.so → Node.js → OpenClaw                │ │ │
│ │ └───────────────────────────────────────────┘ │ │
│ └───────────────────────────────────────────────┘ │
└───────────────────────────────────────────────────┘
```

| | Standard (proot-distro) | This project |
|---|---|---|
| Storage overhead | 1-2GB (Linux + packages) | ~200MB |
| Setup time | 20-30 min | 3-10 min |
| Performance | Slower (proot layer) | Native speed |
| Setup steps | Install distro, configure Linux, install Node.js, fix paths... | Run one command |

## <img src="docs/images/claw-icon.svg" width="28"> Claw App

A standalone Android app is also available. It bundles a terminal emulator and a WebView-based UI into a single APK — no Termux required.

- One-tap setup: bootstrap, Node.js, and OpenClaw installed from within the app
- Built-in dashboard for gateway control, runtime info, and tool management
- Works independently of Termux — installing the app does not affect an existing Termux + `oa` setup

Download the APK from the [Releases](https://github.com/AidanPark/openclaw-android/releases) page.


## Requirements

- Android 7.0 or higher (Android 10+ recommended)
- ~1GB free storage
- Wi-Fi or mobile data connection

## What It Does

The installer automatically resolves the differences between Termux and standard Linux. There's nothing you need to do manually — the single install command handles all of these:

1. **glibc environment** — Installs the glibc dynamic linker (via pacman's glibc-runner) so standard Linux binaries run without modification
2. **Node.js (glibc)** — Downloads official Node.js linux-arm64 and wraps it with an ld.so loader script (no patchelf, which causes segfault on Android)
3. **Path conversion** — Automatically converts standard Linux paths (`/tmp`, `/bin/sh`, `/usr/bin/env`) to Termux paths
4. **Temp folder setup** — Configures an accessible temp folder for Android
5. **Service manager bypass** — Configures normal operation without systemd
6. **OpenCode integration** — If selected, installs OpenCode using proot + ld.so concatenation for Bun standalone binaries

## Step-by-Step Setup (from a fresh phone)

1. [Prepare Your Phone](#step-1-prepare-your-phone)
2. [Install Termux](#step-2-install-termux)
3. [Initial Termux Setup](#step-3-initial-termux-setup)
4. [Install OpenClaw](#step-4-install-openclaw) — one command
5. [Start OpenClaw Setup](#step-5-start-openclaw-setup)
6. [Start OpenClaw (Gateway)](#step-6-start-openclaw-gateway)

### Step 1: Prepare Your Phone

Configure Developer Options, Stay Awake, charge limit, and battery optimization. See the [Keeping Processes Alive guide](docs/disable-phantom-process-killer.md) for step-by-step instructions.

### Step 2: Install Termux

> **Important**: The Play Store version of Termux is discontinued and will not work. You must install from F-Droid.

1. Open your phone's browser and go to [f-droid.org](https://f-droid.org)
2. Search for `Termux`, then tap **Download APK** to download and install
 