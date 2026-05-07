# Hermes Control Interface

A self-hosted web dashboard for the [Hermes AI agent](https://github.com/NousResearch/hermes-agent) stack. Manage terminals, files, sessions, cron jobs, token analytics, multi-agent gateways, and team access — all behind a password gate.

**Stack:** Vanilla JS + Vite · Node.js · Express · WebSocket · xterm.js
**Version:** 3.5.0

---

## Highlights

> **Chat via Gateway API** — Real-time streaming, tool call cards with JSON viewer, session resume, stop button, multi-profile support. Auto-fallback to CLI.

> **RBAC v2** — 20 permissions across 3 roles. Admin, viewer, or custom roles per user.

> **Multi-Agent Gateway** — Start/stop/configure multiple Hermes profiles. Real-time logs. Systemd service management.

> **Token Analytics** — Track sessions, messages, tokens, cost by model, platform, and time range.

> **Security Hardened** — Command injection fixes, CSRF on 21 endpoints, dynamic CORS, comprehensive XSS protection (escapeHtml on all error handlers), 18 findings addressed.

---

## Screenshots

### Navigation — 8 Pages

**Home · Agents · Usage · Skills · Chat · Logs · Maintenance · Files**

### Dark Mode

| Home | Agents |
|------|--------|
| ![Home](docs/screenshots/dark/01-home.png) | ![Agents](docs/screenshots/dark/02-agents.png) |

| Chat | Usage & Analytics |
|------|------------------|
| ![Chat](docs/screenshots/dark/chat.png) | ![Usage](docs/screenshots/dark/03-usage.png) |

| Skills Hub | Maintenance |
|------------|-------------|
| ![Skills](docs/screenshots/dark/04-skills.png) | ![Maintenance](docs/screenshots/dark/05-maintenance.png) |

| File Explorer | Agent Dashboard |
|---------------|----------------|
| ![Files](docs/screenshots/dark/06-files.png) | ![Dashboard](docs/screenshots/dark/07-agent-dashboard.png) |

| Agent Gateway | Agent Sessions |
|---------------|----------------|
| ![Gateway](docs/screenshots/dark/09-agent-gateway.png) | ![Sessions](docs/screenshots/dark/08-agent-sessions.png) |

| Agent Config | Agent Memory |
|---------------|--------------|
| ![Config](docs/screenshots/dark/10-agent-config.png) | ![Memory](docs/screenshots/dark/11-agent-memory.png) |

| Agent Skills | Agent Cron |
|--------------|------------|
| ![Skills](docs/screenshots/dark/12-agent-skills.png) | ![Cron](docs/screenshots/dark/13-agent-cron.png) |

### Light Mode

| Home | Agents | Skills Hub |
|------|--------|------------|
| ![Home](docs/screenshots/light/01-home.png) | ![Agents](docs/screenshots/light/02-agents.png) | ![Skills](docs/screenshots/light/04-skills.png) |

| Gateway | Memory |
|---------|--------|
| ![Gateway](docs/screenshots/light/09-agent-gateway.png) | ![Memory](docs/screenshots/light/11-agent-memory.png) |

---

## Features

### 🔐 Authentication

- Single password login (configurable via `HERMES_CONTROL_PASSWORD`)
- bcrypt password hashing (cost factor 10)
- CSRF tokens on all mutating requests
- Conditional Secure cookie flag (auto-detects HTTPS)
- Rate limiting: 5 failed logins per 15 minutes per IP
- Multi-user support with role-based access control (RBAC)

---

### 🏠 Home Dashboard

System overview at a glance:
- **System Health**: CPU usage, RAM usage, Disk usage, Uptime
- **Agent Overview**: active model, provider, gateway status, configured API keys, active platforms
- **Gateway Status**: per-profile running/stopped indicators
- **Token Usage (7d)**: sessions count, messages, total tokens, estimated cost, models used, platforms breakdown, top tools

---

### 🤖 Agents — Multi-Agent Management

Manage all Hermes profiles from one place:
- List all profiles with status badge (running/stopped) and active model
- Create new profile
- Clone existing profile
- Delete profile
- Set default profile
- Start/Stop/Restart gateway per profile
- Quick gateway log viewer

---

### 💬 Chat — Revamped Interface

The chat interface got a full overhaul in v3.3.0:

**Tool Call Cards**
- Each tool call displayed as a collapsible card
- Shows tool name, status (running/success/error), and execution time
- Expand to see full JSON input/output
- Collapsed by default for clean output

**Session Sidebar**
- List of past chat sessions with timestamps
- Resume any session with one click
- New chat button for fresh session
- Shows active model tag

**Clean Output**
- Banner suppression (`-Q` flag) for noise-free responses
- Auto-detects both new (`session_id:`) and legacy (`Session:`) session ID formats
- `--continue ""` (empty) creates new session
- Bare `--continue` resumes last session

**Session Management**
- Rename sessions
- Delete sessions
- Export session transcript

---

### 📊 Usage & Analytics — Token Insights

Full breakdown of LLM usage:
- **Time Range**: Today, 7d, 30d, 90d filters
- **Agent Filter**: per-profile or all combined
- **Overview Cards**: total sessions, messages, tokens, cost, active hours
- **Models Table**: per-model breakdown — sessions count, total tokens, avg tokens/session
- **Platforms Table**: per-platform breakdown (CLI, Telegram, WhatsAp