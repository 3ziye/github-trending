# DeepGEMM Ascend

DeepGEMM Ascend is a port of DeepGEMM to the HUAWEI Ascend platform. It is fully API-compatible with DeepGEMM and supports BF16, FP8, FP4 GEMM, MQA logits, and MegaMoE. On Ascend platforms, users can simply install the package and use the same APIs and development workflow as DeepGEMM on other supported platforms.

DeepGEMM Ascend provides a lightweight abstraction over the Ascend MAD (matrix multiply-add) primitives, hiding much of the complexity associated with fractal layouts, alignment constraints, address calculations, and verbose low-level parameters. This enables GEMM kernels to remain both concise and efficient. DeepGEMM Ascend makes extensive use of Ascend-specific optimization techniques, such as sparse data loading and coroutine-based pipelining, to approach the performance limits of the Ascend hardware. These implementations can also serve as references for extreme performance optimization on the Ascend platform.

Despite its lightweight codebase, DeepGEMM Ascend can achieve peak hardware performance across a wide range of matrix shapes.

DeepGEMM Ascend 是华为昇腾平台上的 DeepGEMM 实现。它完全兼容 DeepGEMM 的 API，支持 BF16、FP8、FP4 GEMM、MQA logits 和 MegaMoE 算子。DeepGEMM Ascend 和 DeepGEMM 使用相同的包名，用户只需安装当前包，即可沿用其他平台上 DeepGEMM 的 API 和开发流程。

DeepGEMM Ascend 对昇腾平台的矩阵乘加原语（MAD）提供了一个轻量的抽象，能够隐藏分形矩阵布局、对齐约束、地址计算、参数转换等细节，让 GEMM kernel 的实现保持简洁高效。DeepGEMM Ascend 广泛采用昇腾平台特有的优化技术，包括稀疏数据加载、基于协程的流水线等，以接近硬件的性能极限。这些实现也可以作为昇腾平台极致性能优化的参考。

DeepGEMM Ascend 代码轻量，并且在多种矩阵形状上能达到硬件极限性能。

## News

- 2026.09.30: Initial release of DeepGEMM Ascend, with support for Ascend 950 devices. The kernels are designed to achieve near-peak hardware performance.

## Quick Start

### Requirements

- HUAWEI Ascend NPU (developed and validated on the Ascend 950 series)
- CANN 9.20 toolkit providing `bin/bisheng`, `bin/ld.lld`
- Torch NPU package `torch_npu`
- Python 3.10 or higher
- Compilers and standard libraries with C++20 `<format>` support
- `tilelang`, used by the HC prenorm kernel (declared as a package dependency)
- `tree-sitter` and `tree-sitter-cpp`, used to generate Python type stubs when building from source

### Development

```bash
# Submodule must be cloned
git clone --recursive https://github.com/deepseek-ai/DeepGEMM-Ascend.git
cd DeepGEMM-Ascend

# Link some essential includes and build the C++ extension
cat develop.sh
./develop.sh
```

### Installation

```bash
pip install . --no-build-isolation
```

## Interfaces

### Kernel Interface

Please refer to [DeepGEMM's interfaces](https://github.com/deepseek-ai/DeepGEMM#interfaces) for the kernel APIs.

> [!NOTE]
> The scaling factor format on Ascend differs from NVIDIA's: each pair of UE8M0 scaling factors along the K dimension is packed into an `int16`, and the packed values are stored in MN-major order for optimal hardware efficiency.

### Utilities

The library provides some utility functions besides the above kernels:

- `deep_gemm.set_num_sms` / `get_num_sms`: set/get the number of AI cores the kernels may use
- `deep_gemm.set_npu_arch` / `get_npu_arch`: override/query the `dav-*` NPU architecture used for JIT compilation, `0` queries the device
- `deep_gemm.set_mk_alignment_for_contiguous_layout` / `get_mk_alignment_for_contiguous_layout`: set/get the group-level M/K alignment for contiguous layout
- `deep_gemm.get_theoretical_mk_alignment_for_contiguous_layout`: get the theoretical minimum M/K alignment
- `deep_gemm.use_deterministic_algorithms` / `get_deterministic_algorithms`: enable/disable deterministic algorithms
- `deep_gemm.transform_sf_into_required_layout`: transform scaling factors into the required layout
- `deep_gemm.transform_k_grouped_sf_into_required_layout`: transform K-grouped scaling factors into the required layout
- `deep_gemm.get_paged_mqa_logits_metadata`: build the scheduling metadata for the paged MQA kernels
- `deep_gemm.aclnn_fp8_fp4_gemm_{nt, nn, tn, tt}` and `deep_gemm.aclnn_bf16_gemm_{nt, nn, tn, tt}`: ACLNN reference GEMMs used to cross-check the kernels in tests

### Environment Variables

Ascend home path is given by `ASCEND_HOME_PATH` or `ASCEND_TOOLKIT_HOME`.

Each `DG_JIT_*` variable falls back to the corresponding global `DJ_JIT_*` variable when unset, and is snapshotted when the JIT runtime is first created.

- General
    - `DG_JIT_DEBUG`: `0` or `1`, enable JIT debugging features, including compiler commands, load-time reporting, and the selected config per shape; `0` by default
    - `DG_PRINT_CONFIGS`: `0` or `1`, print the selected config for each shape, `0` by default
- JIT cache
    - `DG_JIT_CACHE_DIR`: string, cache directory (or a `:`-separated list of directories) for compiled kernels; lookup searches all paths front-to-back (first hit wins) and a cache miss compiles into the first path, `$HOME/.dj` by default
- Compiler output and artifacts
    - `DG_JIT_PRINT_COMPILER_COMMAND`: `0` or `1`, print compiler and disassembler commands, `0` by default
    - `DG_JIT_PRINT_LOAD_TIME`: `0` or `1`, print kernel load time, `0` by de