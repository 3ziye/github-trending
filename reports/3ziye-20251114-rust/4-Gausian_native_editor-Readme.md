<div align="center">
  <img src="apps/desktop/resources/logo_whitebg.png" width="96" alt="Gausian logo">
  <h1>Gausian Native Editor</h1>
  <p><b>Fast, native video editor and preview tool</b> built in Rust with GPU rendering, timeline editing, and local ComfyUI integration.</p>

  <p>
    <a href="#-getting-started"><b>Get Started</b></a> •
    <a href="#-features"><b>Features</b></a> •
    <a href="#-architecture"><b>Architecture</b></a> •
    <a href="#-desktop-app"><b>Desktop</b></a> •
    <a href="#-cli"><b>CLI</b></a> •
    <a href="#-decoder--gstreamer-notes"><b>Decoders</b></a>
  </p>

  <p>
    <a href="https://gausian.xyz" target="_blank" rel="noopener noreferrer"><b>Visit gausian.xyz ↗</b></a>
    &nbsp;•&nbsp;
    <a href="https://discord.gg/JfsKWDBXHT" target="_blank" rel="noopener noreferrer"><b>Join our Discord ↗</b></a>
  </p>

  <p>
    <img alt="Rust" src="https://img.shields.io/badge/Rust-stable-orange">
    <img alt="UI" src="https://img.shields.io/badge/UI-egui%20%2B%20wgpu-8A2BE2">
    <img alt="Decoders" src="https://img.shields.io/badge/Decode-VideoToolbox%2FGStreamer-2CA5E0">
    <img alt="Platforms" src="https://img.shields.io/badge/Platforms-macOS%20%7C%20Windows%20%7C%20Linux-4CAF50">
    <a href="https://discord.gg/JfsKWDBXHT" target="_blank" rel="noopener noreferrer">
      <img alt="Discord" src="https://img.shields.io/badge/Discord-Join-5865F2?logo=discord&logoColor=white">
    </a>
    <a href="https://x.com/maeng313" target="_blank" rel="noopener noreferrer">
      <img alt="Follow on X" src="https://img.shields.io/badge/X-@maeng313-272a2d?logo=x&logoColor=white">
    </a>
  </p>
</div>

<hr/>

Gausian is a native editor focused on snappy preview, practical timeline tools, and smooth ingest/export. It supports hardware decoding (VideoToolbox on macOS, GStreamer pipelines cross‑platform), a WGPU preview pipeline, and integrates with a local ComfyUI for prompt‑based generation via an embedded WebView and auto‑import of outputs. A CLI is included for headless operations.

## ✨ Features

- GPU-accelerated preview (WGPU) with YUV→RGB shaders and readback
- Timeline editing, assets panel, project persistence (SQLite)
- Local ingest: FFmpeg/ffprobe probing, image/video/audio
- Exporters: FCPXML (1.9/1.10), FCP7 XML, EDL, JSON
- Proxy generation via GStreamer (ProRes/NVENC/VAAPI/software)
- Local ComfyUI: optional embedded WebView and auto‑import from a local ComfyUI output folder
- Screenplay/Storyboard helpers with LLM providers (OpenAI, etc.)
- Cross-platform desktop (macOS/Windows/Linux)

## 🚀 Getting Started

Prerequisites
- Rust (stable)
- FFmpeg/ffprobe on PATH
- GStreamer for proxy/advanced decode paths (recommended on all platforms; required for some proxies)
  - macOS (Homebrew): `brew install ffmpeg gstreamer gst-plugins-base gst-plugins-good gst-plugins-bad gst-libav`
  - Ubuntu/Debian: `sudo apt-get install -y ffmpeg gstreamer1.0-libav gstreamer1.0-plugins-{base,good,bad} gstreamer1.0-tools`
  - Windows: install a recent GStreamer build (system PATH), FFmpeg
 - ComfyUI (local, optional): required if you want to open the embedded WebView or auto‑import its outputs. Install and run ComfyUI locally (default at http://127.0.0.1:8188). See https://github.com/comfyanonymous/ComfyUI

Desktop app
```bash
cargo run --bin desktop
```

CLI (headless)
```bash
# Show commands
cargo run -p cli -- --help
```

<!-- Relay section removed: cloud connections not available yet. -->

## 🧩 Architecture

- apps/desktop (egui + wgpu)
  - Timeline, assets, GPU preview, audio engine, export
  - ComfyUI integration (local only): optional embedded WebView and auto‑import
- apps/comfywebview
  - Minimal native WebView window for ComfyUI
- crates/*
  - timeline — graph, tracks, commands
  - project — SQLite DB, migrations, asset/proxy/job tables
  - media-io — probe/export helpers, waveforms, encoders
  - renderer — WGPU renderer and WGSL shaders
  - exporters — FCPXML/FCP7/EDL/JSON
  - plugin-host — WASM/Python stubs
  - native-decoder — VideoToolbox (macOS) + optional GStreamer backend
  - cli — import/export/convert/analyze/new/encoders

<details>
  <summary>Project Structure (click to expand)</summary>

<pre><code>apps/
  desktop/          # egui UI, preview, decode, export
  comfywebview/     # lightweight native WebView for ComfyUI

crates/
  timeline/         # timeline data structures and commands
  project/          # SQLite DB + migrations
  media-io/         # probe, waveforms, proxy helpers
  renderer/         # WGPU renderer & shaders (WGSL)
  exporters/        # FCPXML/FCP7/EDL/JSON exporters
  plugin-host/      # plugin runtime stubs (WASM/Python)
  native-decoder/   # VideoToolbox & GStreamer backend
  cli/              # headless commands

formats/            # JSON specs (screenplay/storyboard)
</code></pre>
</details>

## 🖥 Desktop App

Build & run
```bash
cargo run --bin desktop
```

Optional features
- Embedded WebView (macOS only): `cargo run --bin desktop --features embed-web