<p align="center">
  <h1 align="center">Secure OpenClaw</h1>
</p>

<p align="center">
  <a href="https://platform.composio.dev?utm_source=github&utm_medium=gif&utm_campaign=2101&utm_content=secure-openclaw">
    <img src="assets/secure-openclaw.gif" alt="Secure OpenClaw Demo" width="800">
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
  <a href="https://x.com/composio">
    <img src="https://img.shields.io/badge/Follow%20on-X-black?logo=x&logoColor=white" alt="Follow on X">
  </a>
</p>

<p align="center">
  A personal 24x7 AI assistant that runs on your messaging platforms. Send a message on WhatsApp, Telegram, Signal, or iMessage and get responses from Claude with full tool access, persistent memory, scheduled reminders, and integrations with 500+ apps.
  <br><br>
  <a href="https://platform.composio.dev?utm_source=github&utm_medium=description&utm_campaign=2101&utm_content=secure-openclaw">
    <b>Get your free API key to get started →</b>
  </a>
</p>

---

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Deploying Remotely](#deploying-remotely)
- [Providers](#providers)
- [Configuration](#configuration)
- [Messaging Platforms](#messaging-platforms)
- [Tool Approvals](#tool-approvals)
- [Memory System](#memory-system)
- [Scheduling and Reminders](#scheduling-and-reminders)
- [App Integrations](#app-integrations)
- [Commands](#commands)
- [Troubleshooting](#troubleshooting)
- [Directory Structure](#directory-structure)
- [Contributing](#contributing)
- [Resources](#resources)
- [Community](#community)

---

## Requirements

- Node.js 18+
- macOS, Linux, or Windows
- Anthropic API key (`ANTHROPIC_API_KEY`)
- Composio API key (`COMPOSIO_API_KEY`)
- **Claude Code** — required if using the Claude provider
- **Opencode** — required if using the Opencode provider

Platform-specific:
- WhatsApp: a phone with WhatsApp installed
- Telegram: a bot token from @BotFather
- Signal: signal-cli installed and registered
- iMessage: macOS only, requires the `imsg` CLI tool

---

## Installation

### 1. Clone and install dependencies

```bash
git clone <repo-url> secure-openclaw
cd secure-openclaw
npm install
```

### 2. Install a provider

You need at least one AI provider installed on the machine.

**Claude Code** (for the Claude provider):

```bash
npm install -g @anthropic-ai/claude-code
```

**Opencode** (for the Opencode provider):

```bash
curl -fsSL https://opencode.ai/install | bash
```

You can install both. The CLI lets you switch between them.

After installing Claude Code, authenticate it locally:

```bash
claude
# Follow the OAuth prompts to log in with your Anthropic account
```

On remote/Docker deployments, authentication is handled by the `ANTHROPIC_API_KEY` environment variable instead — no interactive login needed.

### 3. API keys

**Anthropic** — get your key from https://console.anthropic.com/

```bash
export ANTHROPIC_API_KEY=sk-ant-...
```

**Composio** — provides 500+ app integrations (Gmail, Slack, GitHub, etc.)

```bash
curl -fsSL https://composio.dev/install | bash
composio login
composio whoami   # shows your API key
export COMPOSIO_API_KEY=your-key
```

Add all exports to your shell profile (`~/.zshrc` or `~/.bashrc`) to make them permanent.

---

## Quick Start

```bash
node cli.js
```

This opens the interactive menu:

```
1) Terminal chat      — talk to the assistant in your terminal
2) Start gateway      — run the messaging gateway
3) Setup adapters     — configure WhatsApp, Telegram, etc.
4) Show current config
5) Test connection
6) Change provider
7) Exit
```

Or run directly:

```bash
node cli.js chat     # terminal chat
node cli.js start    # start the gateway
```

---

## Deploying Remotely

The gateway can run on a remote server. Terminal chat is local only.

### DigitalOcean (Recommended)

A $6/month DigitalOcean droplet. No ID verification, just sign up and go.

#### 1. Create a droplet

1. Sign up at [digitalocean.com](https://www.digitalocean.com/)
2. **Create** > **Droplets**
3. Pick a region, select **Ubuntu 24.04**, choose the **$6/mo** plan (1 GB RAM)
4. Set a **root password**
5. Click **Create Droplet** and copy the **public IP** from the dashboard

#### 2. Set up the server

```bash
# SSH in
ssh root@YOUR_DROPLET_IP

# Add swap (the build needs more than 1 GB)
fallocate -l 2G /swapfile && chmod 600 /swapfile && mkswap /swapfile && swapon /swapfile
echo '/swapfile none swap sw 0 0' >> /etc/fstab

# Install Docker
curl -fsSL https://get.docker.com