# DotState

> **A modern, secure, and user-friendly dotfile manager built with Rust**

DotState is a terminal-based tool that helps you manage your dotfiles effortlessly. Whether you're syncing your configuration across multiple machines or setting up a new development environment, DotState makes it simple, safe, and fast.

## Demo
https://github.com/user-attachments/assets/9be0df5e-87ce-4b61-ae0f-1c8ffe94cb36

## Why DotState?

Managing dotfiles can be a pain. You want your `.zshrc`, `.vimrc`, and other config files synced across machines, but traditional solutions are either too complex, insecure, or require too much manual work.

**DotState solves this by being:**
- 🦀 **Built with Rust** - Fast, memory-safe, and reliable
- 🔒 **Secure by design** - No shell injection vulnerabilities, safe file operations
- 🎨 **Beautiful TUI** - Intuitive interface that doesn't require learning Git
- ⚡ **Lightning fast** - Non-blocking operations, instant feedback
- 🛡️ **Safe** - Automatic backups before any file operations
- 🔄 **Git-powered** - Store dotfiles in GitHub, GitLab, Bitbucket, or any git host

## What Makes DotState Different?

### Traditional Dotfile Managers
- Require Git knowledge
- Manual symlink management
- No built-in backup system
- Complex setup process

### DotState
- **Zero Git knowledge required** - We handle everything
- **Automatic symlink management** - Files are linked automatically
- **Built-in backups** - Your files are safe before any operation
- **One-command setup** - Get started in seconds
- **Profile support** - Separate configs for work, personal, Mac, Linux, etc.
- **Package management** - Track and install CLI tools per profile
- **Beautiful TUI** - Visual interface with mouse support

## Features

### 🎯 Core Features

- **Profile Management**: Create separate profiles for different contexts (work, personal, Mac, Linux, etc.)
- **Flexible Git Sync**: Automatic sync with GitHub, GitLab, Bitbucket, or any git host
- **Two Setup Modes**: Let DotState create a GitHub repo for you, or use your own repository
- **Smart File Detection**: Automatically finds common dotfiles in your home directory
- **Safe Operations**: Automatic backups before any file modification
- **Symlink Management**: Automatic creation and management of symlinks
- **Custom Files**: Add any file or directory, not just dotfiles

### 📦 Package Management

- **CLI Tool Tracking**: Define and track CLI tools and dependencies per profile
- **Multi-Manager Support**: Works with Homebrew, Cargo, npm, pip, and more
- **Installation Flow**: Check what's missing and install with one command
- **Custom Packages**: Support for custom installation scripts

### 🎨 User Experience

- **Beautiful TUI**: Modern terminal interface built with Ratatui
- **Mouse Support**: Click to navigate and interact
- **Real-time Feedback**: See what's happening as it happens
- **Error Recovery**: Clear error messages with actionable guidance
- **CLI & TUI**: Full-featured CLI for automation, beautiful TUI for interactive use

### 🔒 Security

- **No Shell Injection**: Direct command execution, no shell interpretation
- **Safe File Operations**: Validates paths, prevents dangerous operations
- **Secure GitHub Integration**: Token-based authentication
- **Backup System**: Automatic backups before any destructive operation

## Installation

### Prebuilt from website (Recommended)
[Installation Guide](https://dotstate.serkan.dev/#installation)
```bash
/bin/bash -c "$(curl -fsSL https://dotstate.serkan.dev/install.sh)"
```

### Using Cargo

```bash
cargo install dotstate
```

### Using Homebrew

```bash
brew tap serkanyersen/dotstate
brew install dotstate
```

Or use the direct install:
```bash
brew install serkanyersen/dotstate/dotstate
```

## Quick Start

1. **Launch DotState**:
   ```bash
   dotstate
   ```

2. **First-time Setup**:
   - Choose how to set up your repository:
     - **Option A: Create for me (GitHub)** - DotState creates a repo on GitHub
       - Enter your GitHub token (create one at [github.com/settings/tokens](https://github.com/settings/tokens))
       - **Tip**: You can also set the `DOTSTATE_GITHUB_TOKEN` environment variable
       - Choose repository name and visibility (private/public)
     - **Option B: Use my own repository** - Bring your own git repo
       - Create a repo on any git host (GitHub, GitLab, Bitbucket, etc.)
       - Clone it locally and set up your credentials
       - Point DotState to your local repo path

3. **Add Your Files**:
   - Navigate to "Manage Files"
   - Select files to sync (they're automatically added)
   - Files are moved to the repo and symlinked automatically

4. **Sync with Remote**:
   - Go to "Sync with Remote"
   - Your files are committed, pulled, and pushed automatically

That's it! Your dotfiles are now synced and ready to use on any machine.

## CLI Usage

DotState also provides a powerful CLI for automation:

```bash
# List all synced files
dotstate list

# Add a file to sync
dotstate a