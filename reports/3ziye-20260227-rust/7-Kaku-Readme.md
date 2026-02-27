<div align="center">
  <h1>Kaku</h1>
  <p><em>A fast, out-of-the-box terminal built for AI coding.</em></p>
</div>

<p align="center">
  <a href="https://github.com/tw93/Kaku/stargazers"><img src="https://img.shields.io/github/stars/tw93/Kaku?style=flat-square" alt="Stars"></a>
  <a href="https://github.com/tw93/Kaku/releases"><img src="https://img.shields.io/github/v/tag/tw93/Kaku?label=version&style=flat-square" alt="Version"></a>
  <a href="LICENSE.md"><img src="https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square" alt="License"></a>
  <a href="https://github.com/tw93/Kaku/commits"><img src="https://img.shields.io/github/commit-activity/m/tw93/Kaku?style=flat-square" alt="Commits"></a>
  <a href="https://twitter.com/HiTw93"><img src="https://img.shields.io/badge/follow-Tw93-red?style=flat-square&logo=Twitter" alt="Twitter"></a>
</p>

<p align="center">
  <img src="assets/kaku.jpeg" alt="Kaku Screenshot" width="1000" />
  <br/>
  Kaku is a deeply customized fork of <a href="https://github.com/wez/wezterm">WezTerm</a>, designed for an out-of-the-box experience.
</p>

## Features

- **Zero Config**: Defaults with JetBrains Mono, opencode theme, macOS font rendering, and low-res font sizing.
- **Curated Shell Suite**: Built-in zsh plugins with optional CLI tools for prompt, diff, and navigation workflows.
- **Fast & Lightweight**: 40% smaller binary, instant startup, lazy loading, stripped-down GPU-accelerated core.
- **WezTerm-Compatible Config**: Use WezTerm's Lua config directly with full API compatibility and no migration.

## Quick Start

1. [Download Kaku DMG](https://github.com/tw93/Kaku/releases/latest) & Drag to Applications
2. Or install with Homebrew: `brew install tw93/tap/kakuku`
3. Open Kaku. The app is notarized by Apple, so it opens without security warnings
4. On first launch, Kaku will automatically set up your shell environment

## Usage Guide

Kaku comes with intuitive macOS-native shortcuts:

| Action | Shortcut |
| :--- | :--- |
| Toggle Global Window | `Cmd + Opt + Ctrl + K` |
| New Tab | `Cmd + T` |
| New Window | `Cmd + N` |
| Close Tab/Pane | `Cmd + W` |
| Navigate Tabs | `Cmd + Shift + [`, `Cmd + Shift + ]` or `Cmd + 1-9` |
| Navigate Panes | `Cmd + Opt + Arrows` |
| Split Pane Vertical | `Cmd + D` |
| Split Pane Horizontal | `Cmd + Shift + D` |
| Toggle Split Direction | `Cmd + Shift + S` |
| Zoom/Unzoom Pane | `Cmd + Shift + Enter` |
| Resize Pane | `Cmd + Ctrl + Arrows` |
| Clear Screen | `Cmd + K` |
| Doctor Panel | `Ctrl + Shift + L` |
| Kaku AI Settings | `Cmd + Shift + A` |
| Kaku Assistant Apply Suggestion | `Cmd + Shift + E` |
| Open Lazygit | `Cmd + Shift + G` |
| Yazi File Manager | `Cmd + Shift + Y` or `y` |
| Font Size | `Cmd + +`, `Cmd + -`, `Cmd + 0` |
| Smart Jump | `z <dir>` |
| Smart Select | `z -l <dir>` |
| Recent Dirs | `z -t` |

### Intuitive Interactions

- **Visual Bell**: A blinking dot appears on inactive tabs when background tasks finish.
- **Global Hotkey**: Press `Cmd + Opt + Ctrl + K` anytime to float Kaku over your current workspace.
- **Copy on Select**: Highlighting any text automatically copies it to your clipboard with a confirmation toast.
- **Zoom Window**: Double-click the title bar or tab bar empty space to safely zoom or unzoom the window.
- **Finder Integration**: Right-click folders in macOS Finder and deploy Kaku via Services, or drop multiple files directly onto the Kaku Dock icon.
- **History Peek**: Scroll up while inside full-screen apps like `less` or `vim` to lift the screen and peek at your primary shell history without exiting.

## Configuration

Kaku comes with a carefully curated shell stack for immediate productivity, so you can focus on AI coding without opening vscode:

Built-in zsh plugins bundled by default:

- **z**: A smarter cd command that learns your most used directories for instant navigation.
- **zsh-completions**: Extended command and subcommand completion definitions.
- **Syntax Highlighting**: Real-time command validation and coloring.
- **Autosuggestions**: Intelligent, history-based completions similar to Fish shell.

Optional CLI tools installed via Homebrew during `kaku init`:

- **Starship**: A fast, customizable prompt showing git status, package versions, and execution time.
- **Delta**: A syntax-highlighting pager for git, diff, and grep output.
- **Lazygit**: A terminal UI for fast, visual Git workflows without leaving the shell.
- **Yazi**: A terminal file manager. Use `y` to launch it and sync the shell directory on exit.

Kaku uses `~/.config/kaku/kaku.lua` for configuration, fully compatible with WezTerm's Lua API, with built-in defaults at `Kaku.app/Contents/Resources/kaku.lua` as fallback.

Run `kaku` in your terminal to see all available commands such as `kaku ai`, `kaku config`, `kaku doctor`, `kaku update`, and `kaku reset`.

## Kaku AI

Kaku includes a built-in assistant for command-line error recovery and a unified settings UI for external AI coding tools.

- **Kaku Assistant**: 