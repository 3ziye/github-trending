<h1 align="center">Spun</h1>

<p align="center">A music player for Linux with CD, vinyl, cassette and recorder views.</p>

<p align="center">
  <img src="assets/screenshots/spun-vinyl.png" alt="Spun in vinyl mode with a gold tonearm and the Cider queue alongside it" width="1000">
</p>

<p align="center">
  <a href="https://buymeacoffee.com/E_Gurl">
    <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Support Spun on Buy Me a Coffee" width="217" height="60">
  </a>
  <br>
  <sub>Optional support for Spun's development.</sub>
</p>

<p align="center">
  <a href="#install">Install</a> ·
  <a href="#start-listening">Get started</a> ·
  <a href="#inside-the-player">Features</a> ·
  <a href="#troubleshooting-and-privacy">Help</a> ·
  <a href="#license">License</a>
</p>

Play local music, browse YouTube Music anonymously, connect to Jellyfin, Navidrome or Subsonic, or control Apple Music through Cider. Spun puts your album artwork on a spinning CD, vinyl record, cassette or TP-7-inspired recorder, with an interface inspired by Material Design 3. Optional 3D players add physical depth and lighting that follows Noctalia's wallpaper palette.

**Source-available · PolyForm Noncommercial 1.0.0.** Personal and other permitted noncommercial use is free. This is not an OSI-approved open-source license. [Read the license details](#license).

## Install

<details>
<summary><b>Build dependencies for Arch and CachyOS</b></summary>

```bash
sudo pacman -S --needed base-devel git cmake ninja python qt6-base qt6-declarative qt6-multimedia qt6-svg qt6-wayland taglib qt6-quick3d
```
</details>

<details>
<summary><b>Build dependencies for Fedora</b></summary>

```bash
sudo dnf install gcc-c++ git cmake ninja-build pkgconf-pkg-config python3 qt6-qtbase-devel qt6-qtdeclarative-devel qt6-qtmultimedia-devel qt6-qtsvg-devel qt6-qtwayland taglib-devel qt6-qtquick3d-devel
```
</details>

Spun builds from source; there is no packaged installer yet. You can do so using these commands:
```bash
git clone https://github.com/yappologistic/Spun.git
cd Spun
./scripts/build.sh -DBUILD_TESTING=OFF
./scripts/install-launcher.sh
```

Spun includes 3D when Qt Quick 3D is available. To build without it, add `-DSPUN_ENABLE_3D=OFF` to the build command.

Open **Spun** from your application menu, or run `./scripts/run.sh` from its folder. The launcher points to that folder. If you move it, run `./scripts/install-launcher.sh` again.

<details>
<summary>Ubuntu 22.04 and 24.04</summary>

The default repositories do not provide the required Qt 6.8+ and TagLib 2.0+. Install a newer Qt SDK with Quick Controls, Multimedia, SVG, and optionally Quick 3D, and build TagLib 2.x using its [upstream instructions](https://github.com/taglib/taglib/blob/master/INSTALL.md).

```bash
sudo apt install build-essential git cmake ninja-build pkg-config python3 libutfcpp-dev zlib1g-dev libgl1-mesa-dev libxkbcommon-dev libxcb-cursor0
```

`libutfcpp-dev` supplies TagLib's UTF-8 dependency. `libxcb-cursor0` is required by Qt's X11 platform plugin. Point CMake at the newer Qt installation rather than the distribution's older Qt:

```bash
./scripts/build.sh -DBUILD_TESTING=OFF -DCMAKE_PREFIX_PATH=/path/to/Qt/gcc_64
```

If TagLib was installed into a custom prefix, add its `lib/pkgconfig` directory to `PKG_CONFIG_PATH` before building. `pkg-config --modversion taglib` must report 2.0 or newer.

</details>

<details>
<summary>Building on another Linux distribution</summary>

You need a C++20 compiler, CMake 3.22+, Ninja, pkg-config, Python 3, Qt 6.8+ with Quick Controls, Multimedia, SVG and development files, and TagLib 2.0+ development files. Qt Quick 3D is optional. Package names differ between distributions. Spun is developed on CachyOS with Hyprland and Noctalia; desktop integration can vary elsewhere.

</details>

<details>
<summary>Nix and NixOS</summary>

With Nix flakes enabled, run from the cloned source folder:

```bash
NIXPKGS_ALLOW_UNFREE=1 nix run --impure .
# Build without launching:
NIXPKGS_ALLOW_UNFREE=1 nix build --impure .
# Development tools:
nix develop
```

The license is noncommercial, so Nix requires an explicit unfree-package opt-in. The flake supports x86_64 and aarch64 Linux. Wayland and X11 plugins are included; no display backend is forced.

</details>

## Start listening

**Local music:** choose **Local**, then **+** to add tracks, or drop files and folders onto Spun. **More → Add music folder** includes artist and album subfolders. Imports show progress, skip songs already in the queue and can be cancelled without adding a partial import. Directory symlinks inside the folder are not followed. Your music files are not copied or modified. **More → Play demo** plays the included original soundcheck.

**Apple Music through Cider:** open Cider, sign in there, then choose **Cider** in Spun. Cider handles authentication and streaming and must remain running. Apple Music playback requires the appropriate access through Cider.

For searc