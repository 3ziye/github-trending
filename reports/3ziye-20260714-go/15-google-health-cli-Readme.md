# ghealth

CLI for the [Google Health API v4](https://developers.google.com/health) — built for AI agents and developers.

- **40 verified data types**: steps, heart rate, exercise, sleep, weight, SpO2, HRV, ECG, blood glucose, nutrition, and more
- **Agent-first**: simplified JSON output, deterministic exit codes, `--dry-run`, `--raw`
- **Single binary**: `go build -o ghealth .`

## Quick Start

```bash
ghealth setup                                              # One-time: GCP project + OAuth
ghealth data steps daily-rollup --from 2026-03-22 --to 2026-03-29  # Weekly step totals
ghealth data heart-rate list --from today --limit 10       # Recent heart rate readings
ghealth schema types                                       # See all available data types
```

## Requirements

Download and Install [Go](https://go.dev/doc/install)

## Installation

```bash
git clone https://github.com/Google-Health-API/google-health-cli.git
cd google-health-cli
go build -o ghealth .
```

## Setup

```bash
ghealth setup
```

Walks you through: GCP project ID, OAuth credentials (download from [Console](https://console.cloud.google.com/apis/credentials) — Desktop application type), Health API enablement, scope selection, and browser-based OAuth login.

Files written under `~/.config/ghealth/` (override with `GHEALTH_CONFIG_DIR`):

- `client_secret.json` — your OAuth client (mode 0600)
- `credentials.json` — access + refresh tokens (mode 0600, plaintext JSON)
- `config.toml` — active profile (project, scopes)

Tokens refresh automatically.

### Non-interactive setup (for agents / CI)

```bash
ghealth setup \
  --project-id my-project \
  --client-secret ~/Downloads/client_secret_123.json \
  --scopes-preset readonly \
  --skip-enable-api \
  --no-prompt
```

Add `--non-interactive-auth` to skip the browser step too — complete later with `ghealth auth login --complete <code>` (see below).

## Authentication

| Scenario | Method |
|----------|--------|
| Interactive | `ghealth setup` or `ghealth auth login` |
| Headless / no browser | `ghealth auth login --non-interactive` → click URL on any device → `ghealth auth login --complete <code>` |
| Move tokens between machines | `ghealth auth export` → `ghealth auth import` |
| Pre-configured token | `export GHEALTH_ACCESS_TOKEN=ya29...` |
| Credential file | `export GHEALTH_CREDENTIALS_FILE=/path/to/creds.json` |
| GCP environment | Application Default Credentials (automatic) |

Precedence: `GHEALTH_ACCESS_TOKEN` > `GHEALTH_CREDENTIALS_FILE` > stored credentials > ADC.

### Headless OAuth flow

```bash
# 1. On the host running ghealth:
ghealth auth login --non-interactive --scopes-preset readonly
# → JSON with auth_url (PKCE S256 challenge + random state baked in)
#   and a complete_command. pending_auth.json holds the verifier locally.

# 2. Open auth_url in any browser, click "Allow".
#    The browser will redirect to a localhost URL that fails to load — expected.
#    Copy either the full redirected URL or just the 'code' query parameter.

# 3. Back on the ghealth host (both forms work):
ghealth auth login --complete 'http://localhost/?code=4/0AX4XfWh...&state=cQq...'
ghealth auth login --complete 4/0AX4XfWh...
# → state validated, PKCE verifier sent on exchange, tokens persisted.
```

State mismatch (URL paste with the wrong `state` parameter) clears the pending flow and returns exit 2. The bare-code form skips state validation but still consumes the pending file, so a stale flow can't be replayed.

### Move tokens between machines

```bash
# source (already authenticated):
ghealth auth export > /tmp/ghealth-creds.json
scp /tmp/ghealth-creds.json target:

# target (also needs client_secret.json — either run 'ghealth setup --non-interactive-auth' or copy it):
ghealth auth import --file /tmp/ghealth-creds.json
```

### Bootstrap from a fresh machine (no client_secret yet)

When no OAuth `client_secret.json` is configured, every auth command returns a
structured error with a `next_steps` array — the same six steps every time —
so an agent can relay it to a user verbatim without scraping prose:

```bash
ghealth auth login
# → exit 5, JSON on stderr:
# {
#   "error": {
#     "type": "config", "code": 5,
#     "message": "No OAuth client_secret.json configured",
#     "hint":    "Run 'ghealth setup' to create or import OAuth credentials",
#     "next_steps": [
#       "Open https://console.cloud.google.com/apis/credentials",
#       "Create or select a Google Cloud project",
#       "Enable the Google Health API (...)",
#       "Create OAuth client ID with Application type: Desktop app",
#       "Download the client_secret JSON",
#       "Run: ghealth setup --client-secret /path/to/client_secret.json"
#     ]
#   }
# }
```

Same `next_steps` are emitted by:

- `ghealth auth login` (interactive / `--non-interactive` / `--complete`)
- `ghealth auth status` when neither stored creds nor env creds are present
- `ghealth auth refresh`, `ghealth auth export` (when nothing to refresh/export)
- `