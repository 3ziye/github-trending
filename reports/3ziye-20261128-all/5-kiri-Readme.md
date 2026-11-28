<div align="center">

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="brand/logo/kiri-horizontal-dark.svg">
    <img src="brand/logo/kiri-horizontal-light.svg" alt="Kiri" width="300">
  </picture>
</p>

<h1>Kiri: a tiny, fast container runtime for macOS, Windows and Linux</h1>

<p>Docker Desktop is slow to start and heavy when idle. Kiri is a lightweight replacement written in Rust. It runs your Docker images and works with the <code>docker</code> CLI, Compose and buildx you already use.</p>

<p align="center">
  <a href="https://github.com/libracoder/kiri/actions/workflows/ui-tests.yml?query=branch%3Amain"><img src="https://img.shields.io/github/actions/workflow/status/libracoder/kiri/ui-tests.yml?branch=main&style=for-the-badge&label=CI" alt="CI status"></a>
  <a href="https://github.com/libracoder/kiri/releases/latest"><img src="https://img.shields.io/github/v/release/libracoder/kiri?style=for-the-badge&label=release&color=2f6feb" alt="Latest release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg?style=for-the-badge" alt="Apache 2.0 License"></a>
  <a href="https://discord.gg/K5A8wuqcC"><img src="https://img.shields.io/badge/Discord-Join%20Us-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord"></a>
  <a href="crates/kiri/src/ui/lang"><img src="https://img.shields.io/badge/languages-42-2ea043?style=for-the-badge" alt="42 languages"></a>
</p>

<p align="center">
  <strong>
    <a href="#quick-start">Quickstart</a> ·
    <a href="https://docs.runkiri.com">Docs</a> ·
    <a href="docs/features.md">Features</a> ·
    <a href="https://runkiri.com/releases/">Download</a> ·
    <a href="SECURITY.md">Security</a> ·
    <a href="README.zh-CN.md">简体中文</a>
  </strong>
</p>

<p align="center">
  <img src="docs/images/kiri-window.png" alt="The Kiri window, showing containers grouped by Compose project with their state, ports, local domains and size" width="900">
</p>

</div>

---

## Before you begin

Make sure you have one of:

- macOS 14 or later, on Apple silicon or Intel
- Windows 10 or 11 with WSL 2, on x86-64 or Arm
- Linux (Ubuntu, Fedora and others)

## Step 1: Install and start Kiri

macOS, with Homebrew:

```bash
brew install --cask libracoder/kiri/kiri
```

Or download the installer for your system:

| Platform | Get it |
|----------|--------|
| macOS 14+ (Apple silicon or Intel) | `.dmg` from [runkiri.com/releases](https://runkiri.com/releases/), or `brew install --cask libracoder/kiri/kiri` |
| Windows 10 and 11 (x86-64 or Arm, through WSL 2) | `.msi` from [runkiri.com/releases](https://runkiri.com/releases/) |
| Linux (Ubuntu, Fedora and others) | `.deb` or `.rpm` from [runkiri.com/releases](https://runkiri.com/releases/) |

The first time you open Kiri, it sets up a `kiri` Docker context. Kiri updates itself, and checks each new release's signature first.

Then run your first container:

```bash
docker --context kiri run --rm alpine echo hello
```

---

## Table of Contents

- [Before you begin](#before-you-begin)
- [Install and start Kiri](#step-1-install-and-start-kiri)
- [Why Kiri?](#why-kiri)
- [Quick Start](#quick-start)
- [Features](#features)
- [Docker commands](#docker-commands)
- [Benchmarks](#benchmarks)
- [Comparison](#comparison)
- [How Kiri Works](#how-kiri-works)
- [Documentation](#documentation)
- [Roadmap](#roadmap)
- [Community](#community)
- [Security](#security)
- [License](#license)

---

## Why Kiri?

Kiri runs containers in one small Linux VM (or straight on the kernel on
Linux) and speaks the Docker Engine API, so your tools just work. The name
comes from the Igbo word *ntakịrị*, "small".

- **Fast**: a container starts and exits in about 2.5 ms through the Docker API. That's around 80 times faster than Docker Desktop.
- **Light**: the VM sleeps after 60 s idle, the daemon stays at about 15 MB, and it wakes in about 0.15 s.
- **Compatible**: `docker`, Compose, buildx, `docker login` and amd64 images through Rosetta.
- **Local domains**: `http://<name>.kiri.local`, with HTTPS from Kiri's own certificate authority.
- **More than containers**: a one-command Kubernetes cluster and Linux machines.
- **A native window** for containers, images, volumes and networks, plus a menu bar item.
- **In your language**: the window comes in 42 languages, on macOS, Windows and Linux alike.

---

## Quick Start

```sh
docker --context kiri run --rm alpine echo hello
docker --context kiri compose up -d
kiri k8s start                      # single-node Kubernetes as the `kiri` kubectl context
kiri machine create dev --distro ubuntu && kiri machine shell dev
kiri import                         # bring images, volumes and containers over from OrbStack or Docker Desktop
```

Docker's commands also work as `kiri` commands (`kiri run`, `kiri ps`,
`kiri compose up`, and so on), and always target Kiri.

---

## Features

| Area | What you get |
|------|--------------|
| **Containers** | The full lifecyc