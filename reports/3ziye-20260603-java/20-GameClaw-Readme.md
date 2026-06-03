<div align="center">

# GameClaw

**Game Enterprise R&D AI Agent Control Plane**

[![Java](https://img.shields.io/badge/Java-25-orange?logo=openjdk)](https://jdk.java.net/25/)
[![Spring Boot](https://img.shields.io/badge/Spring%20Boot-4.0.6-brightgreen?logo=springboot)](https://spring.io/projects/spring-boot)
[![Spring AI](https://img.shields.io/badge/Spring%20AI-2.0.0--M6-6DB33F?logo=spring)](https://spring.io/projects/spring-ai)
[![License](https://img.shields.io/badge/License-LGPL%20v3-blue)](LICENSE)

**English** | [简体中文](docs/readme/README.zh-CN.md)

[Features](#features) · [Quick Start](#quick-start) · [Architecture](#architecture) · [Configuration](#configuration) · [Contributing](#contributing)

</div>

---

## What is GameClaw

GameClaw is an AI Agent control plane designed for game development teams. It enables designers, programmers, QA, and ops to collaborate with AI through natural language, handling daily tasks such as game config generation, code writing, data queries, and test automation.

**Core Values**:

- **Game-Specific** — Built-in Unity / Unreal / Godot API index + hallucination detection; AI won't fabricate non-existent APIs
- **Five-Layer Security** — Network TLS → Access OAuth2 → Application RBAC → Data RLS → Audit logging, enterprise-grade security out of the box
- **Multi-Tenant Isolation** — PostgreSQL 16 Row-Level Security, strict data isolation across projects and teams
- **25+ LLM Providers** — Anthropic / OpenAI / DeepSeek / Ollama / Groq / Qwen / Kimi, switch with a single config
- **Omnichannel Access** — Web / Feishu / Telegram / Discord, the same Agent across all platforms
- **Plugin Ecosystem** — OpenClaw L3 compatibility + Skills hot-reload + MCP protocol, extensible by third-party developers

---

## Features

### Game Design Tools

| Tool | Description |
|------|-------------|
| `generate_monsters` | Natural language description → monster JSON config table |
| `generate_skills` | Generate skill configs |
| `generate_items` | Generate item configs |
| `generate_quests` | Generate quest configs |
| `generate_growth_curve` | Generate growth curve CSV |
| `query_engine_api` | Query engine APIs ("How to load a scene in Unity" → SceneManager.LoadScene) |

### Programmer Tools

| Tool | Description |
|------|-------------|
| `generate_unity_script` | Requirement → C# code + API hallucination check → write to sandbox |
| `generate_unreal_script` | Same as above, C++ |
| `generate_godot_script` | Same as above, GDScript |

### Data Analysis Tools

| Tool | Description |
|------|-------------|
| `query_data` | Natural language → SQL → dual-layer validation → execute → PII-masked response |

### Governance & Security

| Layer | Capability |
|-------|------------|
| Gate 1 | Schema validation (Jackson + Bean Validation) |
| Gate 2 | Rule engine (10 default rules + YAML custom rules) |
| RBAC | 5 risk levels x 10 roles, `@RequireRole` / `@RequireRiskLevel` annotations |
| Quota | Three-tier quotas (user daily / project monthly / global daily budget) |
| PII | Auto-masking + role-based decryption |

### Plugins & Extensions

| Capability | Description |
|------------|-------------|
| OpenClaw L3 Compatible | `@OpenClawPlugin` + `PluginClassLoader` isolation + resource sandbox |
| Skills Hot-Reload | Auto-reload within 250ms after SKILL.md file changes |
| MCP Protocol | Spring AI MCP Client + built-in MCP Server |
| ClawHub Skill Market | install / search / update CLI commands |

---

## Architecture

![GameClaw Architecture](../img/architecture.svg)


### Project Structure

```
GameClaw/
├── base/                    # Core module (20 sub-packages)
│   ├── agent/               # Agent core + LLM abstraction
│   ├── channels/            # Channel registration + session management
│   ├── compat/              # OpenClaw compatibility layer + L3 plugin system
│   ├── concurrency/         # StructuredTaskScope wrapper
│   ├── configuration/       # YAML/JSON dual-format config
│   ├── cost/                # Three-tier quota management
│   ├── files/               # YAML frontmatter parsing
│   ├── governance/          # Four-layer gates + rule engine
│   ├── mcp/                 # MCP connection config
│   ├── observability/       # Micrometer metrics + audit
│   ├── persistence/         # Multi-tenant datasource + RLS
│   ├── project/             # Project management
│   ├── security/            # RBAC + PII + Prompt injection detection
│   ├── skills/              # Skills parsing + hot-reload + ClawHub
│   ├── tasks/               # JobRunr task scheduling
│   └── tools/               # Game tools + Data tools + Sandbox
├── providers/               # LLM providers (7 native + 18 OpenAI-compatible)
├── plugins/                 # Channel plugins (Feishu/Telegram/Discord/Brave/Playwright)
├── mcp-servers/java/        # MCP Server (ClickHouse)
├── app/                     # Spring Boot entry module + CLI
└── deploy/docker/           # Docker deployment (PG16)
```

### Tech Stack

| Com