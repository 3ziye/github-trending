# Gately

**English** | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Español](README.es.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Русский](README.ru.md) | [Português (Brasil)](README.pt-BR.md)

An open-source, auditable network gateway toolkit for home networks, NAS boxes, cloud hosts, and servers of all kinds. DDNS, STUN traversal, port forwarding, reverse proxy, certificates, WAF, and more ship in a single ~32 MB file.

> **fnOS users:** Gately ships as a native fnOS app. It plugs into the **fnOS unified gateway**, so it opens from the fnOS desktop icon and works over the same address you use for fnOS, including your remote domain, with no extra port to open. Once enabled, **fnOS administrators can sign in directly with their fnOS session**, without a Gately password or two-step code. See [fnOS native app](#fnos-native-app).

![Gately overview](docs/images/overview.webp)

![Web services: reverse proxy, static files and redirects by domain, with WAF, IP rules and sign-in per site](docs/images/web.webp)

![Per-site traffic stats: requests, errors, backend health, top client IPs and countries](docs/images/site-stats.webp)

![Port forwarding with SNI routing: one port 443 shared by several services](docs/images/portforward-sni.webp)

![Dynamic DNS](docs/images/ddns.webp)

![Intrusion protection: fail2ban-style bans synced to nftables](docs/images/guard.webp)

![Docker](docs/images/docker.webp)

![frp: several frpc and frps instances, with proxies grouped by client](docs/images/frp.webp)

![Web terminal: SSH, Telnet and the local shell in the browser](docs/images/terminal.webp)

![Configuration history with diff and one-click rollback](docs/images/config-history.webp)

![Built-in API docs](docs/images/api-docs.webp)

## Why Gately

Gately is fully open source, so users and the community can read the source and the configuration directly. For software that sits on your network edge and holds your DNS keys and certificate private keys, open source lets you see exactly what it does. Gately's commitments:

- The source is released under Apache-2.0 and open to community review
- No connections to any project-operated server by default and no device information reported; third-party sign-in uses your own OAuth apps, with no relay in between
- Every outbound address (public IP lookup, STUN servers, and so on) is visible, editable, and can be turned off
- Configuration is plain-text JSON, so you can put it under git for auditing and rollback

## Features

| Module | Capabilities |
| --- | --- |
| Dynamic DNS | Alibaba Cloud, Cloudflare, Tencent Cloud, DNSPod, Huawei Cloud, GoDaddy, Porkbun, dynv6, DuckDNS, Amazon Route 53, OVHcloud, Gandi, NS1, Bunny DNS, Namecheap, DynDNS2 (No-IP, Dynu, …), custom callbacks; IP discovery via URL, network interface, or command; IPv4/IPv6; webhooks |
| STUN traversal | TCP/UDP, keep-alive, UPnP/NAT-PMP, built-in forwarding, webhooks and scripts triggered on address change |
| Port forwarding | TCP/UDP, IPv4/IPv6, port ranges, multi-target failover, connection limits, traffic statistics, PROXY protocol v1/v2; SNI routing that lets several services share one port such as 443 (TLS passthrough by domain, a default target, PROXY protocol per route) |
| SSL certificates | Automatic ACME issuance and renewal via DNS-01 (wildcard) or HTTP-01 (no DNS provider needed), short-lived certificates and certificates for public IP addresses (Let's Encrypt shortlived profile), EAB, upload, read from file, map to a directory and run a script; after renewal, push certificates to other hosts over SSH and run a command, or restart the Docker containers that use them |
| Tailscale | Managed tailscaled (userspace networking, container-friendly) or attach to an existing system daemon; auth keys / login links, Headscale, subnet routes, exit nodes, peer list and SOCKS5 proxy, fixed port, extra tailscaled arguments and environment variables; online install, update, rollback and uninstall on Linux; restore default settings |
| frp | Multiple frpc and frps instances, each running on its own: frpc client (tcp/udp/http/https/stcp/xtcp proxies, changes apply instantly) and frps server (port allowlist, subdomains, dashboard); one-click import of legacy ini and new toml configs; online install, update, rollback and uninstall; restore default settings |
| Cloudflare Tunnel | cloudflared token tunnels and trycloudflare quick tunnels, multiple tunnels, automatic restart, public address display; online install, update, rollback and uninstall; restore default settings |
| Web services | Per-domain reverse proxy / redirect / static files / fixed text / close connection (like nginx return 444); HTTPS and HTTP/3 (QUIC); HTTP and HTTPS on the same port (redirect or serve); WebSocket; PROXY protocol in and out; basic auth, web auth, GitHub/Google/QQ/OIDC sign-in, shared users with TOTP two-step verification and single sign-on across subdomains, a built-in OIDC 