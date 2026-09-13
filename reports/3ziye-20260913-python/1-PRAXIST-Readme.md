<p align="center">
  <img src="docs/assets/brand/praxist-banner.svg" alt="Praxist" width="800">
</p>

<h1 align="left">Praxist: meet your personal R&amp;D team</h1>

<p align="center">
  <a href="../../actions/workflows/ci.yml"><img src="../../actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://praxist.sapient.inc/en/docs"><img src="https://img.shields.io/badge/docs-open-334155" alt="Documentation"></a>
  <a href="https://arxiv.org/abs/2608.25955"><img src="https://img.shields.io/badge/arXiv-2608.25955-B31B1B.svg" alt="arXiv paper"></a>
  <a href="https://discord.gg/sapient"><img src="https://img.shields.io/badge/Discord-Join-5865F2?logo=discord&amp;logoColor=white" alt="Discord"></a>
  <img src="https://img.shields.io/badge/Python-3.11%2B-3776AB" alt="Python 3.11+">
</p>

Praxist is an autonomous research system for measurable, computer-executable
research. It coordinates parallel research peers, task-owned evaluation,
durable evidence, and generation-to-generation synthesis.

Praxist treats research as a persistent process rather than a sequence of
disconnected prompts. Use it when a project already runs and its objective is
measurable, but the best path forward is still unknown.

<p align="center">
  <img src="docs/assets/figures/praxist-overview.svg" alt="Praxist architecture" width="920">
</p>

## Install Praxist

Install the complete runtime integrations and finish first-use setup with one
command:

```bash
python3 -m pip install --index-url https://pypi.org/simple "praxist[agents,codex]" && praxist setup --interactive --install-skills codex
```

The local wizard covers the Fair Source License, User Agreement, privacy,
runtime profile, masked credentials, Codex skills, writable examples,
and readiness checks. It does not select a research project or launch a run.
For Claude Code, use the
[host-specific one-line command](docs/getting-started/installation.md#install-and-configure).

For an agent-managed installation, open Codex:

```bash
codex --yolo
```

Then ask it to install and configure Praxist using the packaged OOBE runbook,
and to stop after readiness checks.

Before starting research, read the [Quickstart](docs/getting-started/quickstart.md)
and [Your First Task](docs/getting-started/first-task.md). They describe the
separate takeover step and the project contract it creates.

Choose **Codex-native mode** to use an existing Codex subscription without an
API key. For sustained research, Praxist generally favors
[open-source model APIs](docs/guides/open-source-model-apis.md) with a high
observed cache-hit rate. The setup wizard also supports other API-backed
profiles.

## Use Praxist Through Codex

We recommend Codex as the interface for operating Praxist. Praxist is not a
replacement for Codex: Codex remains the interactive agent that understands
your project, communicates with you, and uses development tools. Praxist adds
the persistent research loop, parallel peers, evidence protocols, scheduling,
and lifecycle control.

After installation, open Codex in the root of an already runnable research
project and invoke `$praxist-takeover`. The takeover skill inspects readiness,
creates or repairs the task harness, validates its evaluator and evidence
contract, and launches the run after the required gates pass. A precise brief
produces a better research plan; include the objective, metrics, constraints,
resources, exploration choices, and whether launch is authorized.

<details>
<summary>Example takeover brief</summary>

```text
$praxist-takeover

Treat the current directory as the existing runnable research project. Verify
the baseline and its evaluation path before changing anything.

Optimize <primary metric and direction> while preserving <key constraints>.
Use <peer count> peers for up to <generation count> generations within
<time or cost budget>. Use the runtime and model provider selected during
setup. <Allow or disable> literature search, <enable or disable> QD, and
<enable or disable> generation-zero DIG.

Do not download new datasets or replace required project assets. Build a
separate task harness with explicit metric directions, baseline provenance,
protocol-integrity checks, evidence maturity rules, and justified retention
lanes. After readiness checks pass, <launch immediately in detached mode / ask
for confirmation>. Report the task path, run ID, evidence contract, generation
close policy, and monitor command.
```

</details>

Other bundled skills:

| Skill | Purpose |
|---|---|
| `praxist-takeover-codex` | No-key takeover using the saved Codex login |
| `praxist-onboarding` | Explain Praxist and inspect local readiness |
| `praxist-task-initialization` | Build or repair a task harness without launching |
| `praxist-interactive-task-init` | Design a task through confirmation-first setup |
| `praxist-control` | Start, stop, resume, monitor, and inspect runs |
| `praxist-diagnostic` | Diagnose run health and produce reports |
| `praxist-scientific-research` | Gather so