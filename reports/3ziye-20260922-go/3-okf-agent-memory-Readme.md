# OKF Agent Memory

> **A Domain-Neutral, Git-Native Persistent Project Memory for AI Agents based on the Open Knowledge Format (OKF) v0.2.**

[![Specification](https://img.shields.io/badge/Specification-OKF_v0.2-blue.svg)](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
[![Tooling](https://img.shields.io/badge/Tooling-Go_1.26_%7C_Zero_Deps-00ADD8.svg)](pkg/okf)
[![CI](https://github.com/okf-memory/okf-agent-memory/actions/workflows/ci.yml/badge.svg)](https://github.com/okf-memory/okf-agent-memory/actions/workflows/ci.yml)
[![Trendshift](https://img.shields.io/badge/Trendshift-%232_Go_Trending-ff5722.svg)](https://trendshift.io/repositories/215663)
[![Protocol](https://img.shields.io/badge/MCP-Ready-purple.svg)](cmd/okf)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Sponsor](https://img.shields.io/badge/Sponsor-%E2%9D%A4-ea4aaa.svg)](https://github.com/sponsors/sknr)

---

## 🌟 Overview

Conversations with AI agents reset when context windows close. Valuable architectural decisions, domain discoveries, and operational facts are lost unless stored persistently.

Traditional approaches suffer from two fatal failure modes:
1. **The Prompt Monolith**: Stuffing all domain knowledge and rules into `AGENTS.md` or `CLAUDE.md` creates massive context bloat and causes **attention drift** (agents ignore critical instructions).
2. **The RAG Blindspot**: Dumping behavioral rules into vector databases fails because agents never semantically search for operational constraints (e.g. formatting or security rules) during general tasks.

**OKF Agent Memory** resolves this dilemma with the **Dual-Memory Agent Architecture (DMAA)**:

```mermaid
flowchart TD
    subgraph PUSH["1. Normative Working Memory (Push Layer)"]
        direction TB
        C1["Canonical AGENTS.md (~100-150 tokens)"]
        C2["Domain Codex (Invariants, Ethics, Tone)"]
        C3["OKF Memory Bridge (Deterministic Triggers)"]
        C4["Agent Action Grammar (AAG) Micro-Syntax"]
    end

    subgraph PULL["2. Semantic Domain Memory (Pull Layer)"]
        direction TB
        O1["OKF v0.2 Knowledge Bundle (knowledge/)"]
        O2["0 Tokens baseline in system prompt"]
        O3["Selective Retrieval via okf_search / okf_show"]
        O4["Persistent Graph of Decisions, Facts & Runbooks"]
    end

    INPUT["User Request"] --> PUSH
    PUSH -->|Enforces Domain Codex & Triggers| AGENT["AI Agent (LLM)"]
    AGENT -->|Selective Retrieval| PULL
    PULL -->|Context & Facts| AGENT
    AGENT --> OUTPUT["Deterministic Response"]
```

### The Universal Composition Model

In DMAA, every agent configuration is structured by a universal composition:

$$\text{AGENTS.md} = \underbrace{\text{Domain Codex (AAG)}}_{\text{Project Invariants, Tone, Guardrails}} + \underbrace{\text{OKF Memory Bridge}}_{\text{Standardized Triggers: Search-Before-Write}}$$

* **Layer 1: Normative Working Memory (Push Layer)**: A permanent, ultra-compact behavioral codex (~100–150 tokens) expressed in [**Agent Action Grammar (AAG)**](docs/spec/AGENT_ACTION_GRAMMAR_RFC.md). Loaded at session start, enforcing zero-tolerance invariants.
* **Layer 2: Semantic Domain Memory (Pull Layer)**: An [**OKF v0.2**](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) knowledge bundle (`knowledge/`) that consumes **0 tokens at baseline** and is queried on-demand in microseconds.

```mermaid
flowchart TD
    L1["1. OKF v0.2 Specification<br/>(Normative Markdown & YAML Format)"]
    L2["2. Agent Memory Convention & DMAA<br/>(Dual-Memory Model, Search-Before-Write, Trust)"]
    L3["3. Agent Skill & AAG Codex<br/>(Agent Action Grammar, Workflows, Triggers)"]
    L4["4. Tooling Layer: Go Library & CLI<br/>(Deterministic Parsing, Validation, BM25, MCP)"]
    L5["5. Project Knowledge Corpus<br/>(knowledge/ OKF Bundle)"]

    L1 --> L2
    L2 --> L3
    L3 --> L4
    L4 --> L5
```

---

## ⚡ Key Highlights

* **Dual-Memory Cognitive Architecture (DMAA)**: Separates normative push working memory (`AGENTS.md` codex) from semantic pull domain memory (`knowledge/` bundle), completely eliminating prompt bloat.
* **Agent Action Grammar (AAG)**: Ultra-compact, deterministic ASCII micro-syntax saving **~78–85% tokens** compared to natural language prompt instructions.
* **Blazing Fast Performance (<300µs Search, ~4ms Graph Validation)**: In-memory BM25 retrieval and bundle validation execute in microseconds without VM spin-up or network roundtrips.
* **100% Git-Native & Zero Vendor Lock-in**: Everything is version-controlled plain text. Inspect, audit, and review your agent's memory using standard `git diff` and `git log`. No external database required.
* **Zero API Costs for Memory Retrieval**: Local lexical BM25 indexing eliminates recurring vector embedding API costs and network roundtrips.
* **Built on Google OKF v0.2**: Uses the open standard format for agent knowledge with full support for provenance (`sources`), trust tiers (`gen