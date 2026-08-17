<div align="center">

<img src="docs/images/OAK.png" alt="OAK" width="120" />

# 🌳 OAK — Open Agent Kernel

**The Linux kernel for AI agents.**<br>
Build agents that run 100% on-device. No cloud. No latency. No data leaks.

构建 100% 端侧运行的 AI Agent。无云端依赖，无网络延迟，无数据泄露。

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![CI](https://github.com/OpenSparX/MasterAgent/workflows/CI/badge.svg)](https://github.com/OpenSparX/MasterAgent/actions)
[![Platform](https://img.shields.io/badge/platform-CPU%20%7C%20Qualcomm%20NPU-green.svg)](#-supported-hardware)
[![Version](https://img.shields.io/badge/version-2.1.18-orange.svg)](https://github.com/OpenSparX/MasterAgent/releases)

```bash
npm install -g @sparx/cli && sparx demo automotive
```

[Quick Start](#-quick-start) · [Why OAK?](#-why-oak) · [Docs](#-documentation) · [中文文档](#中文)

</div>

---

## ⚡ 30-Second Demo

```bash
$ sparx demo automotive

🚗 Automotive Voice Assistant
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

You: "Turn on AC, set to 22°C, interior mode"

⚙️  Processing...
├─ Intent: climate_control              ✓  0.02ms (deterministic)
├─ Skills: ac.power, ac.temp, ac.mode   ✓
├─ MCP: vehicle.climate                 ✓  87ms
└─ Result: Climate control updated      ✓

⚡ Total: 87ms | Route: deterministic | Model: not invoked
```

No model was loaded. No GPU required. Pattern matching handled it in **0.02ms**.

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

### Install

```bash
# npm (recommended)
npm install -g @sparx/cli

# Homebrew (macOS)
brew install OpenSparX/masteragent/sparx

# curl (macOS / Linux)
curl -fsSL https://raw.githubusercontent.com/OpenSparX/MasterAgent/main/scripts/install.sh | sh
```

### Your First Agent in 60 Seconds

```bash
# Initialize
sparx init my-agent && cd my-agent

# Download a small model (530 MB)
sparx pull qwen2.5-0.5b-instruct

# Run
sparx run
```

That's it. Type a message:

```
> hello
✓ route=deterministic  skill=hello  0.02ms

> what's the weather like?
✓ route=inference  ttft=142ms  total=1830ms  tokens=28
  I don't have access to real-time weather data...
```

> **💡** `sparx run` works without a model — deterministic skills still respond. Only open-ended questions need one.

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         User Input                               │
└──────────────────────────────┬──────────────────────────────────┘
                               ▼
┌──────────────────────────────────────────────────────────────────┐
│  Preprocessing: UTF-8 normalize → parameter extract → memory     │
└──────────────────────────────┬───────────────────────────────────┘
                               ▼
                    ┌─────────────────────┐
                    │  Route Decision     │
                    │  (80% deterministic │
                    │   20% inference)    │
                    └────┬──────────┬─────┘
                         │          │
              ┌──────────▼──┐  ┌───▼────────────┐
              │ Skill Engine │  │ LLM Inference  │
              │ (0.02ms)     │  │ (87ms NPU /    │
              │              │  │  1200ms CPU)   │
              └──────────┬───┘  └───┬────────────┘
                         │          │
                         ▼          ▼
              ┌────────────────────────────────────┐
              │  Task Orchestrator (DAG execution)  │
              │  + WAL Recovery + MCP Services      │
              └────────────────────────────────────┘
                               ▼
              ┌────────────────────────────────────┐
              │  Response (sub-100ms typical)       │
              └────────────────────────────────────┘
```

<!-- PLACEHOLDER_ARCHITECTURE_CONTINUED -->

<details>
<summary><b>📊 Full architecture diagram</b></summary>
<p align="center">
  <img src="docs/images/sparx-architecture.png" alt="Architecture" width="100%" />
</p>
</details>

**Design principles:**
- **Deterministic first** — 