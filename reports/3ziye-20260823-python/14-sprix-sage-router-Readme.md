<div align="center">

# Sprix SAGE Router

### State-aware agent matching for open A2A networks

[![Tests](https://github.com/wang2122/sprix-sage-router/actions/workflows/tests.yml/badge.svg)](https://github.com/wang2122/sprix-sage-router/actions/workflows/tests.yml)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-0F766E.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Research%20Preview-D97706.svg)](#project-status)

**An open-source research output of [Sprix AI](#about-sprix-ai) at 屿智同行.**

Choose whether an agent should **continue alone**, **recruit complementary collaborators**, or **hand off the task**—then assign task-DAG roles, schedule dependencies, and learn from execution evidence under permission, budget, and deadline constraints.

[Quick start](#quick-start) · [Algorithm](ALGORITHM.md) · [Benchmark](#benchmark) · [Contributing](CONTRIBUTING.md) · [Security](SECURITY.md)

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

![SAGE state-aware routing system](docs/assets/sage-routing-system.svg)

<p align="center"><sub><b>Figure 1.</b> SAGE constrains the candidate space before comparing SELF, COLLABORATE, and HANDOFF, then updates contextual trust from execution evidence.</sub></p>

## What makes SAGE different?

- **Mid-execution tri-mode routing.** SELF, COLLABORATE, and HANDOFF compete in the same utility function instead of relying on disconnected heuristics.
- **Progress-aware replanning.** Active executors, completed DAG nodes, failures, accumulated progress, and transferable context affect whether switching is worthwhile.
- **Complementarity before prestige.** A team is rewarded for marginal requirement coverage, not for collecting individually high-ranked but redundant agents.
- **Contextual trust instead of one reputation score.** Reliability is learned per agent and per requirement, so success in coding does not automatically imply strength in research.
- **Task-DAG role assignment.** Every remaining requirement is assigned to an executor; dependency edges become an inspectable communication topology and critical-path latency estimate.
- **Learned outcome model.** A regularized online predictor replaces the original fixed success equation and can later be swapped for a production reward model.
- **Bounded team search.** Beam search compares multiple team prefixes instead of committing to one greedy sequence.
- **Bid fidelity.** Quoted confidence, cost, and latency are calibrated against observed execution evidence.
- **Permission-first matching.** Ineligible agents never enter the ranking, regardless of predicted quality.
- **Evidence-aware credit.** Per-requirement and per-agent outcomes avoid giving every teammate identical full credit.
- **Auditable output.** Every decision includes assignments, topology, success, coverage, cost, latency, risk, utility, and a human-readable rationale.

## Core algorithm

For task requirement \(r\), SAGE combines global and requirement-conditioned trust into calibrated capability \(q_{a,r}\). Team coverage is:

$$
C_r(S)=1-\prod_{a\in S}(1-q_{a,r})
$$

Each requirement is assigned to the strongest calibrated team member. SAGE schedules these assignments over the requirement DAG, serializing work assigned to one agent and parallelizing independent work assigned to different agents. Team-level cost and critical-path latency are checked again after construction.

Every feasible route is ranked by:

$$
U(m,S,z,E)=V\hat p_\theta(y=1\mid x,m,S,z,E)-\lambda_c C-\lambda_l L-\lambda_r R-\lambda_h H-\lambda_o O-\lambda_u\mathcal U+\beta\mathcal B
$$

Here \(z\) is role assignment, \(E\) is the induced communication topology, \(H\) is context-transfer loss, \(O\) is coordination overhead, and \(\mathcal U/\mathcal B\) support uncertainty-aware exploration. The full design and limitations are documented in [ALGORITHM.md](ALGORITHM.md).

![Conceptual SAGE tri-mode policy map](docs/assets/tri-mode-policy-map.svg)

<p al