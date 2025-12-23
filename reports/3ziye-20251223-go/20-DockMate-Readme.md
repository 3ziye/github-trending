
<h1 align="center">DockMate 🐳</h1>
<p align="center"><b>A terminal-based Docker container manager that actually works.</b></p>

<p align="center">
  <span><img src="https://wakatime.com/badge/github/shubh-io/DockMate.svg" /></span>
  <span><img src="https://img.shields.io/github/stars/shubh-io/DockMate?style=flat&logo=github" /></span>
  <span><img src="https://img.shields.io/github/v/release/shubh-io/DockMate?color=green" /></span>
  <span><img src="https://img.shields.io/github/license/shubh-io/DockMate" /></span>
  <span><img src="https://img.shields.io/badge/Go-1.24+-00ADD8?logo=go&logoColor=white" /></span>
  <span><img src="https://img.shields.io/badge/TUI-Bubble%20Tea-blue?logo=go&logoColor=white" /></span>
  <span><img src="https://img.shields.io/badge/Platform-Linux%20%7C%20macOS-blue?style=flat&logo=linux&logoColor=white" /></span>
</p>

> **Note**: Previously named **DockWatch** (renamed to avoid confusion with another project).

![DockMate demo gif](assets/demo.gif)

---

## Overview

DockMate is a **TUI (Text User Interface)** for **managing Docker containers** directly from your terminal.  
Think of `htop`, but for Docker.

- See live container stats at a glance
- Start, stop, restart, and remove containers with single keypresses
- Jump into logs or an interactive shell instantly
- Change Runtime (switch Docker ⇄ Podman)
---

## Comparison
<div align="center">

### DockMate vs LazyDocker

| Feature | DockMate | LazyDocker |
|---------|----------|------------|
| **Installation** | One-command + Homebrew | Homebrew + Multiple package managers |
| **Auto-update** | ✅ Built-in (`dockmate update`) | ❌ Manual updates required |
| **Container loading** | ✅ **Fast (< 2 seconds)** | Slower (variable) |
| **UI Framework** | ✅ **Bubble Tea (modern)** | gocui (older library) |
| **Dependencies** | ✅ **Minimal** (bash, curl) | Multiple system dependencies |
| **Resource usage** | ✅ **Lightweight** | Heavier footprint |
| **Container stats** | ✅ Real-time (CPU, memory, network, disk I/O) | Real-time + ASCII graphs |
| **Docker Compose** | ✅ Full support | ✅ Full support |
| **Interactive logs** | ✅ | ✅ |
| **Shell access** | ✅ One keypress | ✅ |
| **Multi-runtime support** | ✅ **Docker + Podman (native)** | Docker only (Podman via workaround) |
| **Runtime switching** | ✅ **In TUI settings** | ❌ Restart + change env vars |
| **Podman Compose** | ✅ **Auto-detected** | ⚠️ Manual configuration |
| **Image management** | ⏳ Planned | ✅ Layer inspection & pruning |
| **Metrics graphs** | ❌ Text-based (lighter) | ✅ Customizable ASCII graphs |
| **Mouse support** | ❌ Keyboard-focused | ✅ |
| **Best for** | Speed, simplicity, **+ Podman support** | Feature-rich Docker power users |

</div>

### Choose DockMate if you:
- ⚡ Want a **fast, lightweight** Docker TUI
- ⌨️ Prefer **keyboard-driven** workflows
- 📦 Value **simplicity** and **auto-updates**
- 🔄 **Bonus:** Need Podman support (native, zero config)

### Choose LazyDocker if you:
- 📊 Need **ASCII graphs** and visualizations
- 🔍 Want **image layer inspection**
- 🖱️ Prefer **mouse support**
- 🏆 Want a **mature, battle-tested** tool

**Both are excellent - DockMate for speed & simplicity, LazyDocker for advanced features!** 🐳

---

## Features

### 🐳 Docker Management
- Docker and Docker Compose support
- Live metrics (CPU, memory, network I/O, disk I/O)
- Start/stop/restart with one keypress
- Real-time log streaming
- Interactive shell access
- Sort by any column

### ⚡ Performance & UX
- Fast startup 
- Lightweight 
- Fully keyboard-driven
- Persistent settings (`~/.config/dockmate/config.yml`)
- Configurable auto-refresh
- Clean terminal resizing

### 🚀 Bonus: Multi-Runtime Support
- Native Podman support
- Runtime switching (Docker ⇄ Podman)
- Supports Podman Compose
- Helpful error guidance for Podman setup

## Requirements

### Runtime
- **Docker** (recommended) or **Podman** installed and running

### Operating System
- **Linux** (Ubuntu, Debian, Fedora, Arch, etc.)
- **macOS**

### Building from Source (optional)
- **Go 1.24+** required

---

## System Dependencies

DockMate uses the following system tools:

- **curl** - For one-command installation

**macOS:** systemctl checks are automatically skipped.


---

## Installation

### 🍺 Homebrew (Recommended)

```
brew install shubh-io/tap/dockmate
```

Works on both **Linux** and **macOS**. Easiest way to install and update.

### 📦 Quick Install Script

```
curl -fsSL https://raw.githubusercontent.com/shubh-io/DockMate/main/install.sh | sh
```

If that ever fails on your setup, use the two-step variant:

```
curl -fsSL https://raw.githubusercontent.com/shubh-io/DockMate/main/install.sh -o install.sh
sh install.sh
```

### Alternative: User-local installation

If you encounter permission issues with `/usr/local/bin`, install to your user directory instead:

```
curl -fsSL https://raw.githubusercontent.com/shubh-io/dockmate/main/install.sh | INSTALL_DIR=$HOME/.local/bin sh
```

Then add to your PATH. Choose b