# Decionis for Docker

<!-- Badge sweep 2026-08-18: every URL below verified HTTP 200 (rules/discovery.rules.md Rule 1.1),
     with two branch-lifecycle caveats that resolve at merge: the actions.yml badge endpoint
     registers when the workflow reaches the default branch (this README publishes in the same
     merge), and coverage populates on the first master CI run after the codecov upload landed. -->

[![CI](https://github.com/decionis/docker/actions/workflows/actions.yml/badge.svg)](https://github.com/decionis/docker/actions/workflows/actions.yml)
[![License](https://img.shields.io/github/license/decionis/docker)](https://github.com/decionis/docker/blob/master/LICENSE)
[![Go Report Card](https://goreportcard.com/badge/github.com/decionis/docker)](https://goreportcard.com/report/github.com/decionis/docker)
[![Coverage](https://codecov.io/gh/decionis/docker/graph/badge.svg)](https://codecov.io/gh/decionis/docker)
[![Go version](https://img.shields.io/github/go-mod/go-version/decionis/docker)](https://github.com/decionis/docker/blob/master/go.mod)
[![Release](https://img.shields.io/github/v/release/decionis/docker)](https://github.com/decionis/docker/releases)
[![decionis/mcp pulls](https://img.shields.io/docker/pulls/decionis/mcp?label=decionis%2Fmcp%20pulls&logo=docker)](https://hub.docker.com/r/decionis/mcp)
[![desktop-extension pulls](https://img.shields.io/docker/pulls/decionis/desktop-extension?label=desktop-extension%20pulls&logo=docker)](https://hub.docker.com/r/decionis/desktop-extension)

**Deterministic execution authority for AI agents and automated workflows running with Docker.**

Decionis adds an explicit authority boundary between an AI agent's intent and consequential execution.

When an agent attempts a sensitive action—such as deploying infrastructure, modifying production data, publishing a package, invoking a privileged MCP tool, or performing another governed operation—Decionis evaluates the proposed action against deterministic, versioned policy **before execution**.

The result is an explicit decision:

**PROCEED · HOLD · BLOCK**

When policy requires human authority, **Decionis Presence** can request cryptographically verifiable human approval before execution continues.

Every governed decision can produce a signed **Decision Dossier** containing the policy, evidence, reason codes, evaluation metadata, and cryptographic proof behind the decision.

---

## Why Decionis for Docker?

AI coding agents increasingly operate inside containers, development environments, CI/CD pipelines, and MCP-connected toolchains.

They can write code.

They can also:

```text
terraform apply
npm publish
git push --force
docker run --privileged
database.drop
github.create_release
```

The question is no longer only:

> **Can the agent execute this tool?**

It is:

> **Is the agent authorized to execute this action, under this policy, in this context, right now?**

Decionis provides that authority layer.

```text
AI Agent / Automation
        │
        │ proposes action
        ▼
┌──────────────────────┐
│       DECIONIS       │
│  Execution Authority │
│                      │
│ deterministic policy │
└──────────┬───────────┘
           │
    ┌──────┼──────┐
    │      │      │
 PROCEED  HOLD   BLOCK
    │      │
    │      ▼
    │   PRESENCE
    │   Human Authority
    │      │
    │   verified
    │      │
    └──────┴───────────► Execute
                         │
                         ▼
                  Decision Dossier
```

## What this repository provides

`decionis/docker` is the open integration surface for running and experiencing Decionis in Docker-based developer environments.

The project is designed to include:

### Decionis MCP Server

Run **Decionis Execution Authority** as a containerized MCP service for compatible agent environments and MCP clients.

Agents can request deterministic authorization before consequential tool execution and retrieve the resulting Decision Dossier.

### Docker Desktop Extension

A native Docker Desktop experience for observing governed agent activity.

The extension is designed to surface:

- live execution-authority decisions
- PROCEED, HOLD, and BLOCK outcomes
- policy and reason codes
- pending Presence approvals
- policy drift and overrides
- signed Decision Dossiers

### Presence approval

A `HOLD` decision can require human authority before an agent continues.

Presence provides action-bound human verification using supported mechanisms such as passkeys and trusted-device approval.

```text
Agent requests production deployment
              │
              ▼
          Decionis
              │
             HOLD
              │
              ▼
          Presence
              │
       Human approval
              │
              ▼
           PROCEED
              │
              ▼
           Execute
```

The agent does not decide whether human approval is necessary.

**Policy does.**

### Dev Container governance

Decionis can be incorporated into