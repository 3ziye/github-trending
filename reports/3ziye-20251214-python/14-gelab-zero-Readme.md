![GELab-Zero Main Image](./images/main_en.png)

> 👋 Hi, everyone! We are proud to present the first fully open-source GUI Agent with both model and infrastructure. Our solution features plug-and-play engineering with no cloud dependencies, giving you complete privacy control.

<p align="center">
  <!-- <a href="https://github.com/stepfun-ai/gelab-zero"><img src="https://img.shields.io/badge/💻%20GitHub-Repository-black" alt="GitHub" /></a> -->
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

* 🎁 **[Coming Soon...]**

* 🎁 **[2025-12-12]** MCP-Server ready：

<!-- ### Step1 启动 mcp server 以支持多设备管理和任务分发 -->
### Step1 Start MCP server to support multi-device management and task distribution

```bash
# enable mcp server
python mcp_server/detailed_gelab_mcp_server.py
```

### Step2 Import MCP tools in Chatbox
<!-- images/MCP-chatbox.png -->
<div style="display: flex; align-items: center; justify-content: center; width: 80%; margin: 0 auto;">
  <img src="images/MCP-chatbox.png" alt="MCP-Demo" style="flex: 1; height: 400px; object-fit: contain; margin-right: 1px;"/>
</div>



* 🎁 **[2025-12]** We thank the following projects and authors for providing quantization tools & tutorials: [GGUF_v1](https://huggingface.co/bartowski/stepfun-ai_GELab-Zero-4B-preview-GGUF), [GGUF_v2](https://huggingface.co/noctrex/GELab-Zero-4B-preview-GGUF), [EXL3](https://huggingface.co/ArtusDev/stepfun-ai_GELab-Zero-4B-preview-EXL3), [Tutorials_CN](http://xhslink.com/o/1WrmgHGWFYh), [Tutorials_EN](https://www.youtube.com/watch?v=4BMiDyQOpos)
* 🎁 **[2025-11]** We release a lightweight **4B model** on [**Hugging Face**](https://huggingface.co/stepfun-ai/GELab-Zero-4B-preview) and [**Model Scope**](https://modelscope.cn/models/stepfun-ai/GELab-Zero-4B-preview).
* 🎁 **[2025-11]** We release the tasks from the [**AndroidDaily**](https://huggingface.co/datasets/stepfun-ai/AndroidDaily) benchmark.
* 🎁 **[2025-11]** We release the current **GELab-Zero** engineering infrastructure.
* 🎁 **[2025-10]** Our [research](https://github.com/summoneryhl/gelab-engine) paper on **GELab-Engine** is accepted by **NeurIPS 2025**.


## 📑 Table of Contents

- [📖 Background](#-background)
- [🎥 Application Demonstrations](#-application-demonstrations)
- [📊 AndroidDaily](#-androiddaily-a-self-built-benchmark-close-to-daily-life)
- [🏆 Open Benchmark](#-open-benchmark)
- [🚀 Installation & Quick Start](#-installation-quick-start)
- [📝 Citation](#-citation)
- [📧 Contact](#-contact)

## 📖 Background

As AI experiences continue to penetrate consumer-grade terminal devices, mobile Agent research is at a critical juncture transitioning from "feasibility verification" to "large-scale application." GUI-based solutions have emerged as the optimal approach for the current stage in addressing complex mobile ecosystems and achieving scalable Agent capabilities, thanks to their universal compatibility with all apps and zero-cost integration without requiring app vendor adaptation. However, due to the highly fragmented nature of mobile application ecosystems, getting GUI Agents to truly work across different brands and device models often faces numerous engineering challenges: multi-device ADB connections, dependency installation, permission configuration, inference service deployment, task recording and replay. This means Agent developers and MCP users need to handle substantial engineering infrastructure work, making it difficult to focus on strategic innovation.

To address this challenge, we are open-sourcing GELab-Zero to accelerate the innovation and application deployment of GUI Agents. It consists of two main components:

- Plug-and-play complete inference engineering infrastructure that handles all the heavy lifting
- A 4B GUI Agent model capable of running on local computer

It provides a one-click launch experience similar to open-source GUI Agent MCP, can be deployed entirely locally, and puts the entire inference pipeline under your complete control. Specific capabilities include:

- **Local Deployment**: Supports 4B-scale models running on consumer-grade hardware, balancing low latency with privacy.
- **One-click Launch**: Provides unified deployment pipeline that automatically handles environment dependencies and device manag