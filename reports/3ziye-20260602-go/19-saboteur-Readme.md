# Saboteur — HTTP Fault Injection Proxy

A lightweight HTTP-layer fault injection proxy. Intercepts traffic and injects configurable faults based on rules — useful for testing service resilience in development and CI/CD.

**Key differentiator from Toxiproxy:** operates at HTTP layer — understands URLs, methods, headers, and response bodies. Not TCP-level.

---

## Quickstart

```bash
docker run -p 8080:8080 -p 8081:8081 \
  -e UPSTREAM_URL=http://my-service:3000 \
  yourname/saboteur
```

- **Port 8080** — proxy (send your real traffic here)
- **Port 8081** — control UI + API (manage rules, view traffic)

Open `http://localhost:8081` in your browser to use the web UI.

---

## With a config file

```bash
docker run -p 8080:8080 -p 8081:8081 \
  -v $(pwd)/config/example.yaml:/etc/saboteur/config.yaml \
  yourname/saboteur --config /etc/saboteur/config.yaml
```

---

## Docker Compose

```bash
docker compose up
```

Uses `docker-compose.yml` in the repo root. Spins up `saboteur` + a mock upstream (`hashicorp/http-echo`).

---

## Configuration Reference

All settings can be provided via YAML file or environment variables.

| YAML key | Env var | Default | Description |
|----------|---------|---------|-------------|
| `proxy.upstream_url` | `UPSTREAM_URL` | *(required)* | URL to proxy traffic to |
| `proxy.port` | `PROXY_PORT` | `8080` | Proxy listener port |
| `proxy.timeout_ms` | — | `30000` | Upstream request timeout |
| `proxy.max_idle_conns` | — | `100` | Max idle upstream connections |
| `control.port` | `CONTROL_PORT` | `8081` | Control API + UI port |
| `control.bind` | `CONTROL_BIND` | `0.0.0.0` | Control bind address |
| `control.api_key` | `API_KEY` | *(none)* | If set, require `X-API-Key` header on control API |
| `traffic_log.max_entries` | `TRAFFIC_LOG_SIZE` | `1000` | Ring-buffer size |
| `log_level` | `LOG_LEVEL` | `info` | `debug` / `info` / `warn` / `error` |
| `log_format` | `LOG_FORMAT` | `json` | `json` / `text` |

---

## Fault Types

### Latency

Add delay before forwarding or returning.

```yaml
fault:
  type: latency
  mode: fixed       # fixed | uniform | normal
  fixed_ms: 500
  apply_to: request # request | response
```

### Error Response

Return a specific status without hitting upstream.

```yaml
fault:
  type: error
  status_code: 503
  body: '{"error":"down"}'
  headers:
    Retry-After: "30"
```

### Connection Abort

Drop the connection after N bytes.

```yaml
fault:
  type: abort
  after_bytes: 0    # 0 = drop immediately
```

### Timeout

Accept connection, forward to upstream, never respond.

```yaml
fault:
  type: timeout
```

### Body Corruption

Replace the upstream response body.

```yaml
fault:
  type: body_corrupt
  mode: json_invalid  # empty | random_bytes | json_invalid | truncate
  truncate_bytes: 100 # for truncate mode
```

### Header Injection

Add or override headers on request or response.

```yaml
fault:
  type: header_inject
  apply_to: response   # request | response
  headers:
    X-Injected: "true"
```

### Bandwidth Throttle

Rate-limit response streaming.

```yaml
fault:
  type: throttle
  bytes_per_second: 1024
```

---

## Rule System

Rules are evaluated in priority order (lower number = higher priority). A request matches the **first** rule where all matcher conditions are satisfied.

```yaml
rules:
  - id: "payment-errors"
    enabled: true
    priority: 10
    description: "503 on 20% of EU payment POSTs"
    match:
      path_prefix: "/api/payment"
      methods: [POST]
      headers:
        X-Region: "EU"
    percentage: 20        # 0-100; fraction of matching requests that get the fault
    fault:
      type: error
      status_code: 503
      body: '{"error":"unavailable"}'
```

### Matcher fields (all optional; unset = match anything)

| Field | Description |
|-------|-------------|
| `path` | Exact URL path |
| `path_prefix` | URL path prefix |
| `path_regex` | RE2 regex on URL path |
| `methods` | HTTP methods (empty = all) |
| `headers` | All listed headers must match |
| `query_params` | All listed query params must match |

---

## Control API Overview

Base URL: `http://localhost:8081`

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | Health check |
| GET | `/metrics` | Prometheus metrics |
| GET | `/api/rules` | List all rules |
| POST | `/api/rules` | Create rule |
| GET | `/api/rules/{id}` | Get rule |
| PUT | `/api/rules/{id}` | Replace rule |
| PATCH | `/api/rules/{id}` | Update fields (enabled, priority, percentage) |
| DELETE | `/api/rules/{id}` | Delete rule |
| POST | `/api/rules/reset` | Delete all runtime rules (preserves config-file rules) |
| GET | `/api/traffic` | Traffic log (`?limit=100&path_filter=&fault_only=true`) |
| DELETE | `/api/traffic` | Clear traffic log |
| GET | `/api/traffic/stream` | SSE stream of live traffic |
| GET | `/api/config` | Current effective configuration |

Full spec: [`openapi.yaml`](openapi.yaml)

### API Key auth

```bash
curl -H "X-API-Key: mysecret" ht