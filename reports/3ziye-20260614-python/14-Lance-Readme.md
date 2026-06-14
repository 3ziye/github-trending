<div align="center">
  <img src="assets/logo/lance-logo.webp" alt="Lance logo" width="300">

  <h1 align="center"><sup>Lance: Unified Multimodal Modeling by Multi-Task Synergy</sup></h1>
  <p>
    <strong>
    <a href="https://scholar.google.com.hk/citations?user=FXxoQlsAAAAJ&hl=zh-CN&oi=ao" style="text-decoration: none; color: inherit;">Fengyi Fu</a><sup>*</sup>,
    <a href="https://corleone-huang.github.io/" style="text-decoration: none; color: inherit;">Mengqi Huang</a><sup>*,✉</sup>,
    <a href="https://scholar.google.com.hk/citations?user=9ER6nVkAAAAJ&hl=zh-CN&oi=ao" style="text-decoration: none; color: inherit;">Shaojin Wu</a><sup>*</sup>,
    Yunsheng Jiang<sup>*</sup>,
    Yufei Huo,
    <a href="https://guojianzhu.com/" style="text-decoration: none; color: inherit;">Jianzhu Guo</a><sup>✉,§</sup>
    </strong><br>
    Hao Li,
    Yinghang Song,
    Fei Ding,
    Qian He,
    Zheren Fu,
    Zhendong Mao,
    Yongdong Zhang
    <br>
    <em>ByteDance</em>
    <br>
    <sup>*</sup> Equal contribution &nbsp;&nbsp; <sup>✉</sup> Corresponding authors &nbsp;&nbsp; <sup>§</sup> Project lead
  </p>
  <p>
    <a href="https://lance-project.github.io/" style="text-decoration: none; margin: 0 8px;"><img src="https://img.shields.io/badge/Homepage-Lance-blue?style=flat" alt="Homepage"></a>
    <a href="http://arxiv.org/abs/2605.18678" style="text-decoration: none; margin: 0 8px;"><img src="https://img.shields.io/badge/Paper-arXiv-red?style=flat&logo=arxiv" alt="arXiv"></a>
    <a href="https://huggingface.co/bytedance-research/Lance" style="text-decoration: none; margin: 0 8px;"><img src="https://img.shields.io/badge/Model-HuggingFace-yellow?style=flat&logo=huggingface" alt="Model"></a>
    <a href="https://huggingface.co/spaces/bytedance-research/Lance" style="text-decoration: none; margin: 0 8px;"><img src="https://img.shields.io/badge/Demo-HuggingFace-40bfe6?style=flat&logo=huggingface" alt="Demo"></a>
    <br>
    English | <a href="./README_zh.md"><ins>简体中文</ins></a>
  </p>
</div>

> **Note:** Lance is a research project rather than a polished product model. The released checkpoint was trained with up to 128 A100 GPUs, with training conducted up to 768x768 image generation and 480p, 12 FPS video generation. Our goal is to share a research artifact for studying unified image/video understanding, generation, and editing under a relatively small model and limited compute budget. Output quality may vary across prompts, resolutions, duration, motion complexity, and editing scenarios, and we see further opportunities to improve the post-training recipe. We appreciate constructive feedback from the community as we continue improving the project.

## 🔥 Updates

- **`2026/06/03`**: 🚀 Lance is now supported in [vLLM-Omni](https://github.com/vllm-project/vllm-omni). See the [recipe](https://github.com/vllm-project/vllm-omni/blob/main/recipes/ByteDance/Lance.md)!
- **`2026/05/29`**: 💪 Added support for Image-to-Video generation. [More to see](assets/docs/changelog/2026-05-29.md)!
- **`2026/05/26`**: 🎨 The Gradio interface now supports image and video generation, editing, and understanding. [Try it out](assets/docs/changelog/2026-05-26.md)!
- **`2026/05/25`**: ✨ The [Hugging Face Space](https://huggingface.co/spaces/bytedance-research/Lance) is now live, thanks to the HF team!
- **`2026/05/19`**: 🤗 The technical report is now available on [arXiv](http://arxiv.org/abs/2605.18678).
- **`2026/05/18`**: 🔥 We launched the [project homepage](https://lance-project.github.io/) and released the initial inference code and model weights on [GitHub](https://github.com/bytedance/Lance/) and [Hugging Face](https://huggingface.co/bytedance-research/Lance).

## 🌟 Highlights

**Lance** is a 3B native unified multimodal model that supports **image and video understanding, generation, and editing** within a single framework.

- **Efficient at 3B scale.** With only **3B active parameters**, Lance achieves competitive performance across image generation, image editing, and video generation benchmarks.
- **Training from scratch.** Lance is trained from scratch with a staged multi-task recipe and within a budget of **up to 128 A100 GPUs**.

We are actively updating and improving this repository. If you find any bugs or have suggestions, please feel free to open an issue or submit a pull request (PR) 💖.

<div align="center">
  <img src="assets/benchmarks/benchmark-overview.png" alt="Lance benchmark overview across image generation, image editing, video generation, and video understanding" width="980">
</div>

## 📅 Roadmap

- [ ] Release the fine-tuning code.

## 🎨 Demo

<details>
<summary><strong>Show demo results</strong></summary>

<div align="center">
  <strong>🔥 We recommend visiting our <a href="https://lance-project.github.io/">homepage</a> for more visual results. 🔥</strong>
</div>

<h3 align="center">Text-to-Video</h3>

<table align="center">
  <tr>
    <td><a href="assets/text-to-video/videos/text-to-video-demo-01.mp4"><img src="asse