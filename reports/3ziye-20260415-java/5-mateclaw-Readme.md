<div align="center">

<p align="center">
  <img src="mateclaw-ui/public/logo/mateclaw_logo_s.png" alt="MateClaw Logo" width="120">
</p>

# MateClaw

<p align="center"><b>Build AI that thinks, acts, remembers, and ships.</b></p>

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repo-black.svg?logo=github)](https://github.com/matevip/mateclaw)
[![Documentation](https://img.shields.io/badge/Docs-Website-green.svg?logo=readthedocs&label=Docs)](https://claw.mate.vip/docs)
[![Live Demo](https://img.shields.io/badge/Demo-Online-orange.svg?logo=vercel&label=Demo)](https://claw-demo.mate.vip)
[![Website](https://img.shields.io/badge/Website-claw.mate.vip-blue.svg?logo=googlechrome&label=Site)](https://claw.mate.vip)
[![Java Version](https://img.shields.io/badge/Java-17+-blue.svg?logo=openjdk&label=Java)](https://adoptium.net/)
[![Spring Boot](https://img.shields.io/badge/Spring%20Boot-3.5-brightgreen.svg?logo=springboot)](https://spring.io/projects/spring-boot)
[![Vue](https://img.shields.io/badge/Vue-3-4FC08D.svg?logo=vuedotjs)](https://vuejs.org/)
[![Last Commit](https://img.shields.io/github/last-commit/matevip/mateclaw)](https://github.com/matevip/mateclaw)
[![License](https://img.shields.io/badge/license-Apache--2.0-red.svg?logo=opensourceinitiative&label=License)](LICENSE)

[[Website](https://claw.mate.vip)] [[Live Demo](https://claw-demo.mate.vip)] [[Documentation](https://claw.mate.vip/docs)] [[中文](README_zh.md)]

</div>

<p align="center">
  <img src="assets/images/preview.png" alt="MateClaw Preview" width="800">
</p>

---

An AI agent. A knowledge engine. A memory system. A tool runtime. A multi-channel presence.

**One product. The whole widget.**

MateClaw is a personal AI operating system built with **Java + Vue 3**, powered by [Spring AI Alibaba](https://github.com/alibaba/spring-ai-alibaba). It's not a chatbox, not a workflow builder, not just another coding assistant. It's the entire system — from reasoning to remembering to shipping — in one deployment.

Three things make it insanely different:

1. **Agents do work, not just talk** — ReAct + Plan-and-Execute. Not one-shot answers — iterative reasoning that actually completes tasks
2. **Knowledge is shaped, not just stored** — An LLM Wiki that digests raw material into structured, linked pages. The difference between a warehouse and a library
3. **End-to-end, no compromises** — Web console, desktop app, 7 IM channels, tool guardrails, enterprise auth. One team, one deployment, one experience

---

## Why MateClaw

Most AI tools do one thing well. MateClaw does the whole thing.

| Capability | MateClaw | [OpenClaw](https://github.com/openclaw/openclaw) | [CoPaw](https://github.com/agentscope-ai/CoPaw) | [QClaw](https://cntechpost.com/2026/03/20/tencent-opens-qclaw-public-testing-amid-fierce-ai-rivalry/) | [Claude Code](https://github.com/anthropics/claude-code) | [Cursor](https://cursor.com) | [Windsurf](https://windsurf.com) |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Agent Orchestration | **ReAct + Plan-Execute** | Multi-agent teams | Multi-agent collab | Specialist agents | Agent Teams + subagents | Background Agents (cloud VM) | Cascade engine |
| Knowledge System | **LLM Wiki (digestion)** | Intelligence Mode + Wiki | Personal KB | Knowledge graph | CLAUDE.md (no RAG) | Codebase indexing | No |
| Memory | **Extract + Consolidate + Dream** | SQLite + Dreaming + Wiki | ReMe (hybrid retrieval) | 3-layer memory | 3-layer (CLAUDE.md + auto + files) | No persistent memory | Memories (~48h learning) |
| Tool Guard & Approval | **RBAC + approval flow** | HITL + risk levels | No | No | Permissions + Sandbox + Hooks | No | Turbo Mode (auto-approve) |
| Multi-Channel IM | **7 channels** | 25+ channels | 7 channels | 5 channels | 3 channels (preview) | IDE only | IDE only |
| Web Management UI | **Full admin dashboard** | Control UI | Console UI | Dashboard | Enterprise dashboard | No | No |
| Desktop App | **Electron + bundled JRE** | macOS menu bar | Electron (Beta) | Win/Mac app | Claude Desktop (Mac/Win) | VS Code fork | VS Code fork |
| Multimodal Creation | **TTS/STT/Img/Music/Video** | TTS/Video/Music/Image | Vision input | No | Vision input only | No | No |
| Skill Ecosystem | **ClawHub marketplace** | ClawHub registry | Python skills | Templates | 340+ plugins, 1300+ skills | MCP marketplace | MCP one-click |
| Enterprise Auth | **RBAC + JWT** | Basic (password) | Basic auth | No | SSO/SCIM/RBAC | SSO + Teams | Teams plan |
| Open Source | **Apache 2.0** | MIT | Apache 2.0 | Partial | No (source-available) | No | No |
| Pricing | **Free** | Free | Free | Free (beta) | $20–200/mo | $0–200/mo | $0–200/mo |
| Tech Stack | **Java + Vue 3** | TypeScript | Python + TS | OpenClaw fork | TypeScript | Electron (VS Code) | Electron (VS Code) |

**What makes MateClaw different?**

Every product in this table is genuinely strong. Here's where MateClaw carves its own space:

- **Plan-and-Execute orchestration** — Break complex work into ordered steps