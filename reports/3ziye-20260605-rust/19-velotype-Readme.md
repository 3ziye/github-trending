# Velotype

<div align="center">

![Velotype banner](./assets/icon/velotype-banner.png)

**A Rust + GPUI native Markdown editor with WYSIWYG and source editing modes.**

[Editor Showcase](./assets/showcase/showcase.md)

[English](README.md) | [中文](docs/README.zh-CN.md)

[![Rust](https://img.shields.io/badge/Rust-2024-f74c00?logo=rust&logoColor=white)](https://www.rust-lang.org/)
[![GPUI](https://img.shields.io/badge/GUI-GPUI%200.2-4b7bec)](https://gpui.rs/)
[![Platforms](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-2ea44f)](#quick-start)
[![Portable](https://img.shields.io/badge/app-portable%20single%20binary-8b5cf6)](#features)
[![Export](https://img.shields.io/badge/export-HTML%20%7C%20PDF-0ea5e9)](#features)
[![Release](https://img.shields.io/badge/releases-GitHub-181717?logo=github)](https://github.com/manyougz/velotype/releases)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

</div>

Velotype is a block-based Markdown editor built with Rust and [GPUI](https://gpui.rs/). It supports both WYSIWYG-style rendered editing and Markdown source-text editing.

The project is still early, but the core direction is stable: native UI, instant rendered editing, source-text fallback, canonical Markdown serialization, and customization across color, typography, spacing, and layout tokens.

## Features

- **🧱 Block model:** Markdown structure is represented as editable blocks, keeping document structure clear, controllable, and extensible without a preview-pane synchronization loop.
- **⚡ Native UI:** Desktop-native rendering based on GPUI, without depending on Electron, Tauri, or any WebView shell.
- **✍️ Editing modes:** Velotype supports both WYSIWYG-style rendered editing and raw Markdown source editing for common authoring workflows.
- **🚀 Performance and stability:** Rust drives parsing, state updates, and rendering; the parser follows a standard-oriented strategy and falls back to raw Markdown in unstable cases.
- **🎨 Theme customization:** Themes can customize global colors, typography, spacing, menus, dialogs, editor layout tokens, and language packs.
- **📦 Portable single file:** After compilation, Velotype exists as a single executable file. It requires no installation, stays natively portable, and targets Windows, Linux, and macOS.

Velotype already supports exporting the current Markdown document to HTML and PDF. HTML export maps the active theme into CSS, while PDF export reuses the same themed HTML pipeline so visual output stays consistent.

Velotype targets Windows, Linux, and macOS. The app is naturally suitable for distribution as a standalone binary; release builds can run directly without installation.

## Quick Start

### 1. Download a release

Download the build for your platform from the [Velotype Releases](https://github.com/manyougz/velotype/releases) page.

#### Windows and Linux Users

- Download the corresponding `.zip` or `.tar.gz` file
- Unzip to get the executable
- Run directly

#### macOS Users

Two installation options are available:

**Option 1: Single .app package**
- Download `velotype-*.zip` file
- Unzip to get `Velotype.app`
- Drag to `/Applications` or any location
- Double-click to run

**Option 2: PKG Installer(Recommended)**
- Download `velotype-*.pkg` file
- Double-click to run the installer
- Automatically installs to `/Applications`
- Automatically configures command-line tool `velotype`

> **If using the PKG installer:** The CLI command is configured automatically during installation. The PKG installer manages the symlink automatically via its `postinstall` / `preuninstall` scripts. You can still manually trigger installation/uninstallation while in use. 
> 
> **If using the .app package:** Install or Uninstall the CLI command directly from the menu:
> 1. Open Velotype.app
> 2. Click the menu **Help → Install CLI Command**
> 3. Enter administrator password
> 4. Done!
>
> Be careful, if you move or delete `Velotype.app`, the symlink will automatically become invalid. Running `velotype` will report "command not found".

### 2. Build from source

Prerequisites:

- Git
- A Rust toolchain with Rust 2024 edition support
- Cargo
- Platform-native build dependencies required by GPUI and the system toolchain

Build Velotype locally:

```bash
git clone https://github.com/manyougz/velotype.git
```

```bash
cargo build --release
```

If everything works, the build artifact will be stored under `target/release`. You can use the executable directly.

## Roadmap

Velotype already supports almost all basic Markdown syntax and most commonly used extended Markdown syntax, including headings, paragraphs, lists, task lists, quotes, callouts, tables, code blocks, inline formatting, links, reference-style links and images, footnotes, standalone images, comment blocks, and safe native HTML handling.

Syntax support will continue to improve. Planned work includes:

- [x] ~~Optimize the parsing and rendering capabilities for extremel