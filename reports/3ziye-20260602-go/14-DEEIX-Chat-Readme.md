<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./frontend/public/logo-white.svg" />
    <img src="./frontend/public/logo-black.svg" alt="DEEIX Chat" width="160" />
  </picture>
</p>

<p align="center">
  An enterprise AI workspace for model routing, multimodal chat, files, tools, billing, identity, and operations.
</p>

<p align="center">
  English | <a href="./README.zh-CN.md">简体中文</a>
</p>

<p align="center">
  <a href="https://deeix.com"><img alt="Website" src="https://img.shields.io/badge/Website-deeix.com-black" /></a>
  <a href="https://www.apache.org/licenses/LICENSE-2.0"><img alt="License" src="https://img.shields.io/badge/License-Apache%202.0-blue" /></a>
  <img alt="Next.js" src="https://img.shields.io/badge/Next.js-16-black" />
  <img alt="React" src="https://img.shields.io/badge/React-19-149eca" />
  <img alt="Go" src="https://img.shields.io/badge/Go-1.25-00add8" />
</p>

## Overview

DEEIX Chat gives teams a unified workspace for working with multiple AI models and providers. It combines multimodal chat, model routing, file and RAG workflows, MCP tools, usage billing, identity, audit logs, and operational controls in one product.

The architecture is designed for simple deployment, efficient static delivery, and a predictable Go runtime footprint. The admin console centralizes upstream channels, platform model names, routing priority, pricing, subscriptions, users, and security policies, while the conversation workspace keeps the user experience stable and focused.

![DEEIX Chat workspace](./frontend/public/DEEIX-Chat.jpg)

## Features

| Area | Capabilities |
| --- | --- |
| Conversations | Multi-branch chat, streaming, retries, edits, feedback, sharing, cloned shared conversations, rich markdown rendering, file cards, model metadata, usage details, and execution traces. |
| Media generation | Dedicated image generation and image edit flow with task-aware routing, provider-native OpenAI, Google, and xAI image protocols, generated file storage, preview, download, and run history separated from text chat. |
| Model control plane | Platform model catalog, upstream channels, real upstream models, route bindings, priority and weight routing, model capability JSON, display ordering, vendor mapping, automatic icons, and circuit breaker state. |
| Provider protocols | OpenAI Responses, Chat Completions, Images Generations, and Images Edits; Anthropic Messages; Google/Gemini Generate Content and Image Generation; xAI Responses, Images Generations, and Images Edits; OpenRouter defaults; and custom OpenAI-compatible routes. |
| Request governance | Protocol-aware request assembly, user option allowlists and denylists, system-protected fields, previous-response continuation where supported, and context snapshots for review. |
| Files and RAG | File upload, preview, download, deletion, quota control, MIME detection, text extraction, OCR, full-context injection, image context, chunking, embeddings, and semantic retrieval. |
| Memory and context | Message-window truncation, token-budget truncation, context compression, conversation memory, long-term user memory, RAG evidence records, and prompt trace inspection. |
| Tools | Admin-managed MCP servers, tool discovery, per-tool enablement, user-side tool selection, execution limits, retries, trace rendering, and tool result handling. |
| Billing and payments | Subscription plans, top-ups, balances, token/call/duration/tiered model pricing, free models, prepaid thresholds, usage ledgers, billing snapshots, Stripe Checkout, EPay, and webhook validation. |
| Identity and security | Local login, registration, session management, HttpOnly refresh cookies, 2FA/TOTP, recovery codes, trusted devices, SSO/OIDC/OAuth providers, contact verification, timezone, and locale. |
| Administration | Users, roles, auth providers, upstreams, platform models, route bindings, model pricing, subscriptions, balances, usage logs, audit logs, auth events, system events, and runtime settings. |
| Operations | Efficient static delivery, predictable Go runtime footprint, Docker builds, single-runtime frontend/API serving, Swagger docs, structured logs, request IDs, Redis caching, PostgreSQL pgvector, optional GeoIP, optional OpenTelemetry, and S3-compatible storage. |

<p>
  <img src="./frontend/public/DEEIX-Chat-Image.png" alt="DEEIX Chat image generation" width="32%" />
  <img src="./frontend/public/DEEIX-Chat-Dark.png" alt="DEEIX Chat dark mode" width="32%" />
  <img src="./frontend/public/DEEIX-Chat-Usage.png" alt="DEEIX Chat usage and billing" width="32%" />
</p>

## Architecture

```text
frontend/  Next.js App Router web application
backend/   Go API service, domain/application layers, infra adapters, Swagger docs
docker/    Optional document extraction and OCR services
```

Backend code follows a layered structure:

```text
cmd -> internal/cli -> internal/app
transport/http -> application -> repository interfaces -> infra implementations
doma