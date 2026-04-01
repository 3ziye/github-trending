```
 ██╗   ██╗ ██████╗ ███████╗██████╗ ███████╗██████╗
 ██║   ██║╚════██╗██╔════╝██╔══██╗██╔════╝██╔══██╗
 ██║   ██║ █████╔╝███████╗██████╔╝█████╗  ██████╔╝
 ╚██╗ ██╔╝ ╚═══██╗╚════██║██╔═══╝ ██╔══╝  ██╔══██╗
  ╚████╔╝ ██████╔╝███████║██║     ███████╗██║  ██║
   ╚═══╝  ╚═════╝ ╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝
```

# V3SP3R — The AI Brain for Your Flipper Zero

> **Talk to your Flipper Zero like it's your partner-in-hacking.** Vesper turns your pocket hacking tool into an AI-powered command center — controlled entirely through natural language from your Android device or smart glasses.

No menus. No manuals. Just natural language prompting.

[![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-blue.svg)](LICENSE)
[![Android](https://img.shields.io/badge/Android-8.0%2B-green.svg)](https://developer.android.com)
[![Kotlin](https://img.shields.io/badge/Kotlin-2.2-purple.svg)](https://kotlinlang.org)

---

## Why Vesper?

The Flipper Zero is one of the most versatile hardware hacking tools ever made — but navigating its menus, managing files, and crafting signals by hand is tedious. **Vesper eliminates the friction.** Plug in an AI brain via OpenRouter, connect over Bluetooth, and you have a voice-commanded hardware lab in your pocket.

- **Instant expertise** — Don't memorize SubGHz protocols or IR formats. Just say what you want.
- **Real-time control** — The AI reads your Flipper's state, executes commands, and reports back in seconds.
- **Multimodal input** — Voice commands, photo analysis, and text chat. Use your phone camera or smart glasses to show the AI what you're looking at.
- **Signal alchemy** — Build, layer, and export custom RF waveforms with a visual editor.
- **Smart glasses integration** — Pair with Mentra smart glasses for hands-free, heads-up Flipper control.
- **Safety-first architecture** — Every AI action is risk-classified. Destructive operations require explicit confirmation. System paths are locked by default.

Whether you're a security researcher, a red teamer, a CTF competitor, a hardware tinkerer, or just someone who wants to understand the invisible signals around you — Vesper makes the Flipper Zero *dramatically* more accessible and more powerful.

---

## Features

### Chat — AI-Driven Flipper Control
Talk to your Flipper in plain English (voice or text):
- *"Show me my SubGHz captures"*
- *"What's my battery level?"*
- *"Create a backup of all my IR remotes"*
- *"Generate a BadUSB script that opens a reverse shell"*
- *"Change the frequency in garage.sub to 315MHz"*

### Hardware Control
Direct control over all Flipper subsystems:
- **SubGHz** — Transmit and analyze RF signals
- **Infrared** — Send and record IR commands
- **NFC / RFID / iButton** — Emulate stored credentials
- **BadUSB** — Execute HID attack scripts
- **GPIO / LED / Vibro** — Control hardware peripherals
- **App Launcher** — Start any Flipper app by name

### Multimodal Input
- **Voice input** — Speak commands using on-device speech recognition
- **Photo analysis** — Snap a picture of a remote, a device label, or anything — the AI sees what you see
- **Text-to-speech** — AI responses read aloud via OpenRouter TTS
- **Smart glasses** — Hands-free voice + camera via Mentra glasses bridge

### Ops Center
Built for reliability-obsessed users:
- **Pipeline Health** — BLE/RPC/CLI readiness and diagnostics at a glance
- **Runbooks** — One-tap recovery and smoke-test sequences
- **Live Status** — Transport and command pipeline behavior in one view

### Alchemy Lab — Signal Synthesis
Build custom RF signals from scratch:
- Visual waveform editor with real-time preview
- Layer and fuse multiple signal patterns
- Export directly to your Flipper's SD card

### Payload Lab
AI-powered payload generation:
- BadUSB scripts, SubGHz signals, IR remotes, NFC tags
- Validated before deployment — the AI checks format and safety
- Direct push to Flipper storage

### FapHub Browser
Browse and install Flipper applications:
- Search the Flipper app catalog
- One-tap install to your device

### Resource Browser
Find and download community resources:
- Search GitHub for Flipper-compatible files
- Browse repositories and download directly to your Flipper

### Device Manager
Full Flipper visibility:
- Battery, storage, firmware info, and connection status
- Scan, pair, and manage BLE connections
- Direct file browsing and management

### Risk & Permissions Engine
Every AI action is classified before execution:
- **Low risk** — Read-only ops execute automatically
- **Medium risk** — File writes show a diff for review
- **High risk** — Destructive ops require double-tap confirmation
- **Blocked** — System/firmware paths require explicit unlock

Configure **auto-approve** per risk tier in Settings to move faster when you trust the workflow.

### Audit Log
Every action the AI takes is logged:
- Full history of commands, results, and approvals
- Filterable by action type and session
- Exportable for compliance and review

---

## Re