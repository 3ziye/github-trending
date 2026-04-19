<div align="center">

<picture>
    <img src="assets/logo.png" width="320px" style="border: none; box-shadow: none;" alt="OpenSpace Logo">
</picture>

## ✨ OpenSpace: Make Your Agents: Smarter, Low-Cost, Self-Evolving ✨

| 🔋 **46% Fewer Tokens** | **💰 $11K earned in 6 Hours** | 🧬 **Self-Evolving Skills** | 🌐 **Agents Experience Sharing** |

[![Agents](https://img.shields.io/badge/Agents-Claude_Code%20%7C%20Codex%20%7C%20OpenClaw%20%7C%20nanobot%20%7C%20...-99C9BF.svg)](https://modelcontextprotocol.io/)
[![Python](https://img.shields.io/badge/Python-3.12+-FCE7D6.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-C1E5F5.svg)](https://opensource.org/licenses/MIT/)
[![Feishu](https://img.shields.io/badge/Feishu-Group-E9DBFC?style=flat&logo=larksuite&logoColor=white)](./COMMUNICATION.md)
[![WeChat](https://img.shields.io/badge/WeChat-Group-C5EAB4?style=flat&logo=wechat&logoColor=white)](./COMMUNICATION.md)
[![中文文档](https://img.shields.io/badge/文档-中文版-F5C6C6?style=flat)](./README_CN.md)

**One Command to Evolve All Your AI Agents**: OpenClaw, nanobot, Claude Code, Codex, Cursor and etc.

<img src="assets/cli-typing.gif" width="500px" alt="openspace --query your task">

</div>

---

## 📢 News

- **2026-04-16** 📊 **Evolution candidate lifecycle tracking** — skill store now records when evolution suggestions are processed (`evolution_processed_at`), cleanly distinguishing pending candidates from already-handled ones.
- **2026-04-12** 🍎 **macOS platform hardening** — decoupled `atomacos` from core macOS imports so screenshots, window control, and recording work independently without it.
- **2026-04-10** 🎯 **CAPTURED skills** now persist to the host agent's own skill directory instead of the default registry path. Cloud skill uploads now support **private visibility** correctly.
- **2026-04-09** 💬 Multi-channel **communication gateway**. OpenSpace can now receive and respond to messages from external platforms. Ships with **WhatsApp** (Baileys bridge + QR auth) and **Feishu** (HTTP webhook) adapters, session management, attachment caching, and allowlist-based access control. See [`openspace/config/README.md`](openspace/config/README.md) for setup.
- **2026-04-07** 🌐 OpenSpace MCP now supports standalone **SSE** and **streamable HTTP** startup, making it easier for remote hosts to connect over HTTP instead of stdio and bypass stdio-bound MCP server timeout bottlenecks. See the [host integration guide](openspace/host_skills/README.md) for setup details.
- **2026-04-06** 🛠️ Fixed multiple runtime issues across grounding, MCP serving, skill evolution, and persistence, improving execution stability and recovery in long-running workflows.
- **2026-04-05** 🧭 Cleaned up LLM credential resolution: centralized `.env` loading, improved host config auto-detection, and made provider-native env handling more consistent.
- **2026-04-03** 🚀 Released **v0.1.0** — Skill quality monitoring: structural patterns extracted from high-quality skills now evaluate every new submission daily. Faster, more relevant cloud search. Production-grade vertical skill clusters emerging organically from the community. Frontend now supports Chinese (zh) i18n.
- **2026-04-02** ⚡ Cloud search upgraded for higher relevance and lower latency.
- **2026-03-31** 🛡️ Security hardening: hardened zip extraction and `import_skill` against path traversal. CLI now respects `OPENSPACE_MODEL` and `OPENSPACE_LLM_*` env vars; MiniMax compatibility; workflow ID collision fixes.
- **2026-03-29** 🔒 Pinned litellm to <1.82.7 to avoid PYSEC-2026-2 supply-chain attack.
- **2026-03-28** 🔧 Idempotent skill registration — `register_skill_dir` now returns existing `SkillMeta` for already-registered skills. Updated OpenClaw setup docs.
- **2026-03-27** 🪟 Fixed stdio deadlock on Windows; improved evolver confirmation parsing with stem-style keyword matching.
- **2026-03-26** 🌱 Dynamic skill directory re-scanning on each call, lightweight local skill search, and streamlined documentation.
- **2026-03-25** 🎉 OpenSpace is now open source!

---

## The Problem with Today's AI Agents

Today's AI agents — [OpenClaw](https://github.com/openclaw/openclaw), [nanobot](https://github.com/HKUDS/nanobot), [Claude Code](https://docs.anthropic.com/en/docs/claude-code), [Codex](https://github.com/openai/codex), [Cursor](https://cursor.com), etc. — are powerful, but they have a critical weakness: they never **Learn**, **Adapt**, and **Evolve** from real-world experience — let alone **Share** with each other.
- **❌ Massive Token Waste** - How to reuse successful task patterns instead of reasoning from scratch and burning tokens every time?
- **❌ Repeated Costly Failures** - How to share solutions across agents instead of repeating the same costly exploration and mistakes?
- **❌ Poor and Unreliable Skills** - How to maintain skill reliability as tools and APIs evolve — while ensuring community-contributed skills meet rigorous quality standards?

## 🎯 What is OpenSpace?
