> [!WARNING]
> **OpenLogi is under active development** and not yet stable — features and config may still change. Give the repo a **Star** ⭐ and **Watch** 👀 it to get notified the moment a release lands.

<h4 align="right"><strong>English</strong> | <a href="docs/README.zh-CN.md">简体中文</a> | <a href="docs/README.ja.md">日本語</a> | <a href="docs/README.de.md">Deutsch</a> | <a href="docs/README.fr.md">Français</a> | <a href="docs/README.ko.md">한국어</a></h4>

<p align="center">
    <img src="https://assets.openlogi.org/brand/openlogi-icon.png" width="138" alt="OpenLogi"/>
</p>

<h1 align="center">OpenLogi</h1>
<p align="center"><strong>⚡️ A native, local-first alternative to Logitech Options+, written in Rust 🦀<br/>Remap buttons, DPI, and SmartShift over HID++. No account, no telemetry.</strong></p>


<div align="center">
    <a href="https://twitter.com/AprilNEA" target="_blank">
    <img alt="twitter" src="https://img.shields.io/badge/follow-AprilNEA-green?style=social&logo=Twitter"></a>
    <a href="https://t.me/+VDtkR5OSAT04NzVh" target="_blank">
    <img alt="telegram" src="https://img.shields.io/badge/chat-telegram-blueviolet?style=flat&logo=Telegram"></a>
    <a href="https://github.com/AprilNEA/OpenLogi/releases" target="_blank">
    <img alt="GitHub downloads" src="https://img.shields.io/github/downloads/AprilNEA/OpenLogi/total.svg?style=flat"></a>
    <a href="https://github.com/AprilNEA/OpenLogi/commits" target="_blank">
    <img alt="GitHub commit" src="https://img.shields.io/github/commit-activity/m/AprilNEA/OpenLogi?style=flat"></a>
    <img alt="Hits" src="https://hits.aprilnea.com/hits?url=https://github.com/aprilnea/openlogi">
</div>

> **Options+ ? Try OpenLogi.**

Remap buttons, drive DPI and SmartShift, and switch profiles per app — without a Logitech account, telemetry, or the official Options+ install. No cloud, plain TOML config; the only network calls are device-image fetches and an opt-in, off-by-default update check.

---

## What it is

OpenLogi talks to Logitech HID++ mice over a Logi Bolt receiver — or a
Bluetooth-direct / wired connection — without running Logi Options+. It ships
two binaries:

- **[OpenLogi GUI](crates/openlogi-gui)** — a GPUI desktop app: an interactive mouse diagram with clickable hotspots, a per-button action picker (41 built-in actions plus custom keyboard shortcuts authored in the TOML config), DPI presets, a SmartShift panel (wheel mode, sensitivity, permanent ratchet), per-application profile overlays, a device carousel that switches between paired devices live, and a Settings window with a UI localized into 20 languages.
- **[OpenLogi CLI](crates/openlogi-cli)** — a CLI for headless inventory (`list`) plus asset-sync and on-device diagnostic subcommands.

Everything is local: bindings live in a plain TOML file, button presses are remapped through the OS event tap, and DPI / SmartShift changes are written straight to the device over HID++.

macOS and Linux are supported. Windows is an early, untested preview — signed
builds ship with each release; see [Roadmap](#roadmap).

## Beyond Options+

Things OpenLogi does that Options+ won't:

- **Run on Linux.** Options+ ships for macOS and Windows only. OpenLogi treats
  Linux as a first-class platform: evdev/uinput hook, udev rules, a systemd
  user unit, and `.deb` / `.rpm` packages.
- **Move the Gesture Button.** Pick which physical button owns the gesture
  role — thumb pad, middle, back, or forward — with per-direction swipe
  bindings, or turn gestures off entirely. Options+ pins the gesture role to
  the dedicated thumb pad.
- **Keep config in plain text.** Everything is one TOML file you can read,
  diff, version-control, and copy between machines.
- **Script it.** A real CLI: device inventory, asset prefetch, and on-device
  HID++ diagnostics (feature dump, DPI / SmartShift round-trips).
- **Stay light.** Native Rust + GPUI binaries — no Electron suite, no resident
  updaters, no account, no telemetry.

## Roadmap

| Capability | State |
|---|---|
| Discover Bolt receivers + list paired devices (CLI + GUI) | ✅ |
| Unifying receivers (older protocol, replaced by Bolt) | ✅ |
| Bluetooth-direct / wired devices (no receiver) | ✅ |
| Battery percentage / charge state | ✅ (online devices) |
| Interactive GUI: carousel, mouse diagram, action picker | ✅ macOS + Linux |
| Button remapping via the OS event tap / evdev hook | ✅ macOS + Linux |
| 41-action catalog + custom keyboard shortcuts (TOML-authored) | ✅ macOS + Linux¹ |
| DPI control + presets + Cycle / Set-preset actions (HID++ `0x2201`) | ✅ |
| SmartShift wheel: mode toggle + sensitivity + permanent-ratchet panel (HID++ `0x2111`) | ✅ |
| Per-application profile overlays (auto-switch on app focus) | ✅ macOS, 🟡 Linux (X11 only) |
| Settings window: launch-at-login, update check, menu-bar, permissions, language | ✅ macOS + Linux |
| Interface localization (20 languages: da, de, el, en, es, fi, fr, it, ja, ko, nb, nl, pl, pt-BR, pt-PT, ru, sv, zh-CN, zh-HK, zh-TW