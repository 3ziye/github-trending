# Kindle Planner Dashboard

Monochrome, Kindle-friendly planner dashboard with Telegram bot updates.

## Requirements

- A jailbroken Kindle with KUAL installed for the native dashboard.
- Node.js 20+ and npm for scripts, checks, and backend bootstrapping.
- An InsForge account for the database, edge functions, and secrets.
- A Telegram bot token from BotFather for chat-based planner updates.
- Optional: an OpenAI API key for natural-language message parsing. Without
  it, the webhook uses the built-in command parser.
- Optional: Zig or a Kindle-compatible ARM cross compiler to rebuild the KUAL
  package.
- Optional: Xcode and a real iPhone for the Health Sync companion app.

## Setup Instructions

This repo can be published as a bring-your-own-backend kit. Each owner runs
their own InsForge project, Telegram bot, and KUAL package config instead of
connecting to this checkout's production backend.

Start with [docs/INSTALL_FOR_USERS.md](docs/INSTALL_FOR_USERS.md).

If you are using a coding assistant for setup, use
[docs/SETUP_WITH_ASSISTANT.md](docs/SETUP_WITH_ASSISTANT.md).

## Project Structure

- `functions/`: InsForge edge functions for dashboard JSON, live events,
  item toggles, Telegram parsing/actions, version checks, and Health Sync
  uploads.
- `migrations/`: Postgres schema and optional sample-data migrations used by
  the bring-your-own-backend setup.
- `kindle/native/`: Native C++ e-ink dashboard renderer, local render check,
  and KUAL package build targets.
- `kindle/kual/kindle-dashboard/`: KUAL extension files, shell launchers,
  placeholder assets, and `config.sh.example`.
- `kindle/launch-dashboard.sh`: Kindle-side launcher used by installed
  shortcuts and native install helpers.
- `ios/HealthSyncCompanion/`: Optional iOS app that reads Apple Health daily
  aggregates and posts them to the `health-sync` function.
- `scripts/`: Setup and maintenance helpers for InsForge bootstrapping,
  Telegram webhook configuration, Kindle native install, and Kindle proof
  checks.
- `docs/`: Human and coding-assistant setup guides.

## Technical Breakdown

### The Stack

**Renderer:** Native C++ app

**Backend:** InsForge

**Inputs:** Telegram bot + iOS HealthKit

Code entry points:

- Native app: [`kindle/native/src/kindle_dashboard.cpp`](kindle/native/src/kindle_dashboard.cpp)
- Backend functions: [`functions/`](functions/)
- Health companion: [`ios/HealthSyncCompanion/`](ios/HealthSyncCompanion/)
- Owner config template:
  [`kindle/kual/kindle-dashboard/config.sh.example`](kindle/kual/kindle-dashboard/config.sh.example)

### Backend Spine

InsForge handles the cloud layer:

**Postgres Database:** chores, groceries, recipes, meal plans, health summaries,
challenge logs

**Edge functions:** read dashboard data, sync HealthKit, parse Telegram updates,
toggle Kindle tasks, SSE live events

Relevant files:

- Schema:
  [`migrations/001_planner_lists.sql`](migrations/001_planner_lists.sql),
  [`migrations/20260627000000_create-health-daily-summaries.sql`](migrations/20260627000000_create-health-daily-summaries.sql),
  [`migrations/20260629052000_create-recipes.sql`](migrations/20260629052000_create-recipes.sql),
  [`migrations/20260629083000_create-challenge-daily-logs.sql`](migrations/20260629083000_create-challenge-daily-logs.sql),
  [`migrations/20260629162000_create-meal-plan-entries.sql`](migrations/20260629162000_create-meal-plan-entries.sql)
- Dashboard read endpoint:
  [`functions/kindle-dashboard-data.ts`](functions/kindle-dashboard-data.ts)
- Toggle endpoint:
  [`functions/kindle-dashboard-toggle.ts`](functions/kindle-dashboard-toggle.ts)
- Live event endpoint:
  [`functions/kindle-dashboard-events.ts`](functions/kindle-dashboard-events.ts)
- Telegram webhook:
  [`functions/telegram-webhook.ts`](functions/telegram-webhook.ts)
- Health sync endpoint:
  [`functions/health-sync.ts`](functions/health-sync.ts)

The dashboard read endpoint builds a compact payload and hashes the visible
state into a version:

```ts
const payload = {
  ...payloadWithoutVersion,
  version: hashText(JSON.stringify({
    health: payloadWithoutVersion.health,
    challenge: payloadWithoutVersion.challenge,
    lists: payloadWithoutVersion.lists,
    meal_plan: payloadWithoutVersion.meal_plan,
    recipes: payloadWithoutVersion.recipes
  }))
};
```

### Telegram Bot

`Add milk to grocery`

Telegram sends a webhook to InsForge.

The webhook checks:
secret header + allowed chat ID

Code:
[`functions/telegram-webhook.ts`](functions/telegram-webhook.ts)

Then it parses my message into a strict action (how on next slide):

```json
{
  "kind": "planner",
  "action": "add",
  "list_key": "grocery",
  "items": ["milk"],
  "all_lists": false
}
```

The webhook gate is deliberately small:

```ts
const receivedSecret = req.headers.get("x-telegram-bot-api-secret-token");
if (receivedSecret !== configuredSecret) {
  return jsonResponse({ ok: false, error: "Unauthorized" }, 401);
}

if (chatId !== allowedChatId) {
  return jsonResponse(