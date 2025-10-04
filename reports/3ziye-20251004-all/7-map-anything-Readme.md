<div align="center">
<h1>MapAnything: Universal Feed-Forward Metric <br>3D Reconstruction</h1>
<a href="https://map-anything.github.io/assets/MapAnything.pdf"><img src="https://img.shields.io/badge/Paper-blue" alt="Paper"></a>
<a href="https://arxiv.org/abs/2509.13414"><img src="https://img.shields.io/badge/arXiv-2509.13414-b31b1b" alt="arXiv"></a>
<a href="https://map-anything.github.io/"><img src="https://img.shields.io/badge/Project_Page-green" alt="Project Page"></a>
<a href="https://x.com/Nik__V__/status/1968316841618518371"><img src="https://img.shields.io/badge/X_Thread-1DA1F2" alt="X Thread"></a>
<a href="https://huggingface.co/spaces/facebook/map-anything"><img src='https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Demo-blue'></a>
<br>
<br>
<strong>
<a href="https://nik-v9.github.io/">Nikhil Keetha<sup>1,2</sup></a>
&nbsp;&nbsp;
<a href="https://sirwyver.github.io/">Norman Müller<sup>1</sup></a>
&nbsp;&nbsp;
<a href="https://demuc.de/">Johannes Schönberger<sup>1</sup></a>
&nbsp;&nbsp;
<a href="https://www.linkedin.com/in/lorenzoporzi">Lorenzo Porzi<sup>1</sup></a>
&nbsp;&nbsp;
<a href="https://infinity1096.github.io/">Yuchen Zhang<sup>2</sup></a>
<br>
<a href="https://tobiasfshr.github.io/">Tobias Fischer<sup>1</sup></a>
&nbsp;&nbsp;
<a href="https://www.linkedin.com/in/arno-knapitsch">Arno Knapitsch<sup>1</sup></a>
&nbsp;&nbsp;
<a href="https://www.linkedin.com/in/duncan-zauss">Duncan Zauss<sup>1</sup></a>
&nbsp;&nbsp;
<a href="https://ethanweber.me/">Ethan Weber<sup>1</sup></a>
&nbsp;&nbsp;
<a href="https://www.linkedin.com/in/nelsonantunes7">Nelson Antunes<sup>1</sup></a>
<br>
<a href="https://x.com/jonathonluiten?lang=en">Jonathon Luiten<sup>1</sup></a>
&nbsp;&nbsp;
<a href="https://m.lopezantequera.com/">Manuel Lopez-Antequera<sup>1</sup></a>
&nbsp;&nbsp;
<a href="https://scholar.google.com/citations?user=484sccEAAAAJ">Samuel Rota Bulò<sup>1</sup></a>
&nbsp;&nbsp;
<a href="https://richardt.name/">Christian Richardt<sup>1</sup></a>
<br>
<a href="https://www.cs.cmu.edu/~deva/">Deva Ramanan<sup>2</sup></a>
&nbsp;&nbsp;
<a href="https://theairlab.org/team/sebastian/">Sebastian Scherer<sup>2</sup></a>
&nbsp;&nbsp;
<a href="https://www.linkedin.com/in/peter-kontschieder-2a6410134">Peter Kontschieder<sup>1</sup></a>
<br>
<br>
<sup>1</sup> Meta &nbsp;&nbsp;
<sup>2</sup> Carnegie Mellon University
</strong>

</div>

## Overview

MapAnything is a simple, end-to-end trained transformer model that directly regresses the factored metric 3D geometry of a scene given various types of inputs (images, calibration, poses, or depth). A single feed-forward model supports over 12 different 3D reconstruction tasks including multi-image sfm, multi-view stereo, monocular metric depth estimation, registration, depth completion and more.

![Overview](./assets/teaser.png)

## Table of Contents

- [Quick Start](#quick-start)
  - [Installation](#installation)
  - [Image-Only Inference](#image-only-inference)
  - [Multi-Modal Inference](#multi-modal-inference)
- [Interactive Demos](#interactive-demos)
  - [Online Demo](#online-demo)
  - [Local Gradio Demo](#local-gradio-demo)
  - [Rerun Demo](#rerun-demo)
  - [Demo Inference on COLMAP outputs](#demo-inference-on-colmap-outputs)
- [COLMAP & GSplat Support](#colmap--gsplat-support)
  - [Exporting to COLMAP Format](#exporting-to-colmap-format)
  - [Integration with Gaussian Splatting](#integration-with-gaussian-splatting)
- [Data Processing for Training & Benchmarking](#data-processing-for-training--benchmarking)
- [Training](#training)
- [Benchmarking](#benchmarking)
- [Code License](#code-license)
- [Models](#models)
- [Building Blocks for MapAnything](#building-blocks-for-mapanything)
- [Acknowledgments](#acknowledgments)
- [Citation](#citation)

## Quick Start

### Installation

```bash
git clone https://github.com/facebookresearch/map-anything.git
cd map-anything

# Create and activate conda environment
conda create -n mapanything python=3.12 -y
conda activate mapanything

# Optional: Install torch, torchvision & torchaudio specific to your system
# Install MapAnything
pip install -e .

# For all optional dependencies
# See pyproject.toml for more details
pip install -e ".[all]"
pre-commit install
```

Note that we don't pin a specific version of PyTorch or CUDA in our requirements. Please feel free to install PyTorch based on your specific system.

### Image-Only Inference

For metric 3D reconstruction from images without additional geometric inputs:

```python
# Optional config for better memory efficiency
import os
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"

# Required imports
import torch
from mapanything.models import MapAnything
from mapanything.utils.image import load_images

# Get inference device
device = "cuda" if torch.cuda.is_available() else "cpu"

# Init model - This requries internet access or the huggingface hub cache to be pre-downloaded
# For Apache 2.0 license model, use "facebook/map-anything-apache"
model = MapAnythin