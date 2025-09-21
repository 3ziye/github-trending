[中文阅读](README_zh.md)

# **HunyuanWorld-Voyager**

<p align="center">
  <img src="assets/teaser.png">
</p>

<div align="center">
  <a href="https://3d-models.hunyuan.tencent.com/world/" target="_blank"><img src="https://img.shields.io/static/v1?label=Project%20Page&message=Web&color=green" height=22px></a>
  <a href="https://3d-models.hunyuan.tencent.com/voyager/voyager_en/assets/HYWorld_Voyager.pdf" target="_blank"><img src="https://img.shields.io/static/v1?label=Tech%20Report&message=arxiv&color=red" height=22px></a>
  <a href="https://huggingface.co/tencent/HunyuanWorld-Voyager" target="_blank"><img src="https://img.shields.io/static/v1?label=HunyuanWorld-Voyager&message=HuggingFace&color=yellow" height=22px></a>
</div>

-----

We introduce HunyuanWorld-Voyager, a novel video diffusion framework that generates world-consistent 3D point-cloud sequences from a single image with user-defined camera path. Voyager can generate 3D-consistent scene videos for world exploration following custom camera trajectories. It can also generate aligned depth and RGB video for efficient and direct 3D reconstruction.


## 🔥🔥🔥 News!!
* Sep 2, 2025: 👋 We release the code and model weights of HunyuanWorld-Voyager. [Download](ckpts/README.md).

> Join our **[Wechat](#)** and **[Discord](https://discord.gg/dNBrdrGGMa)** group to discuss and find help from us.

| Wechat Group                                     | Xiaohongshu                                           | X                                           | Discord                                           |
|--------------------------------------------------|-------------------------------------------------------|---------------------------------------------|---------------------------------------------------|
| <img src="assets/qrcode/wechat.png"  height=140> | <img src="assets/qrcode/xiaohongshu.png"  height=140> | <img src="assets/qrcode/x.png"  height=140> | <img src="assets/qrcode/discord.png"  height=140> | 

## 🎥 Demo
### Demo Video

<div align="center">
  <video src="https://github.com/user-attachments/assets/2eb844c9-30ba-4770-8066-189c123affee" width="80%" poster=""> </video>
</div>

### Camera-Controllable Video Generation

|  Input | Generated Video  |
|:----------------:|:----------------:|
|  <img src="assets/demo/camera/input1.png" width="80%">        |       <video src="https://github.com/user-attachments/assets/2b03ecd5-9a8f-455c-bf04-c668d3a61b04" width="100%"> </video>        |
| <img src="assets/demo/camera/input2.png" width="80%">         |       <video src="https://github.com/user-attachments/assets/45844ac0-c65a-4e04-9f7d-4c72d47e0339" width="100%"> </video>        | 
| <img src="assets/demo/camera/input3.png" width="80%">         |       <video src="https://github.com/user-attachments/assets/f7f48473-3bb5-4a30-bd22-af3ca95ee8dc" width="100%"> </video>        |

### Multiple Applications

- Video Reconstruction

| Generated Video | Reconstructed Point Cloud |
|:---------------:|:--------------------------------:|
| <video src="https://github.com/user-attachments/assets/72a41804-63fc-4596-963d-1497e68f7790" width="100%"> </video> | <video src="https://github.com/user-attachments/assets/67574e9c-9e21-4ed6-9503-e65d187086a2" width="100%"> </video> |

- Image-to-3D Generation

| | |
|:---------------:|:---------------:|
| <video src="https://github.com/user-attachments/assets/886aa86d-990e-4b86-97a5-0b9110862d14" width="100%"> </video> | <video src="https://github.com/user-attachments/assets/4c1734ba-4e78-4979-b30e-3c8c97aa984b" width="100%"> </video> |

- Video Depth Estimation

| | |
|:---------------:|:---------------:|
| <video src="https://github.com/user-attachments/assets/e4c8b729-e880-4be3-826f-429a5c1f12cd" width="100%"> </video> | <video src="https://github.com/user-attachments/assets/7ede0745-cde7-42f1-9c28-e4dca90dac52" width="100%"> </video> |


## ☯️ **HunyuanWorld-Voyager Introduction**
###  Architecture

Voyager consists of two key components:

(1) World-Consistent Video Diffusion: A unified architecture that jointly generates aligned RGB and depth video sequences, conditioned on existing world observation to ensure global coherence.

(2) Long-Range World Exploration: An efficient world cache with point culling and an auto-regressive inference with smooth video sampling for iterative scene extension with context-aware consistency.

To train Voyager, we propose a scalable data engine, i.e., a video reconstruction pipeline that automates camera pose estimation and metric depth prediction for arbitrary videos, enabling large-scale, diverse training data curation without manual 3D annotations. Using this pipeline, we compile a dataset of over 100,000 video clips, combining real-world captures and synthetic Unreal Engine renders.

<p align="center">
  <img src="assets/backbone.jpg"  height=500>
</p>

### Performance

<table class="comparison-table">
  <thead>
    <tr>
      <th>Method</th>
      <th>WorldScore Average</th>
      <th>Camera Con