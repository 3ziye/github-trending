# WorkTUImer
![work-tuimer](https://github.com/user-attachments/assets/207f9b66-0b08-4e97-a471-a9f413a7369c)

Live demo: https://x.com/KsenKamil/status/1985423210859368716

Simple, keyboard-driven TUI for time-tracking that allows you to quickly add time blocks and automatically group time if same task was done in different sessions
Built with Rust and ratatui for efficient time management.

## Features

- **Fully keyboard-driven**: No mouse required - everything accessible via keybinds
- **Active timer tracking**: Start/stop/pause timers that automatically update work records with actual time spent
- **Time as PIN-Inputs**: Easly type time with 4 clicks, since all time inputs are PIN-input alike
- **Log tasks and breaks, get totals automatically**: Add work entries with start/end times - durations are calculated and summed
- **Task picker with history**: Quickly select from previously used task names or create new ones
- **Calendar navigation**: Jump between days, weeks, and months
- **Arrow keys or Vim motions**: Navigate with arrow keys + Enter, or use h/j/k/l + i for Vim-style workflow
- **Inline editing with undo/redo**: Fix mistakes in place, up to 50 levels of history
- **Auto-saves locally per day**: Data stored as JSON files, for each day, on your machine (`~/.local/share/work-tuimer/`)
- **Optional ticket integration**: Detect and link to JIRA, Linear, GitHub issues from task names - open ticket URLs directly in your browser from the app

## Installation

### Package Managers

#### Cargo (Rust)
LINK: https://crates.io/crates/work-tuimer
```sh
cargo install work-tuimer
```

#### (!!! NOT READY YET !!!) Homebrew (macOS/Linux)

```sh
brew install work-tuimer
```

#### Arch Linux (AUR)
LINK: https://aur.archlinux.org/packages/work-tuimer
```sh
# Using yay
yay -S work-tuimer

# Or manually
git clone https://aur.archlinux.org/work-tuimer.git
cd work-tuimer
makepkg -si
```

#### FreeBSD

```sh
pkg install work-tuimer
```

### Pre-built Binaries

Download the latest pre-built binary for your platform from [GitHub Releases](https://github.com/Kamyil/work-tuimer/releases):

- **Linux (x86_64)**: `work-tuimer-linux-x86_64`
- **macOS (Intel)**: `work-tuimer-macos-x86_64`
- **macOS (Apple Silicon)**: `work-tuimer-macos-aarch64`
- **Windows**: `work-tuimer-windows-x86_64.exe`

After downloading, make the binary executable and run it:

```bash
# Linux / macOS
chmod +x work-tuimer-linux-x86_64
./work-tuimer-linux-x86_64

# Windows
work-tuimer-windows-x86_64.exe
```

### Build from Source

If you prefer to build from source or don't see a binary for your platform:

```bash
cargo build --release
./target/release/work-tuimer
```

## Usage

### Browse Mode

| Key | Action |
|-----|--------|
| `↑/k` | Move selection up |
| `↓/j` | Move selection down |
| `←/h` | Move field left (Name → Start → End) |
| `→/l` | Move field right (Name → Start → End) |
| `[` | Navigate to previous day (auto-saves) |
| `]` | Navigate to next day (auto-saves) |
| `C` | Open calendar view for date navigation |
| `Enter/i` | Enter edit mode on selected field |
| `c` | Change task name (opens picker to select/filter/create) |
| `n` | Add new work record |
| `b` | Add break (uses selected record's end time as start) |
| `d` | Delete selected record |
| `v` | Enter visual mode (multi-select) |
| `S` | Start/Stop timer for selected record |
| `P` | Pause/Resume active timer |
| `t` | Set current time on selected field |
| `T` | Open ticket in browser (only visible if config exists) |
| `L` | Open worklog URL in browser (only visible if config exists) |
| `u` | Undo last change |
| `r` | Redo undone change |
| `s` | Save to file |
| `q` | Quit (auto-saves) |

### Edit Mode

| Key | Action |
|-----|--------|
| `Tab` | Next field (Name → Start → End → Description → Name) |
| `Enter` | Save changes and exit edit mode |
| `Esc` | Cancel and exit edit mode |
| `Backspace` | Delete character |
| Any char | Insert character |

### Task Picker (accessed via `c` in Browse mode)

Press `c` on the Name field to open the task picker:
- Shows all unique task names from the current day
- Type to filter the list
- Press Enter to select a task or create a new one

| Key | Action |
|-----|--------|
| Any char | Type to filter tasks or create new name (including h/j/k/l) |
| `↑` | Move selection up in filtered list |
| `↓` | Move selection down in filtered list |
| `Enter` | Select highlighted task or create typed name |
| `Backspace` | Delete character from filter |
| `Esc` | Cancel and return to browse mode |

### Visual Mode

| Key | Action |
|-----|--------|
| `↑/k` | Extend selection up |
| `↓/j` | Extend selection down |
| `d` | Delete selected records |
| `Esc` | Exit visual mode |

### Calendar View

| Key | Action |
|-----|--------|
| `↑/k` | Move selection up (1 week) |
| `↓/j` | Move selection down (1 week) |
| `←/h` | Move selection left (1 day) |
| `→/l` | Move selection right (1 day) |
| `[/</,` | Previous month |
| `]/>/.` | Next month |
| `Enter` |