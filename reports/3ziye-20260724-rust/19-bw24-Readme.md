# bw24 — from-scratch LLM inference for sm_120a (RTX 50-series Blackwell)

[![ci](https://github.com/avifenesh/bw24/actions/workflows/ci.yml/badge.svg)](https://github.com/avifenesh/bw24/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Rust](https://img.shields.io/badge/rust-edition%202024-orange.svg)
![CUDA](https://img.shields.io/badge/CUDA-12.8%20%2F%2013.1-76B900.svg)
![arch](https://img.shields.io/badge/arch-sm__120a%20(Blackwell)-black.svg)

![bw24 vs llama.cpp perf board](docs/perf-card.svg)

From-scratch LLM inference engine in Rust + CUDA, built for one machine: an RTX 5090 Laptop (Blackwell sm_120a, 24 GB). No frameworks, no ggml — every kernel written and tuned against measured hardware limits, with llama.cpp as the benchmark to beat on the same rig.

The headline capability is **MTP speculative decoding**: up to 2.3x over llama.cpp's best spec config, leading on every supported Qwen model and prompt class (1.06-2.30x per cell), with trimmed drafter heads published ready-to-use ([huggingface.co/Avifenesh/bw24-bench](https://huggingface.co/Avifenesh/bw24-bench)) — behind a drop-in OpenAI-compatible server. Exactness is the contract: speculative output is gated token-identical to plain decode, so the speedup never changes what the model says.

**Use bw24 when** you serve one model to one user on an RTX 50-series card and want measured, exactness-gated speed. **Use something else when** you have any other GPU ([llama.cpp](https://github.com/ggml-org/llama.cpp), [mistral.rs](https://github.com/EricLBuehler/mistral.rs)) or need multi-GPU / batched serving (vLLM, SGLang).

Running bw24 on your own rig — desktop 50-series, older NVIDIA, anything? A [hardware validation report](.github/ISSUE_TEMPLATE/hardware-validation.md) is the fastest way to help: 50-series reports bless the rest of the family, older-card reports map the compatibility floor.

**Current standing: seven supported models, all fully gated, and no plain cell anywhere below llama.cpp (2026-07-24). Qwen leads on every cell (plain 1.06-1.08x, spec 1.06-2.30x). Gemma leads decisively where llama lacks the capability or the depth (31B spec 1.7k 1.16x, E4B spec ≥1.23x, E4B plain 1.10x) and holds 1.00-1.07x elsewhere under the strictest best-vs-best pairing (12B bring-up closed 2026-07-24; 26B/31B/E4B re-audit 2026-07-15).** Every number below is a same-session, same-prompt, interleaved measurement against llama.cpp's best config; exactness is gated (argmax match + speculative self-consistency) on every kernel change, so speed never buys different outputs.

## Model support

| Tier | Models | State |
|---|---|---|
| **Supported** | Qwen3.5-9B, Qwen3.6-27B, Qwen3.6-35B-A3B MoE (NVFP4/IQ4_XS); Gemma-4 12B dense, 26B-A4B MoE, 31B dense, E4B (QAT Q4_0 + MTP drafters) | Board-published, fully gated, exactness-first; margins per model in the tables below |
| **Supported, under tuning** | Hy3 Layer103.5 overlay (VRAM→RAM→dual-NVMe spill) | Runs end-to-end through bw24-native CPU/GPU serving, correctness-gated on the 5090 target; see [docs/HY3-SPILL.md](docs/HY3-SPILL.md) |
| **In progress** | MiniMax-M3 REAP50 (safetensors, VRAM→RAM→NVMe spill) | Loads + generates; hybrid/sigmoid-router tuning remains open |

## Quick start

Prebuilt Linux x86_64 binaries (sm_120a) ship with each [release](https://github.com/avifenesh/bw24/releases) — or build from source:

```bash
cargo build --release
./target/release/kernel-check                     # every kernel vs CPU reference
BW24_CHAT=1 ./target/release/run-gen /path/to/model.gguf --prompt "Explain KV caches."
BW24_SPEC_K=3 ./target/release/run-spec /path/to/qwen36-27b.gguf   # MTP speculative
./target/release/run-gen hf:owner/repo:Q4_K_M --prompt "hi"        # auto-download from HF (needs `hf` CLI)
./target/release/frspec-owngen model.gguf trim.gguf --validate     # build + validate an FR-Spec draft trim from the model's OWN generations
./target/release/bw24-server                      # OpenAI-compatible /v1
```

Expected output — `kernel-check` ends with:

```
ALL GREEN: kernels match CPU reference.
```

and `run-gen` prints its correctness gate before any generation:

```
verify-prefill argmax=N  decode argmax=N  logit maxdiff=...  MATCH
```

Tuned paths are the defaults — no flags needed. Flags exist only for runtime parameters, machine config, and rollback seams (`docs/FLAGS.md`). A MISMATCH line from the gate voids every number after it.

Serving Hy3 (a ~100 GB expert bank) on this 24 GB card uses a frozen HBM resident set, a bounded host cache, and positioned dual-NVMe reads — runbook, ABI safety notes, and current gate results in [docs/HY3-SPILL.md](docs/HY3-SPILL.md).
The paired native AVX-VNNI Q2_K path raises the local N=32 median from 4.37 to 4.60 tok/s across three interleaved, correctness-identical pairs (+5.3% by arm medians; [receipt](research/per-expert-quant/evidence/local-5090-native-next-20260721/q2k-avxvnni-pair-win.md)).

## Perfor