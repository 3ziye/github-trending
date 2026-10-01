<p align="center">
  <a href="https://lockedinlabs.ai">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="docs/brand/lockup-on-dark.svg">
      <img src="docs/brand/lockup-on-light.svg" alt="LockedIn Labs" width="360">
    </picture>
  </a>
</p>

<h1 align="center">Agent Console</h1>

<p align="center">
  <a href="https://github.com/LockedinLabs-AI/agent-console/actions/workflows/ci.yml"><img alt="CI" src="https://img.shields.io/github/actions/workflow/status/LockedinLabs-AI/agent-console/ci.yml?branch=main&label=CI"></a>
  <a href="https://scorecard.dev/viewer/?uri=github.com/LockedinLabs-AI/agent-console"><img alt="OpenSSF Scorecard" src="https://api.scorecard.dev/projects/github.com/LockedinLabs-AI/agent-console/badge"></a>
  <a href="https://www.bestpractices.dev/projects/14979"><img alt="OpenSSF Best Practices" src="https://www.bestpractices.dev/projects/14979/badge"></a>
  <a href="https://github.com/LockedinLabs-AI/agent-console/releases/latest"><img alt="Latest release" src="https://img.shields.io/github/v/release/LockedinLabs-AI/agent-console"></a>
  <a href="https://nodejs.org"><img alt="Node.js 22 or newer" src="https://img.shields.io/badge/node-%3E%3D22-339933"></a>
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/github/license/LockedinLabs-AI/agent-console"></a>
</p>

<p align="center">
  <b>Agent Console by <a href="https://lockedinlabs.ai">LockedIn Labs</a> — open-source, local-first observability for AI coding agents.</b><br>
  Every Claude Code and Codex session's tokens, cache reads and writes, models and list-price cost,
  on this computer and on every computer you connect, in one local console.
</p>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/console-demo-dark.png">
  <img src="docs/console-demo-light.png" alt="Agent Console in demo mode: sessions, machines, token usage and estimated costs. All figures are synthetic.">
</picture>

*Captured from `--demo`. Every figure in it is generated and stamped DEMO.
[The same screen in the light theme.](docs/console-demo-light.png)*

[Get started](#install) · [Documentation](docs/README.md) ·
[Architecture](docs/ARCHITECTURE.md) · [Security](SECURITY.md) ·
[Contribute](CONTRIBUTING.md) · [Changelog](CHANGELOG.md)

| | |
|---|---|
| **Local-first** | Reads the agents' own transcripts on your machines. No telemetry, no update check, no crash reporting — see [data flows](docs/security/DATA-FLOWS.md). |
| **Every machine, one view** | Join laptops, build boxes and servers to a self-hosted team hub; each machine keeps its own lanes and nothing is counted twice. |
| **Gateway and telemetry aware** | Optional ingest of Claude Code OpenTelemetry and Kong or LiteLLM token metrics, a Prometheus `/metrics` endpoint and a [Grafana dashboard](docs/grafana-agent-console.json). |
| **Honest numbers** | Estimates say they are estimates; unknown readings are shown as unknown, never as zero. |
| **Safe to present** | Presenting mode (P) replaces every project, machine and person with a stand-in name. |
| **Verifiable supply chain** | Apple-signed and notarized macOS builds, `SHA256SUMS`, signed build attestations and, from 0.4.1, a CycloneDX SBOM on every release ([verify one](#verify-a-release)); [threat model](docs/security/THREAT-MODEL.md), [NIST SSDF mapping](docs/security/SSDF.md) and an [enterprise security FAQ](docs/security/ENTERPRISE-FAQ.md). |

**Installing with Claude Code or Codex?** Give it this repository's URL and ask
it to follow [INSTALL.md](INSTALL.md). The same guide works if you prefer to
install it yourself: choose the current source, an npm archive, or a standalone
download, then verify the version and open the console.

This page describes **v0.4.1**, published as the
[v0.4.1 release](https://github.com/LockedinLabs-AI/agent-console/releases/tag/v0.4.1)
and as the source on `main`. Run from source to use the current console:

```sh
git clone https://github.com/LockedinLabs-AI/agent-console.git
cd agent-console
node bin/agent-console.mjs --open
```

You need Git and Node.js 22 or newer, or use [Download ZIP](#start-here)
instead of Git. There is no account to create, no package install and no build
step. The command runs this checkout, reads the Claude Code and Codex history already on
this computer, and opens the console in your browser, signed in, normally at
`http://127.0.0.1:6787`. To look around first without reading anything of
yours, add `--demo` before `--open`.

**In the first thirty seconds you see:** the last 24 hours of tokens (or the
last hour, 7 days or 30 days), split into cache read, cache write, output and
uncached input; their list-price estimate;
burn right now, in tokens per minute and dollars per hour; one lane per
session with its model, its subagents and its last hour of activity; and every
machine and person reporting, each with a share of the total.

**Nothing leaves a machine but counts.** Only model ids, minute timestamps,
token counts and salted