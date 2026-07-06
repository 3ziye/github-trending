# locate-anything.cpp

**Brought to you by the [LocalAI](https://github.com/mudler/LocalAI) team**, the folks behind LocalAI, the open-source AI engine that runs any model (LLMs, vision, voice, image, video) on any hardware, no GPU required.

[![Model on Hugging Face](https://huggingface.co/datasets/huggingface/badges/resolve/main/model-on-hf-md.svg)](https://huggingface.co/mudler/locate-anything.cpp-gguf)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![LocalAI](https://img.shields.io/badge/LocalAI-Run_Locally-orange)](https://github.com/mudler/LocalAI)

locate-anything.cpp is a C++17 inference port of NVIDIA's [`LocateAnything-3B`](https://huggingface.co/nvidia/LocateAnything-3B) - an open-vocabulary detection / visual-grounding VLM - built on [ggml](https://github.com/ggml-org/ggml). It gives you fast, dependency-light object detection from a text prompt on CPU (and on GPU through ggml's backends), with no Python runtime at inference time.

The model is Qwen2.5-3B (LM) + MoonViT (vision) + a 2-layer MLP projector; detection happens in *token space* - the model emits coordinate tokens `<0>`..`<1000>` that decode to boxes. The full pixel→labeled-boxes pipeline is ported and **validated against the official implementation**: the boxes come out identical, just faster (details and methodology in [`benchmarks/BENCHMARK.md`](benchmarks/BENCHMARK.md)).

Same detections as the official `LocateAnything-3B`, faster - here on an NVIDIA GB10 GPU,
against the official model run exactly as its model card documents (bf16), across three
scenes:

<p align="center">
  <img src="benchmarks/media/race_gpu.gif" width="88%" alt="GPU: locate-anything.cpp vs official PyTorch (bf16), ~2x faster across three scenes">
</p>

<sub>It also runs on CPU with no GPU at all (~1.7-3× over PyTorch-CPU; see <a href="benchmarks/BENCHMARK.md">benchmarks</a>).</sub>

## What it does

Give it an image and an open-vocabulary prompt; it returns labeled boxes.

<p align="center">
  <img src="benchmarks/media/detections_grid.png" width="90%" alt="annotated open-vocabulary detections on COCO scenes">
</p>

```sh
locate-anything-cli detect --model models/locate-anything-q8_0.gguf \
    --input street.jpg \
    --prompt "Locate all the instances that matches the following description: person</c>car." \
    --annotated out.png
# -> {"detections":[{"label":"person","box":[...]}, ...]}  + an annotated PNG
```

## Performance

Identical detections to the official `LocateAnything-3B`, faster on CPU with no Python.
On a Ryzen 9 9950X3D (CPU, 16 threads), inference-only on the 448 fixture:

| mode | PyTorch (official, f32) | locate-anything.cpp (f32) | speedup | detections |
| ---- | --- | --- | --- | --- |
| slow (pure AR) | 23.65 s | 14.26 s | **1.66×** | identical (IoU 1.000) |
| hybrid (default) | 69.06 s | 22.32 s | **3.09×** | identical (IoU 0.999) |
| fast (MTP-only) | 57.55 s | 19.45 s | **2.96×** | identical (IoU 1.000) |

<p align="center">
  <img src="benchmarks/plots/gpu_speedup.png" width="48%" alt="GB10 GPU speedup vs official bf16">
  <img src="benchmarks/plots/quant_tradeoff.png" width="48%" alt="quantization size/speed tradeoff">
</p>

Quantized (LM matmuls only; ViT/projector/norms stay f32) it gets smaller **and** faster with the same boxes - `q8_0` (6.3 GB) runs slow-mode in **4.89 s**, about **4.8× faster than the official f32 model**, byte-identical detections.

On **GPU** (build with `-DLA_GGML_CUDA=ON`; auto-selects the device, `LA_DEVICE=` for GPU / `LA_DEVICE=cpu` to force CPU) the weights move to VRAM. Run against the official model exactly as its model card documents (**bf16**), greedily, on one NVIDIA GB10: precision-matched (our **f16** vs its bf16) **ours is ~1.7-2.1× faster**, and the recommended **q8_0** build (box-identical) is **~1.9-3.1×**. Vs the official *sampled* out-of-box run it's mixed (faster on sparse scenes, comparable on dense - sampling stops earlier there). Full tables, the f16/q8/greedy/sampling breakdown, quantization, and parity methodology are in [`benchmarks/BENCHMARK.md`](benchmarks/BENCHMARK.md).

## Build

Clone with submodules (ggml is vendored at `third_party/ggml`):

```sh
git clone --recursive https://github.com/mudler/locate-anything.cpp
cd locate-anything.cpp
cmake -B build -DLA_BUILD_TESTS=ON -DLA_BUILD_CLI=ON && cmake --build build -j
```

### CMake options

| Option | Default | Purpose |
| ------ | ------- | ------- |
| `LA_BUILD_TESTS` | OFF | Compile and register the ctest targets |
| `LA_BUILD_CLI`   | ON  | Build `locate-anything-cli` |
| `LA_SHARED`      | OFF | Build `liblocate_anything` as a shared library (ggml static-linked in, no external libggml) |
| `LA_GGML_CUDA`   | OFF | Forward `GGML_CUDA` to the submodule |
| `LA_GGML_METAL`  | OFF | Forward `GGML_METAL` to the submodule |
| `LA_GGML_VULKAN` | OFF | Forward `GGML_VULKAN` to the submodule |

## Models

Prebuilt GGUFs are published on Hugging Face at
[`mudler/locate-anything.cpp-gguf`](https://huggingface.c