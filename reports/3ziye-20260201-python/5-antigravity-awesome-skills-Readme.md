# 🌌 Antigravity Awesome Skills: 625+ Agentic Skills for Claude Code, Gemini CLI, Cursor, Copilot & More

> **The Ultimate Collection of 625+ Universal Agentic Skills for AI Coding Assistants — Claude Code, Gemini CLI, Codex CLI, Antigravity IDE, GitHub Copilot, Cursor, OpenCode**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Anthropic-purple)](https://claude.ai)
[![Gemini CLI](https://img.shields.io/badge/Gemini%20CLI-Google-blue)](https://github.com/google-gemini/gemini-cli)
[![Codex CLI](https://img.shields.io/badge/Codex%20CLI-OpenAI-green)](https://github.com/openai/codex)
[![Cursor](https://img.shields.io/badge/Cursor-AI%20IDE-orange)](https://cursor.sh)
[![Copilot](https://img.shields.io/badge/GitHub%20Copilot-VSCode-lightblue)](https://github.com/features/copilot)
[![OpenCode](https://img.shields.io/badge/OpenCode-CLI-gray)](https://github.com/opencode-ai/opencode)
[![Antigravity](https://img.shields.io/badge/Antigravity-DeepMind-red)](https://github.com/sickn33/antigravity-awesome-skills)

**Antigravity Awesome Skills** is a curated, battle-tested library of **624 high-performance agentic skills** designed to work seamlessly across all major AI coding assistants:

- 🟣 **Claude Code** (Anthropic CLI)
- 🔵 **Gemini CLI** (Google DeepMind)
- 🟢 **Codex CLI** (OpenAI)
- 🔴 **Antigravity IDE** (Google DeepMind)
- 🩵 **GitHub Copilot** (VSCode Extension)
- 🟠 **Cursor** (AI-native IDE)
- ⚪ **OpenCode** (Open-source CLI)

This repository provides essential skills to transform your AI assistant into a **full-stack digital agency**, including official capabilities from **Anthropic**, **OpenAI**, **Google**, **Supabase**, and **Vercel Labs**.

## Table of Contents

- [🚀 New Here? Start Here!](#new-here-start-here)
- [🔌 Compatibility & Invocation](#compatibility--invocation)
- [📦 Features & Categories](#features--categories)
- [🎁 Curated Collections (Bundles)](#curated-collections)
- [📚 Browse 625+ Skills](#browse-625-skills)
- [🛠️ Installation](#installation)
- [🤝 How to Contribute](#how-to-contribute)
- [👥 Contributors & Credits](#credits--sources)
- [⚖️ License](#license)
- [👥 Repo Contributors](#repo-contributors)
- [🌟 Star History](#star-history)

---

## New Here? Start Here!

**Welcome to the V4.0.0 Enterprise Edition.** This isn't just a list of scripts; it's a complete operating system for your AI Agent.

### 1. 🐣 Context: What is this?

**Antigravity Awesome Skills** (Release 4.0.0) is a massive upgrade to your AI's capabilities.

AI Agents (like Claude Code, Cursor, or Gemini) are smart, but they lack **specific tools**. They don't know your company's "Deployment Protocol" or the specific syntax for "AWS CloudFormation".
**Skills** are small markdown files that teach them how to do these specific tasks perfectly, every time.

### 2. ⚡️ Quick Start (The "Bundle" Way)

Install once (clone or npx); then use our **Starter Packs** in [docs/BUNDLES.md](docs/BUNDLES.md) to see which skills fit your role. You get the full repo; Starter Packs are curated lists, not a separate install.

1.  **Install** (pick one):
    ```bash
    # Easiest: npx installer (clones to ~/.agent/skills by default)
    npx antigravity-awesome-skills

    # Or clone manually
    git clone https://github.com/sickn33/antigravity-awesome-skills.git .agent/skills
    ```
2.  **Pick your persona** (See [docs/BUNDLES.md](docs/BUNDLES.md)):
    - **Web Dev?** use the `Web Wizard` pack.
    - **Hacker?** use the `Security Engineer` pack.
    - **Just curious?** start with `Essentials`.

### 3. 🧠 How to use

Once installed, just ask your agent naturally:

> "Use the **@brainstorming** skill to help me plan a SaaS."
> "Run **@lint-and-validate** on this file."

👉 **[Read the Full Getting Started Guide](docs/GETTING_STARTED.md)**

---

## Compatibility & Invocation

These skills follow the universal **SKILL.md** format and work with any AI coding assistant that supports agentic skills.

| Tool            | Type | Invocation Example                | Path              |
| :-------------- | :--- | :-------------------------------- | :---------------- |
| **Claude Code** | CLI  | `>> /skill-name help me...`       | `.claude/skills/` |
| **Gemini CLI**  | CLI  | `(User Prompt) Use skill-name...` | `.gemini/skills/` |
| **Antigravity** | IDE  | `(Agent Mode) Use skill...`       | `.agent/skills/`  |
| **Cursor**      | IDE  | `@skill-name (in Chat)`           | `.cursor/skills/` |
| **Copilot**     | Ext  | `(Paste content manually)`        | N/A               |

> [!TIP]
> **Universal Path**: We recommend cloning to `.agent/skills/`. Most modern tools (Antigravity, recent CLIs) look here by default.

> [!WARNING]
> **Windows Users**: This repository uses **symlinks** for official skills.
> The **npx** installer sets `core.symlinks=true` automatically. For **git clone**, enable Developer Mode or run Git as Administrator:
> `git clone 