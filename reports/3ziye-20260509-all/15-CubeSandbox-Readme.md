<p align="center">
  <img src="docs/assets/cube-sandbox-logo.png" alt="Cube Sandbox Logo" width="140" />
</p>

<h1 align="center">CubeSandbox</h1>

<p align="center">
  <strong>Instant, Concurrent, Secure & Lightweight Sandbox Service for AI Agents</strong>
</p>

<p align="center">
  <a href="https://github.com/tencentcloud/CubeSandbox/stargazers"><img src="https://img.shields.io/github/stars/tencentcloud/cubesandbox?style=social" alt="GitHub Stars" /></a>
  <a href="https://github.com/tencentcloud/CubeSandbox/issues"><img src="https://img.shields.io/github/issues/tencentcloud/cubesandbox" alt="GitHub Issues" /></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/License-Apache_2.0-green" alt="Apache 2.0 License" /></a>
  <a href="./CONTRIBUTING.md"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen" alt="PRs Welcome" /></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/⚡_Startup-Tens_of_ms-blue" alt="Fast startup" />
  <img src="https://img.shields.io/badge/🔒_Isolation-Hardware_Level-critical" alt="Hardware-level isolation" />
  <img src="https://img.shields.io/badge/🔌_API-E2B_Compatible-blueviolet" alt="E2B compatible" />
  <img src="https://img.shields.io/badge/📦_Deploy-High_Concurrency·High_Density-orange" alt="High concurrency & high density" />
</p>

<p align="center">
  <a href="./README_zh.md"><strong>中文文档</strong></a> ·
  <a href="./docs/guide/quickstart.md"><strong>Quick Start</strong></a> ·
  <a href="./docs/index.md"><strong>Documentation</strong></a> ·
  <a href="./docs/changelog.md"><strong>Changelog</strong></a>
</p>

---

Cube Sandbox is a high-performance, out-of-the-box secure sandbox service built on RustVMM and KVM. It supports both single-node deployment and can be easily scaled to a multi-node cluster. It is compatible with the E2B SDK, capable of creating a hardware-isolated sandbox environment with full service capabilities in under 60ms, while maintaining less than 5MB memory overhead.


<p align="center">
  <img src="./docs/assets/readme_speed_en_1.png" width="400" />
  <img src="./docs/assets/readme_overhead_en_1.png" width="400" />
</p>


## Demos

<table align="center">
  <tr align="center" valign="middle">
    <td width="33%" valign="middle">
      <video src="https://github.com/user-attachments/assets/f87c409e-29fc-4e86-9eac-dbeaff2aca18" controls="controls" muted="muted" style="max-width: 100%;"></video>
    </td>
    <td width="33%" valign="middle">
      <video src="https://github.com/user-attachments/assets/50e7126e-bb73-4abc-aa85-677fdf2e8c67" controls="controls" muted="muted" style="max-width: 100%;"></video>
    </td>
    <td width="33%" valign="middle">
      <video src="https://github.com/user-attachments/assets/052e0e77-e2d9-409e-90b8-d13c28b80495" controls="controls" muted="muted" style="max-width: 100%;"></video>
    </td>
  </tr>
  <tr align="center" valign="top">
    <td>
      <em>Installation & Demo</em>
    </td>
    <td>
      <em>Performance Test</em>
    </td>
    <td>
      <em>RL (SWE-Bench)</em>
    </td>
  </tr>
</table>


## Core Highlights

- **Blazing-fast cold start:** Built on resource pool pre-provisioning and snapshot cloning technology, skipping time-consuming initialization entirely. Average end-to-end cold start time for a fully serviceable sandbox is < 60ms.
- **High-density deployment on a single node:** Extreme memory reuse via CoW technology combined with a Rust-rebuilt, aggressively trimmed runtime keeps per-instance memory overhead below 5MB — run thousands of Agents on a single machine.
- **True kernel-level isolation:** No more unsafe Docker shared-kernel (Namespace) hacks. Each Agent runs with its own dedicated Guest OS kernel, eliminating container escape risks and enabling safe execution of any LLM-generated code.
- **Zero-cost migration (E2B drop-in replacement):** Natively compatible with the E2B SDK interface. Just swap one URL environment variable — no business logic changes needed — to migrate from expensive closed-source sandboxes to free Cube Sandbox with better performance.
- **Network security:** CubeVS, powered by eBPF, enforces strict inter-sandbox network isolation at the kernel level with fine-grained egress traffic filtering policies.
- **Ready to use out of the box:** One-click deployment with support for both single-node and cluster setups.
- **Event-level snapshot rollback (coming soon):** High-frequency snapshot rollback at millisecond granularity, enabling rapid fork-based exploration environments from any saved state.
- **Production-ready:** Cube Sandbox has been validated at scale in Tencent Cloud production environments, proven stable and reliable.

## Benchmarks

In the context of AI Agent code execution, CubeSandbox achieves the perfect balance of security and performance:

| Metric | Docker Container | Traditional VM | CubeSandbox |
|---|---|---|---|
| **Isolation Level** | Low (Shared Kernel Namespaces) | High (Dedicated Kernel) | **Extreme (Dedicated Kernel + eB