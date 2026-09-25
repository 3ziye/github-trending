# Serein

<p align="center">
  <a href="https://github.com/ViceVerse-cz/rustcord">
    <img src="docs/preview.png" alt="Serein Native Discord Client" width="900" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 20px rgba(0,0,0,0.3);" />
  </a>
</p>

<p align="center">
  <strong>A lightweight, native Discord desktop client written in Rust, powered by egui and wgpu.</strong>
</p>

<h3 align="center">
  <a href="https://discord.gg/UqTDGCENaN">💬 Join our Discord server for updates</a>
</h3>

<p align="center">
  <a href="#downloads--installation"><strong>📦 Downloads</strong></a> &nbsp;•&nbsp;
  <a href="#highlights"><strong>⚡ Highlights</strong></a> &nbsp;•&nbsp;
  <a href="#feature-showcase"><strong>✨ Showcase</strong></a> &nbsp;•&nbsp;
  <a href="#measured-performance-vs-official-discord"><strong>📊 Benchmarks</strong></a> &nbsp;•&nbsp;
  <a href="#quick-start"><strong>🛠️ Quick Start</strong></a> &nbsp;•&nbsp;
  <a href="#feature-matrix"><strong>📋 Features</strong></a> &nbsp;•&nbsp;
  <a href="#architecture-overview"><strong>🏗️ Architecture</strong></a>
</p>

<p align="center">
  <a href="https://discord.gg/UqTDGCENaN"><img src="https://img.shields.io/badge/Discord-Join%20our%20Discord%20server%20for%20updates-5865F2?logo=discord&logoColor=white" alt="Discord" /></a>
  <a href="https://github.com/ViceVerse-cz/rustcord/releases"><img src="https://img.shields.io/github/v/release/ViceVerse-cz/rustcord?label=release&color=blue" alt="GitHub Release" /></a>
  <a href="Cargo.toml"><img src="https://img.shields.io/badge/rust-1.98.1_pinned-blue.svg?logo=rust" alt="Rust 1.98.1 Pinned" /></a>
  <a href="crates/ui"><img src="https://img.shields.io/badge/ui-egui%20%2F%20wgpu-orange.svg" alt="UI egui/wgpu" /></a>
  <a href="docs/platform-support.md"><img src="https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows-informational.svg" alt="Platform Support" /></a>
  <a href="LICENSE-MIT"><img src="https://img.shields.io/badge/license-MIT%20OR%20Apache--2.0-green.svg" alt="License: MIT or Apache-2.0" /></a>
</p>

---

> [!WARNING]
> **Unofficial and not endorsed by Discord.**
> Serein communicates directly with Discord's public gateway and REST endpoints for your existing account. Automating normal accounts outside the official OAuth2/bot API violates Discord's Terms of Service and carries risk of account termination. Technical interoperability does not imply platform approval. Review the [compatibility matrix](docs/discord-compatibility.md) and [authentication guide](docs/authentication.md) before use.

---

## Downloads & Installation

Pre-compiled releases for macOS, Linux, and Windows are published on GitHub [Releases](https://github.com/ViceVerse-cz/rustcord/releases).

| Platform | Format | Architectures | Details |
|---|---|---|---|
| **Windows** | `-Setup.exe`, `.zip` | `x86_64`, `aarch64` | Per-user NSIS installer (recommended) or standalone portable archive |
| **macOS** | Homebrew Cask, `.zip` | Apple Silicon (`aarch64`) | Signed and notarized `.app` bundle |
| **Linux** | Flatpak (recommended), Repositories (`apt`, `dnf`, `zypper`, `pacman`), Gentoo ebuild, `.AppImage` | `x86_64` | Flatpak with automatic updates; signed package repositories; portable AppImage |

---

<details open>
<summary><h3>🐧 Linux (Flatpak, Repositories, Gentoo, AppImage)</h3></summary>

#### 1. Flatpak (Recommended)

Flatpak is the recommended distribution format for Linux, featuring sandbox isolation, bundled GNOME/WebKit runtimes, and automatic background updates.

- **One-Click Repository Install (Automatic Updates)**:
  ```sh
  flatpak install --user https://viceverse-cz.github.io/Serein/flatpak/serein.flatpakref
  ```
  Once installed, your desktop software store (GNOME Software, KDE Discover) or `flatpak update` will automatically discover and install updates.

- **Standalone Offline Bundle**:
  Download `Serein-linux.flatpak` from [Releases](https://github.com/ViceVerse-cz/rustcord/releases):
  ```sh
  flatpak install --user ./Serein-linux.flatpak
  flatpak run cz.viceverse.serein
  ```

See [Flatpak guide](packaging/flatpak/README.md) for sandbox permissions and source build details.

#### 2. Native Package Repositories (apt, dnf, zypper, pacman)

Configure the signed package repository for your distribution with one command:
```sh
curl -fsSL https://viceverse-cz.github.io/Serein/setup.sh | sh
```
The script detects your distribution (Ubuntu/Debian, Fedora, openSUSE, Arch Linux), cryptographically verifies the GPG signing key, and configures the repository with an option to install immediately.

After setup, manage Serein with your native package manager:
```sh
# Ubuntu / Debian: sudo apt install serein
# Fedora:          sudo dnf install serein
# openSUSE:        sudo zypper install serein
# Arch Linux:      sudo pacman -S serein
```
Your normal system updates (`apt upgrade`, `dnf upgrade`, `zypper update`, `pacman -Syu`) will keep Serein updated. See [Signed package repositories](packagin