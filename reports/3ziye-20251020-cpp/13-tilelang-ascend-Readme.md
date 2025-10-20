<img src=./images/logo-row.svg />

<div align="center">

# TileLang-Ascend


[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/tile-ai/tilelang-ascend)

</div>

Tile Language Ascend (**tilelang-ascend**) is a specialized variant of the tile-lang domain-specific language, specifically optimized for Huawei Ascend NPU (Neural Processing Unit) architecture. Built upon the foundation of tile-lang's Pythonic syntax and [TVM](https://tvm.apache.org/) compiler infrastructure, tilelang-ascend enables developers to efficiently create high-performance AI compute kernels tailored for Ascend processors, including operations like GEMM, vector operations, and attention mechanisms. Tilelang-ascend allows developers to focus on productivity without sacrificing the low-level optimizations necessary for state-of-the-art performance on the NPU. The compiler backend supports two technical routes: [Ascend C & PTO](https://github.com/tile-ai/tilelang-ascend/tree/ascendc_pto) and [AscendNPU IR](https://github.com/tile-ai/tilelang-ascend/tree/npuir).

<p align="center">
  <img src="./images/tl-ascend-gemm.png" width="100%" alt="image">

</p>

## Latest News
- 09/29/2025 🚀: We are excited to announce that tilelang-ascend, a dsl for high performance AI workloads on Ascend NPUs, is now open source and available to the public!

## Tested Devices
Although tilelang-ascend aims to be portable across a range of Ascend devices, it has been specifically tested and validated on the following NPUs: A2 and A3.

## OP Implementation Examples
**tilelang-ascend** provides the building blocks to implement a wide variety of operators on the NPU.
Some examples include:

- [Matrix Multiplication](./examples/gemm/)
- [Vector Add](./examples/elementwise/)
- [Flash Attention](./examples/flash_attention/)


Within the `examples` directory, you will also find additional complex kernels—such as [LightningIndexer](./examples/lightning_indexer/) and [SparseFlashAttention](./examples/sparse_flash_attention/), more operators will continuously be added.


## Installation

### Environment Preparation
We assume you already have an ascend environment with CANN (at least [8.2.RC1](https://www.hiascend.com/developer/download/community/result?from=firmware&product=1&model=30&cann=8.2.RC1)) and torch-npu (at least 2.6.0.RC1) installed. Firstly, set cann environment variables.

  ```bash
  source {your-cann-installed-path}/ascend-toolkit/set_env.sh
  ```

### TileLang-Ascend Installation

Here we use the method of compiling from source code for installation.

#### a) Download

    git clone --recursive https://github.com/tile-ai/tilelang-ascend.git
    cd tilelang-ascend

#### b) Compile and Install
    bash install_ascend.sh

#### c) Environment Variable Setup

    source set_env.sh

## Run


In this section, you will learn how to call NPU TileLang operators.

Here we use the **Matrix Multiplication** operator as an example for introduction.


```
cd examples/gemm
python example_gemm.py
```

Upon success, it will print:

```
Kernel Output Match!
```

## Comparison with NVIDIA Backend Implementation

GPUs primarily feature a three-level memory hierarchy that can be analogously mapped to NPU hardware architecture as follows:

**Memory Hierarchy Mapping:**
- `global memory` ↔ `global memory`
- `shared memory` ↔ `L1 buffer on cube core and unified buffer on vector core`  
- `register memory` ↔ `L0A/B/C buffer`

**Memory Management:**
TileLang-Ascend provides memory allocation primitives similar to the GPU version. For example, `alloc_{L1/ub/...}` functions allow on-chip memory allocation in a manner comparable to GPU programming.

**Execution Model Differences:**
At the execution level, NPUs lack thread-level abstractions. Therefore, we currently provide computation primitives operating at the `tile` granularity on vector cores. While the GPU version enables automatic parallelization of internal computations (e.g., addition) across different threads using `T.Parallel`, the NPU version requires manual vectorization through primitives like `T.add`.

**Cross-Core Communication:**
Additionally, since cube and vector cores on NPUs can only exchange data through global memory/L2 cache, the current implementation requires explicit specification of execution code for different cores using the `T.Scope` primitive. Synchronization between cores is managed through `T.set_cross_flag` and `T.wait_cross_flag`, and intermediate data transfer global tensors must be explicitly specified during kernel definition.


## Quick Start

In this section, you'll learn how to write and execute a straightforward GEMM (matrix multiplication) kernel using tilelang-ascend, The next chapter will introduce how to write a high-performance gemm kernel.

### GEMM Example with Annotations

Below is an example that demonstrates how to quickly implement a gemm on the ascend.

```python
@tilelang.jit(out_idx=[-1])
def matmul(M, N, K, block_M, block_N, K_L1, dtype="float16", accum_dtype="floa