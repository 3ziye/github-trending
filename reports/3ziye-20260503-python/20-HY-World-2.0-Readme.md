

<h1>HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds</h1>

[English](README.md) | [简体中文](README_zh.md)

<p align="center">
  <img src="assets/teaser.png" width="95%" alt="HY-World-2.0 Teaser">
</p>

<div align="center">
  <a href=https://3d.hunyuan.tencent.com/sceneTo3D target="_blank"><img src=https://img.shields.io/badge/Official%20Site-333399.svg?logo=homepage height=22px></a>
  <a href=https://huggingface.co/tencent/HY-World-2.0 target="_blank"><img src=https://img.shields.io/badge/%F0%9F%A4%97%20Models-d96902.svg height=22px></a>
  <a href=https://3d-models.hunyuan.tencent.com/world/ target="_blank"><img src= https://img.shields.io/badge/Page-bb8a2e.svg?logo=github height=22px></a>
  <a href=https://arxiv.org/abs/2604.14268 target="_blank"><img src=https://img.shields.io/badge/Report-b5212f.svg?logo=arxiv height=22px></a>
   <a href=https://modelscope.cn/models/Tencent-Hunyuan/HY-World-2.0 target="_blank"><img src=https://img.shields.io/badge/ModelScope-Models-624aff.svg height=22px></a>
  <a href=https://discord.gg/dNBrdrGGMa target="_blank"><img src= https://img.shields.io/badge/Discord-white.svg?logo=discord height=22px></a>
  <a href=https://x.com/TencentHunyuan target="_blank"><img src=https://img.shields.io/badge/Tencent%20HY-black.svg?logo=x height=22px></a>
 <a href="#community-resources" target="_blank"><img src=https://img.shields.io/badge/Community-lavender.svg?logo=homeassistantcommunitystore height=22px></a>
</div>

<br>
<p align="center">
  <i>"What Is Now Proved Was Once Only Imagined"</i>
</p>

## 🎥 Video
https://github.com/user-attachments/assets/b56f4750-25c9-48fb-83ff-d58526711463

## 🔥 News

- **[April 16, 2026]**: 🚀 Release HY-World 2.0 technical report & partial codes!
- **[April 16, 2026]**: 🤗 Open-source WorldMirror 2.0 inference code and model weights!
- **[Coming Soon]**: Release Full HY-World 2.0 (World Generation) inference code.
- **[Coming Soon]**: Release ![Panorama Generation](https://img.shields.io/badge/Panorama_Generation-4285F4?style=flat-square) (HY-Pano 2.0) model weights & code.
- **[Coming Soon]**: Release ![Trajectory Planning](https://img.shields.io/badge/Trajectory_Planning-EA4335?style=flat-square)（WorldNav） code.
- **[Coming Soon]**: Release ![World Expansion](https://img.shields.io/badge/World_Expansion-FBBC05?style=flat-square)(WorldStereo 2.0) model weights & inference code.


## 📋 Table of Contents
- [📖 Introduction](#-introduction)
- [✨ Highlights](#-highlights)
- [🧩 Architecture](#-architecture)
- [📝 Open-Source Plan](#-open-source-plan)
- [🎁 Model Zoo](#-model-zoo)
- [🤗 Get Started](#-get-started)
- [🔮 Performance](#-performance)
- [🎬 More Examples](#-more-examples)
- [📚 Citation](#-citation)


## 📖 Introduction

**HY-World 2.0** is a multi-modal world model framework for **world generation** and **world reconstruction**. It accepts diverse input modalities — text, single-view images, multi-view images, and videos — and produces 3D world representations (meshes / Gaussian Splattings). It offers two core capabilities:

- **World Generation** (text / single image &rarr; 3D world): syntheses high-fidelity, navigable 3D scenes through a four-stage method —— a) ![Panorama Generation](https://img.shields.io/badge/Panorama_Generation-4285F4?style=flat-square) with HY-Pano 2.0, b) ![Trajectory Planning](https://img.shields.io/badge/Trajectory_Planning-EA4335?style=flat-square) with WorldNav, c) ![World Expansion](https://img.shields.io/badge/World_Expansion-FBBC05?style=flat-square) with WorldStereo 2.0, and d) ![World Composition](https://img.shields.io/badge/World_Composition-34A853?style=flat-square) with WorldMirror 2.0 & 3DGS learning.
- **World Reconstruction** (multi-view images / video &rarr; 3D): Powered by WorldMirror 2.0, a unified feed-forward model that simultaneously predicts depth, surface normals, camera parameters, 3D point clouds, and 3DGS attributes in a single forward pass.

HY-World 2.0 is an **open-source state-of-the-art** world model.  We will release all model weights, code, and technical details to facilitate reproducibility and advance research in this field.

### Why 3D World Models?

Existing world models, such as Genie 3, Cosmos, and HY-World 1.5 (WorldPlay+WorldCompass), generate pixel-level videos — essentially "watching a movie" that vanishes once playback ends. **HY-World 2.0 takes a fundamentally different approach**: it directly produces editable, persistent 3D assets (meshes / 3DGS) that can be imported into game engines like Blender/Unity/Unreal Engine/Isaac Sim — more like "building a playable game" than recording a clip. This paradigm shift natively resolves many long-standing pain points of video world models:

|  | Video World Models | 3D World Model (HY-World 2.0) |
|--|---|---|
| **Output** | Pixel videos (non-editable) | Real 3D assets — meshes / 3DGS (fully editable) |
| **Playable Duration** | Limited (typically 1 min) | Unlimited — assets persist permanently |
| 