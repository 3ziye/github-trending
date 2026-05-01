# sni-spoof-rs

[![Release](https://img.shields.io/github/v/release/therealaleph/sni-spoofing-rust)](https://github.com/therealaleph/sni-spoofing-rust/releases/latest)
[![Total Downloads](https://img.shields.io/github/downloads/therealaleph/sni-spoofing-rust/total?label=total%20downloads)](https://github.com/therealaleph/sni-spoofing-rust/releases)
[![Latest Downloads](https://img.shields.io/github/downloads/therealaleph/sni-spoofing-rust/latest/total?label=latest%20release)](https://github.com/therealaleph/sni-spoofing-rust/releases/latest)
[![Stars](https://img.shields.io/github/stars/therealaleph/sni-spoofing-rust?style=flat)](https://github.com/therealaleph/sni-spoofing-rust/stargazers)
[![License](https://img.shields.io/github/license/therealaleph/sni-spoofing-rust)](LICENSE)

Rust implementation of [patterniha's SNI-Spoofing](https://github.com/patterniha/SNI-Spoofing) DPI bypass technique. All credit for the original idea and method goes to [@patterniha](https://github.com/patterniha).

A TCP forwarder that injects a fake TLS ClientHello with an intentionally wrong TCP sequence number right after the 3-way handshake. Stateful DPI reads the fake SNI and whitelists the flow. The real server drops the packet (out-of-window seq). Real traffic then passes through undetected.

**[English Guide](#setup-guide)** | **[Persian Guide](#%D8%B1%D8%A7%D9%87%D9%86%D9%85%D8%A7%DB%8C-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C)**

## Platforms

- **Linux** -- AF_PACKET raw sockets. Requires root or `CAP_NET_RAW`.
- **macOS** -- BPF device. Requires root.
- **Windows** -- WinDivert driver. Requires Administrator.

## Build

```
cargo build --release
```

Pre-built binaries for Linux (amd64/arm64), macOS (amd64/arm64), and Windows (amd64) are available two ways:
- [GitHub Releases](https://github.com/therealaleph/sni-spoofing-rust/releases) page
- The [`releases/`](releases/) folder in this repository (useful if the Releases page is blocked for you -- just clone the repo or download as ZIP)

## Setup Guide

This tool works with VLESS/VMess configs that go through Cloudflare (CDN-based configs). Your server must be behind Cloudflare.

### Step 1: Find your server's Cloudflare IP

Your v2ray/xray config has a server address (a domain like `myserver.example.com`). Resolve it to get the IP:

```
nslookup myserver.example.com
```

You should get a Cloudflare IP (usually starts with `104.`, `172.67.`, `141.101.`, etc).

### Step 2: Create config.json

```json
{
  "graceful_shutdown_sec": 0,
  "listeners": [
    {
      "listen": "0.0.0.0:40443",
      "connect": "CLOUDFLARE_IP:443",
      "fake_sni": "security.vercel.com"
    }
  ]
}
```

Replace `CLOUDFLARE_IP` with the IP from step 1. The `fake_sni` can be any domain that is allowed by your DPI (a well-known site behind Cloudflare works best).

| Field | Description |
|---|---|
| `listen` | Local address and port to listen on |
| `connect` | Cloudflare IP and port (must be an IP, not a hostname) |
| `fake_sni` | SNI for the fake ClientHello (max 219 bytes) |
| `conn_timeout_sec` | Seconds to wait for the upstream TCP connection to complete (default: `5`) |
| `handshake_timeout_sec` | Seconds to wait for the sniffer to confirm the fake packet was sent (default: `2`) |
| `keepalive_time_sec` | Seconds of idle before TCP keepalive probes begin (default: `11`) |
| `keepalive_interval_sec` | Seconds between individual TCP keepalive probes (default: `2`) |

| Top-level Field | Description |
|---|---|
| `graceful_shutdown_sec` | Seconds to wait for active connections to finish after receiving a shutdown signal. `0` exits immediately (default: `0`) |

Multiple listeners are supported -- each maps to one upstream.

### Step 3: Edit your v2ray/xray config

In your VLESS/VMess client config, change:

- **Address**: from `myserver.example.com` (or its IP) to `127.0.0.1`
- **Port**: to the `listen` port from config.json (e.g. `40443`)
- **Keep everything else the same** (SNI, host, path, UUID, etc.)

Example -- if your original config has:
```
address: myserver.example.com
port: 443
```

Change it to:
```
address: 127.0.0.1
port: 40443
```

The tool sits between your v2ray client and the server. Your client connects to the tool, the tool handles the DPI bypass, and forwards traffic to Cloudflare.

### Step 4: Run

```
# Linux/macOS
sudo ./sni-spoof-rs config.json

# Windows (run as Administrator)
sni-spoof-rs.exe config.json
```

**Windows note:** The Windows download is a zip containing `sni-spoof-rs.exe` and `WinDivert64.sys`. Keep both files in the same folder. The `.sys` file is the kernel driver that WinDivert needs to intercept packets.

Then connect with your v2ray/xray client as usual.

### Finding a working fake_sni (scan mode)

If your chosen `fake_sni` stops working (e.g., after a DPI update), the tool includes a scanner that probes a built-in list of ~650 Cloudflare-fronted domains and reports which ones pass through your network:

```
# scan using built-in list (no sudo needed -- scan 