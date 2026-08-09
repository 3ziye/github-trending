<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/figs/axisrl-logo-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="docs/figs/axisrl-logo-light.svg">
    <img alt="AxisRL - Agentic Post-Training" src="docs/figs/axisrl-logo-light.svg" width="680">
  </picture>

  <p>
    <strong>English</strong> ·
    <a href="docs/README-cn.md">简体中文</a>
  </p>

  <p>
    <a href="https://github.com/XYZ-AI-Lab/axrl/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/XYZ-AI-Lab/axrl/actions/workflows/ci.yml/badge.svg"></a>
    <img alt="Python 3.12+" src="https://img.shields.io/badge/Python-3.12%2B-blue.svg">
    <a href="https://github.com/astral-sh/ruff"><img alt="Ruff" src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json"></a>
    <a href="LICENSE"><img alt="License: Apache-2.0" src="https://img.shields.io/badge/License-Apache_2.0-blue.svg"></a>
    <a href="https://github.com/XYZ-AI-Lab/axrl/pulls"><img alt="PRs Welcome" src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg"></a>
  </p>

  <p>
    <a href="https://xyz-lab.ai">XYZ AI Lab</a> ·
    <a href="https://xyz-lab.ai/blogs/ai4ai-at-scale/">Technical Blog</a>
  </p>
</div>

# AxisRL

AxisRL is an agentic RL post-training framework built on SGLang rollout, Megatron training, and real-world agent workflows.

AxisRL connects high-throughput rollout, large-scale training, weight synchronization, data movement, resource scheduling, and reproducible debugging inside one coherent framework. SGLang and Megatron remain the core serving and training engines; AxisRL handles the system layer around agentic post-training.

## ✨ Highlights

- Built on **SGLang** for high-throughput rollout and **Megatron** for large-scale distributed training.
- Used in agent RL workflows with 300+ turn trajectories and training runs at hundreds-of-billions-parameter scale.
- Provides configurable policy optimization objectives including PPO, GRPO/GRPO2, GSPO, TOPR, TIS, and related variants.
- Supports both white-box agent environments and black-box harness capture through an OpenAI-compatible proxy.
- Reduces rollout/training idle time with partial rollout and a lightweight control plane.
- Provides handle-based data movement, context packing, routing replay, mismatch analysis, and spike replay for rollout-trainer consistency.

## 🧭 Why AxisRL?

LLM post-training workloads are moving beyond single-turn question answering. In agentic RL, a model may interact with a long-lived environment, call tools, observe tool results, update context, and receive a reward only after several turns.

That changes the job of a post-training framework. It has to coordinate multi-turn rollout, environment state, tool calls, verifiers, reward collection, training sample construction, and weight synchronization. It also has to make training behavior observable, because small differences in tokenization, chat templates, logprobs, routing, packing, or weight sync can appear later as loss spikes, reward instability, or rollout-trainer mismatch.

AxisRL is designed for this setting: real agent workflows, SGLang rollout, Megatron training, and the system contracts between them.

## 🏗️ Architecture

![AxisRL workflow](docs/figs/axrl-workflow.png)

At a high level, an AxisRL run follows this loop:

1. Rollout actors execute task-specific agent workflows.
2. SGLang workers serve model generation.
3. Environments, tools, verifiers, or external harnesses produce interaction records and rewards.
4. Megatron workers consume training samples and run PPO or GRPO-family training.
5. Updated weights are synchronized back to the rollout side for the next iteration.

AxisRL keeps the driver lightweight. The driver manages scheduling, lifecycle, metrics, phase transitions, and metadata. Heavy payloads, such as routing replay data or future multimodal artifacts, move through a handle-based data path and are read by trainer workers on demand.

## 🎯 Design Goals

| Goal | Problem | AxisRL Approach |
| --- | --- | --- |
| Flexibility | Agent workflows differ in control flow, tools, rewards, context management, and resource needs. | Use recipes for task logic, support white-box environments and black-box harness capture, and manage heterogeneous components through resource groups. |
| Efficiency | Long-tail trajectories, tool latency, verifiers, and repeated context can leave rollout or training resources idle. | Use partial rollout, thin control-plane scheduling, handle-based data movement, prefix-tree merge, MagiAttention, and off-policy stabilization tools such as TIS, sequence masking, and Icepop. |
| Observability | Rollout and trainer paths can silently diverge in tokenization, masks, logprobs, routing, packing, or weight versions. | Test critical boundaries and provide mismatch analysis, routing replay checks, and spike replay for reproducible debugging. |

## ⚙️ Installation

The recomm