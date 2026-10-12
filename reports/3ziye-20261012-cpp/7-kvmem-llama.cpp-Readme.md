# KVMem: llama.cpp and ninfer backends

<a id="downloads"></a>

## Downloads / 下载导航

**Before starting / 启动前：Use English paths for the package and model. 运行包和模型的完整路径不能含中文，包括用户名、上级目录和文件名。**

| 用途 / Audience | 后端 / Backend | 模型 / Model | 下载 / Download | 状态 / Status |
|---|---|---|---|---|
| Windows NVIDIA RTX 30/40/50 | NInfer | `.ninfer` | [v0.18.0 RC2](https://github.com/kvmem/kvmem-llama.cpp/releases/tag/v0.18.0-ninfer-rc2) | 预发布 / Prerelease |
| Windows NVIDIA | llama.cpp | GGUF | [CUDA RC3](https://github.com/kvmem/kvmem-llama.cpp/releases/tag/v0.16.0-rc3) | 预发布 / Prerelease |
| Linux / WSL2 NVIDIA | llama.cpp | GGUF | [CUDA RC3](https://github.com/kvmem/kvmem-llama.cpp/releases/tag/v0.16.0-rc3) | 预发布 / Prerelease |
| Windows / Linux / WSL2 AMD | llama.cpp | GGUF | [ROCm Beta2](https://github.com/kvmem/kvmem-llama.cpp/releases/tag/rc3-rocm-beta2) | 测试版 / Beta |
| Windows Bonsai 2 | Bonsai 专用 / Dedicated | PTQ1 GGUF | [prism.3](https://github.com/kvmem/kvmem-llama.cpp/releases/tag/v0.16.0-rc3-prism.3) | 专用实验版 / Experiment |
| 自行编译 / Build from source | llama.cpp | GGUF | [v0.17.0 source](https://github.com/kvmem/kvmem-llama.cpp/releases/tag/v0.17.0) | 仅源码 / Source only |

**Windows RTX 30/40/50 users are encouraged to try the NInfer prerelease. 推荐 Windows RTX 30／40／50 系用户尝试 NInfer 预发布版。** NInfer uses `.ninfer` models; llama.cpp uses GGUF. Models are downloaded separately. 两个后端的模型格式不同，模型需另行准备。

**QQ community / QQ 交流群：1040777853**

## Near-lossless Qwen3.8-27B at a full 256K workspace on 16 GiB VRAM

llama.cpp inference with tiered KV memory for long-running agents.

**KVMem** adds a bounded GPU KV working set, host-memory storage and query-based retrieval to [llama.cpp](https://github.com/ggml-org/llama.cpp). llama.cpp handles model loading, inference, quantization and MTP. The separate `llama-kvmem-server` provides OpenAI-compatible chat, tools and optional vision. This source version also supports opt-in NVMe snapshots for inactive sessions; the rc3 prebuilts listed below predate that feature.

This port supports **Qwen3.8-27B GGUF quants**, including IQ3 and IQ4. The sibling [kvmem-qw3](https://github.com/kvmem/kvmem-qw3) is a CUDA-native runtime focused on Q8, primarily tested on RTX PRO 6000.

The logical workspace (`-c`) can extend beyond 256K using host RAM; quality at those lengths remains experimental.

The [KVMem paper](https://arxiv.org/abs/2609.04852) shows that, on queries up to 256K, keeping only a **32K GPU-resident active context** is essentially lossless versus the **full 256K** history: **LongMemEval-S** 85.6% vs 86.6% accuracy, **AgentLongBench** 60.9% vs 59.5% task success.

**KV streaming vs. KVMem.** Both methods support a full 256K context on a 16 GiB GPU by storing part of the KV cache in host RAM. [Raymond Huang’s adaptive KV-cache streaming](https://medium.com/@raymond860909/running-qwen-27b-on-16g-vram-with-full-context-length-building-adaptive-kv-cache-streaming-for-bf1e819116e9) keeps part of the KV cache in VRAM and stores the rest in host RAM. During decoding, it prefetches the offloaded KV layer by layer through reusable GPU buffers, overlapping transfers with computation. This preserves attention over the entire history, but longer contexts increase both attention work and PCIe traffic, eventually slowing decode.

KVMem retrieves relevant historical blocks into a bounded GPU window, limiting the KV used for attention. On RTX 5060 Ti, the current MTP3 256K tool benchmark achieves **32–33 token/s decode**, **437–463 token/s prefill for initial computation** and **242–253 token/s overall prefill**, including input reprocessing and cache management.

**Performance on faster GPUs.** Our measurements use the RTX 5060 Ti, the entry-level 16 GB option in the desktop RTX 50 series. The 16 GB RTX 5070 Ti and RTX 5080 offer substantially more compute and roughly twice the memory bandwidth ([NVIDIA specifications](https://www.nvidia.com/en-us/geforce/graphics-cards/compare/)). We therefore expect substantially faster GPU prefill and decode on these cards. Actual gains depend on the workload, CPU and host-memory transfers; benchmarks on these GPUs are welcome.

Previous milestone: [`v0.16.0-rc3`](docs/milestones/v0.16.0-rc3.md) (pre-release).

**Limitation:** one generation cannot exceed `--kvmem-gen-reserve` (16384 tokens on the IQ3 recipe, 12288 on IQ4), including thinking. Retrieval pins the GPU window; new tokens only use those reserved slots. We are working on fixing this. For agent use, add a line to the system prompt such as: *Keep each turn's output, including thinking, within 16384 tokens* (use 12288 on IQ4). That makes oversized single-turn replies much less likely.

Source version: **0.17.0**. See the [English / 中文 release notes](docs/releases/v0.17.0.md) for the core changes. The prebuilt downloads below are older rc3/beta 2 packages, not v0.17.0 binaries.

## How KVMem works

Completed KV blocks are stored in host RAM. For each agent step, KVMem retrieves relevant blocks u