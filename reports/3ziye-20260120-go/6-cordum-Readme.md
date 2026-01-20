# Cordum - Deterministic Control Plane for Autonomous Workflows

[![License: BUSL-1.1](https://img.shields.io/badge/license-BUSL--1.1-blue)](LICENSE)
[![Release](https://img.shields.io/github/v/release/cordum-io/cordum?sort=semver)](https://github.com/cordum-io/cordum/releases)
[![Go Version](https://img.shields.io/github/go-mod/go-version/cordum-io/cordum)](go.mod)
[![Docker Compose](https://img.shields.io/badge/compose-ready-0f766e)](docker-compose.yml)
[![Docs](https://img.shields.io/badge/docs-cordum--docs-0ea5e9)](docs/README.md)
![Docker Pulls](https://img.shields.io/docker/pulls/cordum/control-plane)
![CI](https://github.com/cordum-io/cordum/workflows/CI/badge.svg)
![CodeQL](https://github.com/cordum-io/cordum/workflows/CodeQL/badge.svg)
![Coverage Target](https://img.shields.io/badge/coverage-target%2080%25-22c55e)
[![Website](https://img.shields.io/badge/website-cordum.io-blue)](https://cordum.io)
[![WebsiteDocs](https://img.shields.io/badge/docs-cordum.io%2Fdocs-0ea5e9)](https://cordum.io/docs)
[![Discord](https://img.shields.io/badge/discord-join-5865F2?logo=discord&logoColor=white)](https://discord.gg/26yw9VQV)

Cordum (cordum.io) is a platform-only control plane for autonomous AI Agents and external workers.
It uses NATS for the bus, Redis for state and payload pointers, and CAP v2 wire contracts for jobs,
results, and heartbeats. Workers and product packs live outside this repo.

See the full product docs at [Cordum](https://cordum.io) (or the local `docs/README.md`).

## 2-minute guardrails demo

Run the approval + remediation demo (worker + policy gate + approval): `./tools/scripts/demo_guardrails.sh`

Walkthrough + GIF recording steps: `docs/demo-guardrails.md`

## Getting started (1 minute)

![Getting started](docs/assets/getting-started.gif)

Install (one-liner):

```bash
curl -fsSL https://get.cordum.io | sh
# or run locally from a clone:
./tools/scripts/install.sh
```

`get.cordum.io` should serve `tools/scripts/install.sh` from this repo.

1. `go run ./cmd/cordumctl up` (requires Go), or `docker compose build && docker compose up -d`.
2. Open `http://localhost:8082` (dashboard).
3. Run `./tools/scripts/platform_smoke.sh`.

## Feature highlights

- Workflow engine with retries/backoff, approvals, timeouts, delays, and crash-safe state.
- Least-loaded scheduling with capability-aware pool routing.
- Policy-before-dispatch (ALLOW/DENY/REQUIRE_APPROVAL/CONSTRAINTS).
- Pack overlays for workflows, schemas, and policy/config fragments.
- Durable job bus on NATS JetStream with Redis-backed pointers and auditability.
- API + CLI for workflows, runs, policy bundles, schemas, packs, locks, and artifacts.

## Architecture (current code)

Core services:
- API gateway: HTTP/WS + gRPC for jobs, workflows/runs, approvals, config, policy, DLQ, schemas, locks, artifacts, traces, packs.
- Scheduler: safety gate, routing, job state, reconciler timeouts.
- Safety kernel: policy check/evaluate/explain/simulate; file policy + config-service fragments.
- Workflow engine: Redis-backed workflows/runs with fan-out, approvals, retries/backoff, delay/notify/condition steps, reruns, timeline.
- Context engine (optional): gRPC helper for context windows and memory in Redis.
- Dashboard (optional): React UI served via Nginx; connects to `/api/v1` and `/api/v1/stream`.

Control plane flow (simplified):

```
Clients/UI
   |
   v
API Gateway  --->  Redis (runs, jobs, pointers, config, policy, DLQ)
   |
   v
Scheduler  --->  Safety Kernel (policy decision)
   |
   v
NATS (JetStream bus)  --->  External workers (your code)
```

Protocol:
- Bus and safety types are CAP v2 (`github.com/cordum-io/cap/v2`) via aliases in `core/protocol/pb/v1`.
- API/Context protos live in `core/protocol/proto/v1`; generated Go types live in `core/protocol/pb/v1` and `sdk/gen/go/cordum/v1`.

SDK:
- Public Go SDK lives under `sdk/` (module `github.com/cordum/cordum/sdk`), including generated protos,
  a minimal gateway client, and a CAP worker runtime (`sdk/runtime`).

## Why Cordum?

Cordum is built for teams that need deterministic automation and policy control.

| Capability | Cordum | Typical workflow engines |
| --- | --- | --- |
| Policy-before-dispatch | Built-in | External/custom |
| Approval gates | Built-in | Manual |
| Scheduling | Least-loaded + pool routing | Queue-based |
| Pack overlays | Built-in | Plugins/scripts |

## Quickstart (Docker)

Requirements: Docker/Compose, curl, jq. Go is required if you want to use `cordumctl`.

```bash
go run ./cmd/cordumctl up
```

Or manually:

```bash
docker compose build
docker compose up -d
```

For prebuilt images:

```bash
export CORDUM_VERSION=v0.1.1
docker compose -f docker-compose.release.yml pull
docker compose -f docker-compose.release.yml up -d
```

## Kubernetes (Helm)

```bash
helm install cordum ./cordum-helm -n cordum --create-namespace
```

Published chart (when available):

```bash
helm repo add cordum https://charts.cordum.io
helm repo update
helm install cordum cordum/cordum