


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
sudo pacman -S gstreamer gst-plugins-base gst-plugins-good gst-plugins-bad gst-plugin-va
```

`gst-plugins-good` provides `qtdemux` for MP4 files, and `gst-plugins-bad` includes the H.264 parser used by many videos.

**Ubuntu/Debian:**
```bash
sudo apt install gstreamer1.0-vaapi gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad
```

**Fedora:**
```bash
sudo dnf install gstreamer1-vaapi gstreamer1-plugins-base gstreamer1-plugins-good gstreamer1-plugins-bad-free
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
the same video.

## Lock screen backgrounds with hyprlock (Wayland)

Hyprlock owns the lock-screen UI, but phonto can render the animated background
on a higher layer while hyprlock is active. Start a second phonto process on the
`overlay` layer before launching hyprlock:

```bash
phonto "$(cat "$HOME/.cache/phonto/current")" --layer overlay &
phonto_lock_pid=$!

hyprlock
kill "$phonto_lock_pid"
```

This pairs well with a normal desktop phonto session running on the default
`background` layer. If you use `phonto --rand`, the cache file lets the lock
screen reuse the same randomly selected wallpaper.

Hyprlock must leave its background transparent or partially transparent for the
video to be visible behind its controls.

## Live lockscreen wallpapers (macOS)

The lock screen is owned by `loginwindow`, which hides every non-Apple-signed window the moment the screen locks. Phonto sidesteps that by registering your video into Apple's aerial catalog, so Apple's own signed extension plays it on both the desktop and the lock screen.

```bash
phonto install-live-lockscreen /path/to/video.mp4
```

This transcodes the video to HEVC Main10 with two temporal sub-layers (the exact bitstream shape the aerials extension requires for multi-cycle playback), generates a thumbnail, and registers the asset under a **Phonto** section in System Settings → Wallpaper.

To activate, open **System Settings → Wallpaper**, pick the **Phonto** category, click your entry, then lock the screen (Apple menu → Lock Screen) to verify it plays across cycles.

To remove a previously-installed entry:

```bash
phonto install-live-lockscreen /path/to/video.mp4 --remove
```

Optional flags:

- `--name <STRING>` — display name shown in the picker (defaults to the file stem).

## Configuration

Phonto reads its config from `$XDG_CONFIG_HOME/phonto/config.toml`, falling back to `~/.config/phonto/config.toml`.

### `search_paths`

A list of directories to scan when using `--rand`. Each entry has a `path` and a `depth` controlling how many levels deep to search.

```toml
[[search_paths]]
path = "/home/user/wallpapers"
depth = 1

[[search_paths]]
path = "/mnt/media/videos"
depth = 2
```

`depth = 0` scans only the top-level directory. `depth = 1` includes one level of subdirectories, and so on.

### GLSL shaders (Wayland only)

`--shader PATH` applies a custom GLSL