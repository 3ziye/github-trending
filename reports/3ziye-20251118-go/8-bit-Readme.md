<div align="center">

<img src="https://github.com/superstarryeyes/bit/blob/main/images/bit-icon.png?raw=true" alt="Bit Icon" width="35%" />

### Bit - Terminal ANSI Logo Designer & Font Library
[![License: MIT](https://img.shields.io/badge/License-MIT-05bd7e.svg)](LICENSE)
[![Terminal](https://img.shields.io/badge/interface-terminal-05bd7e.svg)](https://github.com/superstarryeyes/bit)
[![Go](https://img.shields.io/badge/Go-1.25+-05bd7e.svg)](https://golang.org)
[![Discord](https://img.shields.io/badge/Discord-Join%20our%20Community-5865F2?logo=discord&logoColor=white)](https://discord.gg/z8sE2gnMNk)

[Features](#-features) • [Quick Start](#-quick-start) • [Installation](#-installation) • [Usage](#-usage) • [Library](#-library) • [Font Collection](#%EF%B8%8F-font-collection) • [Contributing](#️-contributing) • [License](#-license) • [Acknowledgments](#-acknowledgments)

<img src="https://github.com/superstarryeyes/bit/blob/main/images/bit-screenshot.gif" alt="Bit Screenshot" width="100%" />

</div>

---

## ✨ Features

| **Feature**                             | **Description**                                                                                |
| --------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **🌟 100+ Font Styles**               | Classic terminal, retro gaming, modern pixel, decorative, and monospace fonts. All free for commercial and personal use.                  |
| **📤 Multi-Format Export**              | Export to TXT, Go, JavaScript, Python, Rust, and Bash with language-specific formatting.               |
| **🎨 Advanced Text Effects**            | Color gradient effects (horizontal & vertical), shadow effects (horizontal & vertical), and text scaling (0.5×–4×).|
| **🌈 Rich Color Support**               | 14 vibrant predefined UI colors that can be combined with gradients. The library and CLI also accept any hex color for unlimited possibilities.|
| **📐 Alignment & Spacing**                   | Adjust character, word, and line spacing. Align text left, center, or right.          |
| **⚡️ Smart Typography**                 | Automatic kerning, descender detection and alignment.           |
| **🛠️ Powerful CLI Tool**                | Render text quickly with extended options for fonts, colors, spacing, and effects.            |
| **📚 Standalone Go Library**           | A simple, self-contained API with type-safe enums for effortless programmatic ANSI text rendering.                           |

---

## 🚀 Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/superstarryeyes/bit
cd bit

# 2. Install dependencies
go mod tidy

# 3. Build the interactive UI
go build -o bit ./cmd/bit

# 4. Start creating!
./bit
```

---

## 📦 Installation

### Prerequisites

- **Go 1.25+** - Required for proper module support

### Build Commands

```bash
# Clone repository
git clone https://github.com/superstarryeyes/bit
cd bit

# Install dependencies
go mod tidy

# Build the interactive UI (includes embedded fonts)
go build -o bit ./cmd/bit

# Build the command line tool
go build -o ansifonts-cli ./cmd/ansifonts
```

> [!NOTE]
> Fonts are embedded using `go:embed`, ensuring the binaries are fully self-contained.

---

## 💻 Usage

### Keyboard Controls

| **Key Binding**                         | **Action Description**                                                                         |
| --------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `← →`                                   | Navigate between the 6 main control panels                                                     |
| `Tab`                                   | Access sub-modes within panels   |
| `↑ ↓`                                   | Adjust values in the currently selected panel or navigate text rows in multi-line mode        |
| `Enter`                                 | Activate/deactivate text input mode for editing      |
| `r`                                     | Randomize font, colors, and gradient settings for instant inspiration                          |
| `e`                                     | Enter export mode to save your creation in various formats                                     |
| `Esc`                                   | Quit the application and return to terminal                                                    |

### Control Panels

The UI features **6 main control panels** with sub-modes accessible via **Tab** key:

#### 1. 🔴 **Text Input Panel** (2 modes)
   - **Text Input Mode**: Enter and edit text with multi-line support
     - Press `↓` to create new row
     - Press `↑↓` to navigate between rows
     - Cursor positions are tracked per-row
     - The row count is shown in label when editing multiple rows
   - **Text Alignment Mode**: Choose Left, Center, or Right alignment

#### 2. 🟢 **Font Selection Panel**
 