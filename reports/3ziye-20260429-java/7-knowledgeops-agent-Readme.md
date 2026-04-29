# KnowledgeOps Agent | Enterprise Spring AI RAG Platform | 智能问答与知识运营平台

[![CI](https://github.com/however-yir/knowledgeops-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/however-yir/knowledgeops-agent/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/however-yir/knowledgeops-agent)](https://github.com/however-yir/knowledgeops-agent/releases)
[![Docs](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://however-yir.github.io/knowledgeops-agent/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Docker](https://img.shields.io/badge/container-GHCR-blue?logo=docker)](https://github.com/however-yir/knowledgeops-agent/pkgs/container/knowledgeops-agent)

KnowledgeOps Agent is an enterprise Spring AI RAG platform that turns document knowledge into deployable, governed, and measurable AI workflows. It combines tenant-isolated retrieval, asynchronous PDF ingestion, JWT/API key/RBAC security, audit trails, Prometheus/Loki/Tempo observability, and regression evaluation so teams can verify the system as a platform instead of treating it as a one-off demo.

> 面向企业知识运营场景的 Spring AI RAG 旗舰项目：覆盖“企业 RAG、租户隔离、异步入库、权限审计、可观测、回归评测”全链路，目标是提供可部署、可运维、可验证的生产级工程基线。

![KnowledgeOps Agent console](docs/assets/console-overview.png)

## Why It Is More Than a Demo

| Proof point | Repository evidence |
|---|---|
| Enterprise RAG | PDF upload, async ingestion jobs, tenant-scoped retrieval, answer citations, evidence snippets |
| Tenant and permission boundary | API Key, JWT, refresh token lifecycle, RBAC permissions, tenant headers, audit logging |
| Operations baseline | Docker Compose, Flyway migrations, structured logs, Prometheus metrics, Loki logs, Tempo traces, Alertmanager rules |
| Quality evidence | Unit tests, Testcontainers integration tests, JaCoCo, regression evaluation, E2E smoke logs, Docker image build |
| Extensible AI workflow | Spring AI chat, ReAct trace payloads, SSE token streaming, model routing, tool execution hooks |

## Product Surfaces

| Surface | What to inspect |
|---|---|
| Console workspace | Session branches, streaming mode, model profile, JWT/API key auth, tenant context |
| RAG answer | Citation chips, evidence snippets, empty-result fallback policy |
| API surface | Swagger UI, curl recipes, chat/RAG/ingestion/auth/audit endpoints |
| Operations surface | Health, Prometheus metrics, E2E artifacts, regression reports, container image |

![RAG answer with citations](docs/assets/rag-answer-citations.png)

## Architecture At a Glance

![KnowledgeOps Agent architecture](docs/assets/architecture-overview.svg)

## 5-Minute Proof Path

```bash
git clone https://github.com/however-yir/knowledgeops-agent.git
cd knowledgeops-agent
./scripts/demo.sh
```

After startup:

- Frontend console: `http://localhost:8088`
- Backend API: `http://localhost:8080`
- Swagger UI: `http://localhost:8080/swagger-ui/index.html`
- Local demo API key: see the seeded development value in `.env.example` or the authentication card in the frontend console.

Prefer Make targets if you use `make`:

```bash
make demo
make demo-verify
make demo-down
```

## Evidence Links

- Documentation: [however-yir.github.io/knowledgeops-agent](https://however-yir.github.io/knowledgeops-agent/)
- Latest release: [v1.0.0](https://github.com/however-yir/knowledgeops-agent/releases/tag/v1.0.0)
- Reproducible demo script: [docs/demo-script.md](docs/demo-script.md)
- Operations guide: [docs/operations.md](docs/operations.md)
- Enterprise architecture: [docs/architecture-enterprise.md](docs/architecture-enterprise.md)

---

## 目录

- Why It Is More Than a Demo
- Product Surfaces
- Architecture At a Glance
- 5-Minute Proof Path
- Evidence Links
- 项目定位
- Why KnowledgeOps Agent?
- 企业级能力矩阵
- 技术栈与版本基线
- 架构总览
- 核心模块
- 快速开始
- 容器化部署
- 生产部署建议
- 环境变量与配置项
- API 概览
- 安全与权限体系
- 可观测与运维
- 测试与质量保障
- 性能与容量规划
- 文档索引
- 路线图
- 项目主周期

---

## 项目定位

本项目按“企业级 Spring AI RAG 平台”设计，不停留在单接口聊天示例，而是把知识入库、检索问答、租户与权限边界、审计可追溯、可观测运维、质量回归放在同一条可验证链路里。它适合作为企业知识库、智能客服、内部运营助手或 AI 平台工程基线继续扩展。

重点解决以下问题：

1. 如何把对话能力稳定落在业务流程中，而不是仅做单轮聊天。
2. 如何把 PDF/文档知识接入检索增强链路，并保证可追溯来源。
3. 如何让工具调用具备权限边界、审计记录和失败可恢复机制。
4. 如何实现线上可运维：日志、指标、链路追踪、告警、回归评测闭环。

适用场景：

- 智能客服与企业知识问答
- 内部知识库检索问答（文档上传、切片、向量化、检索）
- 需要 AI + 业务工具联合执行的流程型场景

---

## Why KnowledgeOps Agent?

| Capability | KnowledgeOps Agent | Typical RAG demo | Typical Spring AI sample |
|---|---|---|---|
| Deployable full stack | Spring Boot API, Vue console, MySQL, Redis/RabbitMQ, pgvector, Docker Compose | Often API-only or notebook-level | Usually focused on one framework feature |
| Tenant-aware security | API Key, JWT, refresh tokens, RBAC, tenant headers, audit logs, rate limits | Rarely included | Usually omitted for clarity |
| Async ingestion | Redis Stream or RabbitMQ queues, retries, DLQ, idempotency, job status | Often synchronous upload and parse | Usually sample-specific |
| RAG production path | Tenant-scoped retrieval, citations, chunking, reranking hooks, pgvector ind