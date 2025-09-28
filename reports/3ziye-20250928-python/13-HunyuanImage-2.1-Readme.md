
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

## Introduction
We are excited to introduce **HunyuanImage-2.1**, a 17B text-to-image model that is capable of generating **2K (2048 × 2048) resolution** images. 

<!-- Leveraging an extensive dataset and structured captions involving multiple expert models, we significantly enhance text-image alignment capabilities. The model employs a highly expressive VAE with a (32 × 32) spatial compression ratio, substantially reducing computational costs. -->

Our architecture consists of two stages:
1. **​Base text-to-image Model**:​​ The first stage is a text-to-image model that utilizes two text encoders: a multimodal large language model (MLLM) to improve image-text alignment, and a multi-language, character-aware encoder to enhance text rendering across various languages. 
2. **Refiner Model**: The second stage introduces a refiner model that further enhances image quality and clarity, while minimizing artifacts. 
<!-- 
Additionally, we developed the PromptEnhancer module to further boost model performance, and employed meanflow distillation for efficient inference. HunyuanImage-2.1 demonstrates robust semantic alignment and cross-scenario generalization, leading to improved consistency between text and image, enhanced control of scene details, character poses, and expressions, and the ability to generate multiple objects with distinct descriptions. -->

👑 We achieved the **Top1** on Arena's leaderboard for text-to-image open-source models.

<div align="center">
  <img src="./assets/leaderboard.png" width=70% alt="HunyuanImage 2.1 Demo">
</div>
 

## 🎉 HunyuanImage-2.1 Key Features

- **High-Quality Generation**: Efficiently produces ultra-high-definition (2K) images with cinematic composition.
- **Multilingual Support**: Provides native support for both Chinese and English prompts.
- **Advanced Architecture**: Built on a multi-modal, single- and dual-stream combined DiT (Diffusion Transformer) backbone.
- **Glyph-Aware Processing**: Utilizes ByT5's text rendering capabilities for improved text generation accuracy.
- **Flexible Aspect Ratios**: Supports a variety of image aspect ratios (1:1, 16:9, 9:16, 4:3, 3:4, 3:2, 2:3).
- **Prompt Enhancement**: Automatically rewrites prompts to improve descriptive accuracy and visual quality.






## 📜 System Requirements

**Hardware and OS Requirements:**
- NVIDIA GPU with CUDA support.

  **Minimum requrement for now:** 24 GB GPU memory for 2048x2048 image generation.
  
  > **Note:** The memory requirements above are measured with model CPU offloading and FP8 quantization enabled. If your GPU has sufficient memory, you may disable offloading for improved inference speed.
- Supported operating system: Linux.


## 🛠️ Dependencies and Installation

1. Clone the repository:
```bash
git clone https://github.com/Tencent-Hunyuan/HunyuanImage-2.1.git
cd HunyuanImage-2.1
```

2. Install dependencies:
```bash
pip install -r requirements.txt
pip install flash-attn==2.7.3 --no-build-isolation
```

## 🧱 Download Pretrained Models

The details of download pretrained models are shown [here](ckpts/checkpoints-download.md).

## 🔑 Usage

### Prompt Enhancement

Prompt enhan