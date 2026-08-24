<div align="center">

<img src="docs/images/OAK.png" alt="OAK" width="120" />

# 🌳 OAK — Open Agent Kernel

**The Linux kernel for AI agents.**<br>
Build agents that run 100% on-device. No cloud. No latency. No data leaks.

构建 100% 端侧运行的 AI Agent。无云端依赖，无网络延迟，无数据泄露。

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![CI](https://github.com/OpenSparX/MasterAgent/workflows/CI/badge.svg)](https://github.com/OpenSparX/MasterAgent/actions)
[![Platform](https://img.shields.io/badge/platform-CPU%20%7C%20Qualcomm%20NPU-green.svg)](#-supported-hardware)

> ⚠️ **Status: Alpha** — Core kernel is functional. APIs are unstable. Contributions welcome.

```bash
git clone https://github.com/OpenSparX/MasterAgent.git && cd MasterAgent
cmake -B build -DCMAKE_BUILD_TYPE=Release && cmake --build build -j$(nproc)
```

[Quick Start](#-quick-start) · [Why OAK?](#-why-oak) · [Docs](#-documentation) · [中文文档](#中文)

</div>

---

## ⚡ 30-Second Demo

```bash
$ cmake -B build && cmake --build build -j$(nproc) && ctest --test-dir build

[100%] Built target bench_strategic
Test project /home/you/MasterAgent/build
    Start 1: test_integration_speculation
1/5 Test #1: test_integration_speculation .....   Passed    0.8 sec
    Start 2: test_orset
2/5 Test #2: test_orset .......................   Passed    0.4 sec
    Start 3: test_merkle
3/5 Test #3: test_merkle ......................   Passed    0.4 sec
    Start 4: test_embedding
4/5 Test #4: test_embedding ...................   Passed    0.4 sec
    Start 5: bench_strategic
5/5 Test #5: bench_strategic ..................   Passed    2.9 sec

100% tests passed, 0 tests failed out of 5
```

The OSS build compiles and tests the strategic features: speculative execution,
CRDT mesh sync, formal verification, and embedding search. The full CLI
(with model inference) requires the kernel runtime — see [Architecture](#-architecture).

---

## 🧠 Why OAK?

<table>
<tr>
<td width="33%">

### ⚡ Sub-100ms
No network round-trip. 80% of requests resolve via pattern matching in **microseconds**. The other 20% run local LLM inference.

</td>
<td width="33%">

### 🔒 Private by Default
Data never leaves the device. No telemetry. No cloud calls. Encrypted-at-rest storage with device-bound keys.

</td>
<td width="33%">

### 🔋 NPU-Optimized
Develop on CPU anywhere. Deploy to Qualcomm NPU for **14× speedup** at **3.5× less power**. Same code, different backend.

</td>
</tr>
</table>

### How OAK compares

| | OAK | LangChain | AutoGPT | Apple Intelligence |
|:---|:---:|:---:|:---:|:---:|
| Runs 100% on-device | ✅ | ❌ | ❌ | ✅ |
| Open source | ✅ | ✅ | ✅ | ❌ |
| Crash recovery (WAL) | ✅ | ❌ | ❌ | ❌ |
| Formal verification | ✅ | ❌ | ❌ | ❌ |
| Multi-device mesh | ✅ | ❌ | ❌ | ❌ |
| Speculative execution | ✅ | ❌ | ❌ | ❌ |
| On-device learning | ✅ | ❌ | ❌ | ❌ |
| NPU acceleration | ✅ | ❌ | ❌ | ✅ |
| Latency (typical) | **87ms** | 2-5s | 3-10s | ~200ms |

---

## 🚀 Quick Start

### Build from Source

```bash
# Prerequisites: CMake 3.18+, C++17 compiler (GCC 9+, Clang 11+)
git clone https://github.com/OpenSparX/MasterAgent.git
cd MasterAgent
cmake -B build -DCMAKE_BUILD_TYPE=Release \
      -DMASTER_AGENT_BUILD_CLI=ON \
      -DMASTER_AGENT_BUILD_TESTS=ON
cmake --build build -j$(nproc)

# Run tests
ctest --test-dir build --output-on-failure
```

### Run with a Local Model (llama.cpp)

```bash
# The sparx CLI connects to any llama-server compatible endpoint.
# Start llama-server (install separately: https://github.com/ggml-org/llama.cpp)
llama-server -m your-model.gguf --port 8080

# Run the CLI
./build/cli/sparx run --endpoint 127.0.0.1:8080
```

### Run in Deterministic-Only Mode (No Model Needed)

```bash
# Deterministic skills respond without any model loaded
./build/cli/sparx demo automotive
```

> **💡** Most intent routing works without a model — only open-ended queries need LLM inference.

---

## 📦 What's Open Source

OAK uses an **open-core** model. This repository contains:

| Component | Status | LOC |
|:---|:---:|---:|
| Speculative Execution (LSTM + HNSW) | ✅ Full source | 2,565 |
| Formal Plan Verification (CDCL SAT) | ✅ Full source | 3,656 |
| Agent Mesh (mDNS + CRDT + Merkle) | ✅ Full source | 4,875 |
| On-Device Learning (DP-SGD) | ✅ Full source | 1,800+ |
| Constrained Decoding (GBNF) | ✅ Full source | 1,200+ |
| llama.cpp Model Runtime | ✅ Full source | 527 |
| Agent Scheduler | ✅ Full source | 600+ |
| Kernel Interfaces (headers) | ✅ Public API | — |
| Kernel Runtime (orchestrator, WAL, dispatch) | ❌ Proprietary | — |

The proprietary kernel runtime handles task orchestration, WAL recovery, and agent dispatch. The strategic feature modules (the algorithmic innovations) are fully open and independently testable.

We're working toward open-sourcing the kernel runtime. Track progress in [#1](https://github.com/OpenSparX/MasterAgent/issues/1).

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         User I