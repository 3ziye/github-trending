<p align="center" style="border-radius: 10px">
  <img src="assets/LongLive-logo.png" width="100%" alt="logo"/>
</p>

# 🎬 LongLive: Real-time Interactive Long Video Generation

[![Paper](https://img.shields.io/badge/ArXiv-Paper-brown)](https://arxiv.org/abs/2509.22622)
[![Code](https://img.shields.io/badge/GitHub-LongLive-blue)](https://github.com/NVlabs/LongLive)
[![Model](https://img.shields.io/badge/HuggingFace-Model-yellow)](https://huggingface.co/Efficient-Large-Model/LongLive-1.3B)
[![Video](https://img.shields.io/badge/YouTube-Video-red)](https://www.youtube.com/watch?v=CO1QC7BNvig)
[![Demo](https://img.shields.io/badge/Demo-Page-bron)](https://nvlabs.github.io/LongLive)

<div align="center">

[![Watch the video](assets/video-first-frame.png)](https://www.youtube.com/watch?v=CO1QC7BNvig)
[![Watch the video](assets/Comparison_with_Sora2.png)](https://x.com/yukangchen_/status/1973405662177529993)

</div>

## 💡 TLDR: Turn interactive prompts into long videos—instantly, as you type!

**LongLive: Real-time Interactive Long Video Generation [[Paper](https://arxiv.org/abs/2509.22622)]** <br />
[Shuai Yang](https://andysonys.github.io/), [Wei Huang](https://aaron-weihuang.com/), [Ruihang Chu](https://ruihang-chu.github.io/), [Yicheng Xiao](https://easonxiao-888.github.io/), [Yuyang Zhao](https://yuyangzhao.com/), [Xianbang Wang](https://peppaking8.github.io/), [Muyang Li](https://lmxyy.me/), [Enze Xie](https://xieenze.github.io/), [Yingcong Chen](https://www.yingcong.me/), [Yao Lu](https://scholar.google.com/citations?user=OI7zFmwAAAAJ&hl=en), [Song Han](http://songhan.mit.edu/), [Yukang Chen](https://yukangchen.com/) <br />

We present LongLive, a frame-level autoregressive (AR) framework for real-time and interactive long video generation. Long video generation presents challenges in both efficiency and quality. Diffusion and Diffusion-Forcing models can produce high-quality videos but suffer from low efficiency due to bidirectional attention. Causal attention AR models support KV caching for faster inference, but often degrade in quality on long videos due to memory challenges during long-video training. In addition, beyond static prompt-based generation, interactive capabilities, such as streaming prompt inputs, are critical for dynamic content creation, enabling users to guide narratives in real time. This interactive requirement significantly increases complexity, especially in ensuring visual consistency and semantic coherence during prompt transitions. To address these challenges, LongLive adopts a causal, frame-level AR design that integrates a KV-recache mechanism that refreshes cached states with new prompts for smooth, adherent switches; streaming long tuning to enable long video training and to align training and inference (train-long-test-long); and short window attention paired with a frame-level attention sink, shorten as frame sink, preserving long-range consistency while enabling faster generation. With these key designs, LongLive fine-tunes a 1.3B-parameter short-clip model to minute-long generation in just 32 GPU-days. At inference, LongLive sustains 20.7 FPS on a single NVIDIA H100, achieves strong performance on VBench in both short and long videos. LongLive supports up to 240-second videos on a single H100 GPU. LongLive further supports INT8-quantized inference with only marginal quality loss.

## TABLE OF CONTENTS
1. [News](#news)
2. [Highlights](#highlights)
3. [Introduction](#introduction)
4. [Installation](#installation)
5. [Inference](#inference)
6. [Training](#training)
7. [How to contribute](#how-to-contribute)
8. [Citation](#citation)
9. [License](#license)
10. [Acknowledgement](#acknowledgement)

## News
- [x] [2025.10.11] Many thanks to @yondonfu for building an interactive UI based on LongLive. Please check it here: https://github.com/daydreamlive/scope
- [x] [2025.10.1] We compare Sora2 (+ GPT-5 prompt engineering) with LongLive-1.3B in the interactive long video generation. See [here](https://x.com/yukangchen_/status/1973405662177529993) for details.
- [x] [2025.9.30] We release [example prompts](https://github.com/NVlabs/LongLive/tree/main/example) to reproduce our demo videos.
- [x] [2025.9.29] We release [Paper](https://arxiv.org/abs/2509.22622), this GitHub repo [LongLive](https://github.com/NVlabs/LongLive) with all training and inference code, the model weight [LongLive-1.3B](https://huggingface.co/Efficient-Large-Model/LongLive-1.3B), and demo page [Website](https://nvlabs.github.io/LongLive).

## Highlights
1. **Long Video Gen**: LongLive supports up to 240s video generation, with visual consistency.
2. **Real-time Inference**: LongLive supports 20.7 FPS generation speed on a single H100 GPU, and 24.8 FPS with FP8 quantization with marginal quality loss.
3. **Efficient Fine-tuning**: LongLive extends a short-clip model to minute-long generation in 32 H100 GPU-days.

## Introduction
<p align="center" style="border-radius: 10px">
  <img src="assets/pipeline.jpg" width