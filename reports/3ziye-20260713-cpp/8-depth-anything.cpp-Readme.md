# depth-anything.cpp

**Brought to you by the [LocalAI](https://github.com/mudler/LocalAI) team**, the folks behind LocalAI, the open-source AI engine that runs any model (LLMs, vision, voice, image, video) on any hardware, no GPU required.

[![Model on Hugging Face](https://huggingface.co/datasets/huggingface/badges/resolve/main/model-on-hf-md.svg)](https://huggingface.co/mudler/depth-anything.cpp-gguf)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![LocalAI](https://img.shields.io/badge/LocalAI-Run_Locally-orange)](https://github.com/mudler/LocalAI)

A from-scratch C++17/[ggml](https://github.com/ggml-org/ggml) port of [Depth Anything 3](https://github.com/bytedance-seed/depth-anything-3) (ByteDance) for **dependency-free monocular metric depth + camera pose** inference. One self-contained GGUF file, no Python, no PyTorch, no CUDA toolkit at inference, just a small native library and CLI, and now **faster than PyTorch on CPU**, bit-exact against the original.

![depth-anything.cpp vs PyTorch on CPU: same depth, ggml finishes first](benchmarks/media/depth_race.gif)

> The same photo, depth computed side by side on CPU: identical output, depth-anything.cpp gets there first ([full clip](benchmarks/media/depth_race.mp4)).

Given an image it recovers a dense **metric depth** map, per-pixel **confidence**, the camera **extrinsics (3x4)** and **intrinsics (3x3)**, an optional **sky** mask, a back-projected **3D point cloud**, and exports to **glb / COLMAP / PLY**. Everything is verified numerically equal to the reference DA3 forward (correlation 1.0), component by component.

---

## Features

- **Monocular metric depth + camera pose** from a single image, plus multi-view depth+pose.
- **Full DA3 family.** small (ViT-S), base (ViT-B), large (ViT-L), giant (ViT-g), metric-large, mono-large, and the nested giant+large metric model - all driven by metadata baked into the GGUF.
- **The whole output surface:** depth, confidence, sky mask, extrinsics/intrinsics, ray-based pose, 3D Gaussians / point cloud, and `glb` / `COLMAP` / `PLY` export.
- **Self-contained GGUF.** Every dimension, hyperparameter and preprocessing constant lives inside the file. The loader reads them; nothing is hardcoded, no external config or vocab is shipped.
- **Quantization** to f16 / q8_0 / q6_k / q5_k / q4_k - q4_k is **99 MB** (0.25x the f32) and near-lossless.
- **CPU-first, GPU-ready.** Tuned CPU path (tinyBLAS, Winograd, flash-attention) plus CUDA / Metal / Vulkan ggml backends.
- **Flat C API** (`include/da_capi.h`) - embed from C, C++, Go, or Rust. Powers the [LocalAI](#use-it-from-localai) backend.
- **Parity-first.** Every component is gated against PyTorch-dumped reference tensors; the end-to-end depth matches the real `net()` at correlation 1.0.

---

## Supported models

Convert any of the official [Depth-Anything-3](https://huggingface.co/depth-anything) checkpoints to GGUF. All run through the same metadata-driven engine:

| Model | Backbone | Output | Notes |
|-------|----------|--------|-------|
| `DA3-SMALL` | ViT-S | depth + conf + pose | smallest / fastest |
| `DA3-BASE` | ViT-B | depth + conf + pose | the default anchor |
| `DA3-LARGE` | ViT-L | depth + conf + pose | higher quality |
| `DA3-GIANT` | ViT-g | depth + conf + pose + 3D Gaussians | reconstruction |
| `DA3MONO-LARGE` | ViT-L | depth + **sky** | monocular DPT head |
| `DA3METRIC-LARGE` | ViT-L | metric depth + sky | metric branch |
| `DA3NESTED-GIANT-LARGE` | ViT-g + ViT-L | aligned **metric** depth + pose | two-branch alignment |

### Depth Anything V2

The same engine also runs [Depth Anything **V2**](https://huggingface.co/depth-anything) checkpoints (single-image depth only — no confidence, pose or sky). Relative models emit inverse depth (ReLU); metric models emit depth in metres (Sigmoid × `max_depth`).

| Model | Backbone | Output | Notes |
|-------|----------|--------|-------|
| `Depth-Anything-V2-Small` | ViT-S | relative depth | smallest / fastest |
| `Depth-Anything-V2-Base` | ViT-B | relative depth | |
| `Depth-Anything-V2-Large` | ViT-L | relative depth | higher quality |
| `Depth-Anything-V2-Metric-Hypersim-{Small,Base,Large}` | ViT-S/B/L | metric depth (m), indoor | `max_depth=20` |
| `Depth-Anything-V2-Metric-VKITTI-{Small,Base,Large}` | ViT-S/B/L | metric depth (m), outdoor | `max_depth=80` |

> DA2 is depth only (no pose/confidence). The ViT-g (Giant) DA2 checkpoint is not shipped — its `Depth-Anything-V2-Giant` HF repo is gated/unreleased.

---

## Performance

depth-anything.cpp is now **faster than PyTorch on CPU**: **1.20x at f32** and **1.31x at q8_0** on the production @504 path, while also running the same model in **half the memory**, **loading ~6.7x faster**, shipping as a **99 MB** quantized file, and needing **no Python / PyTorch / CUDA** at inference, all while staying **bit-exact** (correlation 1.0 vs the reference).

CPU, AMD Ryzen 9 9950X3D (16-core / 32-thread x86), `threads=16`, 504x336, sustained (`repe