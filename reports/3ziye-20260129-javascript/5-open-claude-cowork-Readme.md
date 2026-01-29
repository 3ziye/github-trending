<p align="center">
  <h1 align="center">Open Claude Cowork</h1>
</p>

<p align="center">
  <a href="https://platform.composio.dev/?utm_source=github&utm_medium=banner&utm_campaign=2101&utm_content=open-claude-cowork">
    <img src="assets/open%20claude%20cowork%20wide%20new.png" alt="Open Claude Cowork Banner" width="800">
  </a>
</p>

<p align="center">
  <a href="https://platform.composio.dev?utm_source=github&utm_medium=gif&utm_campaign=2101&utm_content=open-claude-cowork">
    <img src="open-claude-cowork.gif" alt="Open Claude Cowork Demo" width="800">
  </a>
</p>

<p align="center">
  <a href="https://docs.composio.dev/tool-router/overview">
    <img src="https://img.shields.io/badge/Composio-Tool%20Router-orange" alt="Composio">
  </a>
  <a href="https://platform.claude.com/docs/en/agent-sdk/overview">
    <img src="https://img.shields.io/badge/Claude-Agent%20SDK-blue" alt="Claude Agent SDK">
  </a>
  <a href="https://github.com/anthropics/claude-code">
    <img src="https://img.shields.io/badge/Powered%20by-Claude%20Code-purple" alt="Claude Code">
  </a>
  <a href="https://twitter.com/composio">
    <img src="https://img.shields.io/twitter/follow/composio?style=social" alt="Twitter">
  </a>
</p>

<p align="center">
  An open-source desktop chat application powered by Claude Agent SDK and Composio Tool Router. Automate your work end-to-end across desktop and all your work apps in one place.
  <br><br>
  <a href="https://platform.composio.dev?utm_source=github&utm_medium=description&utm_campaign=2101&utm_content=open-claude-cowork">
    <b>Get your free API key to get started →</b>
  </a>
</p>

## Features

- **Multi-Provider Support** - Choose between Claude Agent SDK and Opencode for different model options
- **Claude Agent SDK Integration** - Full agentic capabilities with tool use and multi-turn conversations
- **Opencode SDK Support** - Access multiple LLM providers (Claude, GPT-5, Grok, GLM, MiniMax, and more)
- **Composio Tool Router** - Access to 500+ external tools (Gmail, Slack, GitHub, Google Drive, and more)
- **Persistent Chat Sessions** - Conversations maintain context across messages using SDK session management
- **Multi-Chat Support** - Create and switch between multiple chat sessions
- **Real-time Streaming** - Server-Sent Events (SSE) for smooth, token-by-token response streaming
- **Tool Call Visualization** - See tool inputs and outputs in real-time in the sidebar
- **Progress Tracking** - Todo list integration for tracking agent task progress
- **Skills Support** - Extend Claude with specialized capabilities using custom skills
- **Modern UI** - Clean, dark-themed interface inspired by Claude.ai
- **Desktop App** - Native Electron application for macOS, Windows, and Linux

---

## Tech Stack

| Category | Technology |
|----------|------------|
| **Desktop Framework** | Electron.js |
| **Backend** | Node.js + Express |
| **AI Providers** | Claude Agent SDK + Opencode SDK |
| **Tool Integration** | Composio Tool Router + MCP |
| **Streaming** | Server-Sent Events (SSE) |
| **Markdown** | Marked.js |
| **Styling** | Vanilla CSS |

---

## Getting Started

### Quick Setup (Recommended)

```bash
# Clone the repository
git clone https://github.com/ComposioHQ/open-claude-cowork.git
cd open-claude-cowork

# Run the automated setup script
./setup.sh
```

The setup script will:
- Install Composio CLI if not already installed
- Guide you through Composio signup/login
- Configure your API keys in `.env`
- Install all project dependencies

### Manual Setup

If you prefer manual setup, follow these steps:

#### Prerequisites

- Node.js 18+ installed
- **For Claude Provider:**
  - Anthropic API key ([console.anthropic.com](https://console.anthropic.com))
- **For Opencode Provider:**
  - Opencode API key ([opencode.dev](https://opencode.dev))
- Composio API key ([app.composio.dev](https://app.composio.dev))

#### 1. Clone the Repository

```bash
git clone https://github.com/ComposioHQ/open-claude-cowork.git
cd open-claude-cowork
```

#### 2. Install Dependencies

```bash
# Install Electron app dependencies
npm install

# Install backend dependencies
cd server
npm install
cd ..
```

#### 3. Configure Environment

```bash
cp .env.example .env
```

Edit `.env` with your API keys:

```env
# Claude Provider
ANTHROPIC_API_KEY=your-anthropic-api-key

# Opencode Provider (optional)
OPENCODE_API_KEY=your-opencode-api-key
OPENCODE_HOSTNAME=127.0.0.1
OPENCODE_PORT=4096

# Composio Integration
COMPOSIO_API_KEY=your-composio-api-key
```

**Provider Selection:**
- The app allows switching between **Claude** and **Opencode** providers in the UI
- Only configure the API key(s) for the provider(s) you want to use
- Opencode can route to multiple model providers through a single SDK

### Starting the Application

You need **two terminal windows**:

**Terminal 1 - Backend Server:**
```bash
cd server
npm start
```

**Terminal 2 - Electron App:**
```bash
npm start
```

---

## Architecture

```
┌─────────────────────