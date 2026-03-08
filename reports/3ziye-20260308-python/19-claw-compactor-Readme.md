# 🗜️ Claw Compactor

[![Build](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/aeromomo/claw-compactor)
[![Tests](https://img.shields.io/badge/tests-848%20passed-brightgreen)](https://github.com/aeromomo/claw-compactor)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-purple)](LICENSE)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-skill-orange)](https://openclaw.ai)
[![Release](https://img.shields.io/github/v/release/aeromomo/claw-compactor?color=blue)](https://github.com/aeromomo/claw-compactor/releases)

> **Cut your AI agent's token spend by 50–97%.**  
> One command compresses your entire workspace — memory files, session transcripts,
> sub-agent context — using 6 layered techniques, from deterministic rule-engines
> to a real-time LLM-driven memory system called **Engram**.

*"Cut your tokens. Keep your facts."*

---

## ✨ Why Claw Compactor?

Running long-lived AI agents is expensive. Context windows fill up. Memory files bloat. Session transcripts grow to megabytes. Claw Compactor solves all three:

- **5 deterministic layers** — zero LLM cost, instant, fully reversible
- **Layer 6: Engram** — the real magic: a live, LLM-powered memory engine that observes conversations as they happen and compresses them into structured, priority-annotated knowledge
- **~97% savings** on raw session transcripts  
- **One command** (`full`) to run everything

---

## 🚀 Quick Start

```bash
# 1. Clone
git clone https://github.com/aeromomo/claw-compactor.git
cd claw-compactor

# 2. Dry-run benchmark (non-destructive, no side effects)
python3 scripts/mem_compress.py /path/to/workspace benchmark

# 3. Compress everything
python3 scripts/mem_compress.py /path/to/workspace full
```

**Requirements:** Python 3.9+. No mandatory dependencies.  
Optional: `pip install tiktoken` for exact token counts (falls back to CJK-aware heuristic).

For Engram (Layer 6): configure `engram.yaml` (or set `ANTHROPIC_API_KEY` / `OPENAI_API_KEY` env vars).

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                    mem_compress.py                                  │
│              (unified CLI entry point / dispatcher)                 │
└───┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬───────┘
    │      │      │      │      │      │      │      │      │
    ▼      ▼      ▼      ▼      ▼      ▼      ▼      ▼      ▼
estimate compress dict  dedup observe tiers audit optimize engram
    │      │      │      │      │      │      │      │      │
    └──────┴──────┴──────┴──────┴──────┴──────┴──────┘      │
                          │                                   │
                          ▼                                   ▼
             ┌────────────────────────┐        ┌─────────────────────────┐
             │   scripts/lib/         │        │   ENGRAM ENGINE         │
             │                        │        │  (Layer 6, real-time)   │
             │  tokens.py             │        │                         │
             │    ↳ tiktoken fallback │        │  engram.py              │
             │  markdown.py           │        │    ↳ EngramEngine       │
             │    ↳ section parsing   │        │    ↳ Observer Agent     │
             │  dedup.py              │        │    ↳ Reflector Agent    │
             │    ↳ shingle hashing   │        │                         │
             │  dictionary.py         │        │  engram_storage.py      │
             │    ↳ $XX codebook      │        │    ↳ atomic file I/O    │
             │  rle.py                │        │    ↳ JSONL pending log  │
             │    ↳ path/IP/enum      │        │                         │
             │  tokenizer_optimizer   │        │  engram_prompts.py      │
             │    ↳ format fixes      │        │    ↳ Observer prompt    │
             │  config.py             │        │    ↳ Reflector prompt   │
             │  exceptions.py         │        └─────────────────────────┘
             └────────────────────────┘

Engram Memory Layout (per thread / 每个会话线程):
  memory/engram/{thread_id}/
    ├── pending.jsonl     ← raw messages buffer (auto-cleared after observe)
    ├── observations.md   ← Observer output, append-only structured log
    ├── reflections.md    ← Reflector output, compressed long-term memory
    └── meta.json         ← timestamps, token counts
```

---

## 📊 Compression Layers

| Layer | Name | Technique | Typical Savings | Notes |
|-------|------|-----------|-----------------|-------|
| 1 | **Rule Engine** | Dedup lines, strip markdown filler, merge sections | 4–8% | Lossless |
| 2 | **Dictionary Encoding** | Auto-learned codebook, `$XX` substitution | 4–5% | Lossless |
| 3 | **Observation Compression** | Session JSONL → structured summaries | ~97% | Lossy* |
| 4 | **RLE Patterns** | Path shorthand (`$WS`), IP prefix, enum compaction | 1–2