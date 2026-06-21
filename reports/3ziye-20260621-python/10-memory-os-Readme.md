# Memory OS — Hermes Agent Memory Operating System

![Memory OS Banner](assets/banner.jpg)

> **Your agent finally stops forgetting.**  \
> Permanent memory. Local memory infrastructure. API-provider agnostic. Surgically token-efficient.

Seven memory layers. Automatic, intelligent context injection. Structured facts with trust scoring. A self-curating wiki pipeline. Semantic search across **every conversation you've ever had**.

Memory OS turns Hermes Agent into a real long-term collaborator — one that remembers your projects, your decisions, your reasoning, and brings exactly the right context back at exactly the right moment. Like talking to a colleague who was there for every session.

**Memory infrastructure runs entirely on your machine. Works with any LLM provider — OpenRouter, OpenAI, Anthropic, Ollama, or local models. No memory subscription. No vendor lock-in.**

---

## What's New in v0.2.0

**One-command install.** `curl -sSL https://raw.githubusercontent.com/ClaudioDrews/memory-os/main/setup.sh | bash` sets up the entire stack — Docker services, SQLite databases, Icarus plugin, environment — in one shot. The 10-step manual guide is now a fallback for troubleshooting.

**Community infrastructure.** Issue templates (bug report + feature request), PR checklist, and contributing guide. Project is ready for external contributors — and already has them.

**20+ fixes from systematic audit.** Community-driven review across setup, configuration, performance, and resilience. Highlights: provider-agnostic LLM extraction, O(1) path lookups, FTS5-powered session search, semantic dedup at scale, and idempotent database initialization.

**Installation verified on real hardware.** Smoke tests and ingestion tests ship with the repo. The automated installer has been tested end-to-end — including on modest machines where Docker build times exposed UX gaps that are now handled gracefully.

---

## The problem every serious Hermes user knows

You spend hours configuring the agent, teaching it your preferences, solving hard problems together — and in the next session it acts like it's meeting you for the first time.

- Repeating context at the start of every conversation
- Losing the thread of important decisions made weeks ago
- Structured facts — your stack, your projects, your patterns — with nowhere to live
- Every memory solution you've tried is either cloud-locked or too shallow to matter

After months of hitting these walls in production, I built something that actually works.

---

## What Memory OS is

Not just another plugin. A complete **memory operating system** — 7 layers working in concert, from flat files to a vector database, with surgical context injection, a knowledge pipeline that organizes itself, **and an explicit Ground Truth hierarchy that tells the agent to actually use the injected memory**.

Designed and refined by someone who ran headfirst into every limitation of stock Hermes and every existing memory solution.

**Requirements:** Hermes Agent + Docker (Qdrant + Redis + ARQ Worker) + Python 3.11+.  
Compatible with any LLM provider Hermes supports — OpenRouter, OpenAI, Anthropic, Ollama, and more.

---

## Architecture: 7 memory layers

```
┌──────────────────────────────────────────────────────────────────┐
│  LAYER 1 · WORKSPACE                                              │
│  MEMORY.md · USER.md · CREATIVE.md                               │
│  → Injected into the system prompt every single turn             │
├──────────────────────────────────────────────────────────────────┤
│  LAYER 2 · SESSIONS                                               │
│  state.db (SQLite + FTS5)                                         │
│  → Full-text search across your entire conversation history       │
├──────────────────────────────────────────────────────────────────┤
│  LAYER 3 · STRUCTURED FACTS                                       │
│  memory_store.db (SQLite + HRR + FTS5 + trust scoring)            │
│  → Durable facts with entity resolution and an automatic          │
│    feedback loop that trains trust scores over time               │
├──────────────────────────────────────────────────────────────────┤
│  LAYER 4 · FABRIC (CROSS-SESSION)                                 │
│  Icarus Plugin (heavily forked)                                   │
│  → LLM-powered session extraction + multi-source injection        │
│  → 16 tools: fabric_recall, fabric_write, fabric_brief, etc.      │
├──────────────────────────────────────────────────────────────────┤
│  LAYER 5 · VECTOR DATABASE                                        │
│  Qdrant (4096d Cosine + BM25 sparse)                              │
│  → 4-level fallback: hybrid → dense → lexical → SQLite            │
│  → Weekly decay scanner + semantic dedup (cosine >0.92 → merge)  │
├──────────────────────────────────────────────────────────────────┤
│  LAYER 6 · LLM WIKI                                               │
│  Auto-curated vault: concepts/ · entitie