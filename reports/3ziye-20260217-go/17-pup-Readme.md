# [PREVIEW] Pup - Datadog API CLI Wrapper

**NOTICE: This is in Preview mode, we are fine tuning the interactions and bugs that arise. Please file issues or submit PRs. Thank you for your early interest!**

[![CI](https://github.com/DataDog/pup/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/DataDog/pup/actions/workflows/ci.yml)
[![Go Version](https://img.shields.io/badge/go-1.25+-00ADD8?logo=go)](https://go.dev/)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

A Go-based command-line wrapper for easy interaction with Datadog APIs.

## Features

- **Native Go Implementation**: Fast, cross-platform binary
- **OAuth2 Authentication**: Secure browser-based login with PKCE protection
- **API Key Support**: Traditional API key authentication still available
- **Simple Commands**: Intuitive CLI for common Datadog operations
- **JSON Output**: Structured output for easy parsing and automation
- **Dynamic Client Registration**: Each installation gets unique OAuth credentials

## API Coverage

<!-- Last updated: 2026-02-10 | API Client: v2.54.0 -->

Pup implements **38 of 85+ available Datadog APIs** (44.7% coverage).

See [docs/COMMANDS.md](docs/COMMANDS.md) for detailed command reference.

💡 **Tip:** Use Ctrl/Cmd+F to search for specific APIs. [Request features via GitHub Issues](https://github.com/DataDog/pup/issues).

---

<details>
<summary><b>📊 Core Observability (6/9 implemented)</b></summary>

| API Domain | Status | Pup Commands | Notes |
|------------|--------|--------------|-------|
| Metrics | ✅ | `metrics search`, `metrics query`, `metrics list`, `metrics get` | V1 and V2 APIs supported |
| Logs | ✅ | `logs search`, `logs list`, `logs aggregate` | V1 and V2 APIs supported |
| Events | ✅ | `events list`, `events search`, `events get` | Infrastructure event management |
| RUM | ✅ | `rum apps`, `rum sessions`, `rum metrics list/get`, `rum retention-filters list/get` | Apps, sessions, metrics, retention filters (create/update pending) |
| APM Services | ✅ | `apm services`, `apm entities`, `apm dependencies`, `apm flow-map` | Services stats, operations, resources; entity queries; dependencies; flow visualization |
| Traces | ❌ | - | Not yet implemented |
| Profiling | ❌ | - | Not yet implemented |
| Session Replay | ❌ | - | Not yet implemented |
| Spans Metrics | ❌ | - | Not yet implemented |

</details>

<details>
<summary><b>🔔 Monitoring & Alerting (6/9 implemented)</b></summary>

| API Domain | Status | Pup Commands | Notes |
|------------|--------|--------------|-------|
| Monitors | ✅ | `monitors list`, `monitors get`, `monitors delete`, `monitors search` | Full CRUD support with advanced search |
| Dashboards | ✅ | `dashboards list`, `dashboards get`, `dashboards delete`, `dashboards url` | Full management capabilities |
| SLOs | ✅ | `slos list`, `slos get`, `slos create`, `slos update`, `slos delete`, `slos corrections` | Full CRUD plus corrections |
| Synthetics | ✅ | `synthetics tests list`, `synthetics locations list` | Test management support |
| Downtimes | ✅ | `downtime list`, `downtime get`, `downtime cancel` | Full downtime management |
| Notebooks | ✅ | `notebooks list`, `notebooks get`, `notebooks delete` | Investigation notebooks supported |
| Dashboard Lists | ❌ | - | Not yet implemented |
| Powerpacks | ❌ | - | Not yet implemented |
| Workflow Automation | ❌ | - | Not yet implemented |

</details>

<details>
<summary><b>🔒 Security & Compliance (6/9 implemented)</b></summary>

| API Domain | Status | Pup Commands | Notes |
|------------|--------|--------------|-------|
| Security Monitoring | ✅ | `security rules list`, `security signals list`, `security findings search` | Rules, signals, findings with advanced search |
| Static Analysis | ✅ | `static-analysis ast`, `static-analysis custom-rulesets`, `static-analysis sca`, `static-analysis coverage` | Code security analysis |
| Audit Logs | ✅ | `audit-logs list`, `audit-logs search` | Full audit log search and listing |
| Data Governance | ✅ | `data-governance scanner-rules list` | Sensitive data scanner rules |
| Application Security | ❌ | - | Not yet implemented |
| CSM Threats | ❌ | - | Not yet implemented |
| Cloud Security (CSPM) | ❌ | - | Not yet implemented |
| Sensitive Data Scanner | ❌ | - | Not yet implemented |

</details>

<details>
<summary><b>☁️ Infrastructure & Cloud (6/8 implemented)</b></summary>

| API Domain | Status | Pup Commands | Notes |
|------------|--------|--------------|-------|
| Infrastructure | ✅ | `infrastructure hosts list`, `infrastructure hosts get` | Host inventory management |
| Tags | ✅ | `tags list`, `tags get`, `tags add`, `tags update`, `tags delete` | Host tag operations |
| Network | ⏳ | `network flows list`, `network devices list` | Placeholder - API endpoints pending |
| Cloud (AWS) | ✅ | `cloud aws list` | AWS integration management |
| Cloud (GCP) | ✅ | `cloud gcp list` | GCP integration management |
| Cloud (Azure) | ✅ | `cloud azure list`