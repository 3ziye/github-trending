# Vestige

**The open-source cognitive engine for AI.**

[![GitHub stars](https://img.shields.io/github/stars/samvallad33/vestige?style=social)](https://github.com/samvallad33/vestige)
[![Release](https://img.shields.io/github/v/release/samvallad33/vestige)](https://github.com/samvallad33/vestige/releases/latest)
[![License](https://img.shields.io/badge/license-AGPL--3.0-blue)](LICENSE)
[![MCP Compatible](https://img.shields.io/badge/MCP-compatible-green)](https://modelcontextprotocol.io)

> Your AI forgets everything between sessions. Vestige fixes that. Built on 130 years of memory research — FSRS-6 spaced repetition, prediction error gating, synaptic tagging — all running in a single Rust binary, 100% local.

### What's New in v1.6.0

- **6x vector storage reduction** — F16 quantization + Matryoshka 256-dim truncation
- **Neural reranking** — Jina cross-encoder reranker for ~20% better retrieval
- **Instant startup** — cross-encoder loads in background, zero blocking
- **Auto-migration** — old 768-dim embeddings seamlessly upgraded

See [CHANGELOG](CHANGELOG.md) for full version history.

---

## Give Your AI a Brain in 30 Seconds

```bash
# 1. Install
curl -L https://github.com/samvallad33/vestige/releases/latest/download/vestige-mcp-aarch64-apple-darwin.tar.gz | tar -xz
sudo mv vestige-mcp vestige vestige-restore /usr/local/bin/

# 2. Connect
claude mcp add vestige vestige-mcp -s user

# 3. Test
# "Remember that I prefer TypeScript over JavaScript"
# New session → "What are my coding preferences?"
# It remembers.
```

<details>
<summary>Other platforms & install methods</summary>

**macOS (Intel):**
```bash
curl -L https://github.com/samvallad33/vestige/releases/latest/download/vestige-mcp-x86_64-apple-darwin.tar.gz | tar -xz
sudo mv vestige-mcp vestige vestige-restore /usr/local/bin/
```

**Linux:**
```bash
curl -L https://github.com/samvallad33/vestige/releases/latest/download/vestige-mcp-x86_64-unknown-linux-gnu.tar.gz | tar -xz
sudo mv vestige-mcp vestige vestige-restore /usr/local/bin/
```

**Windows:** Download from [Releases](https://github.com/samvallad33/vestige/releases/latest)

**Build from source:**
```bash
git clone https://github.com/samvallad33/vestige && cd vestige
cargo build --release
sudo cp target/release/{vestige-mcp,vestige,vestige-restore} /usr/local/bin/
```

**npm:**
```bash
npm install -g vestige-mcp
```
</details>

---

## Works Everywhere

Vestige speaks MCP — the universal protocol for AI tools. One brain, every IDE.

| IDE | Setup |
|-----|-------|
| **Claude Code** | `claude mcp add vestige vestige-mcp -s user` |
| **Claude Desktop** | [2-min setup](docs/CONFIGURATION.md#claude-desktop-macos) |
| **Xcode 26.3** | [Integration guide](docs/integrations/xcode.md) |
| **Cursor** | [Integration guide](docs/integrations/cursor.md) |
| **VS Code (Copilot)** | [Integration guide](docs/integrations/vscode.md) |
| **JetBrains** | [Integration guide](docs/integrations/jetbrains.md) |
| **Windsurf** | [Integration guide](docs/integrations/windsurf.md) |

Fix a bug in VS Code. Open Xcode. Your AI already knows about the fix.

---

## Why Not Just Use RAG?

RAG is a dumb bucket. Vestige is an active organ.

| | RAG / Vector Store | Vestige |
|---|---|---|
| **Storage** | Store everything, retrieve everything | **Prediction Error Gating** — only stores what's surprising or new |
| **Retrieval** | Nearest-neighbor similarity | **Spreading activation** — finds related memories through association chains |
| **Decay** | Nothing ever expires | **FSRS-6** — memories fade like yours do, keeping context lean |
| **Duplicates** | Manual dedup or none | **Self-healing** — automatically merges "likes dark mode" + "prefers dark themes" |
| **Importance** | All memories are equal | **Synaptic tagging** — retroactively strengthens memories that turn out to matter |
| **Privacy** | Usually cloud-dependent | **100% local** — your data never leaves your machine |

---

## The Cognitive Science Stack

This isn't a key-value store with an embedding model bolted on. Vestige implements real neuroscience:

**Prediction Error Gating** — The bouncer for your brain. When new information arrives, Vestige compares it against existing memories. Redundant? Merged. Contradictory? Superseded. Novel? Stored. Just like the hippocampus.

**FSRS-6 Spaced Repetition** — 21 parameters governing the mathematics of forgetting. Frequently-used memories stay strong. Unused memories naturally decay. Your context window stays clean.

**Synaptic Tagging** — A memory that seemed trivial this morning can be retroactively tagged as critical tonight. Based on [Frey & Morris, 1997](https://doi.org/10.1038/385533a0).

**Spreading Activation** — Search for "auth bug" and find the related memory about the JWT library update you saved last week. Memories form a graph, not a flat list. Based on [Collins & Loftus, 1975](https://doi.org/10.1037/0033-295X.82.6.407).

**Dual-Strength Model** — Every memory has two values: storage strength (ho