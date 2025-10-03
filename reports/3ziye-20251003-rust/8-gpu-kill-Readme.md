# GPU Kill

A CLI tool for managing GPUs across NVIDIA, AMD, Intel, and Apple Silicon systems. Monitor, control, and secure your GPU infrastructure with ease.

## Community & Support

Join our Discord community for discussions, support, and updates:

[![Discord](https://img.shields.io/badge/Discord-Join%20our%20community-7289DA?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/KqdBcqRk5E)


## Features

- **Monitor GPUs**: Real-time usage, memory, temperature, and processes
- **Kill Processes**: Gracefully terminate stuck GPU processes
- **Security**: Detect crypto miners and suspicious activity
- **Guard Mode**: Policy enforcement to prevent resource abuse
- **Dashboard**: Web interface for cluster monitoring
- **Remote**: Manage GPUs across multiple servers
- **Multi-Vendor**: Works with NVIDIA, AMD, Intel, and Apple Silicon
- **AI Integration**: MCP server for AI assistant integration

## Requirements

### Build Performance

**For faster development builds:**
```bash
# Fast release build (recommended for development)
cargo build --profile release-fast

# Standard release build (optimized for production)
cargo build --release

# Maximum optimization (slowest, best performance)
cargo build --profile release-max
```

**Build times on typical hardware:**
- Debug build: ~3 seconds
- Release-fast: ~28 seconds  
- Release: ~28 seconds (improved from 76 seconds)
- Release-max: ~60+ seconds (maximum optimization)

### System Dependencies

**Linux (Ubuntu/Debian):**
```bash
sudo apt install build-essential libssl-dev pkg-config
```

**Linux (Fedora/RHEL/CentOS):**
```bash
sudo dnf install gcc gcc-c++ pkg-config openssl-devel
# or for older systems:
# sudo yum install gcc gcc-c++ pkg-config openssl-devel
```

**macOS:**
```bash
# Install Xcode command line tools
xcode-select --install
# OpenSSL is included with macOS
```

**Windows:**
- Install Visual Studio Build Tools
- OpenSSL is handled automatically by vcpkg

### GPU Drivers

- **NVIDIA**: NVIDIA drivers installed
- **AMD**: ROCm drivers installed  
- **Intel**: intel-gpu-tools package installed
- **Apple Silicon**: macOS with Apple Silicon (M1/M2/M3/M4)

### Build Requirements

- **OS**: Linux, macOS, or Windows
- **Rust**: 1.70+ (for building from source)

## Quick Start

### Install & Run
```bash
# Build from source (first build may take 2-3 minutes)
git clone https://github.com/kagehq/gpu-kill.git
cd gpu-kill
cargo build --release

# Or install via Cargo
cargo install gpukill

# Or one-liner installers (recommended)
# macOS/Linux
curl -fsSL https://raw.githubusercontent.com/kagehq/gpu-kill/refs/heads/main/scripts/install.sh | sh
# Windows (PowerShell)
irm https://raw.githubusercontent.com/kagehq/gpu-kill/refs/heads/main/scripts/install.ps1 | iex

# List your GPUs
gpukill --list

# Watch GPU usage in real-time
gpukill --list --watch
```

### Dead-simple cheatsheet
```bash
# Live watch (alias)
gpukill watch            # = gpukill --list --watch

# Kill job by PID (positional alias)
gpukill 12345            # = gpukill --kill --pid 12345

# Free a specific GPU index (kill all jobs on GPU 0)
gpukill --kill --gpu 0   # add --batch to actually kill; preview without it

# Force reset a GPU (shorthand)
gpukill --reset 0        # = gpukill --reset --gpu 0

# Safe mode: dry-run first (no changes)
gpukill 12345 --safe     # alias: --dry-run

# Bring up the backend API (and optionally open dashboard)
gpukill up               # = gpukill --server --server-port 8080
gpukill up --open        # tries to open http://localhost:3000
```

## Dashboard

Start the web interface for cluster monitoring:

```bash
# 1. Start the backend API server
gpukill --server --server-port 8080

# 2. Start the dashboard UI (in a new terminal)
cd dashboard
npm install  # First time only
npm run dev

# 3. Access the dashboard
open http://localhost:3000
```

**Note**: You need both the backend server (port 8080) and frontend UI (port 3000) running for the dashboard to work.

![GPU Kill Dashboard](dashboard/public/screenshot.png)

The dashboard provides:
- **Real-time monitoring** of all GPUs
- **Security detection** with threat analysis
- **Policy management** for resource control
- **Cluster overview** with Magic Moment insights

## MCP Server

GPU Kill includes a MCP server that enables AI assistants to interact with GPU management functionality:

- **Resources**: Read GPU status, processes, audit data, policies, and security scans
- **Tools**: Kill processes, reset GPUs, scan for threats, create policies

```bash
# Start the MCP server
cargo run --release -p gpukill-mcp

# Server runs on http://localhost:3001/mcp
```

## Usage

Ask your AI to use the tools.

```text
What GPUs do I have and what's their current usage?
```

```text
Kill the Python process that's stuck on GPU 0
```

```text
Kill all training processes that are using too much GPU memory
```

```text
Show me GPU usage and kill any stuck processes
```

```text
Scan for crypto miners and suspicious activity
```

`