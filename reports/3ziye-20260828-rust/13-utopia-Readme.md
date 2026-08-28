<div align="center">

# Utopia

**The living memory of your organization.**

Open-source, self-hosted knowledge platform: RAG over your own documents, on top of a knowledge graph that remembers *when* each fact was true.

[Quick start](#quick-start) · [Features](#features) · [Configuration](#configuration) · [Roadmap](#roadmap) · [中文](README.zh-CN.md)

[![CI](https://github.com/deeplethe/utopia/actions/workflows/ci.yml/badge.svg)](https://github.com/deeplethe/utopia/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

</div>

---

Most knowledge bases answer *what*. Utopia is built around *when*.

- **"Who owned project X in Q3 2024?"** — every fact carries a validity interval, so the graph can be read as of any moment.
- **"When did this policy change, and what did it say before?"** — facts are append-only. A correction closes the previous version instead of overwriting it, so history stays replayable.
- **Drag the timeline** on the graph page and watch the neighborhood redraw itself at that point in time.

Every edge links back to the sentence it came from. Nothing enters the graph without evidence.

One binary and one Postgres. No Elasticsearch, no vector service, no message queue.

## Features

**Ingest** — PDF, DOCX, PPTX, XLSX/XLS/ODS, CSV/TSV, Markdown, HTML and plain text, with encoding detection for Chinese sources. Web pages and RSS feeds sync on a cron. Push documents from anywhere with a per-source ingest token. Failed parses can be reprocessed in place without re-uploading.

**Search and chat** — Hybrid retrieval: Tantivy full-text (jieba tokenizer for Chinese) and pgvector embeddings, fused with reciprocal rank fusion. Streaming answers carry inline citations that jump to the exact passage. Any OpenAI-compatible endpoint works — DeepSeek, Qwen, GLM, Ollama, vLLM — so the whole stack can run on an air-gapped network.

**Knowledge graph** — LLM extraction of entities and facts against an ontology you can edit. Three-stage entity resolution with a merge log where every merge is reversible. Each fact stores `valid_from` / `valid_to` plus evidence rows pointing back to the source chunk.

**Review queue** — Low-confidence extractions, merge candidates and cardinality conflicts land in a queue rather than interrupting anyone. Confirm, reject or close a fact by hand; the decision is recorded.

**Ask your database** — Register a Postgres connection once at the system level, mount it on a knowledge base, and chat can query it alongside the documents.

**Multi-tenant** — Organizations → workspaces → knowledge bases, with per-KB membership, role-based access and an audit trail.

## Quick start

Requirements: Docker (or Rust 1.85+, Node 20+ and pnpm for local development).

```bash
git clone https://github.com/deeplethe/utopia.git
cd utopia
docker compose --profile app up -d
```

Open http://localhost:8080 and register — the first account becomes the administrator. Then add an OpenAI-compatible endpoint under Settings, create a knowledge base, and drop in some files.

That pulls a prebuilt image from `ghcr.io/deeplethe/utopia`. Uploaded files and the search index live in `./data`, so back that up alongside the database. To build from source instead — after changing code, or to run an unreleased revision:

```bash
docker compose -f docker-compose.yml -f docker-compose.build.yml --profile app up -d --build
```

### Local development

```bash
# 1. Postgres with pgvector
docker compose up -d db

# 2. Backend on :8080 — runs migrations on startup
cargo run -p utopia-server

# 3. Frontend on :5173, proxying /api to the backend
cd web && pnpm install && pnpm dev
```

## Configuration

Everything is an environment variable prefixed with `UTOPIA_`; copy [.env.example](.env.example) to `.env` to get started.

| Variable | Default | Purpose |
|---|---|---|
| `UTOPIA_DATABASE_URL` | `postgres://utopia:utopia@localhost:5432/utopia` | Postgres connection string |
| `UTOPIA_BIND_ADDR` | `0.0.0.0:8080` | Listen address |
| `UTOPIA_JWT_SECRET` | `dev-secret-change-me` | **Change this in production** |
| `UTOPIA_WEB_DIST` | `web/dist` | Built frontend; served as an SPA when present |
| `UTOPIA_DATA_DIR` | `data` | Original files and the full-text index |
| `UTOPIA_OPEN_REGISTRATION` | `true` | When false, only the first account may self-register |

LLM endpoints, models and API keys are configured in the UI, not through environment variables.

## Architecture

```
React + Vite + Tailwind + TanStack
              │  /api/v1
        ┌─────┴─────┐
        │  axum     │  utopia-server   HTTP, auth, jobs
        └─────┬─────┘
   ┌──────────┼──────────┬────────────┐
utopia-ingest  utopia-search  utopia-extract  utopia-llm
 parse/chunk    tantivy+RRF    entities/facts   OpenAI-compatible
   └──────────┴──────────┴────────────┘
                   utopia-store
                        │
              PostgreSQL + pgvector
```

Rust (axum · sqlx · tokio · tantivy) over PostgreSQL 