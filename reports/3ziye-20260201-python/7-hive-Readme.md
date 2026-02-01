<p align="center">
  <img width="100%" alt="Hive Banner" src="https://storage.googleapis.com/aden-prod-assets/website/aden-title-card.png" />
</p>

<p align="center">
  <a href="README.md">English</a> |
  <a href="docs/i18n/zh-CN.md">简体中文</a> |
  <a href="docs/i18n/es.md">Español</a> |
  <a href="docs/i18n/hi.md">हिन्दी</a> |
  <a href="docs/i18n/pt.md">Português</a> |
  <a href="docs/i18n/ja.md">日本語</a> |
  <a href="docs/i18n/ru.md">Русский</a> |
  <a href="docs/i18n/ko.md">한국어</a>
</p>

[![Apache 2.0 License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/adenhq/hive/blob/main/LICENSE)
[![Y Combinator](https://img.shields.io/badge/Y%20Combinator-Aden-orange)](https://www.ycombinator.com/companies/aden)
[![Docker Pulls](https://img.shields.io/docker/pulls/adenhq/hive?logo=Docker&labelColor=%23528bff)](https://hub.docker.com/u/adenhq)
[![Discord](https://img.shields.io/discord/1172610340073242735?logo=discord&labelColor=%235462eb&logoColor=%23f5f5f5&color=%235462eb)](https://discord.com/invite/MXE49hrKDk)
[![Twitter Follow](https://img.shields.io/twitter/follow/teamaden?logo=X&color=%23f5f5f5)](https://x.com/aden_hq)
[![LinkedIn](https://custom-icon-badges.demolab.com/badge/LinkedIn-0A66C2?logo=linkedin-white&logoColor=fff)](https://www.linkedin.com/company/teamaden/)

<p align="center">
  <img src="https://img.shields.io/badge/AI_Agents-Self--Improving-brightgreen?style=flat-square" alt="AI Agents" />
  <img src="https://img.shields.io/badge/Multi--Agent-Systems-blue?style=flat-square" alt="Multi-Agent" />
  <img src="https://img.shields.io/badge/Goal--Driven-Development-purple?style=flat-square" alt="Goal-Driven" />
  <img src="https://img.shields.io/badge/Human--in--the--Loop-orange?style=flat-square" alt="HITL" />
  <img src="https://img.shields.io/badge/Production--Ready-red?style=flat-square" alt="Production" />
</p>
<p align="center">
  <img src="https://img.shields.io/badge/OpenAI-supported-412991?style=flat-square&logo=openai" alt="OpenAI" />
  <img src="https://img.shields.io/badge/Anthropic-supported-d4a574?style=flat-square" alt="Anthropic" />
  <img src="https://img.shields.io/badge/Google_Gemini-supported-4285F4?style=flat-square&logo=google" alt="Gemini" />
  <img src="https://img.shields.io/badge/MCP-19_Tools-00ADD8?style=flat-square" alt="MCP" />
</p>

## Overview

Build reliable, self-improving AI agents without hardcoding workflows. Define your goal through conversation with a coding agent, and the framework generates a node graph with dynamically created connection code. When things break, the framework captures failure data, evolves the agent through the coding agent, and redeploys. Built-in human-in-the-loop nodes, credential management, and real-time monitoring give you control without sacrificing adaptability.

Visit [adenhq.com](https://adenhq.com) for complete documentation, examples, and guides.

## What is Aden

<p align="center">
  <img width="100%" alt="Aden Architecture" src="docs/assets/aden-architecture-diagram.jpg" />
</p>

Aden is a platform for building, deploying, operating, and adapting AI agents:

- **Build** - A Coding Agent generates specialized Worker Agents (Sales, Marketing, Ops) from natural language goals
- **Deploy** - Headless deployment with CI/CD integration and full API lifecycle management
- **Operate** - Real-time monitoring, observability, and runtime guardrails keep agents reliable
- **Adapt** - Continuous evaluation, supervision, and adaptation ensure agents improve over time
- **Infra** - Shared memory, LLM integrations, tools, and skills power every agent

## Quick Links

- **[Documentation](https://docs.adenhq.com/)** - Complete guides and API reference
- **[Self-Hosting Guide](https://docs.adenhq.com/getting-started/quickstart)** - Deploy Hive on your infrastructure
- **[Changelog](https://github.com/adenhq/hive/releases)** - Latest updates and releases
<!-- - **[Roadmap](https://adenhq.com/roadmap)** - Upcoming features and plans -->
- **[Report Issues](https://github.com/adenhq/hive/issues)** - Bug reports and feature requests

## Quick Start

### Prerequisites

- [Python 3.11+](https://www.python.org/downloads/) for agent development
- Claude Code or Cursor for utilizing agent skills

### Installation

```bash
# Clone the repository
git clone https://github.com/adenhq/hive.git
cd hive

# Run quickstart setup
./quickstart.sh
```

This sets up:
- **framework** - Core agent runtime and graph executor (in `core/.venv`)
- **aden_tools** - MCP tools for agent capabilities (in `tools/.venv`)
- All required Python dependencies

### Build Your First Agent

```bash
# Build an agent using Claude Code
claude> /building-agents-construction

# Test your agent
claude> /testing-agent

# Run your agent
PYTHONPATH=core:exports python -m your_agent_name run --input '{...}'
```

**[📖 Complete Setup Guide](ENVIRONMENT_SETUP.md)** - Detailed instructions for agent development

### Cursor IDE Support

Skills are also available in Curso