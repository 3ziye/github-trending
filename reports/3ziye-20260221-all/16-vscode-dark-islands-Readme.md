# Islands Dark

<a href="https://www.buymeacoffee.com/bwya77" style="margin-right: 10px;">
    <img src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black" />
</a>
<a href="https://github.com/sponsors/bwya77">
    <img src="https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AAA" />
</a>


A dark color theme for Visual Studio Code inspired by the easemate IDE. Features floating glass-like panels, rounded corners, smooth animations, and a deeply refined UI.

- [easemate](https://x.com/easemate)
- [easemate Nav](https://x.com/Jakubantalik/status/1952672176450215944)
- [easemate effects](https://x.com/aaroniker/status/1989727838992539655)


![Islands Dark Screenshot](assets/CleanShot%202026-02-14%20at%2021.47.05@2x.png)

## Features

- Deep dark canvas (`#131217`) with floating panels
- Glass-effect borders with directional light simulation (brighter top/left, subtle bottom/right)
- Rounded corners on all panels, notifications, command palette, and sidebars
- Pill-shaped activity bar with glass selection indicators
- Breadcrumb bar and status bar that dim when not hovered
- Tab close buttons that fade in on hover
- Smooth transitions on sidebar selections, scrollbars, and status bar
- Pill-shaped scrollbar thumbs
- Color-matched icon glow effect (works best with [Seti Folder](https://marketplace.visualstudio.com/items?itemName=l-igh-t.vscode-theme-seti-folder) icon theme)
- Warm syntax highlighting with comprehensive language support (JS/TS, Python, Go, Rust, HTML/CSS, JSON, YAML, Markdown)
- IBM Plex Mono in the editor, FiraCode Nerd Font Mono in the terminal

![Islands Dark Screenshot UI](assets/CleanShot%202026-02-14%20at%2021.45.00@2x.png)

## Installation

This theme has two parts: a **color theme** and **CSS customizations** that create the floating glass panel look.

### One-Liner Install (Recommended)

The fastest way to install:

#### macOS/Linux

```bash
curl -fsSL https://raw.githubusercontent.com/bwya77/vscode-dark-islands/main/bootstrap.sh | bash
```

#### Windows

```powershell
irm https://raw.githubusercontent.com/bwya77/vscode-dark-islands/main/bootstrap.ps1 | iex
```

### Manual Clone Install

If you prefer to clone first:

#### macOS/Linux

```bash
git clone https://github.com/bwya77/vscode-dark-islands.git islands-dark
cd islands-dark
./install.sh
```

#### Windows

```powershell
git clone https://github.com/bwya77/vscode-dark-islands.git islands-dark
cd islands-dark
.\install.ps1
```

The scripts will automatically:
- ✅ Install the Islands Dark theme extension
- ✅ Install the Custom UI Style extension
- ✅ Install Bear Sans UI fonts
- ✅ Back up your existing settings and apply Islands Dark settings
- ✅ Enable Custom UI Style and reload VS Code

> **Note:** IBM Plex Mono and FiraCode Nerd Font Mono must be installed separately (the script will remind you).

### Manual Installation

If you prefer to install manually, follow these steps:

#### Step 1: Install the theme

Clone this repo and copy the extension files:

```bash
git clone https://github.com/bwya77/vscode-dark-islands.git islands-dark
cd islands-dark
mkdir -p ~/.vscode/extensions/bwya77.islands-dark-1.0.0
cp package.json ~/.vscode/extensions/bwya77.islands-dark-1.0.0/
cp -r themes ~/.vscode/extensions/bwya77.islands-dark-1.0.0/
```

On Windows (PowerShell):
```powershell
git clone https://github.com/bwya77/vscode-dark-islands.git islands-dark
cd islands-dark
$ext = "$env:USERPROFILE\.vscode\extensions\bwya77.islands-dark-1.0.0"
New-Item -ItemType Directory -Path $ext -Force
Copy-Item package.json $ext\
Copy-Item themes $ext\themes -Recurse
```

#### Step 2: Install the Custom UI Style extension

The floating panels, rounded corners, glass borders, and animations are powered by the **Custom UI Style** extension.

1. Open **Extensions** in VS Code: (`Cmd+Shift+X` / `Ctrl+Shift+X`)
2. Search for **Custom UI Style** (by `subframe7536`)
3. Click **Install**

#### Step 3: Install recommended icon theme

For the best experience with the color-matched icon glow effect, install the **Seti Folder** icon theme:

1. Open **Extensions** in VS Code (`Cmd+Shift+X` / `Ctrl+Shift+X`)
2. Search for **[Seti Folder](https://marketplace.visualstudio.com/items?itemName=l-igh-t.vscode-theme-seti-folder)** (by `l-igh-t`)
3. Click **Install**
4. Set it as your icon theme: **Command Palette** > **Preferences: File Icon Theme** > **Seti Folder**

#### Step 5: Install fonts

This theme uses two fonts:

- **IBM Plex Mono** — used in the editor
- **FiraCode Nerd Font Mono** — used in the terminal
- **Bear Sans UI** — used in the sidebar, tabs, command center, and status bar (included in `fonts/` folder)

To install Bear Sans UI:
1. Open the `fonts/` folder in this repo
2. Select all `.otf` files and double-click to open in Font Book (macOS) or right-click > Install (Windows)

If you prefer different fonts, update the `editor.fontFamily`, `terminal.integ