# Rayfish

**Your machines, on one private network, anywhere.** Rayfish is a peer-to-peer
mesh VPN that lets your laptop, phone, server, and your friends' machines talk
to each other as if they were all plugged into the same router, even when
they're scattered across the world behind different NATs.

There's nothing to host and nothing to sign up for. You don't rent a server,
open a port, or hand out IP addresses. One person runs a command, shares a code,
and the network exists.

```bash
ray create                 # you now have a private network of your own
ray invite gaming          # mint a one-time code to hand out
ray join <invite-code>     # a friend joins with the code
ping alice.gaming.ray      # you reach each other by name
```

That's the whole idea. The rest of this README is the details.

[![License: MPL 2.0](https://img.shields.io/badge/license-MPL%202.0-brightgreen.svg)](LICENSE)
![Status: experimental](https://img.shields.io/badge/status-experimental-orange.svg)

**Jump to:** [Why](#why-rayfish) · [How it works](#how-it-works) · [Features](#features) · [Quick start](#quick-start) · [Managing your network](#managing-your-network) · [Who can join](#who-can-join) · [Firewall](#firewall) · [Provisioning](#declarative-provisioning) · [Permissions](#permissions) · [Custom relay & DNS](#custom-relay--dns) · [Troubleshooting](#troubleshooting) · [How it compares](#how-it-compares) · [FAQ](#faq)

---

## Why Rayfish

- **No infrastructure.** There's no control server to host or trust. Peers find each other through a DHT and connect directly. The only "server" is whoever ran `ray create`, and they can be offline once everyone's admitted.
- **Identity, not IP.** Every machine has a cryptographic identity, and its addresses are derived from that identity: stable, collision-free, and assigned without any coordinator handing them out.
- **Private by default.** Networks are closed unless you say otherwise. The code you share to discover a network isn't enough to join it.
- **Works over NAT.** Hole-punching and end-to-end encryption come from [iroh](https://iroh.computer), including automatic port mapping (UPnP/NAT-PMP/PCP). When a direct path isn't possible (roughly 10% of the time), traffic falls back to encrypted relays. For routers that block automatic port mapping, the daemon listens on a fixed UDP port (41383) you can manually forward to guarantee a direct path. A manual forward maps the port to one machine, so only one node per LAN benefits; the others still use automatic traversal and relay fallback.
- **Reach peers by name.** Magic DNS gives you `name.network.ray` so you never memorize a virtual IP.

## How it works

Each machine runs a small daemon (comparable to Tailscale's `tailscaled`) that creates a TUN device, captures IP packets, and tunnels them over iroh's QUIC connections. Everything else (`create`, `join`, `status`, file sharing) is an unprivileged command that talks to the daemon over a local socket.

1. **Create.** One peer starts a network and becomes its coordinator. The network's public key is its **room id**: it lets others discover the network but, on a closed network, is not enough to get in.
2. **Join.** On a closed network a peer gets in with a one-time invite code (`ray invite`) or by requesting approval (`ray requests` / `ray accept`). The coordinator is the gatekeeper.
3. **Mesh.** Every peer derives its own stable virtual IPv4 (`100.64.0.0/10`) and IPv6 (`200::/7`) from its identity, then connects directly to every other peer.
4. **Use it.** Any TCP/UDP app works, addressed by IP or by `name.network.ray`.

## Features

Each of these has a fuller treatment further down; this is the one-line tour.

- 🔒 **Closed-by-default networks.** One-time invites, reusable fleet keys, or live approval, with `--open` for public ones. See [Who can join](#who-can-join).
- 🤝 **Direct 2-peer links.** `ray connect <contact-id>` ties you to one person with no room id or invite, approved like a friend request. See [Direct 2-peer connections](#direct-2-peer-connections).
- 🌐 **Magic DNS.** Reach peers at `name.network.ray`, updated live as they join, leave, or rename.
- 🧱 **Per-device firewall.** A userspace firewall for mesh traffic, secure by default, layered on top of your host firewall. See [Firewall](#firewall).
- 🔑 **Mesh SSH, no keys.** Log in over the mesh with a stock `ssh` client; peers authenticate by identity. See [SSH, no keys](#ssh-no-keys).
- 📜 **Declarative provisioning.** `ray apply deploy.yaml` stands up networks and firewall rules from a YAML spec, with reusable `aliases:` and `groups:` instead of repeated hostnames.
- 👥 **Multi-device identity.** Pair your laptop and phone under one identity, with encrypted key backup (optionally to 1Password). See [Pairing your own devices](#pairing-your-own-devices).
- 📁 **File sharing.** `ray send file.zip bob`, with optional auto-accept for transfers from your own paired devices.
- 📡 **mDNS** local discovery, and optional **Tor** transport.
