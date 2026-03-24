
<p align="center">
  <pre align="center">
  █   █ █▀▀█ █▀▀█ █▀▄▀█ █  █ █▀▀█ █   █▀▀
  █▄█▄█ █  █ █▄▄▀ █ █ █ █▀▀█ █  █ █   █▀▀
  ▀ ▀ ▀ ▀▀▀▀ ▀ ▀▀ ▀   ▀ ▀  ▀ ▀▀▀▀ ▀▀▀ ▀▀▀
  </pre>
  <br>
  <strong>Expose your localhost to the internet. Instantly.</strong>
  <br><br>
  <a href="https://github.com/MuhammadHananAsghar/wormhole/releases"><img src="https://img.shields.io/github/v/release/MuhammadHananAsghar/wormhole?style=flat-square" alt="Release"></a>
  <a href="https://github.com/MuhammadHananAsghar/wormhole/blob/main/LICENSE"><img src="https://img.shields.io/github/license/MuhammadHananAsghar/wormhole?style=flat-square" alt="License"></a>
  <a href="https://goreportcard.com/report/github.com/MuhammadHananAsghar/wormhole"><img src="https://goreportcard.com/badge/github.com/MuhammadHananAsghar/wormhole?style=flat-square" alt="Go Report"></a>
</p>

---

**Wormhole** is an open-source [ngrok](https://ngrok.com) alternative that gives your local server a public HTTPS URL with a single command. No signup required. No config files. Just works.

```bash
wormhole http 3000
```

```
  █   █ █▀▀█ █▀▀█ █▀▄▀█ █  █ █▀▀█ █   █▀▀
  █▄█▄█ █  █ █▄▄▀ █ █ █ █▀▀█ █  █ █   █▀▀
  ▀ ▀ ▀ ▀▀▀▀ ▀ ▀▀ ▀   ▀ ▀  ▀ ▀▀▀▀ ▀▀▀ ▀▀▀
  v0.1.0

  ╭──────────────────────────────────────────────────╮
  │       Status  ● connected                        │
  │   Forwarding  https://k7x9m2.wormhole.bar → ...  │
  │    Inspector  http://localhost:4040               │
  ╰──────────────────────────────────────────────────╯

  Requests
  --------------------------------------------------------------
  GET     /                          200    12ms
  POST    /webhooks/stripe           200     8ms
  GET     /api/users                 200    34ms
```

## Features

- **One command** — `wormhole http 3000` and you're live
- **HTTPS by default** — TLS handled automatically by Cloudflare
- **Custom subdomains** — `wormhole http 3000 --subdomain myapp` (free with GitHub login)
- **Traffic inspector** — Built-in dashboard at `localhost:4040` with live request stream
- **Request replay** — Re-send any captured request with one click
- **HAR export** — Export captured traffic in standard HAR format
- **Color-coded terminal** — Live request log with method + status code colors
- **Auto-reconnect** — Exponential backoff, seamless recovery
- **WebSocket passthrough** — Full WebSocket support through the tunnel
- **Zero config** — No signup, no config file, no server to deploy
- **Open source** — Fully open source, MIT licensed

## Install

### Quick install (macOS / Linux)

```bash
curl -fsSL https://wormhole.bar/install.sh | sh
```

### Homebrew (macOS)

```bash
brew install MuhammadHananAsghar/tap/wormhole
```

### Go install

```bash
go install github.com/MuhammadHananAsghar/wormhole/cmd/wormhole@latest
```

### Build from source

```bash
git clone https://github.com/MuhammadHananAsghar/wormhole.git
cd wormhole
make build
# Binary: ./wormhole
```

## Quick Start

### Expose a local HTTP server

```bash
# Start your local server on any port
wormhole http 3000
# => https://k7x9m2.wormhole.bar -> http://localhost:3000
```

### Custom subdomain (free)

```bash
# One-time login via GitHub
wormhole login

# Use your own subdomain
wormhole http 3000 --subdomain myapp
# => https://myapp.wormhole.bar -> http://localhost:3000
```

### Traffic inspector

Every tunnel automatically starts a traffic inspector at `http://localhost:4040`:

- Live request/response stream via WebSocket
- Request detail view with headers and body
- One-click request replay
- Filter by method, status code, path
- Export as HAR file

```bash
# Custom inspector port
wormhole http 3000 --inspect localhost:5050

# Disable inspector
wormhole http 3000 --no-inspect
```

## CLI Reference

```bash
wormhole http <port>                    # Expose local HTTP server
wormhole http <port> --subdomain NAME   # Custom subdomain
wormhole http <port> --headless         # No TUI, plain log output
wormhole http <port> --inspect ADDR     # Custom inspector address
wormhole http <port> --no-inspect       # Disable inspector

wormhole login                          # Authenticate via GitHub
wormhole logout                         # Remove stored credentials
wormhole status                         # Show auth status
wormhole uninstall                      # Remove wormhole from system
wormhole uninstall --purge              # Also remove config (~/.wormhole/)
wormhole version                        # Print version
```

## How It Works

```
YOUR LAPTOP                       CLOUDFLARE EDGE (300+ cities)
┌──────────────┐                 ┌─────────────────────────────┐
│              │   WebSocket     │                             │
│  wormhole    │◄───────────────►│  Worker (request router)    │
│  client      │  (encrypted)    │         ↕                   │
│              │                 │  Durable Object (tunnel)    │
│  localhost   │                 │  • Holds your WebSocket     │
│  :3000       │                 │  • Pro