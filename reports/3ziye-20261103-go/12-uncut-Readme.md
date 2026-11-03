<div align="center">
  <img src="assets/logo.svg" alt="UNCUT logo" width="112">
  <h1>UNCUT</h1>
  <p><strong>The lossless, headless coding agent harness.</strong></p>
  <p>One 7 MB static binary, four tools, plain stdin/stdout.<br>No TUI. No telemetry. No silent context cuts.</p>
  <p>Linux · macOS · Windows · amd64 + arm64 · MIT</p>
  <p><a href="https://balanov.pro/uncut/">Landing page: balanov.pro/uncut</a></p>
</div>

[![CI](https://github.com/Balanov/uncut/actions/workflows/ci.yml/badge.svg)](https://github.com/Balanov/uncut/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/Balanov/uncut)](https://github.com/Balanov/uncut/releases/latest)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Go](https://img.shields.io/badge/Go-1.26%2B-00ADD8?logo=go&logoColor=white)](go.mod)

UNCUT is a tiny coding-agent harness for shell pipelines, CI jobs, containers, and agent experiments. It deliberately has no TUI, telemetry, plugin system, background agents, automatic retries, or context compaction.

The entire conversation is sent on every model call. File contents and combined command output are never truncated by UNCUT. If the provider cuts a response at its output limit, UNCUT exits with an error instead of presenting a partial answer as success. [Run the proof yourself](bench/README.md) or inspect the [recorded measurements](BENCHMARKS.md).

## Why UNCUT?

- **Lossless by default.** No summarization, pruning, sliding windows, or silent output caps.
- **Headless only.** Final text goes to stdout; structured NDJSON events are available with `--json`.
- **Small and portable.** One statically linked Go binary, no runtime or third-party Go dependencies.
- **Provider neutral.** Works with OpenAI-compatible Chat Completions endpoints, including local servers.
- **Resumable.** Optional append-only JSONL sessions preserve every message and tool result.
- **Forkable.** 837 lines of implementation Go, four tools, one provider protocol, one agent loop, MIT license.

## Install

### Linux

```sh
VERSION=0.1.1
ARCH=amd64  # Use arm64 on ARM64.
curl -fSLo uncut "https://github.com/Balanov/uncut/releases/download/v${VERSION}/uncut-linux-${ARCH}"
mkdir -p "$HOME/.local/bin"
install -m 0755 uncut "$HOME/.local/bin/uncut"
export PATH="$HOME/.local/bin:$PATH"
uncut --version
```

Make sure `$HOME/.local/bin` is on your `PATH`.

### macOS

```sh
VERSION=0.1.1
ARCH=arm64  # Use amd64 on Intel.
curl -fSLo uncut "https://github.com/Balanov/uncut/releases/download/v${VERSION}/uncut-darwin-${ARCH}"
mkdir -p "$HOME/.local/bin"
install -m 0755 uncut "$HOME/.local/bin/uncut"
export PATH="$HOME/.local/bin:$PATH"
uncut --version
```

### Windows PowerShell

```powershell
$Version = "0.1.1"
$Arch = "amd64"  # Use arm64 on ARM64.
$Dest = "$env:LOCALAPPDATA\Programs\UNCUT"
New-Item -ItemType Directory -Force $Dest | Out-Null
Invoke-WebRequest -Uri "https://github.com/Balanov/uncut/releases/download/v$Version/uncut-windows-$Arch.exe" -OutFile "$Dest\uncut.exe"
$env:Path = "$Dest;$env:Path"
uncut --version
```

Add `$Dest` to your user `PATH` to make UNCUT available in future terminals.

### Checksums and OS warnings

Every release includes `checksums.txt`. For example, verify a Linux download with:

```sh
VERSION=0.1.1
ARCH=amd64
curl -fSLO "https://github.com/Balanov/uncut/releases/download/v${VERSION}/checksums.txt"
grep "uncut-linux-${ARCH}$" checksums.txt | sha256sum -c -
```

The binaries are not code-signed yet, so SmartScreen or Gatekeeper may warn. Verify the SHA-256 checksum before allowing a downloaded executable. On macOS, after verification, remove quarantine from this file only:

```sh
xattr -d com.apple.quarantine "$HOME/.local/bin/uncut"
```

You can also build from source instead.

### Go install and source builds

With Go 1.26+:

```sh
go install github.com/Balanov/uncut/cmd/uncut@latest
```

Or build a checkout:

```sh
git clone https://github.com/Balanov/uncut.git
cd uncut
go build -trimpath -ldflags="-s -w" -o bin/uncut ./cmd/uncut
```

On Windows, use `bin/uncut.exe` as the output path.

## Quick start

Set a model and API key:

```sh
export UNCUT_API_KEY="your-api-key"
export UNCUT_MODEL="your-model-id"
uncut "Inspect this repository and fix the failing tests"
```

For an OpenAI-compatible provider, also set its base URL:

```sh
export UNCUT_BASE_URL="https://openrouter.ai/api/v1"
```

For a local Ollama server with an installed tool-capable model (this exact setup was smoke-tested with `qwen3:8b`):

```sh
ollama pull qwen3:8b
export UNCUT_BASE_URL="http://localhost:11434/v1"
export UNCUT_MODEL="qwen3:8b"
uncut "Explain this repository"
```

No API key is required by default for local endpoints. In PowerShell, set variables with `$env:UNCUT_BASE_URL = "..."` and `$env:UNCUT_MODEL = "..."`. Replace the example model with one actually installed on your machine; tool-call behavior depends on the model.

### Unix pipelines

```sh
git diff | uncut "Review this diff. Do 