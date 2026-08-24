# Omasnap

A native Wayland screenshot and annotation overlay designed for Omarchy and Hyprland.
It captures the focused monitor before mapping an exclusive layer-shell surface, so the
editor never appears in its own screenshot. The editor retains annotations as movable,
resizable vector layers and preserves the monitor's native pixels on scaled displays.

[![Looping Omasnap demonstration](assets/omasnap.gif)](assets/omasnap.mp4)

## Features

- Freeform region, window, and full-monitor capture modes.
- A pointer-side readout that turns any drag into a ruler: the pointer position
  while the crosshair is idle, then the frame size in native export pixels while a
  region, a hovered window, or a crop handle is being sized.
- Window capture is a crop of the focused-monitor frame. Overlapping windows stay
  visible; there is no second clean-window recapture.
- Select/move/resize layers, mouse-wheel scaling, and eight external recropping handles.
- Arrows, straight lines, smoothed freehand strokes, translucent highlighter strokes,
  hollow or filled rectangles (optionally rounded) and ellipses, numbered markers,
  editable Neucha text (on a readability pill), and secure redaction with opaque or
  randomized non-spatial mosaic output.
- Per-layer preset or custom colors (including highlighter ink), undo/redo history,
  one-click whole-image or drag-region OCR (the recognized text is shown beside
  the image and copied to the clipboard),
  mesh-gradient backdrops, and rendered drop shadows.
- Cut tool: drag across a band of the image to remove it and collapse the gap, with a
  live preview and dashed seam marker while dragging; annotations shift to follow.
- Pin a finished capture as a bottom-right always-on-top layer surface, launched
  from the same `omasnap` executable and visible on every workspace.
- Crash-resistant working documents under `/run/user/<UID>/omasnap/` (falling back to
  a private `/tmp/omasnap-<UID>/`): the original source image plus a sidecar JSON
  operation log. Undo still works after a crash or `--file` reopen. Saving and
  copying write a normal flattened PNG to the clipboard or `~/Pictures/Screenshots`.
- Verified PNG clipboard output through `wl-copy`/`wl-paste`, plus timestamped files
  under `~/Pictures/Screenshots` by default.
- Open an image already on the clipboard directly in the annotation editor.
- A recents shelf: the select overlay stacks small cards of the last five captures
  along the right edge; hover to fan them out, click one to reopen it in the editor
  with its layers still editable instead of taking a new screenshot.
- Correct native-pixel export on fractional or integer-scaled monitors.

## Platform scope

The supported target is **Wayland + Hyprland**, with Omarchy as the primary integration.
The renderer, layer surface, clipboard, and monitor capture use Wayland protocols;
monitor/window discovery currently calls `hyprctl`. The focused output is captured
in-process through `ext-image-copy-capture` before the layer maps. Selection displays
that captured frame, while the annotation editor uses
a translucent layer scrim over the live desktop and draws only the selected capture.
Another Wayland compositor could support the application after supplying equivalent
monitor and window discovery; generic Wayland support is not claimed by 1.0.

Runtime commands used by the application:

- `hyprctl`
- `wl-copy` and `wl-paste`
- `tesseract`
- `omarchy-notification-send` when available; saved captures include a thumbnail and
  reopen in Omasnap when clicked. Notification failure does not invalidate output.

## Install on Omarchy

Clone the repository and run the Omarchy installer:

```bash
git clone https://github.com/tobi/omasnap.git
cd omasnap
./install-omarchy
```

The installer uses Omarchy's package helper for missing dependencies, builds in
`~/.cache/omasnap`, and installs under `~/.local`. It does not modify
Hyprland configuration.

### Hyprland binding

Paste this into a Lua config loaded after `require("default.hypr.omarchy")`:

```lua
hl.unbind("PRINT")
hl.unbind("F12")
hl.unbind("ALT + SHIFT + 4")

o.bind("PRINT", "Screenshot", "omasnap")
o.bind("F12", "Screenshot", "omasnap")
o.bind("ALT + SHIFT + 4", "Screenshot", "omasnap")

hl.layer_rule({
  match = { namespace = "^omasnap$" },
  no_anim = true,
  animation = "none",
  no_screen_share = true,
})
```

Each of these keys toggles: the first press opens the overlay, the next press dismisses it.

Apply and verify:

```bash
hyprctl reload
hyprctl configerrors
hyprctl binds -j | jq -c \
  '[.[] | select(.description == "Screenshot") | {modmask,key,description}]'
```

`omarchy plugin add` is intentionally not used. Omarchy plugins are Quickshell QML
extensions; they do not install native executables or system packages.

Set `OMASNAP_PREFIX` before running `install-omarchy` to use a prefix other than
`~/.local`.

### Manual Arch Linux build

Install the complete build/runtime dependency set:

```bash
sudo pacman -S --needed