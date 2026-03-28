<!-- <p align="center">
  <img src="assets/logo-horizontal.png" alt="OpenMAIC" width="420"/>
</p> -->

<p align="center">
  <img src="assets/banner.png" alt="OpenMAIC Banner" width="680"/>
</p>

<p align="center">
  Get an immersive, multi-agent learning experience in just one click
</p>

<p align="center">
  <a href="https://jcst.ict.ac.cn/en/article/doi/10.1007/s11390-025-6000-0"><img src="https://img.shields.io/badge/Paper-JCST'26-blue?style=flat-square" alt="Paper"/></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-AGPL--3.0-blue.svg?style=flat-square" alt="License: AGPL-3.0"/></a>
  <a href="https://open.maic.chat/"><img src="https://img.shields.io/badge/Demo-Live-brightgreen?style=flat-square" alt="Live Demo"/></a>
  <a href="https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FTHU-MAIC%2FOpenMAIC&envDescription=Configure%20at%20least%20one%20LLM%20provider%20API%20key%20(e.g.%20OPENAI_API_KEY%2C%20ANTHROPIC_API_KEY).%20All%20providers%20are%20optional.&envLink=https%3A%2F%2Fgithub.com%2FTHU-MAIC%2FOpenMAIC%2Fblob%2Fmain%2F.env.example&project-name=openmaic&framework=nextjs"><img src="https://vercel.com/button" alt="Deploy with Vercel" height="20"/></a>
  <a href="#-openclaw-integration"><img src="https://img.shields.io/badge/OpenClaw-Integration-F4511E?style=flat-square" alt="OpenClaw Integration"/></a>
  <a href="https://github.com/THU-MAIC/OpenMAIC/stargazers"><img src="https://img.shields.io/github/stars/THU-MAIC/OpenMAIC?style=flat-square" alt="Stars"/></a>
  <br/>
  <a href="https://discord.gg/PtZaaTbH"><img src="https://img.shields.io/badge/Discord-Join_Community-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord"/></a>
  &nbsp;
  <a href="community/feishu.md"><img src="https://img.shields.io/badge/Feishu-飞书交流群-00D6B9?style=for-the-badge&logo=bytedance&logoColor=white" alt="Feishu"/></a>
  <br/>
  <img src="https://img.shields.io/badge/Next.js-16-black?style=flat-square&logo=next.js" alt="Next.js"/>
  <img src="https://img.shields.io/badge/React-19-61DAFB?style=flat-square&logo=react&logoColor=white" alt="React"/>
  <img src="https://img.shields.io/badge/TypeScript-5-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript"/>
  <img src="https://img.shields.io/badge/LangGraph-1.1-purple?style=flat-square" alt="LangGraph"/>
  <img src="https://img.shields.io/badge/Tailwind_CSS-4-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white" alt="Tailwind CSS"/>
</p>

<p align="center">
  <a href="./README.md">English</a> | <a href="./README-zh.md">简体中文</a>
  <br/>
  <a href="https://open.maic.chat/">Live Demo</a> · <a href="#-quick-start">Quick Start</a> · <a href="#-features">Features</a> · <a href="#-use-cases">Use Cases</a> · <a href="#-openclaw-integration">OpenClaw</a>
</p>


## 🗞️ News

- **2026-03-26** — [v0.1.0 released!](https://github.com/THU-MAIC/OpenMAIC/releases/tag/v0.1.0) Discussion TTS, immersive mode, keyboard shortcuts, whiteboard enhancements, new providers, and more. See [changelog](CHANGELOG.md).

## 📖 Overview

**OpenMAIC** (Open Multi-Agent Interactive Classroom) is an open-source AI platform that turns any topic or document into a rich, interactive classroom experience. Powered by multi-agent orchestration, it generates slides, quizzes, interactive simulations, and project-based learning activities — all delivered by AI teachers and AI classmates who can speak, draw on a whiteboard, and engage in real-time discussions with you. With built-in [OpenClaw](https://github.com/openclaw/openclaw) integration, you can generate classrooms directly from messaging apps like Feishu, Slack, or Telegram.

https://github.com/user-attachments/assets/b4ab35ac-f994-46b1-8957-e82fe87ff0e9

### Highlights

- **One-click lesson generation** — Describe a topic or attach your materials; the AI builds a full lesson in minutes
- **Multi-agent classroom** — AI teachers and peers lecture, discuss, and interact with you in real time
- **Rich scene types** — Slides, quizzes, interactive HTML simulations, and project-based learning (PBL)
- **Whiteboard & TTS** — Agents draw diagrams, write formulas, and explain out loud
- **Export anywhere** — Download editable `.pptx` slides or interactive `.html` pages
- **[OpenClaw integration](#-openclaw-integration)** — Generate classrooms from Feishu, Slack, Telegram, and 20+ messaging apps via your AI assistant

---

> [!TIP]
> ### <img src="https://cdn.jsdelivr.net/gh/homarr-labs/dashboard-icons/png/openclaw.png" height="28" align="top"/> OpenClaw — Use OpenMAIC from your chat app, zero setup
>
> With [OpenClaw](https://github.com/openclaw/openclaw), you can generate classrooms directly from Feishu, Slack, Discord, Telegram, and 20+ messaging apps.
>
> 1. `clawhub install openmaic` or just ask your Claw *"install OpenMAIC skill"*
> 2. Pick a mode:
>    - **Hosted mode** — Get an access code at [open.maic.chat](https://open.maic.chat/), no local setup needed
>    - **Self-hosted** — The ski