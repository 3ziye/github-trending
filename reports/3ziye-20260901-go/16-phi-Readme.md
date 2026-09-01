**[English](README.md) | [中文](README.zh-CN.md)**

<p align="center">
  <img src="assets/pixel-text-PHI.png" alt="phi" width="220" style="image-rendering: pixelated; image-rendering: crisp-edges;">
</p>

A minimal terminal coding agent harness in Go — a sibling to Pi.

- **Sub-agents** — spawn isolated jobs and watch the full run unfold in the TUI / job logs, without stuffing every turn into the parent context
- **Hashline edits** — edit by whole-file `@file path#TAG` plus line `LINE#HASH` anchors (same idea as [oh-my-pi](https://github.com/can1357/oh-my-pi)): the model points at anchors instead of rewriting whole files; stale tags/hashes are rejected so over-edits and silent corruption stop here
- **Permission gate** — Gate / Ask before destructive tools fire; safety is not optional when an agent can touch your tree
- **MCP without context death** — configure as many MCP servers as you want; their tool schemas **never** enter the model prompt. The system prompt lists **server names** only (like the Skills catalog); the agent uses three meta-tools (`mcp_list` / `mcp_inspect` / `mcp_call`) to discover and call on demand. Same Gate / Ask / Hooks path as built-in tools. See [MCP](#mcp)
- **Any model** — OpenAI-compatible or Anthropic, no vendor lock-in

<p align="center">
  <a href="https://github.com/pulseaiclub/phi/blob/main/LICENSE"><img src="https://img.shields.io/github/license/pulseaiclub/phi?style=flat&colorA=222222&colorB=58A6FF" alt="License"></a>
  <a href="https://github.com/pulseaiclub/phi/actions"><img src="https://img.shields.io/github/actions/workflow/status/pulseaiclub/phi/ci.yml?style=flat&colorA=222222&colorB=3FB950" alt="CI"></a>
  <a href="https://go.dev"><img src="https://img.shields.io/badge/Go-1.26-00ADD8?style=flat&colorA=222222&logo=go&logoColor=white" alt="Go"></a>
  <a href="https://github.com/pulseaiclub/phi/releases"><img src="https://img.shields.io/github/v/release/pulseaiclub/phi?style=flat&colorA=222222&colorB=8957E5" alt="Release"></a>
  <a href="https://getmerged.abhishekco.de/pulseaiclub/phi"><img src="https://getmerged.abhishekco.de/api/badge/pulseaiclub/phi" alt="GetMerged Scorecard"></a>
</p>

![phi welcome](assets/phi.png)

![phi TUI](assets/image.png)

- [Quick start](#quick-start)
- [Footprint](#footprint)
- [Configuration](#configuration)
- [Interactive mode](#interactive-mode)
- [Commands](#commands)
- [Sessions](#sessions)
- [Headless mode](#headless-mode)
- [Skills](#skills)
- [Permissions](#permissions)
- [Hooks](#hooks)
- [MCP](#mcp)
- [Tools](#tools)
- [Project layout](doc/project-layout.md)

## Quick start

Install the latest release (macOS / Linux):

```sh
curl -fsSL https://raw.githubusercontent.com/pulseaiclub/phi/main/scripts/install.sh | bash
```

Windows (PowerShell 5.1+):

```powershell
irm https://raw.githubusercontent.com/pulseaiclub/phi/main/scripts/install.ps1 | iex
```

First launch needs a model. Open the config editor (creates `~/.phi` layout
and writes `~/.phi/config.yaml`):

```sh
phi config
```

Or set env vars for a one-off run:

```sh
export PHI_MODEL=gpt-4o
export PHI_API_KEY=sk-...
```

Then start the TUI:

```sh
phi
```

Or build from source (Go 1.26.3+, see `go.mod`):

```sh
make build          # produces ./phi
make install        # build and install into $GOBIN
```

On first start, phi automatically creates `~/.phi/{bin,skills,hooks,session}`. Search
tools (`fd`, `rg`) download into `~/.phi/bin` in the background when missing.

The TUI gives the model four core tools — `read`, `write`, `edit`, and
`bash` — plus `grep`, `find`, and `ls`. The model uses these to
fulfill your requests. External HTTP fetch is available via MCP when configured.

## Footprint

phi aims to stay cheap to run and cheap to hack on. Numbers below are for a
stripped release build (`CGO_ENABLED=0`, `-ldflags="-s -w"`), measured on
macOS arm64 unless noted.

| Metric | phi |
| --- | ---: |
| Release binary | **~12 MB** |
| Idle RSS (1 session) | **~21 MB** |
| 10 idle sessions (total RSS) | **~196 MB** (~20 MB each) |
| Time to first frame | **~40 ms** (27–65 ms) |
| Cold `go build` (empty `GOCACHE`) | **~5.5 s** |
| Warm rebuild | **~0.7 s** |
| Go source (excl. tests) | **~22k LOC** / 107 files |
| Go packages | **32** |
| Direct module deps | **6** (15 modules total) |
| Linked runtimes | system libs only (no Node / Electron / Python) |

## Configuration

phi reads `~/.phi/config.yaml` (standard YAML). Environment variables
override it for one-off runs. `phi config` opens an HTML editor for the same
file in your browser.

![phi config](assets/config.png)

```yaml
# ~/.phi/config.yaml
models:
  - name: gpt-4o            # model name; "claude-*" routes to the Anthropic API
    api_key: sk-...         # or set PHI_API_KEY
    base_url: https://api.openai.com/v1   # default; PHI_BASE_URL overrides
    context_window: 128000  # optional
    default: true           # the model used at startup; first entry wins if absent
  - name: claude-sonnet-4-20250514   # extra models; 