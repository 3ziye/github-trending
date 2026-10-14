<p align="center">
  <img
    src="https://img.alicdn.com/imgextra/i1/O1CN01nTg6w21NqT5qFKH1u_!!6000000001621-55-tps-550-550.svg"
    alt="AgentScope Logo"
    width="200"
  />
</p>

<span align="center">

[**中文主页**](https://github.com/agentscope-ai/agentscope-java/blob/main/README_zh.md) | [**Documentation**](https://java.agentscope.io/)

</span>

<p align="center">
    <a href="https://discord.gg/eYMpfnkG8h">
        <img
            src="https://img.shields.io/badge/Discord-Join%20Us-5865F2?logo=discord&logoColor=white"
            alt="discord"
        />
    </a>
    <a href="https://java.agentscope.io/">
        <img
            src="https://img.shields.io/badge/Docs-English%7C%E4%B8%AD%E6%96%87-blue?logo=markdown"
            alt="docs"
        />
    </a>
    <a href="https://img.shields.io/maven-central/v/io.agentscope/agentscope">
        <img
            src="https://img.shields.io/maven-central/v/io.agentscope/agentscope?color=green"
            alt="Maven Central"
        />
    </a>
    <a href="#">
        <img
            src="https://img.shields.io/badge/JDK-17%2B-orange?logo=openjdk"
            alt="JDK 17+"
        />
    </a>
    <a href="./LICENSE">
        <img
            src="https://img.shields.io/badge/license-Apache--2.0-black"
            alt="license"
        />
    </a>
    <a href="https://deepwiki.com/agentscope-ai/agentscope-java">
        <img
            src="https://deepwiki.com/badge.svg"
            alt="Ask DeepWiki"
        />
    </a>
</p>

## What is AgentScope Java 2.0?

AgentScope Java 2.0 is a production-ready framework for building distributed, enterprise-grade agents, providing essential abstractions that work with rising model capability and built-in support for long-running, safely-controlled agent execution.

- [**Event System** →](https://java.agentscope.io/v2/en/docs/building-blocks/message-and-event.html) A unified event stream with 31 typed events for real-time frontend rendering and human-in-the-loop.
- [**Permission System** →](https://java.agentscope.io/v2/en/docs/building-blocks/permission-system.html) Tool-call gating: allow / require user approval / deny.
- [**Middleware** →](https://java.agentscope.io/v2/en/docs/building-blocks/middleware.html) AOP-style hook interception for flexibly extending the reasoning-acting loop.
- [**Workspace & Sandbox** →](https://java.agentscope.io/v2/en/docs/harness/workspace.html) Run tools in isolated environments — local, Docker, Kubernetes, or AgentRun cloud sandbox.
- [**Multi-Agent Orchestration** →](https://java.agentscope.io/v2/en/docs/harness/subagent.html) Multiple subagent definition patterns with `agent_spawn` / `agent_send` and real-time event forwarding.
- [**Distributed Deployment** →](https://java.agentscope.io/v2/en/docs/others/going-to-production.html) True distributed session and memory management (Redis / MySQL / PostgreSQL / OSS / COS) with cross-replica session recovery.
- [**Agent Evolution** →](https://help.aliyun.com/zh/document_detail/3042583.html) Provides Agent observability and auditing, Agent evaluation and experimentation, and Agent asset management and continuous optimization.

<img src="./docs/imgs/landscape.png" alt="agentscope" width="100%"/>

## News
<!-- BEGIN NEWS -->
- **[2026-08] [AgentScope Service](./agentscope-service):** An agent Control Plane and Dashboard for agent observation, registration and orchestration, designed to be compatible with AgentScope, LangChain, ADK, and Claude / Qoder, etc.
- **[2026-07] `v2.0.0 GA`:** First production-ready release! Dual-layer agent architecture, event stream, permission system, middleware, workspace sandbox, multi-agent orchestration, and distributed deployment all ready. [Docs](https://java.agentscope.io/) | [Release Notes](https://github.com/agentscope-ai/agentscope-java/releases/tag/v2.0.0)
- **[2026-07] `v2.0.0-RC5`:** Model provider modularization; unified DataBlock multimodal support; native structured output; Channel IM integration; Tencent Cloud COS state persistence. [Release Notes](https://github.com/agentscope-ai/agentscope-java/releases/tag/v2.0.0-RC5)
- **[2026-06] `v2.0.0-RC4`:** Async tool execution and scheduled wakeup dispatching; subagent cross-replica routing and session recovery. [Release Notes](https://github.com/agentscope-ai/agentscope-java/releases/tag/v2.0.0-RC4)
- **[2026-06] `v2.0.0-RC3`:** Unified `call()` / `streamEvents()` execution core; `AgentResultEvent`, `CustomEvent`, `HintBlockEvent` new event types. [Release Notes](https://github.com/agentscope-ai/agentscope-java/releases/tag/v2.0.0-RC3)
- **[2026-06] `v2.0.0-RC2`:** Fully stateless agent; one-line DistributedBackend; subagent event forwarding; Channel module (DingTalk, Feishu, WeCom); A2A / AG-UI protocol support. [Release Notes](https://github.com/agentscope-ai/agentscope-java/releases/tag/v2.0.0-RC2)
- **[2026-05] `v2.0.0-RC1`:** First 2.0 RC — harness engineering, enterprise distributed deployment, event stream / message model / middleware / HIT