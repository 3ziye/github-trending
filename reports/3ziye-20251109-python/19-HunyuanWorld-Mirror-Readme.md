[中文阅读](README_zh.md)
# **HunyuanWorld-Mirror**

<p align="center">
  <img src="assets/teaser.jpg" width="95%" alt="HunyuanWorld-Mirror Teaser">
</p>

<p align="center">
<a href='https://3d-models.hunyuan.tencent.com/world/'><img src='https://img.shields.io/badge/Project-Page-green'></a>
<a href='https://3d-models.hunyuan.tencent.com/world/worldMirror1_0/HYWorld_Mirror_Tech_Report.pdf'><img src='https://img.shields.io/badge/Technique-Report-red'></a>
<a href='https://huggingface.co/tencent/HunyuanWorld-Mirror'><img src='https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Model-blue'></a>
<a href='https://huggingface.co/spaces/tencent/HunyuanWorld-Mirror'><img src='https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Demo-orange'></a>
<a href=https://discord.gg/dNBrdrGGMa target="_blank"><img src= https://img.shields.io/badge/Discord-white.svg?logo=discord height=22px></a>
  <a href=https://x.com/TencentHunyuan target="_blank"><img src=https://img.shields.io/badge/Hunyuan-black.svg?logo=x height=22px></a>
<p align="center">



HunyuanWorld-Mirror is a versatile feed-forward model for comprehensive 3D geometric prediction. It integrates diverse geometric priors (**camera poses**, **calibrated intrinsics**, **depth maps**) and simultaneously generates various 3D representations (**point clouds**, **multi-view depths**, **camera parameters**, **surface normals**, **3D Gaussians**) in a single forward pass.



https://github.com/user-attachments/assets/146a9a25-5eb7-4400-aa09-5b58e1d10a5e




## 🔥🔥🔥 Updates
* **[Nov 7, 2025]**: 🚀🚀🚀 We release the training and evaluation code. See [Training Instructions](#🤖-training) and [Evaluation Instructions](#📊-evaluation).
* **[Oct 22, 2025]**: We release the inference code and model weights. [Download Pretrained Model](https://huggingface.co/tencent/HunyuanWorld-Mirror).

> Join our **[Wechat](#)** and **[Discord](https://discord.gg/dNBrdrGGMa)** group to discuss and find help from us.

| Wechat Group                                     | Xiaohongshu                                           | X                                           | Discord                                           |
|--------------------------------------------------|-------------------------------------------------------|---------------------------------------------|---------------------------------------------------|
| <img src="assets/qrcode/wechat.png"  height=140> | <img src="assets/qrcode/xiaohongshu.png"  height=140> | <img src="assets/qrcode/x.png"  height=140> | <img src="assets/qrcode/discord.png"  height=140> | 


## Table of Contents

- [Introduction](#☯️-hunyuanworld-mirror-introduction)
  - [Architecture](#architecture)
- [Installation](#🛠️-dependencies-and-installation)
- [Quick Start](#🎮-quick-start)
  - [Online Demo](#online-demo)
  - [Local Demo](#local-demo)
- [Download Pretrained Models](#📦-download-pretrained-models)
- [Inference with Images & Priors](#🚀-inference-with-images--priors)
  - [Example Code Snippet](#example-code-snippet)
  - [Output Format](#output-format)
  - [Inference with More Functions](#inference-with-more-functions)
- [Post 3DGS Optimization (Optional)](#🎯-post-3dgs-optimization-optional)
  - [Install Dependencies](#install-dependencies)
  - [Optimization](#optimization)
- [Performance](#🔮-performance)
  - [Point Cloud Reconstruction](#point-cloud-reconstruction)
  - [Novel View Synthesis](#novel-view-synthesis)
  - [Boost of Geometric Priors](#boost-of-geometric-priors)
- [Training](#🤖-training)
  - [Training Data Preparation](#training-data-preparation)
  - [Install Dependencies](#install-dependencies)
  - [Training Commands](#training-commands)
  - [Fine-tuning Commands](#fine-tuning-commands)
- [Evaluation](#📊-evaluation)
  - [Evaluation Data Preparation](#evaluation-data-preparation)
  - [Install Dependencies](#install-dependencies)
  - [Evaluation Commands](#evaluation-commands)
    - [1. Point Map Reconstruction](#1-point-map-reconstruction)
    - [2. Surface Normal Estimation](#2-surface-normal-estimation)
    - [3. Novel View Synthesis](#3-novel-view-synthesis)
    - [4. Depth Estimation](#4-depth-estimation)
    - [5. Camera Pose Estimation](#5-camera-pose-estimation)
- [Open-Source Plan](#📑-open-source-plan)
- [BibTeX](#🔗-bibtex)
- [Contact](#📧-contact)
- [Acknowledgments](#acknowledgements)


## ☯️ **HunyuanWorld-Mirror Introduction**

### Architecture
HunyuanWorld-Mirror consists of two key components:

**(1) Multi-Modal Prior Prompting**: A mechanism that embeds diverse prior modalities,
including calibrated intrinsics, camera pose, and depth, into the feed-forward model. Given any subset of the available priors, we utilize several lightweight encoding layers to convert each modality into structured tokens.

**(2) Universal Geometric Prediction**: A unified architecture capable of handling
the full spectrum of 3D reconstruction tasks from camera and depth estimation to point map regression, surface normal estimation, and novel view s