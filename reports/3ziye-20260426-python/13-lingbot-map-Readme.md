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

# 📰 News

- **2026-04-24** — Fixed a FlashInfer KV cache bug where `--keyframe_interval > 1` silently cached non-keyframes. **You should now see better pose and reconstruction quality when running with more than 320 frames**.
---

# ⚙️ Quick Start

## Installation

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
> (Optional) For faster first-use, you can additionally install a CUDA-specific JIT cache: `pip install flashinfer-jit-cache -f https://flashinfer.ai/whl/cu128/flashinfer-jit-cache/`.
> See [FlashInfer installation](https://docs.flashinfer.ai/installation.html) for details. If FlashInfer is not installed, the model falls back to SDPA (PyTorch native attention) via `--use_sdpa`.

**5. Visualization dependencies (optional)**

```bash
pip install -e ".[vis]"
```

# 📦 Model Download

| Model Name | Huggingface Repository | ModelScope Repository | Description |
| :--- | :--- | :--- | :--- |
| lingbot-map-long | [robbyant/lingbot-map](https://huggingface.co/robbyant/lingbot-map) | [Robbyant/lingbot-map](https://www.modelscope.cn/models/Robbyant/lingbot-map) | Better suited for long sequences and large scale scenes (Recommend). |
| lingbot-map | [robbyant/lingbot-map](https://huggingface.co/robbyant/lingbot-map) | [Robbyant/lingbot-map](https://www.modelscope.cn/models/Robbyant/lingbot-map) | Balanced checkpoint — trade off all-around performance across short and long sequences. |
| lingbot-map-stage1 | [robbyant/lingbot-map](https://huggingface.co/robbyant/lingbot-map) | [Robbyant/lingbot-map](https://www.modelscope.cn/models/Robbyant/lingbot-map) | Stage-1 training checkpoint of lingbot-map — can be loaded into the VGGT model for bidirectional inference (c2w). |

> 🚧 **Coming soon:** we're training an stronger model that supports longer sequences — stay tuned.

# 🎬 Demo

Run `demo.py` for interactive 3D visualization via a browser-based [viser](https://github.com/nerfstudio-project/viser) viewer (default `http://localhost:8080`).

### Try the Example Scenes

We provide four example scenes in `example/` that you can run out of the box:
`