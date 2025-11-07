# wayscriber

> TL;DR: wayscriber is a ZoomIt-like screen annotation tool for Wayland compositors, written in Rust.
> Works on compositors with the wlr-layer-shell protocol (Hyprland, Sway, river, …); building from source requires Rust 1.85+.
> Quick start: [set it up in four steps](#quick-start).

<details>
<summary>📹 Demo Video (Click to expand)</summary>

https://github.com/user-attachments/assets/7c4b36ec-0f6a-4aad-93fb-f9c966d43873

</details>

<details>
<summary>🖼️ Demo GIF (Click to expand)</summary>

![Demo GIF](https://github.com/user-attachments/assets/e99eb161-c603-4133-926b-79de7a8fb567)

</details>

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Rust](https://img.shields.io/badge/rust-1.85%2B-orange.svg)

- [Why wayscriber?](#why-wayscriber)
- [Quick Start](#quick-start)
- [Features at a Glance](#features-at-a-glance)
- [Demo](#demo)
- [Installation](#installation)
- [Running wayscriber](#running-wayscriber)
- [Controls Reference](#controls-reference)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Additional Information](#additional-information)
- [Project History](#project-history)
- [Contributing & Credits](#contributing--credits)

## Why wayscriber?

- Works across Wayland compositors (Sway, Wayfire, River, Hyprland, …) via wlr-layer-shell. Tested extensively on Hyprland and confirmed working on Niri; reports from other compositors welcome.
- Built for live presentations, classroom sessions, and screenshares - toggle with a key and annotate your screen instantly without breaking flow.
- Complements tools like [Satty](https://github.com/gabm/Satty): Satty excels at capture → annotate → save workflows, while wayscriber stays resident as an always-available drawing layer with instant mode switching.

## Quick Start

**1. Install wayscriber**
1. Arch Linux (AUR):  (build from source)
	- `yay -S wayscriber` 
	- `paru -S wayscriber` 
2. Arch Linux (AUR, prebuilt): 
	- `yay -S wayscriber-bin` 
	- `paru -S wayscriber-bin`.
3. Other distros: see [Installation](#installation), then install `wl-clipboard`, `grim`, and `slurp` for the fastest screenshot workflow.

**2. Choose how to run it:**

### Option 1: One-Shot Mode (Simple)
Launch wayscriber when you need it, exit when done:

```bash
wayscriber --active
```

Or bind to a key in `~/.config/hypr/hyprland.conf`:
```conf
bind = SUPER, D, exec, wayscriber --active
```

Press `F10` for help, `F11` for configurator, `Escape`/`Ctrl+Q` to exit, and `F12` to toggle the status bar.

### Option 2: Daemon Mode (Background Service)
Run wayscriber in the background and toggle it with a keybind:

**Enable the service:**
```bash
systemctl --user enable --now wayscriber.service
```

**Add keybinding** to `~/.config/hypr/hyprland.conf`:
```conf
bind = SUPER, D, exec, pkill -SIGUSR1 wayscriber
```

**Reload Hyprland:**
```bash
hyprctl reload
```

**Note:** If the daemon doesn't start after a reboot, see [Troubleshooting](#daemon-not-starting-after-reboot).

**Alternative:** Use Hyprland's exec-once instead of systemd:
```conf
exec-once = wayscriber --daemon
bind = SUPER, D, exec, pkill -SIGUSR1 wayscriber
```

## Features at a Glance

- **Drawing & editing**: Freehand pen, straight lines, rectangles, ellipses, arrows, and multiline text with smoothing; undo & redo; quick line-width and color changes via hotkeys or scroll.
- **Board modes**: Whiteboard, blackboard, and transparent overlays, each with isolated frames and auto pen contrast; snap back to transparent with `Ctrl+Shift+T`.
- **Capture shortcuts**: Full-screen saves, active-window grabs, and region capture to file or clipboard using `grim`, `slurp`, and `wl-clipboard` when available.
- **Session persistence**: Opt-in per board/monitor storage that restores your canvas plus pen color & thickness; inspect with `wayscriber --session-info` or clear with `wayscriber --clear-session`.
- **Workflow helpers**: Background daemon with SIGUSR1 toggle, tray icon, one-shot mode, live status bar, and in-app help overlay (`F10`).
- **Click highlights**: Presenter-style halo on mouse clicks with configurable colors, radius, and duration; follows your pen color by default, toggle the effect with `Ctrl+Shift+H` or swap to highlight-only mode with `Ctrl+Alt+H`.
- **Configurator & CLI**: Launch `wayscriber-configurator` (or press `F11`) to tweak colors, bindings, persistence, compression, and more; power users can edit the TOML or use CLI switches.
- **Performance & reliability**: Dirty-region rendering keeps redraws fast, while session files use atomic writes, size limits, compression, and backups for safety.

### Session Persistence

Wayscriber can remember your boards between runs (per monitor and per board color) along with pen color/thickness. Persistence is opt-in. Toggle it from the configurator (`F11 → Session` tab) or launch the GUI directly:

```bash
wayscriber-configurator
```

Prefer text? Edit `~/.config/wayscriber/config.toml`. Helpful commands:

```bash
wayscriber --se