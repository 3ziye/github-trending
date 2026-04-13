# Cpueaxh

[English](README.md) | [简体中文](README_CN.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> ![cpueaxh logo](assets/logo.jpg)

`Cpueaxh` is a lightweight, fully dependency-free `x86-64` CPU emulation library with innovative support for emulating execution directly inside the current process memory space.

***This project is under active development. It currently supports common x64 instructions, SSE, SSE2, AVX, AVX2, and a small subset of other instruction sets. The goal is to eventually support the full x86-64 instruction set, including Heaven's Gate transitions. Stay tuned, and issues and contributions are very welcome.***

The project is designed to provide:
- a core execution engine that can be embedded directly in user-mode or kernel/driver-side projects.
- a pure `C ABI` public interface.
- an API style that is as close as practical to [Unicorn](https://github.com/unicorn-engine/unicorn).
- both a [Unicorn](https://github.com/unicorn-engine/unicorn)-like self-managed memory mode **(guest mode)** and direct emulation in real memory space **(host mode)**.
- host-mode memory patching, allowing the emulated CPU to observe bytes different from the underlying real memory.
- a single core codebase that can be built for user mode or compiled directly into a kernel driver through a small platform abstraction layer, without maintaining two copies of the emulator core.
- the library does not depend on exception handling for execution.

### User-mode host-mode demo

![user-mode host-mode demo](assets/example.png)

### Kernel-mode host-mode demo

![kernel-mode host-mode demo](assets/kexample.png)

## Highlights

### 1. Pure C ABI
The public header is [cpueaxh/cpueaxh.hpp](cpueaxh/cpueaxh.hpp).

All exported APIs use the `cpueaxh_*` naming convention and can be called directly from both C and C++.

### 2. Static library form
The core project [cpueaxh/cpueaxh.vcxproj](cpueaxh/cpueaxh.vcxproj) builds as a static library, making integration straightforward.

### 3. Two memory modes
- `CPUEAXH_MEMORY_MODE_GUEST`
  - memory must be mapped explicitly by the user.
  - usage is intentionally close to Unicorn.
- `CPUEAXH_MEMORY_MODE_HOST`
  - emulation runs against the current process address space.
  - supports patch overlays so the CPU can see patched bytes without modifying the underlying real memory.
  - useful for host tracing, live function analysis, and instrumentation.

### 4. Status-based CPU exceptions
Exception state is stored in the CPU context and can be queried through:
- `cpueaxh_code_exception()`
- `cpueaxh_error_code_exception()`

Currently modeled exception types include:
- `#DE`
- `#GP`
- `#SS`
- `#NP`
- `#UD`
- `#PF`
- `#AC`

### 5. Unicorn-like memory management semantics
Guest-mode memory management supports:
- `cpueaxh_mem_map()`
- `cpueaxh_mem_map_ptr()`
- `cpueaxh_mem_unmap()`
- `cpueaxh_mem_protect()`
- `cpueaxh_mem_regions()`

The current implementation includes:
- 4 KB page alignment checks
- range-splitting `unmap` and `protect`
- mapped region enumeration
- separate `READ/WRITE/FETCH_UNMAPPED` results
- separate `READ/WRITE/FETCH_PROT` results

### 6. CPU-level memory attributes
In addition to normal `R/W/X` page permissions, the engine supports CPU-visible page attributes:
- `cpueaxh_mem_set_cpu_attrs()`
- `CPUEAXH_MEM_ATTR_USER`

This allows the emulator to raise proper page faults when CPL and page attributes do not match, rather than degrading to a generic access failure.

### 7. Hooking and escape mechanism
The engine supports basic code hooks, Unicorn-like memory access hooks, and instruction escape handling:
- `cpueaxh_hook_add()` / `cpueaxh_hook_del()`
- `cpueaxh_hook_add_address()` for exact-address hooks
- `CPUEAXH_HOOK_CODE_PRE` and `CPUEAXH_HOOK_CODE_POST`
- `CPUEAXH_HOOK_MEM_READ`, `CPUEAXH_HOOK_MEM_WRITE`, and `CPUEAXH_HOOK_MEM_FETCH`
- `CPUEAXH_HOOK_MEM_READ_UNMAPPED`, `CPUEAXH_HOOK_MEM_WRITE_UNMAPPED`, and `CPUEAXH_HOOK_MEM_FETCH_UNMAPPED`
- `CPUEAXH_HOOK_MEM_READ_PROT`, `CPUEAXH_HOOK_MEM_WRITE_PROT`, and `CPUEAXH_HOOK_MEM_FETCH_PROT`
- `cpueaxh_escape_add()` / `cpueaxh_escape_del()`
- `cpueaxh_host_call()` for bridging an escape into native execution

Memory-access hooks are range-filterable and follow Unicorn-style split semantics. Successful accesses use `cpueaxh_cb_hookmem_t` and report instruction fetches, memory reads, and memory writes together with address, access size, and value. Invalid accesses use `cpueaxh_cb_hookmem_invalid_t`; the callback may fix the mapping/protection state and return nonzero to retry the access, or return `0` to let emulation fail with the corresponding memory error. For invalid reads and fetches the reported value is `0`, while invalid writes report the attempted write value.

An escape is intended for handing selected instructions off from the emulator to a real host-side execution path.
The escape callback receives the decoded instruction bytes together with a mutable `cpueaxh_x86_context`, and ma