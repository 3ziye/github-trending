# envx

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![CI](https://github.com/mikeleppane/envx/workflows/CI/badge.svg)
<img alt="Rust" src="https://img.shields.io/badge/Rust-1.85-orange">
<img alt="License" src="https://img.shields.io/badge/License-MIT-blue">

A powerful and secure environment variable manager for developers, featuring an intuitive Terminal User Interface (TUI)
and comprehensive command-line interface.

## 🎥 Introduction Video

[![Watch the video](https://img.youtube.com/vi/UzrKuQQURFw/maxresdefault.jpg)](https://youtu.be/UzrKuQQURFw)

<p align="center">
  <i>Click the image above to watch a quick introduction to Envx</i>
</p>

[![Watch the video](https://img.youtube.com/vi/DbRPbN9KECw/maxresdefault.jpg)](https://youtu.be/DbRPbN9KECw)
<p align="center">
  <i>Click the image above to watch how interactive wizard works</i>
</p>


## 📸 Screenshots

<p align="center">
  <img src="images/main.png" alt="Envx's Main Page" />
  <span>Envx's Main Page</span>
</p>

<p align="center">
  <img src="images/search.png" alt="Envx's Search Dialog" />
  <span>Envx's Search Dialog</span>
</p>

<p align="center">
  <img src="images/view.png" alt="Envx's View Dialog" />
  <span>Envx's View Dialog</span>
</p>

<p align="center">
  <img src="images/query.png" alt="Envx's CLI Query" />
  <span>Envx's CLI Query Command</span>
</p>

## 🌟 Features

- **🖥️ Interactive TUI**: Beautiful terminal interface for easy environment variable management
- **🔍 Smart Search**: Fast filtering and searching across all environment variables
- **📊 Source Tracking**: Distinguish between System, User, Process, Shell, and Application variables
- **📝 Multi-line Support**: Edit complex environment variables with proper multi-line support
- **🔄 Import/Export**: Support for multiple formats (JSON, YAML, TOML, ENV)
- **📸 Snapshots & Profiles Feature Implementation**: Save and restore variable states
- **📁 Project Configuration**: Define required variables, defaults, and scripts for consistent team environments
- **👀 Watch Mode & Monitor**: Monitor file changes and sync automatically, track environment modifications in real-time
- **⚡ Performance**: Built with Rust for blazing-fast performance
- **🎨 Cross-platform**: Works on Windows, macOS, and Linux

## 📦 Installation

### From Source

```bash
git clone https://github.com/yourusername/envx.git
cd envx
cargo install --path crates/envx
```

### Using Cargo

```bash
cargo install envex
```

### Pre-built Binaries

Download the latest release for your platform from the [releases page](https://github.com/yourusername/envx/releases).

## 🚀 Quick Start

### Launch the TUI

```bash
envx tui
# or
envx ui
```

### List all environment variables

```bash
envx list
```

### Set a variable

```bash
envx set MY_VAR "my value"
```

### Get a variable

```bash
envx get MY_VAR
```

## 📖 Command Line Usage

### Overview

```bash
System Environment Variable Manager

Usage: envx.exe <COMMAND>

Commands:
  list     List environment variables
  get      Get a specific environment variable
  set      Set an environment variable
  delete   Delete environment variable(s)
  analyze  Analyze environment variables
  tui      Launch the TUI [aliases: ui]
  path     Manage PATH variable
  export   Export environment variables to a file
  import   Import environment variables from a file
  help     Print this message or the help of the given subcommand(s)

Options:
  -h, --help     Print help
  -V, --version  Print version
```

### Core Commands

#### `init` - Initialize a new project with the setup wizard

```bash
Initialize a new project with interactive wizard

Usage: envx.exe init [OPTIONS]

Options:
  -t, --template <TEMPLATE>  Use a specific template
  -w, --wizard               Run interactive wizard
      --list-templates       List available templates
  -h, --help                 Print help
```

The `init` command launches an interactive setup wizard that helps you configure your project's environment variables.
The wizard will:

- Detect your project type (Web App, Python, Rust/Go, Docker, Microservices, or Custom)
- Guide you through setting up environment variables with values
- Create profiles for different environments (development, testing, production, etc.)
- Generate `.env` files for each profile
- Set up team collaboration features
- Configure validation rules
- Import existing `.env` files if found

##### Example Usage

```bash
# Run the interactive setup wizard
envx init

# Or
envx init --wizard

```

##### What the Wizard Creates

After running the wizard, you'll have:

1. **Project Configuration** (`.envx/config.yaml`):
   - Required environment variables with descriptions
   - Default values for common variables
   - Validation rules and patterns
   - Auto-load configuration for .env files

2. **Environment Profiles**:
   - Separate profiles for development, testing, production, etc.
   - Profile-specific variable values
   - Easy switc