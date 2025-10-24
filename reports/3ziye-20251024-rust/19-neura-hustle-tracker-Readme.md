[![Rust](https://img.shields.io/badge/rust-%23000000.svg?style=for-the-badge&logo=rust&logoColor=white)](https://www.rust-lang.org)
[![Ratatui](https://img.shields.io/badge/ratatui-%23000000.svg?style=for-the-badge&logo=rust&logoColor=white)](https://ratatui.rs)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
[![PostgreSQL](https://img.shields.io/badge/postgresql-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org)

[![Neura Hustle Tracker](https://img.shields.io/badge/Neura%20Hustle%20Tracker-7f56da)](https://meetneura.ai) [![Powered by Neura AI](https://img.shields.io/badge/Powered%20by-Neura%20AI-7f56da)](https://meetneura.ai)

# Neura Hustle Tracker BETA

A cross-platform time-tracking tool for monitoring your productivity through app usage during work sessions. Built with Rust, Ratatui for the UI and Postgres database. Supports Windows, macOS (macOS and Windows not tested yet, please if you try provide feedback), and Linux (X11 and Wayland).

![Demo](src/screenshots/demo.png)
![Activities Breakdown](src/screenshots/demo-activities-breakdown.png)
![Category Update View](src/screenshots/demo-category-update-view.png)
![Commands View](src/screenshots/demo-commands-view.png)
![History View](src/screenshots/demo-history-view.png)
![Renaming App View](src/screenshots/demo-renaming-app-view.png)
![Renaming Selector View](src/screenshots/demo-rename-selector-view.png)

## Features

- **Interactive Dashboard**: Comprehensive data visualization with bar charts, timelines, and statistics
- **App Categorization**: Automatic categorization of apps (Development, Browsing, Communication, Media, Files, Email, Office, Other) with color coding
- **Fully Responsive Design**: Adaptive layout that adjusts to terminal size for optimal viewing on any device
- **Cross-Platform Support**: Works on Linux (X11), macOS, and Windows
- **Commands Menu**: Popup menu (Shift+C) showing all available shortcuts and commands
- **Multiple Views**: Daily, Weekly, Monthly, and History views with Tab navigation
- **App Renaming**: Interactive renaming of tracked applications
- **Session Management**: Manual start/end sessions with automatic saving
- **Real-time Tracking**: Live monitoring with 5-second dashboard updates and live session duration
- **Enhanced App Detection**: Tracks editors (vim, emacs, vscode), file managers, terminals, chat apps, media players, email clients, and office suites
- **Live Session Display**: Current active session shows real-time duration with [LIVE] indicator
- **Timestamped Logs**: All log entries include timestamps for better debugging
- **PostgreSQL Storage**: Persistent data storage with automatic migrations

## Which Mode Should I Use?

Neura Hustle Tracker supports two operating modes depending on your platform:

### Linux (X11/Wayland) - Unified Mode ✅
- **Recommended**: Use unified mode (default)
- **How it works**: TUI and tracking run in one process
- **Command**: `make run`
- **Why**: Linux window detection works perfectly even when TUI is running
- **Note**: Wayland users need [Window Calls extension](https://extensions.gnome.org/extension/4724/window-calls/)

### macOS/Windows - Daemon Mode 🔄
- **Recommended**: Use daemon mode for accurate tracking
- **How it works**:
  - Background daemon tracks all apps silently
  - TUI opens separately to view stats (doesn't interfere with tracking)
- **Commands**:
  - `make daemon-start` - Start background tracking
  - `make view` - Open TUI to view stats
  - `make daemon-stop` - Stop background tracking
- **Why**: On macOS/Windows, when the TUI runs, it becomes the focused window and can't detect other apps you switch to

### Feature Comparison

##### Basics

|                 | User owns data     | GUI                | Sync                       | Open Source        |
| --------------- |:------------------:|:------------------:|:--------------------------:|:------------------:|
| HustleTracker   | :white_check_mark: | :white_check_mark: | Centralized                | :white_check_mark: |
| [ActivityWatch] | :white_check_mark: | :white_check_mark: | WIP, decentralized         | :white_check_mark: |
| [RescueTime]    | :x:                | :white_check_mark: | Centralized                | :x:                |
| [Selfspy]       | :white_check_mark: | :x:                | :x:                        | :white_check_mark: |
| [ulogme]        | :white_check_mark: | :white_check_mark: | :x:                        | :white_check_mark: |
| [WakaTime]      | :x:                | :white_check_mark: | Centralized                | Clients            |

[ActivityWatch]: https://activitywatch.net/
[RescueTime]: https://www.rescuetime.com/
[Selfspy]: https://github.com/selfspy/selfspy
[ulogme]: https://github.com/karpathy/ulogme
[WakaTime]: https://wakatime.com/

##### Platforms

|               | Windows            | macOS              | Linux        