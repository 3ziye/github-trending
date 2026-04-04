# 🦞 NVIDIA NemoClaw: Reference Stack for Running OpenClaw in OpenShell

<!-- start-badges -->
[![License](https://img.shields.io/badge/License-Apache_2.0-blue)](https://github.com/NVIDIA/NemoClaw/blob/main/LICENSE)
[![Security Policy](https://img.shields.io/badge/Security-Report%20a%20Vulnerability-red)](https://github.com/NVIDIA/NemoClaw/blob/main/SECURITY.md)
[![Project Status](https://img.shields.io/badge/status-alpha-orange)](https://github.com/NVIDIA/NemoClaw/blob/main/docs/about/release-notes.md)
[![Discord](https://img.shields.io/badge/Discord-Join-7289da)](https://discord.gg/XFpfPv9Uvx)
<!-- end-badges -->

<!-- start-intro -->
NVIDIA NemoClaw is an open source reference stack that simplifies running [OpenClaw](https://openclaw.ai) always-on assistants more safely.
It installs the [NVIDIA OpenShell](https://github.com/NVIDIA/OpenShell) runtime, part of NVIDIA Agent Toolkit, which provides additional security for running autonomous agents.
<!-- end-intro -->

> **Alpha software**
>
> NemoClaw is available in early preview starting March 16, 2026.
> This software is not production-ready.
> Interfaces, APIs, and behavior may change without notice as we iterate on the design.
> The project is shared to gather feedback and enable early experimentation.
> We welcome issues and discussion from the community while the project evolves.

NemoClaw adds guided onboarding, a hardened blueprint, state management, messaging bridges, routed inference, and layered protection on top of the [NVIDIA OpenShell](https://github.com/NVIDIA/OpenShell) runtime. For the full feature list, refer to [Overview](https://docs.nvidia.com/nemoclaw/latest/about/overview.html). For the system diagram, component model, and blueprint lifecycle, refer to [How It Works](https://docs.nvidia.com/nemoclaw/latest/about/how-it-works.html) and [Architecture](https://docs.nvidia.com/nemoclaw/latest/reference/architecture.html).

## Getting Started

Follow these steps to install NemoClaw and run your first sandboxed OpenClaw agent.

<!-- start-quickstart-guide -->

### Prerequisites

Before getting started, check the prerequisites to ensure you have the necessary software and hardware to run NemoClaw.

#### Hardware

| Resource | Minimum        | Recommended      |
|----------|----------------|------------------|
| CPU      | 4 vCPU         | 4+ vCPU          |
| RAM      | 8 GB           | 16 GB            |
| Disk     | 20 GB free     | 40 GB free       |

The sandbox image is approximately 2.4 GB compressed. During image push, the Docker daemon, k3s, and the OpenShell gateway run alongside the export pipeline, which buffers decompressed layers in memory. On machines with less than 8 GB of RAM, this combined usage can trigger the OOM killer. If you cannot add memory, configuring at least 8 GB of swap can work around the issue at the cost of slower performance.

#### Software

| Dependency | Version                          |
|------------|----------------------------------|
| Linux      | Ubuntu 22.04 LTS or later |
| Node.js    | 22.16 or later |
| npm        | 10 or later |
| Container runtime | Supported runtime installed and running |
| [OpenShell](https://github.com/NVIDIA/OpenShell) | Installed |

#### Container Runtimes

| Platform | Supported runtimes | Notes |
|----------|--------------------|-------|
| Linux | Docker | Primary supported path. |
| macOS (Apple Silicon) | Colima, Docker Desktop | Install Xcode Command Line Tools (`xcode-select --install`) and start the runtime before running the installer. |
| macOS (Intel) | Podman | Not supported yet. Depends on OpenShell support for Podman on macOS. |
| Windows WSL | Docker Desktop (WSL backend) | Supported target path. |
| DGX Spark | Docker | Refer to the [DGX Spark setup guide](https://github.com/NVIDIA/NemoClaw/blob/main/spark-install.md) for cgroup v2 and Docker configuration. |

### Install NemoClaw and Onboard OpenClaw Agent

Download and run the installer script.
The script installs Node.js if it is not already present, then runs the guided onboard wizard to create a sandbox, configure inference, and apply security policies.

> **ℹ️ Note**
>
> NemoClaw creates a fresh OpenClaw instance inside the sandbox during the onboarding process.

```bash
curl -fsSL https://www.nvidia.com/nemoclaw.sh | bash
```

If you use nvm or fnm to manage Node.js, the installer may not update your current shell's PATH.
If `nemoclaw` is not found after install, run `source ~/.bashrc` (or `source ~/.zshrc` for zsh) or open a new terminal.

When the install completes, a summary confirms the running environment:

```text
──────────────────────────────────────────────────
Sandbox      my-assistant (Landlock + seccomp + netns)
Model        nvidia/nemotron-3-super-120b-a12b (NVIDIA Endpoints)
──────────────────────────────────────────────────
Run:         nemoclaw my-assistant connect
Status:      nemoclaw my-assistant status
Logs:        nemoclaw my-assistant logs --follow
────────────────────────────────