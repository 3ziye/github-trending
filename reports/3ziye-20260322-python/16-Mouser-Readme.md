# Mouser — Logitech Mouse Remapper

<p align="center">
  <img src="images/logo_icon.png" width="128" alt="Mouser logo" />
</p>

A lightweight, open-source, fully local alternative to **Logitech Options+** for
remapping Logitech HID++ mice. The current best experience is on the **MX Master**
family, with early detection and fallback UI support for additional Logitech models.

No telemetry. No cloud. No Logitech account required.

---

## Features

- **macOS support** — full macOS compatibility using CGEventTap for mouse hooking, Quartz CGEvent for key simulation, and NSWorkspace for app detection. See [macOS Setup Guide](readme_mac_osx.md) for details.
- **macOS start at login** — manages a per-user LaunchAgent from the UI, with an optional "Launch hidden after login" mode for menu-bar startup
- **Remap supported programmable controls** — MX Master-family layouts expose middle click, gesture button, back, forward, and horizontal scroll actions
- **Per-application profiles** — automatically switch button mappings when you switch apps (e.g., different bindings for Chrome vs. VS Code)
- **Desktop navigation actions** — includes previous/next desktop switching on both platforms, plus Mission Control, App Expose, Launchpad, and Show Desktop on macOS
- **Platform-aware built-in actions** across navigation, browser, editing, and media categories
- **DPI / pointer speed control** — slider from 200–8000 DPI with quick presets, synced to the device via HID++
- **Scroll direction inversion** — independent toggles for vertical and horizontal scroll
- **Device-aware HID++ gesture support** — discovers `REPROG_CONTROLS_V4`, ranks gesture candidates per device, and diverts the best control it can find
- **Auto-reconnection** — automatically detects when the mouse is turned off/on or disconnected/reconnected and restores full functionality without restarting the app
- **Live connection status** — the UI shows a real-time "Connected" / "Not Connected" badge that updates as the mouse connects or disconnects
- **Device-aware Qt Quick UI** — interactive MX Master layout today, plus a generic fallback card and experimental manual map picker for other detected devices
- **System tray / menu bar** — runs in background, hides on close, and exposes quick open / toggle / quit actions
- **Auto-detect foreground app** — polls the active window and switches profiles instantly
- **Zero external services** — config is a local JSON file, all processing happens on your machine

## Screenshots

<p align="center">
  <img src="images/Screenshot.png" alt="Mouser UI" />
</p>

_The UI is now device-aware. MX Master-family mice get the interactive diagram; other detected Logitech mice fall back to a generic device card with an experimental map override picker._

## Current Device Coverage

| Family / model | Detection + HID++ probing | UI support |
|---|---|---|
| MX Master 3S / 3 / 2S / MX Master | Yes | Dedicated interactive `mx_master` layout |
| MX Anywhere 3S / 3 / 2S | Yes | Generic fallback card, experimental manual override |
| MX Vertical | Yes | Generic fallback card |
| Unknown Logitech HID++ mice | Best effort by PID/name | Generic fallback card |

> **Note:** Only the MX Master family currently has a dedicated visual overlay. Other devices can still be detected, show their model name in the UI, and try the experimental layout override picker, but button positions may not line up until a real overlay is added.

## Default Mappings

| Button | Default Action |
|---|---|
| Back button | Alt + Tab (Switch Windows) |
| Forward button | Alt + Tab (Switch Windows) |
| Middle click | Pass-through |
| Gesture button | Pass-through |
| Horizontal scroll left | Browser Back |
| Horizontal scroll right | Browser Forward |

## Available Actions

Action labels adapt by platform. For example, Windows exposes `Win+D` and `Task View`, while macOS exposes `Mission Control`, `Show Desktop`, `App Expose`, and `Launchpad`.

| Category | Actions |
|---|---|
| **Navigation** | Alt+Tab, Alt+Shift+Tab, Show Desktop, Previous Desktop, Next Desktop, Task View (Windows), Mission Control (macOS), App Expose (macOS), Launchpad (macOS) |
| **Browser** | Back, Forward, Close Tab (Ctrl+W), New Tab (Ctrl+T) |
| **Editing** | Copy, Paste, Cut, Undo, Select All, Save, Find |
| **Media** | Volume Up, Volume Down, Volume Mute, Play/Pause, Next Track, Previous Track |
| **Other** | Do Nothing (pass-through) |

---

## Download & Run

> **No install required.** Just download, extract, and double-click.

<p align="center">
  <a href="https://github.com/TomBadash/Mouser/releases/latest">
    <img src="https://img.shields.io/badge/Download-Mouser.zip-00d4aa?style=for-the-badge&logo=windows" alt="Download" />
  </a>
  <img src="https://img.shields.io/github/downloads/TomBadash/Mouser/total?style=for-the-badge&color=00d4aa&label=Total%20Downloads" alt="Downloads" />
</p>

### Steps

1. Go to the [**latest release page**](https://github.com/TomBadash/Mouser/releases/latest)
2. Cl