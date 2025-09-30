

<p align="center">
    <img src="images/logo.png" alt="SSHM Logo" width="120" />
</p>

# 🚀 SSHM - SSH Manager

[![Go](https://img.shields.io/badge/Go-1.23+-00ADD8?style=for-the-badge&logo=go)](https://golang.org/)
[![Release](https://img.shields.io/github/v/release/Gu1llaum-3/sshm?style=for-the-badge)](https://github.com/Gu1llaum-3/sshm/releases)
[![License](https://img.shields.io/github/license/Gu1llaum-3/sshm?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey?style=for-the-badge)](https://github.com/Gu1llaum-3/sshm/releases)

> **A modern, interactive SSH Manager for your terminal** 🔥

SSHM is a beautiful command-line tool that transforms how you manage and connect to your SSH hosts. Built with Go and featuring an intuitive TUI interface, it makes SSH connection management effortless and enjoyable.

<p align="center">
    <a href="images/sshm.gif" target="_blank">
        <img src="images/sshm.gif" alt="Demo SSHM Terminal" width="800" />
    </a>
    <br>
    <em>🖱️ Click on the image to view in full size</em>
</p>

## ✨ Features

### 🚀 **Core Capabilities**
- **🎨 Beautiful TUI Interface** - Navigate your SSH hosts with an elegant, interactive terminal UI
- **⚡ Quick Connect** - Connect to any host instantly through the TUI or the CLI with `sshm <host>`
- **🔄 Port Forwarding** - Easy setup for Local, Remote, and Dynamic (SOCKS) forwarding with history persistence
- **📝 Easy Management** - Add, edit, move, and manage SSH configurations seamlessly
- **🏷️ Tag Support** - Organize your hosts with custom tags for better categorization
- **🔍 Smart Search** - Find hosts quickly with built-in filtering and search
- **📝 Real-time Status** - Live SSH connectivity indicators with asynchronous ping checks and color-coded status
- **🔔 Smart Updates** - Automatic version checking with update notifications
- **📈 Connection History** - Track your SSH connections with last login timestamps

### 🛠️ **Technical Features**
- **🔒 Secure** - Works directly with your existing `~/.ssh/config` file
- **📁 Custom Config Support** - Use any SSH configuration file with the `-c` flag
- **📂 SSH Include Support** - Full support for SSH Include directives to organize configurations across multiple files
- **⚙️ SSH Options Support** - Add any SSH configuration option through intuitive forms
- **🔄 Automatic Conversion** - Seamlessly converts between command-line and config formats
- **🔄 Automatic Backups** - Backup configurations automatically before changes
- **✅ Validation** - Prevent configuration errors with built-in validation
- **🔗 ProxyJump Support** - Secure connection tunneling through bastion hosts
- **⌨️ Keyboard Shortcuts** - Power user navigation with vim-like shortcuts
- **🌐 Cross-platform** - Supports Linux, macOS (Intel & Apple Silicon), and Windows
- **⚡ Lightweight** - Single binary with no dependencies, zero configuration required

## 🚀 Quick Start

### Installation

**Homebrew (Recommended for macOS):**
```bash
brew install Gu1llaum-3/sshm/sshm
```

**Unix/Linux/macOS (One-line install):**
```bash
curl -sSL https://raw.githubusercontent.com/Gu1llaum-3/sshm/main/install/unix.sh | bash
```

**Windows (PowerShell):**
```powershell
irm https://raw.githubusercontent.com/Gu1llaum-3/sshm/main/install/windows.ps1 | iex
```

**Alternative methods:**

*Linux/macOS:*
```bash
# Download specific release
wget https://github.com/Gu1llaum-3/sshm/releases/latest/download/sshm-linux-amd64.tar.gz

# Extract and install
tar -xzf sshm-linux-amd64.tar.gz
sudo mv sshm-linux-amd64 /usr/local/bin/sshm
```

*Windows:*
```powershell
# Download and extract
Invoke-WebRequest -Uri "https://github.com/Gu1llaum-3/sshm/releases/latest/download/sshm-windows-amd64.zip" -OutFile "sshm-windows-amd64.zip"
Expand-Archive sshm-windows-amd64.zip -DestinationPath C:\tools\
# Add C:\tools to your PATH environment variable
```

## 📖 Usage

### Interactive Mode

Launch SSHM without arguments to enter the beautiful TUI interface:

```bash
sshm
```

**Navigation:**
- `↑/↓` or `j/k` - Navigate hosts
- `Enter` - Connect to selected host
- `a` - Add new host
- `e` - Edit selected host
- `d` - Delete selected host
- `m` - Move host to another config file (requires SSH Include directives)
- `f` - Port forwarding setup
- `q` - Quit
- `/` - Search/filter hosts

**Real-time Status Indicators:**
- 🟢 **Online** - Host is reachable via SSH
- 🟡 **Connecting** - Currently checking host connectivity
- 🔴 **Offline** - Host is unreachable or SSH connection failed
- ⚫ **Unknown** - Connectivity status not yet determined

**Sorting & Filtering:**
- `s` - Switch between sorting modes (name ↔ last login)
- `n` - Sort by **name** (alphabetical)
- `r` - Sort by **recent** (last login time)
- `Tab` - Cycle between filtering modes
- Filter by **name** (default) - Search through host names
- Filter by **last login** - Sort and filter by most recently used connections

The interactive forms will guide you through