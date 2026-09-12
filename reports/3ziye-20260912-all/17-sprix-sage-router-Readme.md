<div align="center">

# Sprix SAGE Router

### Checkpoint-aware mid-execution rerouting for open A2A networks

[![Tests](https://github.com/wang2122/sprix-sage-router/actions/workflows/tests.yml/badge.svg)](https://github.com/wang2122/sprix-sage-router/actions/workflows/tests.yml)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-0F766E.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Research%20Preview-D97706.svg)](#project-status)

**An open-source research output of [Sprix AI](#about-sprix-ai) at 屿智同行.**

Choose whether an in-flight task should **continue**, **recruit collaborators**, or **hand off** after accounting for completed DAG nodes, reusable artifacts, observed partial quality, remaining work, failures, budget, and deadline.

[Quick start](#quick-start) · [Algorithm](ALGORITHM.md) · [Related work](RELATED_WORK.md) · [A2A integration](docs/INTEGRATION.md) · [Operations](docs/OPERATIONS.md) · [Benchmark](#benchmark) · [Changelog](CHANGELOG.md) · [Contributing](CONTRIBUTING.md)

</div>

---

## Why SAGE?

Agent discovery tells a system which agents exist. It does not answer the harder runtime question: **who should work with whom after execution has already begun?**

SAGE—**State-Aware Graph Exchange**—is the decision layer between A2A discovery and task execution. It evaluates three routes in one auditable objective:

| Route | Ownership | Best used when |
|---|---|---|
| **SELF** | Incumbent agent | Existing capability and accumulated context are sufficient |
| **COLLABORATE** | Incumbent retains ownership | A small complementary team covers missing requirements |
| **HANDOFF** | A peer takes full ownership | Specialist advantage exceeds context-transfer loss |

SAGE is designed to sit above the [Agent2Agent (A2A) protocol](https://a2a-protocol.org/latest/). A2A provides Agent Cards, messages, tasks, artifacts, authentication, and transport. SAGE decides **which feasible agent configuration should execute the task, in which mode, and why**.

![SAGE routing pipeline and evidence loop](docs/assets/fig01-system-overview.svg)

<p align="center"><sub><b>Figure 1.</b> SAGE filters candidates, compares all three routing modes, jointly searches assignments and schedules, ranks feasible plans, and learns from execution evidence.</sub></p>

## Research focus

SAGE is deliberately narrow: **checkpoint-aware reconfiguration after execution has begun**.

- **Concrete continuation value.** The router preserves completed requirements and combines in-flight completion, observed partial quality, current ownership, and artifact portability to estimate how much work each candidate must actually redo.
- **Comparable runtime actions.** SELF, COLLABORATE, and HANDOFF share one permission-, budget-, and deadline-constrained action space. Progress-masked and static-coalition baselines receive the same registry and limits.
- **Requirement-conditioned evidence.** Reliability is tracked per agent and requirement instead of assuming that one reputation score transfers across skills.
- **Trajectory-level falsification.** A separate evaluator replays checkpoints and scores artifact reuse, added cost, recovery latency, wasted work, and final quality without calling SAGE's switching equation.

Noisy-OR, beam search, a linear utility, Beta beliefs, online logistic regression, and DAG-induced communication edges are not claimed as inventions. They are replaceable implementation mechanisms. The repository also provides permission-first filtering, bounded candidate search, workload-sensitive quotes, auditable alternatives, degraded-route flags, state persistence, and transport-neutral A2A plans as engineering features.

## Core algorithm

For task requirement \(r\), SAGE combines global and requirement-conditioned trust into calibrated capability \(q_{a,r}\). If the current owner has completed fraction \(f_r\), a candidate owner reuses fraction \(\eta_r\):

$$
\eta_r=\begin{cases}f_r,&\text{owner retained}\\f_r\tau_r,&\text{owner changed}\end{cases},\qquad
\bar q_{a,r}=\eta_r q^{\mathrm{current}}_r+(1-\eta_r)q_{a,r}
$$

Here \(\tau_r\) is artifact portability. Only the assigned owner contributes requirement coverage; adding an unassigned teammate no longer creates a noisy-OR quality gain. The same reused fraction reduces projected remaining cost and duration, so lost work is not charged again inside the learned success probability.

SAGE jointly searches calibrated requirement owners and their schedule. Work assigned to one agent is serialized, work on independent agents can run concurrently, and team-level cost and critical-path latency are checked again after construction.

Every feasible route is ranked by:

$$
U(m,S,z,E)=V\hat p_\theta(y=1\mid x,m,S,z,E)-\lambda_c C-\lambda_l L-\lambda_r R-\lambda_h H-\lambda_o O-\lambda_u\mathcal U+\beta\mathcal B
$$

Here \(z\) is role assignment, \(E\) is the i