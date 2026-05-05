<p align="center">
  <br>
  <strong>nano-ffmpeg</strong>
  <br>
  <em>Every ffmpeg feature. Zero flags to remember.</em>
  <br><br>
  <a href="https://nano-ffmpeg.vercel.app">Website</a> &bull;
  <a href="#quick-start">Quick Start</a> &bull;
  <a href="#install">Install</a> &bull;
  <a href="#features">Features</a> &bull;
  <a href="#usage">Usage</a> &bull;
  <a href="#cli-options">CLI Options</a> &bull;
  <a href="#operations">Operations</a> &bull;
  <a href="#keybindings">Keybindings</a> &bull;
  <a href="#releasing">Releasing</a> &bull;
  <a href="#contributing">Contributing</a> &bull;
  <a href="#license">License</a>
</p>

<p align="center">
  <a href="https://github.com/dgr8akki/nano-ffmpeg/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/dgr8akki/nano-ffmpeg/ci.yml?branch=main&label=CI" alt="CI"></a>
  <a href="https://github.com/dgr8akki/nano-ffmpeg/releases/latest"><img src="https://img.shields.io/github/v/release/dgr8akki/nano-ffmpeg?sort=semver" alt="Latest release"></a>
  <a href="go.mod"><img src="https://img.shields.io/github/go-mod/go-version/dgr8akki/nano-ffmpeg" alt="Go version"></a>
  <a href="#license"><img src="https://img.shields.io/github/license/dgr8akki/nano-ffmpeg" alt="License"></a>
</p>

---

nano-ffmpeg wraps the full power of ffmpeg in a beautiful, keyboard-driven terminal dashboard. No more googling flags. Browse your files, pick what you want to do, tweak settings with presets, and watch a live progress bar while it encodes.

Built for people who know they need ffmpeg but can't remember how to use it.

```
╭─────────────────────────────────────────────────────────────────────╮
│  nano-ffmpeg > Home                                                 │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ╭──────────────────────────────────────────────────────────────╮   │
│  │  ffmpeg 8.1                                                  │   │
│  │  497 codecs  |  231 encoders  |  234 formats  |  489 filters │   │
│  │  HW Accel: videotoolbox                                      │   │
│  ╰──────────────────────────────────────────────────────────────╯   │
│                                                                     │
│  RECENT FILES                                                       │
│     interview.mp4    ~/Videos                                       │
│     concert.mkv      ~/Downloads                                    │
│                                                                     │
│  OPERATIONS                                                         │
│   > Convert Format     Change container or codec                    │
│     Extract Audio      Strip video, keep audio                      │
│     Resize / Scale     Change resolution                            │
│     Trim / Cut         Cut segments by time                         │
│     Compress           Reduce file size                             │
│     ...                                                             │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│  ↑↓ Navigate   Enter Select   q Quit   ? Help                      │
╰─────────────────────────────────────────────────────────────────────╯
```

## Quick Start

If you already have `ffmpeg` and `ffprobe` on your `PATH`:

```bash
# macOS (Homebrew tap -- also pulls ffmpeg-full):
brew install dgr8akki/tap/nano-ffmpeg
nano-ffmpeg
```

```powershell
# Windows (Scoop -- pulls ffmpeg from the extras bucket):
scoop bucket add extras
scoop bucket add nano-ffmpeg https://github.com/dgr8akki/scoop-bucket
scoop install nano-ffmpeg
nano-ffmpeg
```

```bash
# Any Go toolchain:
go install github.com/dgr8akki/nano-ffmpeg@latest
nano-ffmpeg
```

Jump straight into a specific file without clicking through the file picker:

```bash
nano-ffmpeg -d ~/Videos/interview.mp4
```

The TUI takes you from there: pick an operation, tweak the pre-filled defaults, hit Enter. See [Usage](#usage) for the full flow and [CLI Options](#cli-options) for every flag.

## Features

**Core**
- 12 ffmpeg operations accessible through guided, multi-screen workflows
- Pre-filled defaults for every operation so you can hit Enter without thinking about flags
- Command preview on every settings screen -- see the exact `ffmpeg` command before it runs
- Trim pre-fills the input's total duration; Stabilize automatically falls back to `deshake` if `vidstab` isn't in your ffmpeg build

**Progress Tracking**
- Gradient progress bar (green-to-cyan) with percentage
- Real-time stats: elapsed, ETA (smoothed over rolling window), speed, FPS, bitrate, frames, output size
- Braille-dot spinner for indeterminate operations (stream copy, concat)
- Scrollable live log of raw ffmpeg output
- Cancel with confirmation (`Esc` > `y`)

**File Handling**
- Built-in file brows