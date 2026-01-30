<div align="center">

# mmdr

**500-1000x faster Mermaid rendering. Pure Rust. Zero browser dependencies.**

[Installation](#installation) | [Quick Start](#quick-start) | [Benchmarks](#performance) | [Examples](#diagram-types)

</div>

## Performance

mmdr renders diagrams **100-1800x faster** than mermaid-cli by eliminating browser overhead.

<p align="center">
  <img src="docs/benchmarks/comparison.svg" alt="Performance comparison" width="600">
</p>

<div align="center">

| Diagram | mmdr | mermaid-cli | Speedup |
|:--------|-----:|------------:|--------:|
| Flowchart | 2.75 ms | 2,636 ms | **958x** |
| Class Diagram | 3.19 ms | 2,381 ms | **746x** |
| State Diagram | 2.45 ms | 2,647 ms | **1,080x** |
| Sequence Diagram | 2.47 ms | 2,444 ms | **990x** |

<sub>Tested on Intel Core Ultra 7 265V, Linux 6.18.2 | mermaid-cli 11.4.2 via Puppeteer/Chromium</sub>

</div>

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
| flowchart (small) | 10 | 2.75 ms | 2,636 ms | 958x |
| flowchart (medium) | 50 | 9.02 ms | 4,029 ms | 446x |
| flowchart (large) | 200 | 38.64 ms | 4,791 ms | 124x |

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
<td align="center" width="50%">
<strong>State Diagram</strong><br>
<img src="docs/comparisons/state_mmdr.svg" alt="State Diagram" width="100%">
</td>
<td align="center" width="50%">
<strong>Sequence Diagram</strong><br>
<img src="docs/comparisons/sequence_mmdr.svg" alt="Sequence Diagram" width="100%">
</td>
</tr>
</table>

<details>
<summary><strong>Compare with mermaid-cli output</strong></summary>

| Type | mmdr | mermaid-cli |
|:-----|:----:|:-----------:|
| Flowchart | <img src="docs/comparisons/flowchart_mmdr.svg" width="350"> | <img src="docs/comparisons/flowchart_official.svg" width="350"> |
| Class | <img src="docs/comparisons/class_mmdr.svg" width="350"> | <img src="docs/comparisons/class_official.svg" width="350"> |
| State | <img src="docs/comparisons/state_mmdr.svg" width="350"> | <img src="docs/comparisons/state_official.svg" width="350"> |
| Sequence | <img src="docs/comparisons/sequence_mmdr.svg" width="350"> | <img src="docs/comparisons/sequence_official.svg" width="350"> |
| ER Diagram | <img src="docs/comparisons/er_mmdr.svg" width="350"> | <img src="docs/comparisons/er_official.svg" width="350"> |
| Pie Chart | <img src="docs/comparisons/pie_mmdr.svg" width="35