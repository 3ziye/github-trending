<p align="center">
  <img src="ttl.png" alt="ttl logo" width="200">
</p>

# ttl

Network diagnostic tool that goes beyond traceroute: MTU discovery, NAT detection, route flap alerts, IX identification, and more.

![ttl screenshot](ttlss.png)

[![Crates.io](https://img.shields.io/crates/v/ttl.svg)](https://crates.io/crates/ttl)
[![CI](https://github.com/lance0/ttl/actions/workflows/ci.yml/badge.svg)](https://github.com/lance0/ttl/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-MIT%2FApache--2.0-blue.svg)](LICENSE-MIT)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-tip-ff5e5b?logo=ko-fi)](https://ko-fi.com/lance0)

## Quick Start

```bash
# Basic usage
ttl 8.8.8.8                          # Linux (after setcap)
sudo ttl 8.8.8.8                     # macOS (always needs sudo)

# Common options
ttl -p udp google.com                # UDP probes
ttl --flows 8 cloudflare.com         # ECMP path discovery
ttl --pmtud 1.1.1.1                  # Path MTU discovery
ttl 8.8.8.8 1.1.1.1 9.9.9.9          # Multiple targets
ttl --resolve-all google.com         # Trace all resolved IPs
```

See [Installation](#installation) below for setup instructions.

## Features

- **Fast continuous path monitoring** with detailed hop statistics
- **Multiple simultaneous targets** - trace to several destinations at once
- **Paris/Dublin traceroute** - multi-flow probing for ECMP path enumeration
- **Path MTU discovery** - binary search for maximum unfragmented size
- **NAT detection** - identify when NAT devices rewrite source ports
- **Route flap detection** - alert on path changes indicating routing instability
- **Rich enrichment** - ASN, GeoIP, reverse DNS, IX detection (PeeringDB)
- **MPLS label detection** from ICMP extensions
- **ICMP, UDP, TCP probing** with auto-detection
- **Great TUI** with themes, sparklines, and session export
- **Scriptable** - JSON, CSV, and text report output

See [docs/FEATURES.md](docs/FEATURES.md) for detailed documentation, including optional setup for [GeoIP](docs/FEATURES.md#geoip-location) and [IX detection](docs/FEATURES.md#ix-detection).

## Installation

### From crates.io (Recommended)

Requires [Rust](https://www.rust-lang.org/tools/install):

```bash
# Install Rust (if not already installed)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source ~/.cargo/env

# Install ttl
cargo install ttl
```

### Homebrew (macOS/Linux)

```bash
brew install lance0/tap/ttl
```

### Pre-built Binaries

Download from [GitHub Releases](https://github.com/lance0/ttl/releases):

| Platform | Target |
|----------|--------|
| Linux x86_64 | `ttl-x86_64-unknown-linux-musl.tar.gz` |
| Linux ARM64 | `ttl-aarch64-unknown-linux-gnu.tar.gz` |
| macOS Apple Silicon | `ttl-aarch64-apple-darwin.tar.gz` |
| macOS Intel | `ttl-x86_64-apple-darwin.tar.gz` |

```bash
# Download, verify, and install (Linux x86_64 example)
curl -LO https://github.com/lance0/ttl/releases/latest/download/ttl-x86_64-unknown-linux-musl.tar.gz
curl -LO https://github.com/lance0/ttl/releases/latest/download/SHA256SUMS
sha256sum -c SHA256SUMS --ignore-missing  # macOS: shasum -a 256 -c
tar xzf ttl-*.tar.gz && sudo mv ttl /usr/local/bin/
```

### From Source

```bash
git clone https://github.com/lance0/ttl
cd ttl && cargo build --release
sudo cp target/release/ttl /usr/local/bin/
```

### Quick Install Script

> **Note**: Piping scripts from the internet to sh is convenient but bypasses your ability to review the code first. Consider using one of the methods above, or [review the script](https://github.com/lance0/ttl/blob/master/install.sh) before running.

```bash
curl -fsSL https://raw.githubusercontent.com/lance0/ttl/master/install.sh | sh
```

### Permissions (Linux)

Raw sockets require elevated privileges. The easiest approach is to add the capability once:

```bash
# Add capability (works for any install location)
sudo setcap cap_net_raw+ep $(which ttl)

# Then run without sudo:
ttl 8.8.8.8
```

### Shell Completions

```bash
# Bash
ttl --completions bash > ~/.local/share/bash-completion/completions/ttl

# Zsh (add ~/.zfunc to fpath in .zshrc first)
ttl --completions zsh > ~/.zfunc/_ttl

# Fish
ttl --completions fish > ~/.config/fish/completions/ttl.fish

# PowerShell (add to $PROFILE)
ttl --completions powershell >> $PROFILE
```

## Usage Examples

### Interactive TUI

```bash
ttl google.com
ttl 8.8.8.8 1.1.1.1      # Multiple targets (Tab to switch)
```

### Report and Export

```bash
ttl 1.1.1.1 -c 100 --report    # Text report
ttl 1.1.1.1 -c 100 --json      # JSON export
ttl 1.1.1.1 -c 100 --csv       # CSV export
ttl --replay results.json      # Replay saved session
```

### Advanced Options

```bash
ttl -p tcp --port 443 host     # TCP probes to HTTPS
ttl --flows 4 host             # ECMP path enumeration
ttl --interface eth0 host      # Bind to interface
ttl --size 1400 host           # Large packets for MTU testing
ttl --dscp 46 host             # QoS marking (EF)
ttl --wide host                #