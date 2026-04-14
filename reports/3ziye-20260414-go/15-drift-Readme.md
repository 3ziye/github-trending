<div align="center">

<pre>
·  ·    ·        ·     ·    ·  ·
    ·      d r i f t      ·
  ·    ·        ·    ·       ·
</pre>

**A terminal screensaver that turns idle time into ambient art.**

Every OS has a screensaver. The terminal had nothing — until now.

[![Go](https://img.shields.io/badge/go-1.23+-00ADD8?style=flat-square&logo=go&logoColor=white)](https://go.dev)
[![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)
[![Release](https://img.shields.io/github/v/release/phlx0/drift?style=flat-square&color=blueviolet)](https://github.com/phlx0/drift/releases)
[![CI](https://img.shields.io/github/actions/workflow/status/phlx0/drift/ci.yml?style=flat-square&label=ci)](https://github.com/phlx0/drift/actions)
[![Go Report Card](https://goreportcard.com/badge/github.com/phlx0/drift?style=flat-square)](https://goreportcard.com/report/github.com/phlx0/drift)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](CONTRIBUTING.md)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows-brightgreen?style=flat-square)](https://github.com/phlx0/drift/releases)
[![AUR](https://img.shields.io/aur/version/drift-bin?style=flat-square&label=AUR&color=1793d1)](https://aur.archlinux.org/packages/drift-bin)
[![Homebrew](https://img.shields.io/badge/homebrew-phlx0%2Fdrift-orange?style=flat-square&logo=homebrew)](https://github.com/phlx0/homebrew-drift)
[![Downloads](https://img.shields.io/github/downloads/phlx0/drift/total?style=flat-square&label=downloads)](https://github.com/phlx0/drift/releases)

</div>

---

<img src="demo/waveform.gif" width="100%" />

---

## Scenes

drift ships **11 scenes** and **9 built-in themes**. They cycle automatically or you can lock to one.

<table>
<tr>
<td width="50%">

**waveform** — braille sine waves that breathe

<img src="demo/waveform.gif" width="100%" />

</td>
<td width="50%">

**constellation** — stars drift and connect

<img src="demo/constellation.gif" width="100%" />

</td>
</tr>
<tr>
<td width="50%">

**rain** — katakana characters fall in columns

<img src="demo/rain.gif" width="100%" />

</td>
<td width="50%">

**particles** — a flow field of drifting glyphs

<img src="demo/particles.gif" width="100%" />

</td>
</tr>
<tr>
<td width="50%">

**pipes** — box-drawing pipes snake across the screen and wrap at the edges

<img src="demo/pipes.gif" width="100%" />

</td>
<td width="50%">

**maze** — a perfect maze builds itself, holds, then dissolves and regenerates

<img src="demo/maze.gif" width="100%" />

</td>
</tr>
<tr>
<td width="50%">

**life** — Conway's Game of Life; cells flash bright on birth, age through the palette, reset when the grid stagnates

<img src="demo/life.gif" width="100%" />

</td>
<td width="50%">

**clock** — current time in large braille digits, styled in the active theme, with the date below

<img src="demo/clock.gif" width="100%" />

</td>
</tr>
<tr>
<td width="50%">

**orrery** — a stylized solar system with a fixed sun, concentric orbit rings, and braille-rendered planets

<img src="demo/orrery.gif" width="100%" />

</td>
<td width="50%">

**starfield** — classic 3-D star warp; stars accelerate toward you from the centre, brightening and leaving trails as they approach

<img src="demo/starfield.gif" width="100%" />

</td>
</tr>
<tr>
<td width="50%">

**dvd** — the classic bouncing logo; changes palette color on each wall bounce and flashes bright on a corner hit

<img src="demo/dvd.gif" width="100%" />

</td>
<td width="50%">
</td>
</tr>
</table>

## Themes

Nine built-in themes matched to popular terminal colorschemes.

`cosmic` · `nord` · `dracula` · `catppuccin` · `gruvbox` · `forest` · `wildberries` · `mono` · `rosepine`


```bash
drift list themes    # preview all themes with color swatches
```

---

## Installation

### Option 1 — Homebrew (macOS and Linux)

```bash
brew install phlx0/drift/drift
```

### Option 2 — AUR (Arch Linux)

```bash
yay -S drift-bin   # or: paru -S drift-bin
```

### Option 3 — Nix flake

```bash
nix run github:phlx0/drift
```

Or add to your configuration:

```nix
inputs.drift.url = "github:phlx0/drift";
```

### Option 4 — Pre-built binary (no Go required)

1. Go to the [Releases](https://github.com/phlx0/drift/releases) page.
2. Download the archive for your platform:

   | OS | Chip | File |
   |---|---|---|
   | macOS | Apple Silicon (M1/M2/M3) | `drift_darwin_arm64.tar.gz` |
   | macOS | Intel | `drift_darwin_amd64.tar.gz` |
   | Linux | x86-64 | `drift_linux_amd64.tar.gz` |
   | Linux | ARM64 | `drift_linux_arm64.tar.gz` |
   | Windows | x86-64 | `drift_windows_amd64.zip` |

3. Extract and move it somewhere on your `PATH`:

   ```bash
   tar -xzf drift_darwin_arm64.tar.gz
   sudo mv drift /usr/local/bin/
   drift version
   ```

### Option 5 — Go install

```bash
go install github.com/phlx0/drift@latest
```

Make sure Go's bin directory is on your `PATH`:

```bash
# add to ~/.zshrc or ~/.bashrc
export PATH="$PATH:$(g