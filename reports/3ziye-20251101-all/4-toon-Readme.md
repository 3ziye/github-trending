![TOON logo with step‑by‑step guide](./.github/og.png)

# Token-Oriented Object Notation (TOON)

[![CI](https://github.com/johannschopplich/toon/actions/workflows/ci.yml/badge.svg)](https://github.com/johannschopplich/toon/actions)
[![npm version](https://img.shields.io/npm/v/@byjohann/toon.svg)](https://www.npmjs.com/package/@byjohann/toon)
[![SPEC v1.3](https://img.shields.io/badge/spec-v1.3-lightgrey)](./SPEC.md)
[![npm downloads (total)](https://img.shields.io/npm/dt/@byjohann/toon.svg)](https://www.npmjs.com/package/@byjohann/toon)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)

**Token-Oriented Object Notation** is a compact, human-readable format designed for passing structured data to Large Language Models with significantly reduced token usage. It's intended for LLM input, not output.

TOON's sweet spot is **uniform arrays of objects** – multiple fields per row, same structure across items. It borrows YAML's indentation-based structure for nested objects and CSV's tabular format for uniform data rows, then optimizes both for token efficiency in LLM contexts. For deeply nested or non-uniform data, JSON may be more efficient.

> [!TIP]
> Think of TOON as a translation layer: use JSON programmatically, convert to TOON for LLM input.

## Table of Contents

- [Why TOON?](#why-toon)
- [Key Features](#key-features)
- [Benchmarks](#benchmarks)
- [📋 Full Specification](./SPEC.md)
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
<summary>Another reason</summary>

[![xkcd: Standards](https://imgs.xkcd.com/comics/standards_2x.png)](https://xkcd.com/927/)

</details>

## Key Features

- 💸 **Token-efficient:** typically 30–60% fewer tokens than JSON
- 🤿 **LLM-friendly guardrails:** explicit lengths and fields enable validation
- 🍱 **Minimal syntax:** removes redundant punctuation (braces, brackets, most quotes)
- 📐 **Indentation-based structure:** like YAML, uses whitespace instead of braces
- 🧺 **Tabular arrays:** declare keys once, stream data as rows

## Benchmarks

> [!TIP]
> Try the interactive [Format Tokenization Playground](https://www.curiouslychase.com/playground/format-tokenization-exploration) to compare token usage across CSV, JSON, YAML, and TOON with your own data.

The benchmarks test datasets that favor TOON's strengths (uniform tabular data). Real-world performance depends heavily on your data structure.

<!-- automd:file src="./benchmarks/results/token-efficiency.md" -->

### Token Efficiency

```
⭐ GitHub Repositories       ██████████████░░░░░░░░░░░    8,745 tokens
                             vs JSON (-42.3%)           15,145
                             vs JSON compact (-23.7%)   11,455
                             vs YAML (-33.4%)           13,129
                             vs XML (-48.8%)            17,095

📈 Daily Analytics           ██████████░░░░░░░░░░░░░░░    4,507 tokens
                             vs JSON (-58.9%)           10,977
                             vs JSON compact (-35.7%)    7,013
                             vs YAML (-48.8%)            8,810
                             vs XML (-65.7%)            13,128

🛒 E-Commerce Order          ████████████████░░░░░░░░░      166 tokens
                             vs JSON (-35.4%)              257
                             vs JSON compact (-2.9%)       171
                             vs YAML (-15.7%)              197
                             vs XML (-38.7%)               271

─────────────────────────────────────────────────────────────────────
Total                        ██████████████░░░░░░░░░░░   13,418 tokens
                             vs JSON (-49.1%)           26,379
                             vs JSON compact (-28.0%)   18,639
                             vs YAML (-39.4%)           22,136
                             vs XML (-56.0%)            30,494
```

<details>
<summary><strong>Show detailed examples</strong></summary>

#### ⭐ GitHub Repositories

**Configuration:** Top 100 GitHub repositories with stars, forks, and metadata

**Savings:** 6,400 tokens (42.3% reduction vs JSON)

**JSON** (15,145 tokens):

```json
{
  "repositories": [
    {
      "id": 28457823,
      "name": "freeCodeCamp",
      "repo": "freeCodeCamp/freeCodeCamp",
      "de