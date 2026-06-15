<p align="center">
    <picture>
      <img src="./images/intelligent-terminal-logo.png" alt="Intelligent Terminal logo" width="128">
    </picture>
</p>

# Welcome to the Intelligent Terminal repo

<details>
  <summary><strong>Table of Contents</strong></summary>

- [What is Intelligent Terminal?](#what-is-intelligent-terminal)
- [Installing and running Intelligent Terminal](#installing-and-running-intelligent-terminal)
  - [Microsoft Store](#microsoft-store-recommended)
  - [WinGet](#winget)
  - [Downloads](#downloads)
- [Get Started](#get-started)
- [Keyboard Shortcuts](#keyboard-shortcuts)
- [Configuration](#configuration)
- [Features](#features)
  - [Agent Status Bar](#agent-status-bar)
  - [Agent Pane](#agent-pane)
  - [Agent Management](#agent-management)
  - [Error Detection](#error-detection)
  - [Command Palette](#command-palette)
- [Data & Privacy](#data--privacy)
- [Building the Code](#building-the-code)
- [FAQ](./doc/faq.md)
- [Feedback](#feedback)
- [Contributing](#contributing)
- [Code of Conduct](#code-of-conduct)
- [Security](#security)
- [Trademarks](#trademarks)

</details>

<br />

## What is Intelligent Terminal?

Intelligent Terminal is an experimental fork of [Windows Terminal](https://github.com/microsoft/terminal) with native agent integration.

Intelligent Terminal works with any [Agent Client Protocol (ACP)-compatible](https://agentclientprotocol.com/get-started/agents) agent CLI. All you need is to install your preferred agent CLI on your PC. If you don't have a preferred agent, we'll get you setup with [GitHub Copilot CLI](https://github.com/features/copilot/cli/).

Intelligent Terminal takes all the features you love in Windows Terminal such as:  tabs, profiles, themes, settings, shells, and keyboard shortcuts, which all work the way you expect.

Read the [announcement blog post](https://devblogs.microsoft.com/commandline/announcing-intelligent-terminal-version-0-1/) for more details.

---

## Installing and running Intelligent Terminal

> [!NOTE]
> Intelligent Terminal requires Windows 10 2004 (19041) or later. You also need a supported agent CLI and subscription. [GitHub Copilot](https://github.com/features/copilot/cli/) is the default.

### Microsoft Store (recommended)

Install the [Intelligent Terminal from the Microsoft Store](https://apps.microsoft.com/detail/9NMQC2SSJX24).
This allows you to always be on the latest version when we release new builds
with automatic upgrades.

### WinGet

[winget](https://github.com/microsoft/winget-cli) users can download and install
the latest Intelligent Terminal release by installing the `Microsoft.IntelligentTerminal`
package:

```powershell
winget install --id Microsoft.IntelligentTerminal -e
```

### Downloads

| Distribution | Architecture | Link |
|--------------|:------------:|------|
| App Installer | x64, arm64, x86 | [Download](https://github.com/microsoft/intelligent-terminal/releases/latest) |


---

## Get Started

1. On first launch, choose your agent. Intelligent Terminal auto-detects several [ACP-compatible](https://agentclientprotocol.com/get-started/agents) agent CLIs on your machine (Copilot/Claude/Codex/Gemini). If none are found, it defaults to GitHub Copilot CLI and installs it for you via WinGet.
3. If you aren't already authenticated, the agent pane walks you through sign-in.
4. Start asking questions and using the agent pane for assistance. The agent has context on your shell output, no copy-pasting needed.

> [!TIP]
> If you see "running scripts is disabled on this system" or an `UnauthorizedAccess` error in PowerShell, your execution policy is blocking your profile and Intelligent Terminal can't initialize shell integration. Run:
> ```powershell
> Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
> ```
> If you run into any other issues or dependency errors, see [installing-dependencies.md](./doc/installing-dependencies.md).

---

## Keyboard Shortcuts

All shortcuts are customizable through Intelligent Terminal settings.

| Shortcut | Action |
|----------|--------|
| <kbd>Ctrl+Shift+.</kbd> | Toggle the agent pane |
| <kbd>Ctrl+Shift+I</kbd> | Switch focus to/from the agent pane |
| <kbd>Ctrl+Alt+.</kbd> | Open agent pane with error context |
| <kbd>Ctrl+Shift+/</kbd> | Open agent management |
| <kbd>Alt+Shift+/</kbd> | Open Command Palette in prompt mode |
| <kbd>Alt+Shift+B</kbd> | Open an interactive delegate-agent tab with no startup prompt |

---

## Configuration

Everything is configurable through Intelligent Terminal settings, under "Agent" settings.

| Setting | Options |
|---------|---------|
| Agent and model | GitHub Copilot (default), or any ACP-compatible agent CLI, including custom or local agents. Configurable for both the agent pane and command palette. |
| Pane placement | Top, Bottom (default), Left, Right |
| Error detection | Allows Intelligent Terminal