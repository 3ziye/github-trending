# Tock

[Features](#features) • [Quick Start](#quick-start) • [Commands](#commands) • [File Format](#file-format) • [Architecture](#architecture) • [Inspiration](#inspiration) • [License](#license)

## Features

<img src="assets/demo.png" width="820px" />

**Tock** is a powerful time tracking tool for the command line. It saves activity logs as plaintext files and provides an interactive terminal UI for viewing your time.

Built with **Go** using Clean Architecture principles.

- 📝 **Simple plaintext format** - Activities stored in human-readable files
- 🎨 **Interactive TUI** - Beautiful terminal calendar view using Bubble Tea
- 🏗️ **Clean Architecture** - Ports & Adapters pattern for maintainability
- ⚡ **Fast & Lightweight** - Single binary, no dependencies
- 🔄 **Compatible** - Reads/writes Bartib file format and TimeWarrior data files

<hr clear="right"/>

## Quick Start

### Installation

**Homebrew (macOS)**

```bash
brew tap kriuchkov/tap
brew install tock
```

**Go Install**

```bash
go install github.com/kriuchkov/tock/cmd/tock@latest
```

**Build from source**

```bash
go build -o tock ./cmd/tock
```

**Download Binary**

Download the latest release from the [Releases](https://github.com/kriuchkov/tock/releases) page.

### Basic Usage

Start tracking time:

```bash
tock start -d "Implementing features" -p "My Project"
```

Stop the current activity:

```bash
tock stop
```

View activities in interactive calendar:

```bash
tock list
```

### Configuration

#### Storage Backends

Tock supports multiple storage backends.

**1. Flat File (Default)**

Stores activities in a simple plaintext file.

```bash
export TOCK_FILE="$HOME/.tock.txt"
```

**2. TimeWarrior**

Integrates with [TimeWarrior](https://timewarrior.net/) data files.

```bash
# Enable TimeWarrior backend
export TOCK_BACKEND="timewarrior"

# Optional: Specify custom data directory (default: ~/.timewarrior/data)
export TIMEWARRIORDB="/path/to/timewarrior/data"
```

Or use flags:

```bash
tock --backend timewarrior list
```

#### Theming

Tock supports customizable color themes for the calendar view.

**Environment Variables**

Set `TOCK_THEME` to one of:

- `dark`: Standard 256-color dark theme
- `light`: Standard 256-color light theme
- `ansi_dark`: 16-color dark theme
- `ansi_light`: 16-color light theme
- `custom`: Use custom colors defined by environment variables

**Auto-detection**

If `TOCK_THEME` is not set, Tock automatically selects the best theme:

1. Detects terminal capabilities (TrueColor/256 vs ANSI).
2. Detects background color (Light vs Dark).
3. Selects the appropriate theme (e.g. `light` for light background, `ansi_dark` for dark ANSI terminal).

**Custom Colors**

When `TOCK_THEME=custom`, you can override specific colors using these variables (accepts ANSI color codes or hex values):

```bash
export TOCK_THEME="custom"
export TOCK_COLOR_PRIMARY="63"   # Blue
export TOCK_COLOR_SECONDARY="196" # Red
export TOCK_COLOR_TEXT="255"     # White
export TOCK_COLOR_SUBTEXT="248"  # Light Grey
export TOCK_COLOR_FAINT="240"    # Dark Grey
export TOCK_COLOR_HIGHLIGHT="214" # Orange/Gold
```

**Example: Cyberpunk / Fuchsia Theme**

<img src="assets/demo_2.png" width="820px" />

```bash
export TOCK_THEME="custom"
export TOCK_COLOR_PRIMARY="#FF00FF"   # Fuchsia
export TOCK_COLOR_SECONDARY="#00FFFF" # Cyan
export TOCK_COLOR_TEXT="#FFFFFF"      # White
export TOCK_COLOR_SUBTEXT="#B0B0B0"   # Light Grey
export TOCK_COLOR_FAINT="#404040"     # Dark Grey
export TOCK_COLOR_HIGHLIGHT="#FFFF00" # Yellow
```

#### Shell Completion

To enable shell completion (e.g. for Oh My Zsh):

1. Create a directory for the plugin:

```bash
mkdir -p ~/.oh-my-zsh/custom/plugins/tock
```

1. Generate the completion script:

```bash
tock completion zsh > ~/.oh-my-zsh/custom/plugins/tock/_tock
```

1. Add `tock` to your plugins list in `~/.zshrc`:

```bash
plugins=(... tock)
```

1. Restart your shell:

```bash
exec zsh
```

## Commands

### Start tracking

Start a new activity. Description and project are required.

```bash
tock start -p "Project Name" -d "Task description"
tock start -p "Project" -d "Task" -t 14:30  # Start at specific time
```

**Flags:**

- `-d, --description`: Activity description (required)
- `-p, --project`: Project name (required)
- `-t, --time`: Start time in HH:MM format (optional, defaults to now)

### Stop tracking

Stop the currently running activity.

```bash
tock stop
tock stop -t 17:00  # Stop at specific time
```

**Flags:**

- `-t, --time`: End time in HH:MM format (optional, defaults to now)

### Add past activity

Add a completed activity manually. Useful for logging time retroactively.

```bash
tock add -p "Project" -d "Task" -s 10:00 -e 11:00
tock add -p "Project" -d "Task" -s 14:00 --duration 1h30m
```

**Flags:**

- `-d, --description`: Activity description (required)
- `-p, --project`: Project name (required)
- `-s, --start`: Start time (HH:MM or YYYY-MM-DD HH:MM)
- `-e, --end`: End time (HH:MM or YYYY-MM-DD HH:MM)
- `--d