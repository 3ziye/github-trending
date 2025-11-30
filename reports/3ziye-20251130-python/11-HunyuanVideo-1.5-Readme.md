[中文文档](./README_CN.md)

# HunyuanVideo-1.5

<div align="center">

<img src="./assets/logo.png" alt="HunyuanVideo-1.5 Logo" width="80%">

# 🎬 HunyuanVideo-1.5: A leading lightweight video generation model

</div>


<div align="center">
<!-- <img src="./assets/banner.png" alt="HunyuanVideo-1.5 Banner" width="800"> -->

</div>


HunyuanVideo-1.5 is a video generation model that delivers top-tier quality with only 8.3B parameters, significantly lowering the barrier to usage. It runs smoothly on consumer-grade GPUs, making it accessible for every developer and creator. This repository provides the implementation and tools needed to generate creative videos.


<div align="center">
  <a href="https://hunyuan.tencent.com/video/zh?tabIndex=0" target="_blank"><img src=https://img.shields.io/badge/Official%20Site-333399.svg?logo=homepage height=22px></a>
  <a href=https://huggingface.co/tencent/HunyuanVideo-1.5 target="_blank"><img src=https://img.shields.io/badge/%F0%9F%A4%97%20Models-d96902.svg height=22px></a>
  <a href=https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5 target="_blank"><img src= https://img.shields.io/badge/Page-bb8a2e.svg?logo=github height=22px></a>
  <a href="https://arxiv.org/pdf/2511.18870" target="_blank"><img src=https://img.shields.io/badge/Report-b5212f.svg?logo=arxiv height=22px></a>
  <a href=https://x.com/TencentHunyuan target="_blank"><img src=https://img.shields.io/badge/Hunyuan-black.svg?logo=x height=22px></a>
  <a href="https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/blob/main/assets/HunyuanVideo_1_5_Prompt_Handbook_EN.md" target="_blank"><img src=https://img.shields.io/badge/📚-PromptHandBook-blue.svg?logo=book height=22px></a> <br/>
  <a href="./ComfyUI/README.md" target="_blank"><img src=https://img.shields.io/badge/ComfyUI-blue.svg?logo=book height=22px></a>
  <a href="https://github.com/ModelTC/LightX2V" target="_blank"><img src=https://img.shields.io/badge/LightX2V-yellow.svg?logo=book height=22px></a>
  <a href="https://tusi.cn/models/933574988890423836" target="_blank"><img src=https://img.shields.io/badge/吐司-purple.svg?logo=book height=22px></a>
  <a href="https://tensor.art/models/933574988890423836" target="_blank"><img src=https://img.shields.io/badge/TensorArt-cyan.svg?logo=book height=22px></a>

</div>


<p align="center">
    👏 Join our <a href="./assets/wechat.png" target="_blank">WeChat</a> and <a href="https://discord.gg/ehjWMqF5wY">Discord</a> | 
💻 <a href="https://hunyuan.tencent.com/video/zh?tabIndex=0">Official website Try our model!</a>&nbsp&nbsp
</p>

## 🔥🔥🔥 News
* 📚 Training code is coming soon.
* 🚀 Nov 27, 2025: We now support cache inference (deepcache, teacache, taylorcache), achieving significant speedup! Pull the latest code to try it. 🔥🔥🔥🆕 
* 🚀 Nov 24, 2025: We now support deepcache inference.
* 👋 Nov 20, 2025: We release the inference code and model weights of HunyuanVideo-1.5.


## 🎥 Demo
<div align="center">
  <video src="https://github.com/user-attachments/assets/d45ec78e-ea40-47f1-8d4d-f4d9a0682e2d" width="60%"> </video>
</div>

## 🧩 Community Contributions

If you develop/use HunyuanVideo-1.5 in your projects, welcome to let us know.

- **ComfyUI** - [ComfyUI](https://github.com/comfyanonymous/ComfyUI): A powerful and modular diffusion model GUI with a graph/nodes interface. ComfyUI supports HunyuanVideo-1.5 with various engineering optimizations for fast inference. We provide a [ComfyUI Usage Guide](./ComfyUI/README.md) for HunyuanVideo-1.5.

- **Community-implemented ComfyUI Plugin** - [comfyui_hunyuanvideo_1.5_plugin](https://github.com/yuanyuan-spec/comfyui_hunyuanvideo_1.5_plugin): A community-implemented ComfyUI plugin for HunyuanVideo-1.5, offering both simplified and complete node sets for quick usage or deep workflow customization, with built-in automatic model download support.

- **LightX2V** - [LightX2V](https://github.com/ModelTC/LightX2V): A lightweight and efficient video generation framework that integrates HunyuanVideo-1.5, supporting multiple engineering acceleration techniques for fast inference.

- **Wan2GP v9.62** - [Wan2GP](https://github.com/deepbeepmeep/Wan2GP): WanGP is a very low VRAM app (as low 6 GB of VRAM for Hunyuan Video 1.5) supports Lora Accelerator for a 8 steps generation and offers tools to facilitate Video Generation.

- **ComfyUI-MagCache** - [ComfyUI-MagCache](https://github.com/Zehong-Ma/ComfyUI-MagCache): MagCache is a training-free caching approach that accelerates video generation by estimating fluctuating differences among model outputs across timesteps. It achieves 1.7x speedup for HunyuanVideo-1.5 with 20 inference steps.


## 📑 Open-source Plan
- HunyuanVideo-1.5 (T2V/I2V)
  - [x] Inference Code and checkpoints
  - [x] ComfyUI Support
  - [x] LightX2V Support
  - [ ] Diffusers Support
  - [ ] Release all model weights (Sparse attention, distill model, and SR models)

## 📋 Table of Contents
- [🔥🔥🔥 News](#-news)
- [🎥 Demo](#-demo)
- [🧩 Community Contributions](#-community-contributions)
- [📑 Open