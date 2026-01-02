# BoxLite

[![Build](https://github.com/boxlite-labs/boxlite/actions/workflows/build-wheels.yml/badge.svg)](https://github.com/boxlite-labs/boxlite/actions/workflows/build-wheels.yml)
[![Lint](https://github.com/boxlite-labs/boxlite/actions/workflows/lint.yml/badge.svg)](https://github.com/boxlite-labs/boxlite/actions/workflows/lint.yml)
[![PyPI](https://img.shields.io/pypi/v/boxlite.svg)](https://pypi.org/project/boxlite/)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Overview

BoxLite is an embeddable virtual machine runtime for secure, isolated execution environments.
Following the SQLite philosophy of "small, fast, reliable", BoxLite lets you run containers inside
lightweight VMs with hardware-level isolation—no daemon required.

### The Problem

AI agents are most powerful when they have freedom—freedom to write code, install packages, modify
files, access the network, and explore solutions creatively. But that freedom on your host system is
dangerous. And if you're hosting AI agents for customers, you need isolation that scales—without
managing VM infrastructure.

Today's options force you to choose:

| Approach              | Trade-off                                      |
|-----------------------|------------------------------------------------|
| **Restrict the AI**   | Safer, but cripples capability                 |
| **Trust the AI**      | Full power, but one mistake away from disaster |
| **Docker containers** | Partial isolation—shares host kernel           |
| **Traditional VMs**   | Heavy, slow, complex to orchestrate            |
| **Cloud sandboxes**   | Latency, cost, vendor lock-in                  |

### BoxLite's Approach

BoxLite gives AI agents a **complete playground**—a full Linux environment where they can do
*anything*—while guaranteeing nothing escapes to your host. It combines the **security of VMs** with
the **simplicity of containers**:

- **Full Freedom Inside** — Install packages, write files, run servers, use the network
- **Hardware Isolation** — Each Box is a separate VM with its own kernel, not just namespaces
- **Batteries Included** — VM, networking, OCI images, storage—all integrated, nothing to configure
- **Embeddable** — No daemon, no root, just a library in your application
- **OCI Compatible** — Use any Docker/OCI image (`python:slim`, `node:alpine`, etc.)
- **Cross-Platform** — macOS (Apple Silicon) and Linux (x86_64, ARM64)

**The AI explores freely. Your system stays safe.**

### Architecture

```
┌─────────────────────────────────────────────────────────────┐
│  Your Application                                           │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  BoxLite Runtime (embedded library)                  │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐   │   │
│  │  │   Box A     │  │   Box B     │  │   Box C     │   │   │
│  │  │  (micro-VM) │  │  (micro-VM) │  │  (micro-VM) │   │   │
│  │  │ ┌─────────┐ │  │ ┌─────────┐ │  │ ┌─────────┐ │   │   │
│  │  │ │Container│ │  │ │Container│ │  │ │Container│ │   │   │
│  │  │ └─────────┘ │  │ └─────────┘ │  │ └─────────┘ │   │   │
│  │  └─────────────┘  └─────────────┘  └─────────────┘   │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                              │
                    Hardware Virtualization
                      (KVM / Hypervisor.framework)
```

### Use Cases

- **AI Agent Sandbox** — A full computer for your AI to explore, experiment, and build—safely
  isolated from your system
- **AI Agent Hosting** — Serverless multi-tenant runtime—spin up isolated environments on demand for
  each customer's AI
- **Regulated Environments** — Hardware-level isolation for compliance where container breakout is
  unacceptable
- **Local Development** — Consistent Linux environments on macOS and Linux—no Docker Desktop
  required

## Features

### Compute

- **Resource Control** — Configure CPUs, memory limits per box
- **Environment Control** — Custom env vars, working directory
- **Async-First API** — Non-blocking operations, run multiple boxes concurrently
- **Streaming I/O** — Real-time stdout/stderr as execution happens
- **Metrics** — CPU, memory, execution statistics per box

### Storage

- **Volume Mounts** — Mount host directories into the box (read-only or read-write)
- **Persistent Disks** — QCOW2 disk images that survive box restarts
- **Copy-on-Write** — Efficient snapshots with shared base images

### Networking

- **Full Internet Access** — Outbound connections, DNS resolution
- **Port Forwarding** — Map host ports to guest ports (TCP/UDP)
- **Network Metrics** — Bytes sent/received, connection stats

### Images

- **OCI Compatible** — Pull from Docker Hub, GHCR, ECR, or any registry
- **Layer Caching** — Pull once, start fast
- **Custom Rootfs** — Use pre-built rootfs instead of pulling im