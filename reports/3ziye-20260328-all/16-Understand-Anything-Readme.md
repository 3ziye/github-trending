<h1 align="center">Understand Anything</h1>

<p align="center">
  <strong>Turn any codebase into an interactive knowledge graph you can explore, search, and ask questions about.</strong>
</p>

<p align="center">
  <a href="README.md">English</a> | <a href="README.zh-CN.md">中文</a> | <a href="README.ja-JP.md">日本語</a> | <a href="README.tr-TR.md">Türkçe</a>
</p>

<p align="center">
  <a href="#-quick-start"><img src="https://img.shields.io/badge/Quick_Start-blue?style=for-the-badge" alt="Quick Start" /></a>
  <a href="https://github.com/Lum1104/Understand-Anything/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License: MIT" /></a>
  <a href="https://docs.anthropic.com/en/docs/claude-code"><img src="https://img.shields.io/badge/Claude_Code-Plugin-8A2BE2?style=for-the-badge" alt="Claude Code Plugin" /></a>
  <a href="https://lum1104.github.io/Understand-Anything"><img src="https://img.shields.io/badge/Homepage-d4a574?style=for-the-badge" alt="Homepage" /></a>
</p>

<p align="center">
  <img src="assets/hero.jpg" alt="Understand Anything — Turn any codebase into an interactive knowledge graph" width="800" />
</p>

---

> [!TIP]
> **A huge thank you to the community!** The support for Understand-Anything has been incredible. If this tool saves you a few minutes of digging through complexity, that's all I wanted. 🚀

**You just joined a new team. The codebase is 200,000 lines of code. Where do you even start?**

Understand Anything is a [Claude Code](https://docs.anthropic.com/en/docs/claude-code) plugin that analyzes your project with a multi-agent pipeline, builds a knowledge graph of every file, function, class, and dependency, then gives you an interactive dashboard to explore it all visually. Stop reading code blind. Start seeing the big picture.

---

## 🤔 Why?

Reading code is hard. Understanding a whole codebase is harder. Documentation is always out of date, onboarding takes weeks, and every new feature feels like archaeology.

Understand Anything fixes this by combining **LLM intelligence** with **static analysis** to produce a living, explorable map of your project — with plain-English explanations for everything.

---

## 🎯 Who is this for?

<table>
  <tr>
    <td width="33%" valign="top">
      <h3>👩‍💻 Junior Developers</h3>
      <p>Stop drowning in unfamiliar code. Get guided tours that walk you through the architecture step by step, with every function and class explained in plain English.</p>
    </td>
    <td width="33%" valign="top">
      <h3>📋 Product Managers & Designers</h3>
      <p>Finally understand how the system actually works without reading code. Ask questions like "how does authentication work?" and get clear answers grounded in the real codebase.</p>
    </td>
    <td width="33%" valign="top">
      <h3>🤖 AI-Assisted Developers</h3>
      <p>Give your AI tools deep context about your project. Use <code>/understand-diff</code> before code review, <code>/understand-explain</code> to dive into any module, or <code>/understand-chat</code> to reason about architecture.</p>
    </td>
  </tr>
</table>

---

## 🚀 Quick Start

### 1. Install the plugin

```bash
/plugin marketplace add Lum1104/Understand-Anything
/plugin install understand-anything
```

### 2. Analyze your codebase

```bash
/understand
```

A multi-agent pipeline scans your project, extracts every file, function, class, and dependency, then builds a knowledge graph saved to `.understand-anything/knowledge-graph.json`.

### 3. Explore the dashboard

```bash
/understand-dashboard
```

An interactive web dashboard opens with your codebase visualized as a graph — color-coded by architectural layer, searchable, and clickable. Select any node to see its code, relationships, and a plain-English explanation.

### 4. Keep learning

```bash
# Ask anything about the codebase
/understand-chat How does the payment flow work?

# Analyze impact of your current changes
/understand-diff

# Deep-dive into a specific file or function
/understand-explain src/auth/login.ts

# Generate an onboarding guide for new team members
/understand-onboard
```

---

## 🌐 Multi-Platform Installation

Understand-Anything works across multiple AI coding platforms.

### Claude Code (Native)

```bash
/plugin marketplace add Lum1104/Understand-Anything
/plugin install understand-anything
```

### Codex

Tell Codex:
```
Fetch and follow instructions from https://raw.githubusercontent.com/Lum1104/Understand-Anything/refs/heads/main/.codex/INSTALL.md
```

### OpenCode

Tell OpenCode:
```
Fetch and follow instructions from https://raw.githubusercontent.com/Lum1104/Understand-Anything/refs/heads/main/.opencode/INSTALL.md
```

### OpenClaw

Tell OpenClaw:
```
Fetch and follow instructions from https://raw.githubusercontent.com/Lum1104/Understand-Anything/refs/heads/main/.openclaw/INSTALL.md
```

### Cursor

Cursor auto-discovers the plugin via `.cursor-plugin/plugin.json` when this repo is cloned. No manual installati