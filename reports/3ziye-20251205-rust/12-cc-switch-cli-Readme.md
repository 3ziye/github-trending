<div align="center">

# CC-Switch CLI

[![Version](https://img.shields.io/badge/version-4.1.1-blue.svg)](https://github.com/saladday/cc-switch-cli/releases)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](https://github.com/saladday/cc-switch-cli/releases)
[![Built with Rust](https://img.shields.io/badge/built%20with-Rust-orange.svg)](https://www.rust-lang.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**Command-Line Management Tool for Claude Code, Codex & Gemini CLI**

Unified management for Claude Code, Codex & Gemini CLI provider configurations, MCP servers, Skills extensions, and system prompts.

[English](README.md) | [中文](README_ZH.md)

</div>

---

## 📖 About

This project is a **CLI fork** of [CC-Switch](https://github.com/farion1231/cc-switch).


**Credits:** Original architecture and core functionality from [farion1231/cc-switch](https://github.com/farion1231/cc-switch)

---

## 📸 Screenshots

<table>
  <tr>
    <th>Interactive Main Menu</th>
    <th>Provider Management</th>
  </tr>
  <tr>
    <td><img src="assets/screenshots/main-en.png" alt="Main Menu" width="100%"/></td>
    <td><img src="assets/screenshots/add-en.png" alt="Provider Management" width="100%"/></td>
  </tr>
</table>

---

## 🚀 Quick Start

**Interactive Mode (Recommended)**
```bash
cc-switch
```
🤩 Follow on-screen menus to explore features.

**Command-Line Mode**
```bash
cc-switch provider list              # List providers
cc-switch provider switch <id>       # Switch provider
cc-switch mcp sync                   # Sync MCP servers

# Use the global `--app` flag to target specific applications:
cc-switch --app claude provider list    # Manage Claude providers
cc-switch --app codex mcp sync          # Sync Codex MCP servers
cc-switch --app gemini prompts list     # List Gemini prompts

# Supported apps: `claude` (default), `codex`, `gemini`
```

See the "Features" section below for full command list.

---

## ✨ Features

### 🔌 Provider Management

Manage API configurations for **Claude Code**, **Codex**, and **Gemini**.

**Features:** One-click switching, multi-endpoint support, API key management, speed testing, provider duplication.

```bash
cc-switch provider list              # List all providers
cc-switch provider current           # Show current provider
cc-switch provider switch <id>       # Switch provider
cc-switch provider add               # Add new provider
cc-switch provider edit <id>         # Edit existing provider
cc-switch provider duplicate <id>    # Duplicate a provider
cc-switch provider delete <id>       # Delete provider
cc-switch provider speedtest <id>    # Test API latency
```

### 🛠️ MCP Server Management

Manage Model Context Protocol servers across Claude/Codex/Gemini.

**Features:** Unified management, multi-app support, three transport types (stdio/http/sse), automatic sync, smart TOML parser.

```bash
cc-switch mcp list                   # List all MCP servers
cc-switch mcp add                    # Add new MCP server (interactive)
cc-switch mcp edit <id>              # Edit MCP server
cc-switch mcp delete <id>            # Delete MCP server
cc-switch mcp enable <id> --app claude   # Enable for specific app
cc-switch mcp disable <id> --app claude  # Disable for specific app
cc-switch mcp validate <command>     # Validate command in PATH
cc-switch mcp sync                   # Sync to live files
cc-switch mcp import --app claude    # Import from live config
```

### 💬 Prompts Management

Manage system prompt presets for AI coding assistants.

**Cross-app support:** Claude (`CLAUDE.md`), Codex (`AGENTS.md`), Gemini (`GEMINI.md`).

```bash
cc-switch prompts list               # List prompt presets
cc-switch prompts current            # Show current active prompt
cc-switch prompts activate <id>      # Activate prompt
cc-switch prompts deactivate         # Deactivate current active prompt
cc-switch prompts create             # Create new prompt preset
cc-switch prompts edit <id>          # Edit prompt preset
cc-switch prompts show <id>          # Display full content
cc-switch prompts delete <id>        # Delete prompt
```

### 🎯 Skills Management

⚠️ **Note: Not yet implemented in v4.1.x** - This feature is planned for future releases.

Manage and extend Claude Code/Codex/Gemini capabilities with community skills.

**Features:** Search skill marketplace, install/uninstall, repository management, skill information.

```bash
cc-switch skills list                # List installed skills
cc-switch skills search <query>      # Search available skills
cc-switch skills install <name>      # Install a skill
cc-switch skills uninstall <name>    # Uninstall a skill
cc-switch skills info <name>         # Show skill information
cc-switch skills repos               # Manage skill repositories
```

### ⚙️ Configuration Management

Manage configuration backups, imports, and exports.

**Features:** Custom backup naming, interactive b