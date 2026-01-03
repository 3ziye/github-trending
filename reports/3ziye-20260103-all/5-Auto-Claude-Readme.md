# Auto Claude

**Autonomous multi-agent coding framework that plans, builds, and validates software for you.**

![Auto Claude Kanban Board](.github/assets/Auto-Claude-Kanban.png)

<!-- TOP_VERSION_BADGE -->
[![Version](https://img.shields.io/badge/version-2.7.2-blue?style=flat-square)](https://github.com/AndyMik90/Auto-Claude/releases/tag/v2.7.2)
<!-- TOP_VERSION_BADGE_END -->
[![License](https://img.shields.io/badge/license-AGPL--3.0-green?style=flat-square)](./agpl-3.0.txt)
[![Discord](https://img.shields.io/badge/Discord-Join%20Community-5865F2?style=flat-square&logo=discord&logoColor=white)](https://discord.gg/KCXaPBr4Dj)
[![CI](https://img.shields.io/github/actions/workflow/status/AndyMik90/Auto-Claude/ci.yml?branch=main&style=flat-square&label=CI)](https://github.com/AndyMik90/Auto-Claude/actions)

---

## Download

### Stable Release

<!-- STABLE_VERSION_BADGE -->
[![Stable](https://img.shields.io/badge/stable-2.7.2-blue?style=flat-square)](https://github.com/AndyMik90/Auto-Claude/releases/tag/v2.7.2)
<!-- STABLE_VERSION_BADGE_END -->

<!-- STABLE_DOWNLOADS -->
| Platform | Download |
|----------|----------|
| **Windows** | [Auto-Claude-2.7.2-win32-x64.exe](https://github.com/AndyMik90/Auto-Claude/releases/download/v2.7.2/Auto-Claude-2.7.2-win32-x64.exe) |
| **macOS (Apple Silicon)** | [Auto-Claude-2.7.2-darwin-arm64.dmg](https://github.com/AndyMik90/Auto-Claude/releases/download/v2.7.2/Auto-Claude-2.7.2-darwin-arm64.dmg) |
| **macOS (Intel)** | [Auto-Claude-2.7.2-darwin-x64.dmg](https://github.com/AndyMik90/Auto-Claude/releases/download/v2.7.2/Auto-Claude-2.7.2-darwin-x64.dmg) |
| **Linux** | [Auto-Claude-2.7.2-linux-x86_64.AppImage](https://github.com/AndyMik90/Auto-Claude/releases/download/v2.7.2/Auto-Claude-2.7.2-linux-x86_64.AppImage) |
| **Linux (Debian)** | [Auto-Claude-2.7.2-linux-amd64.deb](https://github.com/AndyMik90/Auto-Claude/releases/download/v2.7.2/Auto-Claude-2.7.2-linux-amd64.deb) |
<!-- STABLE_DOWNLOADS_END -->

### Beta Release

> ⚠️ Beta releases may contain bugs and breaking changes. [View all releases](https://github.com/AndyMik90/Auto-Claude/releases)

<!-- BETA_VERSION_BADGE -->
[![Beta](https://img.shields.io/badge/beta-2.7.2--beta.10-orange?style=flat-square)](https://github.com/AndyMik90/Auto-Claude/releases/tag/v2.7.2-beta.10)
<!-- BETA_VERSION_BADGE_END -->

<!-- BETA_DOWNLOADS -->
| Platform | Download |
|----------|----------|
| **Windows** | [Auto-Claude-2.7.2-beta.10-win32-x64.exe](https://github.com/AndyMik90/Auto-Claude/releases/download/v2.7.2-beta.10/Auto-Claude-2.7.2-beta.10-win32-x64.exe) |
| **macOS (Apple Silicon)** | [Auto-Claude-2.7.2-beta.10-darwin-arm64.dmg](https://github.com/AndyMik90/Auto-Claude/releases/download/v2.7.2-beta.10/Auto-Claude-2.7.2-beta.10-darwin-arm64.dmg) |
| **macOS (Intel)** | [Auto-Claude-2.7.2-beta.10-darwin-x64.dmg](https://github.com/AndyMik90/Auto-Claude/releases/download/v2.7.2-beta.10/Auto-Claude-2.7.2-beta.10-darwin-x64.dmg) |
| **Linux** | [Auto-Claude-2.7.2-beta.10-linux-x86_64.AppImage](https://github.com/AndyMik90/Auto-Claude/releases/download/v2.7.2-beta.10/Auto-Claude-2.7.2-beta.10-linux-x86_64.AppImage) |
| **Linux (Debian)** | [Auto-Claude-2.7.2-beta.10-linux-amd64.deb](https://github.com/AndyMik90/Auto-Claude/releases/download/v2.7.2-beta.10/Auto-Claude-2.7.2-beta.10-linux-amd64.deb) |
| **Linux (Flatpak)** | [Auto-Claude-2.7.2-beta.10-linux-x86_64.flatpak](https://github.com/AndyMik90/Auto-Claude/releases/download/v2.7.2-beta.10/Auto-Claude-2.7.2-beta.10-linux-x86_64.flatpak) |
<!-- BETA_DOWNLOADS_END -->

> All releases include SHA256 checksums and VirusTotal scan results for security verification.

---

## Requirements

- **Claude Pro/Max subscription** - [Get one here](https://claude.ai/upgrade)
- **Claude Code CLI** - `npm install -g @anthropic-ai/claude-code`
- **Git repository** - Your project must be initialized as a git repo
- **Python 3.12+** - Required for the backend and Memory Layer

---

## Quick Start

1. **Download and install** the app for your platform
2. **Open your project** - Select a git repository folder
3. **Connect Claude** - The app will guide you through OAuth setup
4. **Create a task** - Describe what you want to build
5. **Watch it work** - Agents plan, code, and validate autonomously

---

## Features

| Feature | Description |
|---------|-------------|
| **Autonomous Tasks** | Describe your goal; agents handle planning, implementation, and validation |
| **Parallel Execution** | Run multiple builds simultaneously with up to 12 agent terminals |
| **Isolated Workspaces** | All changes happen in git worktrees - your main branch stays safe |
| **Self-Validating QA** | Built-in quality assurance loop catches issues before you review |
| **AI-Powered Merge** | Automatic conflict resolution when integrating back to main |
| **Memory Layer** | Agents retain insights across sessions for smarter builds |
| **GitHub/GitLab Integration** | Import issues, investigate with AI, create merge requests |