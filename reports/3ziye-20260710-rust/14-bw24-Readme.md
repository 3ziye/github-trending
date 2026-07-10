# bw24

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Rust](https://img.shields.io/badge/rust-edition%202024-orange.svg)
![CUDA](https://img.shields.io/badge/CUDA-12.8%20%2F%2013.1-76B900.svg)
![arch](https://img.shields.io/badge/arch-sm__120a%20(Blackwell)-black.svg)

![bw24 vs llama.cpp perf board](docs/perf-card.svg)

From-scratch LLM inference engine in Rust + CUDA, built for one machine: an RTX 5090 Laptop (Blackwell sm_120a, 24 GB, 175 W with dynamic boost). No frameworks, no ggml — every kernel written and tuned against measured hardware limits, with llama.cpp as the benchmark to beat on the same rig.

The [Performance](#performance) section and card above show same-session measurements against llama.cpp's best config. Primary format: **GGUF NVFP4** (chosen 2026-07-10 on long-context serving reliability). HF safetensors checkpoints also load directly — supported best-effort, see the note under Performance.

## Why this project

- Real, running inference on sm_120a (consumer Blackwell), with every shipped optimization backed by its measured win/loss record.
- Gated on bit-exactness — argmax match and speculative self-consistency, verified on every kernel change.
- Runs Qwen3.5/3.6 dense and MoE checkpoints on 24 GB — GGUF first-class, HF safetensors supported — including models far larger than VRAM+RAM.

## Requirements

- NVIDIA Blackwell consumer GPU (sm_120a). Primary target: RTX 5090 Laptop.
- CUDA toolkit 13.1 (the build default — `crates/bw24-engine/build.rs` uses `/usr/local/cuda-13.1/bin/nvcc`; override with `BW24_NVCC=/path/to/nvcc`).
- Rust (edition 2024), [cudarc](https://github.com/coreylowman/cudarc) 0.19 with dynamic loading.
- A model — GGUF or an HF safetensors directory (pass either path). Tested: Qwen3.5-9B, Qwen3.6-27B, Qwen3.6-35B-A3B MoE (common quants), nvidia/Qwen3.6-27B-NVFP4, MiniMax-M3 REAP50, Hy3-REAP50.

## Quick start

```bash
# build
cargo build --release

# verify all kernels against the CPU reference
./target/release/kernel-check

# generate text (the fast path is the default — no flags needed)
BW24_CHAT=1 ./target/release/run-gen /path/to/model.gguf --prompt "Explain KV caches in one paragraph."

# speculative decoding with the embedded MTP draft head (Qwen3.6)
BW24_SPEC_K=3 ./target/release/run-spec /path/to/qwen36-27b.gguf

# OpenAI-compatible server
./target/release/bw24-server
```

Every tuned kernel path is the default; environment flags exist only for runtime parameters (prompt, draft depth, trims), machine-specific configuration, and rollback seams (`BW24_FAST=0` drops to the f32 oracle path). The catalog lives in `docs/FLAGS.md`.

`run-gen` prints a prefill/decode correctness gate (prefill argmax must match decode argmax) before timing anything — if that line says MISMATCH, the numbers after it don't count.

## Workspace layout

| Crate | What it does |
|---|---|
| `bw24-engine` | Core: CUDA kernels (`cu/`), forward passes, speculative decoding, MoE cache, CUDA-graph decode |
| `bw24-gguf` | GGUF parser + tensor loading (memory-mapped) |
| `bw24-tokenizer` | BPE tokenizer + chat templates from GGUF metadata |
| `bw24-runtime` | CUDA device/stream/memory primitives over cudarc |
| `bw24-server` | HTTP server (axum), OpenAI-compatible `/v1` endpoints |
| `bw24-probe` | Standalone hardware microbenches (`probe/*.cu`: bandwidth, tensor-core peaks, layout experiments) |

## What's inside

- **NVFP4 (W4) decode path** — block-scaled FP4 matvec with split-plane repack, warp-level dp4a, and an int8 W4A8 tensor-core GEMM for prefill. Auto-dispatches per matrix shape.
- **MTP speculative decoding** — draft with the model's embedded multi-token-prediction head, verify K+1 tokens in one batched target forward. The whole draft chain runs inside a captured CUDA graph; exactness is enforced by a K=1..8 self-consistency gate (all K must emit identical tokens).
- **MoE on 24 GB** — expert-major CSR batching, decode-once dequant kernels, int8 tensor-core expert GEMM, and an SLRU expert-residency cache with VRAM → host → disk spill.
- **FlashAttention-style kernels** — fused prefill and decode attention with quantized KV (q8_0 K / q5_1 V default; FP8 and q4_0 arms exist behind flags — q4_0 V measured quality-taxed and stays off), register-resident dequant, split-K for long context.
- **CUDA-graph decode** — the full per-token decode is one graph replay; per-step host round-trip is 4 bytes.
- **Hybrid architectures** — full-attention + gated-delta-net (SSM) layer mixes, as in Qwen3.6.
- **Safetensors loader** — HF checkpoints load directly (no GGUF conversion): modelopt NVFP4 repacks byte-exact into the GGUF block layout, FP8-E4M3 and large-BF16 tensors re-encode to Q8_0/NVFP4 at load, V-head permutations apply on packed bytes, MoE experts stream through a disk-tier repack cache for models far bigger than VRAM+RAM.
- **Sigmoid-router MoE** (MiniMax/DeepSeek-style) — e_score_correction_bias selection, swigluoai activation, gate-optional attention; 