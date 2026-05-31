<div align="right">
  <strong>繁體中文</strong> | <a href="./README.zh-Hans.md">简体中文</a> | <a href="./README.en.md">English</a>
</div>

<div align="center" markdown="1">

![AI Agent 學習路徑](resources/diagrams/banner.png)

# awesome-agentic-ai-zh

### 🤖 AI Agent 學習地圖 — 從基本 LLM 概念到自己打造多 agent 系統

<p><em><b>學習路線圖 + 240+ 資源 curation + 簡單 illustrative 案例</b><br/>結構化 8 階段、從「LLM 是什麼、token 怎麼算」走到 multi-agent 編排、Computer Use / Browser Use / Sandbox</em></p>

[![License](https://img.shields.io/badge/license-MIT-blue?style=flat)](LICENSE)
[![繁中](https://img.shields.io/badge/語言-繁體中文-red?style=flat)](README.md)
[![简中](https://img.shields.io/badge/語言-简体中文-orange?style=flat)](README.zh-Hans.md)
[![EN](https://img.shields.io/badge/lang-English-blue?style=flat)](README.en.md)
![GitHub stars](https://img.shields.io/github/stars/WenyuChiou/awesome-agentic-ai-zh?style=flat&logo=github)
![GitHub forks](https://img.shields.io/github/forks/WenyuChiou/awesome-agentic-ai-zh?style=flat&logo=github)
[![線上文件站](https://img.shields.io/badge/線上文件站-Pages-2ea44f?style=flat)](https://wenyuchiou.github.io/awesome-agentic-ai-zh/)

</div>

---

## 🎯 專案介紹

**本 repo 角色定位**：**學習路線圖 + 240+ 資源 curation + 簡單 illustrative 案例**——三件事為核心、幫想學 AI / AI agent 的人從「不知道從哪開始」走到「能設計多 agent 系統」。

具體做法：

| 核心 | 做什麼 | 規模 |
|---|---|---|
| **學習路線圖** | 把網路散落的高品質專案、教材、必修閱讀，按**從零開始、循序漸進**整理成 **8 個階段**（含 Stage 5 + Stage 8 兩個共用 hub）+ 2 條學習路線 + 5 條延伸路徑 | 8 stages、2 tracks |
| **資源 curation** | 每階段精選 **240+** 個 project（含星等、適合誰、教什麼、怎麼跑），加上中文 AI 生態(DeepSeek / Zhipu / Kimi 等)MCP / Skill 完整 catalog | 240+ projects、65 MCP/Skill |
| **簡單 illustrative 案例** | 每階段附 1-5 個**基礎練習**（70-150 行 starter + dual-path Ollama/Anthropic SDK 對照 + mock-based test） | 23 個練習 folder |

走完整條路線，你會從「**LLM 使用者**」進階到「**agent 系統建構者**」——能看懂 framework 在做什麼、能設計多 agent 協作、能寫自己的 MCP server。

> 📖 **關於中英文混用**：本專案保留 AI Agent 領域常見英文術語（Prompt Engineering / Context Engineering / Harness / MCP / Skills / RAG 等），因為官方文件、paper、GitHub repo 與 API 文件多以英文為主。每個重要概念會提供 **中文理解名 + 英文正式術語 + 一句白話定位**，讓讀者能先理解概念，再對接英文生態。完整對照見 [`resources/glossary.md`](resources/glossary.md)。

---

## 📋 目錄

- [🎯 專案介紹](#-專案介紹)
- [📚 快速開始](#-快速開始)
  - [線上閱讀](#線上閱讀)
  - [本地下載](#本地下載)
  - [✨ 你會收穫什麼？](#-你會收穫什麼)
- [🗺️ 學習地圖（兩條學習路徑）](#️-學習地圖兩條學習路徑)
- [💡 如何學習](#-如何學習)
- [📚 相關資源](#-相關資源)
- [🤝 如何貢獻](#-如何貢獻)
- [🙏 致謝](#-致謝)
- [🎓 引用](#-引用)
- [License](#license)

---

## 📚 快速開始

### 🚀 第一次接觸 AI agent / 沒寫過 code？

先看 **[`resources/setup-guide.md`](resources/setup-guide.md)** — 30-45 分鐘從零帶你申請 API key、裝好 Python、跑出第一個 LLM hello-world。

### 線上閱讀
- **[學習地圖（兩條學習路徑）](#️-學習地圖兩條學習路徑)** — 看完這節決定走 Track A 還 Track B
- **[Stage 0 基礎準備](stages/00-foundations.md)** — 已經會 Python / git / API 的人可以直接跳 Stage 1

### 本地下載
```bash
git clone https://github.com/WenyuChiou/awesome-agentic-ai-zh.git
cd awesome-agentic-ai-zh
# 從 stages/00-foundations.md 開始
```

### ✨ 你會收穫什麼？

- 📖 **完全免費** — MIT 授權，所有內容開放共學
- 🗺️ **兩條學習路徑** — Track A（CLI Power User）給「想 USE 現成 CLI agent」的人；Track B（Agent Builder）給「想 BUILD 自己 agent」的人。共用 Stage 0-2 基礎
- 🛠️ **基礎動手練習** — 每階段附 1-5 個 illustrative 練習（題目 + dual-path SDK 對照 + success criteria）。定位是**基礎入門 + 路線確認**——chapter-length 深度練習見對應 stage 的 hello-agents / Anthropic Cookbook callout
- 🎯 **精選 240+ 個 projects** — 每個都附星等推薦、適合誰、教什麼、怎麼跑（含本地 LLM 執行：Ollama、llama.cpp、LocalAI、MLX）
- 🌏 **三語完整維護** — 繁中(canonical)/ 簡中 / English,三版皆完整維護、英文非薄翻譯
- 🎓 **不只「框架」、還有「Claude Code 生態」** — MCP / Skills / Plugins / SDK 完整堆疊
- 🔬 **5 條依使用者分流的延伸路線** — 研究員 / 開發者 / 老師 / 知識工作者 / **日常使用者**
- ⏱️ **預估時程寫清楚** — Track A 8-10 週 / Track B 主幹最少 16-22 週、現實 5-7 個月（每週 5-8 hr）

---

## 🗺️ 學習地圖（兩條學習路徑）

![AI Agent 學習地圖](resources/diagrams/learning-map.png)

走完 **Stage 0-2（共用基礎）** 之後，依你的目的選一條學習路徑：

- **Track A — CLI Power User**：你想**用**現成的 CLI agent（Claude Code、Codex、OpenCode、Gemini CLI 等）把工作做順、效率拉高，不打算自己從零寫 agent。3 個 sub-stage（A1-A3）。
- **Track B — Agent Builder**：你想**從零打造**自己的 agent——學 framework、寫 ReAct、設計 multi-agent。Stage 3-7 是主路線。

兩條學習路徑**不互斥**——多數人是先走 A 把 CLI 用起來，再回到 B 學內部運作；或反過來也行。Stage 5（Claude Code 生態）兩條路徑都會用到。

### 共用基礎（Stage 0-2）

| Stage | 主題 | 關鍵內容 | 預估時程 |
|---|---|---|---|
| **0** | [基礎準備（Foundations）](stages/00-foundations.md) | Python · CLI · git · API · JSON | 1-2 週 |
| **1** | [LLM 基礎（LLM Basics）](stages/01-llm-basics.md) | token · API · 各家 LLM 比較 · 本地 LLM | 1 週 |
| **2** | [Prompt 設計（Prompt Engineering）](stages/02-prompt-engineering.md) | 系統 prompt · few-shot · CoT | 1-2 週 |

### Track A — CLI Power User（想用 CLI 把事情做完）

| Stage | 主題 | 關鍵內容 | 預估時程 |
|---|---|---|---|
| **A1** | [選一個 CLI Agent，開始用它做事（CLI Agent Intro & Selection）](tracks/cli/A1-cli-intro.md) | 7 主流 CLI 比較 · 安裝 · 第一次跑 | 1 週 |
| **A2** | [建立可重複使用的 CLI 工作流程（CLI Workflow Patterns）](tracks/cli/A2-cli-workflow.md) | CLAUDE.md · slash command · 多步驟拆解 | 1-2 週 |
| **A3** | [把 CLI Agent 接進真實工作流程（Integration & Production）](tracks/cli/A3-cli-production.md) | MCP 接 CLI · CI 自動化 · cost / observability | 1-2 週 |
| **+5** | [Stage 5 — Claude Code 生態](stages/05-claude-code-ecosystem.md)（**共用 hub**） | MCP · Skills · Plugins · Subagents、Track A 必看 5.1-5.4 /