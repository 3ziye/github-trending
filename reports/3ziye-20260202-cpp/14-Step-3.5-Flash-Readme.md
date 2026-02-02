<!-- ---
license: apache-2.0
base_model:
  - stepfun-ai/step-3.5-flash
--- -->

# Step 3.5 Flash

<div align="center">
  
<div align="center" style="display: flex; justify-content: center; align-items: center;">
  <img src="assets/stepfun.svg" width="25" style="margin-right: 10px;"/>
  <h1 style="margin: 0; border-bottom: none;">Step 3.5 Flash</h1>
</div>

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20HF-StepFun/STEP3p5-preview)](https://huggingface.co/stepfun-ai/Step-3.5-Flash/tree/main)
[![ModelScope](https://img.shields.io/badge/ModelScope-StepFun/STEP3p5-preview)](https://huggingface.co/stepfun-ai/step3p5_preview/tree/main)
[![Paper](https://img.shields.io/badge/Paper-Arxiv-red)](https://huggingface.co/stepfun-ai/Step-3.5-Flash/tree/main)
[![Webpage](https://img.shields.io/badge/Webpage-Blog-blue)](https://static.stepfun.com/blog/step-3.5-flash/)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)]()

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
- [Known Issues and Future Directions](#8-known-issues-and-future-directions)
- [Co-Developing the Future](#9-co-developing-the-future)
- [License](#license)

## 2. Key Capabilities

- **Deep Reasoning at Speed**: While chatbots are built for reading, agents must reason fast. Powered by 3-way Multi-Token Prediction (MTP-3), Step 3.5 Flash achieves a generation throughput of **100–300 tok/s** in typical usage (peaking at **350 tok/s** for single-stream coding tasks). This allows for complex, multi-step reasoning chains with immediate responsiveness.

- **A Robust Engine for Coding & Agents**: Step 3.5 Flash is purpose-built for agentic tasks, integrating a scalable RL framework that drives consistent self-improvement. It achieves **74.4% on SWE-bench Verified** and **51.0% on Terminal-Bench 2.0**, proving its ability to handle sophisticated, long-horizon tasks with unwavering stability.

- **Efficient Long Context**: The model supports a cost-efficient **256K context window** by employing a 3:1 Sliding Window Attention (SWA) ratio—integrating three SWA layers for every full-attention layer. This hybrid approach ensures consistent performance across massive datasets or long codebases while significantly reducing the computational overhead typical of standard long-context models.

- **Accessible Local Deployment**: Optimized for accessibility, Step 3.5 Flash brings elite-level intelligence to local environments. It runs securely on high-end consumer hardware (e.g., Mac Studio M4 Max, NVIDIA DGX Spark), ensuring data privacy without sacrificing performance.

## 3. Performance

Step 3.5 Flash delivers performance parity with leading closed-source systems while remaining open and efficient.

![](assets/step-bar-chart.png)

Performance of Step 3.5 Flash measured across **Reasoning**, **Coding**, and **Agency**. Open-source models (left) are sorted by their total parameter count, while top-tier proprietary models are shown on the right. xbench-DeepSearch scores are sourced from [official publications](https://xbench.org/agi/aisearch) for consistency. The shadowed bars represent the enhanced performance of Step 3.5 Flash using [Parallel Thinking](https://arxiv.org/pdf/2601.05593).

### Detailed Benchmarks

| Benchmark | Step 3.5 Flash | DeepSeek V3.2 | Kimi K2 Thinking / K2.5 | GLM-4.7 | MiniMax M2.1 | MiMo-V2 Flash |
|---|---|---|---|---|---|---|
| # Activated Params | 11B | 37B | 32B | 32B | 10B | 15B |
| # Total Params (MoE) | 196B | 671B | 1T | 355B | 230B | 309B |
| Est. decoding cost (@ 128K context, Hopper GPU**) | **1.0x** (100 tok/s, MTP-3, EP8) | 6.0x (33 tok/s, MTP-1, EP32) | 18.9x (33 tok/s, no MTP, EP32) | 18.9x (100 tok/s, MTP-3, EP8) | 3.9x (100 tok/s, MTP-3, EP8) | 1.2x (100 tok/s, MTP-3, EP8) |
| **Agency** | | | | | | |
| τ²-Bench | **88.2** | 80.3 | 74.3* / — | 87.4 | 80.2* | 80.3 |
| BrowseComp | 51.6 | 51.4 | 41.5* / **60.6** | 52.0 | 47.4 | 45.4 |
| BrowseComp (w/ Context Manager) | 69.0 | 67.6 | 60.2 / **74.9** | 67.5 | 62.0 | 58.3 |
| BrowseComp-ZH | **66.9** | 65.0 | 62.3 / 62.3* | 66.6 | 47.8* | 51.2* |
| BrowseComp-ZH (w/ Context Manager) | **73.7** | — | — / — | — | — | — |
| GAIA (no file) | **84.5** | 75.1* | 75.6* / 75.9