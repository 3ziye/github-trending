# SenPai Scanner

[![CI](https://github.com/matinsenpai/senpaiscanner/actions/workflows/ci.yml/badge.svg)](https://github.com/matinsenpai/senpaiscanner/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/matinsenpai/senpaiscanner?style=flat-square)](https://github.com/matinsenpai/senpaiscanner/releases/latest)
[![Go Version](https://img.shields.io/github/go-mod/go-version/matinsenpai/senpaiscanner?style=flat-square)](go.mod)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)
[![Platforms](https://img.shields.io/badge/platform-linux%20%7C%20macOS%20%7C%20windows-informational?style=flat-square)](#installation)

A Cloudflare IP finder with a terminal UI, built for networks where latency is unpredictable and connections drop without warning. Paste your VLESS or Trojan config, pick your settings, and let it find IPs that actually work through your proxy — no commands to memorize.

---

## How it works

Run `senpaiscanner` and you land in a short menu. Navigate with arrow keys and Enter — no flags, no subcommands.

```
┌────────────────────────────────────────────────────────────┐
│  ▶  Find Working IPs   paste a config and test CF IPs      │
│     About                                                │
│     Quit                                                 │
└────────────────────────────────────────────────────────────┘
```

**Find Working IPs** runs in two phases:

1. **Phase 1 — Connectivity scan** probes candidate Cloudflare IPs using settings derived from your config URL (SNI, host, WebSocket path, port). It checks trace reachability and, for WebSocket configs, whether a WS-style TLS connection survives DPI.
2. **Phase 2 — xray validation** launches an embedded xray instance and tests the best Phase 1 hits end-to-end through your actual VLESS/Trojan config. Results show endpoint, transport type, download speed, latency (TTFB), and pass/fail status.

When Phase 2 finishes, press **`c`** to copy working `IP:port` endpoints to the clipboard and save them to `ips.txt` next to the binary (or current working directory).

---

## Installation

### Pre-built binary

Download from the [releases page](https://github.com/matinsenpai/senpaiscanner/releases/latest).

| Platform | Architecture | File |
|---|---|---|
| Linux | x86_64 | `senpaiscanner_linux_x86_64.tar.gz` |
| Linux | ARM64 | `senpaiscanner_linux_arm64.tar.gz` |
| macOS | Intel | `senpaiscanner_darwin_x86_64.tar.gz` |
| macOS | Apple Silicon | `senpaiscanner_darwin_arm64.tar.gz` |
| Windows | x86_64 | `senpaiscanner_windows_x86_64.zip` |

**Linux / macOS:**

stable release:
```bash
curl -fsSL https://github.com/MatinSenPai/SenPaiScanner/raw/refs/heads/main/install.sh | bash
```

pre-release:
```bash
curl -fsSL https://github.com/MatinSenPai/SenPaiScanner/raw/refs/heads/main/install.sh | bash -s -- --prerelease
```

**Windows (PowerShell):**
```powershell
$r = Invoke-RestMethod https://api.github.com/repos/matinsenpai/senpaiscanner/releases/latest
$url = ($r.assets | Where-Object name -like "*windows*x86_64*").browser_download_url
Invoke-WebRequest $url -OutFile senpaiscanner.zip
Expand-Archive senpaiscanner.zip .
```

### From source

```bash
go install github.com/matinsenpai/senpaiscanner/cmd/senpaiscanner@latest
```

---

## Usage

```bash
senpaiscanner              # open the TUI
senpaiscanner --version    # print version and exit
senpaiscanner -v           # same
senpaiscanner version      # same
```

Everything else is inside the TUI — there are no scan-related CLI flags.

### Navigation

| Key | Action |
|-----|--------|
| `↑` / `↓` or `k` / `j` | move between rows |
| `←` / `→` or `h` / `l` | move between options within a row |
| `Enter` | select / confirm / start |
| `Esc` | go back |
| `q` | quit from menu; during a scan, cancel or return to menu when finished |

On the **Config URL** row, `←` / `→` move the text cursor; `Ctrl+A` / `Ctrl+E` jump to start / end. Vim keys `h` / `j` / `k` / `l` type normally into the URL field on that row.

---

## Find Working IPs

Paste a **`vless://`** or **`trojan://`** share URL, adjust the setup rows, then start the scan.

### Setup rows (Phase 1)

| Row | Options | Notes |
|---|---|---|
| **Source** | Random / From File | random Cloudflare IPv4 ranges, or read candidates from `ips.txt` |
| **Count** | 1,000 / 5,000 / 20,000 / Custom | IPs to probe in Phase 1; **ignored when Source is From File** |
| **Workers** | 50 / 100 / 200 / Custom | parallel probers (default 50 — safe on restricted networks) |
| **Timeout** | 2s / 3s / 5s / Custom | per-probe deadline (default 5s) |
| **Ports** | Config, 443, 8443, 2053, 2083, 2087, 2096 | multi-select; each IP is tested on every selected port |

Press **Enter** on the last row to continue to the optional config step.

### Optional config (before scan starts)

| Row | Options | Notes |
|---|---|---|
| **Config** | paste URL or leave empty | empty → **Phase 1 only** (standard HTTP probe); with URL → Phas