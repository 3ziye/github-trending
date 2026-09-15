<p align="center">
  <img src="https://github.com/chrisgreg/boop/raw/main/docs/boop.png" width="160" alt="Boop logo" />

  <h1 align="center">Boop</h1>

<p align="center">
  <img src="https://img.shields.io/github/actions/workflow/status/chrisgreg/boop/ci.yml?branch=main" alt="CI" />
  <img src="https://img.shields.io/github/go-mod/go-version/chrisgreg/boop?filename=server%2Fgo.mod" alt="Go version" />
  <img src="https://img.shields.io/github/license/chrisgreg/boop" alt="License" />
</p>

A tiny, self-hosted notification inbox for developers. Something happened in one of your apps; Boop tells you on your phone.

One Go binary, one SQLite file, one Docker container. Pushes go straight from your server to Apple's APNs. There is no hosted relay, account system, or telemetry.

</p>

```bash
curl https://boop.example.com/api/v1/events \
  -H "Authorization: Bearer $BOOP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"title": "Backup complete", "level": "success"}'
```

## Architecture

<p align="center">
  <img src="docs/architecture.png" width="900" alt="How Boop works: apps POST events to the Go server, which stores them in SQLite and pushes to APNs; the iOS app fetches full detail from the server; the web UI manages projects and shows the pairing QR." />
</p>

Your apps POST events with a project API key. The Go server redacts and stores them in SQLite, then pushes straight to Apple's APNs using your `.p8` key. The push carries only the title, body and event id; the iOS app fetches the full event from your server with its own device credential. The embedded web UI manages projects and devices and shows the pairing QR the phone scans. An interactive version lives in [`docs/architecture/index.html`](docs/architecture/index.html) (open it locally; the source is `boop.architecture.json`).

## What is in the box

| Part | Where |
| --- | --- |
| Go server (API, SQLite, APNs, embedded web UI) | `server/` |
| Web UI (Svelte, built into the binary) | `server/web/` |
| iOS app (SwiftUI, iOS 26, you build and sign it) + notification service extension | `ios/` — see [ios/README.md](ios/README.md) |
| Client libraries | separate repos — see [Integrations](#integrations) |
| Native desktop client | planned |

## Quick start (Docker)

```bash
git clone https://github.com/chrisgreg/boop && cd boop
cp .env.example .env          # optional: BOOP_BASE_URL and APNS_* values
mkdir -p data && chown 1000:1000 data   # Linux hosts only; the container runs as uid 1000
docker compose up -d --build
open http://localhost:8080
```

The first visit opens a setup wizard: server check, APNs, pairing, first project, test notification. APNs credentials are optional; without them events are stored and shown in the UI but pushes are skipped, and the settings page says so.

Data lives in `./data/boop.db`. Back up by copying that file (use `sqlite3 data/boop.db ".backup backup.db"` for a consistent copy while running). Back up your `.p8` key separately.

## Quick start (binary)

Every [release](https://github.com/chrisgreg/boop/releases) ships a static, dependency-free binary for Linux, macOS and Windows (amd64 and arm64) with the web UI embedded. Download the archive for your platform, verify it against `checksums.txt` if you like, and run:

```bash
tar xzf boop_*_linux_amd64.tar.gz && cd boop_*_linux_amd64
BOOP_DATABASE_PATH=./boop.db ./boop     # listens on :8080
```

Configuration is the same set of environment variables as Docker (see [Configuration](#configuration)). `BOOP_DATABASE_PATH` defaults to `/data/boop.db`, so set it to somewhere writable.

## Send an event

Create a project in the web UI and copy its API key (shown once). Then:

```bash
# minimum
curl http://localhost:8080/api/v1/events \
  -H "Authorization: Bearer boop_proj_..." -H "Content-Type: application/json" \
  -d '{"title": "Deploy complete"}'

# rich
curl http://localhost:8080/api/v1/events \
  -H "Authorization: Bearer boop_proj_..." -H "Content-Type: application/json" \
  -d '{
    "title": "KeyError", "body": "key :can_palette? not found",
    "level": "error", "source": "error_tracker", "fingerprint": "uini-keyerror",
    "data": {
      "exception": {"type": "KeyError", "message": "key :can_palette? not found"},
      "stacktrace": [{"file": "lib/uini_web/live/widget_settings_live.ex", "line": 49, "function": "handle_event/3", "in_app": true}],
      "tags": {"environment": "production"},
      "context": {"user_id": "123"}
    }
  }'
```

Levels: `info`, `success`, `warning`, `error`, `critical`. Anything in `data` is kept as-is (recognised sections such as `exception`, `stacktrace`, `tags`, `context` and `breadcrumbs` get a nicer rendering) after sensitive keys are redacted.

**Actions.** Up to three buttons that open a URL — on the notification itself (long-press or pull down) and in the event detail:

```bash
curl http://localhost:8080/api/v1/events \
  -H "Authorization: Bearer boop_proj_..." -H "Content-Type: application/json" \
  -d '{"title": "