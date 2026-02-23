# NTransformer

High-efficiency C++/CUDA LLM inference engine. Runs Llama 70B on a single RTX 3090 (24GB VRAM) by streaming model layers through GPU memory via PCIe, with optional NVMe direct I/O that bypasses the CPU entirely.

## Key Results

| Model | Mode | Decode | VRAM | Notes |
|-------|------|--------|------|-------|
| Llama 3.1 8B Q8_0 | Resident | 48.9 tok/s | 10.0 GB | All layers in VRAM |
| Llama 3.1 8B Q8_0 | Tiered (auto) | 48.8 tok/s | 10.3 GB | 32/32 layers auto-promoted to VRAM |
| Llama 3.1 70B Q6_K | Streaming (mmap) | 0.006 tok/s | 7.3 GB | Page cache thrashing (53 GB > 48 GB RAM) |
| Llama 3.1 70B Q6_K | Tiered (auto) | 0.2 tok/s | 23.1 GB | 26 VRAM + 54 RAM + 0 NVMe |
| Llama 3.1 70B Q4_K_M | Tiered (auto) | 0.3 tok/s | 22.9 GB | 36 VRAM + 44 RAM (50% faster) |
| Llama 3.1 70B Q4_K_M | **Tiered + layer skip** | **0.5 tok/s** | **22.9 GB** | **36 VRAM + 44 RAM, 20 layers skipped** |

**3-tier adaptive caching** auto-sizes from hardware: VRAM-resident layers (zero I/O) + pinned RAM (H2D only) + NVMe/mmap fallback. Achieves **83x speedup** over mmap baseline for 70B on consumer hardware (RTX 3090 + 48 GB RAM).

Bottleneck is PCIe H2D bandwidth at Gen3 x8 (~6.5 GB/s). Q4_K_M fits 10 more layers in VRAM (36 vs 26), reducing tier B transfers. Layer skip (cosine similarity calibration) eliminates 20/80 layers per token with minimal quality loss.

## Features

- **Zero external dependencies** beyond CUDA Toolkit (no PyTorch, no cuBLAS)
- **GGUF model format** with Q4_0, Q8_0, Q4_K_M, Q5_K, Q6_K, F16, F32 quantization
- **3-Tier Adaptive Caching**: auto-sized VRAM resident + pinned RAM + NVMe/mmap tiers
- **SLEP streaming**: double-buffered layer pipeline overlaps NVMe reads, PCIe DMA, and GPU compute
- **gpu-nvme-direct backend**: userspace NVMe driver reads model weights directly to pinned GPU-accessible memory
- **Layer skip**: cosine-similarity calibration skips redundant layers (20/80 skipped at threshold 0.98)
- **Self-speculative decoding**: VRAM-resident layers as draft model (no extra model needed)
- **Four data paths** (auto-selected): VRAM resident > pinned RAM H2D > mmap pinned > CPU worker memcpy
- Llama architecture: RoPE, GQA, SwiGLU, RMSNorm, KV cache

## Requirements

- Linux (tested on Ubuntu, kernel 6.17+)
- CUDA Toolkit 13.1
- gcc-14 / g++-14
- NVIDIA GPU with Compute Capability 8.0+ (RTX 3090 tested)
- CMake 3.24+
- (Optional) NVMe SSD on separate PCIe slot + [gpu-nvme-direct](https://github.com/xaskasdf/gpu-nvme-direct) library

## Quick Start

```bash
# Build
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_C_COMPILER=gcc-14 \
  -DCMAKE_CXX_COMPILER=g++-14 \
  -DCMAKE_CUDA_COMPILER=/usr/local/cuda-13.1/bin/nvcc
cmake --build . -j

# Run (resident mode — model fits in VRAM)
./ntransformer -m /path/to/llama-8b-q8_0.gguf -p "Hello" -n 128

# Run (streaming mode — model larger than VRAM)
./ntransformer -m /path/to/llama-70b-q6_k.gguf -p "Hello" -n 32 --streaming

# Run with layer skip (fastest for 70B)
./ntransformer -m /path/to/llama-70b-q4_k_m.gguf -p "Hello" -n 32 --streaming --skip-threshold 0.98

# Self-speculative decoding (VRAM layers as draft, no extra model)
./ntransformer -m /path/to/llama-70b-q6_k.gguf -p "Hello" -n 32 --self-spec --draft-k 3

# Chat mode
./ntransformer -m /path/to/model.gguf --chat

# Benchmark
./ntransformer -m /path/to/model.gguf --benchmark -n 64
```

## System Setup

Running ntransformer with NVMe direct I/O requires system-level modifications. An automated setup script handles all of them:

```bash
# Full first-time setup (interactive, creates backups)
sudo ./scripts/setup_system.sh

# Check current system state (no changes)
sudo ./scripts/setup_system.sh --check

# NVMe-only (run after every reboot)
sudo ./scripts/setup_system.sh --nvme-only
```

### What the script modifies and why

| Phase | What | Why | Risk | Rollback |
|-------|------|-----|------|----------|
| 1 | Installs gcc-14, cmake, kernel headers | CUDA 13.1 is incompatible with gcc-15 (Ubuntu 25.10 default) | Low — standard packages | `apt remove` |
| 2 | Adds `amd_iommu=off` to GRUB | AMD root complex drops GPU→NVMe P2P reads if IOMMU is on. Disabling IOMMU lets posted PCIe writes (doorbells) through | **Medium** — removes hardware DMA isolation between all PCIe devices. Don't run on multi-tenant/server systems | Remove `amd_iommu=off` from `/etc/default/grub`, run `update-grub`, reboot |
| 3 | Patches NVIDIA DKMS (`os-mlock.c`) | `follow_pfn()` was removed in kernel 6.12+. Without the patch, `cudaHostRegisterIoMemory` fails and the GPU can't map NVMe BAR0 for MMIO writes | **High** — bad patch prevents GPU driver from loading (black screen on reboot). Backup `.orig` created automatically | `cp os-mlock.c.orig os-mlock.c` in DKMS source dir, `dkms remove/install nvidia/VERSION` |
| 3b | Patches CUDA header (`math_functions.h`) | glibc 2.42+ (Ubuntu 25.10) declares `rsqrt()`/`rsqrtf()` with `noexcept`. CUDA 13.1 declares without, causing build failure | Lo