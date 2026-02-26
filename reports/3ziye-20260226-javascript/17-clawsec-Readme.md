<h1 align="center">
  <img src="./img/prompt-icon.svg" alt="prompt-icon" width="40">
  ClawSec: Security Skill Suite for AI Agents
  <img src="./img/prompt-icon.svg" alt="prompt-icon" width="40">
</h1>

<div align="center">

## Secure Your OpenClaw Bots with a Complete Security Skill Suite

<h4>Brought to you by <a href="https://prompt.security">Prompt Security</a>, the Platform for AI Security</h4>

</div>

<div align="center">

![Prompt Security Logo](./img/Black+Color.png)
<img src="./public/img/mascot.png" alt="clawsec mascot" width="200" />

</div>
<div align="center">

🌐 **Live at: [https://clawsec.prompt.security](https://clawsec.prompt.security) [https://prompt.security/clawsec](https://prompt.security/clawsec)**

[![CI](https://github.com/prompt-security/clawsec/actions/workflows/ci.yml/badge.svg)](https://github.com/prompt-security/clawsec/actions/workflows/ci.yml)
[![Deploy Pages](https://github.com/prompt-security/clawsec/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/prompt-security/clawsec/actions/workflows/deploy-pages.yml)
[![Poll NVD CVEs](https://github.com/prompt-security/clawsec/actions/workflows/poll-nvd-cves.yml/badge.svg)](https://github.com/prompt-security/clawsec/actions/workflows/poll-nvd-cves.yml)


</div>

---

## 🦞 What is ClawSec?

ClawSec is a **complete security skill suite for AI agent platforms**. It provides unified security monitoring, integrity verification, and threat intelligence-protecting your agent's cognitive architecture against prompt injection, drift, and malicious instructions.

### Supported Platforms

- **OpenClaw** (Moltbot, Clawdbot, and clones) - Full suite with skill installer, file integrity protection, and security audits
- **NanoClaw** - Containerized WhatsApp bot security with MCP tools for advisory monitoring, signature verification, and file integrity

### Core Capabilities

- **📦 Suite Installer** - One-command installation of all security skills with integrity verification
- **🛡️ File Integrity Protection** - Drift detection and auto-restore for critical agent files (SOUL.md, IDENTITY.md, etc.)
- **📡 Live Security Advisories** - Automated NVD CVE polling and community threat intelligence
- **🔍 Security Audits** - Self-check scripts to detect prompt injection markers and vulnerabilities
- **🔐 Checksum Verification** - SHA256 checksums for all skill artifacts
- **Health Checks** - Automated updates and integrity verification for all installed skills

---

## 🎬 Product Demos

GitHub strips inline `<video>` tags in repository READMEs. The previews below are lightweight animated GIFs (no audio). Click any preview to open the full MP4 with audio.

### Install Demo (`clawsec-suite`)

[![Install demo animated preview](public/video/install-demo-preview.gif)](public/video/install-demo.mp4)

Direct link: [install-demo.mp4](public/video/install-demo.mp4)

### Drift Detection Demo (`soul-guardian`)

[![Drift detection animated preview](public/video/soul-guardian-demo-preview.gif)](public/video/soul-guardian-demo.mp4)

Direct link: [soul-guardian-demo.mp4](public/video/soul-guardian-demo.mp4)

---

## 🚀 Quick Start

### For AI Agents

```bash
# Fetch and install the ClawSec security suite
curl -sL https://clawsec.prompt.security/releases/latest/download/SKILL.md
```

The skill file contains deployment instructions. Your agent will:
1. Detect its agent family (OpenClaw/MoltBot/ClawdBot or other)
2. Install appropriate skills from the catalog
3. Verify integrity using checksums
4. Set up cron update checks

### For Humans

Copy this instruction to your AI agent:

> Read https://clawsec.prompt.security/releases/latest/download/SKILL.md and follow the instructions to install the protection skill suite.

### Shell and OS Notes

ClawSec scripts are split between:
- Cross-platform Node/Python tooling (`npm run build`, hook/setup `.mjs`, `utils/*.py`)
- POSIX shell workflows (`*.sh`, most manual install snippets)

For Linux/macOS (`bash`/`zsh`):
- Use unquoted or double-quoted home vars: `export INSTALL_ROOT="$HOME/.openclaw/skills"`
- Do **not** single-quote expandable vars (for example, avoid `'$HOME/.openclaw/skills'`)

For Windows (PowerShell):
- Prefer explicit path building:
  - `$env:INSTALL_ROOT = Join-Path $HOME ".openclaw\\skills"`
  - `node "$env:INSTALL_ROOT\\clawsec-suite\\scripts\\setup_advisory_hook.mjs"`
- POSIX `.sh` scripts require WSL or Git Bash.

Troubleshooting: if you see directories such as `~/.openclaw/workspace/$HOME/...`, a home variable was passed literally. Re-run using an absolute path or an unquoted home expression.

---

## 📱 NanoClaw Platform Support

ClawSec now supports **NanoClaw**, a containerized WhatsApp bot powered by Claude agents.

### clawsec-nanoclaw Skill

**Location**: `skills/clawsec-nanoclaw/`

A complete security suite adapted for NanoClaw's containerized architecture:

- **9 MCP Tools** for agents to check vulnerabilities
  - Advisory checking and browsing
  - Pre-installation safety checks
  - Skill 