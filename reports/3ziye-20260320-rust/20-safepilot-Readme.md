# SafePilot

[![Lint](https://github.com/3DCF-Labs/safepilot/actions/workflows/lint.yml/badge.svg)](https://github.com/3DCF-Labs/safepilot/actions/workflows/lint.yml)
[![Test](https://github.com/3DCF-Labs/safepilot/actions/workflows/ci.yml/badge.svg)](https://github.com/3DCF-Labs/safepilot/actions/workflows/ci.yml)
[![Audit](https://github.com/3DCF-Labs/safepilot/actions/workflows/audit.yml/badge.svg)](https://github.com/3DCF-Labs/safepilot/actions/workflows/audit.yml)
[![Docker](https://github.com/3DCF-Labs/safepilot/actions/workflows/docker.yml/badge.svg)](https://github.com/3DCF-Labs/safepilot/actions/workflows/docker.yml)
[![Latest Release](https://img.shields.io/github/v/release/3DCF-Labs/safepilot?display_name=tag)](https://github.com/3DCF-Labs/safepilot/releases/latest)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)


**SafePilot** - a self-hosted AI assistant that executes real work, safely. It turns messages into executable automation runs with SQLite persistence, job execution, [3DCF context compression](https://github.com/3DCF-Labs/doc2dataset), and integrations (Slack/GitHub/Notion/Linear/Jira/Todoist/Weather/Brave Search/Telegram/etc).

> [Configuration guide for begginers](https://safepilot.dev/#configuration-guide)

## Features
- Role-aware Telegram interface with owner/admin/public access. `ALLOWED_USER_ID` bootstraps the owner user, while public channels can be bound to workspace-scoped runtimes.
- Workspace-first UX for create/switch/configure/connect flows (`/ws`, `/wscurrent`, `/wslist`, `/wsnew`, `/wsuse`, `/wsconfig`, `/wspublic`, `/wscaps`).
- Public runtime bindings per integration target (`/bind`, `/unbind`, `/bindings`, `/bindpolicy`) with capability and policy enforcement.
- Inline approval buttons for blocked tasks (callback queries), plus simple natural-language approval for the single blocked task (`"yes"`, `"approve"`, `"go ahead"`, etc).
- Persistent context in SQLite (messages + summaries) with optional 3DCF compression.
  - Recommended: enable [3DCF compression](https://github.com/3DCF-Labs/doc2dataset) in production to reduce prompt size and improve long-run behavior.
- Multiple LLM modes:
  - `LLM_MODE=direct`: uses Anthropic/OpenAI HTTP APIs to produce `{reply, actions}`.
  - `LLM_MODE=agent`: iterative tool-calling loop with per-run checkpoints. Safe tool calls execute inline; risky tool calls are converted into Run Tasks (and may require approval).
- Run scheduler with checkpoints:
  - Each message in `direct` creates (or continues) a **Run** (tasks + deps).
  - Safe tasks are queued as **Jobs** automatically.
  - Risky tasks are blocked until you approve them (or you enable a temporary bypass window).
- Workspace continuity:
  - Each run executes in its assigned workspace path (stored on the run, typically under `DATA_DIR/chats/<chat_id>/<workspace_name>`).
- Safer execution defaults:
  - `shell`/`validate` actions require an allowlisted bare binary name and refuse `bash`/`sh` (supports a separate unsafe allowlist).
  - `fetch` is SSRF-protected by default (blocks private/loopback/link-local/metadata IPs) and pins DNS resolution to validated IPs for the request.
  - Agent-mode write tools are disabled by default.
  - Subprocesses run with a cleared environment (no inherited API keys/tokens), and a minimal `PATH`.

## Architecture

At a high level:
- Telegram chat messages create or continue a durable **Run** (stored in SQLite).
- Each run contains a DAG of **Tasks** (planned actions) with explicit dependencies.
- Eligible tasks execute as **Jobs**. Jobs run in the workspace attached to the run.
- A policy layer classifies tasks into `safe`, `needs_approval`, or `dangerous` and enforces
  checkpoints before execution.

Details: [`docs/architecture.md`](docs/architecture.md).

## Security At A Glance

SafePilot uses checkpointed execution plus defense-in-depth:
- Explicit checkpoints: `/approve`, `/trusted`, `/unsafe`
- Network controls: SSRF protection for `fetch` by default
- Workspace network policy: trusted-domain allowlist mode (`trusted_only`) blocks web access outside configured domains
- Process controls: cleared subprocess env + minimal `PATH` (`TG_ORCH_SAFE_PATH`)
- Optional Linux sandboxing for dangerous jobs (`TG_ORCH_DANGEROUS_SANDBOX*`)

Security docs:
- Model and checkpoint behavior: [`docs/security-model.md`](docs/security-model.md)
- Host hardening: [`docs/hardening.md`](docs/hardening.md)
- Docker hardening/deploy: [`docs/docker.md`](docs/docker.md)
- Security docs index: [`docs/security/README.md`](docs/security/README.md)

## Recommended Security Configuration

Baseline:
- Run in Docker using [`docker-compose.yml`](docker-compose.yml) (non-root, read-only root filesystem, secrets via files, persistent volumes only for `DATA_DIR` and `LOG_DIR`).
- Keep `LLM_MODE=direct` unless you specifically need `LLM_MODE=agent`.
- Keep `AGENT_ENABLE_WRITE_TOOLS=0` and `AGENT_ENABLE_BROWSER_TOOL=0` unless you explicitl