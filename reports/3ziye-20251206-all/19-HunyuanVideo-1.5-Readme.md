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
* 🚀 Dec 05, 2025: **New Release**: We now release the [480p I2V step-distilled model](https://huggingface.co/tencent/HunyuanVideo-1.5/tree/main/transformer/480p_i2v_step_distilled), which generates videos in 8 or 12 steps (recommended)! On RTX 4090, end-to-end generation time is reduced by 75%, and a single RTX 4090 can generate videos within **75 seconds**. The step-distilled model maintains comparable quality to the original model while achieving significant speedup. See [Step Distillation Comparison](./assets/step_distillation_comparison.md) for detailed quality comparisons. For even faster generation, you can also try 4 steps (faster speed with slightly reduced quality). **To enable the step-distilled model, run `generate.py` with the `--enable_step_distill` parameter.** See [Usage](#-usage) for detailed usage instructions. 🔥🔥🔥🆕
* 📚 Dec 05, 2025: **Training Code Released**: We now open-source the training code for HunyuanVideo-1.5! The training script (`train.py`) provides a full training pipeline with support for distributed training, FSDP, context parallel, gradient checkpointing, and more. HunyuanVideo-1.5 is trained using the Muon optimizer, which we have open-sourced in the [Training](#-training) section. **If you would like to continue training our model or fine-tune it with LoRA, please use the Muon optimizer.** See [Training](#-training) section for detailed usage instructions. 🔥🔥🔥🆕
* 🎉 **Diffusers Support**: HunyuanVideo-1.5 is now available on Hugging Face Diffusers! Check out [Diffusers collection](https://huggingface.co/collections/hunyuanvideo-community/hunyuanvideo-15) for easy integration. 🔥🔥🔥🆕
* 🚀 Nov 27, 2025: We now support cache inference (deepcache, teacache, taylorcache), achieving significant speedup! Pull the latest code to try it. 🔥🔥🔥🆕 
* 🚀 Nov 24, 2025: We now support deepcache inference.
* 👋 Nov 20, 2025: We release the inference code and model weights of HunyuanVideo-1.5.


## 🎥 Demo
<div align="center">
  <video src="https://github.com/user-attachments/assets/d45ec78e-ea40-47f1-8d4d-f4d9a0682e2d" width="60%"> </video>
</div>

## 🧩 Community Contributions

If you develop/use HunyuanVideo-1.5 in your projects, welcome to let us know.

- **Diffusers** - [HunyuanVideo-1.5 Diffusers](https://huggingface.co/collections/hunyuanvideo-community/hunyuanvideo-15): Official Hugging Face Diffusers integration for HunyuanVideo-1.5. Easily use HunyuanVideo-1.5 with the Diffusers