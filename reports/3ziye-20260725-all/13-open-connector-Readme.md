<div align="center">

<img src="assets/openconnector-readme-banner.png" alt="OpenConnector - Connect Once. Use Everywhere." width="100%" />

[English](README.md) | [简体中文](docs/README.zh-CN.md) | [繁體中文](docs/README.zh-TW.md) | [日本語](docs/README.ja.md) | [Русский](docs/README.ru.md) | [Français](docs/README.fr.md)

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE.txt)
![Node.js 22+](https://img.shields.io/badge/Node.js-22%2B-339933)
![Cloudflare compatible](https://img.shields.io/badge/Cloudflare-compatible-F38020)
![MCP](https://img.shields.io/badge/MCP-ready-111827)
![OpenAPI](https://img.shields.io/badge/OpenAPI-3.1-6BA539)

[![Providers](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fconnector.oomol.com%2Fv1%2Fcatalog&query=data.providerCount&label=Providers&color=%237d7fe9)](https://oomol.com/apps)
[![Actions](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fconnector.oomol.com%2Fv1%2Fcatalog&query=data.actionCount&label=Actions&color=%237d7fe9)](https://oomol.com/apps)

</div>

OpenConnector is an open-source connector gateway for AI agents and an alternative to Composio.
Connect user app accounts once, then expose a shared catalog of 1,000+ providers and 10,000+
prebuilt Actions to agents and applications.

Use the [Connector SDK](https://github.com/oomol-lab/connector-sdk) from app code,
[oo CLI](https://github.com/oomol-lab/oo-cli) as the local-agent relay, MCP from agent hosts,
HTTP/OpenAPI from custom clients, and the Web Console for administration and debugging.

- Keep credentials, scopes, schemas, policies, and run logs inside an inspectable runtime.
- Run locally, on Fly.io, on Cloudflare-compatible infrastructure, or through OOMOL's hosted
  runtime.
- Use the same provider ids, Action ids, schemas, and contracts across open-source and commercial
  SaaS deployments.

## What It Provides

- A working connector catalog across products such as GitHub, Gmail, Notion, BigQuery, Google
  Analytics, Supabase, Airtable, Slack, and more.
- Credential handling for API keys, OAuth2, custom credentials, and no-auth providers.
- Inspectable Action contracts: request/response schemas, required scopes, and lazy-loaded executor
  source.
- Runtime controls for connection identity, scopes, runtime tokens, action allow/block policies,
  temporary file transit, and redacted run logs.
- Deployment options for local Docker or Node.js, Fly.io with persistent SQLite storage,
  Cloudflare Workers with D1/R2/Static Assets, and OOMOL's hosted runtime.

## Where It Fits

OpenConnector fits products where agents need durable access to the tools users already use, without
handing provider credentials to the agent process.

- Agent products that need reusable access across work apps, developer tools, data systems,
  communication platforms, and AI services.
- Products adding agent workflows that need stable, inspectable Action contracts for user app
  access.
- Teams that want hosted auth for speed while keeping a path to private or self-hosted runtime
  control.

## Developer Tools

| Tool                                                        | Purpose                                                                                                                                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Connector SDK](https://github.com/oomol-lab/connector-sdk) | Thin TypeScript HTTP client. Use `OpenConnector` for self-hosted runtimes, or `Connector` / `ProjectConnector` for OOMOL-hosted personal and SaaS end-user connections. |
| [oo CLI](https://github.com/oomol-lab/oo-cli)               | Local agent relay for connector Actions. `oo connector` can search, inspect, and run Actions against OOMOL-hosted or self-hosted OpenConnector runtimes.                |
| MCP                                                         | Expose app Actions to MCP-capable agent hosts through `http://localhost:3000/mcp`.                                                                                      |
| HTTP / OpenAPI                                              | Call `/v1/actions/*` directly or inspect the generated `/openapi.json` document.                                                                                        |

Endpoint details, response envelopes, auth headers, MCP tools, and Action guide examples are in
[docs/runtime-api.md](docs/runtime-api.md).

## Dashboard Preview

OpenConnector ships with a local Dashboard for browsing connectors, configuring credentials,
creating runtime tokens, and inspecting runtime usage.

### Connector Catalog

Use the connector catalog to see available services, search for providers, and open their Actions
and credential setup from one place.

![OpenConnector connector catalog 