# br/acc open graph

[![WTG Header](docs/brand/bracc-header.jpg)](docs/brand/bracc-header.jpg)

[English](README.md) | [Portugues](docs/pt-BR/README.md)

**Open-source graph infrastructure that cross-references Brazil's public databases to generate actionable intelligence for civic improvement.**

[![CI](https://github.com/World-Open-Graph/br-acc/actions/workflows/ci.yml/badge.svg)](https://github.com/World-Open-Graph/br-acc/actions/workflows/ci.yml)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Last Commit](https://img.shields.io/github/last-commit/World-Open-Graph/br-acc)](https://github.com/World-Open-Graph/br-acc/commits)
[![Issues](https://img.shields.io/github/issues/World-Open-Graph/br-acc)](https://github.com/World-Open-Graph/br-acc/issues)
[![Stars](https://img.shields.io/github/stars/World-Open-Graph/br-acc?style=social)](https://github.com/World-Open-Graph/br-acc/stargazers)
[![Forks](https://img.shields.io/github/forks/World-Open-Graph/br-acc?style=social)](https://github.com/World-Open-Graph/br-acc/network/members)
[![Twitter Follow](https://img.shields.io/twitter/follow/brunoclz?style=social)](https://x.com/brunoclz)
[![Discord](https://img.shields.io/badge/Discord-Join%20us-5865F2?logo=discord&logoColor=white)](https://discord.gg/YyvGGgNGVD)

[Discord](https://discord.gg/YyvGGgNGVD) | [Twitter](https://x.com/brunoclz) | [Website](https://bracc.org) | [Contributing](#contributing)

---

## What is br/acc?

br/acc is a decentralized movement of Brazilian builders using technology and open data to make public information more accessible. This repository is one of its projects: an open-source graph infrastructure that ingests official Brazilian public databases — company registries, health records, education metrics, employment data, public finances, procurement, environment — and normalizes them into a single queryable graph.

It makes public data that is already open but scattered across dozens of portals accessible in one place. It does not interpret, score, or rank results — it surfaces connections and lets users draw their own conclusions.

[Learn more at bracc.org](https://bracc.org)

---

## Features

- **45 implemented ETL pipeline modules** — status is tracked in `docs/source_registry_br_v1.csv` (loaded/partial/stale/blocked/not_built)
- **Neo4j graph infrastructure** — schema, loaders, and query surface for normalized entities and relationships
- **React frontend** — search, explore corporate networks, and analyze entity connections
- **Public API** — programmatic access to graph data via FastAPI
- **Reproducibility tooling** — one-command local bootstrap plus BYO-data ETL workflow
- **Privacy-first** — LGPD compliant, public-safe defaults, no personal data exposure

---

## Quick Start

```bash
cp .env.example .env
docker compose up -d --build
bash infra/scripts/seed-dev.sh
```

This flow starts the Docker stack from the repository root and then loads deterministic development seed data into Neo4j.

Verify with:

- API: http://localhost:8000/health
- API Docs: http://localhost:8000/docs
- Frontend: http://localhost:3000
- Neo4j Browser: http://localhost:7474

### Starting with Docker

You can start the stack (Neo4j, API, frontend) with Docker Compose without running the full bootstrap:

```bash
cp .env.example .env
docker compose up -d
```

Optional: include the ETL service (for running pipelines in a container):

```bash
docker compose --profile etl up -d
```

Same verification URLs apply. For a ready-to-use demo graph with seed data, use `make bootstrap-demo` instead.

---

## One-Command Flow

```bash
# Start all core services (Neo4j + API + Frontend)
docker compose up -d --build

# Load deterministic demo seed
bash infra/scripts/seed-dev.sh

# Include ETL service when needed
docker compose --profile etl up -d --build

# Stop stack
docker compose down

# Heavy full ingestion orchestration (all implemented pipelines)
make bootstrap-all

# Noninteractive heavy run (automation)
make bootstrap-all-noninteractive

# Print latest bootstrap-all report
make bootstrap-all-report
```

`make bootstrap-all` is intentionally heavy:
- full historical default ingestion target
- can take hours (or longer) depending on source availability
- requires substantial disk, memory, and network bandwidth
- continues on errors and writes auditable per-source status summary under `audit-results/bootstrap-all/`

Detailed guide: [`docs/bootstrap_all.md`](docs/bootstrap_all.md)

---

## What Is Included In This Public Repo

- API, frontend, ETL framework, and infrastructure code.
- Source registry and pipeline status documentation.
- Synthetic demo dataset and deterministic local seed path.
- Public safety/compliance gates and release governance docs.

## What Is Not Included By Default

- A pre-populated production Neo4j dump.
- Guaranteed uptime/stability of every third-party public portal.
- Institutional/private modules and operational 