<p align="center">
  <img src="docs/logo.png" alt="HYDRA Logo" width="180">
</p>

<h1 align="center">Hydra Download Manager (HDM)</h1>

<p align="center">
  <strong>Fast, resilient, multi-source download manager and accelerator for Windows, macOS, and Linux.</strong><br>
  <a href="https://hydra.javad.dev"><strong>https://hydra.javad.dev</strong></a>
</p>

<p align="center">
  <a href="https://crates.io/crates/hya-core"><img src="https://img.shields.io/crates/v/hya-core.svg?style=flat-square" alt="crates.io"></a>
  <a href="https://docs.rs/hya-core"><img src="https://img.shields.io/docsrs/hya-core?style=flat-square" alt="docs.rs"></a>
  <a href="https://codecov.io/gh/ja7ad/hydra"><img src="https://codecov.io/gh/ja7ad/hydra/graph/badge.svg?token=bQuMUwagma" alt="Coverage"/></a>
  <a href="https://github.com/ja7ad/hydra/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/ja7ad/hydra/ci.yml?branch=main&label=CI&style=flat-square" alt="CI Status"></a>
  <a href="LICENSING.md"><img src="https://img.shields.io/badge/license-GPL--3.0--or--later%20%7C%20MIT%2FApache--2.0-blue?style=flat-square" alt="License"></a>
  <img src="https://img.shields.io/badge/rust-2021%20edition-orange?style=flat-square" alt="Rust Edition">
</p>

---

## Contents

- [Overview](#overview)
- [Key Features](#key-features)
  - [Engine](#engine)
  - [CLI](#cli)
  - [Desktop GUI](#desktop-gui)
- [Installation](#installation)
  - [Homebrew (macOS / Linux)](#homebrew-macos--linux)
  - [Linux Packages (Ubuntu PPA / Fedora COPR / Arch Linux AUR)](#linux-packages-ubuntu-ppa--fedora-copr--arch-linux-aur)
  - [AppImage (portable, self-updating)](#appimage-portable-self-updating)
  - [Quick Install (prebuilt binaries)](#quick-install-prebuilt-binaries)
  - [From Source](#from-source)
  - [Browser Extension](#browser-extension)
- [Uninstall](#uninstall)
  - [Quick Uninstall (prebuilt installs)](#quick-uninstall-prebuilt-installs)
- [Usage](#usage)
  - [Basic Download](#basic-download)
  - [Multi-Connection & Mirror Sources](#multi-connection--mirror-sources)
  - [Metalink](#metalink)
  - [CLI Compatibility (`wget` / `curl` Mode)](#cli-compatibility-wget--curl-mode)
  - [Interactive Queue Manager (TUI)](#interactive-queue-manager-tui)
  - [Remote Checksum Lookup & Verification](#remote-checksum-lookup--verification)
  - [Portable GUI Profile](#portable-gui-profile)
- [Benchmark](#benchmark)
  - [A fair 100 ms path](#a-fair-100-ms-path)
  - [Four public mirrors](#four-public-mirrors)
  - [Desktop download managers](#desktop-download-manager)
- [Embedding HYDRA — `libhydra`](#embedding-hydra--libhydra)
  - [Platform guides](#platform-guides)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

**Hydra Download Manager (HDM)** is an open-source, high-performance network file retriever and download accelerator designed for speed, resilience, and adaptability. It dynamically partitions downloads across multiple connections and independent mirror sources, continuously rebalancing work to maximize throughput without stalling on slow peers. It ships as both a `wget`/`curl`-compatible CLI and a cross-platform desktop download manager with browser integration.

<p align="center">
  <img src="docs/img/screenshot.jpg" alt="Hydra Download Manager" width="720">
</p>

## Key Features

<table>
<tr><td valign="top" width="33%">

### Engine

- **Adaptive Concurrency** — splits files across connections and mirrors, rebalancing live
- **Range Stealing** — reassigns work from slow peers to fast ones automatically
- **Stall Detection** — statistical estimators catch degraded connections early
- **Broad Protocol Support** — HTTP(S), FTP, CONNECT tunneling, SOCKS4/4a/5
- **Integrity Checks** — checksum manifests plus Reed–Solomon bitrot protection
- **Flat Memory Use** — direct positioned writes keep RAM usage constant

</td><td valign="top" width="33%">

### CLI

- **`hydra` or `hya`** — the same CLI under a short second name, on every platform
- **`wget` / `curl` Compatible** — drop-in flag and dialect support
- **Interactive TUI** — manage, pause, resume, and monitor queued downloads
- **Smart File Sorting** — content-based type detection and auto-sort
- **Remote Checksum Lookup** — verify server-advertised digests before or after download

</td><td valign="top" width="33%">

### Desktop GUI

- **Cross-Platform App** — Windows, macOS, and Linux with categories and progress detail
- **Browser Integration** — Chrome, Edge, Firefox, and Safari extensions hand off downloads
- **Queue & Scheduler** — scheduled start/stop times with retry tracking
- **Desktop Niceties** — tray icon, sounds, launch-on-startup, localized UI
- **Portable Profile** — `hydra-gui --config ./here` keeps settings, downloads list and logs in that directory

</td></tr>
</table>

---

## Installation

### Homebrew (macOS / Linux)

**CLI**:

```bash
brew install ja7ad/tap/hydra
```

**macOS Desktop App (GUI)**:

```bash
brew install --cask ja7ad/tap/h