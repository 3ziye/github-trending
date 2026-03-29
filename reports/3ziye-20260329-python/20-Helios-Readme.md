<div align=center>
<img src="https://raw.githubusercontent.com/SHYuanBest/shyuanbest_media/main/Helios/logo_white.png" width="300px">
</div>

<h1 align="center">Helios: Real Real-Time Long Video Generation Model</h1>

<h5 align="center">⭐ 14B Real-Time Long Video Generation Model can be Cheaper, Faster but Keep Stronger than 1.3B ones ⭐</h5>

<h5 align="center">

[![arXiv](https://img.shields.io/badge/arXiv-2603.04379-b31b1b.svg?logo=arxiv)](https://arxiv.org/abs/2603.04379)
[![hf_paper](https://img.shields.io/badge/🤗-Paper%20In%20HF-red.svg)](https://huggingface.co/papers/2603.04379)
[![Project Page](https://img.shields.io/badge/Project-Website-2ea44f)](https://pku-yuangroup.github.io/Helios-Page)
[![hf_space](https://img.shields.io/badge/🤗-Gradio-00b4d8.svg)](https://huggingface.co/spaces/BestWishYsh/Helios-14B-RealTime)
[![HuggingFace](https://img.shields.io/badge/🤗-HuggingFace-blue)](https://huggingface.co/collections/BestWishYsh/helios)
[![ModelScope](https://img.shields.io/badge/🤖-ModelScope-purple)](https://modelscope.cn/collections/BestWishYSH/Helios)
[![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/PKU-YuanGroup/Helios)
[![GitCode](https://img.shields.io/badge/GitCodes-blue?logo=gitcode)](https://gitcode.com/weixin_47617277/Helios)

[![Ascend](https://img.shields.io/badge/Inference-Ascend--NPU-red)](https://www.hiascend.com/)
[![Diffusers](https://img.shields.io/badge/Inference-Diffusers-blueviolet)](https://github.com/huggingface/diffusers/pull/13208)
[![SGLang Diffusion](https://img.shields.io/badge/Backend-SGLang--Diffusion-yellow)](https://github.com/sgl-project/sglang/pull/19782)
[![vLLM-Omni](https://img.shields.io/badge/Backend-vLLM--Omni-orange)](https://github.com/vllm-project/vllm-omni/pull/1604)



</h5>

<div align="center">
This repository is the official implementation of Helios, which is a breakthrough video generation model that achieves minute-scale, high-quality video synthesis at <strong>19.5 FPS on a single H100 GPU</strong> (about 10 FPS on a single Ascend NPU) —without relying on conventional long video anti-drifting strategies or standard video acceleration techniques.
</div>

<br>

## ✨ Highlights


1. **Without commonly used anti-drifting strategies** (e.g., self-forcing, error-banks, keyframe sampling, or inverted sampling), Helios generates minute-scale videos with high quality and strong coherence.

2. **Without standard acceleration techniques** (e.g., KV-cache, causal masking, sparse/linear attention, TinyVAE, progressive noise schedules, hidden-state caching, or quantization), Helios achieves 19.5 FPS in end-to-end inference on a single H100 GPU.

3. **We introduce optimizations that improve both training and inference throughput while reducing memory consumption,** enabling image-diffusion-scale batch sizes during training while fitting up to four 14B models within 80 GB of GPU memory.



## 🎬 Video Demos

[![Demo Video of Helios](https://github.com/user-attachments/assets/1d10da4a-aba9-4ac1-ab02-cd0dfce8d35b)](https://www.youtube.com/watch?v=vd_AgHtOUFQ)
or you can click <a href="https://github.com/PKU-YuanGroup/Helios-Page/blob/main/videos/helios_features.mp4">here</a> to get the video. Some best prompts are [here](./example/prompt.txt).


## 📣 Latest News!!

* `[2026.03.26]` 🔥 Add summary of FAQ, Tips, and Tutorals: https://github.com/PKU-YuanGroup/Helios/issues/47.
* `[2026.03.24]` 👋 A community-made, unofficial YouTube tutorial for Helios is available [here](https://www.youtube.com/watch?v=AvFniggt6qg). It covers installation on a **consumer-grade PC** and supports **4K video generation**.
* `[2026.03.20]` 🚀 Helios now supports [Ahead-of-Time Compilation (AOTI)](https://huggingface.co/blog/zerogpu-aoti) on Spaces, with special thanks to the HuggingFace Team! Please refer to [this Space](https://huggingface.co/spaces/BestWishYsh/Helios-14B-RealTime-AOTI) for a usage example.
* `[2026.03.20]` 🔧 Based on [issue #38](https://github.com/PKU-YuanGroup/Helios/issues/38), we've identified several ways to further improve Helios's performance, such as fixing the i2v train-inference inconsistency and fully enabling Easy Anti-Drifting. Please refer to [commits](https://github.com/PKU-YuanGroup/Helios/commits/main/) and [correct.yaml](./scripts/training/configs/correct.yaml) for details.
* `[2026.03.12]` ⚡️ Please note that real-time generation performance depends not only on the GPU, but also on the CPU, memory, CUDA driver version, etc. As [tested by a user](https://github.com/PKU-YuanGroup/Helios/issues/3#issuecomment-4034710182) on better hardware with single H100, Helios can reach up to **20.89 FPS**!
* `[2026.03.08]` 🚀 Helios now fully supports [Group Offloading](#-group-offloading-to-save-vram) and [Context Parallelism](#-context-parallelism-on-multiple-gpus)! These features significantly optimize VRAM (**only ~6GB**) usage and enable inference across multiple GPUs with *Ulysses Attention*, *Ring Attention*, *Unified Attention*, an