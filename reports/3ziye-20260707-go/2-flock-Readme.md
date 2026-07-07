<p align="center">
  <b>English</b> ·
  <a href="README.ru.md">Русский</a> ·
  <a href="README.zh.md">中文</a> ·
  <a href="README.es.md">Español</a> ·
  <a href="README.de.md">Deutsch</a> ·
  <a href="README.fr.md">Français</a> ·
  <a href="README.pt-BR.md">Português (BR)</a> ·
  <a href="README.ja.md">日本語</a>
</p>

# Flock

**Run a Claude Code AI dev team on your server and drive it from chat.** Describe a feature in Telegram or VK; the team plans it, builds it on a branch, tests it, reviews it, and opens a PR — each chat in its own isolated workspace.

[![CI](https://github.com/duckbugio/flock/actions/workflows/ci.yml/badge.svg)](https://github.com/duckbugio/flock/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Go 1.26](https://img.shields.io/badge/Go-1.26-00ADD8.svg)](go.mod)
[![image: ghcr.io](https://img.shields.io/badge/image-ghcr.io-2496ED.svg)](https://github.com/orgs/duckbugio/packages)

It runs on your Claude **Pro/Max subscription** (no per-token billing) or an Anthropic API key, ships as **prebuilt Docker images** (no build step), and keeps every chat in its own sandboxed workspace.

## Quick start (Docker)

```bash
git clone https://github.com/duckbugio/flock
cd flock/adapters/telegram
cp .env.example .env        # fill in the REQUIRED block (4 values)
docker compose up -d
```

That pulls the prebuilt image `ghcr.io/duckbugio/flock-telegram` — no build, no Ansible — then message your bot. The minimum `.env`:

| Variable | What |
|---|---|
| `TELEGRAM_BOT_TOKEN` | from [@BotFather](https://t.me/botfather) |
| `TELEGRAM_BOT_USERNAME` | your bot's @username (no `@`) |
| `ALLOWED_USERS` | comma-separated Telegram user IDs allowed to use the bot |
| `CLAUDE_CODE_OAUTH_TOKEN` | `claude setup-token` (subscription) — *or* set `ANTHROPIC_API_KEY` |

Everything else in [`.env.example`](adapters/telegram/.env.example) has sensible defaults. Update later with `docker compose pull && docker compose up -d`.

> **Region:** host in an **Anthropic-supported region** (some countries, e.g. RU/CN, are geo-blocked) — otherwise Claude calls fail.

**VK** is the same pattern under [`adapters/vk/`](adapters/vk/), built on the same core and published as `ghcr.io/duckbugio/flock-vk`. It ships only an env template (no compose file): `cp .env.example .env`, then `docker run --env-file .env ghcr.io/duckbugio/flock-vk`. Claude auth and core settings match Telegram; only the three transport vars change:

| Variable | What |
|---|---|
| `VK_BOT_TOKEN` | community access token (VK community → Manage → API usage → access token) |
| `VK_GROUP_ID` | your community's numeric id (long-poll server + mention parse) |
| `VK_ALLOWED_USERS` | comma-separated VK user IDs allowed to use the bot |

## Highlights

- **The conversation is the task source** — describe what you want in chat and review the PR that comes back; the agent's shell and editor are sandboxed inside the container.
- **A real dev-team pipeline, not a single prompt** — spec-first acceptance criteria, build/regression gates, and an arbiter that breaks loops.
- **Multi-transport** — **Telegram** and **VK** today, both on the same core; a new platform is a thin adapter, not a fork.
- **PR reactions without inbound webhooks** — the bot *polls* your git host for new review comments and routes each back to the chat that opened the PR.
- **Subscription-friendly** — authenticate with a Claude Pro/Max token (no per-token cost) or an Anthropic API key.

## How it works

```
You (in a chat): "implement X across the api + web services"
  → bot's Claude (Lead) → planner → confirm scope → coder ⇄ tester → PR per repo
                                                      → reviewer (inline comments) ⇄ coder → arbiter
                                                                                        ├ APPROVE → you merge
                                                                                        └ ESCALATE → asks you
```

The five subagents — **planner → coder → tester → reviewer → arbiter** — run as native Claude Code subagents in [`core/agents/`](core/agents/). A plain question is just answered; a build request triggers the team. The **arbiter** is the risk-aware, cycle-limited loop-breaker so agents never spin forever. Branches are named `duck/<chatid>/<slug>` so PR-webhook/poll events route back to the right chat.

The team is built for a **microservices** workspace: a feature can span several services, and it coordinates branches and one cross-linked PR per repo. The full pipeline, guardrails, and role table live in [`core/README.md`](core/README.md).

## Repo layout (monorepo)

The platform-agnostic dev-team brain lives in [`core/`](core/); each platform is a thin adapter under `adapters/<name>/` that shares it.

| Adapter | Path | Prebuilt image |
|---|---|---|
| Telegram | [`adapters/telegram/`](adapters/telegram/) | `ghcr.io/duckbugio/flock-telegram` |
| VK | [`adapters/vk/`](adapters/vk/) | `ghcr.io/duc