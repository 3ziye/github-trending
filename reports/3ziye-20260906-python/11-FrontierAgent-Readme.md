<div align="center">
  <picture>
    <img src="./assets/apodex_logo.jpeg" width="30%" alt="Apodex">
  </picture>
</div>
<hr>
<br>

<div align="center">
  <a href="https://www.apodex.ai"><img alt="Online Service" src="https://img.shields.io/badge/🤖%20Online_Service-Apodex_1.1-1783ff"/></a>
  <a href="https://www.apodex.com/"><img alt="Homepage" src="https://img.shields.io/badge/Homepage-Apodex_AI-white"/></a>
  <a href="https://platform.apodex.ai"><img alt="Try Apodex API" src="https://img.shields.io/badge/Try_Apodex_1.1-API_Platform-1783ff"/></a>
  <br>
  <a href="https://huggingface.co/collections/apodex"><img alt="Hugging Face" src="https://img.shields.io/badge/🤗%20Hugging_Face-Apodex_AI-ffc107"/></a>
  <a href="https://discord.gg/TDJA59TCng"><img alt="Discord" src="https://img.shields.io/badge/Discord-Apodex_AI-5865F2"/></a>
  <a href="https://x.com/Apodex_AI"><img alt="X" src="https://img.shields.io/badge/X-@Apodex__AI-000000?logo=x&logoColor=white"/></a>
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/License-Apache_2.0-blue"/></a>
</div>
<br>
<p align="center">
  <b><a href="https://www.apodex.com/blog/apodex-1.1-scaling-agentic-intelligence-for-complex-work">Tech Blog</a></b> ·
  <b><a href="https://arxiv.org/abs/2608.23283">Tech Report</a></b>
</p>

# FrontierAgent

FrontierAgent is an open-source agent runtime, terminal product, and evaluation
suite for long-horizon research and file-based work. The `frontier-agent` TUI
ships two native workflows:

- **ReAct** — one stateful agent researches, reads files, writes deliverables,
  runs commands, and iterates in a task-scoped sandbox.
- **Agent Team** — a coordinator maintains a task board, delegates independent
  work to parallel sub-agents, collects their reports, and synthesizes the result.

The same workflow engine powers the benchmark runner used to evaluate Apodex
models. The framework, tools, workflows, and evaluation layer remain separate,
so each can be reused independently.

> [!IMPORTANT]
> ### 🚀 Try FrontierAgent on the Apodex API — free for the next two weeks!
>
> **No model hosting required.** Get an API key, connect to the OpenAI-compatible
> Apodex-1.1 endpoint, and start running FrontierAgent in minutes.
>
> **[→ Start building for free at platform.apodex.ai](https://platform.apodex.ai/)**
>
> ⏳ This is a limited-time offer—come try it and let us know what you build!

New here? Use the **[documentation index](docs/README.md)** to find the right
installation, SGLang, workflow, evaluation, or developer guide.

<p align="center">
  <img src="./assets/apodex1.1_bench.png" alt="Apodex-1.1 benchmark results across professional work, finance, scientific research, and general reasoning tasks" width="900"/>
</p>

## Highlights

- **Native Agent Team workflow.** The coordinator decomposes the request,
  dispatches bounded parallel assignments, receives structured reports, and can
  use an optional fast reporter for final evidence review.
- **Task Board.** Agent Team's `add_task` and `update_task` events appear live in
  the TUI sidebar with pending, active, completed, blocked, and cancelled state.
- **Sandboxed file work.** Shell and file tools share one task-scoped filesystem:
  `/inputs` is read-only, `/workspace` is working state, and `/outputs` contains
  persistent deliverables. Authorization and sandbox failures are fail-closed.
- **Asynchronous intervention.** Type while an agent is running to queue a new
  instruction. It is injected at the next safe turn boundary without discarding
  the active run. In Agent Team mode it steers the coordinator; already-running
  sub-agents are allowed to finish.
- **Transparent deliverables.** On macOS/Docker, `/outputs` maps to
  `.apodex/runs/<session-id>/outputs` on the host. The same run directory also
  contains its checkpoint, trace, engine log, and trajectories.
- **Approval, trace, and recovery.** Mutating operations show a diff and require
  approval unless `--yes` is enabled. Sessions are checkpointed, every action is
  traced locally, `/revert` restores session changes, and `--resume` continues a
  saved run.
- **Evaluation included.** The subprocess runner supports research and
  file-grounded benchmarks, deterministic artifact collection, concurrency,
  progress inspection, and rerunning individual failures.

<p align="center">
  <img src="./assets/agent_team.png" alt="Conceptual Agent Team workflow: a main agent assigns work to expert sub-agents, collects asynchronous reports, requests verification when needed, and synthesizes the final report" width="900"/>
</p>

<p align="center"><em>Conceptual Agent Team workflow, from task delegation and asynchronous report collection to verification and final synthesis.</em></p>

## How it fits together

```mermaid
flowchart LR
    U["User / benchmark task"] --> TUI["TUI or subprocess runner"]
    TUI --> R["Stateful ReAct"]
    TUI --> C["Agent Team coordinator"]
    C --> B["Task board"]
    B --> S1["Sub-agent 1"]
    B -->