
![AI demo to real app with Nubase](brand/ai-demo-to-real-app-en.png)

# Nubase

**English** · [简体中文](README.zh-CN.md)

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-10A074.svg)](LICENSE)
[![npm](https://img.shields.io/npm/v/nubase_cli?logo=npm&label=nubase_cli&color=cb3837)](https://www.npmjs.com/package/nubase_cli)
[![GitHub stars](https://img.shields.io/github/stars/OtterMind/Nubase?style=social)](https://github.com/OtterMind/Nubase)

**Turn AI-written code into real apps.** Nubase is an open-source, AI-native backend **and deploy layer** that a coding agent drives directly — so a generated app goes live in minutes. Eight capability modules in one self-hostable service: **Database, Auth, Storage, Assets, Functions, AI Gateway, Memory, and cron**.

> An agent can model the data (Database + Auth), deploy backend logic (**Functions**), publish the generated frontend to a public CDN (**Assets**), and schedule recurring work (**cron**) — all through MCP tools, with no separate hosting account. Supabase-style where it makes sense (Postgres, REST, JWTs, RLS, object storage, a Studio dashboard), plus first-class **Memory** and an **MCP** surface built for AI coding agents.

---

## ⚡ Quick Start

### 1. Use Nubase in Claude Code or Codex — one command

From your project folder, run:

```bash
npx -y nubase_cli@latest install-skills
```

That single command:

- 📚 installs the **Nubase skills** for **both Claude Code and Codex**,
- 🔌 wires up the **MCP server** config, and
- 🔐 opens a browser to **authorize** and pick your project.

Then:

- **Claude Code** — restart it in this folder, run `/mcp`, and confirm `nubase` is connected.
- **Codex** — it's added to `~/.codex/config.toml`; just start Codex.

> This connects your agent to a Nubase instance (a hosted one, or your own — spin one up in step 2). Point the CLI at any instance with:
> ```bash
> npx -y nubase_cli@latest install-skills \
>   --studio-url https://studio.example.com \
>   --nubase-url https://api.example.com
> ```

### 2. Run your own Nubase — one command

The all-in-one Docker image bundles **PostgreSQL + Redis + the backend + Studio**:

```bash
docker run -d --name nubase \
  -p 9999:9999 -p 5432:5432 \
  -v nubase_data:/data \
  <your-namespace>/nubase:latest
```

- **Studio** → http://localhost:9999/studio — create an account, create a project, click **Provision** to initialize its database.
- **API** → http://localhost:9999 (the Studio UI is bundled into the backend and served on the same port)

> First-boot secrets are generated into the `/data` volume; keep the volume to retain your projects. For a real deployment with stable secrets, see [Self-host with Docker](#-self-host-with-docker).

### 3. Build with your agent

Your agent can now operate Nubase directly through MCP tools — inspect schema, create tables, run SQL, manage auth & storage, **deploy edge functions, publish a frontend to the public CDN, schedule cron jobs**, and read/write durable **memory**. Try asking:

> "Create a `todos` table with RLS, deploy an edge function that returns the open count, publish a one-page UI to Assets that calls it, and remember the deployment."

See [Deploy an AI-generated app](docs/deploy-ai-generated-apps.md) for the full generate → live walkthrough.

---

## 🚀 Self-host with Docker

The single all-in-one image is everything you need to run Nubase on your own box — **one line, no compose file, no external services**.

**Try it (auto-generated secrets, kept in the volume):**

```bash
docker run -d --name nubase -p 9999:9999 -p 5432:5432 \
  -v nubase_data:/data <your-namespace>/nubase:latest
```

**Production (pin stable secrets so encrypted project credentials survive restarts):**

```bash
docker run -d --name nubase -p 9999:9999 -p 5432:5432 \
  -v nubase_data:/data \
  -e PGRST_ENCRYPTION_MASTER_KEY="$(openssl rand -base64 32)" \
  -e METADATA_SERVICE_ROLE_KEY="$(openssl rand -base64 48)" \
  <your-namespace>/nubase:latest
```

Everything else is configured via environment variables — Postgres, Redis, S3/R2 storage, SMTP, OAuth, and LLM providers. See [docs/docker-all-in-one.md](docs/docker-all-in-one.md) for the full list and a multi-architecture (`amd64` + `arm64`) note.

> Replace `<your-namespace>` with the Docker Hub namespace the image is published under.

---

## Why Nubase

AI-native applications need more than CRUD. They need user memory, retrieval, auth, storage, database APIs, and project isolation from day one. Without that backend layer, every AI coding session produces another demo that still needs weeks of infrastructure work.

Supabase is excellent, but its open-source self-hosted stack is designed around a **single** project. Nubase is built for AI teams and self-hosters who want **one Studio, one backend service, and many isolated AI projects** on their own infrastructure — with three opinionated additions:

1. **Memory is a first-class primitive** — durable memory, entity extraction, history, and hybrid 