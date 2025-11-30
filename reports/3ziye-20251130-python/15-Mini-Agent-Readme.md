# Mini Agent

English | [中文](./README_CN.md)

**Mini Agent** is a minimal yet professional demo project that showcases the best practices for building agents with the MiniMax M2 model. Leveraging an Anthropic-compatible API, it fully supports interleaved thinking to unlock M2's powerful reasoning capabilities for long, complex tasks.

This project comes packed with features designed for a robust and intelligent agent development experience:

*   ✅ **Full Agent Execution Loop**: A complete and reliable foundation with a basic toolset for file system and shell operations.
*   ✅ **Persistent Memory**: An active **Session Note Tool** ensures the agent retains key information across multiple sessions.
*   ✅ **Intelligent Context Management**: Automatically summarizes conversation history to handle contexts up to a configurable token limit, enabling infinitely long tasks.
*   ✅ **Claude Skills Integration**: Comes with 15 professional skills for documents, design, testing, and development.
*   ✅ **MCP Tool Integration**: Natively supports MCP for tools like knowledge graph access and web search.
*   ✅ **Comprehensive Logging**: Detailed logs for every request, response, and tool execution for easy debugging.
*   ✅ **Clean & Simple Design**: A beautiful CLI and a codebase that is easy to understand, making it the perfect starting point for building advanced agents.

## Table of Contents

- [Mini Agent](#mini-agent)
  - [Table of Contents](#table-of-contents)
  - [Quick Start](#quick-start)
    - [1. Get API Key](#1-get-api-key)
    - [2. Choose Your Usage Mode](#2-choose-your-usage-mode)
      - [🚀 Quick Start Mode (Recommended for Beginners)](#-quick-start-mode-recommended-for-beginners)
      - [🔧 Development Mode](#-development-mode)
  - [ACP \& Zed Editor Integration(optional)](#acp--zed-editor-integrationoptional)
  - [Usage Examples](#usage-examples)
    - [Task Execution](#task-execution)
    - [Using a Claude Skill (e.g., PDF Generation)](#using-a-claude-skill-eg-pdf-generation)
    - [Web Search \& Summarization (MCP Tool)](#web-search--summarization-mcp-tool)
  - [Testing](#testing)
    - [Quick Run](#quick-run)
    - [Test Coverage](#test-coverage)
  - [Troubleshooting](#troubleshooting)
    - [SSL Certificate Error](#ssl-certificate-error)
    - [Module Not Found Error](#module-not-found-error)
  - [Related Documentation](#related-documentation)
  - [Contributing](#contributing)
  - [License](#license)
  - [References](#references)

## Quick Start

### 1. Get API Key

MiniMax provides both global and China platforms. Choose based on your network environment:

| Version    | Platform                                                       | API Base                   |
| ---------- | -------------------------------------------------------------- | -------------------------- |
| **Global** | [https://platform.minimax.io](https://platform.minimax.io)     | `https://api.minimax.io`   |
| **China**  | [https://platform.minimaxi.com](https://platform.minimaxi.com) | `https://api.minimaxi.com` |

**Steps to get API Key:**
1. Visit the corresponding platform to register and login
2. Go to **Account Management > API Keys**
3. Click **"Create New Key"**
4. Copy and save it securely (key is only shown once)

> 💡 **Tip**: Remember the API Base address corresponding to your chosen platform, you'll need it for configuration

### 2. Choose Your Usage Mode

**Prerequisites: Install uv**

Both usage modes require uv. If you don't have it installed:

```bash
# macOS/Linux/WSL
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
python -m pip install --user pipx
python -m pipx ensurepath
# Restart PowerShell after installation

# After installation, restart your terminal or run:
source ~/.bashrc  # or ~/.zshrc (macOS/Linux)
```

We offer two usage modes - choose based on your needs:

#### 🚀 Quick Start Mode (Recommended for Beginners)

Perfect for users who want to quickly try Mini Agent without cloning the repository or modifying code.

**Installation:**

```bash
# 1. Install directly from GitHub
uv tool install git+https://github.com/MiniMax-AI/Mini-Agent.git

# 2. Run setup script (automatically creates config files)
# macOS/Linux:
curl -fsSL https://raw.githubusercontent.com/MiniMax-AI/Mini-Agent/main/scripts/setup-config.sh | bash

# Windows (PowerShell):
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/MiniMax-AI/Mini-Agent/main/scripts/setup-config.ps1" -OutFile "$env:TEMP\setup-config.ps1"
powershell -ExecutionPolicy Bypass -File "$env:TEMP\setup-config.ps1"
```

> 💡 **Tip**: If you want to develop locally or modify code, use "Development Mode" below

**Configuration:**

The setup script creates config files in `~/.mini-agent/config/`. Edit the config file:

```bash
# Edit config file
nano ~/.mini-agent/config/config.yaml
```

Fill in your API Key and corresponding API Base:

```yaml
api_key: "YOUR_API_KEY_HERE"          # API Key from step 1
api_base: "https://api.minimax.io"  # Global
