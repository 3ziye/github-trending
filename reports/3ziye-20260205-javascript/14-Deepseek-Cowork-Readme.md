<h1 align="center">DeepSeek Cowork</h1>

<p align="center">
<a href="https://deepseek-cowork.com">
  <img width="1280" height="640" alt="DeepSeek Cowork banner" src="./docs/images/preview.png">
</a>
</p>

<p align="center">
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square" alt="License: MIT" />
  </a>
  <a href="https://github.com/imjszhang/deepseek-cowork">
    <img src="https://img.shields.io/badge/Version-0.1.29-blue.svg?style=flat-square" alt="Version" />
  </a>
  <a href="https://www.electronjs.org/">
    <img src="https://img.shields.io/badge/Electron-28.x-47848F?style=flat-square&logo=electron" alt="Electron" />
  </a>
  <a href="https://nodejs.org/">
    <img src="https://img.shields.io/badge/Node.js-18+-339933?style=flat-square&logo=node.js" alt="Node.js" />
  </a>
</p>

<p align="center">
  <a href="#why-this-project">English</a> | <a href="./docs/README_CN.md">中文文档</a>
</p>

---
## DEMO

https://github.com/user-attachments/assets/a744dd83-0689-4fbe-8638-be0fe5e32935

## Why This Project?

On January 13, 2026, Anthropic released [Claude Cowork](https://claude.ai/cowork):

> *"Introducing Cowork: Claude Code for the rest of your work."*

Great product, but:

| | Claude Cowork | DeepSeek Cowork |
|--|---------------|-----------------|
| **Price** | 💰 Expensive | ✅ Ultra-low cost |
| **Accessibility** | 🔒 Complex setup, regional restrictions | ✅ Ready to use |
| **Open Source** | ❌ Proprietary | ✅ Fully open source |
| **Self-hosting** | ❌ Not supported | ✅ Supports private deployment |

We want everyone to have access to a great AI assistant — so we built this.

## Why DeepSeek?

| Solid Baseline | Ultra Affordable | Fully Open |
|----------------|------------------|------------|
| Reliable performance among open-source LLMs | Most competitive API pricing | Supports local deployment & customization |

## Core Philosophy

> **Open-source models will eventually catch up with closed-source.**

We believe it's only a matter of time. Rather than wait, we're building the infrastructure now.

When open-source models reach parity, DeepSeek Cowork will be ready.

## Why Now?

This would have been impossible before. But two things changed:

1. **AI Coding explosion** - Dramatically reduced development costs, enabling individuals to build complex applications
2. **Engineering bridges the gap** - Prompt engineering, skill systems, and context management can enhance the experience on existing models

## What Can It Do?

Use natural language to have AI help you with:

- 🌐 **Browser Automation** - Open pages, batch fill forms, extract data, cross-site operations
- 📁 **File Management** - Browse, organize, and preview your workspace files
- 🧠 **Persistent Memory** - AI remembers conversation context, understands your habits

**Typical Scenarios**

| Scenario | Example |
|----------|---------|
| Data Collection | "Extract prices from these 10 pages and make a spreadsheet" |
| Form Filling | "Batch fill registration forms using this contact list" |
| Content Organization | "Sort files in my downloads folder by type" |
| Monitoring | "Check this page daily and notify me of updates" |

> 💡 Like having a 24/7 digital assistant at your command

---

# Technical Documentation

## Architecture Highlights

DeepSeek Cowork adopts a unique **Hybrid SaaS** architecture, combining the best of cloud-based SaaS and local desktop applications:

```
┌─────────────────────────────────────────────────────────────────┐
│                        User's Computer                          │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────────┐  │
│  │   Electron   │    │  Web Browser │    │   CLI Tool       │  │
│  │   Desktop    │    │  (Chrome,    │    │ deepseek-cowork  │  │
│  │     App      │    │   Edge...)   │    │                  │  │
│  └──────┬───────┘    └──────┬───────┘    └────────┬─────────┘  │
│         │ IPC               │ HTTP/WS             │ manage     │
│         └───────────────────┼─────────────────────┘            │
│                             ▼                                   │
│                    ┌────────────────┐                          │
│                    │  LocalService  │◄── All data stays local  │
│                    │  (Node.js)     │                          │
│                    └────────┬───────┘                          │
└─────────────────────────────┼───────────────────────────────────┘
                              │ Encrypted
                              ▼
                    ┌────────────────┐
                    │   Happy AI     │
                    │   (Cloud)      │
                    └────────────────┘
```

| Feature | Benefit |
|---------|---------|
| **Zero Server Cost** | Static frontend hosted on GitHub Pages, no backend infrastructure needed |
| **Data Privacy** | All user data, settings, and files remain on your local machine |
| **Unified Experience** | Same UI/UX whether using Desk