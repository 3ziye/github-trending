# KVMem + llama.cpp

**Prebuilt downloads:** [Windows x64 CUDA 13 / 12 (rc3)](https://github.com/kvmem/kvmem-llama.cpp/releases/tag/v0.16.0-rc3) · [Linux / WSL2 x86_64 (rc1)](https://github.com/kvmem/kvmem-llama.cpp/releases/tag/v0.16.0-rc1)

**QQ community / QQ 交流群：1040777853**

## Near-lossless Qwen3.8-27B at a full 256K workspace on 16 GiB VRAM

llama.cpp inference with tiered KV memory for long-running agents.

**KVMem** adds a bounded GPU KV working set, host-memory storage and query-based retrieval to [llama.cpp](https://github.com/ggml-org/llama.cpp). llama.cpp handles model loading, inference, quantization and MTP. The separate `llama-kvmem-server` provides OpenAI-compatible chat, tools and optional vision. **NVMe offload is not implemented.**

This port supports **Qwen3.8-27B GGUF quants**, including IQ3 and IQ4. The sibling [kvmem-qw3](https://github.com/kvmem/kvmem-qw3) is a CUDA-native runtime focused on Q8, primarily tested on RTX PRO 6000.

The logical workspace (`-c`) can extend beyond 256K using host RAM; quality at those lengths remains experimental.

The [KVMem paper](https://arxiv.org/abs/2609.04852) shows that, on queries up to 256K, keeping only a **32K GPU-resident active context** is essentially lossless versus the **full 256K** history: **LongMemEval-S** 85.6% vs 86.6% accuracy, **AgentLongBench** 60.9% vs 59.5% task success.

**KV streaming vs. KVMem.** Both methods support a full 256K context on a 16 GiB GPU by storing part of the KV cache in host RAM. [Raymond Huang’s adaptive KV-cache streaming](https://medium.com/@raymond860909/running-qwen-27b-on-16g-vram-with-full-context-length-building-adaptive-kv-cache-streaming-for-bf1e819116e9) keeps part of the KV cache in VRAM and stores the rest in host RAM. During decoding, it prefetches the offloaded KV layer by layer through reusable GPU buffers, overlapping transfers with computation. This preserves attention over the entire history, but longer contexts increase both attention work and PCIe traffic, eventually slowing decode.

KVMem retrieves relevant historical blocks into a bounded GPU window, limiting the KV used for attention. On RTX 5060 Ti, the current MTP3 256K tool benchmark achieves **32–33 token/s decode**, **437–463 token/s prefill for initial computation** and **242–253 token/s overall prefill**, including input reprocessing and cache management.

**Performance on faster GPUs.** Our measurements use the RTX 5060 Ti, the entry-level 16 GB option in the desktop RTX 50 series. The 16 GB RTX 5070 Ti and RTX 5080 offer substantially more compute and roughly twice the memory bandwidth ([NVIDIA specifications](https://www.nvidia.com/en-us/geforce/graphics-cards/compare/)). We therefore expect substantially faster GPU prefill and decode on these cards. Actual gains depend on the workload, CPU and host-memory transfers; benchmarks on these GPUs are welcome.

Current milestone: [`v0.16.0-rc3`](docs/milestones/v0.16.0-rc3.md) (pre-release).

**Limitation:** one generation cannot exceed `--kvmem-gen-reserve` (16384 tokens on the IQ3 recipe, 12288 on IQ4), including thinking. Retrieval pins the GPU window; new tokens only use those reserved slots. We are working on fixing this. For agent use, add a line to the system prompt such as: *Keep each turn's output, including thinking, within 16384 tokens* (use 12288 on IQ4). That makes oversized single-turn replies much less likely.

Version: **0.16.0-rc3**. See the [English / 中文 release notes](docs/releases/v0.16.0-rc3.md) for CUDA build choices and measured results.

## How KVMem works

Completed KV blocks are stored in host RAM. For each agent step, KVMem retrieves relevant blocks using the current query and places them in chronological order in a bounded GPU working set. Previously computed KV is reused across turns.

![High-level KVMem flow](docs/assets/kvmem-flow.svg)

Core flags (what the 16 GiB recipes still pass):

| Flag | Meaning |
|---|---|
| `-c` | Logical workspace, including history stored off GPU. 256K is the tested default; larger is experimental. |
| `--kvmem-budget` | How many historical tokens retrieval may keep on GPU. |
| `--kvmem-sink-tokens N` | Server and CLI: always keep the prefix in the GPU working set. Default `0` keeps one block (not disabled). Positive values round down to whole blocks, with a minimum of one block. For example, with block size 128, `1024` keeps 1024 tokens and `129` keeps 128. These blocks count toward `--kvmem-budget`. |
| `--kvmem-gen-reserve` | GPU slots reserved for new tokens so retrieval cannot fill the pool. **One generation cannot exceed this length** (including thinking). |
| `--kv-dtype` | Sets the same cache type for **main** attention K and V (IQ3 q8_0, IQ4 q5_0). Use `-ctk q8_0 -ctv q4_0` for mixed precision. |
| `--spec-type draft-mtp` | Enable multi-token prediction. |
| `--mmproj` | Vision projector GGUF. Omit for text-only. |

KVMem retrieval is on by default, with 128-token blocks, query replay `auto`, query policy `user`, M