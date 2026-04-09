## 通过 CDP 操控 Gemini 网页版，实现 AI 生图、对话、图片提取等自动化操作。
<!-- PROJECT SHIELDS -->

<div align="center">

  <a href="https://github.com/WJZ-P/gemini-skill/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/WJZ-P/gemini-skill.svg?style=flat-square" alt="Contributors" style="height: 30px">
  </a>
  &nbsp;
  <a href="https://github.com/WJZ-P/gemini-skill/network/members">
    <img src="https://img.shields.io/github/forks/WJZ-P/gemini-skill.svg?style=flat-square" alt="Forks" style="height: 30px">
  </a>
  &nbsp;
  <a href="https://github.com/WJZ-P/gemini-skill/stargazers">
    <img src="https://img.shields.io/github/stars/WJZ-P/gemini-skill.svg?style=flat-square" alt="Stargazers" style="height: 30px">
  </a>
  &nbsp;
  <a href="https://github.com/WJZ-P/gemini-skill/issues">
    <img src="https://img.shields.io/github/issues/WJZ-P/gemini-skill.svg?style=flat-square" alt="Issues" style="height: 30px">
  </a>
  &nbsp;
  <a href="https://github.com/WJZ-P/gemini-skill/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/WJZ-P/gemini-skill.svg?style=flat-square" alt="License" style="height: 30px">
  </a>

</div>

<br>

<!-- PROJECT LOGO -->

<p align="center">
  <a href="https://github.com/WJZ-P/gemini-skill/">
    <img src="markdown/gemini-color.svg" alt="Logo" width="96" height="96">
  </a>
</p>

<h1 align="center">Gemini Skill</h1>

<p align="center">
  <a href="#-使用">快速开始</a>
  ·
  <a href="https://github.com/WJZ-P/gemini-skill/issues">报告 Bug</a>
  ·
  <a href="https://github.com/WJZ-P/gemini-skill/issues">提出新特性</a>
</p>

<p align="center">
  <a href="./README.en.md">English</a> | 中文
</p>

<br>


<p align="center">
  <a href="https://www.bilibili.com/video/BV1e54y1z7XM">
    <img src="markdown/home.png" alt="纯蓝">
  </a>
</p>
<h2 align="center">

「剥开了尖刺 &nbsp; 却正如你曾经说

赖以生存的温柔只是白纸

盛着破碎的梦和我们的故事」

</h2>

## 目录

- [功能特性](#-功能特性)
- [架构](#️-架构)
- [安装](#-安装)
- [配置](#️-配置)
- [使用](#-使用)
- [MCP 工具列表](#-mcp-工具列表)
- [Daemon 生命周期](#-daemon-生命周期)
- [项目结构](#-项目结构)
- [注意事项](#️-注意事项)
- [To Do List](#-to-do-list)
- [License](#-license)

<br>

<!-- EXAMPLE -->

<p align="center">
  <img src="./markdown/example.png" alt="Gemini 生图示例" width="100%">
</p>

<p align="center"><em>▲ 通过 AI 对话自动生成表情包</em></p>

<br>

## ✨ 功能特性

|  | 功能 | 说明 |
|:---:|------|------|
| 🎨 | **AI 生图** | 发送 prompt 自动生成图片，支持高清原图下载 |
| 💬 | **文本对话** | 与 Gemini 进行多轮对话 |
| 🖼️ | **图片上传** | 上传参考图片，基于参考图生成新图 |
| 📥 | **图片提取** | 提取会话中的图片，支持 base64 和 CDP 完整尺寸下载 |
| 🔄 | **会话管理** | 新建会话、临时会话、切换模型、导航到历史会话 |
| 🧹 | **自动去水印** | 下载的图片自动移除 Gemini 水印 |
| 🤖 | **MCP Server** | 标准 MCP 协议接口，可被任何 MCP 客户端调用 |

<br>

## 🏗️ 架构

```
┌─────────────────────────────────────────────────────┐
│                   MCP Client (AI)                   │
│              Claude / CodeBuddy / ...               │
└──────────────────────┬──────────────────────────────┘
                       │ stdio (JSON-RPC)
                       ▼
┌─────────────────────────────────────────────────────┐
│               mcp-server.js (MCP 协议层)            │
│         注册所有 MCP 工具，编排调用流程              │
└──────────────────────┬──────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────┐
│            index.js → browser.js (连接层)           │
│   ensureBrowser() → 自动拉起 Daemon → CDP 直连      │
└──────────┬──────────────────────────────┬───────────┘
           │ HTTP (acquire/status)        │ WebSocket (CDP)
           ▼                              ▼
┌──────────────────────┐    ┌─────────────────────────┐
│   Browser Daemon     │    │     Chrome / Edge        │
│  (独立后台进程)       │───▶│   gemini.google.com     │
│  daemon/server.js    │    │                         │
│  ├─ engine.js        │    │  Stealth + 反爬检测      │
│  ├─ handlers.js      │    └─────────────────────────┘
│  └─ lifecycle.js     │
│     30 分钟惰性销毁   │
└──────────────────────┘
```

**核心设计理念：**

- **Daemon 模式** — 浏览器进程由独立 Daemon 管理，MCP 调用结束后浏览器不关闭，30 分钟无活动才自动释放
- **按需自启** — Daemon 未运行时 MCP 工具会自动拉起，无需手动启动
- **Stealth 反爬** — 使用 `puppeteer-extra-plugin-stealth` 绕过网站检测
- **职责分离** — `mcp-server.js`（协议层）→ `gemini-ops.js`（操作层）→ `browser.js`（连接层）→ `daemon/`（进程管理）

<br>

## 📦 安装

### 前置条件

- **Node.js** ≥ 18
- **Chrome / Edge / Chromium** — 系统上需安装任一浏览器（或通过 `BROWSER_PATH` 指定路径）
- 浏览器需提前 **登录 Google 账号**（Gemini 需要登录才能使用）

### 安装依赖

```bash
git clone https://github.com/WJZ-P/gemini-skill.git
cd gemini-skill
npm install
```

<br>

## ⚙️ 配置

所有配置通过环境变量或 `.env` 文件设置。项目根目录已提供 `.env` 模板，可直接修改。

**配置优先级：** `process.env` > `.env.development` > `.env` > 代码默认值

> `.env.development` 不会被 git 追踪，适合存放本地私有配置（如浏览器路径）。

### 浏览器配置

| 变量 | 默认值 | 说明 |
|------|--------|------|
| `BROWSER_PATH` | 自动检测 | 浏览器可执行文件路径，支持 Chrome / Edge / Chromium。不设则自动按优先级检测系统已安装的浏览器 |
| `BROWSER_DEBUG_PORT` | `40821` | CDP 远程调试端口。多个 skill（如 douyin-upload-mcp-skill）共享同一端口即共享同一浏览器实例 |
| `BROWSER_HEADLESS` | `false` | 是否无头模式。首次使用建议关闭（`false`），方便登录 Google 账号 |
| `BROWSER_USER_DATA_DIR` | 自动解析 | 浏览器用户数据目录，保存登录态、coo