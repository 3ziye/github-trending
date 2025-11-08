![TOON logo with step‑by‑step guide](./.github/og.png)

# Token-Oriented Object Notation (TOON)

[![CI](https://github.com/toon-format/toon/actions/workflows/ci.yml/badge.svg)](https://github.com/toon-format/toon/actions)
[![npm version](https://img.shields.io/npm/v/@toon-format/toon.svg)](https://www.npmjs.com/package/@toon-format/toon)
[![SPEC v1.4](https://img.shields.io/badge/spec-v1.4-lightgray)](https://github.com/toon-format/spec)
[![npm downloads (total)](https://img.shields.io/npm/dt/@toon-format/toon.svg)](https://www.npmjs.com/package/@toon-format/toon)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)

**Token-Oriented Object Notation** is a compact, human-readable serialization format designed for passing structured data to Large Language Models with significantly reduced token usage. It's intended for *LLM input* as a lossless, drop-in representation of JSON data.

TOON's sweet spot is **uniform arrays of objects** – multiple fields per row, same structure across items. It borrows YAML's indentation-based structure for nested objects and CSV's tabular format for uniform data rows, then optimizes both for token efficiency in LLM contexts. For deeply nested or non-uniform data, JSON may be more efficient.

TOON achieves CSV-like compactness while adding explicit structure that helps LLMs parse and validate data reliably.

> [!TIP]
> Think of TOON as a translation layer: use JSON programmatically, convert to TOON for LLM input.

## Table of Contents

- [Why TOON?](#why-toon)
- [Key Features](#key-features)
- [Benchmarks](#benchmarks)
- [📋 Full Specification](https://github.com/toon-format/spec/blob/main/SPEC.md)
- [Installation & Quick Start](#installation--quick-start)
- [CLI](#cli)
- [Format Overview](#format-overview)
- [API](#api)
- [Using TOON in LLM Prompts](#using-toon-in-llm-prompts)
- [Notes and Limitations](#notes-and-limitations)
- [Syntax Cheatsheet](#syntax-cheatsheet)
- [Other Implementations](#other-implementations)

## Why TOON?

AI is becoming cheaper and more accessible, but larger context windows allow for larger data inputs as well. **LLM tokens still cost money** – and standard JSON is verbose and token-expensive:

```json
{
  "users": [
    { "id": 1, "name": "Alice", "role": "admin" },
    { "id": 2, "name": "Bob", "role": "user" }
  ]
}
```

TOON conveys the same information with **fewer tokens**:

```
users[2]{id,name,role}:
  1,Alice,admin
  2,Bob,user
```

<details>
<summary><strong>Why create a new format?</strong></summary>

For small payloads, JSON/CSV/YAML work fine. TOON's value emerges at scale: when you're making hundreds of LLM calls with uniform tabular data, eliminating repeated keys compounds savings significantly. If token costs matter to your use case, TOON reduces them. If not, stick with what works.

</details>

<details>
<summary><strong>When NOT to use TOON</strong></summary>

TOON excels with uniform arrays of objects, but there are cases where other formats are better:

- **Deeply nested or non-uniform structures** (tabular eligibility ≈ 0%): JSON-compact often uses fewer tokens. Example: complex configuration objects with many nested levels.
- **Semi-uniform arrays** (~40–60% tabular eligibility): Token savings diminish. Prefer JSON if your pipelines already rely on it.
- **Flat CSV use-cases**: CSV is smaller than TOON for pure tabular data. TOON adds minimal overhead (~5-10%) to provide structure (length markers, field headers, delimiter scoping) that improves LLM reliability.

See [benchmarks](#benchmarks) for concrete comparisons across different data structures.

</details>

## Key Features

- 💸 **Token-efficient:** typically 30-60% fewer tokens on large uniform arrays vs formatted JSON[^1]
- 🤿 **LLM-friendly guardrails:** explicit lengths and fields enable validation
- 🍱 **Minimal syntax:** removes redundant punctuation (braces, brackets, most quotes)
- 📐 **Indentation-based structure:** like YAML, uses whitespace instead of braces
- 🧺 **Tabular arrays:** declare keys once, stream data as rows

[^1]: For flat tabular data, CSV is more compact. TOON adds minimal overhead to provide explicit structure and validation that improves LLM reliability.

## Benchmarks

> [!TIP]
> Try the interactive [Format Tokenization Playground](https://www.curiouslychase.com/playground/format-tokenization-exploration) to compare token usage across CSV, JSON, YAML, and TOON with your own data.

Benchmarks are organized into two tracks to ensure fair comparisons:

- **Mixed-Structure Track**: Datasets with nested or semi-uniform structures (TOON vs JSON, YAML, XML). CSV excluded as it cannot properly represent these structures.
- **Flat-Only Track**: Datasets with flat tabular structures where CSV is applicable (CSV vs TOON vs JSON, YAML, XML).

### Token Efficiency

Token counts are measured using the GPT-5 `o200k_base` tokenizer via [`gpt-tokenizer`](https://github.com/niieani/gpt-tokenizer). Savings are calculated against formatted JSO