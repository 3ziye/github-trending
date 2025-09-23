# Shannon — Production AI Agents That Actually Work

<div align="center">

![Shannon Dashboard](docs/images/dashboard-demo.gif)

*Real-time observability dashboard showing agent traffic control, metrics, and event streams*

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│     Real-time metrics, event tracking, and system health monitoring.         │
│     Access at http://localhost:3000 after running 'make dev'                 │
│                                                                              │
│     Please ⭐ star this repo to show your support and stay updated!          │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

</div>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Go Version](https://img.shields.io/badge/Go-1.24%2B-blue.svg)](https://golang.org/)
[![Rust](https://img.shields.io/badge/Rust-stable-orange.svg)](https://www.rust-lang.org/)
[![Docker](https://img.shields.io/badge/Docker-required-blue.svg)](https://www.docker.com/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Stop burning money on AI tokens. Ship reliable agents that won't break in production.**

Shannon is battle-tested infrastructure for AI agents that solves the problems you'll hit at scale: runaway costs, non-deterministic failures, and security nightmares. Built on Temporal workflows and WASI sandboxing, it's the platform we wished existed when our LLM bills hit $50k/month.

## 🔥 The Problems We Solve

- **"Our AI costs are out of control"** → 70% token reduction via intelligent caching
- **"We can't debug production issues"** → Deterministic replay of any workflow
- **"Agents keep breaking randomly"** → Time-travel debugging with full state history
- **"We're worried about prompt injection"** → WASI sandbox + OPA policies for bulletproof security
- **"Different teams need different models"** → Hot-swap between 15+ LLM providers
- **"We need audit trails for compliance"** → Every decision logged and traceable

## ⚡ What Makes Shannon Different

### 🚀 Ship Faster
- **Zero Configuration Multi-Agent** - Just describe what you want: "Analyze data, then create report" → Shannon handles dependencies automatically
- **Multiple AI Patterns** - ReAct, Tree-of-Thoughts, Chain-of-Thought, Debate, and Reflection (configurable via `cognitive_strategy`)
- **Time-Travel Debugging** - Export and replay any workflow to reproduce exact agent behavior
- **Hot Configuration** - Change models, prompts, and policies without restarts

### 🔒 Production Ready
- **WASI Sandbox** - Full Python 3.11 support with bulletproof security ([→ Guide](docs/python-code-execution.md))
- **Token Budget Control** - Hard limits per user/session with real-time tracking
- **Policy Engine (OPA)** - Define who can use which tools, models, and data
- **Multi-Tenancy** - Complete isolation between users, sessions, and organizations

### 📈 Scale Without Breaking
- **70% Cost Reduction** - Smart caching, session management, and token optimization
- **Provider Agnostic** - OpenAI, Anthropic, Google, Azure, Bedrock, DeepSeek, Groq, and more
- **Observable by Default** - Real-time dashboard, Prometheus metrics, OpenTelemetry tracing
- **Distributed by Design** - Horizontal scaling with Temporal workflow orchestration

*Model pricing is centralized in `config/models.yaml` - all services load from this single source for consistent cost tracking.*

## 🎯 Why Shannon vs. Others?

| Challenge | Shannon | LangGraph | AutoGen | CrewAI |
|---------|---------|-----------|---------|---------|
| **Multi-Agent Orchestration** | ✅ DAG/Graph workflows | ✅ Stateful graphs | ✅ Group chat | ✅ Crew/roles |
| **Agent Communication** | ✅ Message passing | ✅ Tool calling | ✅ Conversations | ✅ Delegation |
| **Memory & Context** | ✅ Long/short-term, vector | ✅ Multiple types | ✅ Conversation history | ✅ Shared memory |
| **Debugging Production Issues** | ✅ Replay any workflow | ❌ Limited debugging | ❌ Basic logging | ❌ |
| **Token Cost Control** | ✅ Hard budget limits | ❌ | ❌ | ❌ |
| **Security Sandbox** | ✅ WASI isolation | ❌ | ❌ | ❌ |
| **Policy Control (OPA)** | ✅ Fine-grained rules | ❌ | ❌ | ❌ |
| **Deterministic Replay** | ✅ Time-travel debugging | ❌ | ❌ | ❌ |
| **Session Persistence** | ✅ Redis-backed, durable | ⚠️ In-memory only | ⚠️ Limited | ❌ |
| **Multi-Language** | ✅ Go/Rust/Python | ⚠️ Python only | ⚠️ Python only | ⚠️ Python only |
| **Production Metrics** | ✅ Dashboard/Prometheus | ⚠️ DIY | ❌ | ❌ |

## 🚀 Quick Start

### Prerequisites

- Docker and Docker Compose
- Make, curl, grpcurl
- An API key for at least one supported LLM provider

<details>
<summary><b>Docker Setup Instructions</b> (click to expand)</summary>

#### Installin