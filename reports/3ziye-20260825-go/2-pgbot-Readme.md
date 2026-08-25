
<h1 align="center">pgbot</h1>

<p align="center">
  <strong>In-database observability for PostgreSQL.</strong><br>
  One static binary connects read-only, reads Postgres's own statistics views,
  and prints a findings-first health report — plus what changed since last time.<br>
  No agent, no external service, no write privilege anywhere in the path.
</p>

<p align="center">
  <a href="https://github.com/pgrundev/pgbot/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/pgrundev/pgbot/actions/workflows/ci.yml/badge.svg"></a>
  <a href="https://github.com/pgrundev/pgbot/releases/latest"><img alt="Release" src="https://img.shields.io/github/v/release/pgrundev/pgbot"></a>
  <a href="https://pkg.go.dev/github.com/pgrundev/pgbot"><img alt="Go Reference" src="https://pkg.go.dev/badge/github.com/pgrundev/pgbot.svg"></a>
  <a href="https://goreportcard.com/report/github.com/pgrundev/pgbot"><img alt="Go Report Card" src="https://goreportcard.com/badge/github.com/pgrundev/pgbot"></a>
  <a href="LICENSE"><img alt="License: Apache-2.0" src="https://img.shields.io/badge/license-Apache--2.0-blue"></a>
  <img alt="PostgreSQL 14–18" src="https://img.shields.io/badge/postgres-14%E2%80%9318-336791">
</p>

<p align="center">
  <a href="#quickstart">Quickstart</a> ·
  <a href="#install">Install</a> ·
  <a href="#setup--a-read-only-role-with-pg_monitor">Setup</a> ·
  <a href="#commands-and-flags">Commands</a> ·
  <a href="#ci-integration">CI</a> ·
  <a href="#mcp--use-pgbot-as-an-agent-tool">MCP</a> ·
  <a href="#the---json-contract">JSON contract</a> ·
  <a href="#troubleshooting">Troubleshooting</a> ·
  <a href="docs/providers.md">Provider notes</a>
</p>

> **Status: beta.** The `--json` contract is versioned (currently `1.2.0`, JSON
> Schema published in [`schema/`](schema/)) and breaking changes to it are
> treated as breaking changes to the tool. The human-readable report is **not**
> a stable interface — parse `--json`, not the terminal output.

---

## Quickstart

![pgbot inspect — a read-only vital-signs read: headline gauges with a status, then the checks that came back clean](docs/img/dashboard.png)

```sh
curl -fsSL https://pgbot.dev/install | sh
pgbot inspect "postgres://pgbot_ro@host:5432/db"
```

Or set the connection once in the environment and drop the argument — handy for
CI and shells, and it keeps the password out of your history and `ps`:

```sh
export DATABASE_URL="postgres://pgbot_ro@host:5432/db"
pgbot inspect
```

pgbot reads the argument first, then `$DATABASE_URL`, then `$PGBOT_DATABASE_URL`.
(Shell note: `export DATABASE_URL="…"` — no `$` on the left, no spaces around `=`.)

Everything pgbot takes from the environment fits in one block — the connection,
and (only if you want the optional `ask`/`explain` AI layer) one model key:

```sh
export DATABASE_URL="postgres://pgbot_ro:…@host:5432/db?sslmode=require"

# optional, for `pgbot ask` / `pgbot explain` — one of:
export OPENAI_API_KEY=sk-…        # → OpenAI (gpt-4o-mini by default)
export GEMINI_API_KEY=…           # → Google Gemini (AI Studio key)
```

Everything else — `inspect`, `queries`, `indexes`, MCP, CI — is fully
deterministic and needs **no key**; nothing leaves your machine. Provider
pinning and model/endpoint overrides: [the AI layer](#explain--optional-ai-layer).

```
connected · db.example.com · postgres 17.4 · read-only · 6h20m window

Database health: 82/100

CRITICAL
● transaction-id age 1.8B — 84% toward wraparound

WARNING
● orders queries 3.2× slower (8 → 26 ms mean)
● 3 unused indexes consume 18 GB
● connection usage reached 87%

GOOD
● cache hit ratio 99.4%
● replication healthy
● no deadlocks

Details: pgbot inspect --full   ·   Machine-readable: --json
Ask it: pgbot ask "what's wrong?"
```

The default report is a **graded read**: a health score, findings bucketed
CRITICAL / WARNING / NOTE, then a GOOD list naming the healthy subsystems with
their values (a tool that names what it verified reads like a colleague who
looked, not an alarm). `pgbot inspect --full` adds a subsystem status board plus
the section tables and per-finding caveats; focused commands (`indexes`,
`queries`, `tables`, `vacuum`) each drill into one signal; `pgbot ask "…"` and
`pgbot explain` put a plain-language AI reading on top of the same findings.
`--json` is the complete, versioned contract for agents and scripts.

```
$ pgbot ask "what's wrong?"

Your database is mostly healthy.

1 critical issue:
orders queries became 3.2× slower in the last 6 hours.

Likely cause:
sequential scans increased after the orders table grew 18%.

Recommended:
review an index on customer_id + created_at.
```

## Why pgbot

| | |
|---|---|
| **Read-only by role, not by flag** | The guarantee is a `pg_monitor` login role with no write grants. Session pinning (`default_transaction_read_only`, `statement_timeout=15s`, `lock_timeout=2s`) and `BEGIN READ ONLY` are defence in depth on top of it. |
| **It remembers** | Every run writes a local baseline, so from the third