<div align="center">

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║        ███████╗██╗   ██╗██████╗ ███╗   ███╗██╗ ██████╗██████╗  ██████╗        ║
║        ██╔════╝██║   ██║██╔══██╗████╗ ████║██║██╔════╝██╔══██╗██╔═══██╗       ║
║        ███████╗██║   ██║██████╔╝██╔████╔██║██║██║     ██████╔╝██║   ██║       ║
║        ╚════██║██║   ██║██╔══██╗██║╚██╔╝██║██║██║     ██╔══██╗██║   ██║       ║
║        ███████║╚██████╔╝██████╔╝██║ ╚═╝ ██║██║╚██████╗██║  ██║╚██████╔╝       ║
║        ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝        ║
║                                                                               ║
║            Sub-Microsecond Execution Engine for Algorithmic Trading           ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

<h1>Ultra-Low Latency Trading System</h1>

<p>
<b>Deterministic, nanosecond-precise execution engine for quantitative trading research</b>
</p>

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen?style=for-the-badge)](.)
[![C++17](https://img.shields.io/badge/C%2B%2B-17-blue?style=for-the-badge&logo=cplusplus)](.)
[![Rust](https://img.shields.io/badge/Rust-1.70%2B-orange?style=for-the-badge&logo=rust)](.)
[![License](https://img.shields.io/badge/license-Proprietary-red?style=for-the-badge)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=for-the-badge)](.)
[![GitHub Sponsors](https://img.shields.io/badge/Sponsor-krish567366-ff69b4?style=for-the-badge&logo=github)](https://github.com/sponsors/krish567366)

<p>
<a href="https://submicro.krishnabajpai.me/">Live Demo</a> •
<a href="#key-features">Features</a> •
<a href="#quick-start">Quick Start</a> •
<a href="#benchmarks">Benchmarks</a> •
<a href="#architecture">Architecture</a> •
<a href="#documentation">Docs</a>
</p>

---

### **890ns median latency** | **Deterministic replay** | **Lock-free architecture** | **Research-grade framework**

**[View Interactive Documentation →](https://submicro.krishnabajpai.me/)**

---

> [!TIP]
> **Branching Strategy**:
> *   **`main`**: Fundamental execution infrastructure. Primary focus is **Latency Minimization** (median < 900ns) and system determinism.
> *   **`alpha-optimized`**: Quantitative modeling layer. Primary focus is **Alpha & Signal Optimization** (multi-kernel Hawkes, SIMD features) while keeping latency within sub-microsecond thresholds.

</div>

---

## What Makes This Special?

> **Built for researchers and systems engineers pushing the boundaries of low-latency execution.**

This isn't just another trading bot. It's a **complete infrastructure** for understanding, measuring, and optimizing execution latency at the **hardware level**.

### The Problem
Traditional trading systems are black boxes with unpredictable latency, non-deterministic behavior, and poor visibility into where microseconds are lost.

### The Solution
A **transparent, deterministic execution engine** that:
- Achieves **sub-microsecond decision latency** (890ns median)
- Guarantees **bit-identical replay** for audit and debugging
- Provides **nanosecond-level instrumentation** at every stage
- Uses **zero-allocation hot paths** and lock-free data structures
- Simulates **kernel-bypass networking** (DPDK-style)
- Implements **institutional-grade logging** and monitoring

**Research & Education Only** — Not production-ready. Hardware validation (DPDK/FPGA) is simulated. [Learn more](#hardware-validation--future-work).

**PROPRIETARY LICENSE** — Commercial use prohibited. Written permission required. Contact: krishna@krishnabajpai.me

## Performance Snapshot

<div align="center">

| **Component** | **Median** | **p99** | **p99.9** | 
|------------------|--------------|-----------|--------------|
| Market Data Ingestion | **87 ns** | 124 ns | 201 ns |
| Signal Extraction (SIMD) | **40 ns** | 48 ns | 67 ns |
| Hawkes Update (Power-Law) | **150 ns** | 189 ns | 234 ns |
| **End-to-End Decision** | **890 ns** | **921 ns** | **1047 ns** |
| Order Serialization | **34 ns** | 41 ns | 58 ns |

**Measurement Precision:** ±5ns (TSC jitter) | ±17ns (PTP offset)  
**Test Hardware:** Intel Xeon Platinum 8280 @ 2.7GHz, isolated core, RT kernel

</div>

---

## Key Features

<table>
<tr>
<td width="50%">

### **Performance**
- Sub-microsecond decision latency
- Zero-copy data paths
- Lock-free SPSC/MPSC queues
- Cache-aligned data structures
- SIMD-optimized computations (AVX-512)

</td>
<td width="50%">

### **Determinism**
- Bit-identical replay guarantees
- Event-driven scheduling
- Fixed RNG seeds
- Pre-allocated memory pools
- TSC-level timestamp precision

</td>
</tr>
<tr>
<td width="50%">

### **Architecture**
- Kernel-bypass NIC simulation
- Multivariate Hawkes process
- Avellaneda-Stoikov market making
- Adaptive risk management
- C++/Rust FFI integration

</td>
<td width="50%">

