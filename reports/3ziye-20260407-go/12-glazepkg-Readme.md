<div align="center">

# GlazePKG (`gpk`)

**See every package on your system — one gorgeous terminal dashboard.**

A beautiful TUI that unifies **36 package managers** into a single searchable, snapshotable, diffable view.
Built with [Bubble Tea](https://github.com/charmbracelet/bubbletea). Zero config. One binary. Just run `gpk`.

[![CI](https://img.shields.io/github/actions/workflow/status/neur0map/glazepkg/ci.yml?style=for-the-badge)](https://github.com/neur0map/glazepkg/actions/workflows/ci.yml)
[![Go](https://img.shields.io/github/go-mod/go-version/neur0map/glazepkg?style=for-the-badge&color=00ADD8)](https://go.dev/)
[![Release](https://img.shields.io/github/v/release/neur0map/glazepkg?style=for-the-badge&color=4c1)](https://github.com/neur0map/glazepkg/releases)
[![License: GPL-3.0](https://img.shields.io/badge/license-GPL--3.0-blue?style=for-the-badge)](LICENSE)
[![Downloads](https://img.shields.io/github/downloads/neur0map/glazepkg/total?style=for-the-badge&color=orange)](https://github.com/neur0map/glazepkg/releases)
[![Stars](https://img.shields.io/github/stars/neur0map/glazepkg?style=for-the-badge&color=yellow)](https://github.com/neur0map/glazepkg/stargazers)

![demo](demo.gif)

</div>

---

## Why?

You have `brew`, `pip`, `cargo`, `npm`, `apt`, maybe `flatpak` — all installing software independently. Knowing what's actually on your machine means running 6+ commands across different CLIs with different flags and output formats.

**GlazePKG fixes this.** One command, one view, every package. Track what changed over time with snapshots and diffs. Export everything to JSON for backup or migration.

## Features

- **36 package managers** — brew, pacman, AUR, apt, dnf, snap, pip, pipx, uv, cargo, go, npm, pnpm, bun, flatpak, MacPorts, pkgsrc, opam, gem, pkg, composer, mas, apk, nix, conda/mamba, luarocks, XBPS, Portage, Guix, winget, Chocolatey, Scoop, NuGet, PowerShell modules, Maven, Windows Update
- **Instant startup** — scans once, caches for 10 days, opens in milliseconds on repeat launches
- **Fuzzy search** — find any package across all managers instantly with `/`
- **Package operations** — upgrade, remove, search, and install packages without leaving the TUI
- **Multi-select** — batch upgrade or remove with smart sudo batching
- **Snapshots & diffs** — save system state, diff to see what changed
- **Update detection** — `↑` indicator for packages with available updates
- **Export** — dump to JSON or text for backup, migration, or dotfile tracking
- **Zero dependencies** — single static Go binary, cross-platform

## Install

### Homebrew (macOS / Linux)

```bash
brew install neur0map/tap/gpk
```

### Arch Linux (AUR)

```bash
yay -S gpk-bin
```

### Go

```bash
go install github.com/neur0map/glazepkg/cmd/gpk@latest
```

### Pre-built binaries

Grab a binary from [releases](https://github.com/neur0map/glazepkg/releases) for macOS (ARM/Intel), Linux (x64/ARM), or Windows (x64/ARM).

<details>
<summary>Build from source</summary>

```bash
git clone https://github.com/neur0map/glazepkg.git
cd glazepkg && go build ./cmd/gpk
```

If `gpk` is not found after installing via `go install`, add Go's bin directory to your PATH:

```bash
export PATH="$PATH:$HOME/go/bin"
```

</details>

## Quick Start

```
gpk              Launch TUI
gpk update       Self-update to latest release
gpk version      Show current version
gpk --help       Show keybind reference
```

Just run `gpk` — navigate with `j`/`k`, switch managers with `Tab`, search with `/`, press `s` to snapshot, `d` to diff, `e` to export. Press `?` for the full keybind reference.

<details>
<summary><strong>Keybindings</strong></summary>

| Key | Action |
|-----|--------|
| `j`/`k`, `↑`/`↓` | Navigate |
| `g` / `G` | Jump to top / bottom |
| `Ctrl+d` / `Ctrl+u` | Half-page down / up |
| `PgDn` / `PgUp` | Page down / up |
| `Tab` / `Shift+Tab` | Cycle manager tabs |
| `f` | Cycle size filter |
| `/` | Fuzzy search |
| `Enter` | Package details |
| `u` (detail) | Upgrade package |
| `x` (detail) | Remove package |
| `d` (detail) | View dependencies |
| `h` (detail) | Package help/usage |
| `e` (detail) | Edit description |
| `i` | Search + install packages |
| `m` | Toggle multi-select mode |
| `Space` (multi-select) | Toggle package selection |
| `s` | Save snapshot |
| `d` | Diff against last snapshot |
| `e` | Export (JSON or text) |
| `r` | Force rescan |
| `?` | Help overlay |
| `q` | Quit |

</details>

<details>
<summary><strong>Package Operations</strong></summary>

### Upgrade (`u` in detail view)

Open a package with `Enter`, then press `u`. A confirmation modal shows the exact command. Privileged managers (apt, pacman, dnf, snap, apk, xbps) include a password field for sudo. The upgrade runs in the background while you keep using the TUI.

### Remove (`x` in detail view)

Open a package with `Enter`, then press `x`. Managers that support it (apt, pacman, dnf, xbps) offer two modes: remove package only, or remove package with orphaned depend