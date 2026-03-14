# llmfit

<p align="center">
  <img src="assets/icon.svg" alt="llmfit icon" width="128" height="128">
</p>
<p align="center">
  <a href="https://github.com/AlexsJones/llmfit/actions/workflows/ci.yml"><img src="https://github.com/AlexsJones/llmfit/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://crates.io/crates/llmfit"><img src="https://img.shields.io/crates/v/llmfit.svg" alt="Crates.io"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"></a>
</p>

**Hundreds of models & providers. One command to find what runs on your hardware.**

A terminal tool that right-sizes LLM models to your system's RAM, CPU, and GPU. Detects your hardware, scores each model across quality, speed, fit, and context dimensions, and tells you which ones will actually run well on your machine.

Ships with an interactive TUI (default) and a classic CLI mode. Supports multi-GPU setups, MoE architectures, dynamic quantization selection, speed estimation, and local runtime providers (Ollama, llama.cpp, MLX).

> **Sister project:** Check out [sympozium](https://github.com/AlexsJones/sympozium/) for managing agents in Kubernetes.

![demo](demo.gif)

---

## Install

### Windows
```sh
scoop install llmfit
```

If Scoop is not installed, follow the [Scoop installation guide](https://scoop.sh/).

### macOS / Linux

#### Homebrew
```sh
brew install llmfit
```

#### Quick install
```sh
curl -fsSL https://llmfit.axjns.dev/install.sh | sh
```

Downloads the latest release binary from GitHub and installs it to `/usr/local/bin` (or `~/.local/bin` if no sudo).

**Install to `~/.local/bin` without sudo:**
```sh
curl -fsSL https://llmfit.axjns.dev/install.sh | sh -s -- --local
```

### Docker / Podman
```sh
docker run ghcr.io/alexsjones/llmfit
```
This prints JSON from `llmfit recommend` command. The JSON could be further queried with `jq`.
```
podman run ghcr.io/alexsjones/llmfit recommend --use-case coding | jq '.models[].name'
```

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
| `a` | Cycle availability filter: All, GGUF Avail, Installed |
| `s` | Cycle sort column: Score, Params, Mem%, Ctx, Date, Use Case |
| `v` | Enter Visual mode (select multiple models) |
| `V` | Enter Select mode (column-based filtering) |
| `t` | Cycle color theme (saved automatically) |
| `p` | Open Plan mode for selected model (hardware planning) |
| `P` | Open provider filter popup |
| `U` | Open use-case filter popup |
| `C` | Open capability filter popup |
| `m` | Mark selected model for compare |
| `c` | Open compare view (marked vs selected) |
| `x` | Clear compare mark |
| `i` | Toggle installed-first sorting (any detected runtime provider) |
| `d` | Download selected model (provider picker when multiple are available) |
| `r` | Refresh installed models from runtime providers |
| `Enter` | Toggle detail view for selected model |
| `PgUp` / `PgDn` | Scroll by 10 |
| `g` / `G` | Jump to top / bottom |
| `q` | Quit |

### Vim-like modes

The TUI uses Vim-inspired modes shown in the bottom-left status bar. The current mode determines which keys are active.

#### Normal mode

The default mode. Navigate, search, filter, and open views. All keys in the table above apply here.

#### Visual mode (`v`)

Select a contiguous range of models for bulk comparison. Press `v` to anchor at the current row, then navigate with `j`/`k` or arrow keys to extend the selection. Selected rows are highlighted.

| Key | Action |
|---|---|
| `j` / `k` or arrows | Extend selection up/down |
| `c` | Compare all selected models (opens multi-compare view) |
| `m` | Mark current model for two-model compare |
| `Esc` or `v` | Exit Visual mode |

The multi-compare view displays a table where rows are attributes (Score, tok/s, Fit, Mem%, Params, Mode, Context, Quant, etc.) and columns are models. Best values are highlighted. Use `h`/`l` or arrow keys to scroll horizontally if more models are selected than fit on screen.

#### Select mode (`V`)

Column-based filtering. Press `V` (shift-v) to enter Select mode, then use `h`/`l` or arrow keys to move between column headers. The active column is visually highlighted. Press `Enter` or `Space` to activate the appropriate filter for that column:

|