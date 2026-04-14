# lark-cli

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Go Version](https://img.shields.io/badge/go-%3E%3D1.23-blue.svg)](https://go.dev/)
[![npm version](https://img.shields.io/npm/v/@larksuite/cli.svg)](https://www.npmjs.com/package/@larksuite/cli)

[中文版](./README.zh.md) | [English](./README.md)

The official [Lark/Feishu](https://www.larksuite.com/) CLI tool, maintained by the [larksuite](https://github.com/larksuite) team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Slides, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 22 AI Agent [Skills](./skills/).

[Install](#installation--quick-start) · [AI Agent Skills](#agent-skills) · [Auth](#authentication) · [Commands](#three-layer-command-system) · [Advanced](#advanced-usage) · [Security](#security--risk-warnings-read-before-use) · [Contributing](#contributing)

## Why lark-cli?

- **Agent-Native Design** — 22 structured [Skills](./skills/) out of the box, compatible with popular AI tools — Agents can operate Lark with zero extra setup
- **Wide Coverage** — 14 business domains, 200+ curated commands, 22 AI Agent [Skills](./skills/)
- **AI-Friendly & Optimized** — Every command is tested with real Agents, featuring concise parameters, smart defaults, and structured output to maximize Agent call success rates
- **Open Source, Zero Barriers** — MIT license, ready to use, just `npm install`
- **Up and Running in 3 Minutes** — One-click app creation, interactive login, from install to first API call in just 3 steps
- **Secure & Controllable** — Input injection protection, terminal output sanitization, OS-native keychain credential storage
- **Three-Layer Architecture** — Shortcuts (human & AI friendly) → API Commands (platform-synced) → Raw API (full coverage), choose the right granularity

## Features

| Category      | Capabilities                                                                                                                      |
| ------------- |-----------------------------------------------------------------------------------------------------------------------------------|
| 📅 Calendar   | View agenda, create events, invite attendees, check free/busy status, time suggestions                                            |
| 💬 Messenger  | Send/reply messages, create and manage group chats, view chat history & threads, search messages, download media                  |
| 📄 Docs       | Create, read, update, and search documents, read/write media & whiteboards                                                        |
| 📁 Drive      | Upload and download files, search docs & wiki, manage comments                                                                    |
| 📊 Base       | Create and manage tables, fields, records, views, dashboards, workflows, forms, roles & permissions, data aggregation & analytics |
| 📈 Sheets     | Create, read, write, append, find, and export spreadsheet data                                                                    |
| 🖼️ Slides     | Create and manage presentations, read presentation content, and add or remove slides                                             |
| ✅ Tasks      | Create, query, update, and complete tasks; manage task lists, subtasks, comments & reminders                                      |
| 📚 Wiki       | Create and manage knowledge spaces, nodes, and documents                                                                          |
| 👤 Contact    | Search users by name/email/phone, get user profiles                                                                               |
| 📧 Mail       | Browse, search, read emails, send, reply, forward, manage drafts, watch new mail                                                  |
| 🎥 Meetings   | Search meeting records, query meeting minutes & recordings                                                                        |
| 🕐 Attendance | Query personal attendance check-in records                                                                                        |
| ✍️ Approval   | Query approval tasks, approve/reject/transfer tasks, cancel and CC instances                                                      |

## Installation & Quick Start

### Requirements

Before you start, make sure you have:

- Node.js (`npm`/`npx`)
- Go `v1.23`+ and Python 3 (only required for building from source)

### Quick Start (Human Users)

> **Note for AI assistants:** If you are an AI Agent helping the user with installation, jump directly to [Quick Start (AI Agent)](#quick-start-ai-agent), which contains all the steps you need to complete.

#### Install

Choose **one** of the following methods:

**Option 1 — From npm (recommended):**

```bash
# Install CLI
npm install -g @larksuite/cli

# Install CLI SKILL (required)
npx skills add larksuite/cli -y -g
```

**Option 2 — From source:**

Requires Go `v1.23`+ 