<div align="center">
  <img src="frontend/public/logo.png" alt="CPA-Helper Logo" width="104" height="104" />
  <h1>CPA-Helper</h1>
  <p><strong>A local self-hosted multi-user admin panel for CLIProxyAPI</strong></p>
  <p>Usage analytics · Request tracing · User balances · API key management · Model pricing maintenance · Codex auth file inspection</p>
  <p>
    <strong>English</strong>
    <span> · </span>
    <a href="README.zh-CN.md">中文</a>
  </p>
  <p>
    <a href="https://go.dev/"><img src="https://img.shields.io/badge/Go-1.25+-00ADD8?logo=go&logoColor=white" alt="Go 1.25+" /></a>
    <a href="https://vuejs.org/"><img src="https://img.shields.io/badge/Vue-3.5+-42b883?logo=vuedotjs&logoColor=white" alt="Vue 3.5+" /></a>
    <a href="https://vitejs.dev/"><img src="https://img.shields.io/badge/Vite-5.4+-646cff?logo=vite&logoColor=white" alt="Vite 5.4+" /></a>
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License" /></a>
    <a href="https://linux.do"><img src="https://shorturl.at/ggSqS" alt="LINUX DO" /></a>
  </p>
</div>

---

CPA-Helper is a local self-hosted multi-user administration panel for CLIProxyAPI / CPA users. It centralizes usage analytics, request records, user accounts, API keys, model pricing, available models and Codex auth file inspection.

It separates API keys and usage data by user: each user can create and manage their own keys and inspect their own requests, tokens and cost statistics, while administrators can create or disable regular accounts and review global plus per-user usage. It is built with Go, SQLite, Vue 3 and Vite, with runtime data stored in the root-level `data/` directory by default.

For clarity, model requests initiated by an Agent are still sent directly from that Agent to CPA. CPA-Helper does not proxy or relay those requests; it only calls CPA management-style interfaces such as the usage queue, API key creation and deletion, and credential management for usage views, key management and credential maintenance.

## Table of Contents

- [Features](#features)
- [Screenshots](#screenshots)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Quick Start](#quick-start)
- [Configuration](#configuration)
- [Development and Checks](#development-and-checks)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)
- [License](#license)

## Features

- **Usage analytics and cost estimation**: Track requests, tokens, success rate, latency, model distribution and estimated cost from global, per-user and current-account views.
- **Request record tracing**: Admins can filter global request events by time, user, API key description, provider, model, endpoint and failure state; regular users inspect only their own account records.
- **User and permission management**: Provide administrator and regular-user views; admins can create or disable regular accounts and manage nicknames, login accounts, passwords and roles.
- **User balances and automatic key pause**: Users are unlimited by default; admins can configure monthly balance and lifetime balance, usage is priced in USD with current model prices, monthly balance is consumed first, and exhausted users only have their CPA API keys paused.
- **API key lifecycle management**: Each user can independently create, edit, copy and delete their own API keys and synchronize them to CPA, with usage counted per user and per-key request guidance plus live request testing.
- **Model pricing maintenance**: Maintain token-model input, output and cache prices in USD per million tokens; models whose name contains `image` are charged by a fixed USD price per successful request, with CPA model comparison for quickly filling LiteLLM / manual prices.
- **Card shop index**: Admins can browse real-time public card-shop and product snapshots, search by product title, use popular tags, sort results and favorite shops for faster lookup. This is only a public information index and does not participate in transactions.
- **Available model aggregation**: Query available models through the current account's bound CPA API keys and enrich them with local pricing data.
- **CLIProxyAPI / CPAMC integration**: Configure the service URL, management key, usage queue and local collector options to persist remote usage events into SQLite.
- **Codex auth file inspection**: Support Cron scheduling, quota thresholds, check-only mode, conditional scanning, concurrent workers, priority rules, account enable/disable and deletion.
- **Local-first data storage**: Use SQLite and the `data/` directory by default, with `CPA_HELPER_DATA_DIR` available for overriding the runtime data path.
- **Modern admin interface**: Built with Vue 3, Naive UI, ECharts and lucide icons, with light, dark and system theme modes.

## Screenshots

### Admin

**Usage dashboard**

Admins can inspect global request volume, tokens, cost, trends and distributions by time range, user, model and e