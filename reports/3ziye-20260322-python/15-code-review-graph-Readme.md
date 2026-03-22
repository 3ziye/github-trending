<h1 align="center">code-review-graph</h1>

<p align="center">
  <strong>Stop burning tokens. Start reviewing smarter.</strong>
</p>

<p align="center">
  <a href="https://github.com/tirth8205/code-review-graph/stargazers"><img src="https://img.shields.io/github/stars/tirth8205/code-review-graph?style=flat-square" alt="Stars"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square" alt="MIT Licence"></a>
  <a href="https://github.com/tirth8205/code-review-graph/actions/workflows/ci.yml"><img src="https://github.com/tirth8205/code-review-graph/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.10%2B-blue.svg?style=flat-square" alt="Python 3.10+"></a>
  <a href="https://modelcontextprotocol.io/"><img src="https://img.shields.io/badge/MCP-compatible-green.svg?style=flat-square" alt="MCP"></a>
  <a href="#"><img src="https://img.shields.io/badge/version-1.8.4-purple.svg?style=flat-square" alt="v1.8.4"></a>
</p>

<br>

Claude Code re-reads your entire codebase on every task. `code-review-graph` fixes that. It builds a structural map of your code with [Tree-sitter](https://tree-sitter.github.io/tree-sitter/), tracks changes incrementally, and gives Claude precise context so it reads only what matters.

<p align="center">
  <img src="diagrams/diagram1_before_vs_after.png" alt="The Token Problem: 6.8x fewer tokens with higher review quality" width="85%" />
</p>

---

## Quick Start

**Claude Code Plugin** (recommended)

```bash
claude plugin marketplace add tirth8205/code-review-graph
claude plugin install code-review-graph@code-review-graph
```

**pip**

```bash
pip install code-review-graph
code-review-graph install
```

Restart Claude Code after either method. Requires Python 3.10+ and [uv](https://docs.astral.sh/uv/).

Then open your project and tell Claude:

```
Build the code review graph for this project
```

The initial build takes ~10 seconds for a 500-file project. After that, the graph updates automatically on every file edit and git commit.

---

## How It Works

Your repository is parsed into an AST with Tree-sitter, stored as a graph of nodes (functions, classes, imports) and edges (calls, inheritance, test coverage), then queried at review time to compute the minimal set of files Claude needs to read.

<p align="center">
  <img src="diagrams/diagram2_architecture_pipeline.png" alt="Architecture pipeline: Repository to Tree-sitter Parser to SQLite Graph to Blast Radius to Minimal Review Set" width="100%" />
</p>

<details>
<summary><strong>Blast-radius analysis</strong></summary>
<br>

When a file changes, the graph traces every caller, dependent, and test that could be affected. This is the "blast radius" of the change. Claude reads only these files instead of scanning the whole project.

<p align="center">
  <img src="diagrams/diagram3_blast_radius.png" alt="Blast radius visualization showing how a change to login() propagates to callers, dependents, and tests" width="70%" />
</p>

</details>

<details>
<summary><strong>Incremental updates in &lt; 2 seconds</strong></summary>
<br>

On every git commit or file save, a hook fires. The graph diffs changed files, finds their dependents via SHA-256 hash checks, and re-parses only what changed. A 2,900-file project re-indexes in under 2 seconds.

<p align="center">
  <img src="diagrams/diagram4_incremental_update.png" alt="Incremental update flow: git commit triggers diff, finds dependents, re-parses only 5 files while 2,910 are skipped" width="90%" />
</p>

</details>

<details>
<summary><strong>14 supported languages</strong></summary>
<br>

Python, TypeScript, JavaScript, Vue, Go, Rust, Java, C#, Ruby, Kotlin, Swift, PHP, Solidity, C/C++

Each language has full Tree-sitter grammar support for functions, classes, imports, call sites, inheritance, and test detection.

</details>

---

## Benchmarks

All figures come from real tests on three production open-source repositories.

<p align="center">
  <img src="diagrams/diagram5_benchmark_board.png" alt="Benchmarks: httpx 27.3x, FastAPI 6.3x, Next.js 4.9x token reduction with higher review quality" width="90%" />
</p>

<details>
<summary><strong>Code review benchmark details (6.8x average reduction)</strong></summary>
<br>

Tested across 6 real git commits. The graph replaces reading entire source files with a compact structural summary (156-207 tokens) covering blast radius, test coverage gaps, and dependency chains.

| Repo | Size | Standard Approach | With Graph | Reduction | Review Quality |
|------|-----:|------------------:|-----------:|----------:|:-:|
| [httpx](https://github.com/encode/httpx) | 125 files | 12,507 tokens | 458 tokens | 26.2x | 9.0 vs 7.0 |
| [FastAPI](https://github.com/fastapi/fastapi) | 2,915 files | 5,495 tokens | 871 tokens | 8.1x | 8.5 vs 7.5 |
| [Next.js](https://github.com/vercel/next.js) | 27,732 files | 21,614 tokens 