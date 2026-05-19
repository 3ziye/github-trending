# 🦀 📦 Crabbox

[![CI](https://github.com/openclaw/crabbox/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/openclaw/crabbox/actions/workflows/ci.yml)
[![Release](https://github.com/openclaw/crabbox/actions/workflows/release.yml/badge.svg)](https://github.com/openclaw/crabbox/actions/workflows/release.yml)
[![Latest release](https://img.shields.io/github/v/release/openclaw/crabbox?sort=semver)](https://github.com/openclaw/crabbox/releases/latest)

**Warm a box, sync the diff, run the suite.**

Crabbox is an open-source agent workspace control plane for maintainers and AI
agents. Lease fast managed cloud capacity, point at an existing SSH host, or use
an agent sandbox provider, then sync your dirty checkout, run commands remotely,
stream output, collect evidence, and release. Local edit-save-run loop,
cloud-grade compute, agent-ready observability.

```sh
crabbox run -- pnpm test
```

Behind that single command: a Go CLI on your laptop, a Cloudflare Worker broker
that owns provider credentials and lease state, and a managed or delegated
runner.

Supported providers:

- [AWS EC2](docs/providers/aws.md) (`provider: aws`): brokered or direct Linux,
  native Windows, Windows WSL2, and EC2 Mac.
- [Azure](docs/providers/azure.md) (`provider: azure`): brokered or direct
  Linux, native Windows, and Windows WSL2 VMs.
- [Google Cloud](docs/providers/gcp.md) (`provider: gcp`): brokered or direct
  Linux Compute Engine VMs.
- [Hetzner Cloud](docs/providers/hetzner.md) (`provider: hetzner`): brokered or
  direct Linux VMs.
- [Proxmox](docs/providers/proxmox.md) (`provider: proxmox`): direct Linux QEMU
  VM clones from private Proxmox VE templates.
- [Static SSH](docs/providers/ssh.md) (`provider: ssh`): existing Linux, macOS,
  Windows, or WSL2 hosts.
- [exe.dev](docs/providers/exe-dev.md) (`provider: exe-dev`): exe.dev VMs
  exposed as normal SSH leases.
- [Blacksmith Testbox](docs/providers/blacksmith-testbox.md)
  (`provider: blacksmith-testbox`): delegated Testbox lifecycle and execution.
- [Namespace Devbox](docs/providers/namespace-devbox.md)
  (`provider: namespace-devbox`): Namespace-managed Devboxes over SSH.
- [Semaphore CI testbox](docs/providers/semaphore.md) (`provider: semaphore`):
  Semaphore jobs leased as SSH testboxes.
- [Sprites](docs/providers/sprites.md) (`provider: sprites`): Sprites
  microVMs exposed as SSH leases through `sprite proxy`.
- [Daytona](docs/providers/daytona.md) (`provider: daytona`): Daytona
  SDK/toolbox sandbox execution.
- [Islo](docs/providers/islo.md) (`provider: islo`): delegated Islo sandbox
  execution.
- [E2B](docs/providers/e2b.md) (`provider: e2b`): delegated E2B sandbox
  execution.
- [Modal](docs/providers/modal.md) (`provider: modal`): delegated Modal
  Sandbox execution through the local Python client.
- [Tensorlake](docs/providers/tensorlake.md) (`provider: tensorlake`):
  delegated Tensorlake Firecracker sandbox execution through the Tensorlake CLI.
- [Cloudflare](docs/providers/cloudflare.md)
  (`provider: cloudflare`): delegated Cloudflare execution through a Worker and
  container runner.
- [Railway](docs/providers/railway.md) (`provider: railway`): delegated
  redeploy-and-stream execution against a pre-existing Railway service through
  the [Railway](https://railway.com) GraphQL API.

---

## Install

```sh
brew install openclaw/tap/crabbox
crabbox --version
```

No Homebrew? Grab a [GoReleaser archive](https://github.com/openclaw/crabbox/releases) for macOS, Linux, or Windows.

Prerequisites on the laptop: `git`, `ssh`, `ssh-keygen`, `rsync`, `curl`.

## Quick start

The hosted broker at `https://crabbox.openclaw.ai` is restricted to the
configured GitHub org/team. If `crabbox login` completes GitHub OAuth and then
returns an org-membership error, use direct-provider mode for a personal cloud
account or self-host the Worker broker with your own provider credentials and
spend caps. See [Getting started](docs/getting-started.md#hosted-broker-access)
and [Infrastructure](docs/infrastructure.md#self-hosted-broker-minimum) for the
setup paths.

```sh
# log in once per machine (stores a broker token in user config)
crabbox login

# verify local prerequisites and broker reachability
crabbox doctor

# one-shot: lease, sync, run, release
crabbox run -- pnpm test

# named repo workflow from .crabbox.yaml
crabbox job run full-ci

# or warm a box once, then reuse it
crabbox warmup                                       # prints cbx_... + a slug
crabbox run --id blue-lobster -- pnpm test:changed
crabbox ssh --id blue-lobster
crabbox stop blue-lobster
```

Every lease has a stable `cbx_...` ID and a friendly crustacean slug (`blue-lobster`, `swift-hermit`, …). Either works wherever an `--id` is accepted. Use `--slug <name>` on fresh leases when a specific reusable slug helps, and `--label <text>` on `run` when the history entry needs a human-readable name.

## How it works

```text
your laptop                Cloudflare Worker            cloud provider
----