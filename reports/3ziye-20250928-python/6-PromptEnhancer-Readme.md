<div align="center">

# PromptEnhancer: A Simple Approach to Enhance Text-to-Image Models via Chain-of-Thought Prompt Rewriting

[**Linqing Wang**](https://scholar.google.com/citations?hl=en&view_op=list_works&gmla=AH8HC4z9rmDHYjp5o28xKk8U4ddD_n7BuMnk8UZFP-jygFBtHUSz6pf-5FP32B_yKMpRU9VpDY3iT8eM0zORHA&user=Hy12lcEAAAAJ) · 
[**Ximing Xing**](https://ximinng.github.io/) · 
[**Yiji Cheng**](https://scholar.google.com/citations?user=Plo8ZSYAAAAJ&hl=en) · 
Zhiyuan Zhao · 
Donghao Li ·
Tiankai Hang ·
Zhenxi Li ·
[**Jiale Tao**](https://scholar.google.com/citations?user=WF5DPWkAAAAJ&hl=en) · 
[**QiXun Wang**](https://github.com/wangqixun) · 
[**Ruihuang Li**](https://scholar.google.com/citations?user=8CfyOtQAAAAJ&hl=en) · 
Comi Chen ·
Xin Li · 
[**Mingrui Wu**](https://scholar.google.com/citations?user=sbCKwnYAAAAJ&hl=en) · 
Xinchi Deng · 
Shuyang Gu · 
[**Chunyu Wang**](https://scholar.google.com/citations?user=VXQV5xwAAAAJ&hl=en)<sup>†</sup> · 
[**Qinglin Lu**](https://luqinglin.weebly.com/)<sup>*</sup>

Tencent Hunyuan

<sup>†</sup>Project Lead · <sup>*</sup>Corresponding Author

</div>

<p align="center">
  <a href="https://www.arxiv.org/abs/2509.04545"><img src="https://img.shields.io/badge/Paper-arXiv:2509.04545-red?logo=arxiv" alt="arXiv"></a>
  <a href="https://zhuanlan.zhihu.com/p/1949013083109459515"><img src="https://img.shields.io/badge/知乎-技术解读-0084ff?logo=zhihu" alt="Zhihu"></a>
  <a href="https://huggingface.co/tencent/HunyuanImage-2.1/tree/main/reprompt"><img src="https://img.shields.io/badge/Model-PromptEnhancer_7B-blue?logo=huggingface" alt="HuggingFace Model"></a>
  <!-- <a href="https://huggingface.co/PromptEnhancer/PromptEnhancer-32B"><img src="https://img.shields.io/badge/Model-PromptEnhancer_32B-blue?logo=huggingface" alt="HuggingFace Model"></a> -->
  <a href="https://huggingface.co/datasets/PromptEnhancer/T2I-Keypoints-Eval"><img src="https://img.shields.io/badge/Benchmark-T2I_Keypoints_Eval-blue?logo=huggingface" alt="T2I-Keypoints-Eval Dataset"></a>
  <a href="https://hunyuan-promptenhancer.github.io/"><img src="https://img.shields.io/badge/Homepage-PromptEnhancer-1abc9c?logo=homeassistant&logoColor=white" alt="Homepage"></a>
  <a href="https://github.com/Tencent-Hunyuan/HunyuanImage-2.1"><img src="https://img.shields.io/badge/Code-HunyuanImage2.1-2ecc71?logo=github" alt="HunyuanImage2.1 Code"></a>
  <a href="https://huggingface.co/tencent/HunyuanImage-2.1"><img src="https://img.shields.io/badge/Model-HunyuanImage2.1-3498db?logo=huggingface" alt="HunyuanImage2.1 Model"></a>
  <a href=https://x.com/TencentHunyuan target="_blank"><img src=https://img.shields.io/badge/Hunyuan-black.svg?logo=x height=22px></a>
</p>

---

<p align="center">
  <img src="assets/teaser-1.png" alt="PromptEnhancer Teaser"/>
</p>

## Overview

Hunyuan-PromptEnhancer is a prompt rewriting utility. It restructures an input prompt while preserving the original intent, producing clearer, layered, and logically consistent prompts suitable for downstream image generation or similar tasks.

- Preserves intent across key elements (subject/action/quantity/style/layout/relations/attributes/text, etc.).
- Encourages a "global–details–summary" narrative, describing primary elements first, then secondary/background elements, ending with a concise style/type summary.
- Robust output parsing with graceful fallback: prioritizes `<answer>...</answer>`; if missing, removes `<think>...</think>` and extracts clean text; otherwise falls back to the original input.
- Configurable inference parameters (temperature, top_p, max_new_tokens) for balancing determinism and diversity.

## 🔥🔥🔥Updates

- [2025-09-22] 🚀 Thanks @mradermacher for adding **GGUF model support** for efficient inference with quantized models!
- [2025-09-18] ✨ Try the [PromptEnhancer-32B](https://huggingface.co/PromptEnhancer/PromptEnhancer-32B) for higher-quality prompt enhancement!
- [2025-09-16] Release [T2I-Keypoints-Eval dataset](https://huggingface.co/datasets/PromptEnhancer/T2I-Keypoints-Eval).
- [2025-09-07] Release [PromptEnhancer-7B model](https://huggingface.co/tencent/HunyuanImage-2.1/tree/main/reprompt).
- [2025-09-07] Release [technical report](https://arxiv.org/abs/2509.04545).

## Prerequisites

- **Python**: 3.8 or higher
- **CUDA**: 11.8+ (recommended for GPU acceleration)
- **Storage**: At least 20GB free space for models
- **Memory**: 8GB+ RAM (16GB+ recommended for 32B models)

## Installation

### Option 1: Standard Installation (Recommended for most users)
```bash
pip install -r requirements.txt
```

### Option 2: GGUF Installation (For quantized models with CUDA support)
```bash
chmod +x script/install_gguf.sh && ./script/install_gguf.sh
```

> **💡 Tip**: Choose GGUF installation if you want faster inference with lower memory usage, especially for the 32B model.

## Model Download

### 🎯 Quick Start (Recommended)
For most users, we recommend starting with the **PromptEnhancer-7B** model:

```bash
# Download PromptEnhancer-7B (13GB) - Best balance of