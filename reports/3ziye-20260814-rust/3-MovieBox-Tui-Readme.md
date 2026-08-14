<div align="center">

# MovieBox-TUI

Search, browse, play, and download movies, series, anime, and IPTV streams from a keyboard-first terminal interface using external media players.

[![Crates.io](https://img.shields.io/crates/v/moviebox-tui.svg?logo=rust)](https://crates.io/crates/moviebox-tui)
[![CI](https://github.com/mesamirh/MovieBox-Tui/actions/workflows/ci.yml/badge.svg)](https://github.com/mesamirh/MovieBox-Tui/actions/workflows/ci.yml)
[![Platforms](https://img.shields.io/badge/Platforms-macOS%20%7C%20Linux%20%7C%20Windows%20%7C%20Android-brightgreen)](#requirements)
[![License](https://img.shields.io/badge/license-MIT%20OR%20Apache--2.0-blue.svg)](#license)

<video src="https://github.com/user-attachments/assets/e3dc0c11-524f-4b0e-8902-e0c66d6ca88d" alt="MovieBox-TUI demo" width="85%" autoplay loop muted></video>

</div>

## Documentation

This README is the project landing page (features, install, usage). The full
documentation set — architecture, providers, players, cache, logging, TV mode,
configuration, and debugging — lives in [`docs/`](docs/README.md). Contribution
guidance is in [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Features

### Catalogs & Browsing

- Search and browse movies, TV series, and anime from multiple content catalogs
- Inspect stream quality groupings and subtitle options before playback

> **Note on BDIX:** BDIX sources are only accessible from supported Bangladeshi ISP networks. Because of this, they are hidden by default. You can enable them manually if your network supports it.

### Playback

- Play streams directly in your local media player (mpv, VLC, or IINA)
- Play protected streams seamlessly without manual configuration

### Downloads

- Download full seasons or episodes with automatic subtitle language selection
- Resume interrupted downloads without losing progress

### IPTV

- Watch live TV by loading remote or local `.m3u` playlists organized by category

### User Interface & App

- View rich graphical posters in supported terminals (Kitty, iTerm2, Sixel) or fallback to text art
- Let the app automatically manage configuration and clean up expired caches

MovieBox-TUI resolves links from upstream services. Availability can change when those services change, and some mirrors are region- or rate-limit-dependent.

## Requirements

- 64-bit Windows, macOS, Linux, or Android (Termux)
- Terminal size of at least 85×24
- One supported player: mpv, VLC, IINA, or any native Android video player
- Internet connection

## Installation

Prebuilt binaries are available for macOS, Linux, and Windows releases. The official install scripts verify the release SHA-256 checksum automatically.
On Termux, install from TUR or build from source with `cargo install` on-device.

### macOS or Linux

#### Homebrew

```bash
brew tap mesamirh/moviebox-tui https://github.com/mesamirh/MovieBox-Tui
brew install mesamirh/moviebox-tui/moviebox-tui
```

The formula selects the correct macOS, Linux x86_64, or Linux ARM64 release.

#### Install script

```bash
curl -fsSL https://raw.githubusercontent.com/mesamirh/MovieBox-Tui/main/install.sh | bash
```

The script detects OS and CPU architecture, then installs to `/usr/local/bin`. Without write access or `sudo`, it uses `~/.local/bin`.

### Windows

Works in PowerShell or Command Prompt (cmd):

```cmd
powershell -Command "irm https://raw.githubusercontent.com/mesamirh/MovieBox-Tui/main/install.ps1 | iex"
```

The installer selects x86_64 or ARM64, installs under `%LOCALAPPDATA%\MovieBox-Tui`, and adds that directory to the user PATH. Open a new terminal after first installation.

### Android (Termux)

MovieBox-Tui runs natively in Termux and opens videos through the Android app chooser on supported devices.

Preferred install via TUR (Termux User Repository):

```bash
pkg install tur-repo
pkg install moviebox-tui
termux-setup-storage
```

TUR packages are distributed separately from crates.io. New MovieBox-Tui GitHub
releases may take some time to appear in TUR, and users still need to update
packages normally in Termux (for example via `pkg upgrade`). Termux playback
should be rechecked on real devices for each release.
If you previously installed MovieBox-Tui with `cargo install`, see
[Troubleshooting](#troubleshooting) for the Termux PATH fix.

Alternative source-based install:

```bash
pkg install rust openssl pkg-config
cargo install moviebox-tui --locked
termux-setup-storage
```

_`termux-setup-storage` is recommended if you want downloads saved to the real
Android `Download` folder._

<details>
<summary><b>Build from source</b></summary>

```bash
git clone https://github.com/mesamirh/MovieBox-Tui.git
cd MovieBox-Tui
cargo build --release --locked
```

Binary location: `target/release/moviebox-tui` (`moviebox-tui.exe` on Windows).

</details>

## Supported Players

MovieBox-TUI checks standard application locations, PATH executables, and Linux Flatpak installations.

Detected automatically:

- **macOS:** `/Applications`, `~/Applications`, 