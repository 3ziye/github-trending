# numbat

Endpoint visibility into AI agent activity, with local detection, optional
pre-action blocking, and forensic reconstruction.

numbat observes supported desktop, CLI, IDE, and gateway agents through local
hooks and plugins, OTLP/HTTP logs, and on-disk session artifacts. Live and
at-rest activity is normalized into one event model and evaluated by the same
CEL rule engine. Detection runs locally; records can be written to stdout or a
local file and optionally delivered over HTTP.

The [coverage matrix](docs/agent-coverage.md#matrix) is authoritative for each
host and surface. Blocking is off by default and limited to supported
synchronous pre-action hooks; see the [enforcement guide](docs/enforcement.md).

## Features

- **Live monitoring** through hooks, plugins, and OTLP/HTTP log exporters.
- **Endpoint-local detection** with built-in CEL rules, multi-step sequence rules,
  and custom YAML rules.
- **Opt-in blocking** through supported pre-action hooks. Enforce mode is
  disabled by default and applies only to rules marked `enforce: true`; all
  shipped rules are monitor-only.
- **Forensic reconstruction** from supported on-disk session artifacts, without
  prior numbat instrumentation.
- **Versioned NDJSON records** for events, findings, enforcement decisions,
  indicators, and scan summaries. Events and findings retain source references;
  [JSON Schemas](docs/schema/v0.3.0/) define the wire format.
- **Read-only artifact scanning** with secret redaction. Normal record output
  never includes a complete raw transcript; adding raw evidence files to a case
  bundle is opt-in.
- **Inventory and investigation tools** for read-only agent discovery,
  per-session timelines, and portable case bundles with SHA-256 manifests.
- **Single-binary distribution** for macOS, Linux, and Windows, built without
  cgo.

## Quick start

### Install

[Download a release](https://github.com/perplexityai/numbat/releases) for macOS, Linux,
or Windows on amd64 or arm64. Each release includes SHA-256 checksums. You can
also install with Go 1.26.6 or newer:

```
go install github.com/perplexityai/numbat/cmd/numbat@latest
```

<details>
<summary>Build a static binary from a checkout</summary>

macOS or Linux:

```
CGO_ENABLED=0 go build -trimpath -o numbat ./cmd/numbat
```

Windows PowerShell:

```powershell
$env:CGO_ENABLED = "0"
go build -trimpath -o numbat.exe ./cmd/numbat
```

</details>

### Inventory and scan

These read-only commands do not install hooks or change agent configuration:

```
numbat agents
# scan all discovered parser-backed agents
numbat scan
# or limit automatic discovery to Codex
numbat scan --agent codex
```

### Monitor and enforce

Install live monitoring for any agent with
[live-capture support](docs/agent-coverage.md#matrix); the commands below use
Codex as a concrete example. Hooks start in monitor-only mode. `--emit all`
writes events, findings, indicators, and applicable enforcement decisions to
`~/.numbat/records.ndjson`.

```
numbat hook install --agent codex --emit all
numbat hook status --agent codex
```

> **Hook trust:** Requirements vary by agent and scope. For the Codex user hook
> above, review and trust its current definition in `/hooks` (CLI) or
> Settings > Hooks (app), including after changes such as `--enforce`. Codex
> hooks installed with `--managed` are trusted by policy. `hook status` verifies
> configuration, not execution or delivery. See the
> [deployment guide](docs/deployment.md#hook-trust-and-activation) for other
> agents and scopes.

All shipped rules are monitor-only. To enforce a detection, copy its complete
[shipped YAML](rules/) into a controlled operator directory, keep the same id,
add `enforce: true`, and bump its version. Validate and install that effective
policy for a supported pre-action hook:

```
numbat rules check --rules-dir ./numbat-policy
numbat hook install --agent codex --emit all \
  --rules-dir ./numbat-policy --enforce
```

### Example output

<details>
<summary><strong>Hook event</strong> (OpenClaw cloud-metadata browser request)</summary>

A controlled OpenClaw `before_tool_call` callback passed through numbat's
generated plugin becomes a typed network event with its proposed destination
and execution context. It also matches the high-severity cloud-metadata rule.

```json
{
  "actor": "assistant",
  "confidence": "medium",
  "content_preview": "http://169.254.169.254/latest/meta-data/iam/security-credentials/",
  "endpoint": {
    "hostname": "developer-workstation", "os": "linux", "arch": "arm64",
    "username": "node", "uid": "1000"
  },
  "event_id": "hook-run-20260724T151125.690671167-fa0a4148090fa1ba",
  "event_type": "network.indicator",
  "evidence": {"artifact_type": "hook"},
  "project_path": "/workspace/acme-api",
  "record_type": "event",
  "run_id": "run-20260724T151125.690671167-fa0a4148090fa1ba",
  "schema_version": "0.3.0",
  "session_id": "agent:research:metadata-review",
  "source_agent": "openclaw",
  "source_type": "hook",