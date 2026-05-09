<p align="center">
  <strong>Hermes Web UI</strong>
  <a href="./README_zh.md">中文</a>
</p>

<p align="center">
  A full-featured web dashboard for <a href="https://github.com/NousResearch/hermes-agent">Hermes Agent</a>.<br/>
  Manage AI chat sessions, monitor usage & costs, configure platform channels,<br/>
  schedule cron jobs, browse skills — all from a clean, responsive web interface.
</p>

<p align="center">
  <code>npm install -g hermes-web-ui && hermes-web-ui start</code>
</p>

<p align="center">
  <img src="https://github.com/EKKOLearnAI/hermes-web-ui/blob/main/packages/client/src/assets/image1.png" alt="Hermes Web UI Demo" width="680"/>
</p>

<p align="center">
  <img src="https://github.com/EKKOLearnAI/hermes-web-ui/blob/main/packages/client/src/assets/image2.png" alt="Hermes Web UI Demo" width="680"/>
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/hermes-web-ui"><img src="https://img.shields.io/npm/v/hermes-web-ui?style=flat-square&color=blue" alt="npm version"/></a>
  <a href="https://github.com/EKKOLearnAI/hermes-web-ui/blob/main/LICENSE"><img src="https://img.shields.io/npm/l/hermes-web-ui?style=flat-square" alt="license"/></a>
  <a href="https://github.com/EKKOLearnAI/hermes-web-ui/stargazers"><img src="https://img.shields.io/github/stars/EKKOLearnAI/hermes-web-ui?style=flat-square" alt="stars"/></a>
</p>

---

## Features

### AI Chat

- Real-time streaming via SSE with async run support
- Multi-session management — create, rename, delete, switch between sessions
- **Self-built session database** — local SQLite storage with automatic sync from Hermes state.db on first startup
- Session grouping by source (Telegram, Discord, Slack, etc.) with collapsible accordion
- Active session indicator — live sessions pin to top with spinner icon
- Sessions sorted by latest message time
- Markdown rendering with syntax highlighting and code copy
- Tool call detail expansion (arguments / result)
- File upload support
- File download support — download user-uploaded files and agent-generated files across local, Docker, SSH, and Singularity backends
- Session search — Ctrl+K global search across all conversations
- Global model selector — discovers models from `~/.hermes/auth.json` credential pool
- Per-session model display badge and context token usage

### Platform Channels

Unified configuration for **8 platforms** in one page:

| Platform      | Features                                                               |
| ------------- | ---------------------------------------------------------------------- |
| Telegram      | Bot token, mention control, reactions, free-response chats             |
| Discord       | Bot token, mention, auto-thread, reactions, channel allow/ignore lists |
| Slack         | Bot token, mention control, bot message handling                       |
| WhatsApp      | Enable/disable, mention control, mention patterns                      |
| Matrix        | Access token, homeserver, auto-thread, DM mention threads              |
| Feishu (Lark) | App ID / Secret, mention control                                       |
| WeChat        | QR code login (scan in browser, auto-save credentials)                 |
| WeCom         | Bot ID / Secret                                                        |

- Credential management writes to `~/.hermes/.env`
- Channel behavior settings write to `~/.hermes/config.yaml`
- Auto gateway restart on config change
- Per-platform configured/unconfigured status detection

### Usage Analytics

- Total token usage breakdown (input / output)
- Session count with daily average
- Estimated cost tracking & cache hit rate
- Model usage distribution chart
- 30-day daily trend (bar chart + data table)

### Scheduled Jobs

- Create, edit, pause, resume, delete cron jobs
- Trigger immediate execution
- Cron expression quick presets

### Model Management

- Auto-discover models from credential pool (`~/.hermes/auth.json`)
- Fetch available models from each provider endpoint (`/v1/models`)
- Add, update, and delete providers (preset & custom OpenAI-compatible)
- OpenAI Codex & Nous Portal OAuth login
- Provider URL auto-detection for non-v1 API versions (e.g. `/v4`)
- Provider-level model grouping with default model switching

### Multi-Profile & Gateway

- Create, rename, delete, and switch between Hermes profiles
- Clone existing profile or import from archive (`.tar.gz`)
- Export profile for backup or sharing
- Multi-gateway management — start, stop, and monitor gateway per profile
- Auto port conflict resolution
- Profile-scoped configuration and cache isolation

### File Browser

- Browse files on remote backends (local, Docker, SSH, Singularity)
- Upload, download, rename, copy, move, and delete files
- Create directories
- View file content with syntax highlighting

### Group Chat

- Multi-agent chat rooms with real-time messaging via Socket.IO
- @mention routing — mention an agent to trigger a contextual reply
- Context compression — a