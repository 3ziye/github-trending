<div align="center">

<img src="assets/hero.svg" alt="SlothDB" width="100%">

<h3>Run analytics faster.</h3>

<p>SlothDB is an embedded SQL database that runs everywhere: on your laptop, on a server, and in the browser. Built from scratch. <b>Up to 5x faster</b> where it counts.</p>

<p align="center">
  <a href="https://discord.gg/XJWyGmX5G">
    <img src="assets/discord-cta.svg" alt="Join the SlothDB Discord" width="340">
  </a>
</p>

[![PyPI](https://img.shields.io/pypi/v/slothdb?color=3775A9&logo=pypi&logoColor=white&cacheSeconds=60)](https://pypi.org/project/slothdb/)
[![npm](https://img.shields.io/npm/v/@slothdb/wasm?color=CB3837&logo=npm&label=npm)](https://www.npmjs.com/package/@slothdb/wasm)
[![PyPI downloads](https://static.pepy.tech/badge/slothdb)](https://pepy.tech/project/slothdb)
[![npm downloads](https://img.shields.io/npm/dt/@slothdb/wasm?label=npm%20downloads&color=CB3837)](https://www.npmjs.com/package/@slothdb/wasm)
[![CI](https://github.com/SouravRoy-ETL/slothdb/actions/workflows/ci.yml/badge.svg)](https://github.com/SouravRoy-ETL/slothdb/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Stars](https://img.shields.io/github/stars/SouravRoy-ETL/slothdb?style=social)](https://github.com/SouravRoy-ETL/slothdb)
[![PeerPush](https://peerpush.net/p/slothdb/badge.png)](https://peerpush.net/p/slothdb)

[Website](https://slothdb.org) · [**Playground**](https://slothdb.org/playground/) · [**Discord**](https://discord.gg/XJWyGmX5G) · [Blog](https://slothdb.org/blog/compiling-a-database-to-wasm.html) · [Docs](docs/DOCUMENTATION.md) · [Benchmarks](#performance) · [Python](docs/DOCUMENTATION.md#6-python-api) · [SQL Guide](docs/DOCUMENTATION.md#4-sql-guide)

<br>

<img src="assets/demo.svg" alt="SlothDB 60-second demo - side-by-side timing vs DuckDB" width="90%">

</div>

---

## Ask in any language. Get SQL.

Type `.ask` at the `slothdb>` prompt. A rules parser handles catalog questions and common English shapes in under 10 ms with no model. Anything else falls through to a local Qwen2.5-Coder (0.5B for simple, 1.5B for analytic; lazy-downloaded on first use under `-DSLOTHDB_ASK_MODEL=ON`), which speaks 29 natural languages: English, Chinese, Spanish, French, German, Japanese, Korean, Russian, Arabic, Portuguese, Italian, Hindi, and more. Every generated statement is shown before it runs. Nothing leaves the machine. Set `SLOTHDB_ASK_CONFIRM=1` to add a `[Y/n]` prompt before each run.

<div align="center">
  <img src="assets/ask-demo.svg" alt=".ask: rules-first, router, two local Qwens, [Y/n] gate" width="100%">
</div>

| tier | what | cost | covers |
|---|---|--:|---|
| 1 | **Rules parser** (default) | sub-10 ms, no model | catalog, COUNT/SUM/AVG/GROUP BY/TOP-N, file-source |
| 2 | **Local Qwen 2.5-Coder 0.5B Q4_K_M** | ~200 ms, ~310 MB | open-ended SELECT/GROUP BY/filter |
| 3 | **Local Qwen 2.5-Coder 1.5B Q4_K_M** | ~500 ms, ~986 MB | window functions, ranking within groups, LAG/LEAD, joins |

Both model tiers download lazily in parallel on first `.ask` (total ~1.3 GB). Router is a pure function of the question: no LLM call involved in routing. Cumulative / running / moving aggregates refuse cleanly (engine gap, not model gap). Full spec, router signals, refusal policy: [docs/ASK.md](docs/ASK.md).

## Try it in 60 seconds

**In your browser** - no install, no account: **[slothdb.org/playground](https://slothdb.org/playground/)**. Full SlothDB compiled to WebAssembly, with a pre-loaded 1,000-row demo CSV + matching Parquet to compare format performance. Files you add stay on your machine.

**In Python** - CPython 3.8+ on Linux / macOS / Windows (see [latest release](https://github.com/SouravRoy-ETL/slothdb/releases/latest) for published wheel tags; falls back to source build if no wheel matches):

```bash
pip install slothdb
python -c "import slothdb; slothdb.demo()"
```

That generates a 100 000-row CSV, runs three queries, and prints the side-by-side with DuckDB shown above. No files to find, no setup.

```python
# Your own files, same API. pandas round-trip in two lines:
import slothdb, pandas as pd
db = slothdb.connect()
df = db.sql("SELECT region, SUM(revenue) AS rev FROM 'sales.parquet' GROUP BY region").fetchdf()
```

**In Node/JS** - `npm install @slothdb/wasm`:

```js
import { SlothDB } from '@slothdb/wasm';
const db = await SlothDB.create();
const { columns, rows } = db.query("SELECT 1 AS n");
```

**In the shell** - [download](https://github.com/SouravRoy-ETL/slothdb/releases/latest) or build from source; then `slothdb analytics.slothdb` for a persistent single-file DB.

---

## What's new in 0.2.5

- **Nested aggregates work everywhere.** `ROUND(AVG(x))`, `AVG(x) + 1`, `SUM(x) / COUNT(*)`, `CAST(SUM(y) AS DOUBLE)` and other shapes that wrap an aggregate inside a scalar function or arithmetic used to throw "Function execution for: AVG". The planner now walks the whole expression tree and hoists every aggregate it finds, no matter how deep, so