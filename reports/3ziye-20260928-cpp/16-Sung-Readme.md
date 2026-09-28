<div align="center">

<img src="assets/readme-now-playing.png" alt="Sung playing a song, the cover in a flower shape ringed by the visualizer" width="100%">

<a href="https://buymeacoffee.com/e_gurl">
  <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Support Sung on Buy Me a Coffee" width="217" height="60">
</a>

# Sung

**YouTube Music, your music files, and your music server. Native on Linux.**

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Linux](https://img.shields.io/badge/platform-Linux-blue.svg)
![Qt 6](https://img.shields.io/badge/built_with-Qt_6-41CD52.svg)

A minimal Material 3 player built with C++ and Qt Quick, designed for CachyOS and Wayland.

[Install](#install) · [Features](#features) · [Development](#development)

</div>

## Features

- **YouTube Music**: search songs, albums, artists and playlists; play audio without an embedded browser or ad interface, at standard quality or a data saver setting.
- **Navidrome / Subsonic**: browse and search your server, play original or transcoded audio, edit server playlists, rate songs, sync favorites and listening history, and display server lyrics.
- **Jellyfin**: browse music libraries, albums, artists and genres; search, stream original or transcoded audio, manage permitted server playlists, sync favorites and display synchronized lyrics.
- **Apple Music through Cider**: browse your Apple Music library, search Apple's catalogue and play it through [Cider](https://cider.sh), with Sung's queue, lyrics, history and animated covers.
- **Your music**: import FLAC, MP3 and other supported audio files or folders; browse albums and artists, search paths and group songs by folder. Mix local and YouTube songs in the same playlists.
- **Animated artwork**: local animated covers and automatic online covers for matching YouTube songs, shared across the player, immersive view and mini player; lists use still covers.
- **Appearance**: light and dark themes, a pickable Material accent color, artwork-derived color, an ambient cover backdrop, density and per-view layouts.
- **Lyrics**: synchronized lyrics, an immersive view, optional poster-style lines, timing adjustments, LRC import, seek previews and search with jump-to-line playback.
- **Offline**: songs you have played are kept on disk under a limit you set, so a replay starts at once and needs no network.
- **Library tools**: likes, listening history, smart mixes, custom smart playlists, M3U playlist import and export, custom playlist covers, playlist cleanup, multi-selection, drag reordering and Undo.
- **Playback controls**: mini player, queue editing with source headings, an immersive up-next carousel, volume normalization, shuffle, repeat, sleep timer, playback speed and audio-device selection.
- **Keyboard and assistive use**: every control takes focus and shows it, sections are marked as headings, and colors are solved to keep 4.5:1 contrast in both themes and at either contrast setting.
- **Desktop integration**: media keys through MPRIS, optional notifications, light/dark themes and Noctalia palette support.

Native rendering and bounded artwork caches keep Sung lightweight. Animated covers share one additional decoder, released when the player is hidden. Animations can be disabled in Settings.

## Install

### CachyOS / Arch Linux

Install the build and runtime dependencies:

```bash
sudo pacman -S --needed git base-devel cmake ninja python nodejs ffmpeg qt6-base qt6-declarative qt6-multimedia qt6-svg qt6-wayland qt6-imageformats
```

Download and install Sung:

```bash
git clone https://github.com/yappologistic/Sung.git
cd Sung
./scripts/install.sh
```

Open **Sung** from your application menu, or run:

```bash
~/.local/bin/sung
```

Installation is per-user in `~/.local`; do not run the install script with `sudo`. Python dependencies are installed in an isolated environment. Internet access is needed during installation and for YouTube playback.

### Other Linux distributions

Install the equivalent development packages for **Qt 6.8+** (Core, Gui, Quick, Qml, QuickControls2, Multimedia, Network, DBus, Svg and Wayland), a C++20 compiler, CMake 3.24+, Ninja, Python 3 with `venv`/`pip`, Node.js 20+ and FFmpeg. Install the Qt image-format plugins for WebP artwork. Then follow the clone and install commands above.

Sung uses Google Sans Flex when installed and otherwise falls back to a system font. Noctalia is optional.

## Getting started

### Music library

Search for music or paste a YouTube song or playlist link. Use **Library → Local files → +** to add files, or **Folders → Add folder…** for a whole music folder. Enter its absolute path (or `~/Music`), or use **Browse…**, then choose **Add folder**. This also works for network shares mounted as local folders and does not depend on the system folder picker. Subfolders are scanned recursively. Saved folders update automatically while Sung is running. Settings can disable automatic updates; th