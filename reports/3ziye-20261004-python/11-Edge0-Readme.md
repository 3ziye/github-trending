<div align="center">

<img src="assets/20260908-223115.jpg" alt="edge0" width="100%">

# edge0

**An open-source streaming MoE inference framework — SSD expert offload + Recover-LoRA + prerouter routing prediction.**

**Python** · **macOS** · **iOS** · **Android** — one recipe, every device.

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Edge0--35B--A3B--preview-yellow?style=for-the-badge)](https://huggingface.co/Edge0/Edge0-35B-A3B-preview)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Edge0--8B--A1B--preview-yellow?style=for-the-badge)](https://huggingface.co/Edge0/Edge0-8B-A1B-preview)
[![ModelScope](https://img.shields.io/badge/ModelScope-Edge0--35B--A3B--preview-624AFF?style=for-the-badge)](https://www.modelscope.cn/models/Edge0/Edge0-35B-A3B-preview)
[![ModelScope](https://img.shields.io/badge/ModelScope-Edge0--8B--A1B--preview-624AFF?style=for-the-badge)](https://www.modelscope.cn/models/Edge0/Edge0-8B-A1B-preview)
[![arXiv](https://img.shields.io/badge/arXiv-2609.18063-B31B1B?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2609.18063)
[![GitHub](https://img.shields.io/badge/GitHub-Edge0--AI%2FEdge0-black?style=for-the-badge&logo=github)](https://github.com/Edge0-AI/Edge0)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue?style=for-the-badge)](LICENSE)

English | [中文](README_zh.md) | [日本語](README_ja.md) | [Español](README_es.md) | [Français](README_fr.md)

</div>

## News

- **[2026-09-30]** We released the **edge0 inference engines for four platforms — iOS, macOS, Android and Windows** — so users get the best inference experience across architectures and platforms. The source is open-sourced in this repo ([`ios/`](ios/) · [`macos/`](macos/) · [`android/`](android/) · [`windows/`](windows/)) — see each directory's README for details. The **unified inference framework** follows in **Q4 2026**; see the [Roadmap](#roadmap).
- **[2026-09-16]** Our technical report is on arXiv: [The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://arxiv.org/abs/2609.18063).
- **[2026-09-08]** Initial open-source release of **edge0**, together with both model tiers — [`Edge0-35B-A3B-preview`](https://huggingface.co/Edge0/Edge0-35B-A3B-preview) and [`Edge0-8B-A1B-preview`](https://huggingface.co/Edge0/Edge0-8B-A1B-preview) — on Hugging Face and ModelScope.

## About

**edge0** is an open-source streaming MoE inference framework. It
generalizes the production-proven recipe — **SSD expert offload +
Recover-LoRA + prerouter routing prediction** — into an extensible
framework that runs large sparse-MoE models on consumer hardware: peak
memory is bounded by the *active* expert set, not the parameter count.

### Core mechanisms

- **SSD expert offload**: expert weights are streamed from storage on
  demand; peak memory is bounded by the active set, not the parameter
  count.
- **Prerouter**: a trained head predicts expert routing one step
  ahead, so expert loads overlap the forward pass instead of stalling
  it — **up to +59%** decode throughput; the gain grows with storage
  latency, model size, and routed width *K*.
- **Recover-LoRA**: the int4 base is frozen and LoRA adapters are
  trained by distillation from the FP teacher, recovering most of the
  quantization loss at 4-bit (see [Quality](#quality)). Adapters stay
  unmerged: one read-only base serves multiple adapter sets.

### Platforms

One repo, one recipe, per-platform runtimes:

| Platform | Directory | Stack | Status |
|---|---|---|---|
| **Python** (macOS · Apple Silicon) | [`python/`](python/README.md) | Python + MLX | ✅ Available now |
| **macOS** app & CLI | [`macos/`](macos/README.md) | Rust | ✅ Open-sourced (2026-09-30) |
| **iOS** app | [`ios/`](ios/README.md) | Swift + MLX Swift | ✅ Open-sourced (2026-09-30) |
| **Android** app & engine | [`android/`](android/README.md) | Kotlin + native engine | ✅ Open-sourced (2026-09-30) |
| **Windows** app & engine | [`windows/`](windows/README.md) | C++ + Vulkan | ✅ Open-sourced (2026-09-30) |

### Models

Two model tiers ship with the framework. Each tier is an end-to-end
release: the released checkpoint, the trained LoRA adapters, and the
trained prerouter heads work together as one unit.

| Tier | Released checkpoint | Inference profile |
|---|---|---|
| `edge0-35b` | [`Edge0/Edge0-35B-A3B-preview`](https://huggingface.co/Edge0/Edge0-35B-A3B-preview) · [ModelScope](https://www.modelscope.cn/models/Edge0/Edge0-35B-A3B-preview) | 4-bit, 40 layers, 256 experts, prerouter K=4 |
| `edge0-8b` | [`Edge0/Edge0-8B-A1B-preview`](https://huggingface.co/Edge0/Edge0-8B-A1B-preview) · [ModelScope](https://www.modelscope.cn/models/Edge0/Edge0-8B-A1B-preview) | 4-bit, 24 layers, 128 experts, prerouter K=8 |

Both checkpoints are built on open sparse-MoE base models (Qwen3.6-35B-A3B
and the Ling 3.0 bailing hybrid respectively) and ship with the
LoRA and prerouter training done for this 