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
| `t` | Cycle color theme (saved automatically) |
| `p` | Open Plan mode for selected model (hardware planning) |
| `P` | Open provider filter popup |
| `i` | Toggle installed-first sorting (any detected runtime provider) |
| `d` | Download selected model (provider picker when multiple are available) |
| `r` | Refresh installed models from runtime providers |
| `1`-`9` | Toggle provider visibility |
| `Enter` | Toggle detail view for selected model |
| `PgUp` / `PgDn` | Scroll by 10 |
| `g` / `G` | Jump to top / bottom |
| `q` | Quit |

### TUI Plan mode (`p`)

Plan mode inverts normal fit analysis: instead of asking "what fits my hardware?", it estimates "what hardware is needed for this model config?".

Use `p` on a selected row, then:

| Key | Action |
|---|---|
| `Tab` / `j` / `k` | Move between editable fields (Context, Quant, Target TPS) |
| `Left` / `Right` | Move cursor in current field |
| Type | Edit current field |
| `Backspace` / `Delete` | Remove characters |
| `Ctrl-U` | Clear current field |
| `Esc` or `q` | Exit Plan mode |

Plan mode shows estimates for:
- minimum and recommended VRAM/RAM/CPU cores
- feasible run paths (GPU, CPU offload, CPU-only)
- upgrade deltas to reach better fit targets

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
llm