<div align="center">

<a href="https://github.com/VoltAgent/voltagent">
<img width="1500" height="500" alt="social" src="https://github.com/user-attachments/assets/a6f310af-8fed-4766-9649-b190575b399d" />
</a>

<br/>
<br/>

<div align="center">
    <strong>Discover 3002 community-built OpenClaw skills, organized by category.
    </strong>
    <br />
    <br />
</div>

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
<a href="https://github.com/VoltAgent/voltagent">
  <img alt="VoltAgent" src="https://cdn.voltagent.dev/website/logo/logo-2-svg.svg" height="20" />
</a> 

[![AI Agent Papers](https://img.shields.io/badge/AI%20Agent-Research%20Papers-b31b1b)](https://github.com/VoltAgent/awesome-ai-agent-papers)
![Skills Count](https://img.shields.io/badge/skills-3002-blue?style=flat-square)
![Last Update](https://img.shields.io/github/last-commit/VoltAgent/awesome-clawdbot-skills?label=Last%20update&style=flat-square)
[![Discord](https://img.shields.io/discord/1361559153780195478.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://s.voltagent.dev/discord)
[![GitHub forks](https://img.shields.io/github/forks/VoltAgent/awesome-clawdbot-skills?style=social)](https://github.com/VoltAgent/awesome-claude-skills/network/members)
</div>

# Awesome OpenClaw Skills

OpenClaw (previously known as Moltbot, originally Clawdbot... identity crisis included, no extra charge) is a locally-running AI assistant that operates directly on your machine. Skills extend its capabilities, allowing it to interact with external services, automate workflows, and perform specialized tasks. This collection helps you discover and install the right skills for your needs.

Skills in this list are sourced from [ClawHub](https://www.clawhub.ai/) (OpenClaw's public skills registry) and categorized for easier discovery.

These skills follow the Agent Skill convention develop by Anthropic, an open standard for AI coding assistants.

> **Want to add a skill?** This list only includes skills that are **already published** in the "github.com/openclaw/skills". We do not accept links to personal repos, gists, or any other external source. If your skill isn't in the OpenClaw skills repo yet, publish it there first. See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## Installation

### ClawHub CLI

> **Note:** As you probably know, they keep renaming things. This reflects the current official docs. We'll update this when they rename it again.

```bash
npx clawhub@latest install <skill-slug>
```

### Manual Installation

Copy the skill folder to one of these locations:

| Location | Path |
|----------|------|
| Global | `~/.openclaw/skills/` |
| Workspace | `<project>/skills/` |

Priority: Workspace > Local > Bundled

### Alternative

You can also paste the skill's GitHub repository link directly into your assistant's chat and ask it to use it. The assistant will handle the setup automatically in the background.


## Why This List Exists?

OpenClaw's public registry (ClawHub) hosts **5,705 community-built skills** as of February 7, 2026. This awesome list has **3,002 skills**. Here's what we filtered out:

| Filter | Excluded |
|--------|----------|
| Possibly spam — bulk accounts, bot accounts, test/junk | 1,180 |
| Crypto / Blockchain / Finance / Trade | 672 |
| Duplicate / Similar name | 492 |
| Malicious — identified by security audits published by researchers (excluding VirusTotal) | 396 |
| Non-English — descriptions not in English | 8 |
| **Total not taken from OpenClaw's official skill registry** | **2,748** |

> **Disclaimer:** Inclusion in this list does **not** guarantee a skill is safe or trustworthy. OpenClaw now has a VirusTotal partnership that provides security scanning for skills. Before installing a skill, visit its page on ClawHub and check the VirusTotal report to see if it's flagged as risky. We also recommend reviewing a skill's source code before installing and using tools like Claude Code or Codex to inspect it for potentially harmful behavior.

If you think a skill was incorrectly excluded or miscategorized, feel free to open an issue or PR. We may have made mistakes.

<br/>

<a href="https://github.com/VoltAgent/voltagent">
<img width="1390" height="296" alt="social" src="https://github.com/user-attachments/assets/5d8822c0-e97b-4183-a71e-a922ab88e1a0" />
</a>

<br/>

## Table of Contents

| | | |
|---|---|---|
| [Coding Agents & IDEs](#coding-agents--ides) (133) | [Marketing & Sales](#marketing--sales) (143) | [Communication](#communication) (132) |
| [Git & GitHub](#git--github) (66) | [Productivity & Tasks](#productivity--tasks) (135) | [Speech & Transcription](#speech--transcription) (65) |
| [Moltbook](#moltbook) (51) | [AI & LLMs](#ai--llms) (287) | [Smart Home & IoT](#smart-home--iot) (56) |
| [Web & Frontend Development](#web--frontend-development) (202) | [Data & Analytics](#data--analytics) (46) | [Shopping & E-commerce](#shopping--e-commerce) (51) |
| [DevOps & Cloud](#devops-