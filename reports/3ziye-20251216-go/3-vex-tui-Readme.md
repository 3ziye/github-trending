# 📊 Vex - Terminal Spreadsheet Editor

A beautiful, fast, and feature-rich terminal-based Excel and CSV editor with vim-style keybindings and formula support.

[![Go Version](https://img.shields.io/badge/Go-1.21+-00ADD8?style=flat&logo=go)](https://golang.org/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-2.0.1-brightgreen.svg)](https://github.com/CodeOne45/vex-tui/releases)

![Vex Demo](assets/vex-demo.gif)

## ✨ Features

### 🎨 Ten Beautiful Themes

**Dark Themes:**
- **Catppuccin Mocha** - Soft pastels, perfect for all-day use
- **Nord** - Cool Arctic blues, minimal and focused
- **Rosé Pine** - Elegant rose tones, sophisticated
- **Tokyo Night** - Vibrant cyberpunk aesthetic
- **Gruvbox** - Warm retro colors, comfortable
- **Dracula** - Classic high contrast theme

**Light Themes:**
- **Catppuccin Latte** - Gentle pastel light theme
- **Solarized Light** - Balanced contrast
- **GitHub Light** - Clean and minimal
- **One Light** - Soft Atom-inspired colors

### ✏️ Full Editing Capabilities

- **Edit cells** with formulas and values
- **Insert/delete** rows and columns
- **Copy/paste** single cells or ranges
- **Fill down/right** for quick data entry
- **Apply formulas** to entire ranges with automatic reference adjustment
- **Auto-save** with modification tracking
- **Undo-friendly** workflow with clear status messages

### 📐 Powerful Formula Engine

**Arithmetic:** `=A1+B1`, `=C1*2`, `=D1/E1-F1`

**15+ Built-in Functions:**
- `SUM(A1:A10)` - Sum range
- `AVERAGE(B1:B20)` / `AVG(...)` - Average values
- `COUNT(C1:C50)` - Count numbers
- `MAX(D1:D100)` / `MIN(...)` - Find max/min
- `IF(A1>100, "High", "Low")` - Conditional logic
- `CONCATENATE(A1, " ", B1)` / `CONCAT(...)` - Join text
- `UPPER(A1)` / `LOWER(A1)` - Change case
- `LEN(A1)` - Text length
- `ROUND(A1, 2)` - Round numbers
- `ABS(A1)` - Absolute value
- `SQRT(A1)` - Square root
- `POWER(2, 8)` / `POW(...)` - Exponentiation

**Auto-recalculation** when cells change

### 🔍 Powerful Navigation

- **Vim-style keybindings** (hjkl) and arrow keys
- **Jump to cell** (Ctrl+G) - supports `A100`, `500`, or `10,5` formats
- **Search** (/) across cells and formulas
- **Navigate results** (n/N)
- **Page Up/Down**, Home/End
- **Multi-sheet** support with Tab navigation

### 📋 Data Operations

- **Copy** cell (c) or entire row (C)
- **Paste** (p) with multi-cell support
- **Export** to CSV or JSON
- **Save** (Ctrl+S) with format preservation
- **Save As** (Ctrl+Shift+S) to new file
- **Toggle formula display** (f)
- **View cell details** (Enter)

### 📊 Live Data Visualization

- **Bar charts** - Compare values visually
- **Line charts** - Show trends over time
- **Sparklines** - Compact inline charts
- **Pie charts** - Display proportions

**How to use:**
1. Press `V` to start range selection
2. Move cursor and press `V` again
3. Press `v` to open visualization
4. Press 1-4 to switch chart types

### 📑 File Support

- **Excel files** (.xlsx, .xlsm, .xls) with formula preservation
- **CSV files** with formula support (saved as text)
- **Multiple sheets** with easy navigation
- **Large file optimization** with lazy loading
- **Safe saving** with backup on errors

## 🚀 Installation

### Using Homebrew (macOS/Linux)

```bash
brew install CodeOne45/tap/vex
```

### Using go install

```bash
go install github.com/CodeOne45/vex-tui@latest
```

### Download Binary

Download pre-built binaries from the [releases page](https://github.com/CodeOne45/vex-tui/releases).

**Available for:**
- macOS (Intel & Apple Silicon)
- Linux (x64 & ARM64)
- Windows (x64)

### Build from Source

```bash
# Clone the repository
git clone https://github.com/CodeOne45/vex-tui.git
cd vex-tui

# Install dependencies
go mod download

# Build
go build -o vex .

# Optional: Install globally
sudo mv vex /usr/local/bin/
```

## 📖 Usage

```bash
# View a file (read-only until you press 'i')
vex data.xlsx

# Start with a specific theme
vex report.csv --theme nord

# Create new file (will be created on first save)
vex newfile.xlsx
```

## ⌨️ Keyboard Shortcuts

### Navigation

- `↑↓←→` or `hjkl` - Navigate cells
- `Page Up/Down` or `Ctrl+U/D` - Scroll by page
- `Home/End` or `0/$` - First/last column
- `g/G` - First/last column
- `Tab/Shift+Tab` - Next/previous sheet
- `Ctrl+G` - Jump to specific cell

### Editing

- `i` - Enter edit mode
- `Enter` - Commit changes (in edit) / View details (in normal)
- `Tab` - Save and move right (in edit mode)
- `Shift+Tab` - Save and move left (in edit mode)
- `Esc` - Cancel editing
- `x` - Delete cell content
- `dd` - Delete current row
- `dc` - Delete current column

### Cell Operations

- `c` - Copy cell
- `C` - Copy entire row
- `p` - Paste
- `o` - Insert row below
- `O` - Insert column right
- `Ctrl+J` - Fill down (requires selection)
- `Ctrl+L` - Fill right (requires selection)
- `Ctrl+A` - Apply formula to range (requires selection)

### File Operations

- `Ctrl+S` - Save file
- `C