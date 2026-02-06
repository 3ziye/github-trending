# WSL Dashboard

<p align="center">
  <img src="assets/logo/logo.png" width="128" height="128" />
</p>

A modern, high-performance, and lightweight WSL (Windows Subsystem for Linux) instance management dashboard. Built with Rust and Slint for a premium native experience.

---

[![Rust](https://img.shields.io/badge/rust-v1.92+-orange.svg)](https://www.rust-lang.org)
[![Slint](https://img.shields.io/badge/UI-Slint-blue.svg)](https://slint.dev)
[![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg)](LICENSE)

I18N: [简体中文](./manual/README_zh_CN.md) | [繁體中文](./manual/README_zh_TW.md) | English | [日本語](./manual/README_ja.md) | [Français](./manual/README_fr.md) | [Español](./manual/README_es.md) | [Русский](./manual/README_ru.md) | [Português](./manual/README_pt.md) | [Deutsch](./manual/README_de.md) | [Italiano](./manual/README_it.md) | [Türkçe](./manual/README_tr.md) | [Bahasa Indonesia](./manual/README_id.md) | [हिन्दी](./manual/README_hi.md) | [বাংলা](./manual/README_bn.md)

---

## 🖼️ Screenshots

### Home (Light & Dark Mode)
<p align="center">
  <img src="assets/screenshot/home.png" width="48%" />
  <img src="assets/screenshot/home-dark.png" width="48%" />
</p>

### Add Instance & Settings
<p align="center">
  <img src="assets/screenshot/add.png" width="48%" />
  <img src="assets/screenshot/settings.png" width="48%" />
</p>

### About & Collapse menu
<p align="center">
  <img src="assets/screenshot/about.png" width="48%" />
  <img src="assets/screenshot/collapsed.png" width="48%" />
</p>

## 🎬 Operation Demo

Below is a demonstration of the WSL Dashboard in action:

![WSL Dashboard Demo](assets/screenshot/demo.gif)

## 🚀 Key Features

- Intuitive GUI with dark mode support and smooth animations.
- One-click management for all your WSL distributions (Start, Stop, Terminate, Unregister).
- Quick access to distribution terminals, VS Code, and File Explorer.
- Comprehensive distribution settings: Set as default, auto-startup on boot, and custom directory paths.
- Real-time WSL instance status monitoring and display.
- Export and backup to `.tar` or compressed `.tar.gz` archives.
- Import and clone instances from backups or existing distributions.
- Move distribution to any specified directory (VHDX migration) to save C: drive space.
- Smart distribution installation from Microsoft Store or GitHub.
- Built-in RootFS download helper for manual installs.
- Detailed insights into VHDX file location, virtual disk size, and actual disk usage.

## System Requirements

- Windows 10 or Windows 11 with WSL enabled (WSL 2 recommended).
- At least one WSL distribution installed, or permission to install new ones.
- 64-bit CPU; 4 GB RAM or more recommended for smooth multi-distro usage.

## 📦 Installation

### Option 1: Download prebuilt binary

The easiest way to get started is to use the precompiled release:

1. Go to the [GitHub Releases](https://github.com/owu/wsl-dashboard/releases) page.
2. Download the latest `wsldashboard` executable for Windows.
3. Extract (if packaged) and run `wsldashboard.exe`.

No installer is required; the app is a single portable binary.

### Option 2: Build from source

Ensure you have the Rust toolchain (Rust 1.92+ or newer) installed.

1. Clone the repository:

   ```powershell
   git clone https://github.com/owu/wsl-dashboard.git
   cd wsl-dashboard
   ```

2. Build and run:

   - For development:

     ```powershell
     cargo run
     ```

   - Optimized release build:

     ```powershell
     cargo run --release
     ```

   - Using the build script (recommended for producing release binaries):

     > The build script requires the `x86_64-pc-windows-gnu` toolchain.

     ```powershell
     .\build\scripts\build.ps1
     ```

## 🧭 Usage Overview

- Manage existing distributions: start, stop, terminate, unregister, or set as default distro from the main view.
- Configure distributions: set auto-startup behavior and customize Terminal/VS Code launch directories.
- Open tools quickly: launch a distro in your terminal, VS Code, or File Explorer with a single click.
- Create new instances: use the Add Instance view to install from the Microsoft Store, download RootFS images, or clone existing distributions.
- Backup and restore: export distributions to `.tar` / `.tar.gz` archives and import them later or on another machine.
- Move distribution: move the distribution to the specified directory for better storage management.
- Monitor status: keep an eye on real-time distribution status and storage usage while WSL Dashboard runs.

## ⚙️ Configuration & Logs

All configuration is managed through the Settings view:

- Choose the default installation directory for new WSL instances.
- Configure the log directory and log level (Error / Warn / Info / Debug / Trace).
- Pick the UI language or let it follow the system language.
- Toggle dark mode and whether the app can auto-shutdown WSL after operations.
- Configure how often the app checks for updates (daily, weekly, biweekly, monthly)