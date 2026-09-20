<div align="center">

<img src="assets/20260908-223115.jpg" alt="edge0" width="100%">

# edge0

**An open-source streaming MoE inference framework — SSD expert offload + Recover-LoRA + prerouter routing prediction.**

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Edge0--35B--A3B--preview-yellow?style=for-the-badge)](https://huggingface.co/Edge0/Edge0-35B-A3B-preview)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Edge0--8B--A1B--preview-yellow?style=for-the-badge)](https://huggingface.co/Edge0/Edge0-8B-A1B-preview)
[![ModelScope](https://img.shields.io/badge/ModelScope-Edge0--35B--A3B--preview-624AFF?style=for-the-badge)](https://www.modelscope.cn/models/Edge0/Edge0-35B-A3B-preview)
[![ModelScope](https://img.shields.io/badge/ModelScope-Edge0--8B--A1B--preview-624AFF?style=for-the-badge)](https://www.modelscope.cn/models/Edge0/Edge0-8B-A1B-preview)
[![arXiv](https://img.shields.io/badge/arXiv-2609.18063-B31B1B?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2609.18063)
[![GitHub](https://img.shields.io/badge/GitHub-Edge0--AI%2FEdge0-black?style=for-the-badge&logo=github)](https://github.com/Edge0-AI/Edge0)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue?style=for-the-badge)](LICENSE)

English | [中文](README_zh.md)

</div>

**edge0** is an open-source streaming MoE inference framework. It
generalizes the production-proven recipe — **SSD expert offload +
Recover-LoRA + prerouter routing prediction** — into an extensible
framework. The backend is isolated by design: the current MLX backend
runs on Apple Silicon, and additional platforms (CUDA, …) plug into the
same core abstractions.

Two model tiers ship with the framework. Each tier is an end-to-end
release: the released checkpoint, the trained LoRA adapters, and the
trained prerouter heads work together as one unit.

| Tier | Released checkpoint | Inference profile |
|---|---|---|
| `edge0-35b` | [`Edge0/Edge0-35B-A3B-preview`](https://huggingface.co/Edge0/Edge0-35B-A3B-preview) · [ModelScope](https://www.modelscope.cn/models/Edge0/Edge0-35B-A3B-preview) | 4-bit, 40 layers, 256 experts, prerouter K=4 |
| `edge0-8b` | [`Edge0/Edge0-8B-A1B-preview`](https://huggingface.co/Edge0/Edge0-8B-A1B-preview) · [ModelScope](https://www.modelscope.cn/models/Edge0/Edge0-8B-A1B-preview) | 4-bit, 24 layers, 128 experts, prerouter K=8 |

Both checkpoints are built on open sparse-MoE base models (Qwen3.6-35B-A3B
and the Ling 3.0 bailing hybrid respectively) and ship with the
LoRA and prerouter training done for this framework — the adapter files
are co-located with each checkpoint and load automatically, so
`edge0 serve <tier>` runs the trained pipeline out of the box.

## Requirements

- **OS / hardware**: the MLX backend runs on macOS with Apple Silicon
  (M1/M2/M3/M4). The CUDA backend is on the roadmap — no other
  platforms are supported yet.
- **Python**: 3.10+ (3.12 recommended).
- **MLX**: `mlx==0.30.6` / `mlx-metal==0.30.6` with `mlx-lm==0.31.0` (see
  `pyproject.toml`). Garbled, mixed-language output on Apple A18 / A18 Pro
  means an older `mlx`: `pip install 'mlx==0.30.6' 'mlx-metal==0.30.6'`
  ([#8](https://github.com/Edge0-AI/Edge0/issues/8)).
- **Memory**: ~2.9 GB peak active memory for `edge0-35b`, ~1.0 GB for
  `edge0-8b` (short contexts; see [Benchmark](#benchmark)). Add
  headroom for the OS, tokenizer, and long-context KV growth.
- **Disk**: the 4-bit checkpoints are ~23 GB (`edge0-35b`) and ~4.2 GB
  (`edge0-8b`); expert weights are mmapped and read on demand, they are
  not loaded into RAM up front.

## Design

- **transformers-style usage**: `AutoModel` / `AutoConfig` / `AutoEngine`
  resolve the tier from the model name;
- **Backend isolation**: all MLX code lives under `edge0/backends/mlx/`;
  the core logic (model specs, prerouter, streaming expert pool, server)
  depends only on the backend facade (`edge0/backends/base.py`), so a new
  backend implements the same facade (`backends/cuda/` is a reserved
  slot) with zero changes to core code;
- **Adapters as safetensors**: LoRA and prerouter weights are
  `.safetensors` files with provenance metadata (source, version, owner
  layers), resolved from the model directory or `artifacts/`;
- **Model + adapters in one directory**: a model directory holds both
  the base checkpoint (`config.json` / `model*.safetensors` / tokenizer)
  and that model's adapters; upgrading adapters swaps adapter
  files only — the base stays read-only and is never merged.

## Core mechanisms

- **SSD expert offload**: expert weights are streamed from storage on
  demand; peak memory is bounded by the active set, not the parameter
  count.
- **Prerouter**: a trained head predicts expert routing one step
  ahead, so expert loads overlap the forward pass instead of stalling
  it — **up to +59%** decode throughput; the gain grows with storage
  latency, model size, and routed width *K*.
- **Recover-LoRA**: the int4 base is frozen and