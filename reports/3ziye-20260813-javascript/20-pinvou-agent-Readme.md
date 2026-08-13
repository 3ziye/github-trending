<div align="center">

<img src="pinvou3-app/src-tauri/icons/icon.png" alt="Pinvou Agent logo" width="120" />

# Pinvou Agent

**An open-source desktop AI agent workspace for work, design, and coding.**

[English](README.md) · [简体中文](README.zh-CN.md)

[![CI](https://github.com/Pinvou/pinvou-agent/actions/workflows/pr-check.yml/badge.svg)](https://github.com/Pinvou/pinvou-agent/actions/workflows/pr-check.yml)
[![License: MIT](https://img.shields.io/github/license/Pinvou/pinvou-agent)](LICENSE)
[![Version](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2FPinvou%2Fpinvou-agent%2Fmain%2Fpinvou3-app%2Fpackage.json&query=%24.version&label=version&color=blue)](pinvou3-app/package.json)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)](#-quick-start)
[![GitHub Stars](https://img.shields.io/github/stars/Pinvou/pinvou-agent?style=flat)](https://github.com/Pinvou/pinvou-agent/stargazers)

[Download Preview](https://github.com/Pinvou/pinvou-agent/releases) · [Website](https://pinvou.com/) · [Issues](https://github.com/Pinvou/pinvou-agent/issues) · [Discussions](https://github.com/Pinvou/pinvou-agent/discussions) · [Security](SECURITY.md)

<p align="center">
  <a href="https://pinvou.com/assets/videos/pinvou-agent-feature-update-2026-07.mp4">
    <img src="docs/assets/screenshots/mode-work.webp" alt="Pinvou Agent Work mode">
  </a>
</p>
<p align="center">
  <a href="https://pinvou.com/assets/videos/pinvou-agent-feature-update-2026-07.mp4"><strong>▶ Watch the 90-second feature demo (Chinese)</strong></a>
</p>

</div>

Pinvou Agent is more than a chat window. It brings everyday work, visual design, and software development into one desktop workspace — designed for tasks that should end with **a result**, not just another chat response. Use tools, work with files, and build personal knowledge; bring a dedicated coding agent into a real project over ACP; or turn a prompt into a visual artifact you can continue editing.

Use a local model for a fully private loop, connect any OpenAI-compatible endpoint, and extend the agent with MCP servers, CLI connectors, Skills, and workflows.

## 🧭 One workspace, three ways to work

### 💼 Work: give the agent a real task

Combine attachments, personal knowledge, specialist personas, Skills, MCP tools, and workflows to research, analyze, write, and deliver reusable files — not just another block of chat text.

### 🎨 Design: from a prompt to an editable visual

Create posters and data visualizations in natural language. Open the result in design mode, select elements directly, and adjust copy, fonts, colors, dimensions, and layout — or keep describing changes and let the agent iterate on the current design.

### 💻 Code: bring a coding agent into a real project

Use **Codex, Claude Code, or Kimi** through [ACP](docs/multi-agent-acp.md) in the same desktop workspace. The coding agent can read and edit a real project or an isolated temporary workspace, run commands, and surface plans, tool steps, permission requests, and file changes. Sessions stay bound to their workspace and can be continued after restarting the app.

## ✨ Features

### 🎯 From conversation to deliverables

- **Multi-session workspace** with title search — messages, tool calls, and artifacts persist with each session
- **Attachments** for PDF, Office documents, images, and text — drag, drop, or paste them in
- **Artifact panel** automatically collects every file the agent creates or edits; preview, locate, and open them in one place
- **Editable Markdown artifacts** — edit directly, or select a passage and ask the agent to revise it
- **Plan / YOLO modes** — review the plan first for complex work, or execute directly when the task is clear

### 🧠 Knowledge and memory

- **Local knowledge base** with file management, full-text and vector retrieval; attach multiple collections to one chat, enable or disable each independently, and retain collection and file provenance in answers
- **Memory center** captures long-term preferences and context, with explicit candidate review and confirmation
- **Persona card pool** — create, save, and apply specialist roles for different domains
- **Skills, Commands, and workflows** turn proven methods into stable, reusable capabilities

### 🔌 Real tools and connectors

- **Unified tool store** for local MCP servers, remote MCP servers, CLI tools, and API connectors
- **OAuth / SSO authorization** where supported — no manual key pasting
- Ready-made connectors for **Feishu (Lark), DingTalk, WeCom, Tencent Meeting, Tencent ima, Obsidian**, enterprise knowledge bases, and legal / enterprise data services
- **Remote control** — scan a QR code from your phone to view and steer the running workspace

### 🖥️ Built for daily operation

- **Local voice input** with on-demand speech model downloads
- **Centralized monitoring** of GPU, memory, disk, model service, and context usage
- **In-app updates** on Linux, with OTA