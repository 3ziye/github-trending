[中文阅读](README_zh_cn.md)


<p align="center">
  <img src="./assets/banner.png" alt="Banner" width="100%">
</p>

<div align="center">
  <a href="https://hunyuan.tencent.com/motion" target="_blank">
    <img src="https://img.shields.io/badge/Official%20Site-333399.svg?logo=homepage" height="22px" alt="Official Site">
  </a>
  <a href="https://github.com/Tencent-Hunyuan/HY-Motion-1.0" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-Repo-181717?logo=github&logoColor=white" height="22px" alt="Github Repo">
  </a>
  <a href="https://huggingface.co/spaces/tencent/HY-Motion-1.0" target="_blank">
    <img src="https://img.shields.io/badge/%F0%9F%A4%97%20Demo-276cb4.svg" height="22px" alt="HuggingFace Space">
  </a>
  <a href="https://huggingface.co/tencent/HY-Motion-1.0" target="_blank">
    <img src="https://img.shields.io/badge/%F0%9F%A4%97%20Models-d96902.svg" height="22px" alt="HuggingFace Models">
  </a>
  <a href="https://arxiv.org/pdf/2512.23464" target="_blank">
    <img src="https://img.shields.io/badge/Report-b5212f.svg?logo=arxiv" height="22px" alt="ArXiv Report">
  </a>
  <a href="https://x.com/TencentHunyuan" target="_blank">
    <img src="https://img.shields.io/badge/Hunyuan-black.svg?logo=x" height="22px" alt="X (Twitter)">
  </a>
</div>


# HY-Motion 1.0: Scaling Flow Matching Models for 3D Motion Generation


<p align="center">
  <img src="./assets/teaser.jpg" alt="Teaser" width="100%">
</p>


## 🔥 News
- **Dec 30, 2025**: 🤗 We released the inference code and pretrained models of [HY-Motion 1.0](https://huggingface.co/tencent/HY-Motion-1.0). Please give it a try via our [HuggingFace Space](https://huggingface.co/spaces/tencent/HY-Motion-1.0) and our [Official Site](https://hunyuan.tencent.com/motion)!


## **Introduction**

**HY-Motion 1.0** is a series of text-to-3D human motion generation models based on Diffusion Transformer (DiT) and Flow Matching. It allows developers to generate skeleton-based 3D character animations from simple text prompts, which can be directly integrated into various 3D animation pipelines. This model series is the first to scale DiT-based text-to-motion models to the billion-parameter level, achieving significant improvements in instruction-following capabilities and motion quality over existing open-source models.

### Key Features
- **State-of-the-Art Performance**: Achieves state-of-the-art performance in both instruction-following capability and generated motion quality.

- **Billion-Scale Models**: We are the first to successfully scale DiT-based models to the billion-parameter level for text-to-motion generation. This results in superior instruction understanding and following capabilities, outperforming comparable open-source models.

- **Advanced Three-Stage Training**: Our models are trained using a comprehensive three-stage process:

    - *Large-Scale Pre-training*: Trained on over 3,000 hours of diverse motion data to learn a broad motion prior.

    - *High-Quality Fine-tuning*: Fine-tuned on 400 hours of curated, high-quality 3D motion data to enhance motion detail and smoothness.

    - *Reinforcement Learning*: Utilizes Reinforcement Learning from human feedback and reward models to further refine instruction-following and motion naturalness.



<p align="center">
  <img src="./assets/pipeline.png" alt="System Overview" width="100%">
</p>

<p align="center">
  <img src="./assets/arch.png" alt="Architecture" width="100%">
</p>

<p align="center">
  <img src="./assets/sotacomp.jpg" alt="ComparisonSoTA" width="100%">
</p>




## 🎁 Model Zoo

**HY-Motion 1.0 Series**

| Model | Description | Date | Size | Huggingface | VRAM (min) |
|:-------|:-------------|:------:|:------:|:-------------:|:-------------:|
| **HY-Motion-1.0** | Standard Text2Motion Model | 2025-12-30 | 1.0B | [Download](https://huggingface.co/tencent/HY-Motion-1.0/tree/main/HY-Motion-1.0) | 26GB |
| **HY-Motion-1.0-Lite** | Lightweight Text2Motion Model | 2025-12-30 | 0.46B | [Download](https://huggingface.co/tencent/HY-Motion-1.0/tree/main/HY-Motion-1.0-Lite) | 24GB |

*Note*: To reduce GPU VRAM requirements, please use the following settings: `--num_seeds=1`, text prompt with less than 30 words, and motion length less than 5 seconds.  
*Note*: This table does not includes GPU VRAM requirements for LLM-based prompt engineering feature. If you have sufficient VRAM to run HY-Motion-1.0 model but gradio fails with a VRAM-related error, Run the Gradio application with prompt engineering disabled by setting the environment variable like this: `DISABLE_PROMPT_ENGINEERING=True python3 gradio_app.py`

## 🤗 Get Started with HY-Motion 1.0

HY-Motion 1.0 supports macOS, Windows, and Linux.


- [Code Usage (CLI)](#code-usage-cli)
- [Gradio App](#gradio-app)


#### 1. Installation

First, install PyTorch via the [official site](https://pytorch.org/). Then install the dependencies:

```bash
git clone https://github.com/Tencent-Hunyuan/HY-Motion-1.0.git
cd HY-Motion-1.0/
# Make sure git-lf