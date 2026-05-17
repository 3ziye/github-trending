# SenseNova-U1: Unifying Multimodal Understanding and Generation with NEO-unify Architecture

<p align="center">
  <strong>English</strong> | <a href="./README_CN.md">简体中文</a>
</p>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/arXiv-Coming-b31b1b.svg" alt="arXiv"></a>
  <a href="https://huggingface.co/collections/sensenova/sensenova-u1"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20HuggingFace-Model-yellow" alt="HuggingFace Model"></a>
  <a href="https://modelscope.cn/collections/SenseNova/SenseNova-U1"><img src="https://img.shields.io/badge/%F0%9F%A4%96%20ModelScope-模型-purple" alt="ModelScope-模型"></a>
  <a href="https://unify.light-ai.top/"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20SenseNova_U1-Demo-Green" alt="SenseNova-U1 Demo"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="License"></a>
  <a href="https://discord.com/invite/BuTXPHmQub"><img src="https://img.shields.io/badge/Discord-Join-5865F2?logo=discord&logoColor=white" alt="Discord"></a>
</p>

<p align="center">
  <img src="docs/assets/teaser.webp" alt="SenseNova-U1" width="900">
</p>

<p align="center">
  <img src="docs/assets/teaser_2.webp" alt="visualization" width="900">
</p>

## 📣 Updated News

- `[2026.05.15]` Release [SenseNova-U1-8B-MoT-Infographic 📊](https://huggingface.co/sensenova/SenseNova-U1-8B-MoT-Infographic) model for improved infographic generation. See [U1 Infographic Model](docs/u1_infographic_model.md) for details, and [✨ Infographic Showcases ](docs/u1_infographic_showcases.md) for 100 generated examples.

- `[2026.05.10]` Release [🔥SenseNova-U1 Technical Report🔥](https://github.com/OpenSenseNova/SenseNova-U1/blob/main/docs/pdf/SenseNOVA_U1.pdf) and the weights for [SenseNova-U1-A3B-MoT-SFT](https://huggingface.co/sensenova/SenseNova-U1-A3B-MoT-SFT) & [SenseNova-U1-A3B-MoT](https://huggingface.co/sensenova/SenseNova-U1-A3B-MoT).

- `[2026.05.08]` Add **GGUF quantized checkpoints** and **layer-offload VRAM modes** for low-VRAM single-GPU inference. See [Memory-efficient inference](#-memory-efficient-inference-gguf--vram-modes). GGUF weights for `SenseNova-U1-8B-MoT-Merger` are available at [🤗 smthem/SenseNova-U1-8B-MoT-Merger-gguf](https://huggingface.co/smthem/SenseNova-U1-8B-MoT-Merger-gguf) — many thanks to [@smthem](https://github.com/smthem) for contributing the quantized weights.

- `[2026.05.06]` Release [SenseNova-U1-8B-MoT-LoRA-8step-V1.0](https://huggingface.co/sensenova/SenseNova-U1-8B-MoT-LoRAs/blob/main/SenseNova-U1-8B-MoT-LoRA-8step-V1.0.safetensors). Please see the [example script](docs/base_vs_distill.md#run-base-and-distilled-model).

- `[2026.04.30]` Release the preview version of the 8-step inference model [SenseNova-U1-8B-MoT-8step-preview](https://huggingface.co/sensenova/SenseNova-U1-8B-MoT-8step-preview). In most cases, the image generation quality of this model closely matches that of the base model (see [comparison and existing issues](docs/base_vs_distill.md)). To test this model, you can use the [inference scripts](examples/README.md), but with the following parameters: ```--cfg_scale 1.0 --num_steps 8``` .

- `[2026.04.27]` Initial release of the weights for [SenseNova-U1-8B-MoT-SFT](https://huggingface.co/sensenova/SenseNova-U1-8B-MoT-SFT) and [SenseNova-U1-8B-MoT](https://huggingface.co/sensenova/SenseNova-U1-8B-MoT).

- `[2026.04.27]` Initial release of the [inference code](https://github.com/OpenSenseNova/SenseNova-U1/blob/main/examples/README.md) for SenseNova-U1.  

## 🌟 Overview

🚀 **SenseNova U1** is a new series of native multimodal models that unifies multimodal understanding, reasoning, and generation within a monolithic architecture. 
It marks a fundamental paradigm shift in multimodal AI: **from modality integration to true unification**. Rather than relying on adapters to translate between modalities, SenseNova U1 models think-and-act across language and vision natively.

Unifying visual understanding and generation in an end-to-end architecture from pixel to word opens tremendous possibilities, enabling highly efficient and strong understanding, generation, and interleaved reasoning in a natively multimodal manner.

<p align="center">
  <img src="docs/assets/teaser_1.webp" alt="radar plot" width="900">
</p>

#### 🏗️ *Key Pillars:*      

At the core of SenseNova U1 is **[NEO-unify](https://huggingface.co/blog/sensenova/neo-unify)**, a novel architecture designed from the first principles for multimodal AI:  *It eliminates both Visual Encoder (VE) and Variational Auto-Encoder (VAE) where pixel-word information are inherently and deeply correlated.* Several important features are as follows:

- 🔗 Model language and visual information end-to-end as a unified compound.   
- 🖼️ Preserve semantic richness while maintaining pixel-level visual fidelity.     
- 🧠 Reason across modalities with high efficiency & minimal conflict via native MoTs. 

#### ✨ *What This Unlocks:*

Powered by this new co