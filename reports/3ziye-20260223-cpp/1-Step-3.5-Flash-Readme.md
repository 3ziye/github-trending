<!-- ---
license: apache-2.0
base_model:
  - stepfun-ai/step-3.5-flash
--- -->

<div align="center"> 
  <h1 style="margin: 0; border-bottom: none;"> <img src="assets/stepfun.svg" width="25" style="margin-right: 10px;"/>  Step 3.5 Flash</h1>
</div>

<p align="center">
    <strong>English</strong>&nbsp; | &nbsp;<a href="README.zh-CN.md">简体中文</a>
</p>


<p align="center">
    <a href="./cookbooks/openclaw">OpenClaw Guide</a>&nbsp; | &nbsp;<a href="./cookbooks/claude-code-best-practices/README.en.md">Claude Code Guide</a>&nbsp; | &nbsp;<a href="./cookbooks/roo-code-integration-guide">Roo Code Guide</a>&nbsp; | &nbsp;<a href="./cookbooks/hybrid-local-agent-macos">Local Agent Guide</a>
</p>



[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20HF-StepFun/STEP3p5-preview)](https://huggingface.co/stepfun-ai/Step-3.5-Flash/tree/main)
[![ModelScope](https://img.shields.io/badge/ModelScope-StepFun/STEP3p5-preview)](https://modelscope.cn/models/stepfun-ai/Step-3.5-Flash)
[![Discord](https://img.shields.io/badge/Discord-Join-5865F2?logo=discord&logoColor=white)](https://discord.gg/RcMJhNVAQc)
[![Paper](https://img.shields.io/badge/Paper-Arxiv-red)](https://arxiv.org/pdf/2602.10604)
[![Webpage](https://img.shields.io/badge/Webpage-Blog-blue)](https://static.stepfun.com/blog/step-3.5-flash/)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)]()
[![Chat with the model on OpenRouter](https://img.shields.io/badge/Chat%20with%20the%20model-OpenRouter-5B3DF5?logo=chatbot&logoColor=white)](https://openrouter.ai/chat?models=stepfun/step-3.5-flash:free)
[![Chat with the model on HuggingfaceSpace](https://img.shields.io/badge/Chat%20with%20the%20model-HuggingfaceSpace-5B3DF5?logo=chatbot&logoColor=white)](https://huggingface.co/spaces/stepfun-ai/Step-3.5-Flash)
[![OpenClaw Integration](https://img.shields.io/badge/Agent-OpenClaw-purple?logo=robot&logoColor=white)](./cookbooks/openclaw)

</div>

## 1. Introduction 

**Step 3.5 Flash** ([visit website](https://static.stepfun.com/blog/step-3.5-flash/)) is our most capable open-source foundation model, engineered to deliver frontier reasoning and agentic capabilities with exceptional efficiency. Built on a sparse Mixture of Experts (MoE) architecture, it selectively activates only 11B of its 196B parameters per token. This "intelligence density" allows it to rival the reasoning depth of top-tier proprietary models, while maintaining the agility required for real-time interaction.

### Contents
- [Key Capabilities](#2-key-capabilities)
- [Performance](#3-performance)
- [Architecture Details](#4-architecture-details)
- [Quick Start](#5-quick-start)
- [Local Deployment](#6-local-deployment)
- [Using Step 3.5 Flash on Agent Platforms](#7-using-step-35-flash-on-agent-platforms)
- [Cookbooks](#8-cookbooks)
- [Known Issues and Future Directions](#9-known-issues-and-future-directions)
- [Co-Developing the Future](#10-co-developing-the-future)
- [License](#license)

## 2. Key Capabilities

- **Deep Reasoning at Speed**: While chatbots are built for reading, agents must reason fast. Powered by 3-way Multi-Token Prediction (MTP-3), Step 3.5 Flash achieves a generation throughput of **100–300 tok/s** in typical usage (peaking at **350 tok/s** for single-stream coding tasks). This allows for complex, multi-step reasoning chains with immediate responsiveness.

- **A Robust Engine for Coding & Agents**: Step 3.5 Flash is purpose-built for agentic tasks, integrating a scalable RL framework that drives consistent self-improvement. It achieves **74.4% on SWE-bench Verified** and **51.0% on Terminal-Bench 2.0**, proving its ability to handle sophisticated, long-horizon tasks with unwavering stability.

- **Efficient Long Context**: The model supports a cost-efficient **256K context window** by employing a 3:1 Sliding Window Attention (SWA) ratio—integrating three SWA layers for every full-attention layer. This hybrid approach ensures consistent performance across massive datasets or long codebases while significantly reducing the computational overhead typical of standard long-context models.

- **Accessible Local Deployment**: Optimized for accessibility, Step 3.5 Flash brings elite-level intelligence to local environments. It runs securely on high-end consumer hardware (e.g., Mac Studio M4 Max, NVIDIA DGX Spark), ensuring data privacy without sacrificing performance.

## 3. Performance

Step 3.5 Flash delivers performance parity with leading closed-source systems while remaining open and efficient.

![](assets/step-bar-chart.png)

Performance of Step 3.5 Flash measured across **Reasoning**, **Coding**, and **Agentic Capabilities**. Open-source models (left) are sorted by their total parameter count, while top-tier proprietary models are shown on the right. xbench-DeepSearch scores are sourced from [official publications](https://xbench.org/agi/aisearch) for consistency. The shadowed bars represent the enhanced performance of Step 3.5 Flash using [Parallel Thinking](https://