# Agent Substrate

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

NOTE: This is not an officially supported Google product. This project is not
eligible for the [Google Open Source Software Vulnerability Rewards Program](https://bughunters.google.com/open-source-security).

## What is Agent Substrate?

Agent substrate is a system built on top of Kubernetes which manages agent-like
workloads to achieve higher scale and efficiency than Kubernetes alone can
offer, with lower latency.  It builds on top of Kubernetes features like
Pods and Pod autoscaling, but takes the Kubernetes control-plane out of the
critical path to achieve lower latency.

It can run on any Kubernetes cluster and does not inhibit “regular” use of
Kubernetes in any way. Kubernetes provides the infrastructure provisioning and
management for all types of workloads, while Agent Substrate provides
agent-specific scheduling and control.

At its core, Agent Substrate maps a larger set of “actors” (applications such
as agents) onto a smaller set of ready “workers” (Kubernetes Pods), relying on
the fact that agent-like applications tend to be idle most of the time to
achieve heavy multiplexing.  It provides functionality to manage an actor’s
lifecycle (e.g. create/destroy, suspend/resume), to assign actors to workers in real
time, and to route incoming traffic to them.

Agent Substrate is intended to be a low-opinion system.  The workloads it
manages don't have to be literal AI agents, but those are the best example of
the kind of applications it is designed for.  It is not an SDK for building
agents, but rather a system for running them at scale.

## Demo

[![Agent Substrate Demo](https://img.youtube.com/vi/ZEzkCFJkzjY/hq1.jpg)](https://www.youtube.com/watch?v=ZEzkCFJkzjY)

*Watch the Agent Substrate cluster multiplex ~250 stateful actor sessions across just 8 physical pods.*

This demo highlights the core developer experience and "Agentic Infrastructure" capabilities of Substrate:

1.  **Instant Session Teleport:** High-performance suspend and resume of actors onto any available worker in the pool with sub-second activation.
2.  **State Persistence:** Persistent working memory (volatile RAM) and filesystem state preserved perfectly across hibernation cycles via full-state snapshots.
3.  **Agent Swarm Multiplexing:** Demonstrates 30x+ oversubscription by "juggling" a large registry of stateful actors onto a small pool of shared physical pods.

To reproduce this demo in your own cluster, please refer to the detailed walkthroughs in the **[Counter Demo](demos/counter/README.md)** and **[Secret Agent Demo](demos/agent-secret/README.md)**.

For more videos and walkthroughs, visit our YouTube channel: **[agent-substrate](https://www.youtube.com/channel/UCN9PPqlTtVxlcpbQ-NWpfZQ)**.

## Framework Agnostic & Compatibility

Agent Substrate is designed to be **framework and agent harness agnostic**. Because it manages standard OCI containers at the kernel level (via gVisor), it can host agents built on any stack.

*   **Agent Development Kit (ADK):** Native support for ADK-compatible session identity and persistent working memory.
*   **LangChain:** Ideal execution environment for long-running, stateful LangChain agents and sandboxed tool-calling.
*   **Claude Code & CodeX:** Support for high-density, stateful coding environments that preserve terminal and filesystem state across sessions.
*   **Model Context Protocol (MCP):** Deploy secure, sandboxed MCP servers as Substrate Actors to provide durable tools for any LLM.

## Ecosystem & Examples

*   **[Agent Executor](https://github.com/google/ax):** A distributed agent runtime that demonstrates building a secure, hyper-scalable agent harness on Agent Substrate (see the [announcement blog](https://cloud.google.com/blog/products/ai-machine-learning/agent-executor-googles-distributed-agent-runtime) and [integration guide](https://github.com/google/ax/blob/main/manifests/README.md)).

## Status and compatibility

Agent Substrate is currently in VERY early development.  It is not ready for
production use, and the APIs are almost guaranteed to change.  We are not
making any guarantees about backward compatibility at this stage, and
everything in this project may be changed.

### Supported Kubernetes Releases

Currently we aim to support the [latest stable release](https://kubernetes.io/releases/) of Kubernetes, and the previous minor release.

## Community

For announcements, technical discussions, and community support, please join
the **[ate-dev](https://groups.google.com/g/ate-dev)** Google Group.

We also have channels in the CNCF slack; [request an invite here](https://slack.cncf.io/)
if you don't have access.

- [#substrate-users](https://cloud-native.slack.com/archives/C0B6RCAJULW) to discuss using substrate.
- [#substrate-dev](https://cloud-native.slack.com/archives/C0B6M3E2J3D) to discuss developing substrate.

## Developing

Please se