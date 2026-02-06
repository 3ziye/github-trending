<div align="center">

# mmdr

**100–1400x faster Mermaid rendering. Pure Rust. Zero browser dependencies.**

[Installation](#installation) | [Quick Start](#quick-start) | [Benchmarks](#performance) | [Examples](#diagram-types)

</div>

## Performance

mmdr renders diagrams **100–1400x faster** than mermaid-cli by eliminating browser overhead.
With the built-in font cache (warm after first run), tiny diagrams reach **500–900×** (and `--fastText` exceeds **1600×**).

<p align="center">
  <img src="docs/benchmarks/comparison.svg" alt="Performance comparison" width="600">
</p>

<div align="center">

| Diagram | mmdr | mermaid-cli | Speedup |
|:--------|-----:|------------:|--------:|
| Flowchart | 4.54 ms | 2,449 ms | **540x** |
| Class Diagram | 6.51 ms | 2,417 ms | **371x** |
| State Diagram | 5.99 ms | 2,778 ms | **464x** |
| Sequence Diagram | 5.71 ms | 2,297 ms | **402x** |

<sub>Tested on Intel Core Ultra 7 265V, Linux 6.18.2 | mermaid-cli 11.4.2 via Puppeteer/Chromium</sub>

</div>

<details>
<summary><strong>Font cache (default, warm after first run)</strong></summary>

Once the font cache is populated, tiny/common diagrams reach **500–900×**:

| Diagram (tiny) | mmdr (warm cache) | mermaid-cli | Speedup |
|:--|--:|--:|--:|
| Flowchart | 2.96 ms | 2,259 ms | **764×** |
| Class | 2.55 ms | 2,347 ms | **919×** |
| State | 2.67 ms | 2,111 ms | **789×** |
| Sequence | 3.75 ms | 2,010 ms | **536×** |

<sub>Measured Feb 2, 2026 on the same machine.</sub>
</details>

<details>
<summary><strong>Fast text metrics (optional, fastest)</strong></summary>

Enable `--fastText` to use calibrated fallback widths for ASCII labels (avoids font DB load).
On tiny/common diagrams this reaches **1600–2069×** speedups:

| Diagram (tiny) | mmdr `--fastText` | mermaid-cli | Speedup |
|:--|--:|--:|--:|
| Flowchart | 1.32 ms | 2,116 ms | **1,601×** |
| Class | 1.23 ms | 2,314 ms | **1,880×** |
| State | 1.09 ms | 2,258 ms | **2,069×** |
| Sequence | 1.16 ms | 2,158 ms | **1,868×** |

<sub>Measured Feb 2, 2026 on the same machine.</sub>
</details>

<p align="center">
  <img src="docs/benchmarks/breakdown.svg" alt="Pipeline breakdown" width="500">
</p>

<details>
<summary><strong>Library Performance (no CLI overhead)</strong></summary>

When used as a Rust library, mmdr is even faster with no process spawn overhead:

<p align="center">
  <img src="docs/benchmarks/library.svg" alt="Library performance" width="500">
</p>

| Diagram | Library Time |
|:--------|-------------:|
| Flowchart | 1.49 ms |
| Class Diagram | 2.51 ms |
| State Diagram | 2.04 ms |
| Sequence Diagram | 0.07 ms |

These are raw render times measured with Criterion, ideal for embedding in applications.

</details>

<details>
<summary><strong>Extended Benchmarks</strong></summary>

Performance on larger diagrams:

| Diagram | Nodes | mmdr | mermaid-cli | Speedup |
|:--------|------:|-----:|------------:|--------:|
| flowchart (small) | 10 | 7.04 ms | 2,135 ms | 303x |
| flowchart (medium) | 50 | 5.20 ms | 2,197 ms | 422x |
| flowchart (large) | 200 | 21.84 ms | 2,612 ms | 120x |

The speedup advantage decreases for very large diagrams as actual layout computation becomes more significant relative to browser startup overhead. Still, mmdr remains **100x+ faster** even for 200-node diagrams.

</details>

## Why mmdr?

The official `mermaid-cli` spawns a **headless Chromium browser** for every diagram, adding 2-3 seconds of startup overhead.

| Use Case | mermaid-cli | mmdr |
|:---------|:------------|:-----|
| CI/CD pipeline with 50 diagrams | ~2 minutes | **< 1 second** |
| Real-time editor preview | Unusable lag | **Instant** |
| Batch doc generation | Coffee break | **Blink of an eye** |

mmdr parses Mermaid syntax natively in Rust and renders directly to SVG. No browser. No Node.js. No Puppeteer.

## Installation

```bash
# From source
cargo install --path .

# Homebrew (macOS/Linux)
brew tap 1jehuang/mmdr && brew install mmdr

# Scoop (Windows)
scoop bucket add mmdr https://github.com/1jehuang/scoop-mmdr && scoop install mmdr

# AUR (Arch)
yay -S mmdr-bin
```

## Quick Start

```bash
# Pipe diagram to stdout
echo 'flowchart LR; A-->B-->C' | mmdr -e svg

# File to file
mmdr -i diagram.mmd -o output.svg -e svg
mmdr -i diagram.mmd -o output.png -e png

# Render all diagrams from a Markdown file
mmdr -i README.md -o ./diagrams/ -e svg
```

## Diagram Types

mmdr supports **13 Mermaid diagram types**:

| Category | Diagrams |
|:---------|:---------|
| **Core** | Flowchart, Sequence, Class, State |
| **Data** | ER Diagram, Pie Chart, XY Chart, Quadrant Chart |
| **Planning** | Gantt, Timeline, Journey |
| **Other** | Mindmap, Git Graph |

<table>
<tr>
<td align="center" width="50%">
<strong>Flowchart</strong><br>
<img src="docs/comparisons/flowchart_mmdr.svg" alt="Flowchart" width="100%">
</td>
<td align="center" width="50%">
<strong>Class Diagram</strong><br>
<img src="docs/comparisons/class_mmdr.svg" alt="Class Diagram" width="100%">
</td>
</tr>
<tr>
<td align="cente