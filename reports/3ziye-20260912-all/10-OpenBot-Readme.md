<div align="center">

# OpenBot

**AI coworkers you can hand real work to, and actually trust with the access.** Each gets a computer of its own: a real browser with its own logins, its own files, and only the tools you grant. Every action decided before it happens and recorded after.

[**copilotkit.ai/openbot**](https://copilotkit.ai/openbot) · [**Quick start**](#quick-start) · [**Features**](#features) · [**Bring your own agent**](#bring-your-own-agent) · [**Architecture**](#architecture) · [**Docs**](docs/README.md)

[![CI](https://github.com/CopilotKit/openbot/actions/workflows/ci.yml/badge.svg)](https://github.com/CopilotKit/openbot/actions/workflows/ci.yml)
[![security](https://github.com/CopilotKit/openbot/actions/workflows/security_zizmor.yml/badge.svg)](https://github.com/CopilotKit/openbot/actions/workflows/security_zizmor.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)
![Alpha](https://img.shields.io/badge/status-alpha-orange.svg)

[![Trendshift: #3 Repository Of The Day](https://trendshift.io/api/badge/trendshift/repositories/175080/daily)](https://trendshift.io/repositories/175080)

</div>

https://github.com/user-attachments/assets/535ef7ee-1631-4a69-b839-564c56cf90b4

<div align="center">

Bring any AG-UI agent, written on a framework or by hand, and it arrives as a
coworker with a channel of its own. Watch it work on its own screen, take the
wheel when it reaches something it should not do alone, then hand it back. It
answers with components rather than only prose, and the whole thing runs on
your own machine.

</div>

> **A template, not a product.** OpenBot is meant to be cloned and made your own. There is no hosted version to sign up for, and nothing here is published as a package to depend on: every workspace in this repository is private. You take the repository, replace the example tenant package under `examples/` with your own coworkers, channels and skills, and run it. Everything below describes a starting point, not a finished thing somebody operates for you.

> **Alpha, and under active development.** OpenBot is early. Expect rough edges and bugs, and expect things to move. Issues and pull requests are welcome.

> **Runs on your machine.** Everything below is written for a laptop. `.env.example` carries `OPENBOT_SINGLE_USER=true`, which admits every request as one administrator, so a fresh clone reaches the product without registering an OAuth client first. [Sign-in](#sign-in) turns that off, and is required before anybody else can reach the deployment.

## What it is

An agent platform that runs inside your own infrastructure. Docker Compose brings up every part of it, the data sits in your PostgreSQL, and the model is yours to choose: no model ships in the box, and an administrator supplies the credential, which is encrypted at rest and never logged.

Three coworkers ship in the example package, and they are configuration rather than code: **General Assistant** for everyday work, **Knowledge** for company questions, **Risk Analyst** for risk and compliance. Add your own by editing `agents.yaml` or from `/agents` in the UI.

Anything a Bot does to a computer, a file, an MCP server or a component goes through one gateway that decides and records it. That is the difference between an agent that can use your tools and an agent you can let near them.

More at [copilotkit.ai/openbot](https://copilotkit.ai/openbot).

## Built on AG-UI

A Bot is any endpoint speaking [AG-UI](https://github.com/ag-ui-protocol/ag-ui), the open protocol for agent-to-user interaction, so OpenBot is not tied to a framework and neither are you. Agents built with LangGraph, Mastra, CrewAI, Pydantic AI, Google ADK or written by hand all arrive the same way, and the governance rides the protocol rather than the framework.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/architecture-dark.svg">
  <img src="assets/architecture-light.svg" alt="You talk to the server, which sends the turn to a Bot over AG-UI. Every tool call the Bot makes comes back through the gateway, which resolves the target, decides it against your policy, records an audit row, and only then acts, or refuses and names the rule. Allowed browser and file actions reach that Bot's own computer, one container each with its own Chromium, logins and workspace, built by the supervisor. Decisions land in PostgreSQL and threads in CopilotKit Intelligence.">
</picture>

## Requirements

- Docker, for PostgreSQL and the shipped Bots.
- [Bun](https://bun.sh) 1.3+, for the app and API server.
- A CopilotKit Intelligence project and license. A free plan is available, and Intelligence can be self-hosted.
- A model key. The proof-of-concept Bot uses OpenAI; the LangGraph Bot can use OpenAI, Anthropic, or Google.

## Quick start

> **Setting up with an AI assistant?** Paste [`prompt.txt`](prompt.txt) into it first. It carries the
> same steps as below plus the things that are easy to get wrong: which of