<p align="center" style="margin-bottom: 0;">
  <img src=".github/assets/logo.png" alt="skillshare" width="280">
</p>

<h1 align="center" style="margin-top: 0.5rem; margin-bottom: 0.5rem;">skillshare</h1>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="go.mod"><img src="https://img.shields.io/github/go-mod/go-version/runkids/skillshare" alt="Go Version"></a>
  <a href="https://github.com/runkids/skillshare/releases"><img src="https://img.shields.io/github/v/release/runkids/skillshare" alt="Release"></a>
</p>

<p align="center">
  <strong>Sync skills to all your AI CLI tools with one command</strong><br>
  Supports Amp, Claude Code, Codex CLI, Crush, Cursor, Gemini CLI, GitHub Copilot, Goose, Letta, Antigravity, OpenCode
</p>

<p align="center">
  <img src=".github/assets/demo.gif" alt="skillshare demo" width="600">
</p>

<p align="center">
  <a href="#installation">Install</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="#commands">Commands</a> •
  <a href="#team-edition">Team Edition</a> •
  <a href="#reference">Reference</a> •
  <a href="#faq">FAQ</a> •
  <a href="#common-issues">Common Issues</a>
</p>

> [!NOTE]
> **[What's New in 0.6.0 — Team Edition 🎉](https://github.com/runkids/skillshare/releases/tag/v0.6.0)**
> - **Tracked Repositories**: `install --track` to clone team skill repos, `update` to keep them current
> - **Nested Skills**: Organize skills in folders (`work/api/` → `work__api/`)
> - **Auto-Pruning**: Orphaned symlinks are automatically cleaned on sync
> - **Collision Detection**: Warns when multiple skills share the same name
> - [Learn more →](#team-edition)

## Why skillshare?

**The problem:** You create a skill in Claude, but need it in Cursor, Codex, and Gemini too. Manually copying? Tedious. What if you update it? Copy again.

**The solution:** One source of truth. Create once, sync everywhere.

```bash
skillshare pull claude && skillshare sync  # Pull from Claude → sync to all
```

| What makes it different | |
|-------------------------|---|
| 🔄 Bidirectional sync | `pull` from any target, `sync` to all |
| 🌐 Cross-machine sync | `push` / `pull --remote` via git |
| 💾 Backup & restore | Automatic before sync, restore anytime |
| 🔍 Diagnostics | `doctor` checks git, broken links, duplicates |
| 🤖 AI-native | Built-in skill lets your AI manage everything |

## AI-Native Execution

The built-in [`skillshare` skill](https://github.com/runkids/skillshare/tree/main/skills/skillshare) enables your AI CLI to manage skills directly. Just download the skill folder into your AI CLI's skills directory — the binary is auto-downloaded on first use.

```text
┌─────────────────────────────────────────────────────────────┐
│  User: "sync my skills to all targets"                      │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  AI reads skillshare skill                                  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  skillshare sync                                            │
│  ✓ Synced 5 skills to claude, codex, cursor                 │
└─────────────────────────────────────────────────────────────┘
```

> [!TIP]
> Once installed, just say:
> - *"Show my skillshare status"*
> - *"Sync my skills to all targets"*
> - *"Pull skills from Claude and sync everywhere"*
> - *"Install the pdf skill from anthropics/skills"*

## Installation

### Quick Install

```bash
curl -fsSL https://raw.githubusercontent.com/runkids/skillshare/main/install.sh | sh
```

Installs to `/usr/local/bin/`. Works on macOS and Linux.

### Homebrew (macOS)

```bash
brew install runkids/tap/skillshare
```

### Uninstall

```bash
brew uninstall skillshare              # Homebrew
sudo rm /usr/local/bin/skillshare      # Manual install
rm -rf ~/.config/skillshare            # Config & data (optional)
```

## Quick Start

```bash
skillshare init --dry-run  # Preview setup
skillshare init            # Auto-detects installed CLIs, sets up git
skillshare sync            # Syncs skills to all targets
```

Done! Your skills are now synced across all AI CLI tools.

## How It Works

```
┌─────────────────────────────────────────────────────────────┐
│                  ~/.config/skillshare/skills/               │
│         my-skill/   another-skill/   shared-util/           │
└─────────────────────────────────────────────────────────────┘
                              │
              ┌───────────────┼───────────────┐
              │               │               │
              ▼               ▼               ▼
       ┌───────────┐   ┌───────────┐   ┌───────────┐
       │  Claude   │   │   Codex   │   │  OpenCode │
       │  skill