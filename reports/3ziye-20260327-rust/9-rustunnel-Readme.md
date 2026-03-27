# rustunnel

[![CI](https://github.com/joaoh82/rustunnel/actions/workflows/ci.yml/badge.svg)](https://github.com/joaoh82/rustunnel/actions/workflows/ci.yml)
[![License: AGPLv3](https://img.shields.io/badge/License-AGPLv3-blue.svg)](LICENSE)
[![Rust](https://img.shields.io/badge/rust-1.76%2B-orange.svg)](https://www.rust-lang.org)

![rustunnel logo](images/rustunnel-logo-light.png)

A ngrok-style secure tunnel server written in Rust. Expose local services through a public server over encrypted WebSocket connections with TLS termination, HTTP/TCP proxying, a live dashboard, Prometheus metrics, and audit logging.

You can self-host or use our managed service.

---

## Table of Contents

- [Hosted service](#hosted-service)
- [Architecture overview](#architecture-overview)
- [Requirements](#requirements)
- [Local development setup](#local-development-setup)
  - [Build](#build)
  - [Run tests](#run-tests)
  - [Run the server locally](#run-the-server-locally)
  - [Run the client locally](#run-the-client-locally)
  - [Git hooks](#git-hooks)
- [Production deployment (Ubuntu / systemd)](#production-deployment-ubuntu--systemd)
  - [1 — Install dependencies](#1--install-dependencies)
  - [2 — Build release binaries](#2--build-release-binaries)
  - [3 — Create system user and directories](#3--create-system-user-and-directories)
  - [4 — Install the server binary](#4--install-the-server-binary)
  - [5 — Create the server config file](#5--create-the-server-config-file)
  - [6 — TLS certificates (Let's Encrypt + Cloudflare)](#6--tls-certificates-lets-encrypt--cloudflare)
  - [7 — Set up systemd service](#7--set-up-systemd-service)
  - [8 — Open firewall ports](#8--open-firewall-ports)
  - [9 — Verify the server is running](#9--verify-the-server-is-running)
  - [Updating the server](#updating-the-server)
- [Docker deployment](#docker-deployment) · [full guide](docs/docker-deployment.md)
- [Client configuration](#client-configuration)
  - [Installation](#installation)
  - [Setup wizard](#setup-wizard)
  - [Quick start (CLI flags)](#quick-start-cli-flags)
  - [Config file](#config-file)
  - [Token management](#token-management)
- [Port reference](#port-reference)
- [Config file reference (server)](#config-file-reference-server)
- [REST API](#rest-api)
- [AI agent integration (MCP server)](#ai-agent-integration-mcp-server)
  - [OpenClaw skill](#openclaw-skill)
- [Monitoring](#monitoring)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Hosted service

You can use rustunnel without running your own server. We operate a global fleet of public edge servers that you can connect to immediately.

### Available regions

| Region ID | Server | Location | Control plane | Status |
|-----------|--------|----------|---------------|--------|
| `eu` | `eu.edge.rustunnel.com` | Helsinki, FI | `:4040` | Live |
| `us` | `us.edge.rustunnel.com` | Hillsboro, OR | `:4040` | Live |
| `ap` | `ap.edge.rustunnel.com` | Singapore | `:4040` | Live |

The client auto-selects the nearest region by default. Use `--region <id>` to connect to a specific one. The legacy address `edge.rustunnel.com` is a CNAME to `eu.edge.rustunnel.com` and will continue to work for backward compatibility.

### Getting an auth token

Access to the hosted service requires an auth token. To request one:

1. Open a [GitHub Issue](https://github.com/joaoh82/rustunnel/issues/new) titled **"Token request"**
2. Include your **email address** or **Discord username** in the body
3. We will send you a token privately

Tokens are issued manually for now while the service is in early access.

### Quick start with the hosted server

Once you have a token, run the setup wizard:

```bash
rustunnel setup
# Tunnel server address [edge.rustunnel.com:4040]: (press Enter)
# Auth token: <paste your token>
# Region [auto / eu / us / ap] (default: auto): (press Enter)
```

Then expose a local service:

```bash
# HTTP tunnel — auto-selects the nearest region
rustunnel http 3000

# Connect to a specific region
rustunnel http 3000 --region eu

# Custom subdomain
rustunnel http 3000 --subdomain myapp

# TCP tunnel — e.g. expose a local database
rustunnel tcp 5432
```

The client prints the public URL as soon as the tunnel is established:

```
  Selecting nearest region… eu 12ms · us 143ms · ap 311ms → eu (Helsinki, FI) 12ms
✓ tunnel open  https://abc123.eu.edge.rustunnel.com
```

---

## Architecture overview

![rustunnel architecture](images/rustunnel_architecture.png)

```
                        ┌──────────────────────────────────────────┐
                        │           rustunnel-server               │
                        │                                          │
Internet ──── :80 ─────▶│  HTTP edge (301 → HTTPS)                 │
Internet ──── :443 ────▶│  HTTPS edge  ──▶ yamux stream ──▶ client │
Client ───── :4040 ────▶│  Control-plane WebSocket (TLS)           │
Browser ──── :8443 ────▶│  Dashboard UI + REST API               