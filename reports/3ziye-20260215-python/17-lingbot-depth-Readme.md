# LingBot-Depth: Masked Depth Modeling for Spatial Perception


[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch 2.6+](https://img.shields.io/badge/pytorch-2.6+-green.svg)](https://pytorch.org/)

📄 **[Technical Report](https://github.com/Robbyant/lingbot-depth/blob/main/tech-report.pdf)** |
📄 **[arXiv](https://arxiv.org/abs/2601.17895)** |
🌐 **[Project Page](https://technology.robbyant.com/lingbot-depth)** |
💻 **[Code](https://github.com/robbyant/lingbot-depth)** |
🤗 **[Hugging Face](https://huggingface.co/collections/robbyant/lingbot-depth)** |
🤖 **[ModelScope](https://www.modelscope.cn/collections/Robbyant/LingBot-Depth)** ｜
🤖 **[Video](https://www.bilibili.com/video/BV1oa6uBXEyh)**


**LingBot-Depth** transforms incomplete and noisy depth sensor data into high-quality, metric-accurate 3D measurements. By jointly aligning RGB appearance and depth geometry in a unified latent space, our model serves as a powerful spatial perception foundation for robot learning and 3D vision applications.

<p align="center">
  <img src="assets/teaser/teaser-crop.png" width="100%">
</p>

Our approach refines raw sensor depth into clean, complete measurements, enabling:
- **Depth Completion & Refinement**: Fills missing regions with metric accuracy and improved quality
- **Scene Reconstruction**: High-fidelity indoor mapping with a strong depth prior
- **4D Point Tracking**: Accurate dynamic tracking in metric space for robot learning
- **Dexterous Manipulation**: Robust grasping with precise geometric understanding

## News

- **[2026.02.15]** Upload LingBot-Depth-v0.5 which fixes the bug in previous version.

## Artifacts Release

### Model Zoo

We provide pretrained models for different scenarios:

| Model | Hugging Face Model | ModelScope Model | Description |
|-------|-----------|-----------|-------------|
| LingBot-Depth-v0.5 | [robbyant/lingbot-depth-pretrain-vitl-14-v0.5](https://huggingface.co/robbyant/lingbot-depth-pretrain-vitl-14-v0.5/tree/main) | [robbyant/lingbot-depth-pretrain-vitl-14-v0.5](https://www.modelscope.cn/models/Robbyant/lingbot-depth-pretrain-vitl-14-v0.5)| ⭐ **Recommended!** General-purpose depth refinement and completion (fixes the bug in LingBot-Depth-v0.1)|
| LingBot-Depth-v0.1 | [robbyant/lingbot-depth-pretrain-vitl-14](https://huggingface.co/robbyant/lingbot-depth-pretrain-vitl-14/tree/main) | [robbyant/lingbot-depth-pretrain-vitl-14](https://www.modelscope.cn/models/Robbyant/lingbot-depth-pretrain-vitl-14)| General-purpose depth refinement |
| LingBot-Depth-DC | [robbyant/lingbot-depth-postrain-dc-vitl14](https://huggingface.co/robbyant/lingbot-depth-postrain-dc-vitl14/tree/main) | [robbyant/lingbot-depth-postrain-dc-vitl14](https://www.modelscope.cn/models/Robbyant/lingbot-depth-postrain-dc-vitl14)| Optimized for sparse depth completion |

### Data Release (Coming Soon)
- The curated 3M RGB-D dataset will be released upon completion of the necessary licensing and approval procedures. 
- Expected release: **mid-March 2026**.

## Installation

### Requirements

• Python ≥ 3.9 • PyTorch ≥ 2.0.0 • CUDA-capable GPU (recommended)

### From source

```bash
git clone https://github.com/robbyant/lingbot-depth
cd lingbot-depth

# Install the package (use 'python -m pip' to ensure correct environment)
conda create -n lingbot-depth python=3.9
conda activate lingbot-depth
python -m pip install -e .
```
## Quick Start

**Inference:**

```python
import torch
import cv2
import numpy as np
from mdm.model.v2 import MDMModel

# Load model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = MDMModel.from_pretrained('robbyant/lingbot-depth-pretrain-vitl-14-v0.5').to(device)

# Load and prepare inputs
image = cv2.cvtColor(cv2.imread('examples/0/rgb.png'), cv2.COLOR_BGR2RGB)
h, w = image.shape[:2]
image = torch.tensor(image / 255, dtype=torch.float32, device=device).permute(2, 0, 1)[None]

depth = cv2.imread('examples/0/raw_depth.png', cv2.IMREAD_UNCHANGED).astype(np.float32) / 1000.0
depth = torch.tensor(depth, dtype=torch.float32, device=device)[None]

intrinsics = np.loadtxt('examples/0/intrinsics.txt')
intrinsics[0] /= w  # Normalize fx and cx by width
intrinsics[1] /= h  # Normalize fy and cy by height
intrinsics = torch.tensor(intrinsics, dtype=torch.float32, device=device)[None]

# Run inference
output = model.infer(
    image,
    depth_in=depth,
    intrinsics=intrinsics)

depth_pred = output['depth']  # Refined depth map
points = output['points']      # 3D point cloud
```

**Run example:**

The model is automatically downloaded from Hugging Face on first run (no manual download needed):

```bash
# Basic usage - processes example 0
python example.py

# Use a different example (0-7 available)
python example.py --example 1

# Use depth completion optimized model
python example.py --model robbyant/lingbot-depth-postrain-dc-vitl14-v0.5

#