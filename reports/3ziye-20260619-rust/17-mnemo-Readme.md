# mnemo

> Local-first AI memory layer for any LLM. Persistent knowledge graph,
> entity extraction, semantic retrieval — no cloud required.

![Build Status](https://img.shields.io/github/actions/workflow/status/zaydmulani09/mnemo/ci.yml?branch=main)
![License](https://img.shields.io/badge/license-MIT-blue)
![Crates.io](https://img.shields.io/crates/v/mnemo-core)
![PyPI](https://img.shields.io/pypi/v/mnemo-sdk)
![Docker](https://img.shields.io/docker/pulls/zaydmulani09/mnemo)

---

## What is mnemo?

LLM apps built on custom pipelines have no persistent memory between
sessions. mnemo is a local sidecar that extracts entities, builds a
knowledge graph, and injects scored context back into your prompts —
no cloud, no Python runtime, no vendor lock-in.

mnemo is a sidecar service that watches every conversation you feed it, extracts named entities and relationships using an LLM, builds a persistent knowledge graph in SQLite, and injects relevant context back into future prompts — automatically, in under 50ms. It works with **Ollama** (fully local, free), OpenAI, Anthropic, or any OpenAI-compatible API. It ships as a single static binary with zero cloud dependency.

---

## How it works

```
  your app
     │
     ▼
  POST /ingest ──► entity extraction (LLM) ──► knowledge graph (SQLite + petgraph)
                                                        │
  POST /retrieve ◄── scoring + ranking ◄── graph traversal + full-text search
     │
     ▼
  context_prompt  ──► inject into your LLM prompt
```

1. You POST raw text to `/ingest` (a conversation turn, a document, a note).
2. mnemo sends it to your configured LLM and extracts entities (people, tools, places, concepts) and the relationships between them.
3. Entities are deduplicated by name+type, aliases are merged, and everything is written to SQLite. The in-memory petgraph is updated atomically.
4. On POST `/retrieve`, mnemo runs a 6-stage pipeline: full-text chunk search → entity name search → graph expansion (BFS over the knowledge graph) → relation filter → score+rank → assemble a `context_prompt` string.
5. You inject `context_prompt` into your LLM's system prompt. Done.

---

## Why mnemo

There are a lot of AI memory tools. Here's what makes mnemo different:

| | mnemo | Most alternatives |
|---|---|---|
| **Runtime** | Single Rust binary | Python daemon |
| **Storage** | SQLite, survives restarts | In-memory or cloud |
| **Graph layer** | petgraph, multi-hop traversal | None |
| **Cloud dependency** | Zero | Required or optional |
| **LLM backend** | Any OpenAI-compatible | Often locked to one |
| **Retrieval** | Scored + ranked, graph-expanded | Naive context dump |

**mnemo is not for everyone.** If you're using a managed agent
harness that handles memory for you, you don't need it. mnemo
is for developers building custom LLM pipelines who need
persistent, structured, local memory they fully control.

The graph layer is the real differentiator — entities are
deduplicated across sessions, relationships are weighted and
traversed at query time, and graph-expanded results score at
0.5x so direct matches always rank higher than inferred ones.

---

## Quickstart

### Path A — Docker + Ollama (fully free, recommended)

```bash
git clone https://github.com/zaydmulani09/mnemo
cd mnemo
docker compose up -d

# Pull the llama3 model the first time (~4 GB)
docker exec mnemo-ollama ollama pull llama3

# Verify everything is healthy
curl http://localhost:8080/health
```

### Path B — Binary (Ollama or OpenAI running separately)

```bash
cargo install --path crates/mnemo-api

# With Ollama
export MNEMO_LLM_BASE_URL=http://localhost:11434/v1
mnemo-api

# With OpenAI
export MNEMO_LLM_BASE_URL=https://api.openai.com/v1
export MNEMO_LLM_API_KEY=sk-...
export MNEMO_LLM_MODEL=gpt-4o-mini
export MNEMO_LLM_PROVIDER=openai
mnemo-api
```

### Path C — Python SDK

```bash
pip install mnemo-sdk
```

```python
from mnemo import MnemoClient

client = MnemoClient()  # server at http://localhost:8080

# Store a memory
client.ingest("I'm building a Rust vector database called vecdb")

# Get context for injection into your next LLM prompt
print(client.get_context("what am I working on?"))
```

---

## API Reference

All endpoints accept and return `application/json`. Base URL: `http://localhost:8080`.

| Method | Path | Description | Request body | Response |
|--------|------|-------------|--------------|----------|
| `GET` | `/health` | Server + DB + LLM status | — | `HealthResponse` |
| `POST` | `/ingest` | Store text, extract entities | `IngestRequest` | `IngestResponse` |
| `POST` | `/retrieve` | Retrieve ranked memory context | `RetrievalQuery` | `RetrievalResult` |
| `GET` | `/entities` | List entities (paginated) | `?limit&offset` | `Entity[]` |
| `GET` | `/entities/:id` | Get entity by UUID | — | `Entity` |
| `DELETE` | `/entities/:id` | Delete entity (cascades) | — | `{"deleted":true}` |
| `GET` | `/entities/:id/neighbors` | Knowledge graph neighbors | `?depth` (max 5) | `