# fairshare

**Fair resource allocation for shared Linux systems**

A lightweight resource manager that prevents any single user from monopolizing CPU and memory on multi-user Linux servers. fairshare automatically enforces per-user limits while allowing users to request additional resources dynamically when they need them.

### The Problem fairshare Solves

On shared Linux systems, one user running a heavy workload can consume all available CPU and memory, leaving nothing for other users. This creates a terrible experience and reduces productivity.

### The Solution

fairshare allocates resources fairly across all users:
- **Default**: Each user gets 1 CPU core and 2GB RAM by default
- **Reserved**: System reserves resources for OS and background processes (2 CPUs, 4GB RAM by default)
- **On-demand**: Users can request more resources when needed (up to 1000 CPU cores and 10000 GB RAM)
- **Automatic**: The system grants requests only if resources are truly available
- **Fair**: No user can monopolize the entire system

## Installation

### Quick Install (Recommended)

The easiest way to install fairshare is using the installation script:

```bash
# Download and run the installer
curl -sSL https://raw.github.com/WilliamJudge94/fairshare/main/install.sh | bash
```

Or if you prefer to inspect the script first:

```bash
# Download the installer
wget https://raw.github.com/WilliamJudge94/fairshare/main/install.sh

# Review it
cat install.sh

# Run it
bash install.sh
```

The installer will:
- Detect if PolicyKit is installed (automatically installs it if missing)
- Download the latest release binary for your architecture
- Install the binary and wrapper script
- Set up PolicyKit policies
- Configure default resource limits (1 CPU core, 2GB RAM per user)
- Set system reserves (2 CPUs, 4GB RAM by default)

![Admin Setup](static/root-admin-setup.png)

### Build from Source

If you prefer to build from source or are developing fairshare:

```bash
# 1. Build the release binary
cargo build --release

# 2. Run the installer (it will detect the local build and install PolicyKit if needed)
bash install.sh
```

Alternatively, use the Makefile for manual installation:

```bash
# Build and install binary and wrapper
cargo build --release
sudo make release

# Ensure PolicyKit is installed (required for fairshare to work)
# Debian/Ubuntu
sudo apt install policykit-1

# Fedora/RHEL
sudo dnf install polkit

# Arch Linux
sudo pacman -S polkit

# Setup admin defaults and PolicyKit policies (REQUIRED)
sudo fairshare admin setup --cpu 1 --mem 2
```

### What Gets Installed

- **`/usr/local/bin/fairshare`** - Wrapper script (user-facing command)
- **`/usr/local/libexec/fairshare-bin`** - Real binary (internal use only)
- **PolicyKit policies** - Allow passwordless execution for active users
- **Systemd configuration** - Default resource limits for all user slices

The wrapper script automatically detects whether you're running an admin command (requires `sudo`) or a regular user command (automatically uses `pkexec`).

### Requirements
- **Linux** with systemd (including user session support)
- **PolicyKit (polkit)** for privilege escalation (automatically installed by the installer if missing)
- **Rust 1.70+** (only needed for building from source)

### Uninstall

To remove fairshare from your system:

```bash
# Using the uninstall script
curl -sSL https://raw.github.com/WilliamJudge94/fairshare/main/uninstall.sh | bash

# Or if you have the repository
bash uninstall.sh

# Or manually
sudo fairshare admin uninstall --force
```

## Usage Guide

### User Commands (No sudo required)

Regular users can manage their own resource allocations. The wrapper script automatically handles privilege escalation via PolicyKit, so you don't need to type `pkexec` or `sudo`.

#### 1. Check System Status
See how much CPU and memory is available and what each user is currently using.
```bash
fairshare status
```

![User Status](static/user-status.png)

#### 2. Check Your Current Allocation
View how much CPU and memory your user session has access to.
```bash
fairshare info
```

#### 3. Request Resources
Ask for CPU and memory resources. The system uses **smart delta-based checking** - it only needs enough free resources to cover the increase from your current allocation.

```bash
fairshare request --cpu 4 --mem 8
```

![User Request](static/user-request.png)

**Smart Allocation Example:**
- You currently have: 9GB RAM allocated
- System has: 2GB free
- You request: 10GB RAM
- Result: **SUCCESS** (net increase is only 1GB, which fits in the 2GB available)

**Constraints:**
- CPU: 1–1000 cores
- Memory: 1–10000 GB

#### 4. Release Resources
Return your resources to the system and revert to the default allocation (1 CPU core, 2GB RAM).
```bash
fairshare release
```

![User Release](static/user-release.png)

### Administrator Commands (Requires sudo)

> **Note:** Admin commands must be run with `sudo`

#### Set Default Limits and System Reserves
Configure