[中文文档](./README_zh_CN.md)

<div align="center">

<img src="./assets/logo.png" alt="HunyuanImage-3.0 Logo" width="600">

# 🎨 HunyuanImage-3.0: A Powerful Native Multimodal Model for Image Generation

</div>


<div align="center">
<img src="./assets/banner.png" alt="HunyuanImage-3.0 Banner" width="800">

</div>

<div align="center">
  <a href=https://hunyuan.tencent.com/image target="_blank"><img src=https://img.shields.io/badge/Official%20Site-333399.svg?logo=homepage height=22px></a>
  <a href=https://huggingface.co/tencent/HunyuanImage-3.0 target="_blank"><img src=https://img.shields.io/badge/%F0%9F%A4%97%20Models-d96902.svg height=22px></a>
  <a href=https://github.com/Tencent-Hunyuan/HunyuanImage-3.0 target="_blank"><img src= https://img.shields.io/badge/Page-bb8a2e.svg?logo=github height=22px></a>
  <a href=https://arxiv.org/pdf/2509.23951 target="_blank"><img src=https://img.shields.io/badge/Report-b5212f.svg?logo=arxiv height=22px></a>
  <a href=https://x.com/TencentHunyuan target="_blank"><img src=https://img.shields.io/badge/Hunyuan-black.svg?logo=x height=22px></a>
  <a href=https://docs.qq.com/doc/DUVVadmhCdG9qRXBU target="_blank"><img src=https://img.shields.io/badge/📚-PromptHandBook-blue.svg?logo=book height=22px></a>
</div>


<p align="center">
    👏 Join our <a href="./assets/WECHAT.md" target="_blank">WeChat</a> and <a href="https://discord.gg/ehjWMqF5wY">Discord</a> | 
💻 <a href="https://hunyuan.tencent.com/modelSquare/home/play?modelId=289&from=/visual">Official website(官网) Try our model!</a>&nbsp&nbsp
</p>

## 🔥🔥🔥 News
- **September 28, 2025**: 📖 **HunyuanImage-3.0 Technical Report Released** - Comprehensive technical documentation now available
- **September 28, 2025**: 🚀 **HunyuanImage-3.0 Open Source Release** - Inference code and model weights publicly available


## 🧩 Community Contributions

If you develop/use HunyuanImage-3.0 in your projects, welcome to let us know.

## 📑 Open-source Plan

- HunyuanImage-3.0 (Image Generation Model)
  - [x] Inference 
  - [x] HunyuanImage-3.0 Checkpoints
  - [ ] HunyuanImage-3.0-Instruct Checkpoints (with reasoning)
  - [ ] VLLM Support
  - [ ] Distilled Checkpoints
  - [ ] Image-to-Image Generation
  - [ ] Multi-turn Interaction


## 🗂️ Contents
- [🔥🔥🔥 News](#-news)
- [🧩 Community Contributions](#-community-contributions)
- [📑 Open-source Plan](#-open-source-plan)
- [📖 Introduction](#-introduction)
- [✨ Key Features](#-key-features)
- [🛠️ Dependencies and Installation](#-dependencies-and-installation)
  - [💻 System Requirements](#-system-requirements)
  - [📦 Environment Setup](#-environment-setup)
  - [📥 Install Dependencies](#-install-dependencies)
  - [Performance Optimizations](#performance-optimizations)
- [🚀 Usage](#-usage)
  - [🔥 Quick Start with Transformers](#-quick-start-with-transformers)
  - [🏠 Local Installation & Usage](#-local-installation--usage)
  - [🎨 Interactive Gradio Demo](#-interactive-gradio-demo)
- [🧱 Models Cards](#-models-cards)
- [📝 Prompt Guide](#-prompt-guide)
  - [Manually Writing Prompts](#manually-writing-prompts)
  - [System Prompt For Automatic Rewriting the Prompt](#system-prompt-for-automatic-rewriting-the-prompt)
  - [Advanced Tips](#advanced-tips)
  - [More Cases](#more-cases)
- [📊 Evaluation](#-evaluation)
- [📚 Citation](#-citation)
- [🙏 Acknowledgements](#-acknowledgements)
- [🌟🚀  Github Star History](#-github-star-history)

---

## 📖 Introduction

**HunyuanImage-3.0** is a groundbreaking native multimodal model that unifies multimodal understanding and generation within an autoregressive framework. Our text-to-image module achieves performance **comparable to or surpassing** leading closed-source models.


<div align="center">
  <img src="./assets/framework.png" alt="HunyuanImage-3.0 Framework" width="90%">
</div>

## ✨ Key Features

* 🧠 **Unified Multimodal Architecture:** Moving beyond the prevalent DiT-based architectures, HunyuanImage-3.0 employs a unified autoregressive framework. This design enables a more direct and integrated modeling of text and image modalities, leading to surprisingly effective and contextually rich image generation.

* 🏆 **The Largest Image Generation MoE Model:** This is the largest open-source image generation Mixture of Experts (MoE) model to date. It features 64 experts and a total of 80 billion parameters, with 13 billion activated per token, significantly enhancing its capacity and performance.

* 🎨 **Superior Image Generation Performance:** Through rigorous dataset curation and advanced reinforcement learning post-training, we've achieved an optimal balance between semantic accuracy and visual excellence. The model demonstrates exceptional prompt adherence while delivering photorealistic imagery with stunning aesthetic quality and fine-grained details.

* 💭 **Intelligent World-Knowledge Reasoning:** The unified multimodal architecture endows HunyuanImage-3.0 with powerful reasoning capabilities. It leverages its extensive world knowledge to intelligently interpret user int