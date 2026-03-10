# discrawl 🛰️ — Mirror Discord into SQLite; search server history locally

`discrawl` mirrors Discord guild data into local SQLite so you can search, inspect, and query server history without depending on Discord search.

It is a bot-token crawler. No user-token hacks. Data stays local.

## What It Does

- discovers every guild the configured bot can access
- syncs channels, threads, members, and message history into SQLite
- maintains FTS5 search indexes for fast local text search
- extracts small text-like attachments into the local search index
- records structured user and role mentions for direct querying
- tails Gateway events for live updates, with periodic repair syncs
- exposes read-only SQL for ad hoc analysis
- keeps schema multi-guild ready while preserving a simple single-guild default UX

Search defaults to all guilds. `sync` and `tail` default to the configured default guild when one exists, otherwise they fan out to all discovered guilds.

## Requirements

- Go `1.26+`
- a Discord bot token the bot can use to read the target guilds
- bot permissions for the channels you want archived

### Discord Bot Setup

`discrawl` needs a real bot token. Not a user token.

Minimum practical setup:

1. Create or reuse a Discord application in the Discord developer portal.
2. Add a bot user to that application.
3. Invite the bot to the target guilds.
4. Enable these intents for the bot:
   - `Server Members Intent`
   - `Message Content Intent`
5. Ensure the bot can at least:
   - view channels
   - read message history

Without those intents/permissions, `sync`, `tail`, member snapshots, or message content archiving will be partial or fail.

### Bot Token Sources

Token resolution:

1. OpenClaw config, if `discord.token_source` is not `env`
2. `DISCORD_BOT_TOKEN` or the configured `discord.token_env`

`discrawl` accepts either raw token text or a value prefixed with `Bot `. It normalizes that automatically.

Fastest env-only path:

```bash
export DISCORD_BOT_TOKEN="your-bot-token"
bin/discrawl doctor
bin/discrawl init
```

If you keep shell secrets in `~/.profile`, add:

```bash
export DISCORD_BOT_TOKEN="your-bot-token"
```

Then reload your shell before running `discrawl`.

If you already use OpenClaw, `discrawl` can reuse the Discord token from `~/.openclaw/openclaw.json` by default.

Default runtime paths:

- config: `~/.discrawl/config.toml`
- database: `~/.discrawl/discrawl.db`
- cache: `~/.discrawl/cache/`
- logs: `~/.discrawl/logs/`

## Install

Build from source:

```bash
git clone https://github.com/steipete/discrawl.git
cd discrawl
go build -o bin/discrawl ./cmd/discrawl
./bin/discrawl --version
```

Homebrew tap:

```bash
brew tap steipete/tap
brew install steipete/tap/discrawl
```

## Quick Start

Reuse an existing OpenClaw Discord bot config:

```bash
bin/discrawl init --from-openclaw ~/.openclaw/openclaw.json
bin/discrawl doctor
bin/discrawl sync --full
bin/discrawl search "panic: nil pointer"
bin/discrawl tail
```

Env-only setup:

```bash
export DISCORD_BOT_TOKEN="..."
bin/discrawl doctor
bin/discrawl init
bin/discrawl sync --full
```

`init` discovers accessible guilds and writes `~/.discrawl/config.toml`. If exactly one guild is available, that guild becomes the default automatically.

`doctor` is the fastest sanity check:

- confirms config can be loaded
- shows where the token was resolved from
- verifies bot auth
- shows how many guilds the bot can access
- verifies DB + FTS wiring

## Commands

### `init`

Creates the local config and discovers accessible guilds.

```bash
bin/discrawl init
bin/discrawl init --from-openclaw ~/.openclaw/openclaw.json
bin/discrawl init --guild 123456789012345678
bin/discrawl init --db ~/data/discrawl.db
```

### `sync`

Backfills guild state into SQLite.

```bash
bin/discrawl sync --full
bin/discrawl sync --guild 123456789012345678
bin/discrawl sync --guilds 123,456 --concurrency 8
bin/discrawl sync --channels 111,222 --since 2026-03-01T00:00:00Z
```

`sync` already uses parallel channel workers. `--concurrency` overrides the default, and the default is auto-sized from `GOMAXPROCS` with a floor of `8` and a cap of `32`.
When `--channels` includes a forum channel id, `discrawl` expands that forum's threads and syncs their messages as part of the targeted run.

### `tail`

Runs the live Gateway tail and periodic repair loop.

```bash
bin/discrawl tail
bin/discrawl tail --guild 123456789012345678
bin/discrawl tail --repair-every 30m
```

### `search`

Runs FTS search over archived messages.

```bash
bin/discrawl search "panic: nil pointer"
bin/discrawl search --guild 123456789012345678 "payment failed"
bin/discrawl search --channel billing --author steipete --limit 50 "invoice"
bin/discrawl search --include-empty "GitHub"
bin/discrawl --json search "websocket closed"
```

By default, `search` skips rows with no searchable content. Attachment text, attachment filenames, embeds, and replies still count as content. Use `--include-empty` to opt back in.

### `