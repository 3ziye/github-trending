# iron-proxy

[![Docs](https://img.shields.io/badge/docs-iron--proxy-blue)](https://docs.iron.sh)
[![Latest Release](https://img.shields.io/github/v/release/ironsh/iron-proxy)](https://github.com/ironsh/iron-proxy/releases/latest)
[![Docker Pulls](https://img.shields.io/docker/pulls/ironsh/iron-proxy)](https://hub.docker.com/r/ironsh/iron-proxy)

## The problem

CI jobs, AI coding agents, and sandboxed containers can make arbitrary outbound
requests. A compromised dependency, a prompt injection, or a malicious build
step can exfiltrate secrets, phone home, or open a reverse shell. Most
teams have zero visibility into what's leaving their workloads, let alone any
way to stop it.

## What iron-proxy does

iron-proxy is a MITM egress proxy with a built-in DNS server that sits between
your untrusted workload and the internet. It enforces default-deny at the
network boundary, so the workload can only reach domains you explicitly allow.
Real secrets never enter the sandbox. Workloads use proxy tokens, and
iron-proxy swaps in real credentials at egress, meaning a compromised workload
can exfiltrate a token that's worthless outside the proxy.

Single binary. Single YAML config.

- **Default-deny egress.** Every outbound request is blocked unless the
  destination matches your allowlist. List your domains and CIDRs, everything
  else gets a 403.
- **Boundary-level secret injection.** Workloads send proxy tokens; iron-proxy
  replaces them with real secrets before the request leaves. If the sandbox is
  compromised, the attacker gets tokens that are useless outside the proxy.
- **Per-request audit trail.** Every request logged as structured JSON with
  the full transform pipeline result: which secrets were swapped, which rules
  matched, what got blocked and why.
- **Streaming-aware.** WebSocket upgrades and Server-Sent Events are proxied
  natively. No special configuration for agent workloads that hold long-lived
  connections.
- **CONNECT and SOCKS5 support.** Optional tunnel listener for tools that
  natively support proxy configuration via `HTTPS_PROXY` or SOCKS5 settings.

Built for CI pipelines, GitHub Actions, AI agents (Claude Code, Cursor,
Codex), and any environment where you run code you don't fully trust.

<div align="center">
    <strong>Blocked exfiltration + secret rewriting in action:</strong>
    <br/><br/>
    <a href="https://screen.studio/share/Gq2zqtrp" target="_blank">
        <img src="./images/intro.gif" width="75%" />
    </a>
</div>
 
## Installation
 
Docker images are available on [Docker Hub](https://hub.docker.com/r/ironsh/iron-proxy)
and pre-built binaries for Linux/macOS (amd64/arm64) are on
[GitHub Releases](https://github.com/ironsh/iron-proxy/releases).
 
Or build from source:
 
```bash
go build -o iron-proxy ./cmd/iron-proxy
```

## Quick start

```bash
cd examples/docker-compose
docker compose up
```

This starts iron-proxy and a demo client that fires five requests through the
proxy. Check the logs to see allowed, blocked, and secret-rewritten requests:

```bash
docker compose logs proxy
```

Every request produces a structured JSON audit entry:

```json
{
  "host": "httpbin.org",
  "method": "GET",
  "path": "/headers",
  "action": "allow",
  "status_code": 200,
  "duration_ms": 142,
  "request_transforms": [
    { "name": "allowlist", "action": "continue" },
    {
      "name": "secrets",
      "action": "continue",
      "annotations": { "swapped": [{ "secret": "OPENAI_API_KEY", "locations": ["header:Authorization"] }] }
    }
  ]
}
```

Rejected requests include a `rejected_by` field and log at WARN level. See
[Audit log format](#audit-log-format) for the full schema.

## Production usage

### 1. Generate a CA

iron-proxy terminates TLS by generating leaf certificates on the fly, signed by
a CA you provide. Client containers must trust this CA.

```bash
mkdir -p certs
openssl genrsa -out certs/ca.key 4096
openssl req -x509 -new -nodes \
    -key certs/ca.key \
    -sha256 -days 3650 \
    -subj "/CN=iron-proxy CA" \
    -addext "basicConstraints=critical,CA:TRUE" \
    -addext "keyUsage=critical,keyCertSign" \
    -out certs/ca.crt
```

### 2. Create a Docker network

iron-proxy needs a fixed IP so containers can point their DNS at it:

```bash
docker network create --subnet=172.20.0.0/24 iron-proxy
```

### 3. Start iron-proxy

Create an env file with your secrets (keep this out of version control):

```bash
echo "OPENAI_API_KEY=sk-real-key" > .env
```

```bash
docker run -d --name iron-proxy \
  --network iron-proxy --ip 172.20.0.2 \
  -v $(pwd)/proxy.yaml:/etc/iron-proxy/proxy.yaml:ro \
  -v $(pwd)/certs/ca.crt:/etc/iron-proxy/ca.crt:ro \
  -v $(pwd)/certs/ca.key:/etc/iron-proxy/ca.key:ro \
  --env-file .env \
  ironsh/iron-proxy:latest -config /etc/iron-proxy/proxy.yaml
```

### 4. Route containers through the proxy

The simplest approach is DNS-based routing: point the container's DNS at
iron-proxy and all hostname lookups resolve to the proxy IP, routing traffic
throug