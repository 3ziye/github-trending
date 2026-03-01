<p align="center">
  <img src="docs/assets/logo.png" alt="OpenAkita Logo" width="200" />
</p>

<h1 align="center">OpenAkita</h1>

<p align="center">
  <strong>Self-Evolving AI Agent — Learns Autonomously, Never Gives Up</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square" alt="License" height="20" />
  <img src="https://img.shields.io/badge/python-3.11+-blue.svg?style=flat-square" alt="Python Version" height="20" />
  <img src="https://img.shields.io/github/v/release/openakita/openakita?color=green&style=flat-square" alt="Version" height="20" />
  <img src="https://img.shields.io/pypi/v/openakita?color=green&style=flat-square" alt="PyPI" height="20" />
  <img src="https://img.shields.io/github/actions/workflow/status/openakita/openakita/ci.yml?branch=main&style=flat-square" alt="Build Status" height="20" />
</p>

<p align="center">
  <a href="#desktop-terminal">Desktop Terminal</a> •
  <a href="#features">Features</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="#architecture">Architecture</a> •
  <a href="#documentation">Documentation</a>
</p>

<p align="center">
  <strong>English</strong> | <a href="README_CN.md">中文</a>
</p>

---

## What is OpenAkita?

**An AI Agent that keeps getting smarter while you sleep.**

Most AI assistants forget you the moment the chat ends. OpenAkita teaches itself new skills, fixes its own bugs, and remembers everything you've told it — like the Akita dog it's named after: **loyal, reliable, never quits**.

Set up in 3 minutes with just an API key. 8 personas, 6 IM platforms, and yes — it sends memes.

---

## Desktop Terminal

<p align="center">
  <img src="docs/assets/desktop_terminal_en.png" alt="OpenAkita Desktop Terminal" width="800" />
</p>

OpenAkita provides a cross-platform **Desktop Terminal** (built with Tauri + React) — an all-in-one AI assistant with chat, configuration, monitoring, and skill management:

- **AI Chat Assistant** — Streaming output, Markdown rendering, multimodal input, Thinking display, Plan mode
- **Bilingual (CN/EN)** — Auto-detects system language, one-click switch, fully internationalized
- **Localization & i18n** — First-class support for Chinese and international ecosystems, PyPI mirrors, IM channels
- **LLM Endpoint Manager** — Multi-provider, multi-endpoint, auto-failover, online model list fetching
- **IM Channel Setup** — Telegram, Feishu, WeCom, DingTalk, QQ Official Bot, OneBot — all in one place
- **Persona & Living Presence** — 8 role presets, proactive greetings, memory recall, learns your preferences
- **Skill Marketplace** — Browse, download, configure skills in one place
- **Status Monitor** — Compact dashboard: service/LLM/IM health at a glance
- **System Tray** — Background residency + auto-start on boot, one-click start/stop

> **Download**: [GitHub Releases](https://github.com/openakita/openakita/releases)
>
> Available for Windows (.exe) / macOS (.dmg) / Linux (.deb / .AppImage)

### 3-Minute Quick Setup — Zero to Chatting

No command line. No config files. **From install to conversation in 3 minutes**:

<p align="center">
  <img src="docs/assets/desktop_quick_config.gif" alt="OpenAkita Quick Setup vs Full Setup" width="800" />
</p>

<table>
<tr>
<td width="50%">

**Quick Setup (Recommended for new users)**

```
① Fill in  → Add LLM endpoint + IM (optional)
② One-click → Auto-create env, install deps, write config
③ Done      → Launch service, start chatting
```

Just one API Key, everything else is automatic:
- Auto-create workspace
- Auto-download & install Python 3.11
- Auto-create venv + pip install
- Auto-write 40+ recommended defaults
- Auto-save IM channel settings

</td>
<td width="50%">

**Full Setup (Power users)**

```
Workspace → Python → Install → LLM Endpoints
→ IM Channels → Tools & Skills → Agent System → Finish
```

8-step guided wizard with full control:
- Custom workspaces (multi-env isolation)
- Choose Python version & install source
- Configure desktop automation, MCP tools
- Tune persona, living presence parameters
- Logging, memory, scheduler & more

</td>
</tr>
</table>

> Switch between modes anytime — click "Switch Setup Mode" in the sidebar to return to the selection page without losing existing configuration.
>
> See [Configuration Guide](docs/configuration-guide.md) for full details.

---

## Features

| | Feature | In One Line |
|:---:|---------|-------------|
| **1** | **Self-Learning & Evolution** | Daily self-check, memory consolidation, task retrospection, auto skill generation — it gets smarter while you sleep |
| **2** | **8 Personas + Living Presence** | Girlfriend / Butler / Jarvis… not just role-play — proactive greetings, remembers your birthday, auto-mutes at night |
| **3** | **3-Min Quick Setup** | Desktop app, one-click start — just drop in an API Key, Python/env/deps/config all automatic |
| **4** | **Plan Mode** | Complex tasks auto-decomposed into multi-step plans, real-time tracking, Plan → Act → Verify lo