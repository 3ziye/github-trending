<div align="center">

<p align="center">
  <img src="./assets/logo.png" width="200px" alt="Live Avatar Teaser">
</p>

<h1>🎬 Live Avatar: Streaming Real-time Audio-Driven Avatar Generation with Infinite Length</h1>
<!-- <h3>The code will be open source in <strong><span style="color: #87CEEB;">early December</span></strong>.</h3> -->


<p>
<a href="https://github.com/Yubo-Shankui" style="color: inherit;">Yubo Huang</a><sup>1,2</sup> ·
<a href="#" style="color: inherit;">Hailong Guo</a><sup>2,3</sup> ·
<a href="#" style="color: inherit;">Fangtai Wu</a><sup>2,4</sup> ·
<a href="#" style="color: inherit;">Shifeng Zhang</a><sup>2</sup> ·
<a href="#" style="color: inherit;">Shijie Huang</a><sup>2</sup> ·
<a href="#" style="color: inherit;">Qijun Gan</a><sup>4</sup> ·
<a href="#" style="color: inherit;">Lin Liu</a><sup>1</sup> ·
<a href="#" style="color: inherit;">Sirui Zhao</a><sup>1,*</sup> ·
<a href="http://staff.ustc.edu.cn/~cheneh/" style="color: inherit;">Enhong Chen</a><sup>1,*</sup> ·
<a href="https://openreview.net/profile?id=%7EJiaming_Liu7" style="color: inherit;">Jiaming Liu</a><sup>2,‡</sup> ·
<a href="https://sites.google.com/view/stevenhoi/" style="color: inherit;">Steven Hoi</a><sup>2</sup>
</p>

<p style="font-size: 0.9em;">
<sup>1</sup> University of Science and Technology of China &nbsp;&nbsp;
<sup>2</sup> Alibaba Group &nbsp;&nbsp;
<sup>3</sup> Beijing University of Posts and Telecommunications &nbsp;&nbsp;
<sup>4</sup> Zhejiang University
</p>

<p style="font-size: 0.9em;">
<sup>*</sup> Corresponding authors. &nbsp;&nbsp; <sup>‡</sup> Project leader.
</p>

<!-- Badges -->
<a href="https://arxiv.org/abs/2512.04677"><img src="https://img.shields.io/badge/arXiv-2512.04677-b31b1b.svg?style=for-the-badge" alt="arXiv"></a> <a href="https://huggingface.co/papers/2512.04677"><img src="https://img.shields.io/badge/🤗%20Daily%20Paper-ff9d00?style=for-the-badge" alt="Daily Paper"></a> <a href="https://huggingface.co/Quark-Vision/Live-Avatar"><img src="https://img.shields.io/badge/Hugging%20Face-Model-ffbd45?style=for-the-badge&logo=huggingface&logoColor=white" alt="HuggingFace"></a> <a href="https://github.com/Alibaba-Quark/LiveAvatar"><img src="https://img.shields.io/badge/Github-Code-black?style=for-the-badge&logo=github" alt="Github"></a> <a href="https://liveavatar.github.io/"><img src="https://img.shields.io/badge/Project-Page-blue?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Project Page"></a>

</div>

> **TL;DR:** **Live Avatar** is an algorithm–system co-designed framework that enables real-time, streaming, infinite-length interactive avatar video generation. Powered by a **14B-parameter** diffusion model, it achieves **20 FPS** on **5×H800** GPUs with **4-step** sampling and supports **Block-wise Autoregressive** processing for **10,000+** second streaming videos.

<div align="center">

[![Watch the video](assets/demo.png)](https://www.youtube.com/watch?v=srbsGlLNpAc)

<strong>👀 More Demos:</strong> <br>
🤖 Human-AI Conversation &nbsp;|&nbsp; ♾️ Infinite Video &nbsp;|&nbsp; 🎭 Diverse Characters &nbsp;|&nbsp; 🎬 Animated Tech Explanation <br>
<a href="https://liveavatar.github.io/">
  <strong>👉 Click Here to Visit Project Page! 🌐</strong>
</a>
<br>

</div>

---
## ✨ Highlights

> - ⚡ **​​Real-time Streaming Interaction**​​ - Achieve **20** FPS real-time streaming with low latency
> - ♾️ ​​**​​Infinite-length Autoregressive Generation**​​​​ - Support **10,000+** second continuous video generation
> - 🎨 ​​**​​Generalization Performances**​​​​ - Strong generalization across cartoon characters, singing, and diverse scenarios 


---
## 📰 News
- **[2025.12.16]** 🎉 LiveAvatar has reached 1,000+ stars on GitHub! Thank you to the community for the incredible support! ⭐
- **[2025.12.12]** 🚀 We released single-gpu inference [Code](infinite_inference_single_gpu.sh) — no need for 5×H100 (house-priced server), a single 80GB VRAM GPU is enough to enjoy. 
- **[2025.12.08]** 🚀 We released real-time inference [Code](infinite_inference_multi_gpu.sh) and the model [Weight](https://huggingface.co/Quark-Vision/Live-Avatar).
- **[2025.12.08]** 🎉 LiveAvatar won the Hugging Face [#1 Paper of the day](https://huggingface.co/papers/date/2025-12-05)!
- **[2025.12.04]** 🏃‍♂️ We committed to open-sourcing the code in **early December**.
- **[2025.12.04]** 🔥 We released [Paper](https://arxiv.org/abs/2512.04677) and [demo page](https://liveavatar.github.io/) Website.

---

## 📑 Todo List

### 🌟 **Early December** (core code release)

- ✅ Release the paper
- ✅ Release the demo website
- ✅ Release checkpoints on Hugging Face
- ✅ Release Gradio Web UI
- ✅ Experimental real-time streaming inference on at least H800 GPUs
  - ✅ Distribution-matching distillation to 4 steps
  - ✅ Timestep-forcing pipeline parallelism

### ⚙️ **Later updates**

- ✅ Inference code supporting single GPU (offline generation)
- ⬜ Multi-character support
- ⬜ UI integration for easily streaming interaction
- ⬜ TTS integration
- ⬜ Training code 
- 