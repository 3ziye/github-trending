<div align="center">
  <img src="assets/teaser.png" width="100%">

<h1>LingBot-Map: Geometric Context Transformer for Streaming 3D Reconstruction</h1>

Robbyant Team

</div>

<div align="center">

[![Paper](https://img.shields.io/static/v1?label=Paper&message=arXiv&color=red&logo=arxiv)](https://arxiv.org/abs/2604.14141)
[![PDF](https://img.shields.io/static/v1?label=Paper&message=PDF&color=red&logo=adobeacrobatreader)](lingbot-map_paper.pdf)
[![Project](https://img.shields.io/badge/Project-Website-blue)](https://technology.robbyant.com/lingbot-map)
[![HuggingFace](https://img.shields.io/static/v1?label=%F0%9F%A4%97%20Model&message=HuggingFace&color=orange)](https://huggingface.co/robbyant/lingbot-map)
[![ModelScope](https://img.shields.io/static/v1?label=%F0%9F%A4%96%20Model&message=ModelScope&color=purple)](https://www.modelscope.cn/models/Robbyant/lingbot-map)
[![License](https://img.shields.io/badge/License-Apache--2.0-green)](LICENSE.txt)

</div>

https://github.com/user-attachments/assets/fe39e095-af2c-4ec9-b68d-a8ba97e505ab

-----

### 🗺️ Meet LingBot-Map! We've built a feed-forward 3D foundation model for streaming 3D reconstruction! 🏗️🌍

LingBot-Map has focused on:

- **Geometric Context Transformer**: Architecturally unifies coordinate grounding, dense geometric cues, and long-range drift correction within a single streaming framework through anchor context, pose-reference window, and trajectory memory.
- **High-Efficiency Streaming Inference**: A feed-forward architecture with paged KV cache attention, enabling stable inference at ~20 FPS on 518×378 resolution over long sequences exceeding 10,000 frames.
- **State-of-the-Art Reconstruction**: Superior performance on diverse benchmarks compared to both existing streaming and iterative optimization-based approaches.

---

## 📑 Table of Contents

<details>
<summary>Click to expand</summary>

- [📰 News](#-news)
- [📋 TODO](#-todo)
- [⚙️ Installation](#️-installation)
- [📦 Model Download](#-model-download)
- [🚀 Quick Start](#-quick-start)
- [🎬 Interactive Demo (`demo.py`)](#-interactive-demo-demopy)
  - [Try the Example Scenes](#try-the-example-scenes)
  - [Streaming with Keyframe Interval](#streaming-with-keyframe-interval)
  - [Windowed Inference (for long sequences, >3000 frames)](#windowed-inference-for-long-sequences-3000-frames)
  - [Sky Masking](#sky-masking)
  - [Visualization Options](#visualization-options)
  - [Performance & Memory](#performance--memory)
- [🎥 Offline Rendering Pipeline (`demo_render/batch_demo.py`)](#-offline-rendering-pipeline-demo_renderbatch_demopy)
- [📜 License](#-license)
- [📖 Citation](#-citation)
- [✨ Acknowledgments](#-acknowledgments)

</details>

---

## 📰 News

- **2026-04-29** — 📹 **Long-video demo released**. We released a very-long-video example (~25 000 frames, 13-minute indoor walkthrough) rendered with the offline pipeline — see [Worked Example](#worked-example--long-indoor-walkthrough-25-000-frames-13-minutes) for the command, flag rationale, and rendered output.
- **2026-04-27** — 🚀 **LingBot-Map accelerated**. Pull the latest `main` and run `python demo.py --compile ...` or `python gct_profile.py --backend flashinfer --dtype bf16 --compile` to verify on your hardware.
- **2026-04-24** — Fixed a FlashInfer KV cache bug where `--keyframe_interval > 1` silently cached non-keyframes. **You should now see better pose and reconstruction quality when running with more than 320 frames**.

---

## 📋 TODO

- ⬜ Release evaluation benchmark
- ✅ Release demo scripts
  - ✅ Indoor long-video demo ([Featured indoor walkthrough](#-featured-indoor-walkthrough-25-000-frames-13-minutes))
  - ⬜ Outdoor long-video demo
  - ⬜ LingBot-World demo
  - ⬜ Aerial long-video demo

---

## ⚙️ Installation

**1. Create conda environment**

```bash
conda create -n lingbot-map python=3.10 -y
conda activate lingbot-map
```

**2. Install PyTorch (CUDA 12.8)**

```bash
pip install torch==2.8.0 torchvision==0.23.0 --index-url https://download.pytorch.org/whl/cu128
```

> PyTorch 2.8.0 is the recommended version because NVIDIA Kaolin (required by the batch rendering pipeline) has prebuilt wheels for `torch-2.8.0_cu128`. If you only need `demo.py` you may use a newer PyTorch, but the batch renderer then requires building Kaolin from source.
> For other CUDA versions, see [PyTorch Get Started](https://pytorch.org/get-started/locally/).

**3. Install lingbot-map**

```bash
pip install -e .
```

**4. Install FlashInfer (recommended)**

FlashInfer provides paged KV cache attention for efficient streaming inference. It is a pure-Python package that JIT-compiles CUDA kernels on first use, so a single wheel works across CUDA/PyTorch versions:

```bash
pip install --index-url https://pypi.org/simple flashinfer-python
```

> `--index-url https://pypi.org/simple` is only needed if your default pip index is an internal mirror that doesn't have `flashinfer-python`.
> (Optional) For faster first-use, you can additionally install a CUDA-specific JIT cache: `