```
 _   _
| | | |_   _ _ __  _   _ _ __ __ _
| |_| | | | | '_ \| | | | '__/ _` |
|  _  | |_| | |_) | |_| | | | (_| |
|_| |_|\__, | .__/ \__,_|_|  \__,_|
       |___/|_|
   Run models too big for your Mac's memory
```

Hypura is a storage-tier-aware LLM inference scheduler for Apple Silicon.
It places model tensors across GPU, RAM, and NVMe tiers based on access
patterns, bandwidth costs, and hardware capabilities — enabling models
that exceed physical memory to run without crashing the system.

Run a 31 GB Mixtral 8x7B on a 32 GB Mac Mini at 2.2 tok/s. A 40 GB Llama 70B at 0.3 tok/s. Vanilla llama.cpp crashes on both.

## Why does this matter?

Consumer hardware (MacBook Pro, Mac Studio) ships with fast unified memory
and NVMe storage, but limited capacity. A 32 GB M1 Max cannot naively load
a 40 GB model — the OS will swap-thrash until the OOM killer intervenes.

Hypura solves this by understanding the model architecture:

- **Norms and embeddings** are tiny but accessed every token — pinned to GPU
- **MoE expert routing** exploits sparsity — only 2 of 8 experts fire per token.
  Router interception identifies selected experts in the eval callback, then loads
  only the needed expert strides from NVMe (75% I/O reduction). A neuron cache tracks
  loaded expert slices across tokens, achieving 99.5% hit rate from temporal locality.
  Co-activation tracking predicts which experts will fire next for speculative prefetch.
- **Dense FFN weights** (gate, up, down — ~60% of model size) stream from NVMe through
  a dynamically-sized pool buffer while attention + norms stay GPU-resident. Prefetch
  lookahead depth scales automatically with available memory.

The result: models that would crash your machine under naive mmap become runnable.
Models that fit in memory run at full Metal GPU speed with zero overhead.

## How it works

Hypura reads the GGUF file, profiles your hardware (GPU working set, RAM, NVMe bandwidth),
and solves a placement optimization that assigns every tensor to a tier:

- **GPU (Metal)** — Attention layers, norms, embeddings. Fastest access, limited by `recommendedMaxWorkingSetSize`.
- **RAM** — Overflow layers that don't fit in the GPU working set. Accessed via mmap.
- **NVMe** — Remaining layers loaded on-demand via direct I/O (`F_NOCACHE` + `pread`), prefetched ahead of the forward pass.

Hypura selects the best inference mode automatically based on model size, architecture, and available memory:

- **Full-resident** — Model fits in GPU+RAM. No NVMe I/O. Full Metal speed.
- **Expert-streaming** — For MoE models (Mixtral). Only non-expert tensors (~1 GB) stay on GPU. Expert tensors stream from NVMe through a pool buffer on demand, with a neuron cache (99.5% hit rate) that eliminates most I/O after warmup.
- **Dense FFN-streaming** — For dense models too large for GPU (Llama 70B). Attention + norms stay on GPU (~8 GB). FFN tensors (~32 GB) stream from NVMe through a dynamically-sized pool buffer, with scaled prefetch lookahead.

Pool buffer size, prefetch depth, and memory budgets are computed automatically from your hardware profile — no manual tuning needed.

## Performance

All benchmarks on **M1 Max, 32 GB unified memory, ~5.1 GB/s NVMe sequential read**.

| Model | Size | GPU | NVMe | Mode | Hypura | llama.cpp | Notes |
|---|---|---|---|---|---|---|---|
| Qwen 2.5 14B Q4_K_M | 8.4 GB | 8.4 GB | — | full-resident | **21 tok/s** | ~21 tok/s | Fits in GPU; no overhead |
| Mixtral 8x7B Q5_K_M | 30.9 GB | 1.1 GB | 29.8 GB | expert-streaming | **2.2 tok/s** | **OOM** | All layers on Metal; 99.5% cache hit rate |
| Llama 3.3 70B Q4_K_M | 39.6 GB | 7.8 GB | 31.8 GB | dense-FFN-streaming | **0.3 tok/s** | **OOM** | All layers on Metal; dynamic 24-slot pool, 7-layer prefetch |

**Key takeaway:** For models that fit in memory, Hypura adds zero overhead. For models that don't fit, Hypura is the difference between "runs" and "crashes." Expert-streaming on Mixtral achieves usable interactive speeds by keeping only non-expert tensors on GPU and exploiting MoE sparsity (only 2/8 experts fire per token). Dense FFN-streaming extends this to non-MoE models like Llama 70B. Pool sizes and prefetch depth scale automatically with available memory.

## Install

Hypura builds from source with Cargo. You'll need Rust 1.75+ and CMake (for the vendored llama.cpp).

```sh
git clone --recurse-submodules https://github.com/hypura/hypura.git
cd hypura
cargo build --release
```

The binary is at `target/release/hypura`.

> Homebrew tap coming soon.

## Quick start

```sh
# Profile your hardware (runs once, cached)
hypura profile

# Run inference on a GGUF model
hypura run ./model.gguf --prompt "Hello, world"

# Interactive chat
hypura run ./model.gguf --interactive

# Benchmark: Hypura scheduling vs naive baseline
hypura bench ./model.gguf

# Inspect model placement plan without loading
hypura inspect ./model.gguf
```

Start with `--max-tokens 10` on untested models before scaling up.

## Ollama-compatible server

Hypura