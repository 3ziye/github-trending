<p align="center">
  <img src="img/readme-hero.gif" alt="JoyAI-VL-Interaction banner" width="100%">
</p>

<div align="center">

<h1>JoyAI-VL-Interaction</h1>

<p><strong>⚡ An Open Real-time Video-Language Interaction System</strong></p>

<p>An 8B-scale, fully open vision-language interaction model with a complete deployable system — the model, training recipe, time-aligned interaction data, and a real-time streaming stack, all in one repository.</p>

<p>
  <a href="https://arxiv.org/pdf/2606.14777"><b>📄 arXiv</b></a> |
  <a href="https://joyai-vl-video-future-academy-jd.github.io/JoyAI-VL-Interaction/"><b>🚀 Blog</b></a> |
  <a href="https://github.com/jd-opensource/JoyAI-VL-Interaction"><b>💻 Code</b></a> |
  <a href="https://huggingface.co/jdopensource/JoyAI-VL-Interaction-Preview"><b>🤗 Model</b></a> |
  <a href="https://huggingface.co/datasets/jdopensource/JoyAI-VL-Interaction"><b>📦 Dataset</b></a>
</p>

<p>
  <a href="#-quick-start"><b>🚀 Quick Start</b></a> |
  <a href="#-capability"><b>🧩 Capability</b></a> |
  <a href="#-evaluation"><b>📊 Evaluation</b></a> |
  <a href="#-citation"><b>📝 Citation</b></a>
</p>

<p>
  <img src="https://img.shields.io/badge/Model-8B-blue?style=flat-square" alt="8B Model">
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.12">
  <img src="https://img.shields.io/badge/vLLM-Inference-orange?style=flat-square" alt="vLLM">
  <img src="https://img.shields.io/badge/CUDA-12.x-76B900?style=flat-square&logo=nvidia&logoColor=white" alt="CUDA 12.x">
  <img src="https://img.shields.io/badge/License-Apache_2.0-green?style=flat-square" alt="Apache 2.0">
  <img src="https://img.shields.io/badge/Latency-<1s-d61f2c?style=flat-square" alt="Sub-second latency">
</p>

</div>

> 中文文档: [README.zh-CN.md](README.zh-CN.md)

## 🔥 News

- **[2026-06-20]** 🎉 Full open-source release — model weights, deployable system, and technical report are now available.
- **[2026-06-20]** 🚀 Day-0 deployment support via [vLLM-Omni](https://github.com/vllm-project/vllm-omni) ([recipe](https://github.com/vllm-project/vllm-omni/blob/main/recipes/JD/JoyAI-VL-Interaction.md)).
- **[2026-06-20]** 🎉 Release aligned interaction training data.

[https://github.com/user-attachments/assets/2853fc95-ad21-4972-8206-5f3d19798b14](https://github.com/user-attachments/assets/2853fc95-ad21-4972-8206-5f3d19798b14)

## ✨ Introduction

![JoyAI-VL-Interaction overview](img/overview.png)

The most important moments rarely wait for you to ask. A pot boils over while your hands are full. A toddler wanders toward the stove. The best moment of the game is gone before you can react. Today's AI can't help with moments like these — these models are turn-based by design: they sit quietly until you address them, then answer the question you asked.

We think the next step is a model that's **present like a person**: one that watches what's happening now, decides on its own when a moment is worth a word, speaks up when it matters and stays quiet when it doesn't, and hands off to a stronger model when a problem is hard.

**JoyAI-VL-Interaction** is an 8B-scale, vision-first interaction model released together with its training recipe, its data, and a complete deployable system — all fully open. Point a webcam or a livestream at it and it's immediately present in the scene, watching and responding in real time.

### 🌟 Key Features


|     | Feature                          | Description                                                                                    |
| --- | -------------------------------- | ---------------------------------------------------------------------------------------------- |
| ⚡   | **Real-time Presence**           | Watches continuously and responds in under a second when needed.                               |
| 👁️ | **Vision-triggered Proactivity** | Speaks from what it sees, while staying quiet when nothing matters.                            |
| 🤖  | **Agent Delegation**             | Hands hard subtasks to a background model, API, or agent while continuing to watch the stream. |
| 🔓  | **Fully Open Stack**             | Model, data, training recipe, and deployable system — all released for full reproducibility.   |


## 🚀 Quick Start

```bash
git clone https://github.com/jd-opensource/JoyAI-VL-Interaction.git
cd JoyAI-VL-Interaction

# Install dependencies
./install/install.sh --with-all

# Download all model weights
./install/download-models.sh --all

# Start the core services
./services/scripts/run.sh minimal
```

Then open `https://127.0.0.1:8099` in your browser.

👉 For the full setup (ASR, TTS, background agent) and configuration details, see the [Getting Started Guide](doc/getting_started.md).

🚑 If you run into deployment issues, see the [Troubleshooting Guide](doc/troubleshooting.md).

## 🛠️ System Architecture

![JoyAI-VL-Interaction system architecture](img/joyvl-system-architecture.png)

At the core of JoyAI-VL-Interaction is one deci