<h1 align="center">Resterm</h1>

<p align="center">
  <em>a terminal-based REST/GraphQL/gRPC client.</em>
</p>

<p align="center">
  <img src="_media/resterm_base.png" alt="Screenshot of resterm TUI base" width="720" />
</p>

<p align="center">
  <strong>split in horizontal view</strong>
</p>

<p align="center">
  <img src="_media/resterm_hsplit.png" alt="Screenshot of resterm TUI in horizontal split" width="720" />
</p>

<p align="center">
  <strong>split panes with response diffing side-by-side</strong>
</p>

<p align="center">
  <img src="_media/resterm_full.png" alt="Screenshot of resterm TUI fulleditor" width="720" />
</p>

<p align="center">
  <strong>Split panes response and profiler</strong>
</p>

<p align="center">
  <img src="_media/resterm_profiler.png" alt="Screenshot of resterm profiler" width="720" />
</p>

<p align="center">
  <strong>Workflow run with step-by-step validation</strong>
</p>

<p align="center">
  <img src="_media/resterm_workflow.png" alt="Screenshot of resterm workflow run" width="720" />
</p>

Resterm is a terminal-first client for working with **HTTP**, **GraphQL**, and **gRPC** services. No cloud sync, no signups, no heavy desktop app. Simple, yet feature rich, terminal client for .http/.rest files.
It pairs a Vim-like-style editor with a workspace explorer, response diff, history, profiler and scripting so you can iterate on requests without leaving the keyboard.

## Highlights
- **Editor** with inline syntax highlighting, search (`Ctrl+F`), clipboard motions, and inline metadata completions (type `@` for contextual hints).
- **Workspace** navigator that filters `.http` / `.rest` files, supports recursion and keeps request lists in sync as you edit.
- **Inline** requests and **curl** import for one-off calls (`Ctrl+Enter` on a URL or curl block).
- **Pretty/Raw/Header/Diff/History** views with optional split panes and pinned comparisons.
- **Variable** scopes, captures, JavaScript hooks, and multi-step workflows with per-step expectations and overrides.
- **GraphQL** helpers (`@graphql`, `@variables`, `@query`) and gRPC directives (`@grpc`, `@grpc-descriptor`, reflection, metadata).
- **Built-in** OAuth 2.0 client plus support for basic, bearer, API key, and custom header auth.
- **Latency** with `@profile` to benchmark endpoints and render histograms right inside the TUI.
- **Multi-step workflows** let you compose several named requests into one workflow (`@workflow` + `@step`), override per-step variables, and review aggregated results in History.

## Installation

### Quick Install

**Linux / macOS:**

```bash
curl -fsSL https://raw.githubusercontent.com/unkn0wn-root/resterm/main/install.sh | bash
```

or with `wget`:

```bash
wget -qO- https://raw.githubusercontent.com/unkn0wn-root/resterm/main/install.sh | bash
```

**Windows (PowerShell):**

```powershell
iwr -useb https://raw.githubusercontent.com/unkn0wn-root/resterm/main/install.ps1 | iex
```

These scripts will automatically detect your architecture, download the latest release, and install the binary.

### Manual Installation

> [!NOTE]
> The manual install helper uses `curl` and `jq`. Install `jq` with your package manager (`brew install jq`, `sudo apt install jq`, etc.).

#### Linux / macOS

```bash
# Detect latest tag
LATEST_TAG=$(curl -fsSL https://api.github.com/repos/unkn0wn-root/resterm/releases/latest | jq -r .tag_name)

# Download the matching binary (Darwin/Linux + amd64/arm64)
curl -fL -o resterm "https://github.com/unkn0wn-root/resterm/releases/download/${LATEST_TAG}/resterm_$(uname -s)_$(uname -m)"

# Make it executable and move it onto your PATH
chmod +x resterm
sudo install -m 0755 resterm /usr/local/bin/resterm
```

#### Windows (PowerShell)

```powershell
$latest = Invoke-RestMethod https://api.github.com/repos/unkn0wn-root/resterm/releases/latest
$asset  = $latest.assets | Where-Object { $_.name -like 'resterm_Windows_*' } | Select-Object -First 1
Invoke-WebRequest -Uri $asset.browser_download_url -OutFile resterm.exe
# Optionally relocate to a directory on PATH, e.g.:
Move-Item resterm.exe "$env:USERPROFILE\bin\resterm.exe"
```

#### From source

```bash
go install github.com/unkn0wn-root/resterm/cmd/resterm@latest
```

## Update

```bash
resterm --check-update
resterm --update
```

The first command reports whether a newer release is available; the second downloads and installs it (Windows users receive a staged binary to swap on restart).

## Quick Start

1. Create or open a directory that contains `.http` / `.rest` files (see `_examples/` for samples). If you want to start right away without any .http - just open resterm...
2. ... or launch Resterm: `resterm --workspace path/to/project` (or if your .http/.rest file is in the same dir. - just type `resterm` and it will be autodiscovered).
3. Pick a request from the sidebar and press `Ctrl+Enter` to send it. Responses appear in the right pane. If you don't have any .http file, just switch to the editor (`Tab`) and type `https://<some_url_dot_