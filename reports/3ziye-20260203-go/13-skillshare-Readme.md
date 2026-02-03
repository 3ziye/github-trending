<p align="center" style="margin-bottom: 0;">
  <img src=".github/assets/logo.png" alt="skillshare" width="280">
</p>

<h1 align="center" style="margin-top: 0.5rem; margin-bottom: 0.5rem;">skillshare</h1>

<p align="center">
  <a href="https://skillshare.runkids.cc"><img src="https://img.shields.io/badge/Website-skillshare.runkids.cc-blue?logo=docusaurus" alt="Website"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="go.mod"><img src="https://img.shields.io/github/go-mod/go-version/runkids/skillshare" alt="Go Version"></a>
  <a href="https://github.com/runkids/skillshare/releases"><img src="https://img.shields.io/github/v/release/runkids/skillshare" alt="Release"></a>
  <img src="https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows-blue" alt="Platform">
  <a href="https://goreportcard.com/report/github.com/runkids/skillshare"><img src="https://goreportcard.com/badge/github.com/runkids/skillshare" alt="Go Report Card"></a>
  <a href="https://deepwiki.com/runkids/skillshare"><img src="https://deepwiki.com/badge.svg" alt="Ask DeepWiki"></a>
</p>

<p align="center">
  <a href="https://github.com/runkids/skillshare/stargazers"><img src="https://img.shields.io/github/stars/runkids/skillshare?style=social" alt="Star on GitHub"></a>
</p>

<p align="center">
  <strong>One source of truth for AI CLI skills. Sync everywhere with one command and simplify team sharing.</strong><br>
  Claude Code, OpenClaw, OpenCode & 40+ more.
</p>

<p align="center">
  <img src=".github/assets/demo.gif" alt="skillshare demo" width="960">
</p>

<p align="center">
  <a href="https://skillshare.runkids.cc">Website</a> •
  <a href="#installation">Install</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="#commands">Commands</a> •
  <a href="#team-edition">Team Edition</a> •
  <a href="https://skillshare.runkids.cc/docs/intro">Docs</a>
</p>

> [!NOTE]
> **Recent Updates**
> | Version | Highlights |
> |---------|------------|
> | [0.8.0](https://github.com/runkids/skillshare/releases/tag/v0.8.0) | `pull` → `collect` rename, clearer command symmetry, refactoring |
> | [0.7.0](https://github.com/runkids/skillshare/releases/tag/v0.7.0) | Windows support, GitHub skill search |
> | [0.6.0](https://github.com/runkids/skillshare/releases/tag/v0.6.0) | Team Edition with tracked repos |

## Why skillshare?

Install tools get skills onto agents. **Skillshare keeps them in sync.**

| Feature | Description |
|---------|-------------|
| 🔗 **Non-destructive Merge** | Sync shared skills while preserving CLI-specific ones. Per-skill symlinks keep local skills untouched. |
| ↔️ **Bidirectional Sync** | Created a skill in Claude? Collect it back to source and share with OpenClaw, OpenCode, and others. |
| 🌐 **Cross-machine Sync** | One git push/pull syncs skills across all your machines. No re-running install commands. |
| 📦 **Unified Source** | Local skills and installed skills live together in one directory. No separate management. |
| 👥 **Team Sharing** | Install team repos once, update anytime with git pull. Changes sync to all agents instantly. |
| ✨ **AI-Native** | Built-in skill lets AI operate skillshare directly. No manual CLI needed. |

## Installation

### Quick Install (macOS/Linux)

```bash
curl -fsSL https://raw.githubusercontent.com/runkids/skillshare/main/install.sh | sh
```

### Quick Install (Windows PowerShell)

```powershell
irm https://raw.githubusercontent.com/runkids/skillshare/main/install.ps1 | iex
```

### Homebrew (macOS)

```bash
brew install runkids/tap/skillshare
```

### Uninstall

```bash
# macOS/Linux
brew uninstall skillshare               # Homebrew
sudo rm /usr/local/bin/skillshare       # Manual install
rm -rf ~/.config/skillshare             # Config & data (optional)

# Windows (PowerShell)
Remove-Item "$env:LOCALAPPDATA\Programs\skillshare" -Recurse -Force
Remove-Item "$env:USERPROFILE\.config\skillshare" -Recurse -Force  # optional
```

### Shorthand (Optional)

Add an alias to your shell config (`~/.zshrc` or `~/.bashrc`):

```bash
alias ss='skillshare'
```

## Quick Start

```bash
skillshare init --dry-run  # Preview setup
skillshare init            # Auto-detects CLIs, sets up git
skillshare sync            # Sync to all targets
```

Done. Your skills are now synced across all AI CLI tools.

## How It Works

```
┌─────────────────────────────────────────────────────────────┐
│                       Source Directory                      │
│                 ~/.config/skillshare/skills/                │
└─────────────────────────────────────────────────────────────┘
                              │ sync
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
       ┌───────────┐   ┌───────────┐   ┌───────────┐
       │  Claude   │   │  OpenCode │   │ OpenClaw  │   ...
       └───────────┘   └───────────┘   └───────────┘
```

| Platform | Source Path | Link Type |
|----------|----