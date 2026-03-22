<p align="center">
  <img src="assets/banner.png" alt="Anthropic Cybersecurity Skills — 753 skills for AI agents" width="100%" />
</p>

<p align="center">
  <a href="https://opensource.org/licenses/Apache-2.0"><img src="https://img.shields.io/badge/License-Apache_2.0-blue.svg?style=for-the-badge" alt="License: Apache 2.0" /></a>
  <a href="https://github.com/mukul975/Anthropic-Cybersecurity-Skills/stargazers"><img src="https://img.shields.io/github/stars/mukul975/Anthropic-Cybersecurity-Skills?style=for-the-badge&logo=github" alt="GitHub Stars" /></a>
  <a href="https://github.com/mukul975/Anthropic-Cybersecurity-Skills/network/members"><img src="https://img.shields.io/github/forks/mukul975/Anthropic-Cybersecurity-Skills?style=for-the-badge&logo=github" alt="GitHub Forks" /></a>
  <a href="https://github.com/mukul975/Anthropic-Cybersecurity-Skills/commits"><img src="https://img.shields.io/github/last-commit/mukul975/Anthropic-Cybersecurity-Skills?style=for-the-badge&logo=github" alt="Last Commit" /></a>
  <a href="https://github.com/mukul975/Anthropic-Cybersecurity-Skills"><img src="https://img.shields.io/badge/Skills-753-blueviolet?style=for-the-badge&logo=bookstack&logoColor=white" alt="753 Skills" /></a>
  <a href="https://attack.mitre.org/"><img src="https://img.shields.io/badge/MITRE_ATT%26CK-Mapped-red?style=for-the-badge&logo=shield&logoColor=white" alt="MITRE ATT&CK Mapped" /></a>
  <a href="https://github.com/mukul975/Anthropic-Cybersecurity-Skills/graphs/contributors"><img src="https://img.shields.io/github/contributors/mukul975/Anthropic-Cybersecurity-Skills?style=for-the-badge&logo=github" alt="Contributors" /></a>
</p>

<p align="center">
  <b>The largest open-source collection of cybersecurity skills for AI agents.<br/>753 structured skills · MITRE ATT&CK mapped · NIST CSF 2.0 aligned · <a href="https://agentskills.io">agentskills.io</a> open standard</b>
</p>

<p align="center">
  <a href="https://mahipal.engineer/Anthropic-Cybersecurity-Skills/">🌐 Landing Page</a> · <a href="https://github.com/mukul975/Anthropic-Cybersecurity-Skills/releases/tag/v1.0.0">📦 v1.0.0 Release</a> · <a href="https://github.com/mukul975/Anthropic-Cybersecurity-Skills/issues">🐛 Report Bug</a> · <a href="https://github.com/mukul975/Anthropic-Cybersecurity-Skills/issues">💡 Request Feature</a>
</p>

---

Anthropic Cybersecurity Skills gives every AI agent — from Claude Code to GitHub Copilot to your custom LangChain pipeline — instant access to **753 production-grade cybersecurity skills** spanning 26 security domains. Each skill follows the [agentskills.io](https://agentskills.io) open standard: a YAML frontmatter header for lightning-fast discovery, a structured Markdown body for step-by-step execution, and reference files for deep technical context. The entire collection is mapped to **MITRE ATT&CK** (all 14 Enterprise tactics, 200+ techniques) and aligned to **NIST CSF 2.0** — giving AI agents the same structured knowledge that senior security practitioners carry in their heads. Install in one command and your agent immediately knows how to perform memory forensics, hunt for C2 beaconing, audit Kubernetes RBAC, reverse .NET malware, and hundreds more tasks.

## 📑 Table of contents

- [🚀 Quick start](#-quick-start--install-cybersecurity-skills-for-ai-agents)
- [🛡️ What's inside](#️-whats-inside--753-cybersecurity-skills-across-38-domains)
- [🤖 Compatible platforms](#-compatible-ai-agent-platforms)
- [📐 Skill structure](#-skill-structure-and-agentskillsio-format)
- [🗺️ MITRE ATT&CK coverage](#️-mitre-attck-and-nist-csf-20-coverage)
- [🧠 How AI agents use these skills](#-how-ai-agents-use-these-cybersecurity-skills)
- [📝 Example skills](#-example-cybersecurity-skills)
- [👥 Contributors](#-contributors)
- [🤝 Contributing](#-contributing-to-cybersecurity-ai-skills)
- [⭐ Star history](#-star-history)
- [🌐 Community](#-community)
- [📄 License](#-license)

---

## 🚀 Quick start — install cybersecurity skills for AI agents

Get up and running in under 30 seconds. Choose your preferred method:

### Option 1 · npx (recommended)

```bash
npx skills add mukul975/Anthropic-Cybersecurity-Skills
```

### Option 2 · Claude Code plugin marketplace

```
/plugin marketplace add mukul975/Anthropic-Cybersecurity-Skills
```

### Option 3 · Manual clone

```bash
git clone https://github.com/mukul975/Anthropic-Cybersecurity-Skills.git
cd Anthropic-Cybersecurity-Skills
```

> **That's it.** Your AI agent can now discover and execute 753 cybersecurity skills on demand. No configuration, no API keys, no setup scripts.

---

## 🛡️ What's inside — 753 cybersecurity skills across 38 domains

Every skill is a self-contained directory with structured workflows, reference materials, helper scripts, and validation steps. Here are the top 16 domains:

| Domain | Skills | Example capabilities |
|:-------|:------:|:---------------------|
| ☁️ **Cloud Security** | **48** | AWS S3 bucket audit, Azure AD config review, GCP IAM assessment |
| 🌐 **Web Applic