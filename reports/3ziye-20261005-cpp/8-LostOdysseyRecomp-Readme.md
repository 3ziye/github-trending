<div align="center">

<img src="assets/lost-odyssey-recomp.png" alt="Lost Odyssey Recomp logo" width="112">

# Lost Odyssey Recomp

**An experimental native PC port of Lost Odyssey for Xbox 360.**

[![Latest release](https://img.shields.io/github/v/release/freefrank/LostOdysseyRecomp?label=release)](https://github.com/freefrank/LostOdysseyRecomp/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/freefrank/LostOdysseyRecomp/total?label=downloads)](https://github.com/freefrank/LostOdysseyRecomp/releases)
[![Stars](https://img.shields.io/github/stars/freefrank/LostOdysseyRecomp?style=flat)](https://github.com/freefrank/LostOdysseyRecomp/stargazers)
[![License: GPL-3.0](https://img.shields.io/badge/license-GPL--3.0-blue)](LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/freefrank/LostOdysseyRecomp?label=last%20commit)](https://github.com/freefrank/LostOdysseyRecomp/commits/main)
[![Open issues](https://img.shields.io/github/issues/freefrank/LostOdysseyRecomp?label=issues)](https://github.com/freefrank/LostOdysseyRecomp/issues)
[![Support on Ko-fi](https://img.shields.io/badge/Ko--fi-support-FF5E5B?logo=kofi&logoColor=white)](https://ko-fi.com/dotslash)

![Windows x64](https://img.shields.io/badge/Windows-x64-0078D6)
![Linux x64](https://img.shields.io/badge/Linux-x64-FCC624?logo=linux&logoColor=black)
![macOS arm64 (experimental)](https://img.shields.io/badge/macOS-arm64%20%28experimental%29-000000?logo=apple&logoColor=white)
![Android arm64 (experimental)](https://img.shields.io/badge/Android-arm64%20%28experimental%29-3DDC84?logo=android&logoColor=white)
![Direct3D 12](https://img.shields.io/badge/Direct3D-12-5E5E5E)
![Vulkan](https://img.shields.io/badge/Vulkan-AC162C?logo=vulkan&logoColor=white)
![Metal](https://img.shields.io/badge/Metal-147EFB)

### [Download](https://github.com/freefrank/LostOdysseyRecomp/releases/latest) · [Installation guide](docs/INSTALLING.md) · [简体中文](README.zh-CN.md)

[Changelog](CHANGELOG.md) · [Report an issue](https://github.com/freefrank/LostOdysseyRecomp/issues) · [Project board](https://github.com/users/freefrank/projects/3) · [Build from source](docs/BUILDING.md)

</div>

> [!IMPORTANT]
> **The port is still in early testing.** Opening areas and selected scenes have been tested; a complete playthrough has not. Rendering and stability issues remain. Supply your own supported game files.

## Contents

- [Start playing](#start-playing)
  - [macOS (experimental)](#macos-experimental)
  - [Android (experimental)](#android-experimental)
  - [HDR (experimental)](#hdr-experimental)
  - [Latest changes](#latest-changes)
- [Current features](#current-features)
- [Controls](#controls)
- [Debug menu](#debug-menu)
  - [Overview: captures and game actions](#overview-captures-and-game-actions)
  - [Teleport: positions within the current map](#teleport-positions-within-the-current-map)
  - [Cheats: speed and game-data tools](#cheats-speed-and-game-data-tools)
- [Files and folders](#files-and-folders)
- [Command-line options](#command-line-options)
- [Reporting a problem](#reporting-a-problem)
- [In-game screenshots](#in-game-screenshots)
- [Development](#development)
- [Sponsors](#sponsors)
- [Credits and game data](#credits-and-game-data)

## Start playing

Choose a package from the [latest release](https://github.com/freefrank/LostOdysseyRecomp/releases/latest). The current published version is **v0.8.21**.

| Platform | Package | First launch |
| :--- | :--- | :--- |
| Windows x64 | `LostOdysseyRecomp-windows-x64-v0.8.21.zip` | Extract the whole ZIP to a writable folder and run `LostOdysseyRecomp.exe`. Needs a CPU with AVX. |
| Linux x64 | `LostOdysseyRecomp-linux-x64-v0.8.21.AppImage` | Make it executable with `chmod +x`, then run it. |
| Linux x64 | `LostOdysseyRecomp-linux-x64-v0.8.21.flatpak` | Install the Freedesktop 26.08 runtime, then the bundle ([commands](docs/INSTALLING.md#flatpak)). |
| macOS arm64 (experimental) | `LostOdysseyRecomp-macos-arm64-v0.8.21.dmg` | Drag `LostOdysseyRecomp.app` to Applications. Needs an Apple Silicon Mac with macOS 15 or later. See [macOS](#macos-experimental) for the first launch. |
| Android arm64 (experimental) | `LostOdysseyRecomp-android-arm64-v0.8.21.apk` | Install the APK and open it once. Needs a 64-bit Android 8.0+ device with Vulkan. See [Android](#android-experimental). |

1. **Import your game data.** The importer opens when no game is found. Use **Files** or **Folder** to select an extracted game folder, `default.xex`, an ISO or GOD data.
2. **Choose the languages and graphics options.** On the first start the game offers to download precompiled shaders for your renderer; if you skip, it compiles them on your PC once.
3. **Add the other discs and DLC when you need them** in Settings → **Gameplay → Import discs & DLC**. With all four discs imported, the game switches discs on its own.

Disc 1 is required to start. Use one of the supported four-disc sets (Asian multilingual or USA/Europe) and don't mi