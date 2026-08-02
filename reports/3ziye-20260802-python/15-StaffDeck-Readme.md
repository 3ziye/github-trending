<div align="center">

<img src="packaging/assets/staffdeck_banner_en.png" alt="StaffDeck logo" />

<p align="center">
  <a href="https://staffdeck.openbmb.cn/"><img src="https://img.shields.io/badge/Website-staffdeck.openbmb.cn-FF6B35?style=flat-square&logo=googlechrome&logoColor=white" alt="Official Website"/></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-AGPL_3.0-blue.svg?style=flat-square" alt="License"/></a>
  <a href="https://github.com/OpenBMB/StaffDeck/stargazers"><img src="https://img.shields.io/github/stars/OpenBMB/StaffDeck?style=flat-square" alt="Stars"/></a>
  <br/>
  <a href="#-Community"><img src="https://img.shields.io/badge/Discord-Join_Community-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord"/></a>
  &nbsp;
  <a href="#-Community"><img src="https://img.shields.io/badge/Feishu-Community-00D6B9?style=for-the-badge&logo=bytedance&logoColor=white" alt="Feishu"/></a>
  &nbsp;
  <a href="#-Community"><img src="https://img.shields.io/badge/WeChat-Community-07C160?style=for-the-badge&logo=wechat&logoColor=white" alt="WeChat"/></a>
  <br/>
</p>

**English** | [简体中文](./README.zh.md)
</div>

## News

- 📌 **Pinned · 2026-07-15**: StaffDeck is now open source! We welcome your feedback and support with a Star.

# 💡 About StaffDeck

StaffDeck is an enterprise platform for building and managing digital employees. It helps professionals turn their work experience, business processes, and decision criteria into digital employees that can operate continuously, take over repetitive tasks, and preserve individual expertise as reusable, evolvable, and traceable organizational assets. StaffDeck is jointly developed by the [ModelBest](https://modelbest.cn/), [NEU-ModelBest Data Intelligence Joint Lab](https://neuir.github.io/), [THUNLP](https://nlp.csai.tsinghua.edu.cn/), [OpenBMB](https://www.openbmb.cn/home), and [AI9Stars](https://github.com/AI9Stars) for enterprises and institutions seeking to advance AI from a personal productivity tool to an organizational capability.

## Core Features

- 🧑‍💼 **Build and manage digital employees**: Turn professional experience, processes, and decision criteria into digital employees with positions, employee IDs, capability profiles, and work records. Support capability growth, permission isolation, publishing, and reuse.
- 🧩 **State-machine-driven procedural skills**: Generate structured SOPs from natural language and use state machines to execute complex processes accurately. Support real-time switching across multiple flows, context preservation, visual editing, version management, and branch evolution.
- 📚 **Document-structure-aware knowledge retrieval**: Build navigable indexes across documents, chapters, pages, summaries, and other levels, allowing digital employees to first estimate where information may reside and then locate the original text step by step. Support knowledge buckets, targeted retrieval, source citations, and retrieval debugging.
- 🔌 **Autonomous execution and continuous improvement**: Perform real business operations through HTTP APIs, MCP, and scheduled tasks, then close the improvement loop with long-term memory, complete traces, human takeover, user feedback, and feedback analysis.

## Desktop Downloads

Visit the [StaffDeck official website](https://staffdeck.openbmb.cn/) or download the latest desktop release directly:

| Platform | Architecture | Download |
| --- | --- | --- |
| macOS | Apple Silicon (arm64) | [Download `.dmg`](https://github.com/OpenBMB/StaffDeck/releases/latest/download/StaffDeck-macos-arm64.dmg) |
| Windows | x64 | [Download installer `.exe`](https://github.com/OpenBMB/StaffDeck/releases/latest/download/StaffDeck-windows-x64-setup.exe) |
| Linux | x86_64 (Debian/Ubuntu) | [Download `.deb`](https://github.com/OpenBMB/StaffDeck/releases/latest/download/StaffDeck-linux-x86_64.deb) |

## Agent-Friendly Quick Deploy

Paste the prompt below into Cursor, Claude Code, or Codex:

```text
Read https://raw.githubusercontent.com/OpenBMB/StaffDeck/main/README.md.
Clone the OpenBMB/StaffDeck repository, prepare Python 3.11 or newer and Node.js 20,
create backend/.venv, install the backend and frontend dependencies, copy
backend/.env.example to backend/.env, ask me for the OpenAI-compatible model
endpoint and API key if they are missing, and use the commands documented for
the current OS. Start with scripts/dev_up.sh --detach on macOS/Linux/WSL or
.\scripts\dev_up.ps1 --detach on Windows PowerShell, then verify /api/health
plus /workspace/gallery before reporting success.
```


## Table of Contents

- [💡 About StaffDeck](#-about-staffdeck)
  - [Core Features](#core-features)
  - [Desktop Downloads](#desktop-downloads)
  - [Agent-Friendly Quick Deploy](#agent-friendly-quick-deploy)
  - [Table of Contents](#table-of-contents)
  - [Quick Start](#quick-start)
    - [Requirements](#requirements)
    - [1. Clone and Install](#1-clone-and-install)
    - [2. Configure a Model](#2-configure-a-model)
  