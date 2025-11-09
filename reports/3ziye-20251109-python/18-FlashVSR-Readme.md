# ⚡ FlashVSR

**Towards Real-Time Diffusion-Based Streaming Video Super-Resolution**

**Authors:** Junhao Zhuang, Shi Guo, Xin Cai, Xiaohui Li, Yihao Liu, Chun Yuan, Tianfan Xue

<a href='http://zhuang2002.github.io/FlashVSR'><img src='https://img.shields.io/badge/Project-Page-Green'></a> &nbsp;
<a href="https://huggingface.co/JunhaoZhuang/FlashVSR"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Model%20(v1)-blue"></a> &nbsp;
<a href="https://huggingface.co/JunhaoZhuang/FlashVSR-v1.1"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Model%20(v1.1)-blue"></a> &nbsp;
<a href="https://huggingface.co/datasets/JunhaoZhuang/VSR-120K"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-orange"></a> &nbsp;
<a href="https://arxiv.org/abs/2510.12747"><img src="https://img.shields.io/badge/arXiv-2510.12747-b31b1b.svg"></a>

**Your star means a lot for us to develop this project!** :star:

<img src="./examples/WanVSR/assets/teaser.png" />

---

### 🌟 Abstract

Diffusion models have recently advanced video restoration, but applying them to real-world video super-resolution (VSR) remains challenging due to high latency, prohibitive computation, and poor generalization to ultra-high resolutions. Our goal in this work is to make diffusion-based VSR practical by achieving **efficiency, scalability, and real-time performance**. To this end, we propose **FlashVSR**, the first diffusion-based one-step streaming framework towards real-time VSR. **FlashVSR runs at ∼17 FPS for 768 × 1408 videos on a single A100 GPU** by combining three complementary innovations: (i) a train-friendly three-stage distillation pipeline that enables streaming super-resolution, (ii) locality-constrained sparse attention that cuts redundant computation while bridging the train–test resolution gap, and (iii) a tiny conditional decoder that accelerates reconstruction without sacrificing quality. To support large-scale training, we also construct **VSR-120K**, a new dataset with 120k videos and 180k images. Extensive experiments show that FlashVSR scales reliably to ultra-high resolutions and achieves **state-of-the-art performance with up to ∼12× speedup** over prior one-step diffusion VSR models.

---

### 📰 News

- **Nov 2025 — 🎉 [FlashVSR v1.1](https://huggingface.co/JunhaoZhuang/FlashVSR-v1.1) released:** enhanced stability + fidelity  
- **Oct 2025 — [FlashVSR v1](https://huggingface.co/JunhaoZhuang/FlashVSR)  (initial release)**: Inference code and model weights are available now! 🎉  
- **Bug Fix (October 21, 2025):** Fixed `local_attention_mask` update logic to prevent artifacts when switching between different aspect ratios during continuous inference.  
- **Coming Soon:** Dataset release (**VSR-120K**) for large-scale training.

---

### 📢 Important Quality Note (ComfyUI & other third-party implementations)

First of all, huge thanks to the community for the fast adoption, feedback, and contributions to FlashVSR! 🙌  
During community testing, we noticed that some third-party implementations of FlashVSR (e.g. early ComfyUI versions) do **not include our Locality-Constrained Sparse Attention (LCSA)** module and instead fall back to **dense attention**. This may lead to **noticeable quality degradation**, especially at higher resolutions.  
Community discussion: https://github.com/kijai/ComfyUI-WanVideoWrapper/issues/1441

Below is a comparison example provided by a community member:

| Fig.1 – LR Input Video | Fig.2 – 3rd-party (no LCSA) | Fig.3 – Official FlashVSR |
|------------------|-----------------------------------------------|--------------------------------------|
| <video src="https://github.com/user-attachments/assets/ea12a191-48d5-47c0-a8e5-e19ad13581a9" controls width="260"></video> | <video src="https://github.com/user-attachments/assets/c8e53bd5-7eca-420d-9cc6-2b9c06831047" controls width="260"></video> | <video src="https://github.com/user-attachments/assets/a4d80618-d13d-4346-8e37-38d2fabf9827" controls width="260"></video> |

✅ The **official FlashVSR pipeline (this repository)**:
- **Better preserves fine structures and details**
- **Effectively avoids texture aliasing and visual artifacts**

We are also working on a **version that does not rely on the Block-Sparse Attention library** while keeping **the same output quality**; this alternative may run slower than the optimized original implementation.

Thanks again to the community for actively testing and helping improve FlashVSR together! 🚀

---

### 📋 TODO

- ✅ Release inference code and model weights  
- ⬜ Release dataset (VSR-120K)

---

### 🚀 Getting Started

Follow these steps to set up and run **FlashVSR** on your local machine:

> ⚠️ **Note:** This project is primarily designed and optimized for **4× video super-resolution**.  
> We **strongly recommend** using the **4× SR setting** to achieve better results and stability. ✅

#### 1️⃣ Clone the Repository

```bash
git clone https://github.com/OpenImaging