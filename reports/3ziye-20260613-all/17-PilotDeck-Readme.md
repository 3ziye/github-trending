<p align="center">
  <img src="assets/banner.png" alt="PilotDeck" width="680"/>
</p>

<p align="center">
  Task-oriented AI Agent productivity platform — redefining operational boundaries and memory evolution, one WorkSpace at a time.
</p>

<p align="center">
  <a href="https://pilotdeck.openbmb.cn"><img src="https://img.shields.io/badge/Website-pilotdeck.openbmb.cn-FF6B35?style=flat-square&logo=googlechrome&logoColor=white" alt="Official Website"/></a>
  <a href="https://pilotdeck.openbmb.cn/pilotdeck.github.io/demo/p/pilotdeck-demo"><img src="https://img.shields.io/badge/Demo-Live-brightgreen?style=flat-square" alt="Live Demo"/></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-AGPL_3.0-blue.svg?style=flat-square" alt="License"/></a>
  <a href="https://modelcontextprotocol.io/"><img src="https://img.shields.io/badge/MCP-Native-6366F1?style=flat-square" alt="MCP Native"/></a>
  <a href="https://github.com/OpenBMB/PilotDeck/stargazers"><img src="https://img.shields.io/github/stars/OpenBMB/PilotDeck?style=flat-square" alt="Stars"/></a>
  <br/>
  <a href="#-community"><img src="https://img.shields.io/badge/Discord-Join_Community-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord"/></a>
  &nbsp;
  <a href="#-community"><img src="https://img.shields.io/badge/Feishu-Community-00D6B9?style=for-the-badge&logo=bytedance&logoColor=white" alt="Feishu"/></a>
  &nbsp;
  <a href="#-community"><img src="https://img.shields.io/badge/WeChat-Community-07C160?style=for-the-badge&logo=wechat&logoColor=white" alt="WeChat"/></a>
  <br/>
</p>

<p align="center">
  <b>English</b> | <a href="./README.zh.md">简体中文</a>
  <br/>
  <a href="https://pilotdeck.openbmb.cn">Website</a> · <a href="https://pilotdeck.openbmb.cn/pilotdeck.github.io/demo/p/pilotdeck-demo">Live Demo</a> · <a href="https://pilotdeck.openbmb.cn/pilotdeck.github.io/docs/en/introduction">Tutorial</a> · <a href="#-installation--quick-start">Quick Start</a> · <a href="#-key-highlights">Highlights</a> · <a href="#use-cases">Use Cases</a> · <a href="#-community">Community</a>
</p>

---

**News** 🔥

- **[2026.05.28]** PilotDeck is now open source! Visit our official website at [pilotdeck.openbmb.cn](https://pilotdeck.openbmb.cn). We welcome contributions, feedback, and stars from the community.

---

## 💡 About PilotDeck

**PilotDeck** is an open-source agent operating system designed around the concept of "WorkSpace". It is jointly developed and open-sourced by Tsinghua University [THUNLP](https://nlp.csai.tsinghua.edu.cn/), [ModelBest](https://modelbest.cn/), [OpenBMB](https://www.openbmb.cn/), and [AI9Stars](https://github.com/AI9Stars). Targeting general-purpose, multi-task scenarios, PilotDeck is built to be a true *productivity tool* for the Agent era.

A wave of excellent AI Agent harnesses has emerged in recent years, each with its own focus: **Claude Code / Cursor / Trae Solo** brought model reasoning deep into the programming IDE; **Claude Cowork** introduced the notion of project-level isolation to desktop-side knowledge work; **WorkBuddy** connected agents to IM ecosystems such as WeCom and Feishu so AI is one message away.

When we shift the lens from "one-shot programming" or "immediate Q&A" to **long-running, multi-project productivity work**, however, several questions remain open:

- When many projects run in parallel, can memory be **white-box and traceable**? When the AI gets something wrong, can you pinpoint which memory entry caused it and edit it directly — without starting a new chat from scratch?
- Can token cost be **tracked per task**, so that running agents in the background actually becomes economically viable?
- Can tasks of different difficulty **automatically be matched to different models**, instead of burning the flagship model on trivial calls?
- When you step away from the keyboard, can the work keep moving? Can the agent **proactively discover what's worth doing, report progress, and land results as files on disk**?

PilotDeck is an incremental exploration around exactly these questions. It uses the WorkSpace as the fundamental unit — completely isolating files, memory and skills per project — and pairs it with three pillar capabilities: **White-box Memory**, **Smart Routing** and **Always-on**. The entire system natively supports the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) and behaves consistently across front-ends (Web / CLI / IM).

### ✨ Key Highlights

<table width="100%">
<tr>
<td width="50%" valign="top">

**WorkSpace-Level Isolation & Accretion**

Every project gets its own file system, memory store and skill set. Parallel work no longer interferes with itself, retrieval has a bounded scope, and skills accrete naturally as each task grows — no more global context pollution.

<p align="center">
  <img src="assets/workspace_en.gif" width="100%" alt="WorkSpace isolation demo"/>
</p>

</td>
<td width="50%" valign="top">

**Traceable White-box Memory**

Memory generation