


# Phonto

> phonto (/'fon.to/) — from Greek φόντο: background

GPU-accelerated video wallpaper program for Wayland compositors and macOS, written in Rust. Also supports live lockscreen wallpapers on macOS.


![example](./mac-example.gif)


On Linux, phonto plays videos as your desktop background with minimal overhead, decoding and rendering entirely on the GPU through GStreamer and EGL. On macOS it drives an `AVPlayerLayer` attached to a window sitting just below the system wallpaper level, so VideoToolbox handles decoding and CoreAnimation handles compositing.

## Installation

Using Nix (NixOS and macOS with nix-darwin):

```bash
nix profile install github:museslabs/phonto
```

Using Homebrew (macOS and Linux x86_64):

```bash
brew tap museslabs/phonto
brew install phonto
```

Using AUR on Arch Linux:

```bash
yay -S phonto
```

Using cargo:

```bash
cargo install phonto
```

From source:

```bash
git clone https://github.com/museslabs/phonto
cd phonto
cargo build --release
```

## Dependencies

### Linux (Wayland)

Phonto requires GStreamer runtime plugins in addition to the VA-API plugin used for GPU-accelerated decoding. On Linux, missing demuxer or codec plugins can cause startup failures  when opening MP4/H.264 files. Without the VA-API plugin, GStreamer falls back to software decoding and CPU usage will be significantly higher.

**Arch Linux:**
```bash
sudo pacman -S gstreamer gst-plugins-base gst-plugins-good gst-plugins-bad gst-libav gst-plugin-va
```

`gst-plugins-good` provides `qtdemux` for MP4 files, and `gst-plugins-bad` includes the H.264 parser used by many videos.

**Ubuntu/Debian:**
```bash
sudo apt install gstreamer1.0-vaapi gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-libav
```

**Fedora:**
```bash
sudo dnf install gstreamer1-vaapi gstreamer1-plugins-base gstreamer1-plugins-good gstreamer1-plugins-bad-free gstreamer1-libav
```

### macOS

No external dependencies. phonto links against system frameworks (`AVFoundation`, `CoreMedia`, `AppKit`, `QuartzCore`). Decoding goes through VideoToolbox automatically for codecs the OS supports (H.264, HEVC, ProRes, etc.).

## Usage

Play a specific video:
```bash
phonto /path/to/video.mp4
```

Play a random wallpaper from your configured search paths:
```bash
phonto --rand
```

On Linux/Wayland, choose the layer-shell layer to render on:
```bash
phonto /path/to/video.mp4 --layer background
```

Available layers are `background` (default), `bottom`, `top`, and `overlay`.

Phonto also writes the currently selected video path to `~/.cache/phonto/current`.
This is useful when `--rand` chooses a wallpaper and another tool needs to reuse
the same video. For per-display playback there is no single "current" video, so the
cache file is skipped in that mode.

## Multi-monitor

By default phonto mirrors a single video across every connected display. New
monitors plugged in mid-session attach automatically, and unplugging then
re-plugging a monitor brings the wallpaper back without restart.

### Listing displays

```bash
phonto displays
```

The first column is the native ID for the current OS. You can pass that string
straight into `--display`, or wire it into an `[[alias]]` block ([see below](#cross-platform-aliases)) to
share one config across machines.

### Pinning videos per display from the CLI

Repeat `--display ID PATH` for each display you want to set. Every display must
be named explicitly. There is no implicit default.

```bash
phonto --display "DELL U2723QE" /path/to/ocean.mp4 \
       --display "eDP-1" /path/to/forest.mp4
```

The first value is the display ID (as printed by `phonto displays`, or an alias
name from your config) and the second is the video path.

For a random video on one specific display, use `--display-rand ID`. It picks
from your `search_paths` the same way `--rand` does.

```bash
phonto --display "DELL U2723QE" /path/to/pinned.mp4 \
       --display-rand "eDP-1"
```

`--display` and `--display-rand` can be mixed and repeated. Displays you don't
mention get no wallpaper from phonto and keep whatever the OS is showing there.

### Persistent assignment via config

The same assignments belong in `config.toml` under `[[display]]` blocks. Then
`phonto` with no arguments reads them.

```toml
[[display]]
id = "DELL U2723QE"
path = "~/Videos/ocean.mp4"

[[display]]
id = "eDP-1"
random = true
```

Each `[[display]]` needs exactly one of `path` or `random = true`. Phonto errors
at startup if both or neither are set.

A `[[display]]` whose display is not currently connected is not an error.
Phonto waits and attaches the wallpaper when that display appears.

### Cross-platform aliases

Native display IDs differ across operating systems. The same monitor might be
`"DELL U2723QE"` on macOS and `"DP-1"` on a wlroots compositor. Alias blocks
let you give a portable name to a physical display once and reference it from
`[[display]].id`.

```toml
[[alias]]
name = "main"
wayland = "DP-1"
macos = "DEL