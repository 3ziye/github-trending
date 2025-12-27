![GELab-Zero Main Image](./images/main_en.png)

> 👋 Hi, everyone! We are proud to present the first fully open-source GUI Agent with both model and infrastructure. Our solution features plug-and-play engineering with no cloud dependencies, giving you complete privacy control.

<p align="center">
  <!-- <a href="https://github.com/stepfun-ai/gelab-zero"><img src="https://img.shields.io/badge/💻%20GitHub-Repository-black" alt="GitHub" /></a> -->
  <a href="https://arxiv.org/abs/2512.15431"><img src="https://img.shields.io/badge/arXiv-Step--GUI Technical Report-B31B1B.svg?logo=arxiv&logoColor=white" alt="arXiv" /></a>
  <a href="https://opengelab.github.io/"><img src="https://img.shields.io/badge/🌐%20Website-Project%20Page-blue" alt="Website" /></a>
  <a href="https://huggingface.co/stepfun-ai/GELab-Zero-4B-preview"><img src="https://img.shields.io/badge/🤗%20Hugging%20Face-GELab--Zero--4B--preview-orange" alt="Hugging Face Model" /></a>
  <a href="https://huggingface.co/datasets/stepfun-ai/AndroidDaily"><img src="https://img.shields.io/badge/📚%20Hugging%20Face-AndroidDaily-yellow" alt="Hugging Face Dataset" /></a>
  <a href="https://modelscope.cn/models/stepfun-ai/GELab-Zero-4B-preview"><img src="https://img.shields.io/badge/🤖%20Model%20Scope-GELab--Zero--4B--preview-blue" alt="Model Scope" /></a>
</p>

<p align="center">
  <a href="./README.md">English</a> |
  <a href="./README_CN.md">简体中文</a>
</p>

## 📰 News

* 🎁 **[2025-12-18]** We release **Step-GUI Technical Report** on [**arXiv**](https://arxiv.org/abs/2512.15431)!
* 🎁 **[2025-12-18]** We release a more powerful **API** for GUI automation tasks. [Apply for API access here](https://wvixbzgc0u7.feishu.cn/share/base/form/shrcnNStxEmuE7aY6jTW07CZHMf)!
* 🎁 **[2025-12-12]** We release **MCP-Server** support for multi-device management and task distribution. See [Installation & Quick Start](#-installation-quick-start) and [MCP-Server Setup](#optional-mcp-server-setup) for setup instructions.
* 🎁 **[2025-12-1]** We thank the following projects and authors for providing quantization tools & tutorials: [GGUF_v1](https://huggingface.co/bartowski/stepfun-ai_GELab-Zero-4B-preview-GGUF), [GGUF_v2](https://huggingface.co/noctrex/GELab-Zero-4B-preview-GGUF), [EXL3](https://huggingface.co/ArtusDev/stepfun-ai_GELab-Zero-4B-preview-EXL3), [Tutorials_CN](http://xhslink.com/o/1WrmgHGWFYh), [Tutorials_EN](https://www.youtube.com/watch?v=4BMiDyQOpos)
* 🎁 **[2025-11-31]** We release a lightweight **4B** model GELab-Zero-4B-preview on [**Hugging Face**](https://huggingface.co/stepfun-ai/GELab-Zero-4B-preview) and [**Model Scope**](https://modelscope.cn/models/stepfun-ai/GELab-Zero-4B-preview).
* 🎁 **[2025-11-31]** We release the tasks from the [**AndroidDaily**](https://huggingface.co/datasets/stepfun-ai/AndroidDaily) benchmark.
* 🎁 **[2025-11-30]** We release the current **GELab-Zero** engineering infrastructure.
* 🎁 **[2025-10]** Our [**research**](https://github.com/summoneryhl/gelab-engine) paper on GELab-Engine is accepted by **NeurIPS 2025**.



## 📑 Table of Contents

- [📖 Background](#-background)
- [🎥 Application Demonstrations](#-application-demonstrations)
- [🏆 Open Benchmark](#-open-benchmark)
- [🚀 Installation & Quick Start](#-installation-quick-start)
- [📝 Citation](#-citation)


## 📧 Contact

You can contact us and communicate with us by joining our WeChat group:

| WeChat Group |
|:-------------------------:|
| <img src="images/wechat_group2.jpeg" width="200"> |



## 📖 Background

As AI experiences increasingly penetrate consumer-grade devices, Mobile Agent research is at a critical juncture: transitioning from **"feasibility verification"** to **"large-scale application."** While GUI-based solutions offer universal compatibility, the fragmentation of mobile ecosystems imposes heavy engineering burdens that hinder innovation. GELab-Zero is designed to dismantle these barriers.

* ⚡️ **Out-of-the-Box Full-Stack Infrastructure** 
Resolves the fragmentation of the mobile ecosystem with a unified, one-click inference pipeline. It automatically handles multi-device ADB connections, dependencies, and permissions, allowing developers to focus on strategic innovation rather than engineering infrastructure.

* 🖥️ **Consumer-Grade Local Deployment** 
Features a built-in 4B GUI Agent model **fully optimized for Mac (M-series) and NVIDIA RTX 4060**. It supports complete local execution, ensuring data privacy and low latency on standard consumer hardware.

* 📱 **Flexible Task Distribution & Orchestration** 
Supports distributing tasks across multiple devices with interaction trajectory recording. It offers three versatile modes—ReAct loops, multi-agent collaboration, and scheduled tasks—to handle complex, real-world business scenarios.

* 🚀 **Accelerate from Prototype to Production** 
Empowers developers to rapidly validate interaction strategies while allowing enterprises to directly reuse the underlying infrastructure for zero-cost MCP integration, bridging the critical gap