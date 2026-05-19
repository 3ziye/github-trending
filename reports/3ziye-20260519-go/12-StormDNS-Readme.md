<h1 align="center">⚡ StormDNS</h1>

<p align="center">
  <strong>A DNS-based TCP tunnel for censored, lossy, high-latency networks.</strong>
</p>

<p align="center">
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/license-MIT-00a36c?style=for-the-badge"></a>
  <img alt="Go" src="https://img.shields.io/badge/Go-1.25-00add8?style=for-the-badge&logo=go&logoColor=white">
  <img alt="Transport" src="https://img.shields.io/badge/transport-DNS%20over%20UDP%2F53-4f46e5?style=for-the-badge">
  <img alt="Platforms" src="https://img.shields.io/badge/platforms-Windows%20%7C%20Linux%20%7C%20macOS%20%7C%20Termux-f59e0b?style=for-the-badge">
</p>

<p align="center">
  <a href="README_FA.MD">فارسی</a> ·
  <a href="https://github.com/nullroute1970/StormDNS/releases/latest">Latest Release</a> ·
  <a href="https://t.me/nulllroute1970">Telegram Channel</a>
</p>

StormDNS is a client/server tunneling system that moves TCP traffic through DNS queries and DNS responses. The client runs on the user's device and exposes a local SOCKS5 proxy or a raw TCP listener. Applications connect to that local listener like they would connect to any normal proxy. StormDNS then splits each stream into small DNS-safe packets, applies optional compression and encryption, sends packets through one or more DNS resolvers, and reconstructs the stream on the remote StormDNS server. The server finally opens the real outbound connection directly, through an optional upstream SOCKS5 proxy, or to a fixed TCP target depending on configuration.

The project is built for networks where common circumvention protocols are blocked, throttled, actively probed, or unreliable, but DNS traffic still has a usable path. This includes environments with small resolver payload limits, high latency, unstable resolver behavior, weak upload bandwidth, aggressive rate limits, and frequent packet loss. StormDNS treats those problems as normal operating conditions: it uses MTU discovery, resolver health checks, multi-resolver balancing, packet duplication, ARQ retransmission, ACK/NACK handling, packet packing, and log-based startup to keep the tunnel usable when the network is hostile.

Typical deployment is straightforward: run the server on a VPS with UDP/53 reachable, delegate a short DNS subdomain to that server, put the generated encryption key and domain into the client config, add working resolvers, then point your browser or application at the local SOCKS5 listener. Advanced deployments can enable tunneled DNS handling, tune resolver/MTU behavior, chain server egress through another SOCKS5 proxy, or run the client as a Linux service.

> [!NOTE]
> DNS tunneling is constrained by resolver payload size, latency, rate limits, and packet loss. StormDNS is built for usable connectivity under pressure, not for unrealistic benchmark-only claims or replacing a normal VPN on clean, high-bandwidth networks.

## 💸 Financial Support

Financial support is optional. If you want to support ongoing development, use one of these wallet addresses:

| 💰 Network | 🔐 Address |
| --- | --- |
| TON | `UQDfjVk2UdpiMg-bsxqoLa0O_icuaF20D-wWJgIJwK1Ha2Ul` |
| USDT Tron (TRC20) | `TR8ibZGKutPKoDm5nMbHFwGPFBuMKwjG6j` |
| USDT BNB Smart Chain (BEP20) | `0x8c45d6bae8a5a572b2a776779fe0bcae3d3f9107` |

## 🧭 Quick Navigation

| Area | Go To |
| --- | --- |
| 🚀 First deployment | [Quick Start](#quick-start), [Server Setup](#server-setup), [Client Setup](#client-setup) |
| 🌐 DNS/domain requirements | [Network And Domain Requirements](#network-and-domain-requirements) |
| ⚙️ Configuration | [Configuration Overview](#configuration-overview), [Current Config Keys](#current-config-keys) |
| 📡 Resolver and MTU tuning | [Resolver, MTU, And Loss Tuning](#resolver-mtu-and-loss-tuning) |
| 🧱 Architecture | [Architecture](#architecture) |
| 🧯 Problems and fixes | [Troubleshooting](#troubleshooting) |
| 🧑‍💻 Development | [Development](#development) |

## 🎯 Built For Hostile Networks

| Network Reality | StormDNS Response |
| --- | --- |
| 📏 DNS payloads are small | Low protocol overhead, DNS-safe encoding, active MTU discovery |
| 📉 Packet loss is normal | ARQ windows, ACK/NACK, retransmission timers, terminal drain handling |
| 📡 Resolvers degrade or disappear | Health checks, runtime auto-disable, background recheck, stream failover |
| ⬆️ Upload is often the bottleneck | Separate duplication controls for data, ACKs, setup, and control packets |
| 🕒 Startup can be expensive | Resolver cache logs and log-based startup mode |
| 🧪 Resolver behavior is inconsistent | Per-resolver MTU validation and balancing strategies |
| 🧱 DPI/protocol filtering is common | DNS-only transport over ordinary UDP/53 query/response flow |

## ✨ Main Capabilities

| Category | Capabilities |
| --- | --- |
| 🌐 Transport | DNS tunnel over UDP/53, delegated tunnel domains, multi-resolver routing |
| 🧦 Local access | SOCKS5 proxy mode and raw TCP forwarding mode |
| 📡 Resolver runtime | Random, round-robin, least-loss