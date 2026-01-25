# SimpleMem: Efficient Lifelong Memory for LLM Agents

<div align="center">

<p align="center">
  <img src="fig/Fig_icon.png" width="70%">
</p>


[![Project Page](https://img.shields.io/badge/🎬_INTERACTIVE_DEMO-Visit_Our_Website-FF6B6B?style=for-the-badge&labelColor=FF6B6B&color=4ECDC4&logoColor=white)](https://aiming-lab.github.io/SimpleMem-Page)

[![Paper](https://img.shields.io/badge/📄_Paper-arXiv-b31b1b?style=flat-square)](https://arxiv.org/abs/2601.02553)
[![GitHub](https://img.shields.io/badge/GitHub-SimpleMem-181717?logo=github&style=flat-square)](https://github.com/aiming-lab/SimpleMem)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

</div>

---

## 🔥 News
- **[01/20/2026]** **SimpleMem is now available on PyPI!** 📦 You can now install SimpleMem directly via `pip install simplemem` for easier setup and integration. [View Package Usage Guide →](docs/PACKAGE_USAGE.md)
- **[01/19/2026]** **Added Local Memory Storage for SimpleMem Skill!** 💾 SimpleMem Skill now supports local memory storage, enabling seamless memory retention and management directly within Claude Skills.
- **[01/18/2026]** **SimpleMem now supports Claude Skills!** 🚀 Use SimpleMem in claude.ai to remember long-term information and project history across conversations. Register at [mcp.simplemem.cloud](https://mcp.simplemem.cloud), add the domain to Claude's network whitelist, **configure with your token in the skill file**, and import the skill!
- **[01/14/2026]** **SimpleMem MCP Server is now LIVE and Open Source!** 🎉 Experience SimpleMem as a cloud-hosted memory service at [mcp.simplemem.cloud](https://mcp.simplemem.cloud). Easily integrate with your favorite chat platforms (LM Studio, Cherry Studio) and AI agents (Cursor, Claude Desktop) using the **Streamable HTTP** MCP protocol. The MCP implementation features production-ready optimizations including multi-tenant user isolation, faster response times, and enhanced security. [View MCP Documentation →](MCP/README.md)
- **[01/08/2026]** We've set up a Discord server and WeChat group to make it easier to collaborate and exchange ideas on this project. Welcome to join the Group to share your thoughts, ask questions, or contribute your ideas! 🔥 Join our [Discord](https://discord.gg/KA2zC32M) and [WeChat Group](fig/wechat_logo2.jpg) Now!
- **[01/05/2026]** SimpleMem paper was released on [arXiv](https://arxiv.org/abs/2601.02553)!

---

## 📑 Table of Contents

- [🌟 Overview](#-overview)
- [🎯 Key Contributions](#-key-contributions)
- [🚀 Performance Highlights](#-performance-highlights)
- [📦 Installation](#-installation)
- [⚡ Quick Start](#-quick-start)
- [🔌 MCP Server](#-mcp-server)
- [📊 Evaluation](#-evaluation)
- [📁 File Structure](#-file-structure)
- [📝 Citation](#-citation)
- [📄 License](#-license)
- [🙏 Acknowledgments](#-acknowledgments)

---

## 🌟 Overview

<div align="center">
<img src="fig/Fig_tradeoff.png" alt="Performance vs Efficiency Trade-off" width="900"/>

*SimpleMem achieves superior F1 score (43.24%) with minimal token cost (~550), occupying the ideal top-left position.*
</div>


**SimpleMem** addresses the fundamental challenge of **efficient long-term memory for LLM agents** through a three-stage pipeline grounded in **Semantic Lossless Compression**. Unlike existing systems that either passively accumulate redundant context or rely on expensive iterative reasoning loops, SimpleMem maximizes **information density** and **token utilization** through:

<table>
<tr>
<td width="33%" align="center">

### 🔍 Stage 1
**Semantic Structured Compression**

Entropy-based filtering and de-linearization of dialogue into self-contained atomic facts

</td>
<td width="33%" align="center">

### 🗂️ Stage 2
**Structured Indexing**

Asynchronous evolution from fragmented atoms to higher-order molecular insights

</td>
<td width="33%" align="center">

### 🎯 Stage 3
**Adaptive Retrieval**

Complexity-aware pruning across semantic, lexical, and symbolic layers

</td>
</tr>
</table>

<img src="fig/Fig_framework.png" alt="SimpleMem Framework" width="900"/>

*The SimpleMem Architecture: A three-stage pipeline for efficient lifelong memory through semantic lossless compression*

---

### 🏆 Performance Comparison

<div align="center">

**Speed Comparison Demo**

<video src="https://github.com/aiming-lab/SimpleMem/raw/main/fig/simplemem-new.mp4" controls width="900"></video>

*SimpleMem vs. Baseline: Real-time speed comparison demonstration*

</div>

<div align="center">

**LoCoMo-10 Benchmark Results (GPT-4.1-mini)**

| Model | ⏱️ Construction Time | 🔎 Retrieval Time | ⚡ Total Time | 🎯 Average F1 |
|:------|:--------------------:|:-----------------:|:-------------:|:-------------:|
| A-Mem | 5140.5s | 796.7s | 5937.2s | 32.58% |
| LightMem | 97.8s | 577.1s | 675.9s | 24.63% |
| Mem0 | 1350.9s | 583.4s | 1934.3s | 34.20% |
| **SimpleMem** ⭐ | **92.6s** | **388.3s** | **480.9s** | **43.24%** |

</div>

> **💡 Key Advantages:**
> - 🏆 **Highest F1 Score**: 43.24% (+