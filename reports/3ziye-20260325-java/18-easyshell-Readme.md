<p align="center">
  <img src="docs/images/logo.png" alt="EasyShell Logo" width="200" />
</p>

# EasyShell

**AI-Native Server Operations Platform**

Let AI write your scripts, orchestrate multi-host tasks, and analyze your infrastructure — while you focus on what matters.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Docs](https://img.shields.io/badge/Docs-docs.easyshell.ai-green.svg)](https://docs.easyshell.ai)
[![Discord](https://img.shields.io/badge/Discord-Join%20Us-7289da?logo=discord&logoColor=white)](https://discord.gg/akQqRgNB6t)

**Language**: English | [简体中文](./README.zh-CN.md) | [繁體中文](./README.zh-TW.md) | [한국어](./README.ko.md) | [Русский](./README.ru.md) | [日本語](./README.ja.md)

---

## Why EasyShell?

Traditional server management tools expect you to write every script, SSH into every box, and interpret every output yourself. EasyShell flips that model: **AI is the operator, you are the decision-maker.**

- **Describe what you need in plain language** → AI writes production-ready shell scripts with diff review
- **Set a goal across multiple hosts** → AI plans the execution steps, runs them, and synthesizes the results
- **Schedule automated inspections** → AI analyzes output and decides whether to alert your team via bot channels
- **Connect via Web SSH** → Full terminal with file manager, multi-tab, search — no local client needed

---

## Core Features

### 1. AI Script Assistant

> Describe what you want. AI writes the script. Review the diff. One click to apply.

The AI Script Workbench is a split-panel editor where you describe requirements in natural language, and AI generates (or modifies) shell scripts targeting your chosen OS. Real-time streaming shows the script being written. A built-in diff view highlights exactly what changed. A summary tab explains the modifications in your language.

<p align="center">
  <img src="docs/images/AI%20Script%20helper.png" alt="AI Script Assistant — live code generation with diff review" width="90%" />
</p>

**How it works:**
1. **Describe** — write your requirements in natural language, choose the target OS
2. **Generate** — AI streams a production-ready script in real time
3. **Review** — built-in diff view highlights every change; summary tab explains modifications
4. **Apply** — one click to save the script to your library or dispatch it immediately

### 2. AI Task Orchestration

> "Check disk and memory on all hosts, flag anything over 80%, and suggest fixes." — Done.

The AI Chat interface lets you issue high-level operational goals. AI decomposes them into a multi-step execution plan (explore → analyze → report), dispatches scripts to target hosts, collects results, and delivers a structured analysis with risk assessment and actionable recommendations — all in a single conversation turn.

<p align="center">
  <img src="docs/images/AI%20task%20orchestration.png" alt="AI Task Orchestration — multi-step execution plan with analysis" width="90%" />
</p>

**How it works:**
1. **Instruct** — describe a high-level goal in the AI Chat (e.g. "check disk on all hosts")
2. **Plan** — AI decomposes the goal into a multi-step execution plan (explore → analyze → report)
3. **Execute** — scripts are dispatched to target hosts in parallel; results collected automatically
4. **Report** — AI delivers a structured analysis with risk assessment and actionable recommendations

### 3. AI Scheduled Inspections

> **Cron → Script → AI Analysis → Intelligent Alert** — AI analyzes output and decides whether to alert your team.

Schedule inspection tasks with cron expressions and select scripts from the built-in script library. EasyShell dispatches them to agents on schedule, collects output (disk, memory, services, logs), sends it to your AI model for intelligent analysis, and **lets AI decide whether the results warrant an alert** — pushing notifications only when they matter.

<p align="center">
  <img src="docs/images/schedule_task.png" alt="AI Scheduled Inspections — cron-based tasks with AI-powered output analysis and intelligent alerting" width="90%" />
</p>

**How it works:**
1. **Configure** — cron expression + script (from library or custom) + AI analysis prompt + notification rules
2. **Execute** — EasyShell dispatches to target agents on schedule
3. **Analyze** — Output sent to AI model (OpenAI / Gemini / GitHub Copilot / Custom) for intelligent analysis
4. **Notify** — AI determines severity and pushes alerts via bot channels when action is needed

**Notification modes:** Always push, push on failure, push on warning, or **AI decides** — the AI model evaluates the output and autonomously determines if an alert is necessary.

**Supported Bot Channels** ([Configuration Guide](https://docs.easyshell.ai/configuration/bot-channels/)):

| Bot | Status |
|-----|--------|
| [Telegram](https://docs.easyshell.ai/configuration/bot-channels/) | ✅ Supported |
| [Discord](https://docs.easyshell.ai/configuration/bot-channels/) | ✅ Sup