<div align="center">
  <a href="https://github.com/openfoundry/openfoundry-go">
    <img src="images/logo.png" alt="OpenFoundry" width="420" />
  </a>


  **The Open-Source Data Operating System**

  An open, cloud-native operational data platform for building data products with datasets, ontologies, applications, AI/ML, governance, and observability from one monorepo.

  <p align="center">
    <a href="https://github.com/openfoundry/openfoundry-go/actions/workflows/openfoundry-go.yml"><img src="https://img.shields.io/github/actions/workflow/status/openfoundry/openfoundry-go/openfoundry-go.yml?branch=main&style=for-the-badge&label=Go%20CI" alt="Go CI" /></a>
    <a href="https://github.com/openfoundry/openfoundry-go/actions/workflows/ci-frontend.yml"><img src="https://img.shields.io/github/actions/workflow/status/openfoundry/openfoundry-go/ci-frontend.yml?branch=main&style=for-the-badge&label=Frontend%20CI" alt="Frontend CI" /></a>
    <a href="https://github.com/openfoundry/openfoundry-go/actions/workflows/proto-check.yml"><img src="https://img.shields.io/github/actions/workflow/status/openfoundry/openfoundry-go/proto-check.yml?branch=main&style=for-the-badge&label=Proto%20Check" alt="Proto Check" /></a>
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-AGPL--3.0--only-blue.svg?style=for-the-badge" alt="AGPL-3.0-only license" /></a>
  </p>

  [Documentation](docs/) · [Architecture](ARCHITECTURE.md) · [Contributing](CONTRIBUTING.md) · [Security](SECURITY.md) · [Issues](https://github.com/openfoundry/openfoundry-go/issues)
</div>

---

OpenFoundry is an open-source operational data platform inspired by the capability model of Palantir Foundry, implemented as auditable, extensible software. It combines **50 service directories**, **36 shared libraries**, Protobuf/OpenAPI contracts, generated SDKs, a **React 19 + Vite + TypeScript** web console, and declarative infrastructure for Kubernetes.

The goal is to provide a reproducible foundation for teams that need to connect sources, version datasets, model an ontology, expose APIs, automate workflows, govern access, and operate analytical or AI workloads with end-to-end traceability.

> **Working with this codebase as an AI agent?** Start at [`CLAUDE.md`](CLAUDE.md). It is the canonical onboarding guide for commands, conventions, security-critical zones, and what not to read by default.

## Features & Status

- **Cloud-native architecture:** small Go services, one entrypoint per service, and delivery through Helm, ArgoCD, and Terraform.
- **Ontology at the core:** object types, actions, functions, object views, lineage, and stable contracts for building applications on operational data.
- **Contracts first:** Protobuf as the source of truth, generated OpenAPI, and synchronized TypeScript, Python, and Java SDKs.
- **Integrated governance:** authentication, authorization, Cedar policies, audit, tenancy, SSO/MFA, and egress controls.
- **Observability by default:** `/healthz`, `/metrics`, Prometheus, Grafana, Mimir, structured logs, and OTel traces.
- **Developer platform:** CLI tooling, SDK generation, service templates, VitePress docs, and unit/integration test paths.

| Capability | Status | Capability | Status |
| :-- | :-- | :-- | :-- |
| **Datasets & versioning** | ✅ Available | **Ontology services** | ✅ Available |
| **React web console** | ✅ Available | **Generated SDKs** | ✅ Available |
| **Protobuf/OpenAPI contracts** | ✅ Available | **AuthN/AuthZ foundations** | ✅ Available |
| **Observability stack** | ✅ Available | **Helm/ArgoCD delivery** | ✅ Available |
| **Kafka/NATS integrations** | ✅ Available | **Lakehouse/Iceberg paths** | Under active development |
| **AI/agent runtime services** | Under active development | **Production hardening** | In progress |

## OpenFoundry vs closed data platforms

| Area | OpenFoundry | Closed platforms |
| :-- | :-- | :-- |
| **Control** | Auditable code, contracts, and infrastructure in one monorepo. | Strong provider dependency and less implementation visibility. |
| **Extensibility** | Services, libraries, SDKs, and docs can evolve with your needs. | Extensions are limited by external APIs and vendor roadmaps. |
| **Deployment** | Kubernetes, Helm, ArgoCD, Terraform, and Compose for reproducible environments. | Usually SaaS or managed deployments with less operational control. |
| **Governance** | Policies, audit, and tenancy live beside the platform code. | Governance is coupled to the product and its commercial boundaries. |
| **Developer workflow** | Standard Go, TypeScript, Python, Java, Protobuf, and Makefile workflows. | Proprietary tooling or local workflows that are harder to automate. |

## Quickstart

### 1. Clone the repository

```sh
git clone https://github.com/openfoundry/openfoundry-go.git
cd openfoundry-go
```

### 2. Install development tools

```sh
make tools
```

This installs the Go tools used by the monorepo into `./bin`, including `buf`, `golangci-lint`, `sqlc`, and `gofumpt`