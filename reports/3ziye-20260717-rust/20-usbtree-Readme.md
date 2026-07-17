# usbtree

Cross-platform TUI for inspecting the USB device tree (Linux, macOS, Windows). Enumerates via [nusb](https://crates.io/crates/nusb) — pure Rust, no root, no libusb. One static binary, zero runtime deps: **~1.5 MB download, ~5–7 MB on disk**.

![usbtree](https://img.shields.io/badge/rust-ratatui-blue)
[![license: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![ci](https://github.com/gnomeria/usbtree/actions/workflows/ci.yml/badge.svg)](https://github.com/gnomeria/usbtree/actions/workflows/ci.yml)
[![release](https://img.shields.io/github/v/release/gnomeria/usbtree)](https://github.com/gnomeria/usbtree/releases/latest)

**Website:** [gnomeria.github.io/usbtree](https://gnomeria.github.io/usbtree)

![usbtree demo](docs/screenshots/demo.gif)

## Platform support

| Feature                                              |     Linux     | macOS | Windows |
| ---------------------------------------------------- | :-----------: | :---: | :-----: |
| Device tree — hubs, classes, speeds, tree rails      |      ✅       |  ✅   |   ✅    |
| Friendly names (`overrides.ids` + usb.ids)           |      ✅       |  ✅   |   ✅    |
| Hot-plug watch + timestamped event log               |      ✅       |  ✅   |   ✅    |
| Detail panel — sysfs path, vid:pid, serial, children |      ✅       |  ✅   |   ✅    |
| Device power — advertised `bMaxPower`                |      ✅       |  ✅   |    —    |
| Live activity sparklines — URBs/s (unprivileged)     |      ✅       |   —   |    —    |
| Real bandwidth — bytes/s via usbmon (root)           |      ✅       |   —   |    —    |
| Prebuilt binaries                                    | amd64 · arm64 | arm64 |  amd64  |

Live per-device activity is Linux-only — [why →](#activity-metrics-linux).

## Install

> [!NOTE]
> The shell installer and prebuilt links need a published GitHub release. None yet? Install from source.

**Linux / macOS**

```sh
curl -fsSL https://raw.githubusercontent.com/gnomeria/usbtree/main/scripts/install.sh | sh
```

**Windows**

```powershell
irm https://raw.githubusercontent.com/gnomeria/usbtree/main/scripts/install.ps1 | iex
```

**From source**

```sh
cargo install --git https://github.com/gnomeria/usbtree
```

Installers verify the archive's sha256 against `checksums.txt` and install to `/usr/local/bin` or `~/.local/bin` (Linux/macOS) / `%LOCALAPPDATA%\usbtree\bin` + user `PATH` (Windows). Env vars (prefix `$env:` in PowerShell):

| Variable               | Effect                                                     |
| ---------------------- | ---------------------------------------------------------- |
| `USBTREE_VERSION`      | pin a version, e.g. `0.0.1` (default: latest)              |
| `USBTREE_INSTALL_DIR`  | install directory override                                 |
| `USBTREE_SUDO_SYMLINK` | `1` also symlinks into `/usr/local/bin` via `sudo`, so `sudo usbtree` finds it for usbmon bytes/s |

Or grab a `usbtree_<version>_<os>-<arch>.{tar.gz,zip}` archive from the [latest release](https://github.com/gnomeria/usbtree/releases/latest); each sha256 is in `checksums.txt`.

> [!NOTE]
> **macOS and Windows binaries are not code-signed or notarized.**
> - **macOS**: the install script clears the quarantine flag; manual downloads need `xattr -d com.apple.quarantine ./usbtree` (or right-click → Open once).
> - **Windows**: SmartScreen may warn — _More info_ → _Run anyway_, or `Unblock-File usbtree.exe`.
> Verify the sha256 or build from source if in doubt.

## Features

- Live USB tree — color-coded class gutter, per-class icons, tree rails, speed badges (`▂` low/full, `▄` high 480M, `█` SuperSpeed+ 5G/10G); rescans every second. Collapse hubs with `Enter`/`Space`/`h`/`l` → `▸` + `+N` child badge
- Names via fallback chain: `overrides.ids` → descriptor strings → downloaded [usb.ids](http://www.linux-usb.org/usb-ids.html) (`--updatelist`) → embedded snapshot → vendor/class heuristics
- Composite/Misc (0xef) devices classified by interface class, so e.g. a MOTU M2 shows as Audio, not Misc
- Hot-plug watch — plugged flash green, unplugged linger as red ghosts for 30 s, all events logged with timestamps
- Live per-device activity (Linux) — inline sparklines + detail-pane bandwidth graph; URBs/s unprivileged, real bytes/s via usbmon (root, see below)
- Detail panel — sysfs path, vid:pid, vendor, class, speed, `bMaxPower`, serial, connected children
- Safe eject (Linux, unprivileged) — `e` on a mass-storage device unmounts + cuts port power via udisks2, with a confirm dialog
- PCI view (`p`) — flat address-sorted PCI list with detail pane (prog-if, subsystem, link speed/width, NUMA, IOMMU group, power state)
- Live filter (`/`), yank (`y` vid:pid, `Y` full details), `--dump` prints the tree once (no TUI)

## Usage

```sh
usbtree                 # TUI
usbtree --dump          # print the tree once and exit
usbtree --updatelist    # download the latest usb.ids into the config dir
usbtree --demo          # fake tree with scripted hot-plug + t