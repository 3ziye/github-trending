
[中文阅读](./README_CN.md)

<p align="center">
  <img src="./assets/logo.png"  height=100>
</p>

<div align="center">

# HunyuanImage-2.1: An Efficient Diffusion Model for High-Resolution (2K) Text-to-Image Generation​

</div>


<p align="center"> &nbsp&nbsp🤗 <a href="https://huggingface.co/tencent/HunyuanImage-2.1">HuggingFace</a>&nbsp&nbsp | 
💻 <a href="https://hunyuan.tencent.com/modelSquare/home/play?modelId=286&from=/visual">Official website(官网) Try our model!</a>&nbsp&nbsp
</p>


<!-- <div align="center">
  <a href=https://github.com/Tencent-Hunyuan/HunyuanImage-2.1 target="_blank"><img src=https://img.shields.io/badge/Code-black.svg?logo=github height=22px></a>
  <a href="https://huggingface.co/spaces/tencent/HunyuanImage-2.1" target="_blank">
    <img src="https://img.shields.io/badge/Demo%20Page-blue" height="22px"></a>
  <a href=https://huggingface.co/tencent/HunyuanImage-2.1 target="_blank"><img src=https://img.shields.io/badge/%F0%9F%A4%97%20Models-d96902.svg height=22px></a>
  <a href="#" target="_blank"><img src="https://img.shields.io/badge/Report-Coming%20Soon-blue" height="22px"></a><br/>
  <a href="https://www.arxiv.org/abs/2509.04545" target="https://arxiv.org/abs/2509.04545"><img src="https://img.shields.io/badge/PromptEnhancer-Report-yellow" height="22px"></a>
  <a href= https://hunyuan-promptenhancer.github.io/ target="_blank"><img src=https://img.shields.io/badge/PromptEnhancer-bb8a2e.svg?logo=github height=22px></a><br/>
  <a href=https://x.com/TencentHunyuan target="_blank"><img src=https://img.shields.io/badge/Hunyuan-black.svg?logo=x height=22px></a>
</div> -->

<p align="center">
    👏 Join our <a href="assets/WECHAT.md" target="_blank">WeChat</a> and <a href="https://discord.gg/ehjWMqF5wY">Discord</a>
</p>


-----

This repo contains PyTorch model definitions, pretrained weights and inference/sampling code for our HunyuanImage-2.1. You can <span style="color:red">**directly try our model**</span> on [Official website(官网)](https://hunyuan.tencent.com/modelSquare/home/play?modelId=286&from=/visual) and find more visualizations on our [project page](https://hunyuan.tencent.com/image/en?tabIndex=0).


<div align="center">
  <img src="./assets/demo.jpg" width=100% alt="HunyuanImage 2.1 Demo">
</div>

## 🔥🔥🔥 Latest Updates
- September 18, 2025: ✨ Try the [PromptEnhancer-32B model](https://huggingface.co/PromptEnhancer/PromptEnhancer-32B) for higher-quality prompt enhancement!​.
- September 18, 2025: ✨ [ComfyUI workflow of HunyuanImage-2.1](https://github.com/KimbingNg/ComfyUI-HunyuanImage2.1) is available now!
- September 16, 2025: 👑 We achieved the Top1 on Arena's leaderboard for text-to-image open-source models. [Leaderboard](https://artificialanalysis.ai/text-to-image/arena/leaderboard-text)
- September 12, 2025: 🚀 Released FP8 quantized models! Making it possible to generate 2K images with only 24GB GPU memory!
- September 8, 2025: 🚀 Released inference code and model weights for HunyuanImage-2.1.


<!-- ## 🎥 Demo

<div align="center">
  <img src="./assets/demo.jpg" width=100% alt="HunyuanImage 2.1 Demo">
</div> -->

<!-- ## Contents
- [HunyuanImage-2.1: An Efficient Diffusion Model for High-Resolution (2K) Text-to-Image Generation​](#hunyuanimage-21-an-efficient-diffusion-model-for-high-resolution-2k-text-to-image-generation)
  - [🔥🔥🔥 Latest Updates](#-latest-updates)
  - [🎥 Demo](#-demo)
  - [Contents](#contents)
  - [Abstract](#abstract)
  - [HunyuanImage-2.1 Overall Pipeline](#hunyuanimage-21-overall-pipeline)
    - [Training Data and Caption](#training-data-and-caption)
    - [Text-to-Image Model Architecture](#text-to-image-model-architecture)
    - [Reinforcement Learning from Human Feedback](#reinforcement-learning-from-human-feedback)
    - [Rewriting Model](#rewriting-model)
    - [Model distillation](#model-distillation)
  - [🎉 HunyuanImage-2.1 Key Features](#-hunyuanimage-21-key-features)
  - [Prompt Enhanced Demo](#prompt-enhanced-demo)
  - [📈 Comparisons](#-comparisons)
    - [SSAE Evaluation](#ssae-evaluation)
    - [GSB Evaluation](#gsb-evaluation)
  - [📜 System Requirements](#-system-requirements)
  - [🛠️ Dependencies and Installation](#️-dependencies-and-installation)
  - [🧱 Download Pretrained Models](#-download-pretrained-models)
  - [🔑 Usage](#-usage)
  - [🔗 BibTeX](#-bibtex)
  - [Acknowledgements](#acknowledgements)
  - [Github Star History](#github-star-history)

--- -->
<!-- - [🧩 Community Contributions](#-community-contributions) -->
## Introduction
We are excited to introduce **HunyuanImage-2.1**, a 17B text-to-image model that is capable of generating **2K (2048 × 2048) resolution** images. 

<!-- Leveraging an extensive dataset and structured captions involving multiple expert models, we significantly enhance text-image alignment capabilities. The model employs a highly expressive VAE with a (32 × 32) spatial compression ratio, substantially reducing computational costs. -->

Our architecture consists of two stages:
1. **​Base text-to-image Model**:​​ The f