# llmfit

<p align="center">
  <img src="assets/icon.svg" alt="llmfit icon" width="128" height="128">
</p>

**497 models. 133 providers. One command to find what runs on your hardware.**

A terminal tool that right-sizes LLM models to your system's RAM, CPU, and GPU. Detects your hardware, scores each model across quality, speed, fit, and context dimensions, and tells you which ones will actually run well on your machine.

Ships with an interactive TUI (default) and a classic CLI mode. Supports multi-GPU setups, MoE architectures, dynamic quantization selection, and speed estimation.

> **Sister project:** Check out [kubeclaw](https://github.com/AlexsJones/kubeclaw/) for managing agents in Kubernetes.

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

Downloads the latest release binary from GitHub and installs it to `/usr/local/bin` (or `~/.local/bin` if no sudo).

**Install to `~/.local/bin` without sudo:**

```sh
curl -fsSL https://llmfit.axjns.dev/install.sh | sh -s -- --local
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
| `s` | Cycle sort column: Score, Params, Mem%, Ctx, Date, Use Case |
| `t` | Cycle color theme (saved automatically) |
| `p` | Open provider filter popup |
| `i` | Toggle installed-first sorting (Ollama only) |
| `d` | Pull/download selected model via Ollama |
| `r` | Refresh installed models from Ollama |
| `1`-`9` | Toggle provider visibility |
| `Enter` | Toggle detail view for selected model |
| `PgUp` / `PgDn` | Scroll by 10 |
| `g` / `G` | Jump to top / bottom |
| `q` | Quit |

### Themes

Press `t` to cycle through 6 built-in color themes. Your selection is saved automatically to `~/.config/llmfit/theme` and restored on next launch.

| Theme | Description |
|---|---|
| **Default** | Original llmfit colors |
| **Dracula** | Dark purple background with pastel accents |
| **Solarized** | Ethan Schoonover's Solarized Dark palette |
| **Nord** | Arctic, cool blue-gray tones |
| **Monokai** | Monokai Pro warm syntax colors |
| **Gruvbox** | Retro groove palette with warm earth tones |

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

### GPU memory override

GPU VRAM autodetection can fail on some systems (e.g. broken `nvidia-smi`, VMs, passthrough setups). Use `--memory` to manually specify your GPU's VRAM:

```sh
# Override with 32 GB VRAM
llmfit --memory=32G

# Megabytes also work (32000 MB ≈ 31.25 GB)
llmfit --memory=32000M

# Works with all modes: TUI, CLI, and subcommands
llmfit --memory=24G --cli
llmfit --memory=24G fit --perfect -n 5
llmfit --memory=24G system
llmfit --memory=24G info "Llama-3.1-70B"
llmfit --memory=24G recommend --json
```

Accepted suffixes: `G`/`GB`/`GiB` (gigabytes), `M`/`MB`/`MiB` (megabytes), `T`/`TB`/`TiB` (terabytes). Case-insensitive. If no GPU was detected, the override creates a synthetic GPU entry so models are scored for GPU i