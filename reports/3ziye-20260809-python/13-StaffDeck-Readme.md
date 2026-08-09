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
| macOS | Intel (x86_64) | [Download `.dmg`](https://github.com/OpenBMB/StaffDeck/releases/latest/download/StaffDeck-macos-x86_64.dmg) |
| Windows | x64 | [Download installer `.exe`](https://github.com/OpenBMB/StaffDeck/releases/latest/download/StaffDeck-windows-x64-setup.exe) |
| Linux | x86_64 (Debian/Ubuntu) | [Download `.deb`](https://github.com/OpenBMB/StaffDeck/releases/latest/download/StaffDeck-linux-x86_64.deb) |

Linux packages listen on `127.0.0.1` by default. Use `staffdeck setup` from a
terminal to choose the listening mode and port, including on a headless host:

```bash
staffdeck setup
staffdeck setup --mode local --port 5173
staffdeck setup --mode lan --port 5173
staffdeck setup --mode public --port 5173 --public-url https://staff.example.com
```

`local` listens only on the machine; `lan` and `public` listen on `0.0.0.0`.
`--port` sets the listening port. In interactive terminals, `public` tries to
infer a public URL first; if it cannot, or when running headless, pass
`--public-url` explicitly. For public deployments, use an HTTPS reverse proxy
and set the same public URL as `OIDC_REDIRECT_URI` when SSO is enabled. The
setup is saved per user and applied on the next launch.

## Agent-Friendly Quick Deploy

Paste the prompt below into Cursor, Claude Code, or Codex. For code-based
deployments, you can also override the launch at runtime with
`ULTRARAG_HOST`, `ULTRARAG_POR