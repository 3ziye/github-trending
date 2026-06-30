# agent-compose

[![CI](https://github.com/chaitin/agent-compose/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/chaitin/agent-compose/actions/workflows/ci.yml)
[![Images & Release](https://github.com/chaitin/agent-compose/actions/workflows/images.yml/badge.svg?branch=main)](https://github.com/chaitin/agent-compose/actions/workflows/images.yml)

agent-compose is an experimental control plane for running isolated agent
sessions. It provides a daemon, CLI, Connect APIs, runtime drivers, workspace
provisioning, scheduler automation, event history, and a Jupyter proxy for
notebook-style guest runtimes.

agent-compose is a public preview project: APIs, runtime packaging, deployment
defaults, and operational guidance may still change.

Chinese documentation is available at [docs/zh-CN/README.md](docs/zh-CN/README.md).

## What It Does

- Runs a long-lived daemon that owns state, scheduler execution, runtime
  lifecycle, Connect APIs, and Jupyter proxying.
- Provides a CLI for `up`, `run`, `logs`, `ps`, `down`, and image operations.
- Supports project definitions in `agent-compose.yml`.
- Starts isolated guest runtimes with Docker, BoxLite, or Microsandbox.
- Provisions workspaces from local directories or Git repositories.
- Exposes v1 session-oriented APIs and v2 project/run/image APIs.
- Includes JavaScript runtime components under `runtime/`.

The web UI lives in a separate repository,
[agent-compose-ui](https://github.com/chaitin/agent-compose-ui).

## Maturity

agent-compose is currently suitable for experimentation, local development, and
preview deployments. It is not yet a stable production platform.

Before using it with untrusted workloads, review the runtime driver behavior,
network access, authentication settings, workspace upload limits, and Jupyter
proxy assumptions.

## Repository Layout

```text
cmd/agent-compose/             daemon and CLI entrypoint
pkg/agentcompose/              sessions, projects, loaders, proxy, stores, APIs
pkg/driver/                    Docker, BoxLite, and Microsandbox runtime drivers
pkg/auth/                      authentication middleware and login flows
pkg/config/                    environment configuration
pkg/imagecache/                OCI image cache helpers
proto/                         Connect API definitions and generated Go code
proto-client/                  npm package config for the generated TypeScript client
runtime/                       guest runtime SDKs and JavaScript scheduler runtime
guest-images/                  guest image Dockerfiles
loader-script/                 scheduler script examples and API notes
docs/design/                   design notes
```

## Requirements

- Go toolchain compatible with the version declared in `go.mod`
- Node.js and npm
- Task, for the documented `task ...` commands
- Docker, when using Docker runtime or building Docker images
- Runtime-specific dependencies for BoxLite or Microsandbox when using those
  drivers directly

## Quick Start

Build the CLI and daemon:

```bash
task build
```

Start the daemon:

```bash
agent-compose daemon
```

By default, the daemon listens on a local Unix socket. To expose an HTTP endpoint
for local development:

```bash
HTTP_LISTEN=127.0.0.1:7410 agent-compose daemon
```

Check daemon status:

```bash
agent-compose status
agent-compose --host http://127.0.0.1:7410 status
```

Create an `agent-compose.yml`:

```yaml
name: demo
agents:
  reviewer:
    provider: codex
    model: gpt-test
    image: debian:bookworm-slim
    scheduler:
      triggers:
        - name: hourly
          cron: "0 * * * *"
          prompt: "Review the current workspace state."
```

Apply and run it:

```bash
agent-compose up
agent-compose ps
agent-compose run reviewer --prompt "Review this change"
agent-compose logs --agent reviewer
agent-compose down
```

## CLI

The main commands are:

- `agent-compose daemon`: start the HTTP/Connect daemon.
- `agent-compose up`: read `agent-compose.yml` and apply the project to the daemon.
- `agent-compose run <agent>`: start a project agent run.
- `agent-compose logs`: inspect project run logs.
- `agent-compose ps`: list project agents, recent runs, and active sessions.
- `agent-compose down`: disable managed schedulers and stop running sessions.
- `agent-compose images`, `pull`, `rmi`, `image inspect`: manage daemon-side images.

Useful flags and environment variables:

- `--file, -f`: choose a compose file.
- `--project-name`: override the compose project name.
- `--json`: emit stable JSON for scripts.
- `--host` or `AGENT_COMPOSE_HOST`: connect to a TCP daemon.
- `AGENT_COMPOSE_SOCKET`: choose the local Unix socket path.

## Compose File

Top-level fields:

- `name`: project name. If omitted, the compose file directory name is used.
- `variables`: project variables with `${ENV_NAME}` interpolation.
- `workspace`: default project workspace.
- `agents`: agent definitions keyed by agent name.
- `network.mode`: currently supports `default`.

Common agent 