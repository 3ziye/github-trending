<div align="center">

<img src="docs/assets/hero.svg" alt="Duckle" width="100%"/>

<h3>The local-first data studio with a built-in AI assistant.</h3>

<p><b>Duckle</b> is an open-source desktop ETL / ELT studio. Drag a pipeline onto the canvas, describe what you need in plain English to <b>Duckie</b> (the on-device AI assistant), and execute at native speed through DuckDB. 290+ connectors, 50+ transforms, a built-in scheduler, and a chat assistant that runs entirely on your CPU. Ships as a ~65 MB single-file desktop app. No cloud, no servers, no lock-in.</p>

<p>
<img alt="status" src="https://img.shields.io/badge/status-beta-3b82f6"/>
<img alt="license" src="https://img.shields.io/badge/license-MIT%20OR%20Apache--2.0-blue"/>
<img alt="platforms" src="https://img.shields.io/badge/platforms-Windows%20%C2%B7%20macOS%20%C2%B7%20Linux-2b6cb0"/>
<img alt="rust" src="https://img.shields.io/badge/Rust-000000?logo=rust&logoColor=white"/>
<img alt="tauri" src="https://img.shields.io/badge/Tauri%202-24C8DB?logo=tauri&logoColor=white"/>
<img alt="react" src="https://img.shields.io/badge/React%2019-20232A?logo=react&logoColor=61DAFB"/>
<img alt="typescript" src="https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=white"/>
<img alt="duckdb" src="https://img.shields.io/badge/DuckDB-FFF000?logo=duckdb&logoColor=black"/>
<img alt="stars" src="https://img.shields.io/github/stars/SouravRoy-ETL/duckle?style=social"/>
</p>

</div>

---

## Quick links

<table>
<tr>
<td valign="top" width="25%">

**Get started**

- [What is Duckle?](#what-is-duckle)
- [Quickstart (60 s)](#quickstart-60-seconds)
- [Download / Install](#download--install)
- [Build from source](#build-from-source)
- [Run your first pipeline](#run-your-first-pipeline)

</td>
<td valign="top" width="25%">

**Use the product**

- [Meet Duckie (AI)](#meet-duckie---the-local-ai-pipeline-assistant)
- [How to use Duckle](#how-to-use-duckle)
- [Recipes / examples](#recipes-and-examples)
- [In-app Git (GitHub/GitLab)](#git-integration-github--gitlab)
- [Workspace + Git flow](#workspace-and-git-flow)
- [Schedules](#schedules-and-triggers)
- [Server deployment](#server-deployment-build-pipeline)
- [MCP server (Claude / LLM integration)](#mcp-server-connect-claude-or-any-llm-to-duckle)
- [Connection management](#connection-management)
- [Context variables](#context-variables)

</td>
<td valign="top" width="25%">

**Reference**

- [Capabilities matrix](#capabilities)
- [Sources](#sources-74-available)
- [Transforms](#transforms-126-available)
- [Sinks](#sinks-58-available)
- [Data quality](#data-quality-12-available)
- [Custom code](#custom-code-7-available)
- [Control flow](#control-flow-19-available)
- [Advanced settings](#advanced-settings-per-node)
- [Engines](#engines)
- [Configuration](#configuration)

</td>
<td valign="top" width="25%">

**Resources**

- [Architecture](#architecture)
- [Clean data for AI](#clean-data-before-it-reaches-your-ai)
- [Performance tips](#performance-tips)
- [FAQ](#faq)
- [Troubleshooting](#troubleshooting)
- [CI / CD](#ci--cd)
- [Status](#status)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [Sponsor Duckle](SPONSORS.md)
- [License](#license)
- [Releases](https://github.com/SouravRoy-ETL/duckle/releases)
- [Roadmap doc](docs/roadmap.md)
- [Contributing doc](CONTRIBUTING.md)

</td>
</tr>
</table>

---

## What is Duckle?

A visual data pipeline studio that runs on your laptop. Drag sources, transforms, validators, and sinks onto a canvas. Wire them together. Press **Run**. Duckle compiles the graph to SQL and executes it through a real columnar engine, with live previews, generated SQL on every node, and zero hidden state.

Three things make Duckle different from the heavyweights and the toy ETL tools:

1. **An AI assistant that ships in the box.** Describe the pipeline you want in English; Duckie writes the JSON and drops it onto the canvas. The model runs locally - no API key, no telemetry, no cloud round-trip.
2. **290+ connectors at install time.** Files, lakehouses, SQL databases, warehouses, NoSQL, vector DBs, streaming brokers, SaaS REST/GraphQL APIs, even FTP and IMAP - working today, not coming-soon.
3. **A self-contained binary you can audit.** ~65 MB download. Engines install on first launch. Workspaces are plain files in a folder you choose. Diff them, branch them, ship them.

<div align="center">
<img src="docs/assets/flow.svg" alt="Sources flow through 50+ transforms into files, databases, object storage, vector stores, and AI" width="100%"/>
</div>

---

## Meet Duckie - the local AI pipeline assistant

> Describe what you need. Duckie writes the pipeline.

<p align="center">
<img src="docs/assets/real-life-screenshot/duckie.png" alt="Duckie AI Assistant panel open beside a real pipeline on the canvas, showing example prompts and a LOCAL badge" width="100%"/>
</p>

The sidebar on the right is **Duckie AI Assistant** - powered by **Qwen 2.5 Coder 1.5B** running through **llama.cpp**, downloaded once