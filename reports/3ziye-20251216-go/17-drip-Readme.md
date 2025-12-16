<p align="center">
  <img src="assets/logo.png" alt="Drip Logo" width="200" />
</p>

<h1 align="center">Drip</h1>
<h3 align="center">Your Tunnel, Your Domain, Anywhere</h3>

<p align="center">
  A self-hosted tunneling solution to securely expose your services to the internet.
</p>

<p align="center ">
  <a href="README.md">English</a>
  <span> | </span>
  <a href="README_CN.md">中文文档</a>
</p>

<div align="center">

[![Go](https://img.shields.io/badge/Go-1.21+-00ADD8?style=flat&logo=go)](https://golang.org/)
[![License](https://img.shields.io/badge/License-BSD--3--Clause-blue.svg)](LICENSE)
[![TLS](https://img.shields.io/badge/TLS-1.3-green.svg)](https://tools.ietf.org/html/rfc8446)

</div>

> Drip is a quiet, disciplined tunnel.  
> You light a small lamp on your network, and it carries that light outward—through your own infrastructure, on your own terms.


## Why?

**Control your data.** No third-party servers means your traffic stays between your client and your server.

**No limits.** Run as many tunnels as you need, use as much bandwidth as your server can handle.

**Actually free.** Use your own domain, no paid tiers or feature restrictions.

| Feature | Drip | ngrok Free |
|---------|------|------------|
| Privacy | Your infrastructure | Third-party servers |
| Domain | Your domain | 1 static subdomain |
| Bandwidth | Unlimited | 1 GB/month |
| Active Endpoints | Unlimited | 1 endpoint |
| Tunnels per Agent | Unlimited | Up to 3 |
| Requests | Unlimited | 20,000/month |
| Interstitial Page | None | Yes (removable with header) |
| Open Source | ✓ | ✗ |

## What's New in v0.5.0

### 🔄 Switched to Yamux Protocol

Our custom multiplexing protocol had too many edge-case bugs. We replaced it with [yamux](https://github.com/hashicorp/yamux), HashiCorp's battle-tested stream multiplexing library.

**Why Yamux?**
- Production-proven in Consul, Nomad, and other critical infrastructure
- Built-in flow control and keepalive support
- Active maintenance and community support

**What changed:**
- Removed: Custom HPACK compression, flow control, binary framing, HTTP codec
- Added: Yamux-based connection pooling and session management
- Result: ~60% less protocol code, significantly improved stability

### ⚡ Performance Improvements

| Metric | Improvement |
|--------|-------------|
| Connection setup | 3x faster (session reuse) |
| Memory per tunnel | -50% (simplified state) |
| Latency (p99) | -40% (fewer encoding layers) |
| Throughput | +80% (efficient multiplexing) |

> ⚠️ **Breaking Change**: Protocol incompatible with v0.4.x. Upgrade both client and server.

## Quick Install

```bash
bash <(curl -sL https://raw.githubusercontent.com/Gouryella/drip/main/scripts/install.sh)
```

- Pick a language, then choose to install the **client** (macOS/Linux) or **server** (Linux).
- Non-interactive examples:
  - Client: `bash <(curl -sL https://raw.githubusercontent.com/Gouryella/drip/main/scripts/install.sh) --client`
  - Server: `bash <(curl -sL https://raw.githubusercontent.com/Gouryella/drip/main/scripts/install.sh) --server`

### Uninstall
```bash
bash <(curl -sL https://raw.githubusercontent.com/Gouryella/drip/main/scripts/uninstall.sh)
```

## Usage

### First Time Setup

```bash
# Configure server and token (only needed once)
drip config init
```

### Basic Tunnels

```bash
# Expose local HTTP server
drip http 3000

# Expose local HTTPS server
drip https 443

# Pick your subdomain
drip http 3000 -n myapp
# → https://myapp.your-domain.com

# Expose TCP service (database, SSH, etc.)
drip tcp 5432
```

### Forward to Any Address

Not just localhost - forward to any device on your network:

```bash
# Forward to another machine on LAN
drip http 8080 -a 192.168.1.100

# Forward to Docker container
drip http 3000 -a 172.17.0.2

# Forward to specific interface
drip http 3000 -a 10.0.0.5
```

### Background Mode

Run tunnels in the background with `-d`:

```bash
# Start tunnel in background
drip http 3000 -d
drip https 8443 -n api -d

# List running tunnels
drip list

# View tunnel logs
drip attach http 3000

# Stop tunnels
drip stop http 3000
drip stop all
```

## Server Deployment

### Prerequisites

- A domain with DNS pointing to your server (A record)
- Wildcard DNS for subdomains: `*.tunnel.example.com -> YOUR_IP`
- SSL certificate (wildcard recommended)

### Option 1: Direct (Recommended)

Drip server handles TLS directly on port 443:

```bash
# Get wildcard certificate
sudo certbot certonly --manual --preferred-challenges dns \
  -d "*.tunnel.example.com" -d "tunnel.example.com"

# Start server
drip-server \
  --port 443 \
  --domain tunnel.example.com \
  --tls-cert /etc/letsencrypt/live/tunnel.example.com/fullchain.pem \
  --tls-key /etc/letsencrypt/live/tunnel.example.com/privkey.pem \
  --token YOUR_SECRET_TOKEN
```

### Option 2: Behind Nginx

Run Drip on port 8443, let Nginx handle SSL termination:

```nginx
server {
    listen 443 ssl http2;
    server_name *.tunnel.example.com;

    ssl_certificate /etc/le