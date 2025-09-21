<div align=“center” style=“font-family: charter;”>
<h1 align="center">Directly Aligning the Full Diffusion Trajectory with Fine-Grained Human Preference </h1>
<div align="center">
  <a href='https://arxiv.org/abs/2509.06942'><img src='https://img.shields.io/badge/ArXiv-red?logo=arxiv'></a>  &nbsp;
  <a href='https://huggingface.co/tencent/SRPO/'><img src='https://img.shields.io/badge/Model-blue?logo=huggingface'></a> &nbsp; 
  <a href='https://tencent.github.io/srpo-project-page/'><img src='https://img.shields.io/badge/%F0%9F%92%BB_Project-SRPO-blue'></a> &nbsp;
</div>
<div align="center">
  Xiangwei Shen<sup>1,2,3*</sup>,
  <a href="https://scholar.google.com/citations?user=Lnr1FQEAAAAJ&hl=zh-CN" target="_blank"><b>Zhimin Li</b></a><sup>1*</sup>,
  <a href="https://scholar.google.com.hk/citations?user=Fz3X5FwAAAAJ" target="_blank"><b>Zhantao Yang</b></a><sup>1</sup>, 
  <a href="https://shiyi-zh0408.github.io/" target="_blank"><b>Shiyi Zhang</b></a><sup>3</sup>,
  Yingfang Zhang<sup>1</sup>,
  Donghao Li<sup>1</sup>,
  <br>
  <a href="https://scholar.google.com/citations?user=VXQV5xwAAAAJ&hl=en" target="_blank"><b>Chunyu Wang</b></a><sup>1✝</sup>,
  <a href="https://openreview.net/profile?id=%7EQinglin_Lu2" target="_blank"><b>Qinglin Lu</b></a><sup>1</sup>,
  <a href="https://andytang15.github.io" target="_blank"><b>Yansong Tang</b></a><sup>3,✉️</sup>
</div>
<div align="center">
  <sup>1</sup>Hunyuan, Tencent 
  <br>
  <sup>2</sup>School of Science and Engineering, The Chinese University of Hong Kong, Shenzhen 
  <br>
  <sup>3</sup>Shenzhen International Graduate School, Tsinghua University 
  <br>
  <sup>*</sup>Equal contribution 
  <sup>✝</sup>Project lead 
  <sup>✉️</sup>Corresponding author
</div>

![head](assets/head.jpg)

## 🎉 Key Features
1. **Direct Align**: We introduce a new sampling strategy for diffusion fine-tuning that can effectively restore highly noisy images, leading to an optimization process that is more stable and less computationally demanding, especially during the initial timesteps.
2. **Faster Training**:   By rolling out only a single image and optimizing directly with analytical gradients—a key distinction from GRPO—our method achieves significant performance improvements for FLUX.1.dev in under 10 minutes of training. To further accelerate the process, our method supports replacing online rollouts entirely with a small dataset of real images; we find that fewer than 1500 images are sufficient to effectively train FLUX.1.dev.
3. **Free of Reward Hacking**: We have improved the training strategy for method that direct backpropagation on reward signal (such as ReFL and DRaFT). Moreover, we directly regularize the model using negative rewards, without the need for KL divergence or a separate reward system. In our experiments, this approach achieves comparable performance with multiple different rewards, improving the perceptual quality of FLUX.1.dev without suffering from reward hacking issues, such as overfitting to color or oversaturation preferences.
4. **Potential for Controllable Fine-tuning**: For the first time in online RL, we incorporate dynamically controllable text conditions, enabling on-the-fly adjustment of reward preference towards styles within the scope of the reward model.

## 🔥 News

- __[2025.9.12]__:  🎉 We released the complete training code. We also share tips and experiences to help you train your models. You’re welcome to discuss and ask questions in the issues! 💬✨
- __[2025.9.12]__:  🎉 We provide a standard workflow—feel free to use it in ComfyUI.
- __[2025.9.8]__:   🎉 We released the paper, checkpoint, inference code.

## 📑 Open-source Plan
- [X] The training code is under internal review and will be open-sourced by this weekend at the latest.
- [ ] Release a quantized version for the FLUX community.
- [ ] Extend support to other models.

## 🛠️ Dependencies and Installation

```bash
conda create -n SRPO python=3.10.16 -y
conda activate SRPO
bash ./env_setup.sh 
```
💡 The environment dependency is basically the same as DanceGRPO

## 🤗 Download Models

1. Model Cards

|       Model       |                           Huggingface Download URL                                      |  
|:-----------------:|:---------------------------------------------------------------------------------------:|
|       SRPO        |           [diffusion_pytorch_model](https://huggingface.co/tencent/SRPO/tree/main)      |

2. Download our `diffusion_pytorch_model.safetensors` in [https://huggingface.co/tencent/SRPO]
```bash
mkdir ./srpo
huggingface-cli login
huggingface-cli download --resume-download Tencent/SRPO diffusion_pytorch_model.safetensors --local-dir ./srpo/
```
3. Load your FLUX cache or use the `black-forest-labs/FLUX.1-dev`[https://huggingface.co/black-forest-labs/FLUX.1-dev]
```bash
mkdir ./data/flux
huggingface-cli login
huggingface-cli download --resume-download  black-forest-labs/FLUX.1-dev --local-dir ./data/flux
```

## 🔑 Inference

### Using ComfyUI

You can use