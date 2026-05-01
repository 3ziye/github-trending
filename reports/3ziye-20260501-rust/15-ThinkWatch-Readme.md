<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/logo-dark.png">
    <img src="assets/logo.png" alt="ThinkWatch" width="480">
  </picture>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white" />
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" />
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white" />
</p>

# ThinkWatch

**[English](README.md) | [中文](README.zh-CN.md)**

**The enterprise-grade secure gateway for AI.** Secure, audit, and govern every AI API call and MCP tool invocation across your organization — from a single control plane.

Just as an SSH secure gateway is the single gateway through which all server access must flow, ThinkWatch is the single gateway through which all AI access must flow. Every model request. Every tool call. Every token. Authenticated, authorized, rate-limited, logged, and accounted for.

```
                    ┌──────────────────────────────────────┐
 Claude Code ──────>│                                      │──> OpenAI
 Cursor ───────────>│    Gateway  :3000                    │──> Anthropic
 Custom Agent ─────>│    AI API + MCP Unified Proxy        │──> Google Gemini
 CI/CD Pipeline ───>│                                      │──> Azure OpenAI / AWS Bedrock
                    └──────────────────────────────────────┘
                    ┌──────────────────────────────────────┐
 Admin Browser ────>│    Console  :3001                    │
                    │    Management UI + Admin API          │
                    └──────────────────────────────────────┘
```

## Why ThinkWatch?

As AI agents proliferate across engineering teams, organizations face a growing governance challenge:

- **API keys scattered everywhere** — hardcoded in `.env` files, shared in Slack, rotated never
- **Zero visibility** — who used which model, how many tokens, at what cost?
- **No access control** — every developer has direct access to every model and every MCP tool
- **Compliance gaps** — no audit trail for AI-assisted code generation or data access
- **Cost surprises** — monthly AI bills that nobody can explain or attribute

ThinkWatch solves all of this with a single deployment.

## Key Features

### AI API Gateway
- **Multi-format API proxy** — natively serves OpenAI Chat Completions (`/v1/chat/completions`), Anthropic Messages (`/v1/messages`), and OpenAI Responses (`/v1/responses`) APIs on a single port; works as a drop-in replacement for Cursor, Continue, Cline, Claude Code, and the OpenAI/Anthropic SDKs
- **Multi-provider routing** — OpenAI, Anthropic, Google Gemini, Azure OpenAI, AWS Bedrock, or any OpenAI-compatible endpoint
- **Automatic format conversion** — Anthropic Messages API, Google Gemini, Azure OpenAI, AWS Bedrock Converse API, and more, all behind a unified interface
- **Provider auto-loading** — active providers are loaded from the database at startup and registered in the model router; default model prefixes (`gpt-`/`o1-`/`o3-`/`o4-` for OpenAI, `claude-` for Anthropic, `gemini-` for Google) route automatically; Azure and Bedrock require explicit model registration
- **Streaming SSE pass-through** — zero-overhead forwarding with real-time token counting
- **Virtual API keys** — issue scoped `tw-` keys; the same `tw-` token works on both the AI gateway and the MCP gateway via a per-key `surfaces` allowlist
- **API key lifecycle management** — automatic rotation with grace periods, per-key inactivity timeout, expiry warnings, and background policy enforcement
- **Composable rate limits & budgets** — multi-window sliding limits (1m / 5m / 1h / 5h / 1d / 1w) and natural-period token budgets (daily / weekly / monthly), keyed per user, per API key, per provider, or per MCP server. See [Rate limits & budgets](#rate-limits--budgets) below
- **Per-model token weighting** — gpt-4o tokens can count more than gpt-3.5 tokens against the same quota via configurable `input_multiplier` / `output_multiplier`
- **Circuit breaker** — three-state (Closed/Open/HalfOpen) circuit breaker with configurable failure threshold and recovery period
- **Retry with exponential backoff** — configurable retries with jitter for network errors and upstream rate limits
- **Real-time cost tracking** — per-model pricing with team attribution

### MCP Gateway
- **Centralized tool proxy** — one MCP endpoint that aggregates tools from all upstream servers
- **Namespace isolation** — `github__create_issue`, `postgres__query` — no tool name collisions
- **Tool-level