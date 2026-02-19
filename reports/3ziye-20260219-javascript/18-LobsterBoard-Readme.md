# 🦞 LobsterBoard

A self-hosted, drag-and-drop dashboard builder with 50 widgets, a template gallery, custom pages, and zero cloud dependencies. One Node.js server, no frameworks, no build step needed.

**Works standalone or with [OpenClaw](https://github.com/openclaw/openclaw).** LobsterBoard is a general-purpose dashboard — use it to monitor your homelab, track stocks, display weather, manage todos, or anything else. OpenClaw users get bonus widgets (auth status, cron jobs, activity logs), but they're completely optional.

![LobsterBoard](lobsterboard-logo-final.png)

![LobsterBoard Dashboard](lobsterboard-screenshot.jpg)

## Quick Start

```bash
npm install lobsterboard
cd node_modules/lobsterboard
node server.cjs
```

Or clone it:

```bash
git clone https://github.com/Curbob/LobsterBoard.git
cd LobsterBoard
npm install
node server.cjs
```

Open **http://localhost:8080** → press **Ctrl+E** to enter edit mode → drag widgets from the sidebar → click **💾 Save**.

![Edit Mode](lobsterboard-editor.jpg)

## Features

- **Drag-and-drop editor** — visual layout with 20px snap grid, resize handles, property panel
- **50 widgets** — system monitoring, weather, calendars, RSS, smart home, finance, AI/LLM tracking, notes, and more
- **Template Gallery** — export, import, and share dashboard layouts with auto-screenshot previews; import as merge or full replace
- **Custom pages** — extend your dashboard with full custom pages (notes, kanban boards, anything)
- **Canvas sizes** — preset resolutions (1920×1080, 2560×1440, etc.) or custom sizes
- **Live data** — system stats stream via Server-Sent Events, widgets auto-refresh
- **Dark theme** — the only correct choice
- **No cloud** — everything runs locally, your data stays yours

## Configuration

```bash
PORT=3000 node server.cjs              # Custom port
HOST=0.0.0.0 node server.cjs           # Expose to network
```

Widget settings are edited in the right-hand panel during edit mode. All configuration saves to `config.json`.

## Template Gallery

![Template Gallery](lobsterboard-templates.jpg)

LobsterBoard includes a built-in template system for sharing and reusing dashboard layouts.

![Template Import](lobsterboard-template-detail.jpg)

- **Export** your current dashboard as a template (auto-captures a screenshot preview)
- **Browse** the template gallery to discover pre-built layouts
- **Import** templates in two modes:
  - **Replace** — swap your entire dashboard for the template
  - **Merge** — append the template's widgets below your existing layout
- Templates are stored in the `templates/` directory and can be shared as folders

![Dashboard Example](lobsterboard-dashboard-2.jpg)

## Widgets

### 🖥️ System Monitoring
| Widget | Description |
|--------|-------------|
| CPU / Memory | Real-time CPU load and memory usage |
| Disk Usage | Disk space with ring gauge |
| Network Speed | Upload/download throughput |
| Uptime Monitor | System uptime, CPU load, memory summary |
| Docker Containers | Container list with status |

### 🌤️ Weather
| Widget | Description |
|--------|-------------|
| Local Weather | Current conditions for your city |
| World Weather | Multi-city weather overview |

### ⏰ Time & Productivity
| Widget | Description |
|--------|-------------|
| Clock | Analog/digital clock |
| World Clock | Multiple time zones |
| Countdown | Timer to a target date |
| Todo List | Persistent task list |
| Pomodoro Timer | Work/break timer |
| Notes | Persistent rich-text notes with auto-save |

### 📰 Media & Content
| Widget | Description |
|--------|-------------|
| RSS Ticker | Scrolling feed from any RSS/Atom URL |
| Calendar | iCal feed display (Google, Apple, Outlook) |
| Now Playing | Currently playing media |
| Quote of Day | Random inspirational quotes |
| Quick Links | Bookmark grid |

### 🤖 AI / LLM Monitoring
| Widget | Description |
|--------|-------------|
| Claude Usage | Anthropic API spend tracking |
| AI Cost Tracker | Monthly cost breakdown |
| API Status | Provider availability |
| Active Sessions | OpenClaw session monitor |
| Token Gauge | Context window usage |

### 💰 Finance
| Widget | Description |
|--------|-------------|
| Stock Ticker | Live stock prices (requires API key) |
| Crypto Price | Cryptocurrency tracker |

### 🏠 Smart Home
| Widget | Description |
|--------|-------------|
| Indoor Climate | Temperature/humidity sensors |
| Camera Feed | IP camera stream |
| Power Usage | Energy monitoring |

### 🔗 Embeds & Media
| Widget | Description |
|--------|-------------|
| Image / Random Image / Web Image / Latest Image | Static, rotating, remote, or latest images (with browse button for directory selection) |
| Iframe Embed | Embed any webpage |

### 🔧 Utility
| Widget | Description |
|--------|-------------|
| Auth Status | Authentication status display |
| Sleep Score | Garmin sleep score widget |
| GitHub Stats | Repository stats — stars, forks, open issues, open PRs |
| Unread Emails | Email inbox counter |
| System Log | Rec