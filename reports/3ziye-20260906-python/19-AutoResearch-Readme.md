# AutoResearch

<h2 align="center">From Idea to Paper-Ready Evidence</h2>

<p align="center">
  Insight In, Hallucination Out.
</p>

<p align="center">
  English &nbsp;·&nbsp; <a href="README_CN.md">简体中文</a>
</p>

<p align="center">
  <a href="LICENSE"><img alt="License: Apache-2.0" src="https://img.shields.io/badge/License-Apache--2.0-47C9E7"></a>
  <a href="https://www.python.org/"><img alt="Python 3.10+" src="https://img.shields.io/badge/Python-3.10%2B-0B1324"></a>
  <a href="https://evomap.ai"><img alt="EvoMap ecosystem" src="https://img.shields.io/badge/EvoMap-Ecosystem-47C9E7"></a>
  <a href="https://arxiv.org/abs/2608.17906"><img alt="Report: arXiv:2608.17906" src="https://img.shields.io/badge/Report-arXiv%3A2608.17906-B31B1B"></a>
</p>

<p align="center">
  <a href="https://scholar.google.com/citations?user=ayf4nGIAAAAJ">Yiming Ren</a>
  &nbsp;·&nbsp;
  <a href="mailto:liuxiang@evomap.ai">Xiang Liu</a>
  &nbsp;·&nbsp;
  <a href="mailto:sun@evomap.ai">Qumeng Sun</a>
  &nbsp;·&nbsp;
  <a href="mailto:zhangxiao@evomap.ai">Xiao Zhang</a>
  &nbsp;·&nbsp;
  <a href="https://github.com/likaho991007-design">Jiahao Li</a>
</p>

<p align="center">
  Project Leaders:
  <strong><a href="https://autogame-17.github.io/">Haoyang Zhang</a></strong>
  &nbsp;·&nbsp;
  <strong><a href="https://wangjunjie-ai.github.io/">Junjie Wang</a></strong>
</p>

<p align="center">
  Infinite Evolution Lab, <a href="https://evomap.ai">EvoMap</a>
</p>

![AutoResearch workflow from a research idea to reviewable evidence](docs/diagrams/autoresearch-workflow.svg)

AutoResearch is an open-source agent workflow for AI and machine learning research. Give it a research idea, or let it discover directions from recent papers, developer communities, and open-source trends. It continues through experiment planning, implementation, review, execution, result analysis, and independent evaluation to produce an evidence package ready for paper writing.

The workflow is stateful and recoverable. It can iterate based on pilot results and independent review. Research plans, code, run logs, metrics, failure causes, critic reports, and blind reviews are written to disk so researchers can inspect, take over, or stop the process.

![AutoResearch project monitor showing pipeline progress, reviews, and execution rounds](docs/images/autoresearch-project-monitor.png)

## 1. Ways to Use AutoResearch

| Your starting point | Path | Main outputs |
|---|---|---|
| You do not have a specific idea yet | Run Idea Generation | Candidate research directions, reviewed ideas, and experiment plans |
| You already have an idea | Execute the idea directly | Experiment code, run logs, result analysis, and independent review |
| You want the complete workflow | Generate ideas, then select a plan for execution | A complete record from research signals to paper-ready evidence |

## 2. Core Capabilities

| Capability | What you get |
|---|---|
| Cross-domain idea generation | Discover problems from recent external signals, then add constraints and experience from your own domain knowledge |
| Independent multi-model review | Use at least three distinct models during Idea Generation instead of letting one model generate and approve its own work |
| Stateful experiment execution | Persist plans, code, queues, logs, and conclusions so long-running work can resume after interruption |
| Pilot before scaling | Test feasibility at lower cost before starting full experiments or stopping early |
| Traceable evidence and sources | Record Forge sources, knowledge directions, experiment results, critic reports, and blind reviews |
| Support for negative results | Preserve evidence and stop when a hypothesis fails instead of forcing every experiment into a success story |

Research agents can invent missing details when evidence is thin and repeatedly validate their own output. AutoResearch grounds problem discovery in real signals, adds domain knowledge from a local knowledge base, and checks important claims through cross-model review, source records, experiment logs, critic reports, and blind review. These mechanisms reduce unsupported generation, unclear provenance, inflated self-evaluation, and overinterpretation of negative results. The system cannot guarantee that every conclusion is correct, but it preserves the evidence and state needed for researcher review.

## 3. Quickstart

### 3.1 Clone the Repository and Check the Environment

Prepare a Linux machine, either local or accessible over SSH, with Git, Python 3.10+, and `python3-venv` installed:

```bash
git clone https://github.com/EvoMap/AutoResearch.git
cd AutoResearch
bash scripts/bringup.sh
```

`scripts/bringup.sh` creates `.venv`, installs Python dependencies, runs the baseline tests and secret scan, and checks the current model configuration. It does not contact model services or incur API charges.

On the first run, before API credentials are configured, a final `BLOCKED` result or nonzero exit is expected. Confirm that 