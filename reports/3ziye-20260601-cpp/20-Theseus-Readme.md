# Theseus

[![build](https://github.com/MrMilenko/Theseus/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/MrMilenko/Theseus/actions/workflows/build.yml)
[![License](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Xbox%20%7C%20macOS%20%7C%20Linux%20%7C%20Windows-lightgrey.svg)](#)

<p align="center">
  <img src="docs/images/vulkan-logo.svg" height="36" alt="Vulkan">
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="docs/images/metal-logo.png" height="36" alt="Metal">
</p>

Six years of reverse engineering the original Xbox dashboard. This repo is the result.

Theseus boots on modded Xbox hardware as a drop in replacement for the stock dashboard. The same engine compiles natively on macOS, Linux, and Windows, where it doubles as **UIX Desktop**: a 3D launcher and media center. The desktop build renders through [bgfx](https://github.com/bkaradzic/bgfx): Metal on macOS, Vulkan on Linux and Windows.

The split is intentional. The Xbox build stays faithful to what you'd expect from the Xbox dashboard (or UIX Lite, if you've used a custom dashboard before). Everything that doesn't belong on an Xbox (Steam libraries, modern video playback, emulator-hosted ISOs, playlists, skin authoring tools) lives on the desktop side instead. Two projects, one engine.

<p align="center">
  <img src="docs/images/xbox-dashboard.png" width="48%" alt="Xbox dashboard">
  <img src="docs/images/desktop-launcher.png" width="48%" alt="UIX Desktop launcher">
</p>
<p align="center">
  <img src="docs/images/media-library.png" width="48%" alt="Media library">
  <img src="docs/images/custom-skin.png" width="48%" alt="Custom skin">
</p>
<p align="center">
  <img src="docs/images/steam-tab.png" width="48%" alt="Steam tab in Title Maker">
  <img src="docs/images/retroarch-tab.png" width="48%" alt="RetroArch tab in Title Maker">
</p>

## On Xbox

A drop-in replacement for the stock Xbox dashboard on modded consoles. Same look and behavior, because that's what it is. Rebuilt plank by plank and still going.

What works:
- Every original scene, animation, and skin slot
- UIX Lite skins drop in unchanged. Skin authors don't have to do anything
- Hot swap skins from settings, no reboot
- ISO / CCI launching from the harddrive menu, plus the original XBE flow
- Hundreds of titles scan in milliseconds
- Title icons auto populate from each game's XBE certificate
- Quick overlay (LT + B) for ISO loader, file manager, FTP / drive widgets
- FTP server, recovery / panic screen, MP3 soundtrack playback

[Download for Xbox ->](https://github.com/MrMilenko/Theseus/releases) (or build from source, see below)

## On the desktop (UIX Desktop)

UIX Desktop is the Theseus engine compiled for your computer, with the modern features bolted on. macOS, Linux, Windows, Steam Deck friendly.

- **3D launcher** for native PC games, Steam libraries, RetroArch ROMs, and Xbox ISOs via [xemu](https://xemu.app)
- **Media library** that scans your Movies and TV folders, pulls posters from [TMDB](https://www.themoviedb.org/), plays back through libmpv
- **Skin editor** with live XAP scripting and a scene inspector. Change a skin, see it instantly
- **Title Maker** for adding games and apps, with per launcher import flows for Steam and RetroArch
- **Xbox HDD browser** that opens qcow2 and FATX images
- **CRT post process** for the old TV look. Scanlines, curvature, phosphor, bloom, all tunable
- **Graphics knobs** in Settings -> Display: vsync mode, FPS cap, MSAA, hardware video decode
- **Controllers**: Xbox and PlayStation pads via SDL2

[Download for desktop ->](https://github.com/MrMilenko/Theseus/releases)

## Quick Start

### Xbox

1. Grab the latest Xbox release (`default.xbe` + `uixdata/`)
2. Drop the XBE somewhere on the Xbox HDD, e.g. `E:\Dashboards\Theseus\default.xbe`
3. Copy `uixdata/` next to it
4. Copy `Configs/` to `C:\UIX Configs\`
5. Boot it. If something's missing, the panic screen tells you what.

### Desktop

1. Grab the release for your OS
2. Run it. That's it.

The Windows release ships with the DLLs it needs. macOS and Linux dynamically link to system libraries, so you'll want these installed:

**macOS (Homebrew):**
```
brew install sdl2 sdl2_mixer mpv curl
```

**Linux (Debian / Ubuntu):**
```
sudo apt install libsdl2-2.0-0 libsdl2-mixer-2.0-0 libmpv2 libcurl4
```

(Some distros ship `libmpv1` instead of `libmpv2`. Either works.)

If you'd rather build from source, jump down to [Building](#building).

## Adding games

Title Maker (F3 from the dashboard) is where you connect games to dashboard tiles. Three tabs:

**Main** is the catch all. Every title you've added shows up here, regardless of which tab created it. This is also where you add the weird stuff that doesn't belong to a launcher: a Windows .exe, a .bat script, a macOS .command file, a shell one liner, anything that takes a path or command. Edit names, swap icons, tweak the launch line. Most of your time mana