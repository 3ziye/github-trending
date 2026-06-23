<div align="center">

<img src="imgs/CrossLinkBanner.png" alt="CrossLink Banner">

<br/>

<img src="https://img.shields.io/badge/Go-1.22+-00ADD8?style=for-the-badge&logo=go" alt="Go Version">
<img src="https://img.shields.io/badge/License-Apache%202.0-blue?style=for-the-badge" alt="License">
<img src="https://img.shields.io/badge/PRs-Welcome-brightgreen?style=for-the-badge" alt="PRs Welcome">

<br/>
<br/>

# CrossLink

### One Gateway. Every Model. Zero Lock-in.

**OpenAI & Anthropic Compatible LLM API Gateway**

[English](#quick-start) | [中文](README_zh.md)

Unified proxy with intelligent routing, automatic failover, protocol translation,
rate limiting, caching, MCP gateway, and a built-in admin dashboard.

[Get Started](#quick-start) · [Features](#features) · [Architecture](#architecture) · [API Docs](#api-endpoints) · [Contributing](CONTRIBUTING.md)

</div>

---

## Why CrossLink?

Every LLM provider has a different API format, auth mechanism, and feature set.
Adapting your code for each one is tedious, error-prone, and locks you in.

CrossLink solves this by acting as a **universal adapter** between your application and
any LLM provider:

- **One endpoint** — Your code talks to a single API in either OpenAI or Anthropic format
- **Any provider** — Requests are routed to OpenAI, Anthropic, Azure, DeepSeek, Qwen,
  Ollama, or any OpenAI-compatible service
- **Automatic translation** — Full bidirectional protocol conversion including streaming SSE,
  tool use, and extended thinking
- **Resilient by default** — Circuit breakers, fallback chains, and retry policies keep your
  application running when providers don't

---

## Features

### Core Gateway

- **Dual Protocol** — Exposes both `/v1/chat/completions` (OpenAI) and `/v1/messages` (Anthropic)
  endpoints with automatic bidirectional translation
- **Multi-Provider** — Route to OpenAI, Anthropic, Azure OpenAI, DeepSeek, Qwen, Moonshot, Ollama,
  and any OpenAI-compatible provider
- **Intelligent Routing** — 6 strategies: weighted random, round-robin, least latency, least cost,
  least busy, and canary deployment
- **Automatic Failover** — Multi-provider fallback chains with circuit breakers, configurable retry
  policies (exponential/fixed/linear backoff), and error classification
- **Response Caching** — Redis-based caching with per-model TTL, gzip compression, and
  cache key isolation per user

### Security & Control

- **Rate Limiting** — Per-key RPM/TPM limits with global concurrency control (2000)
- **RBAC** — Role-based access control for providers, models, API keys, and MCP
- **Budget Management** — Per-key and per-team budget limits with automatic circuit breaking
- **Guardrails** — Content safety engine framework with configurable rules and actions
- **Crypto Flexibility** — Standard (SHA-256/RSA/AES) or Chinese national cryptography (SM3/SM2/SM4)

### Observability

- **Usage Analytics** — Token usage, cost tracking, latency metrics, cache hit rates, and
  fallback/retry counts per request
- **Prometheus Metrics** — Built-in metrics endpoint for monitoring
- **OpenTelemetry** — Distributed tracing support
- **Structured Logging** — JSON logging with request context

### MCP Gateway

- **Model Context Protocol** — HTTP/SSE transport, tool discovery with caching, health checks
- **Permission Management** — Per-principal tool access control (allow/deny by key, team, or role)
- **Call Logging** — Comprehensive tool call logging with monthly partitioning and auto-cleanup

### Operations

- **Vue 3 Admin Dashboard** — Built-in web UI for providers, models, keys, usage, and MCP
  management ([CrossLink-UI-Standard](https://github.com/HotRiceNoodles/CrossLink-UI-Standard))
- **Multi-Instance** — Redis Pub/Sub for provider registry sync and distributed round-robin
- **Graceful Shutdown** — 4-phase drain: in-flight SSE streams → HTTP shutdown → worker flush →
  background goroutine cancellation
- **One-Command Deploy** — Docker Compose spins up gateway, frontend, PostgreSQL, and Redis in one command

---

## Architecture

<p align="center">
  <img src="imgs/Architecture.png" alt="CrossLink Architecture" width="720">
</p>

---

## Quick Start

### Prerequisites

- Go 1.22+ (building from source)
- PostgreSQL 14+
- Redis 7+

### Docker Compose (Recommended)

Frontend ([CrossLink-UI-Standard](https://github.com/HotRiceNoodles/CrossLink-UI-Standard)) and backend are built together. One command starts everything:

```bash
git clone https://github.com/HotRiceNoodles/CrossLink.git
cd CrossLink
docker compose -f deployments/docker-compose.dev.yaml up --build
```

Frontend dashboard and API gateway are available at `http://localhost` (port 80).

> **China network?** Use `docker compose -f deployments/docker-compose.cn.yaml up --build` with Go and npm mirrors pre-configured.

### Build from Source

```bash
git clone https://github.com/HotRiceNoodles/CrossLink.git
cd CrossLink
cp configs/config.example.yaml configs/config.yaml
# Edit config.yaml with your database