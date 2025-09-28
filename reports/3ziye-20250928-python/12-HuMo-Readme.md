<div align="center">
<h1> HuMo: Human-Centric Video Generation via Collaborative Multi-Modal Conditioning </h1>

<a href="https://arxiv.org/abs/2509.08519"><img src="https://img.shields.io/badge/arXiv%20paper-2509.08519-b31b1b.svg"></a>
<a href="https://phantom-video.github.io/HuMo/"><img src="https://img.shields.io/badge/Project_page-More_visualizations-green"></a>
<a href="https://huggingface.co/bytedance-research/HuMo"><img src="https://img.shields.io/static/v1?label=%F0%9F%A4%97%20Hugging%20Face&message=Model&color=orange"></a>

[Liyang Chen](https://scholar.google.com/citations?user=jk6jWXgAAAAJ&hl)<sup> * </sup>, [Tianxiang Ma](https://tianxiangma.github.io/)<sup> * </sup>, [Jiawei Liu](https://scholar.google.com/citations?user=X21Fz-EAAAAJ), [Bingchuan Li](https://scholar.google.com/citations?user=ac5Se6QAAAAJ)<sup> &dagger; </sup>, <br>[Zhuowei Chen](https://scholar.google.com/citations?user=ow1jGJkAAAAJ), [Lijie Liu](https://liulj13.github.io/), [Xu He](https://scholar.google.com/citations?user=KMrFk2MAAAAJ&hl), [Gen Li](https://scholar.google.com/citations?user=wqA7EIoAAAAJ), [Qian He](https://scholar.google.com/citations?user=9rWWCgUAAAAJ), [Zhiyong Wu](https://scholar.google.com/citations?user=7Xl6KdkAAAAJ)<sup> § </sup><br>
<sup> * </sup>Equal contribution, <sup> &dagger; </sup>Project lead, <sup> § </sup>Corresponding author  
Tsinghua University | Intelligent Creation Team, ByteDance

</div>

<p align="center">
<img src="assets/teaser.png" width=95%>
<p>

## 🔥 Latest News

* A Best-Practice Guide for HuMo will be released soon. Stay tuned.
* Sep 17, 2025: 🔥🔥 [ComfyUI](https://github.com/comfyanonymous/ComfyUI/pull/9903) officially supports HuMo-1.7B!
* Sep 16, 2025: 🔥🔥 We release the [1.7B weights](https://huggingface.co/bytedance-research/HuMo/tree/main/HuMo-1.7B), which generate a 480P video in 8 minutes on a 32G GPU. The visual quality is lower than that of the 17B model, but the audio-visual sync remains nearly unaffected.
* Sep 13, 2025: 🔥🔥 The 17B model is merged into [ComfyUI-Wan](https://github.com/kijai/ComfyUI-WanVideoWrapper), which can be run on a NVIDIA 3090 GPU. Thank [kijai](https://github.com/kijai) for the update!
* Sep 10, 2025: 🔥🔥 We release the [17B weights](https://huggingface.co/bytedance-research/HuMo/tree/main/HuMo-17B) and inference codes.
* Sep 9, 2025: We release the [Project Page](https://phantom-video.github.io/HuMo/) and [Technique Report](https://arxiv.org/abs/2509.08519/) of **HuMo**.


## ✨ Key Features
HuMo is a unified, human-centric video generation framework designed to produce high-quality, fine-grained, and controllable human videos from multimodal inputs—including text, images, and audio. It supports strong text prompt following, consistent subject preservation, synchronized audio-driven motion.

> - **​​VideoGen from Text-Image**​​ - Customize character appearance, clothing, makeup, props, and scenes using text prompts combined with reference images.
> - **​​VideoGen from Text-Audio**​​ - Generate audio-synchronized videos solely from text and audio inputs, removing the need for image references and enabling greater creative freedom.
> - **​​VideoGen from Text-Image-Audio**​​ - Achieve the higher level of customization and control by combining text, image, and audio guidance.

## 📑 Todo List
- [x] Release Paper
- [x] Checkpoint of HuMo-17B
- [x] Checkpoint of HuMo-1.7B
- [x] Inference Codes
  - [ ] Text-Image Input
  - [x] Text-Audio Input
  - [x] Text-Image-Audio Input
- [x] Multi-GPU Inference
- [ ] Best-Practice Guide of HuMo for Movie-Level Generation
- [ ] Checkpoint for Longer Generation
- [ ] Prompts to Generate Demo of ***Faceless Thrones***
- [ ] Training Data

## ⚡️ Quickstart

### Installation
```
conda create -n humo python=3.11
conda activate humo
pip install torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 --index-url https://download.pytorch.org/whl/cu124
pip install flash_attn==2.6.3
pip install -r requirements.txt
conda install -c conda-forge ffmpeg
```

### Model Preparation
| Models       | Download Link                                                                                                                                           |    Notes                      |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| HuMo-17B      | 🤗 [Huggingface](https://huggingface.co/bytedance-research/HuMo/tree/main/HuMo-17B)   | Supports 480P & 720P 
| HuMo-1.7B | 🤗 [Huggingface](https://huggingface.co/bytedance-research/HuMo/tree/main/HuMo-1.7B) | Lightweight on 32G GPU
| HuMo-Longer | 🤗 [Huggingface](https://huggingface.co/bytedance-research/HuMo) | Longer generation to be released in Oct.
| Wan-2.1 | 🤗 [Huggingface](https://huggingface.co/Wan-AI/Wan2.1-T2V-1.3B) | VAE & Text encoder
| Whisper-large-v3 |      🤗 [Huggingface](https://huggingface.co/openai/whisper-large-v3)          | 