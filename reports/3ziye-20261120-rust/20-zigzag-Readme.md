<img src="packaging/macos/AppIcon-dark.png" alt="ZigZag dark mode app icon" width="160" height="160">

# ZigZag

**[Visit zigzag.diy](https://zigzag.diy/)**

ZigZag is a visual embroidery editor built in Rust for performance, with
built-in **MCP (Model Context Protocol)** support so AI agents can create and
edit designs alongside you. Turn SVG artwork into stitches, fine-tune it in
the editor, and export **PES, DST, EXP, JEF, or VP3** for broad compatibility
with embroidery machines—or send designs directly to a **Brother Skitch
(PP1) over Bluetooth**.

Draw in Illustrator, draw in ZigZag, or let an agent draw. The Rust engine
and `zigzag` command-line tool power the same workflow outside the editor.

## See ZigZag in action

https://github.com/user-attachments/assets/94812f25-82f4-429f-85db-5e20c1d5e723

**Stitching on a Brother Skitch (PP1)**

<a href="https://github.com/simpsoka/zigzag/raw/refs/heads/main/packaging/media/skitch-pp1-demo.mp4">
  <img src="packaging/media/skitch-pp1-demo.jpg" alt="Download the video of ZigZag stitching a design on a Brother Skitch PP1" width="320">
</a>

[Download the video (MP4, 1080p)](https://github.com/simpsoka/zigzag/raw/refs/heads/main/packaging/media/skitch-pp1-demo.mp4)
· [Original post on X](https://x.com/simpsoka/status/2115254318161182876).

## Download for Mac

**[Download ZigZag.dmg](https://github.com/simpsoka/zigzag/releases/latest/download/ZigZag.dmg)**

For Apple Silicon and Intel Macs, macOS 11 or later. Open the DMG, then drag
ZigZag into Applications. The release is signed and notarized by Apple.
No Rust installation is needed.

Or with [Homebrew](https://brew.sh):

```sh
brew install --cask simpsoka/zigzag/zigzag
```

To update a Homebrew installation:

```sh
brew upgrade --cask --greedy simpsoka/zigzag/zigzag
```

Starting with version 0.1.3, ZigZag also offers an in-app updater: it tells
you when there's a newer release and installs it when you say (ZigZag ›
Check for Updates…).

## Download for Windows

**[Download ZigZag for Windows](https://github.com/simpsoka/zigzag/releases/latest)**
— the `ZigZag-<version>-x86_64-windows.zip` asset on the latest release.

For 64-bit Windows 10 (version 1709 or later) and Windows 11. Unzip it and
double-click **ZigZag.exe**. Windows SmartScreen warns on apps without a
Microsoft-trusted signature the first time they run; click *More info* →
*Run anyway*. No Rust installation is needed.

## Download for Linux

**[Download ZigZag for Linux](https://github.com/simpsoka/zigzag/releases/latest)**
— the `ZigZag-<version>-x86_64-linux.tar.gz` asset on the latest release.

For x86-64 Linux desktops with glibc 2.35 or newer (Ubuntu 22.04+, Debian 12+),
X11 or Wayland, and OpenGL. Extract the archive and run `./zigzag-studio`
inside the extracted folder. It also includes the `zigzag` CLI and
`zigzag-mcp` bridge; no Rust installation is needed. See the included
`README.txt` for runtime dependencies and Bluetooth setup.

[Release notes and checksums](https://github.com/simpsoka/zigzag/releases/latest)
· [Changelog](CHANGELOG.md)
· [Publishing a release](RELEASE.md)

```
zigzag/
  src/svg.rs              SVG import (usvg): fill and stroke parts, transforms, text
  src/document/           editable document; settings saved back into SVG ids,
                          layout edits as SVG transforms, lettering
  src/params.rs           stitch settings tokens + fabric presets
  src/stitch/fill.rs      tatami fill (scanline sections, staggered rows)
  src/stitch/satin.rs     satin columns: two rails, auto-satin, underlays, short stitches, lean
  src/stitch/cat.rs       letters into satin columns by their chordal axis (strokes, joins, mitres)
  src/stitch/columns.rs   shapes that branch or have holes, cut into satin columns (`cut`)
  src/stitch/stroke.rs    running / triple-run stitch
  src/boolean.rs          polygon booleans and offsets (i_overlay)
  src/design.rs           planner: overlap removal, cap order, routing, trims
  src/route.rs            travel out of sight: a way through fills and under what covers
  src/checks.rs           digitizing checks (sizes, widths, lettering, hoop)
  src/machine/profile.rs  machine profiles: hoops and file format, built in (profiles.json) or your own
  src/formats/            PES (+PEC), DST, EXP, JEF, VP3, Skitch PEN writers;
                          PES/PEC/DST/EXP/JEF readers; preview; worksheet
  src/machine/            Skitch Bluetooth protocol (+ btleplug client, `ble` feature)
  src/studio/             editor (egui on OpenGL via glow) + MCP server (`gui` feature)
  src/mcp_bridge.rs       stdio ↔ HTTP bridge for MCP clients that launch a command
```

## Build

```sh
cargo build --release                        # CLI + MCP bridge, no system deps
cargo build --release --features gui,ble     # + the studio editor and Skitch upload
```

Linux needs the usual X11/Wayland and OpenGL dev libraries for `gui`. libdbus
is vendored for `ble`.

## Stitch types

| Type | What it does | Works on |