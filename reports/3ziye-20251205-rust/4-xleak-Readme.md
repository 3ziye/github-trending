# xleak <img src="assets/logo.jpg" align="right" width="120" />

[![CI](https://img.shields.io/github/actions/workflow/status/bgreenwell/xleak/ci.yml?style=for-the-badge)](https://github.com/bgreenwell/xleak/actions/workflows/ci.yml)
[![Crates.io](https://img.shields.io/crates/v/xleak.svg?style=for-the-badge&color=%23107C41)](https://crates.io/crates/xleak)
[![Downloads](https://img.shields.io/crates/d/xleak?style=for-the-badge&color=%23107C41)](https://crates.io/crates/xleak)

[![License: MIT](https://img.shields.io/badge/License-MIT-%232196F3.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Rust](https://img.shields.io/badge/rust-1.70%2B-%23D34516.svg?style=for-the-badge&logo=rust&logoColor=white)](https://www.rust-lang.org/)
[![Easy Install](https://img.shields.io/badge/Easy%20Install-Homebrew%20%7C%20Scoop-%23FBB040?style=for-the-badge)](#installation)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-blue?style=for-the-badge)](https://github.com/bgreenwell/xleak/releases/latest)

> Expose Excel files in your terminal - no Microsoft Excel required!

Inspired by [doxx](https://github.com/bgreenwell/doxx), `xleak` brings Excel spreadsheets to your command line with beautiful rendering, powerful export capabilities, and a feature-rich interactive TUI.

![xleak demo](assets/demo.gif)

## Features

### Core Functionality
- **Beautiful terminal rendering** with formatted tables
- **Interactive TUI mode** - full keyboard navigation with ratatui
- **Smart data type handling** - numbers right-aligned, text left-aligned, booleans centered
- **Multi-sheet support** - seamlessly navigate between sheets (Tab/Shift+Tab)
- **Excel Table support** - list and extract named tables (.xlsx only)
- **Multiple export formats** - CSV, JSON, plain text
- **Blazing fast** - powered by `calamine`, the fastest Excel parser in Rust
- **Multiple file formats** - supports `.xlsx`, `.xls`, `.xlsm`, `.xlsb`, `.ods`

### Interactive TUI Features
- **Full-text search** - search across all cells with `/`, navigate with `n`/`N`
- **Clipboard support** - copy cells (`c`) or entire rows (`C`) to clipboard
- **Formula display** - view Excel formulas in cell detail view (Enter key)
- **Jump to row/column** - press `Ctrl+G` to jump to any cell (e.g., `A100`, `500`, `10,5`)
- **Large file optimization** - lazy loading for files with 1000+ rows
- **Progress indicators** - real-time feedback for long operations
- **Visual cell highlighting** - current row, column, and cell clearly marked

## Installation

### Package Managers

**macOS / Linux (Homebrew):**
```bash
brew install bgreenwell/tap/xleak
```

**Windows (Scoop):**
```powershell
scoop bucket add bgreenwell https://github.com/bgreenwell/scoop-bucket
scoop install xleak
```

**Arch Linux (AUR):**
```bash
# Using yay
yay -S xleak-bin

# Or using paru
paru -S xleak-bin
```

**Cargo (all platforms):**
```bash
cargo install xleak
```

**Nix:**
```bash
# Run directly
nix run github:bgreenwell/xleak -- file.xlsx

# Install with flakes
nix profile install github:bgreenwell/xleak
```

### Quick Install Scripts

**macOS / Linux:**
```bash
curl --proto '=https' --tlsv1.2 -LsSf https://github.com/bgreenwell/xleak/releases/latest/download/xleak-installer.sh | sh
```

**Windows (PowerShell):**
```powershell
irm https://github.com/bgreenwell/xleak/releases/latest/download/xleak-installer.ps1 | iex
```

### Pre-built Binaries

Download platform-specific binaries from the [latest release](https://github.com/bgreenwell/xleak/releases/latest):

- **macOS**: Universal binary (Apple Silicon + Intel)
- **Linux**: x86_64 (glibc and musl)
- **Windows**: x86_64 MSI installer or standalone `.exe`

### Build from Source

```bash
git clone https://github.com/bgreenwell/xleak.git
cd xleak
cargo install --path .
```

**Requirements:** Rust 1.70 or later

## Usage

### Interactive TUI Mode (Recommended)
```bash
# Launch interactive viewer
xleak quarterly-report.xlsx -i

# Start on a specific sheet
xleak report.xlsx --sheet "Q3 Results" -i

# View formulas by default
xleak data.xlsx -i --formulas

# Enable horizontal scrolling for wide files (auto-size columns)
xleak wide-data.xlsx -i -H
```

**TUI Keyboard Shortcuts:**
- `↑ ↓ ← →` - Navigate cells
- `Enter` - View cell details (including formulas)
- `/` - Search across all cells
- `n` / `N` - Jump to next/previous search result
- `Ctrl+G` - Jump to specific row/cell (e.g., `100`, `A50`, `10,5`)
- `c` - Copy current cell to clipboard
- `C` - Copy entire row to clipboard
- `Tab` / `Shift+Tab` - Switch between sheets
- `?` - Show help
- `q` - Quit

### Non-Interactive Mode

#### View a spreadsheet
```bash
xleak quarterly-report.xlsx
```

#### View a specific sheet
```bash
# By name
xleak report.xlsx --sheet "Q3 Results"

# By index (1-based)
xleak report.xlsx --sheet 2
```

#### Limit displayed rows
```bash
# Show only first 20 rows
xleak large-file.xlsx -n 20

# Show all rows
xleak file.xlsx -n 0
```

#### Export data
