# FlashRT

**FlashRT is a high-performance realtime inference engine for small-batch, latency-sensitive AI workloads.**

A general kernel library composed into static graphs — no ONNX export, no engine compilation, no per-driver rebuild. Hand-written kernels (norm / activation / fusion / RoPE / FP8 / NVFP4 GEMM / attention) cover standard transformer, DiT, and SigLIP primitives. The composition pattern itself is hardware-agnostic; today the codebase ships with NVIDIA implementations spanning edge to server (Jetson AGX Thor through A100 / RTX 4090 / 5090).

The flagship integration today is **VLA control** — production frontends for Pi0, Pi0.5, GROOT N1.6, GROOT N1.7, and Pi0-FAST, validated on LIBERO where applicable. The same kernel set also powers the BAGEL world-model image-generation pipeline (research preview) and audio / video generation (4× over PyTorch). FlashRT now also serves **single-stream LLM inference** — the v1 release ships **Qwen3.6-27B (NVFP4)** with **256 K context on a single RTX 5090**, an OpenAI-compatible HTTP server, and warm decode throughput from **~120 tok/s at 512-token prompts to ~130 tok/s at 256 K** (peak measured bucket: **176 tok/s at 64 K**; see [Performance](#performance)). The pattern is workload-shaped (small-batch realtime), not model-class-shaped.

Existing inference tooling is shaped for different workloads — TensorRT for tactic-search compile to frozen engines, vLLM / SGLang for high-batch LLM serving. FlashRT targets the small-batch realtime cell with hand-tuned kernels and no compile step.

## FlashRT is fast with:

- **hand-written CUDA kernels**: norm, activation, residual+norm+quant fusion, RoPE / qkv-split, FP8 / NVFP4 GEMM, cuBLASLt FP8, CUTLASS SM100 FP8, vendored Flash-Attention 2, Thor CUTLASS FMHA
- **Static CUDA Graph capture** of the entire forward — zero Python overhead at replay
- **Production FP8 (E4M3) and NVFP4** with automatic per-tensor calibration, JSON-cached to disk
- **No compile, no export**: direct safetensors / Orbax loading, first call ~3 s, every call after is graph replay
- Survives CUDA driver upgrades, GPU swaps, and prompt changes without rebuild

## FlashRT is easy to use with:

- **3-line API**: `flash_rt.load_model(...).predict(images, prompt)`
- **Auto-dispatched hardware**: same code path on Jetson Thor / RTX 5090 / RTX 4090
- **PyTorch and JAX frontends** share one kernel binary, equivalent results (cosine ≥ 0.999)
- **Plugin model registration** — add a new VLA via one frontend file + a declarative `WEIGHT_SPEC`, no fork required
- **LIBERO benchmark integration** out of the box; ~6 minutes from `git clone` to first inference

## FlashRT supports:

- **VLA models**: Pi0, Pi0.5, GROOT N1.6, GROOT N1.7, Pi0-FAST. Pi0/Pi0.5/GROOT N1.6/Pi0-FAST are production-validated on LIBERO; GROOT N1.7 currently exposes an RTX SM120 DiT FA2 path. Motus RTX beta — Wan2.2-based robot policy path at ~167 ms / ~100 ms with TeaCache. BAGEL world-model (research preview) — image-gen pipeline at ~4× vs PyTorch.
- **LLM**: **Qwen3.6-27B NVFP4 — FP8-KV long-context decode to 256 K on one RTX 5090** — speculative decoding via the FP8 ckpt's MTP head, OpenAI-compatible HTTP server, **130 tok/s at 256 K** and **176 tok/s at 64 K** in the warm 64-token table. **Qwen3-8B NVFP4** text-only serving reaches **150 tok/s** warm decode.
- **Hardware (today)**: NVIDIA Jetson AGX Thor (SM110), RTX 5090 (SM120), RTX 4090 (SM89), and SM80 / SM86 / SM89 cards (A100, RTX 3090, 4060 Ti, etc.). The kernel composition pattern is portable to other accelerators.
- **Frameworks**: PyTorch (safetensors) + JAX (Orbax) — same compiled kernels

Pi0.5: 44 ms / 23 Hz on Jetson AGX Thor (2v, FP8) · 39.78 ms / 25 Hz (2v, NVFP4) · 17.58 ms / 57 Hz on RTX 5090. Cosine ≥ 0.9996 vs the production reference. See [Performance](#performance) for the full sweep.

## News

- [2026/05] **Qwen3.6-27B NVFP4** is supported with 256 K context on a single RTX 5090, OpenAI-compatible serving, FP8-KV long-context verify, and **130 tok/s warm decode at 256 K**. See [Qwen3.6 NVFP4](docs/qwen36_nvfp4.md) and [Performance](#qwen36-performance).
- [2026/05] **Qwen3-8B NVFP4** text-only serving is supported on RTX 5090, with **9.1 ms TTFT at P=64** and **150 tok/s** warm decode. See [Qwen3-8B NVFP4](docs/qwen3_8b_nvfp4.md) and [Performance](#qwen3-8b-performance).
- [2026/05] **Wan2.2 TI2V-5B** official-pipeline baseline is available on RTX SM120, with opt-in TeaCache acceleration. See [Wan2.2 usage](docs/wan22_usage.md).
- [2026/05] **Lingbot-VLA** is supported. See [Lingbot usage](https://github.com/LiangSu8899/FlashRT/blob/main/docs/lingbot_usage.md).
- [2026/05] Community Pi0.5 hardware benchmarks: thanks to [@cuihengrui35](https://github.com/cuihengrui35) for **RTX 5060 Ti** results (**41.4 ms / ~24 Hz**, plus LIBERO Spatial **344/350 = 98.3%**) and [@wangerforcs](https://github.com/wangerforcs) for **NVIDIA L40** results (**26.6 ms / 38 Hz**) on 2-view FP8. See [community benchmarks](#community-benc