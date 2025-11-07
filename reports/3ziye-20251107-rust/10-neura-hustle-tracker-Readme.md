[![Rust](https://img.shields.io/badge/rust-%23000000.svg?style=for-the-badge&logo=rust&logoColor=white)](https://www.rust-lang.org)
[![Ratatui](https://img.shields.io/badge/ratatui-%23000000.svg?style=for-the-badge&logo=rust&logoColor=white)](https://ratatui.rs)
[![Docker](https://img.shields.io/badge/docker-%23000000.svg?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
[![Make](https://img.shields.io/badge/Make-%23000000.svg?style=for-the-badge&logo=gnu&logoColor=white)](https://www.gnu.org/software/make/)
[![PostgreSQL](https://img.shields.io/badge/postgresql-%23000000.svg?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org)

[![Neura Hustle Tracker](https://img.shields.io/badge/Neura%20Hustle%20Tracker-7f56da)](https://meetneura.ai) [![Powered by Neura AI](https://img.shields.io/badge/Powered%20by-Neura%20AI-7f56da)](https://meetneura.ai)

# Neura Hustle Tracker BETA

**Track what apps you use and how long you spend on them.**

This app runs in your terminal and shows you exactly where your time goes during work sessions. Built with Ratatui.

![Demo](src/screenshots/hustler-tracker-demo-new.gif)

## What Does This Do?

- **Tracks your app usage** - Automatically monitors which programs you're using
- **Shows pretty charts** - See your time broken down by app and category
- **Saves your data** - Everything stored locally in your own PostgreSQL database
- **Works everywhere** - Linux, macOS, and Windows

## Quick Start (Easiest Way)

### Linux

Copy and paste this into your terminal:

```bash
sudo apt update && sudo apt install -y make docker.io curl git openssl && curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y && source ~/.cargo/env && git clone https://github.com/adolfousier/neura-hustle-tracker.git && cd neura-hustle-tracker && make run
```

That's it! The app will start tracking automatically.

### macOS

1. Install [Docker Desktop](https://docs.docker.com/desktop/install/mac-install/) first
2. Then paste this into Terminal:

```bash
brew install make git rustup-init && rustup-init -y && source ~/.cargo/env && git clone https://github.com/adolfousier/neura-hustle-tracker.git && cd neura-hustle-tracker && make daemon-start
```

3. View your stats anytime: `make view`

### Windows

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. Open PowerShell as Administrator
3. Run this:

```powershell
powershell -Command "iwr -useb https://raw.githubusercontent.com/adolfousier/neura-hustle-tracker/main/src/scripts/windows_build/windows-install.ps1 | iex"
```

4. View your stats anytime: `hustle-view`

## Already Have Rust and Docker?

If you already have the prerequisites installed:

```bash
git clone https://github.com/adolfousier/neura-hustle-tracker
cd neura-hustle-tracker
make run
```

Done! The app handles everything else automatically.

## How to Use It

Once the app is running:

- **Tab** - Switch between Daily, Weekly, and Monthly views
- **h** - See your complete session history
- **r** - Rename apps to organize them better
- **Shift+C** - See all available commands
- **q** - Quit

The app tracks automatically. Just switch between your programs normally and it records everything.

## Two Ways to Run (Important!)

### Linux Users → Use "Unified Mode"

Run `make run` and you're done. Everything works in one window.

**Available commands for Linux:**

- `make run` - Start DB + build + run app (all in one!)
- `make dev` - Start DB + run in dev mode (faster builds)
- `make db-up` - Start PostgreSQL in Docker
- `make db-down` - Stop PostgreSQL
- `make build` - Build TUI binary only
- `make build-daemon` - Build daemon binary only
- `make clean` - Clean all build artifacts and stop DB
- `make help` - Show all available commands

### macOS/Windows Users → Use "Daemon Mode"

You need two steps because of how these systems work:

1. **Start tracking in background**: `make daemon-start`
2. **Open the dashboard**: `make view`

Why? On macOS/Windows, if the tracking runs in the dashboard window, it can't see when you switch to other apps. Running it in the background fixes this.

**Commands for daemon mode:**

- `make daemon-start` - Start tracking
- `make view` - Open dashboard
- `make daemon-stop` - Stop tracking
- `make daemon-status` - Check if running

## What You Need

- **Computer**: Windows 10+, macOS 10.15+, or Linux with a desktop
- **Space**: About 500MB for Docker and dependencies
- **Permissions**:
  - **macOS**: Terminal application needs the following permissions (daemon binary itself does NOT need permissions):
    - Accessibility
    - Screen & System Audio Settings
    - Input Monitoring
  - **Windows**: Works out of the box
  - **Linux**: Needs a desktop environment (GNOME, KDE, etc.)

  **Note**: On macOS/Windows, the daemon runs in the background without needing permissions. The **Terminal application** itself needs the permissions listed above to monitor your system properly.

## Special Notes
