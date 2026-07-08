# Flowdesk

Original Java 21 / Spring Boot 3 AI Office Automation Backend with RAG Citations, Ollama/DashScope, MCP Adapter, and Demo Pack.

[![CI](https://github.com/evans778-star/flowdesk/actions/workflows/ci.yml/badge.svg)](https://github.com/evans778-star/flowdesk/actions/workflows/ci.yml)
![Java 21](https://img.shields.io/badge/Java-21-blue)
![Spring Boot 3](https://img.shields.io/badge/Spring%20Boot-3.2-brightgreen)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Docker Compose](https://img.shields.io/badge/Docker%20Compose-MongoDB%20%2B%20Redis%20Stack-2496ED)

Flowdesk is an original Java 21 / Spring Boot 3 backend template for AI-assisted office workflows. It combines normal office automation APIs with local RAG, citations, an offline RAG quality lab, MCP HTTP/JSON-RPC previews, and a local stdio MCP bridge for AI developer clients.

**Beta status:** this beta repository is ready for demos, learning, GitHub review, and internal template adaptation. It is not recommended for direct production use before you add RBAC, rate limits, real monitoring, backups, production storage, and deployment-specific security controls.

Core capabilities:

- User / department / group management
- Todo / approval workflows
- AI chat with DashScope or Ollama
- Local RAG with Redis Stack / RediSearch
- RAG citations and quality lab
- MCP adapter preview for AI clients
- Demo Pack with smoke verification
- Request ID observability and production hardening docs

## Try It In 10 Minutes

Run local demo in 10 minutes with the Demo Pack:

```powershell
.\mvnw.cmd package
docker compose -f docker-compose.demo.yml up -d --build
.\scripts\demo-smoke.ps1
```

The demo compose starts MongoDB, Redis Stack, and the Flowdesk backend with AI disabled, MCP enabled, and write tools disabled. It uses local placeholder credentials only.
Real AI chat still requires Ollama or DashScope, while the default demo path works without API keys.
Real RAG retrieval requires Redis Stack + embedding provider configuration.

## What Works Without API Keys

| Capability | Works without API keys? | Notes |
| --- | --- | --- |
| Health/login/upload/MCP metadata | Yes | Covered by `scripts\demo-smoke.ps1`. |
| JSON-RPC initialize/ping/tools/list | Yes | Requires local login token only. |
| RAG citation response shape | Yes | The endpoint can return the `citations` field without real retrieval. |
| Real AI answer | No | Requires Ollama or DashScope. |
| Real vector retrieval | No | Requires Redis Stack + embedding provider. |

## Release Readiness

| Check | Status |
| --- | --- |
| CI | Java 21 Maven build on Linux and Windows. |
| Tests | Unit and smoke-style tests run without real MongoDB, Redis, DashScope, or Ollama. |
| Package | Spring Boot jar is built by Maven. |
| Demo smoke | `scripts\demo-smoke.ps1` verifies health, login, MCP, and citation response shape. |
| Secret scan | Broad scan is documented; high-confidence scan must be clean. |
| Docs | Demo, MCP, RAG, production hardening, observability, and release docs are linked below. |

Release workflow docs:

- [GitHub issue pack](docs/github-issue-pack.md)
- [v0.1.0 release notes draft](docs/release-notes-v0.1.0.md)
- [Roadmap](ROADMAP.md)

MCP preview example:

```bash
curl -X POST http://localhost:8888/v1/mcp/tools/flowdesk_search_knowledge/call \
  -H "Authorization: Bearer <jwt-token>" \
  -H "Content-Type: application/json" \
  -d '{"arguments":{"query":"What should employees do before taking leave?","topK":3}}'
```

Run with DashScope in production-like cloud mode, or use Ollama for a no-key local AI demo. Flowdesk is designed for demos, learning, and internal adaptation without mixing secrets, local state, and production configuration into the repository.

JSON-RPC preview:

```bash
curl -X POST http://localhost:8888/v1/mcp/jsonrpc \
  -H "Authorization: Bearer <jwt-token>" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":"init-1","method":"initialize","params":{"protocolVersion":"2025-06-18"}}'
```

MCP is disabled unless `FLOWDESK_MCP_ENABLED=true`; write tools remain disabled unless `FLOWDESK_MCP_WRITE_TOOLS_ENABLED=true`.
See [docs/demo-pack.md](docs/demo-pack.md) for the Docker demo and [tools/mcp-bridge](tools/mcp-bridge) for the stdio bridge preview.

## Start Here

- [Local demo](docs/demo.md)
- [Demo Pack](docs/demo-pack.md)
- [Demo walkthrough](docs/demo-walkthrough.md)
- [Demo assets guide](docs/demo-assets.md)
- [HTTP examples](docs/api-examples.http)
- [Architecture](docs/architecture.md)
- [Configuration](docs/configuration.md)
- [RAG guide](docs/rag.md)
- [RAG Quality Lab](docs/rag-quality-lab.md)
- [MCP adapter preview](docs/mcp.md)
- [MCP client examples](docs/mcp-client-examples.md)
- [Deployment notes](docs/deployment.md)
- [Production hardening](docs/production-hardening.md)
- [Observability](docs/observability.md)
- [Release checklist](docs/release-checklist.md)
- [GitHub issue pack](docs/github-issue-pack.md)
- [v0.1.0 relea