[English](README.md) | [简体中文](README.zh-CN.md)

<div align="center">
  <img src="webui/public/vite.svg" width="48" alt="Resin Logo" />
  <h1>Resin</h1>
  <p><strong>Turn massive proxy subscriptions into a stable, smart, and observable network with sticky sessions.</strong></p>
</div>

<p align="center">
  <a href="https://github.com/Resinat/Resin/releases"><img src="https://img.shields.io/github/v/release/Resinat/Resin?style=flat-square&label=release&sort=semver" alt="Release" /></a>
  <a href="https://github.com/Resinat/Resin/actions/workflows/release.yml"><img src="https://img.shields.io/github/actions/workflow/status/Resinat/Resin/release.yml?style=flat-square&label=release%20pipeline" alt="Release Pipeline" /></a>
  <a href="https://github.com/Resinat/Resin/pkgs/container/resin"><img src="https://img.shields.io/badge/ghcr-ghcr.io%2Fresinat%2Fresin-2496ED?style=flat-square&logo=docker&logoColor=white" alt="GHCR Image" /></a>
  <a href="https://github.com/Resinat/Resin/blob/master/LICENSE"><img src="https://img.shields.io/github/license/Resinat/Resin?style=flat-square" alt="License" /></a>
  <a href="https://github.com/Resinat/Resin/blob/master/go.mod"><img src="https://img.shields.io/github/go-mod/go-version/Resinat/Resin?style=flat-square" alt="Go Version" /></a>
  <a href="https://github.com/Resinat/Resin/releases"><img src="https://img.shields.io/badge/support-linux%20%7C%20macOS%20%7C%20windows%20%C2%B7%20amd64%20%7C%20arm64-0A7EA4?style=flat-square" alt="Support Matrix" /></a>
  <a href="DESIGN.md"><img src="https://img.shields.io/badge/docs-DESIGN.md-1F6FEB?style=flat-square" alt="Design Docs" /></a>
</p>

---

**Resin** is a **high-performance intelligent proxy pool gateway** built for operating massive numbers of proxy nodes.

It helps shield your services from unstable upstream proxies and aggregates them into a single HTTP gateway with **session stickiness (sticky routing)**.

## 💡 Why Resin?

- **Massive-scale management**: Easily handles 100k+ proxy nodes with native high-concurrency performance.
- **Smart scheduling and circuit breaking**: Fully automated **passive + active** health checks, outbound IP probing, and latency analysis to remove bad nodes precisely. Uses P2C plus domain-aware latency-weighted scoring for optimal node selection.
- **Business-friendly sticky proxying**: Keeps the same business account bound to a stable outbound IP. If a node fails, Resin seamlessly switches to another node with the same IP.
- **Dual access modes**: Supports both standard forward proxy (HTTP Proxy) and URL-based reverse proxy.
- **Observability**: Detailed metrics and logs, plus a visual Web UI. Includes complete structured request logs for querying and auditing by platform, account, target site, and more.
- **Simple and powerful**: Works out of the box with default settings, while still offering deep customization for enterprise-grade needs.
- **Cross-subscription deduplication**: Automatically merges identical nodes from different subscriptions and shares their health state.
- **Hot reload**: Update common settings without restart. Refresh subscriptions without dropping existing traffic.
- **Persistent state**: Keeps node health, latency stats, and lease bindings across restarts.
- **Zero-intrusion sticky access**: Can extract account identity from existing request headers (for example API keys), so clients often need no code changes.
- **Incremental subscription refresh**: Syncs subscription updates without interrupting current connections.
- **Flexible node isolation**: Use Platform rules (regex, region, etc.) to build independent proxy pools for different business scenarios.

> [!TIP]
> You can feed this README and [`DESIGN.md`](DESIGN.md) to AI and ask it anything about the project.

![](doc/images/dashboard_en-us.png)

---

## 🔌 Supported Protocols and Subscription Formats

### Subscription sources

- Remote subscription URL: `http://` or `https://`.
- Local subscription content: paste subscription content directly in the UI/API.

### Subscription content formats

- sing-box JSON: `{"outbounds":[...]}` or raw outbound array `[...]`.
- Clash JSON/YAML: `{"proxies":[...]}` or YAML `proxies:`.
- URI line format (one node per line): `vmess://`, `vless://`, `trojan://`, `ss://`, `hysteria2://`, `http://`, `https://`, `socks5://`, `socks5h://`.
  For `http://`, `https://`, `socks5://`, `socks5h://`, use `scheme://[user:pass@]host:port` (optional `#tag`; `https` also supports `sni`/`servername`/`peer` and `allowInsecure`/`insecure` query parameters).
- Plain HTTP proxy lines: `IP:PORT` or `IP:PORT:USER:PASS` (IPv4 and IPv6).
- Base64-wrapped text subscriptions (for URI lines/plain-text node lists).

### Supported outbound node types

- For sing-box JSON/raw outbounds: `socks`, `http`, `shadowsocks`, `vmess`, `trojan`, `wireguard`, `hysteria`, `vless`, `shadowtls`, `tuic`, `hysteria2`, `anytls`, `ssh`.
- For Clash conversion: `ss`/`shadowsocks`, `socks`/`socks4`/`socks4a`/`socks5`, `http`, `vmess`, 