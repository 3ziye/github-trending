<p align="center">
  <img src="assets/taws-logo.png" alt="taws" width="400"/>
</p>

# taws - Terminal UI for AWS

**taws** provides a terminal UI to interact with your AWS resources. The aim of this project is to make it easier to navigate, observe, and manage your AWS infrastructure in the wild.

---

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Rust](https://img.shields.io/badge/rust-1.70%2B-orange.svg)](https://www.rust-lang.org/)

---

## Screenshots

<p align="center">
  <img src="assets/screenshot-ec2.png" alt="EC2 Instances View" width="800"/>
</p>

<p align="center">
  <img src="assets/screenshot-lambda.png" alt="Lambda Functions View" width="800"/>
</p>

---

## Features

- **Multi-Profile Support** - Easily switch between AWS profiles
- **Multi-Region Support** - Navigate across different AWS regions
- **94+ Resource Types** - Browse and manage resources across 60+ AWS services
- **Manual Refresh** - Refresh resources with a single keystroke
- **Pagination** - Navigate through large resource lists with `]` / `[` keys
- **Keyboard-Driven** - Vim-like navigation and commands
- **Resource Actions** - Start, stop, terminate EC2 instances directly
- **Detailed Views** - JSON/YAML view of resource details
- **Filtering** - Filter resources by name or attributes
- **Autocomplete** - Smart resource type autocomplete with fuzzy matching

---

## Installation

### Homebrew (macOS/Linux)

```bash
brew install huseyinbabal/tap/taws
```

### Scoop (Windows)

```powershell
scoop bucket add huseyinbabal https://github.com/huseyinbabal/scoop-bucket
scoop install taws
```

### Download Pre-built Binaries

Download the latest release from the [Releases page](https://github.com/huseyinbabal/taws/releases/latest).

| Platform | Architecture | Download |
|----------|--------------|----------|
| **macOS** | Apple Silicon (M1/M2/M3) | `taws-aarch64-apple-darwin.tar.gz` |
| **macOS** | Intel | `taws-x86_64-apple-darwin.tar.gz` |
| **Linux** | x86_64 (musl) | `taws-x86_64-unknown-linux-musl.tar.gz` |
| **Linux** | ARM64 (musl) | `taws-aarch64-unknown-linux-musl.tar.gz` |
| **Windows** | x86_64 | `taws-x86_64-pc-windows-msvc.zip` |

#### Quick Install (macOS/Linux)

```bash
# macOS Apple Silicon
curl -sL https://github.com/huseyinbabal/taws/releases/latest/download/taws-aarch64-apple-darwin.tar.gz | tar xz
sudo mv taws /usr/local/bin/

# macOS Intel
curl -sL https://github.com/huseyinbabal/taws/releases/latest/download/taws-x86_64-apple-darwin.tar.gz | tar xz
sudo mv taws /usr/local/bin/

# Linux x86_64 (musl - works on Alpine, Void, etc.)
curl -sL https://github.com/huseyinbabal/taws/releases/latest/download/taws-x86_64-unknown-linux-musl.tar.gz | tar xz
sudo mv taws /usr/local/bin/

# Linux ARM64 (musl - works on Alpine, Void, etc.)
curl -sL https://github.com/huseyinbabal/taws/releases/latest/download/taws-aarch64-unknown-linux-musl.tar.gz | tar xz
sudo mv taws /usr/local/bin/
```

#### Windows

1. Download `taws-x86_64-pc-windows-msvc.zip` from the [Releases page](https://github.com/huseyinbabal/taws/releases/latest)
2. Extract the zip file
3. Add the extracted folder to your PATH, or move `taws.exe` to a directory in your PATH

### Using Cargo

```bash
cargo install taws
```

### Using Docker

```bash
# Run interactively
docker run --rm -it ghcr.io/huseyinbabal/taws

# Launch with a specific profile (mount AWS credentials)
docker run --rm -it \
  -v ~/.aws:/root/.aws:ro \
  ghcr.io/huseyinbabal/taws --profile production

# Launch in a specific region
docker run --rm -it \
  -v ~/.aws:/root/.aws:ro \
  ghcr.io/huseyinbabal/taws --region us-west-2

# Using environment variables
docker run --rm -it \
  -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
  -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
  -e AWS_REGION=us-east-1 \
  ghcr.io/huseyinbabal/taws

# Build locally
docker build -t taws .
docker run --rm -it -v ~/.aws:/root/.aws:ro taws
```

> **Note:** Use `-it` flags for interactive terminal support (required for TUI). Mount your `~/.aws` directory as read-only to use your existing AWS credentials.

### From Source

taws is built with Rust. Make sure you have Rust 1.70+ installed, along with a C compiler and linker.

#### Build Dependencies

| Platform | Install Command |
|----------|-----------------|
| **Amazon Linux / RHEL / Fedora** | `sudo yum groupinstall "Development Tools" -y` |
| **Ubuntu / Debian** | `sudo apt update && sudo apt install build-essential -y` |
| **macOS** | `xcode-select --install` |
| **Windows** | Install [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) |

```bash
# Clone the repository
git clone https://github.com/huseyinbabal/taws.git
cd taws

# Build and run
cargo build --release
./target/release/taws
```

---

## Prerequisites

- **AWS Credentials** - See [Authentication](#authentication) section below
- **IAM Permissions** - Your AWS user/role needs appropriate read permissions for the services you want to browse. At m