<img width="897" height="427" alt="image" src="https://github.com/user-attachments/assets/74400c8b-9d7d-49ce-8de7-45dfd556e256" />

<div align="center">

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Rust](https://img.shields.io/badge/rust-1.77+-orange.svg)
![Tauri](https://img.shields.io/badge/tauri-v2-blue.svg)
![Platform](https://img.shields.io/badge/platform-linux-lightgrey.svg)
![Version](https://img.shields.io/github/v/release/gustavosett/Windows-11-Clipboard-History-For-Linux?color=green)
![Sites](https://img.shields.io/website?down_color=red&down_message=offline&up_color=green&up_message=online&url=https%3A%2F%2Fclipboard.gustavosett.dev)

**A beautiful, [Windows 11-style Clipboard History Manager for Linux](https://clipboard.gustavosett.dev).**

*Works on Wayland & X11.*

Built with 🦀 **Rust** + ⚡ **Tauri v2** + ⚛️ **React** + 🎨 **Tailwind CSS**

[Features](#-features) • [Installation](#-installation) • [How to Use](#-how-to-use) • [Development](#-development)

</div>

---

## ✨ Features

- 🐧 **Wayland & X11 Support** - Uses OS-level shortcuts and `uinput` for pasting to support Wayland & X11.
- ⚡ **Global Hotkey** - Press `Super+V` or `Ctrl+Alt+V` to open instantly.
- 🖱️ **Smart Positioning** - Window follows your mouse cursor across multiple monitors.
- 📌 **Pinning** - Keep important items at the top of your list.
- 🖼️ **Rich Media** - Supports Images, Text, etc.
- 🎬 **GIF Integration** - Search and paste GIFs from Tenor directly into Discord, Slack, etc.
- 🤩 **Emoji Picker** - Built-in searchable emoji keyboard.
- 🏎️ **Performance** - Native Rust backend ensures minimal resource usage.
- 🛡️ **Privacy Focused** - History is stored locally and never leaves your machine.
- 🧙 **Setup Wizard** - First-run wizard guides you through permission setup, detects shortcut conflicts, and autostart configuration.

---

## 📥 Installation

### 🚀 Recommended: One-Line Install

This script automatically detects your distro and architecture (x86_64, ARM64), downloads the correct package, and sets up permissions.

```bash
curl -fsSL https://raw.githubusercontent.com/gustavosett/Windows-11-Clipboard-History-For-Linux/master/scripts/install.sh | bash
```

> **Note:** The installer uses ACLs to grant immediate access to input devices — **no logout required!**

### 📦 Manual Installation

Download the latest release from the [Releases Page](https://github.com/gustavosett/Windows-11-Clipboard-History-For-Linux/releases).

<details>
<summary><b>Debian / Ubuntu / Pop!_OS / Linux Mint</b></summary>

**Option 1: APT Repository (Recommended - enables automatic updates)**

```bash
# Add the Cloudsmith repository
curl -1sLf 'https://dl.cloudsmith.io/public/gustavosett/clipboard-manager/setup.deb.sh' | sudo -E bash

# Install the package
sudo apt update
sudo apt install win11-clipboard-history

# For immediate paste access (without logout):
sudo setfacl -m u:$USER:rw /dev/uinput
```

**Option 2: Direct Download**

```bash
# Download and install (replace VERSION with actual version)
sudo apt install ./win11-clipboard-history_VERSION_amd64.deb

# The package sets up udev rules automatically.
# For immediate paste access (without logout):
sudo setfacl -m u:$USER:rw /dev/uinput
```

</details>

<details>
<summary><b>Fedora / RHEL / CentOS</b></summary>

**Option 1: DNF Repository (Recommended - enables automatic updates)**

```bash
# Add the Cloudsmith repository
curl -1sLf 'https://dl.cloudsmith.io/public/gustavosett/clipboard-manager/setup.rpm.sh' | sudo -E bash

# Install the package
sudo dnf install win11-clipboard-history

# For immediate paste access (without logout):
sudo setfacl -m u:$USER:rw /dev/uinput
```

**Option 2: Direct Download**

```bash
# Download and install (replace VERSION with actual version)
sudo dnf install ./win11-clipboard-history-VERSION-1.x86_64.rpm

# For immediate paste access (without logout):
sudo setfacl -m u:$USER:rw /dev/uinput
```

</details>

<details>
<summary><b>Arch Linux (AUR)</b></summary>

```bash
# Using yay
yay -S win11-clipboard-history-bin

# Or using paru
paru -S win11-clipboard-history-bin
```

</details>

<details>
<summary><b>AppImage (Universal)</b></summary>

**Quick Start**

```bash
# Download the AppImage from the releases page
chmod +x win11-clipboard-history_*.AppImage

# Grant uinput access for paste simulation
sudo setfacl -m u:$USER:rw /dev/uinput

# Run the app
./win11-clipboard-history_*.AppImage
```

**Full Installation (recommended for regular use)**

```bash
# Create directories
mkdir -p ~/.local/bin ~/.local/share/applications

# Move AppImage to local bin
mv win11-clipboard-history_*.AppImage ~/.local/bin/win11-clipboard-history.AppImage
chmod +x ~/.local/bin/win11-clipboard-history.AppImage

# Create a wrapper script for clean environment
cat > ~/.local/bin/win11-clipboard-history << 'EOF'
#!/bin/bash
unset LD_LIBRARY_PATH LD_PRELOAD GTK_PATH GIO_MODULE_DIR
export GDK_BACKEND="x11" NO_AT_BRIDGE=1
exec "$HOME/.local/bin/win11-clipboard-history.AppI