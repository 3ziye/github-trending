<!--
SPDX-FileCopyrightText: Copyright Hewlett Packard Enterprise Development LP
SPDX-License-Identifier: MIT
-->

<p align="center">
  <img src="docs/assets/pig-project-banner.png" alt="PiG project banner: There are many agent harnesses, but this one is yours. Meet Pi-in-Go.">
</p>

# PiG

[![CI](https://github.com/MichaelKinsy/PiG/actions/workflows/ci.yml/badge.svg)](https://github.com/MichaelKinsy/PiG/actions/workflows/ci.yml)
[![CodeQL](https://github.com/MichaelKinsy/PiG/actions/workflows/security.yml/badge.svg)](https://github.com/MichaelKinsy/PiG/actions/workflows/security.yml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/MichaelKinsy/PiG/badge)](https://scorecard.dev/viewer/?uri=github.com/MichaelKinsy/PiG)
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/14941/badge)](https://www.bestpractices.dev/projects/14941)
[![REUSE status](https://api.reuse.software/badge/github.com/MichaelKinsy/PiG)](https://api.reuse.software/info/github.com/MichaelKinsy/PiG)
[![Go Reference](https://pkg.go.dev/badge/github.com/MichaelKinsy/PiG.svg)](https://pkg.go.dev/github.com/MichaelKinsy/PiG)
[![Minimum Go version](https://img.shields.io/github/go-mod/go-version/MichaelKinsy/PiG?label=Go%20%E2%89%A5)](go.mod)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Latest release](https://img.shields.io/github/v/release/MichaelKinsy/PiG?sort=semver)](https://github.com/MichaelKinsy/PiG/releases)
[![Pi pin 1.0.3](https://img.shields.io/badge/Pi%20pin-1.0.3-8A2BE2)](https://github.com/earendil-works/pi/releases/tag/v1.0.3)
[![Pi port progress](.github/badges/parity-coverage.svg)](test/parity/coverage.md)
[![Follow PiG on X](https://img.shields.io/badge/X-%40PiGCodingAgent-000000?logo=x&logoColor=white)](https://x.com/PiGCodingAgent)
[![Join r/PiGCodingAgent](https://img.shields.io/badge/Reddit-r%2FPiGCodingAgent-FF4500?logo=reddit&logoColor=white)](https://www.reddit.com/r/PiGCodingAgent/)

PiG is [Pi](https://github.com/earendil-works/pi), the minimal and extensible coding agent for the terminal, rebuilt in Go as one native binary. It starts quickly, needs no Node.js, and runs Pi's TypeScript extensions unchanged. You can also write extensions in Go, Rust, or Python, and bundle extensions, skills, and prompts into a Piglet: one named agent you can share or build into its own executable.

PiG is a pre-stable 0.x release. Core paths are ported and checked against Pi 1.0.3 with paired parity scenarios; edge cases are still hardening. See the [port status](test/parity/coverage.md) and [file map](docs/parity/PORT_MAP.md) for current scope and evidence.

If PiG behaves differently from Pi, that is either a bug or a documented divergence. Windows support is a preview.

## Install

On macOS, Linux, or Android with [Termux](docs/site/docs/termux.md) (arm64):

```bash
curl -fsSL https://pi-in-go.dev/install.sh | sh
```

On Windows, in PowerShell:

```powershell
irm https://pi-in-go.dev/install.ps1 | iex
```

With npm, on any supported platform:

```bash
npm install -g @pi-in-go/pig
```

With Go:

```bash
go install github.com/MichaelKinsy/PiG/cmd/pig@latest
```

You can also download an archive from [GitHub Releases](https://github.com/MichaelKinsy/PiG/releases) or [build from source](#build-from-source). [pi-in-go.dev/install](https://pi-in-go.dev/install) covers every method, including updates and uninstalling.

## Quick start

Start PiG in the directory where you want it to work, run `/login` to connect a subscription or set your provider's API key (for example `OPENAI_API_KEY`), then ask it something:

```bash
cd /path/to/project
pig
```

Interactive `/login` masks secret input by default. Turn off **Mask secret input** in `/settings` to restore Pi's plain-text typing and submitted input (D80). See [login privacy](docs/site/docs/providers.md#authentication).

The [documentation](https://pi-in-go.dev/docs/latest) covers everything else, starting with the [quickstart](https://pi-in-go.dev/docs/latest/quickstart). You can also ask PiG to explain itself.

## Upstream Pi

Pi is the reference implementation. PiG follows Pi's behavior and design unless a Go constraint or an approved product-neutral requirement makes a difference necessary.

Use the upstream project for Pi itself:

- [Pi source](https://github.com/earendil-works/pi)
- [Pi documentation](https://pi.dev/docs/latest)
- [Earendil Works](https://github.com/earendil-works)
- [Pi community](https://discord.com/invite/3cU7Bz4UPx)

PiG is not an official Pi release. The Pi maintainers do not endorse PiG.

## Origins

Michael Kinsy created PiG working at Hewlett Packard Enterprise.

PiG is maintained as an independent open-source project. Project decisions, issues, and contributions belong in this repository. See [docs/project/GOVERNANCE.md](docs/project/GOVERNANCE.md) and [docs/project/MAINTAINERS.md](docs/project/MAINTAINERS.md).

## Compatibility philosophy

PiG adds a Go implementation to the Pi ecosystem and