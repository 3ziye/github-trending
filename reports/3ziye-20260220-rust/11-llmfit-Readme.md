# llmfit

<p align="center">
  <img src="assets/icon.svg" alt="llmfit icon" width="128" height="128">
</p>

**157 models. 30 providers. One command to find what runs on your hardware.**

A terminal tool that right-sizes LLM models to your system's RAM, CPU, and GPU. Detects your hardware, scores each model across quality, speed, fit, and context dimensions, and tells you which ones will actually run well on your machine.

Ships with an interactive TUI (default) and a classic CLI mode. Supports multi-GPU setups, MoE architectures, dynamic quantization selection, and speed estimation.

### Quick install (macOS / Linux)

```sh
curl -fsSL https://llmfit.axjns.dev/install.sh | sh
```
_Downloads the latest release binary from GitHub and installs it to `/usr/local/bin` (or `~/.local/bin`)_

Or
```sh
brew tap AlexsJones/llmfit
brew install llmfit
```

Windows users: see the **Install** section below.

![demo](demo.gif)

Example of a medium performance home laptop

![home](home_laptop.png)


Example of models with Mixture-of-Experts architectures

![moe](moe.png)

Downloading a model via Ollama integration

![download](download.gif)
---

## Install

### Cargo (Windows / macOS / Linux)

```sh
cargo install llmfit
```

If `cargo` is not installed yet, install Rust via [rustup](https://rustup.rs/).

### macOS / Linux

#### Homebrew

```sh
brew tap AlexsJones/llmfit
brew install llmfit
```

#### Quick install

```sh
curl -fsSL https://llmfit.axjns.dev/install.sh | sh
```

Downloads the latest release binary from GitHub and installs it to `/usr/local/bin` (or `~/.local/bin`).

### From source

```sh
git clone https://github.com/AlexsJones/llmfit.git
cd llmfit
cargo build --release
# binary is at target/release/llmfit
```

---

## Usage

### TUI (default)

```sh
llmfit
```

Launches the interactive terminal UI. Your system specs (CPU, RAM, GPU name, VRAM, backend) are shown at the top. Models are listed in a scrollable table sorted by composite score. Each row shows the model's score, estimated tok/s, best quantization for your hardware, run mode, memory usage, and use-case category.

| Key | Action |
|---|---|
| `Up` / `Down` or `j` / `k` | Navigate models |
| `/` | Enter search mode (partial match on name, provider, params, use case) |
| `Esc` or `Enter` | Exit search mode |
| `Ctrl-U` | Clear search |
| `f` | Cycle fit filter: All, Runnable, Perfect, Good, Marginal |
| `p` | Open provider filter popup |
| `i` | Toggle installed-first sorting (Ollama only) |
| `d` | Pull/download selected model via Ollama |
| `r` | Refresh installed models from Ollama |
| `1`-`9` | Toggle provider visibility |
| `Enter` | Toggle detail view for selected model |
| `PgUp` / `PgDn` | Scroll by 10 |
| `g` / `G` | Jump to top / bottom |
| `q` | Quit |

### CLI mode

Use `--cli` or any subcommand to get classic table output:

```sh
# Table of all models ranked by fit
llmfit --cli

# Only perfectly fitting models, top 5
llmfit fit --perfect -n 5

# Show detected system specs
llmfit system

# List all models in the database
llmfit list

# Search by name, provider, or size
llmfit search "llama 8b"

# Detailed view of a single model
llmfit info "Mistral-7B"

# Top 5 recommendations (JSON, for agent/script consumption)
llmfit recommend --json --limit 5

# Recommendations filtered by use case
llmfit recommend --json --use-case coding --limit 3
```

### JSON output

Add `--json` to any subcommand for machine-readable output:

```sh
llmfit --json system     # Hardware specs as JSON
llmfit --json fit -n 10  # Top 10 fits as JSON
llmfit recommend --json  # Top 5 recommendations (JSON is default for recommend)
```

---

## How it works

1. **Hardware detection** -- Reads total/available RAM via `sysinfo`, counts CPU cores, and probes for GPUs:
   - **NVIDIA** -- Multi-GPU support via `nvidia-smi`. Aggregates VRAM across all detected GPUs. Falls back to VRAM estimation from GPU model name if reporting fails.
   - **AMD** -- Detected via `rocm-smi`.
   - **Intel Arc** -- Discrete VRAM via sysfs, integrated via `lspci`.
   - **Apple Silicon** -- Unified memory via `system_profiler`. VRAM = system RAM.
   - **Backend detection** -- Automatically identifies the acceleration backend (CUDA, Metal, ROCm, SYCL, CPU ARM, CPU x86) for speed estimation.

2. **Model database** -- 157 models sourced from the HuggingFace API, stored in `data/hf_models.json` and embedded at compile time. Memory requirements are computed from parameter counts across a quantization hierarchy (Q8_0 through Q2_K). VRAM is the primary constraint for GPU inference; system RAM is the fallback for CPU-only execution.

   **MoE support** -- Models with Mixture-of-Experts architectures (Mixtral, DeepSeek-V2/V3) are detected automatically. Only a subset of experts is active per token, so the effective VRAM requirement is much lower than total parameter count suggests. For example, Mixtral 8x7B has 46.7B total parameters but only activates ~12.9B per token, reducing VRAM from 23.9 GB to ~6.6 GB wi