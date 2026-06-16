<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./frontend/public/logo-white.svg" />
    <img src="./frontend/public/logo-black.svg" alt="DEEIX Chat" width="160" />
  </picture>
</p>

<p align="center">
  An integrated AI platform for enterprise model routing, chat, files, tools, billing, identity, and operations.
</p>

<p align="center">
  English | <a href="./README.zh-CN.md">简体中文</a>
</p>

<p align="center">
  <a href="https://deeix.com"><img alt="Website" src="https://img.shields.io/badge/Website-deeix.com-black" /></a>
  <a href="https://deeix.com/docs/deeix-chat/quickstart"><img alt="Guide" src="https://img.shields.io/badge/Guide-Quickstart-0f766e" /></a>
  <a href="https://t.me/deeix_chat"><img alt="Telegram" src="https://img.shields.io/badge/Telegram-deeix_chat-26A5E4?logo=telegram&logoColor=white" /></a>
  <a href="https://x.com/DEEIX_AI"><img alt="X" src="https://img.shields.io/badge/X-%40DEEIX_AI-black?logo=x&logoColor=white" /></a>
  <a href="https://www.apache.org/licenses/LICENSE-2.0"><img alt="License" src="https://img.shields.io/badge/License-Apache%202.0-blue" /></a>
  <img alt="Next.js" src="https://img.shields.io/badge/Next.js-16-black" />
  <img alt="React" src="https://img.shields.io/badge/React-19-149eca" />
  <img alt="Go" src="https://img.shields.io/badge/Go-1.26-00add8" />
</p>

## Overview

DEEIX Chat is an open-source, deployable AI platform for individuals, teams, and enterprises that need long-term, stable, and unified access to multiple model providers. It provides one clear entry point for multiple upstream models and providers, integrating multimodal chat, model routing, files and RAG, MCP tools, usage billing, identity, audit logs, and operational controls into one product.

The system is designed around simple deployment, efficient static delivery, and a low runtime resource footprint: lightweight without feeling limited, restrained without losing capability, and open without becoming disorderly.

![DEEIX Chat workspace](./frontend/public/DEEIX-Chat.jpg)

## Features

| Area | Capabilities |
| --- | --- |
| Conversations | A multimodal chat interface for daily use, with streaming, branches, retries, edits, feedback, sharing, rich rendering, and traceable model execution metadata. |
| Models and routing | A platform-model layer for upstream channels, real models, route bindings, priority, weights, circuit breaking, vendor mapping, and capability configuration, reducing the cost of multi-provider operations. |
| Protocols and adaptation | Unified support for OpenAI, Anthropic, Google/Gemini, xAI, OpenRouter, and OpenAI-compatible protocols across text, image, tools, and provider-native capability differences. |
| Files and retrieval | File upload, preview, extraction, OCR, storage quota, full-context injection, chunking, embeddings, and semantic retrieval so file content can naturally enter the conversation context. |
| Tool ecosystem | MCP servers and provider-native official tools with discovery, enablement, user selection, execution limits, result rendering, and tool-call traceability. |
| Context and memory | Message windows, token budgets, summary compression, conversation memory, long-term memory, and RAG evidence records for controlled-cost continuity. |
| Billing and payments | Model pricing, per-call tool pricing, subscriptions, top-ups, balances, usage ledgers, billing snapshots, Stripe Checkout, EPay, and webhook validation. |
| Identity and security | Local accounts, session management, HttpOnly refresh cookies, 2FA/TOTP, trusted devices, SSO/OIDC/OAuth, contact verification, and encrypted sensitive data. |
| Administration and audit | Centralized management for users, roles, upstreams, models, routes, pricing, subscriptions, balances, usage logs, audit logs, auth events, and system events. |
| Deployment and operations | Single-runtime frontend/API serving, Docker deployment, SQLite or PostgreSQL, in-memory cache or Redis, S3-compatible storage, Swagger, structured logs, version endpoint, GeoIP, and OpenTelemetry. |

<p align="center">
  <img src="./frontend/public/DEEIX-Chat-Image.png" alt="DEEIX Chat image generation" width="49.45%" />
  <img src="./frontend/public/DEEIX-Chat-Dark.png" alt="DEEIX Chat dark mode" width="49.45%" />
</p>

<p align="center">
  <img src="./frontend/public/DEEIX-Chat-Usage.png" alt="DEEIX Chat usage and billing" width="32.3%" />
  <img src="./frontend/public/DEEIX-Chat-Artifacts.png" alt="DEEIX Chat artifacts" width="32.3%" />
  <img src="./frontend/public/DEEIX-Chat-Html.png" alt="DEEIX Chat HTML rendering" width="32.3%" />
</p>

## Architecture and Tech Stack

DEEIX Chat uses a split frontend/backend development model with a single-runtime deployment path. The frontend is built into static assets and served by the Go service, while APIs, authorization, model routing, files, billing, and audit capabilities run in the same backend runtime. Heavy document extraction and OCR capabilities are opti