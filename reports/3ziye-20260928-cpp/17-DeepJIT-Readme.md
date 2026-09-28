# DeepJIT

DeepJIT is a lightweight, header-only C++20 JIT runtime for **NVIDIA CUDA GPUs** and **HUAWEI Ascend (昇腾) NPUs**. It gives C++/Python extension authors a shared interface for compiling kernel source at runtime, caching the resulting binaries, loading them onto the device, and launching them with backend-specific options.

DeepJIT handles the JIT infrastructure so that kernel libraries can focus on their device code. Both backends share runtime configuration, source and include hashing, in-memory and on-disk caches, and lazy initialization. Kernel source and compiler/launch options remain specific to the selected backend.

**Main authors:** [@guyan364](https://github.com/guyan364), [@kurisu6912](https://github.com/kurisu6912), [@LyricZhao](https://github.com/LyricZhao).

## Features

- **CUDA and Ascend backends:** use `deep_jit::Runtime<deep_jit::CUDA>` or `deep_jit::Runtime<deep_jit::Ascend>` with the same compile/load/launch workflow.
- **Kernel caching:** reuse loaded kernels in memory and compiled artifacts on disk. Cache keys account for source, tracked includes, compiler versions, effective compiler options, and an application-provided dependency signature.
- **Distributed filesystems and shared caches:** share one cache directory across users, processes, and nodes to reuse compiled kernels. Both backends support local and distributed filesystems with the required POSIX filesystem semantics; see [Shared cache](#shared-cache) for configuration.
- **Lazy initialization:** defer device and compiler discovery until the runtime is first used.
- **PyTorch integration:** use the current PyTorch CUDA or `torch_npu` stream by default, and expose the configured runtime through pybind11 with `get_jit()`.
- **Compilation controls and diagnostics:** configure runtime defaults and per-kernel overrides, inspect compilation metadata, and dump CUDA PTX/SASS or Ascend assembly. CUDA also supports a Python post-compilation hook.

### In development (WIP)

- **Cache warmup from history:** use historical cache entries to anticipate kernels that future runs may need and warm up their cache in advance, reducing compilation delays during execution. This feature is under development and is not yet available.
- **Python compilation API:** pass kernel source code directly from Python to compile CUDA or Ascend kernels. This feature is under development and is not yet available.

## Supported backends

| Backend | Device toolchain and runtime | Integration requirements |
| --- | --- | --- |
| **CUDA** | NVCC compiles CUDA source to CUBIN; the CUDA Driver API loads and launches kernels. | CUDA headers 12.4+, NVCC 12.9+, and PyTorch with CUDA support. |
| **Ascend** | Bisheng and ld.lld compile and link Ascend kernel source; ACL loads and launches kernels. | CANN with `bin/bisheng`, `bin/ld.lld`, and the Ascend `adv_api` headers; ACL and `torch_npu` headers and runtime. |

The host environment must provide Linux, a C++20 compiler and standard library with `std::format` support, Python, pybind11, and the dependencies for the selected backend. DeepJIT is intended to be embedded into your extension as a header-only dependency.

See [Integration](#integration) for setup, [CUDA](#cuda) for GPU usage, and [Ascend](#ascend) for NPU usage.

## Shared cache

CUDA and Ascend use the same disk-cache implementation. It supports local and distributed filesystems that provide atomic directory rename within a filesystem and file/directory `fsync`. Builds use unique temporary directories, synchronize their contents, and publish complete entries through an atomic rename. Concurrent processes can compile the same entry and reuse the published result.

Multiple users, processes, and nodes can point to the same cache directory:

```bash
export DJ_JIT_CACHE_DIR=/shared/deep_jit
```

Configure directory permissions so participating users can read shared artifacts and writers can create and publish entries under the cache root. As with all DeepJIT caches, use a trusted shared directory. Matching compilation inputs and cache tags allow users to reuse each other's compiled kernels.

You can also combine a writable personal cache with a shared lookup cache:

```bash
export DJ_JIT_CACHE_DIR="$HOME/.dj:/shared/deep_jit"
```

DeepJIT searches all roots in order and writes cache misses only to the first root. The shared lookup cache can be read-only. To configure a single consumer library, use its prefix instead, for example `MYLIB_JIT_CACHE_DIR`.

## Repository layout

| Path | Contents |
| --- | --- |
| [`include/deep_jit/runtime/`](include/deep_jit/runtime/) | Shared runtime and configuration. |
| [`include/deep_jit/backend/cuda/`](include/deep_jit/backend/cuda/) | CUDA compiler, device queries, kernel loading, and launch options. |
| [`include/deep_jit/backend/ascend/`](include/deep_jit/backend/ascend/) | Ascend compiler/linker integration, device queries, kernel loading, and launch options. |
| [`include/deep_jit/cache/`](include/deep_jit/cache/