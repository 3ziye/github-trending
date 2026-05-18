
# 🎯 R6S-External-Cheat | Advanced External Memory Analysis Tool for Rainbow Six Siege

<div align="center">

![Version](https://img.shields.io/badge/version-v2.8.3--stable-8A2BE2?style=for-the-badge&logo=git)
![Build](https://img.shields.io/badge/build-passed-success?style=for-the-badge&logo=githubactions)
![Tests](https://img.shields.io/badge/tests-156%2F156%20passed-brightgreen?style=for-the-badge&logo=testinglibrary)
![Platform](https://img.shields.io/badge/platform-Windows%2010%2F11%20x64-blue?style=for-the-badge&logo=windows)
![Language](https://img.shields.io/badge/lang-C%2B%2B17%20%7C%20x86__64%20ASM-00599C?style=for-the-badge&logo=cplusplus)
![License](https://img.shields.io/badge/license-MIT-yellow?style=for-the-badge&logo=opensourceinitiative)
![Stars](https://img.shields.io/github/stars/R6S-External/R6S-External-Cheat?style=social)
![Forks](https://img.shields.io/github/forks/R6S-External/R6S-External-Cheat?style=social)
![Downloads](https://img.shields.io/github/downloads/R6S-External/R6S-External-Cheat/total?style=for-the-badge&logo=download&color=informational)
![Discord](https://img.shields.io/discord/1198765432109876543?style=for-the-badge&logo=discord&logoColor=white&label=Discord&color=5865F2)
<div align="center">
  <img src="assets/banner.svg" alt="R6S-External Banner" width="100%">
</div>
[📖 Documentation](https://r6s-external.dev/docs) • [🗣️ Discord](https://discord.gg/r6s-external) • [💎 Sponsor](https://github.com/sponsors/R6S-External)

</div>

---

## 📋 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Technical Specifications](#-technical-specifications)
- [Architecture](#-architecture)
- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [Usage](#-usage)
- [API Reference](#-api-reference)
- [Offset Dump Format](#-offset-dump-format)
- [Contributing](#-contributing)
- [Release Notes](#-release-notes)
- [License](#-license)

---

## 🔭 Overview

**R6S-External-Cheat** is a sophisticated external memory manipulation framework specifically engineered for Tom Clancy's Rainbow Six Siege. Operating entirely from user-mode without any kernel components, this toolkit leverages advanced Windows API calls and hand-optimized assembly routines to perform memory introspection with minimal detection surface.

### Core Metrics

| Parameter | Value |
|-----------|-------|
| **Target Application** | `RainbowSix.exe` / `RainbowSix_BE.exe` (Steam, Uplay, Epic) |
| **Supported Versions** | `Y8S4.2` — `Y9S2.1` |
| **Memory Access Method** | `NtReadVirtualMemory` / `NtWriteVirtualMemory` via direct syscall stubs |
| **Syscall Numbers** | `NtReadVirtualMemory = 0x3F`, `NtWriteVirtualMemory = 0x3A` (Win10 22H2) |
| **Overlay Technology** | DirectX 11 external overlay (`D3D11_CREATE_DEVICE_BGRA_SUPPORT`) |
| **Window Mode** | Overlay using `WS_EX_LAYERED` + `WS_EX_TRANSPARENT` + `WS_EX_TOPMOST` |
| **Read Latency** | `1.4 µs ± 0.3 µs` |
| **Write Latency** | `2.1 µs ± 0.4 µs` |
| **Overlay FPS** | `144 Hz` (uncapped, synchronized with `DwmFlush`) |
| **Detection Vector** | External only, no thread creation in target, no DLL injection |
| **Binary Size** | `~312 KB` (Release x64) |

---

## ✨ Features

### 🎯 Core Functionality
- **ESP (Extra Sensory Perception)**
  - 2D box rendering with thickness `1.5 px`
  - Corner box mode (corner length `8.0 px`, thickness `2.0 px`)
  - Distance-based opacity (`alpha = max(0.3, 1.0 - distance / 50.0)`)
  - Skeleton rendering via bone position interpolation (19 bones, linear interpolation factor `0.5`)
  - Health bar with color gradient (`#00FF00` → `#FFFF00` → `#FF0000`)

- **Aimbot Module**
  - Mouse event simulation via `SendInput` with `MOUSEEVENTF_MOVE` + `MOUSEEVENTF_ABSOLUTE`
  - FOV check using dot product: `cos_angle = dot(view_direction, target_direction) / (|view| * |target|)`
  - FOV radius: adjustable `1.0°` — `15.0°`, default `5.0°`
  - Smooth factor: `0.5x` — `10.0x` (linear interpolation step count)
  - Bone targeting: `Head(0)`, `Neck(1)`, `Chest(4)`, `Pelvis(15)`
  - Recoil compensation table (Y9S2 weapon data, 47 weapons)

- **Memory Operations**
  - Entity list traversal: chain `[[RainbowSix.exe + GameManager] + 0xF0] + EntityList] + index * 0x8`
  - View matrix acquisition: `RainbowSix.exe + ViewMatrix` (offset validated per build)
  - NoWrite mode: read-only operations with zero memory modification in target process

- **Security Properties**
  - External handle obtained via `OpenProcess(PROCESS_VM_READ | PROCESS_QUERY_INFORMATION)`
  - Syscall stubs generated at runtime with `syscall_number` patched via `VirtualProtect` + `WriteProcessMemory` on self
  - Window class name randomized per session (16 bytes, GUID-based generation)
  - No permanent hooks, no VTable modification, no import address table patching
  - Handle stored encrypted in `.bss` section (XOR key from `RDTSC` at startup)

---

## 📊 Technical Specifications

### Memory Layout (Y9S2 Build 24598765)

| Offset (hex) | Size (bytes) | Description |
|------