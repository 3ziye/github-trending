# Easy Proxies

English | [简体中文](README_ZH.md)

A proxy node pool management tool based on [sing-box](https://github.com/SagerNet/sing-box), supporting multiple protocols, automatic failover, and load balancing.

## Features

- **Multi-Protocol Support**: VMess, VLESS, Hysteria2, Shadowsocks, Trojan
- **Multiple Transports**: TCP, WebSocket, HTTP/2, gRPC, HTTPUpgrade
- **Subscription Support**: Auto-fetch nodes from subscription links (Base64, Clash YAML, etc.)
- **Subscription Auto-Refresh**: Automatic periodic refresh with WebUI manual trigger (⚠️ causes connection interruption)
- **Pool Mode**: Automatic failover and load balancing
- **Multi-Port Mode**: Each node listens on independent port
- **Web Dashboard**: Real-time node status, latency probing, one-click export
- **Password Protection**: WebUI authentication support
- **Auto Health Check**: Initial check on startup, periodic checks every 5 minutes
- **Smart Node Filtering**: Auto-hide unavailable nodes, sort by latency
- **Flexible Configuration**: Config file, node file, subscription links

## Quick Start

### 1. Configuration

Copy example config files:

```bash
cp config.example.yaml config.yaml
cp nodes.example nodes.txt
```

Edit `config.yaml` to set listen address and credentials, edit `nodes.txt` to add proxy nodes.

### 2. Run

**Docker (Recommended):**

```bash
./start.sh
```

Or manually:

```bash
docker compose up -d
```

**Local Build:**

```bash
go build -tags "with_utls with_quic with_grpc" -o easy-proxies ./cmd/easy_proxies
./easy-proxies --config config.yaml
```

## Configuration

### Basic Config

```yaml
mode: pool                    # Mode: pool or multi-port
log_level: info               # Log level: debug, info, warn, error
external_ip: ""               # External IP for export (recommended for Docker)

# Subscription URLs (optional, multiple supported)
subscriptions:
  - "https://example.com/subscribe"

# Management Interface
management:
  enabled: true
  listen: 0.0.0.0:9090        # Web dashboard address
  probe_target: www.apple.com:80  # Latency probe target
  password: ""                # WebUI password (optional)

# Unified Entry Listener
listener:
  address: 0.0.0.0
  port: 2323
  username: username
  password: password

# Pool Settings
pool:
  mode: sequential            # sequential or random
  failure_threshold: 3        # Failures before blacklist
  blacklist_duration: 24h     # Blacklist duration

# Multi-Port Mode
multi_port:
  address: 0.0.0.0
  base_port: 24000            # Starting port, auto-increment
  username: mpuser
  password: mppass
```

### Operating Modes

#### Pool Mode

All nodes share a single entry point, program auto-selects available nodes:

```yaml
mode: pool

listener:
  address: 0.0.0.0
  port: 2323
  username: user
  password: pass

pool:
  mode: sequential  # sequential or random
  failure_threshold: 3
  blacklist_duration: 24h
```

**Use Case:** Automatic failover, load balancing

**Usage:** Set proxy to `http://user:pass@localhost:2323`

#### Multi-Port Mode

Each node listens on its own port for precise control:

**Config Format:** Two syntaxes supported

```yaml
mode: multi-port  # Recommended: hyphen format
# or
mode: multi_port  # Compatible: underscore format
```

**Full Example:**

```yaml
mode: multi-port

multi_port:
  address: 0.0.0.0
  base_port: 24000  # Ports auto-increment from here
  username: user
  password: pass

nodes_file: nodes.txt
```

**Startup Output:**

```
📡 Proxy Links:
═══════════════════════════════════════════════════════════════
🔌 Multi-Port Mode (3 nodes):

   [24000] Taiwan Node
       http://user:pass@0.0.0.0:24000
   [24001] Hong Kong Node
       http://user:pass@0.0.0.0:24001
   [24002] US Node
       http://user:pass@0.0.0.0:24002
═══════════════════════════════════════════════════════════════
```

**Use Case:** Specific node selection, performance testing

**Usage:** Each node has independent proxy address

### Node Configuration

**Method 1: Subscription Links (Recommended)**

Auto-fetch nodes from subscription URLs:

```yaml
subscriptions:
  - "https://example.com/subscribe/v2ray"
  - "https://example.com/subscribe/clash"
```

Supported formats:
- **Base64 Encoded**: V2Ray standard subscription
- **Clash YAML**: Clash config format
- **Plain Text**: One URI per line

**Method 2: Node File**

Specify in `config.yaml`:

```yaml
nodes_file: nodes.txt
```

`nodes.txt` - one URI per line:

```
vless://uuid@server:443?security=reality&sni=example.com#NodeName
hysteria2://password@server:443?sni=example.com#HY2Node
ss://base64@server:8388#SSNode
trojan://password@server:443?sni=example.com#TrojanNode
vmess://base64...#VMessNode
```

**Method 3: Direct in Config**

```yaml
nodes:
  - uri: "vless://uuid@server:443#Node1"
  - name: custom-name
    uri: "ss://base64@server:8388"
    port: 24001  # Optional, manual port
```

> **Tip**: Multiple methods can be combined, nodes are merged automatically.

## Supported Protocols

| Protocol | URI Format | Features |
