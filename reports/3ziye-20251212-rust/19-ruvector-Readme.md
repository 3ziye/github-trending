# RuVector

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Crates.io](https://img.shields.io/crates/v/ruvector-core.svg)](https://crates.io/crates/ruvector-core)
[![postgres](https://img.shields.io/crates/v/ruvector-postgres.svg?label=postgres)](https://crates.io/crates/ruvector-postgres)
[![SONA](https://img.shields.io/crates/v/ruvector-sona.svg?label=sona)](https://crates.io/crates/ruvector-sona)
[![npm](https://img.shields.io/npm/v/ruvector.svg)](https://www.npmjs.com/package/ruvector)
[![@ruvector/sona](https://img.shields.io/npm/v/@ruvector/sona.svg?label=%40ruvector%2Fsona)](https://www.npmjs.com/package/@ruvector/sona)
[![Rust](https://img.shields.io/badge/rust-1.77%2B-orange.svg)](https://www.rust-lang.org)
[![Build](https://img.shields.io/github/actions/workflow/status/ruvnet/ruvector/ci.yml?branch=main)](https://github.com/ruvnet/ruvector/actions)
[![Docs](https://img.shields.io/badge/docs-latest-brightgreen.svg)](./docs/)

**A distributed vector database that learns.** Store embeddings, query with Cypher, scale horizontally with Raft consensus, and let the index improve itself through Graph Neural Networks.

```bash
npx ruvector
```

> **All-in-One Package**: The core `ruvector` package includes everything — vector search, graph queries, GNN layers, distributed clustering, AI routing, and WASM support. No additional packages needed.

## What Problem Does RuVector Solve?

Traditional vector databases just store and search. When you ask "find similar items," they return results but never get smarter. They don't scale horizontally. They can't route AI requests intelligently.

**RuVector is different:**

1. **Store vectors** like any vector DB (embeddings from OpenAI, Cohere, etc.)
2. **Query with Cypher** like Neo4j (`MATCH (a)-[:SIMILAR]->(b) RETURN b`)
3. **The index learns** — GNN layers make search results improve over time
4. **Scale horizontally** — Raft consensus, multi-master replication, auto-sharding
5. **Route AI requests** — Semantic routing and FastGRNN neural inference for LLM optimization
6. **Compress automatically** — 2-32x memory reduction with adaptive tiered compression
7. **39 attention mechanisms** — Flash, linear, graph, hyperbolic for custom models
8. **Drop into Postgres** — pgvector-compatible extension with SIMD acceleration
9. **Run anywhere** — Node.js, browser (WASM), HTTP server, or native Rust
10. **Continuous learning** — SONA enables runtime adaptation with LoRA, EWC++, and ReasoningBank

Think of it as: **Pinecone + Neo4j + PyTorch + postgres + etcd** in one Rust package.



## How the GNN Works

Traditional vector search:
```
Query → HNSW Index → Top K Results
```

RuVector with GNN:
```
Query → HNSW Index → GNN Layer → Enhanced Results
                ↑                      │
                └──── learns from ─────┘
```

The GNN layer:
1. Takes your query and its nearest neighborsa
2. Applies multi-head attention to weigh which neighbors matter
3. Updates representations based on graph structure
4. Returns better-ranked results

Over time, frequently-accessed paths get reinforced, making common queries faster and more accurate.


## Quick Start

### One-Line Install
 

### Node.js / Browser

```bash
# Install
npm install ruvector

# Or try instantly
npx ruvector
```


## Comparison

| Feature | RuVector | Pinecone | Qdrant | Milvus | ChromaDB |
|---------|----------|----------|--------|--------|----------|
| **Latency (p50)** | **61µs** | ~2ms | ~1ms | ~5ms | ~50ms |
| **Memory (1M vec)** | 200MB* | 2GB | 1.5GB | 1GB | 3GB |
| **Graph Queries** | ✅ Cypher | ❌ | ❌ | ❌ | ❌ |
| **Hyperedges** | ✅ | ❌ | ❌ | ❌ | ❌ |
| **Self-Learning (GNN)** | ✅ | ❌ | ❌ | ❌ | ❌ |
| **Runtime Adaptation (SONA)** | ✅ LoRA+EWC++ | ❌ | ❌ | ❌ | ❌ |
| **AI Agent Routing** | ✅ Tiny Dancer | ❌ | ❌ | ❌ | ❌ |
| **Attention Mechanisms** | ✅ 39 types | ❌ | ❌ | ❌ | ❌ |
| **Hyperbolic Embeddings** | ✅ Poincaré | ❌ | ❌ | ❌ | ❌ |
| **PostgreSQL Extension** | ✅ pgvector drop-in | ❌ | ❌ | ❌ | ❌ |
| **SIMD Optimization** | ✅ AVX-512/NEON | Partial | ✅ | ✅ | ❌ |
| **Metadata Filtering** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Sparse Vectors** | ✅ BM25/TF-IDF | ✅ | ✅ | ✅ | ❌ |
| **Raft Consensus** | ✅ | ❌ | ✅ | ❌ | ❌ |
| **Multi-Master Replication** | ✅ | ❌ | ❌ | ✅ | ❌ |
| **Auto-Sharding** | ✅ | ✅ | ✅ | ✅ | ❌ |
| **Auto-Compression** | ✅ 2-32x | ❌ | ❌ | ✅ | ❌ |
| **Snapshots/Backups** | ✅ | ✅ | ✅ | ✅ | ❌ |
| **Browser/WASM** | ✅ | ❌ | ❌ | ❌ | ❌ |
| **Differentiable** | ✅ | ❌ | ❌ | ❌ | ❌ |
| **Multi-Tenancy** | ✅ Collections | ✅ | ✅ | ✅ | ✅ |
| **Open Source** | ✅ MIT | ❌ | ✅ | ✅ | ✅ |

*With PQ8 compression. Benchmarks on Apple M2 / Intel i7.



## Features

### Core Capabilities

| Feature | What It Does | Why It Matters |
|---------|--------------|----------------|
| **Vector Search** | HNSW index, <0.5ms latency, SIMD acceleration | Fast enough for real-time apps |
| **Cypher Queries** | `MATCH`, `WHERE`, `CREATE`, `RETURN` | Familiar Neo4j syntax |
| **G