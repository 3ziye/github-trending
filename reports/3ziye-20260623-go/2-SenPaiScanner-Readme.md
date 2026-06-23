# SenPai Scanner

> **Persian / فارسی:** [README.fa.md](README.fa.md)

[![CI](https://github.com/matinsenpai/senpaiscanner/actions/workflows/ci.yml/badge.svg)](https://github.com/matinsenpai/senpaiscanner/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/matinsenpai/senpaiscanner?style=flat-square)](https://github.com/matinsenpai/senpaiscanner/releases/latest)
[![Go Version](https://img.shields.io/github/go-mod/go-version/matinsenpai/senpaiscanner?style=flat-square)](go.mod)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)
[![Platforms](https://img.shields.io/badge/platform-linux%20%7C%20macOS%20%7C%20windows%20%7C%20android%20%7C%20termux-informational?style=flat-square)](#installation)

<img width="825" height="589" alt="image" src="https://github.com/user-attachments/assets/6558f7b1-bd9d-460a-adf2-d314fe70c48a" />

A Cloudflare IP finder with a terminal UI and an Android app, built for networks where latency is unpredictable and connections drop without warning. Probe Cloudflare edge IPs, optionally validate them through your VLESS or Trojan config with embedded xray — no commands to memorize.

---

## Features

*   **Cloudflare IP Scanning**: Quickly finds working Cloudflare IPs.
*   **Terminal UI (TUI)**: Interactive menu-driven interface, no complex CLI flags.
*   **Multi-Platform**: Linux, macOS, Windows, Android (APK & Termux).
*   **Proxy Validation**: End-to-end testing of IPs using VLESS/Trojan configurations (via embedded Xray).
*   **Neighbor Scan**: Explores nearby IPs in the same Cloudflare block for more hits.
*   **Persistency**: Saves last scan settings automatically.
*   **Clipboard & File Output**: Copy working IPs to clipboard and save to `ips.txt`.

## How it works

Run `senpaiscanner` and you land in a short menu. Navigate with arrow keys and Enter — no scan-related CLI flags.

```
┌────────────────────────────────────────────────────────────┐
│  ▶  Find Working IPs   scan Cloudflare IPs — config optional │
│     Retry Last Scan    retry last scan with previous config  │
│     About                                                │
│     Quit                                                 │
└────────────────────────────────────────────────────────────┘
```

**Find Working IPs** can run in one or two phases:

1.  **Phase 1 — Connectivity scan** probes candidate Cloudflare IPs. Without a config URL it uses a standard HTTP probe; with a URL it derives SNI, host, WebSocket path, and port from your link. SenPai Scanner intelligently parses your VLESS or Trojan configuration URL. In **Random** mode, healthy hits also trigger a **neighbor scan** — nearby addresses in the same Cloudflare block are explored automatically.
2.  **Phase 2 — xray validation** (optional) launches an embedded xray instance and tests the best Phase 1 hits end-to-end through your actual VLESS/Trojan config. Results show endpoint, transport type, download speed, latency (TTFB), and pass/fail status.

Press **`c`** when a scan finishes to copy working `IP:port` endpoints to the clipboard and save them to `ips.txt` next to the binary (or current working directory).

Your last scan settings are saved automatically. Use **Retry Last Scan** on the home screen to repeat the previous run without re-entering anything.

---

## Installation

### Desktop — pre-built binary

Download from the [releases page](https://github.com/matinsenpai/senpaiscanner/releases/latest).

| Platform | Architecture | File |
|---|---|---|
| Linux | x86_64 | `senpaiscanner-linux-amd64` |
| Linux | ARM64 | `senpaiscanner-linux-arm64` |
| Linux | 32-bit x86 | `senpaiscanner-linux-386` |
| macOS | Intel | `senpaiscanner-darwin-amd64` |
| macOS | Apple Silicon | `senpaiscanner-darwin-arm64` |
| Windows | x86_64 | `senpaiscanner-windows-amd64.exe` |
| Windows | 32-bit x86 | `senpaiscanner-windows-386.exe` |

**Linux / macOS:**

```bash
# stable release
curl -fsSL https://github.com/MatinSenPai/SenPaiScanner/raw/refs/heads/main/install.sh | bash

# pre-release
curl -fsSL https://github.com/MatinSenPai/SenPaiScanner/raw/refs/heads/main/install.sh | bash -s -- --prerelease
```

**Windows (PowerShell):**

```powershell
$r = Invoke-RestMethod https://api.github.com/repos/matinsenpai/senpaiscanner/releases/latest
$url = ($r.assets | Where-Object name -eq "senpaiscanner-windows-amd64.exe").browser_download_url
Invoke-WebRequest $url -OutFile senpaiscanner.exe
```

### Android — pre-built APK

Signed release APKs are attached to each GitHub release:

| File pattern | Description |
|---|---|
| `SenPaiScanner-{version}-universal-release.apk` | All ABIs (recommended) |
| `SenPaiScanner-{version}-arm64-v8a-release.apk` | 64-bit ARM only |
| `SenPaiScanner-{version}-armeabi-v7a-release.apk` | 32-bit ARM only |

Install the APK on your device (enable “Install from unknown sources” if needed), grant network permission, and tap **START SCAN** on the home screen.

### Termux (Android terminal)

Run the