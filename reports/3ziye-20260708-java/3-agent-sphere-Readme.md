<p align="center">
  <img src="https://img.shields.io/badge/Java-21-%23ED8B00?logo=openjdk&logoColor=white" alt="Java 21"/>
  <img src="https://img.shields.io/badge/Spring%20Boot-3.4.3-%236DB33F?logo=springboot&logoColor=white" alt="Spring Boot 3.4.3"/>
  <img src="https://img.shields.io/badge/React-19-%2361DAFB?logo=react&logoColor=black" alt="React 19"/>
  <img src="https://img.shields.io/badge/UmiJS-4.6-%239F46FF" alt="UmiJS 4.6"/>
  <img src="https://img.shields.io/badge/Ant%20Design-6-%230170FE?logo=antdesign&logoColor=white" alt="Ant Design 6"/>
  <img src="https://img.shields.io/badge/PostgreSQL-14-%23336791?logo=postgresql&logoColor=white" alt="PostgreSQL 14"/>
  <img src="https://img.shields.io/badge/Redis-7-%23FF4438?logo=redis&logoColor=white" alt="Redis 7"/>
  <img src="https://img.shields.io/badge/TypeScript-6-%233178C6?logo=typescript&logoColor=white" alt="TypeScript 6"/>
  <img src="https://img.shields.io/badge/MyBatis--Plus-3.5.9-%23D32F2F" alt="MyBatis-Plus 3.5.9"/>
  <img src="https://img.shields.io/badge/License-MIT-%23FF9900" alt="MIT"/>
</p>

<p align="center"><b><a href="http://as.buukle.top" target="_blank">🔗 线上预览 / Live Demo → as.buukle.top</a></b></p>

This project is an AI Agent orchestration platform. Driven by an LLM-based decision engine and combined with capabilities (built-in tools, MCP protocol, CLI execution, browser automation, etc.), it implements a primary closed loop of **Perception → Planning → Execution → Feedback**.

It supports configuring different model providers: OpenAI, DeepSeek, QuickRouter (relay station), BigModel (Zhipu AI), LiteLLM.
---

Screenshots

![ui-register.png](agent-sphere-readme/ui-register.png)

![ui-chat.png](agent-sphere-readme/ui-chat.png)

![ui-chat-toolcalls.png](agent-sphere-readme/ui-chat-toolcalls.png)

![ui-artifact-document.png](agent-sphere-readme/ui-artifact-document.png)

▶ [Click to watch the video demo](https://www.bilibili.com/video/BV1WqTT62Efq/)

[![Video preview](agent-sphere-readme/ui-preview.gif)](https://www.bilibili.com/video/BV1WqTT62Efq/)

## 1. Quick Start for Development

See: [QUICK_START.md](QUICK_START.md)

## 2. Architecture

### 2.1 Overall Structure

![agentsphere-architecture.png](agent-sphere-readme/agentsphere-architecture.png)

### 2.2 Core Components

#### 2.2.1 SessionRunner (ReAct Engine)

Manages the complete execution lifecycle of an AI session, implementing the **Plan → Act → Observe → Learn** loop:

![SessionRunner.run execution lifecycle](agent-sphere-readme/session-runner-flow.png)

**Alignment with the ReAct pattern:**

![ReAct pattern alignment](agent-sphere-readme/react-mode.png)

#### 2.2.2 Capability Layer

| Capability Type | Implementation | Description | Examples |
|-----------------|----------------|-------------|----------|
| **MCP (Model Context Protocol)** | MCP Server client | Standard protocol, connects to any MCP Server | Jira, GitHub, Slack, databases |
| **Builtin (built-in tools)** | SPI: `CapabilityBuiltinToolSpi` | Java SPI extension | WebFetch, WebRead, Chrome, Todowrite, DocWrite |
| **Chrome Browser** | Chrome Extension bridge | DOM operations + real-time visual feedback | Navigate, click, fill forms, screenshot |
| **CLI (command line)** | `ProcessBuilder` execution | Local or remote shell | Git operations, build/deploy, system administration |
| **Skill (composite skills)** | Multi-step task orchestration | LLM-driven task decomposition | Cross-system workflows |

#### 2.2.3 Chrome Extension (Browser Bridge)

![Chrome Extension browser bridge structure](agent-sphere-readme/chrome-extension-structure.png)

---

## 3. Algorithm — Core Algorithms

### 3.1 ReAct Execution Loop

The core loop of AgentSphere follows the **ReAct (Reasoning + Acting)** pattern, combining the LLM's reasoning ability with tool execution ability:

![ReAct execution loop](agent-sphere-readme/react-loop.png)

**Message structure:**

```
[
  {role: "system",    content: "You are a browser assistant..."},
  {role: "user",      content: "Help me check the weather in Guangzhou"},
  {role: "assistant", tool_calls: [{id: "call_1", name: "navigate", args: "..."}}]},
  {role: "tool",      tool_call_id: "call_1", content: '{"tabId": 42, "url": "..."}'},
  {role: "assistant", content: "The weather in Guangzhou tomorrow is..."},
  {role: "user",      content: "What should I prepare for going out tomorrow"},
  ...
]
```

**Multi-turn tool call example:**

![Multi-turn tool call example](agent-sphere-readme/multi-loop-sequence.png)

### 3.2 Multi-level Memory System

AgentSphere implements a multi-level memory system covering the full chain from persistence to runtime caching:

![Multi-level Memory System](agent-sphere-readme/memory-system.png)

#### Memory Level Details

| Level | Storage | Lifecycle | Capacity | Purpose |
|-------|---------|-----------|----------|---------|
| L1: KernelContext | ConcurrentHashMap | During run (TTL 30min) | 1 per session | Tool list, model route |
| L2: Messages | ArrayList | During ru