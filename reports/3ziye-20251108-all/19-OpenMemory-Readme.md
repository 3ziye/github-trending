<img width="1577" height="781" alt="image" src="https://github.com/user-attachments/assets/3baada32-1111-4c2c-bf13-558f2034e511" />

# OpenMemory

Long-term memory for AI systems. Open source, self-hosted, and explainable.

⚠️ **Upgrading from v1.1?** Multi-user tenant support requires database migration. See [MIGRATION.md](./MIGRATION.md) for upgrade instructions.

[VS Code Extension](https://marketplace.visualstudio.com/items?itemName=Nullure.openmemory-vscode) • [Report Bug](https://github.com/caviraOSS/openmemory/issues) • [Request Feature](https://github.com/caviraOSS/openmemor/issues) • [Discord server](https://discord.gg/P7HaRayqTh)

---

## 1. Overview

OpenMemory gives AI systems persistent memory. It stores what matters, recalls it when needed, and explains why it matters.

Unlike traditional vector databases, OpenMemory uses a cognitive architecture. It organizes memories by type (semantic, episodic, procedural, emotional, reflective), tracks importance over time, and builds associations between related memories.

### Key Features

- **Multi-sector memory** - Different memory types for different content
- **Automatic decay** - Memories fade naturally unless reinforced
- **Graph associations** - Memories link to related memories
- **Pattern recognition** - Finds and consolidates similar memories
- **User isolation** - Each user gets separate memory space
- **Local or cloud** - Run with your own embeddings or use OpenAI/Gemini
- **Framework agnostic** - Works with any LLM or agent system

### VS Code Extension

The OpenMemory extension tracks your coding activity and gives AI assistants access to your project history.

**[Get it on VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=Nullure.openmemory-vscode)**

Works with GitHub Copilot, Cursor, Claude Desktop, Windsurf, and any MCP-compatible AI.

Features:

- Tracks file edits, saves, and opens
- Compresses context to reduce token usage by 30-70%
- Query responses under 80ms
- Supports Direct HTTP and MCP protocol modes
- Zero configuration required

### Architecture

OpenMemory uses Hierarchical Memory Decomposition (HMD):

- One canonical node per memory (no duplication)
- Multiple embeddings per memory (one per sector)
- Single-waypoint linking between memories
- Composite similarity scoring across sectors

This approach improves recall accuracy while reducing costs.

---

## 2. Competitor Comparison

| **Feature / Metric**                     | **OpenMemory (Our Tests – Nov 2025)**                       | **Zep (Their Benchmarks)**         | **Supermemory (Their Docs)**    | **Mem0 (Their Tests)**        | **OpenAI Memory**          | **LangChain Memory**        | **Vector DBs (Chroma / Weaviate / Pinecone)** |
| ---------------------------------------- | ----------------------------------------------------------- | ---------------------------------- | ------------------------------- | ----------------------------- | -------------------------- | --------------------------- | --------------------------------------------- |
| **Open-source License**                  | ✅ MIT (verified)                                           | ✅ Apache 2.0                      | ✅ Source available (GPL-like)  | ✅ Apache 2.0                 | ❌ Closed                  | ✅ Apache 2.0               | ✅ Varies (OSS + Cloud)                       |
| **Self-hosted / Local**                  | ✅ Full (Local / Docker / MCP) tested ✓                     | ✅ Local + Cloud SDK               | ⚠️ Mostly managed cloud tier    | ✅ Self-hosted ✓              | ❌ No                      | ✅ Yes (in your stack)      | ✅ Chroma / Weaviate ❌ Pinecone (cloud)      |
| **Per-user namespacing (`user_id`)**     | ✅ Built-in (`user_id` linking added)                       | ✅ Sessions / Users API            | ⚠️ Multi-tenant via API key     | ✅ Explicit `user_id` field ✓ | ❌ Internal only           | ✅ Namespaces via LangGraph | ✅ Collection-per-user schema                 |
| **Architecture**                         | HSG v3 (Hierarchical Semantic Graph + Decay + Coactivation) | Flat embeddings + Postgres + FAISS | Graph + Embeddings              | Flat vector store             | Proprietary cache          | Context memory utils        | Vector index (ANN)                            |
| **Avg Response Time (100k nodes)**       | **115 ms avg (measured)**                                   | 310 ms (docs)                      | 200–340 ms (on-prem/cloud)      | ~250 ms                       | 300 ms (observed)          | 200 ms (avg)                | 160 ms (avg)                                  |
| **Throughput (QPS)**                     | **338 QPS avg (8 workers, P95 103 ms)** ✓                   | ~180 QPS (reported)                | ~220 QPS (on-prem)              | ~150 QPS                      | ~180 QPS                   | ~140 QPS                    | ~250 QPS typical                              |
| **Recall @5 (Accuracy)**                 | **95 % re