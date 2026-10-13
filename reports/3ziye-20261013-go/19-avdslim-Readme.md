# ⚡ AVD-SLIM™

> **Android Emulator RAM & CPU Optimizer**  
> *Inspired by [MobAI-App/simslim](https://github.com/MobAI-App/simslim) for iOS simulators.*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Go Report Card](https://goreportcard.com/badge/github.com/kdbhalala/avdslim)](https://goreportcard.com/report/github.com/kdbhalala/avdslim)
[![Release](https://img.shields.io/github/v/release/kdbhalala/avdslim)](https://github.com/kdbhalala/avdslim/releases)
[![GitHub Marketplace](https://img.shields.io/badge/Marketplace-AVD--SLIM-blue?logo=github-actions&logoColor=white)](https://github.com/marketplace/actions/avd-slim-android-emulator-ram-ci-optimizer)

`avdslim` is a lightweight, zero-dependency CLI tool that cuts Android Virtual Device (AVD) host memory from **~8.5 GB to ~2.5 GB** in Activity Monitor (**~1.5 GB** of it actually resident) and cuts idle CPU overhead to near-zero on Apple Silicon & Linux.

```
┌────────────────────────────────────────────────────────────────────────┐
│  Activity Monitor (phys_footprint), Pixel 10 Pro:                      │
│  Before:  qemu-system-aarch64  ██████████████████████████  8,518 MB    │
│  After:   qemu-system-aarch64  ████████                    2,498 MB    │
│                                                                        │
│  ⚡ Reclaimed: ~6.0 GB host RAM (71% reduction)                        │
└────────────────────────────────────────────────────────────────────────┘
```

## ⚡ Quick Start

```bash
brew tap kdbhalala/avdslim https://github.com/kdbhalala/avdslim.git && brew install avdslim
avdslim doctor      # read-only audit: what is costing RAM on this machine
avdslim tune-avd    # 1536 MB + host GPU in the AVD's config.ini (backup kept)
avdslim start       # launch with -lowram; slims the guest once it boots
avdslim off         # undo the guest changes any time
```

Launching from Android Studio's ▶ button instead? See the optional
[`install-shim`](#1-android-studio-1-click-integration-install-shim) below.

---

## 🛡️ Fidelity & Safety Guarantee

The #1 fear with debloating tools is silent breakage. `avdslim` is designed to be **safe by default**:

| Subsystem / Service | Status | Guarantee |
| :--- | :---: | :--- |
| **Firebase Cloud Messaging (FCM)** | ✅ **100% Active** | `GcmService` allowlisted; push notifications work out of the box |
| **Firebase Auth & Google Sign-In** | ✅ **100% Active** | Core `com.google.android.gms` APIs are protected and never disabled |
| **Android System WebView** | ✅ **100% Active** | Chromium engine, JavaScript, and in-app browsers untouched |
| **Flutter / React Native / Native** | ✅ **100% Active** | Hot reload, DevTools, debugging, and JNI/NDK runtimes work 100% |
| **Localhost & Network Sockets** | ✅ **100% Active** | TCP/UDP, Metro bundler (`:8081`), and adb reverse unaffected |
| **Full Revert (`off`)** | ✅ **One Command** | `avdslim off` re-enables every package avdslim disabled and puts each changed setting back to its previous value. If a package can't be re-enabled, it says which and `off` can be re-run. After `avdslim bake`, also run `avdslim unbake` (the snapshot is slimmed). |

---

## 💡 Golden SDK Recommendation: Which System Image to Choose?

When creating Virtual Devices in **Android Studio Device Manager**, your choice of system image makes an enormous difference in RAM consumption:

| System Image Type | Status | Why? |
| :--- | :---: | :--- |
| **Google APIs** *(Standard 4 KB)* | ✅ **ALWAYS USE (Best)** | **100% Firebase Auth, FCM Push & Maps active** with zero Play Store background updaters. Allows `adb root` so `avdslim` can compact kernel memory. **Runs ultra-smooth at 1536 MB RAM**. |
| **Google Play** | ❌ **AVOID** | Runs heavy Play Store self-updaters and background Play Protect scanning loops. Production build locks out `adb root` (cannot flush kernel caches). Consumes ~40% more RAM. |
| **16 KB Page Size** *(`ps16k`)* | ❌ **AVOID** | Hardcodes a **4,096 MB minimum RAM ceiling in QEMU** (ignoring low-memory flags). Uses 4x larger page buffers. Only use if specifically debugging 16K native C/C++ alignment. |

---

## 🎯 The Problem

When developing Android apps on macOS or Linux, developers often discover `qemu-system-aarch64` consuming **5 GB to 8+ GB of RAM** in Activity Monitor.

### Why Does the Emulator Consume 8 GB?
1. **The Lavapipe Trap**: Android Studio frequently defaults `hw.gpu.mode = auto`, which falls back to Mesa CPU software rasterization (`lavapipe`). This allocates **~4 GB of software rendering buffers** directly in host RAM on top of the guest OS RAM.
2. **16 KB Page Size Images**: On modern ARM64 images (`google_apis_ps16k`), QEMU hardcodes a minimum RAM threshold (`minRam = 4096MB`), silently overriding lower RAM settings.
3. **Android Bloatware**: Over 35 non-essential daemons (Google Assistant, System Intelligence, Maps, Photos, YouTube, telemetry) wake CPU cores and pollute memory.
4. **Stale Snapshots**: A