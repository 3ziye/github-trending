<p align="center">
  <img src="https://cordum.io/_next/image?url=%2Flogo.png&w=1200&q=75" alt="Cordum" width="200"/>
</p>

<h1 align="center">Cordum</h1>

<p align="center">
  <strong>AI Agent Governance Platform</strong><br/>
  Deploy autonomous agents with built-in safety, observability, and control.
</p>

<p align="center">
  <a href="https://github.com/cordum-io/cordum/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-BUSL--1.1-blue" alt="License"/></a>
  <a href="https://github.com/cordum-io/cordum/releases"><img src="https://img.shields.io/github/v/release/cordum-io/cordum?sort=semver" alt="Release"/></a>
  <a href="https://discord.gg/cordum"><img src="https://img.shields.io/discord/YOUR_DISCORD_ID?label=discord&logo=discord" alt="Discord"/></a>
  <a href="https://github.com/cordum-io/cap"><img src="https://img.shields.io/badge/protocol-CAP%20v2-green" alt="CAP Protocol"/></a>
</p>

---

## The Problem

AI agents are powerful. They're also unpredictable.

Teams deploying agents in production face the **Trust Gap**: the distance between what an agent *can* do and what you're *confident* letting it do unsupervised.

Without governance, you're flying blind:
- No visibility into what agents are doing
- No safety rails before dangerous actions
- No audit trail when things go wrong
- No way to require human approval for sensitive operations

## The Solution

Cordum is a **control plane for AI agents** that closes the Trust Gap.

![Cordum control plane](./Screenshot%202026-01-23%20162612.png)

```
┌─────────────────────────────────────────────────────────────────┐
│                         Cordum                                  │
│                                                                 │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────────┐ │
│  │   API    │──▶│ Scheduler│──▶│  Safety  │──▶│ Worker Pools │ │
│  │ Gateway  │   │          │   │  Kernel  │   │              │ │
│  └──────────┘   └──────────┘   └──────────┘   └──────────────┘ │
│       │              │              │                │         │
│       ▼              ▼              ▼                ▼         │
│  [Dashboard]    [Workflows]    [Policies]      [Your Agents]   │
└─────────────────────────────────────────────────────────────────┘
```

**What Cordum does:**

- **Safety Kernel** — Policy checks (allow/deny/throttle/human-approve) before any job runs
- **Workflow Engine** — Orchestrate multi-step agent workflows with retries, approvals, and timeouts
- **Job Routing** — Distribute work across agent pools with capability-based routing
- **Observability** — Full audit trail, traces, and real-time dashboard
- **Human-in-the-Loop** — Require approval for sensitive operations

## Quickstart

**Prerequisites:** Docker, Docker Compose

```bash
# Clone the repo
git clone https://github.com/cordum-io/cordum.git
cd cordum

# Start everything
docker compose up -d

# Open dashboard
open http://localhost:8082
```

**Run the smoke test:**

```bash
./tools/scripts/platform_smoke.sh
```

That's it. You have a running Cordum instance with API, scheduler, safety kernel, and dashboard.

## How It Works

Cordum uses [CAP (Cordum Agent Protocol)](https://github.com/cordum-io/cap) for all agent communication:

1. **Submit** — Client submits a job via API
2. **Safety Check** — Scheduler asks Safety Kernel: allow, deny, throttle, or require approval?
3. **Dispatch** — Approved jobs route to the right worker pool via NATS
4. **Execute** — Your agent runs the job (using MCP, LangChain, whatever)
5. **Result** — Agent returns result; Cordum updates state and notifies client

```
Client ──▶ API ──▶ Scheduler ──▶ Safety Kernel ──▶ NATS ──▶ Agent Pool
                       │                              │
                       ▼                              ▼
                  [Redis State]                 [Your Agents]
```

**Key design choices:**
- **Payloads stay off the bus** — `context_ptr` and `result_ptr` reference Redis/S3, keeping the message bus lean
- **Protocol-first** — CAP is an independent spec; Cordum is the reference implementation
- **Workers are external** — Cordum is the control plane; your agents run wherever you want

## Key Features

| Feature | Description |
|---------|-------------|
| **Safety Policies** | Define rules for what agents can/can't do. Enforce before execution. |
| **Human Approval** | Flag sensitive jobs for manual review before they run. |
| **Workflows** | Multi-step DAGs with fan-out, retries, delays, and conditions. |
| **Pool Routing** | Route jobs by capability, region, or custom tags. |
| **Heartbeats** | Know which agents are alive, their capacity, and load. |
| **Audit Trail** | Every job, decision, and result logged and queryable. |
| **Dashboard** | Real-time UI for workflows, jobs, approvals, and policies. |
| **Multi-tenant** | API keys with RBAC for teams and environments. |

## Architecture

```
cordum/
├── cmd/                          # Service entrypoints + CLI
│   ├── cord