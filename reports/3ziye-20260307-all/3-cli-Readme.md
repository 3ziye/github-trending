<h1 align="center">gws</h1>

**One CLI for all of Google Workspace — built for humans and AI agents.**<br>
Drive, Gmail, Calendar, and every Workspace API. Zero boilerplate. Structured JSON output. 40+ agent skills included.

> [!IMPORTANT]
> Temporarily disabling non-collaborator pull requests. See this discussion, https://github.com/googleworkspace/cli/discussions/249.

> [!NOTE]
> This is **not** an officially supported Google product.

<p>
  <a href="https://www.npmjs.com/package/@googleworkspace/cli"><img src="https://img.shields.io/npm/v/@googleworkspace/cli" alt="npm version"></a>
  <a href="https://github.com/googleworkspace/cli/blob/main/LICENSE"><img src="https://img.shields.io/github/license/googleworkspace/cli" alt="license"></a>
  <a href="https://github.com/googleworkspace/cli/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/googleworkspace/cli/ci.yml?branch=main&label=CI" alt="CI status"></a>
  <a href="https://www.npmjs.com/package/@googleworkspace/cli"><img src="https://img.shields.io/npm/unpacked-size/@googleworkspace/cli" alt="install size"></a>
</p>
<br>

```bash
npm install -g @googleworkspace/cli
```

`gws` doesn't ship a static list of commands. It reads Google's own [Discovery Service](https://developers.google.com/discovery) at runtime and builds its entire command surface dynamically. When Google Workspace adds an API endpoint or method, `gws` picks it up automatically.

> [!IMPORTANT]
> This project is under active development. Expect breaking changes as we march toward v1.0.

## Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Why gws?](#why-gws)
- [Authentication](#authentication)
- [AI Agent Skills](#ai-agent-skills)
- [Advanced Usage](#advanced-usage)
- [Environment Variables](#environment-variables)
- [Architecture](#architecture)
- [Troubleshooting](#troubleshooting)
- [Development](#development)

## Prerequisites

- **Node.js 18+** — for `npm install` (or download a pre-built binary from [GitHub Releases](https://github.com/googleworkspace/cli/releases))
- **A Google Cloud project** — required for OAuth credentials. You can create one via the [Google Cloud Console](https://console.cloud.google.com/) or with the [`gcloud` CLI](https://cloud.google.com/sdk/docs/install) or with the `gws auth setup` command.
- **A Google account** with access to Google Workspace

## Installation

```bash
npm install -g @googleworkspace/cli
```

> The npm package bundles pre-built native binaries for your OS and architecture.
> No Rust toolchain required.

Pre-built binaries are also available on the [GitHub Releases](https://github.com/googleworkspace/cli/releases) page.

Or build from source:

```bash
cargo install --git https://github.com/googleworkspace/cli --locked
```

A Nix flake is also available at `github:googleworkspace/cli`

```bash
nix run github:googleworkspace/cli
```

## Quick Start

```bash
gws auth setup     # walks you through Google Cloud project config
gws auth login     # subsequent OAuth login
gws drive files list --params '{"pageSize": 5}'
```

## Why gws?

**For humans** — stop writing `curl` calls against REST docs. `gws` gives you `--help` on every resource, `--dry-run` to preview requests, and auto‑pagination.

**For AI agents** — every response is structured JSON. Pair it with the included agent skills and your LLM can manage Workspace without custom tooling.

```bash
# List the 10 most recent files
gws drive files list --params '{"pageSize": 10}'

# Create a spreadsheet
gws sheets spreadsheets create --json '{"properties": {"title": "Q1 Budget"}}'

# Send a Chat message
gws chat spaces messages create \
  --params '{"parent": "spaces/xyz"}' \
  --json '{"text": "Deploy complete."}' \
  --dry-run

# Introspect any method's request/response schema
gws schema drive.files.list

# Stream paginated results as NDJSON
gws drive files list --params '{"pageSize": 100}' --page-all | jq -r '.files[].name'
```

## Authentication

The CLI supports multiple auth workflows so it works on your laptop, in CI, and on a server.

### Which setup should I use?

| I have… | Use |
|---|---|
| `gcloud` installed and authenticated | [`gws auth setup`](#interactive-local-desktop) (fastest) |
| A GCP project but no `gcloud` | [Manual OAuth setup](#manual-oauth-setup-google-cloud-console) |
| An existing OAuth access token | [`GOOGLE_WORKSPACE_CLI_TOKEN`](#pre-obtained-access-token) |
| Existing Credentials | [`GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE`](#service-account-server-to-server) |

### Interactive (local desktop)

Credentials are encrypted at rest (AES-256-GCM) with the key stored in your OS keyring.

```bash
gws auth setup       # one-time: creates a Cloud project, enables APIs, logs you in
gws auth login       # subsequent scope selection and login
```

> `gws auth setup` requires the [`gcloud` CLI](https://cloud.google.com/sdk/docs/install). If you don't have `gcloud`, use the [manual 