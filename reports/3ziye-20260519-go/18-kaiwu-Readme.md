<div align="center">

# Kaiwu · 开物

**Auto-tuned local LLM serving: Kaiwu probes your hardware, model, KV cache, and context window so you get the fastest OpenAI-compatible endpoint your machine can actually sustain.**

**自动调优本地大模型：Kaiwu 探测你的硬件、模型、KV cache 和上下文窗口，给你一个机器能稳定跑出的最快 OpenAI 兼容端点。**

[English](#english) · [中文](#中文)

</div>

---

<a name="english"></a>
# Kaiwu

LM Studio and Ollama make models run. Kaiwu makes them run *well* — by measuring, not guessing.

It probes your GPU, reads the model architecture, benchmarks KV cache options, and walks the context window down from the model's native maximum until it finds the largest window your hardware can sustain at a useful speed. That config is cached. Second launch takes 2 seconds.

## Proof

### 30B MoE on 8GB GPU — the hard case

Model: Qwen3-30B-A3B Q3_K_XL · RTX 5060 Laptop 8GB · Windows 11

| | LM Studio | Kaiwu |
|---|---|---|
| Speed | 3 tok/s | **8.7 tok/s** |
| Context window | 4K (default) | **32K (auto)** |
| VRAM used | 7,549 MB (93%) | 4,800 MB (59%) |
| Config required | Manual | **None** |

LM Studio fills VRAM trying to load the full model. Kaiwu detects the MoE architecture, keeps attention layers on GPU, routes 128 expert layers through CPU — usable speed at 32K context on hardware that can't fit the model at all.

### 8B dense — everyday use

Model: Llama 3.1 8B Q5_K_M · RTX 5060 8GB

| | LM Studio | Kaiwu |
|---|---|---|
| Speed (8K ctx) | 46.5 tok/s | **51.7 tok/s** |
| Context window | 4–8K (default) | **64K (auto)** |

Same speed, 8× more context. Kaiwu calculates whether f16 KV cache fits in VRAM and uses it when it does — matching LM Studio's speed while running a much larger context window.

### Dual 4090 — high-end

Model: Qwen3.6-35B-A3B · 2× RTX 4090 24GB

- **115 tok/s** · **256K context** · fully automatic tensor split

## How It Works

```
kaiwu run Qwen3-30B-A3B
```

That's it. Kaiwu:

1. **Probes your hardware** — GPU model, VRAM, memory bandwidth, SM version, CPU cores, RAM
2. **Reads the model** — architecture, layer count, KV heads, native context limit, MoE structure
3. **Selects KV cache** — calculates f16 footprint; uses f16 if it fits, q8_0+q4_0 if not, iso3 for tight VRAM
4. **Runs warmup benchmark** — walks ctx from native max downward, stops where speed ≥ 20 tok/s
5. **Tunes parameters** — ubatch size, thread count, mlock — all measured, not guessed
6. **Caches the result** — next launch skips warmup entirely (2s startup)

On subsequent runs:

```
✓ Using last config  (64K ctx · 26.2 tok/s · 3 days ago)
```

## Installation

**Windows** (PowerShell):
```powershell
irm https://raw.githubusercontent.com/val1813/kaiwu/main/install.ps1 | iex
```

**Linux / macOS**:
```bash
curl -fsSL https://raw.githubusercontent.com/val1813/kaiwu/main/install.sh | sh
```

Or download manually from [Releases](https://github.com/val1813/kaiwu/releases).

## Quick Start

```bash
# Run a model (auto-downloads if needed)
kaiwu run Qwen3-30B-A3B

# Run a local GGUF file
kaiwu run /path/to/model.gguf

# Connect your IDE (Continue, Cursor, Claude Code)
# Point it to: http://localhost:11435/v1

# Check what's running
kaiwu status

# Stop
kaiwu stop
```

The API is OpenAI-compatible. Any tool that works with the OpenAI API works with Kaiwu.

## Advanced Usage

```bash
# Override context size
kaiwu run Qwen3-8B --ctx-size 12000

# Force re-tune (after hardware change)
kaiwu run Qwen3-8B --reset

# Fast start — skip warmup, use cached config only
kaiwu run Qwen3-8B --fast

# List available models
kaiwu list

# Inject IDE config automatically
kaiwu inject
```

## What Gets Auto-Tuned

| Parameter | How Kaiwu decides |
|---|---|
| Context length | Walks from model's native max down; stops where speed ≥ 20 tok/s |
| KV cache type | Calculates f16 footprint; uses f16 → q8_0+q4_0 → iso3 by VRAM fit |
| MoE expert placement | Detects `.ffn_.*_exps.` tensors; routes to CPU automatically |
| ubatch size | Benchmarks 128 vs 512; picks the faster one |
| Thread count | 2 for full-GPU, physical_cores/2 for MoE offload |
| mlock | Enabled when RAM headroom > 30% |
| GPU tensor split | Weighted by VRAM × bandwidth when multiple GPUs detected |

## Requirements

- **GPU**: NVIDIA (CUDA) — 4GB+ VRAM recommended
- **Driver**: ≥ 550.54 (Windows) / ≥ 550.54 (Linux) — required for CUDA 12.4 runtime bundled with Kaiwu
  - Check: `nvidia-smi` → look for "Driver Version"
  - Update at: [nvidia.com/drivers](https://www.nvidia.com/drivers)
- **OS**: Windows 10/11, Linux (Ubuntu 20.04+)
- **RAM**: 8GB+ (16GB+ for 30B MoE models)
- **Model format**: GGUF

CPU-only inference is supported but not the focus.

## Commands

| Command | What it does |
|---|---|
| `run <model>` | Start a model. Downloads if needed. |
| `stop` | Stop the running model. |
| `status` | Show running model, speed, VRAM usage. |
| `list` | List available and downloaded models. |
| `probe` | Show detected hardware. |
| `inject` | Configure Continue/Cursor to use Kaiwu. |
| `version` | Show versi