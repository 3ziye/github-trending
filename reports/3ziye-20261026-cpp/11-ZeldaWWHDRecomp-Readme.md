# The Legend of Zelda: The Wind Waker HD — native port (macOS, Linux, Windows, Android)

A static recompilation of the Wii U version (USA or European) that runs natively on **macOS** (Apple Silicon),
**Linux**, **Windows** and **Android** (arm64; the setup app builds the game on the phone, see
[Android](#android-build-it-yourself)). The
game's PowerPC code is translated to C ahead of time, the Cafe OS libraries the game uses are
reimplemented natively, and GX2 graphics are implemented directly on Metal (macOS) or Vulkan (all
platforms), with no Cemu runtime and no GPU command emulation.

How it works and how it differs from running the game in Cemu: [docs/how-it-works.md](docs/how-it-works.md).

The project has three parts:
- **The port** (this repository): the recompiled game on macOS, Linux, Windows and Android, described below.
- **The decompilation** ([ZeldaWWHDDecomp/wwhd](https://github.com/ZeldaWWHDDecomp/wwhd)): readable C++ source
  for the game's code, each function tested against the original. The port can already run it in an
  experimental **decomp build**, the path towards a fully native source port; see
  [decomp build](#optional-decomp-build-experimental).
- **Mods** ([ZeldaWWHDRecomp/ZeldaWWHDMods](https://github.com/ZeldaWWHDRecomp/ZeldaWWHDMods)): built-in options
  and a catalogue of community mods, installed from inside the game; see [Mods](#mods).

## What's new

**v0.4.0: the world editor and a big Android update.**
- **World editor** (a preview for mod makers): start the game with `--editor` to place the game's villagers,
  enemies, chests, switches, doors and your own models while the game runs, and to build quests, letters, scenes,
  islands and levels of your own. It also works with AI assistants through MCP (off by default).
- **Android:** two-screen handhelds, a heat guard for handhelds with a fan, even frame pacing at 60 fps, code mods
  and dynamic resolution.
- **Faster on every platform**, a 40 fps mode, toon clouds, more comfort options and many fixes.

The changes in each update are in [CHANGELOG.md](CHANGELOG.md) and in the release notes on the
[Releases](https://github.com/ZeldaWWHDRecomp/ZeldaWWHDRecomp/releases) page.

## Legal notice

This is an unofficial fan project. It is not affiliated with, endorsed or sponsored by Nintendo.
"The Legend of Zelda", "The Wind Waker", "Wii U" and related names are trademarks of their
respective owners and are used here only to describe what this software is compatible with.

This repository contains **no game code, no game assets and no keys**: no executable, no
recompiled or disassembled game code, no textures, models, audio, shaders, screenshots or other
material from the game, and no console encryption keys. It contains only the tools and the
runtime written for this project (plus the third-party code listed under Credits).

To use it you need your own, legally obtained copy of the game, dumped from your own Wii U disc
and console. Everything game-specific (the extracted files, the recompiled code in `build/gen/`,
shader caches) is generated locally on your machine from your dump, and must not be
redistributed. The `.gitignore` keeps all of it out of the repository.

## Install (releases)

Releases are portable: unzip, start **Wind Waker HD**, choose your dump. Releases contain only this
project's runtime, tools and setup: **no game files, no game code and no keys**. The game's code can
only exist once it is built from your own dump, so the first start prepares the game once, on your
computer (about two minutes); every later start launches the game directly.

1. Download the zip for your system from the
   [Releases](https://github.com/ZeldaWWHDRecomp/ZeldaWWHDRecomp/releases) page and unzip it anywhere
   (a games folder, an external drive):
   - **macOS**: Apple Silicon, macOS 14 or newer (Metal renderer; Vulkan through MoltenVK, included, can
     be picked in Graphics > Renderer)
   - **Windows**: x86-64 (`windows-x86_64`, Windows 10 version 1903 or newer, or Windows 11) or arm64 (`windows-arm64`, Windows 11 on
     ARM, e.g. Snapdragon X), a GPU with Vulkan 1.3 drivers (or Vulkan 1.1 / 1.2 drivers with
     `VK_KHR_dynamic_rendering`). The arm64 zip runs natively, and only on ARM64 (its setup says so
     on an x86-64 PC). On ARM, 60 fps keeps the game's speed by default (Graphics > "Keep game
     speed"), as on Android: where two frames per step do not fit, in-between frames are skipped
     instead of slowing the whole game down
   - **Linux**: x86-64 (`linux-x86_64`) or arm64 (`linux-aarch64`, e.g. Raspberry Pi 5, Asahi Linux
     on Apple Silicon, other ARM boards and laptops), glibc 2.35 or newer (Ubuntu 22.04+, Debian 12+,
     Fedora 36+, Arch, SteamOS 3, Raspberry Pi OS 12), a GPU with Vulkan 1.3 drivers (or 1.1 / 1.2 with
     `VK_KHR_dynamic_rendering`). Take the zip
     that matches `uname -m` (`x86_64` or `aarch64`); setup says so if it doesn't. Or take the
     single-file **AppImage** (same two architectures)