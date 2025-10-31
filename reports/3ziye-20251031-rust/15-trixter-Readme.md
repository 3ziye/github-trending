# Project Overview

- [`trixter`](#trixter--chaos-monkey-tcp-proxy) — a high‑performance, runtime‑tunable TCP chaos proxy — a minimal, blazing‑fast written in Rust with **Tokio**. It lets you inject latency, throttle bandwidth, slice writes (to simulate small MTUs/Nagle‑like behavior), corrupt bytes in flight by injecting random bytes, randomly terminate connections, and hard‑timeout sessions – all controllable per connection via a simple REST API.

- [`tokio-netem`](tokio-netem/README.md) — a collection of Tokio `AsyncRead`/`AsyncWrite` adapters (delay, throttle, slice, terminate, shutdown, corrupt data, inject data) that power the `Trixter` proxy and can be used independently in tests and harnesses. [![Crates.io][crates-badge]][crates-url]

The remainder of this document dives into the proxy. For the adapter crate’s detailed guide, follow the `tokio-netem` link above.

[![MIT licensed][mit-badge]][mit-url]

[crates-badge]: https://img.shields.io/crates/v/tokio-netem.svg
[crates-url]: https://crates.io/crates/tokio-netem
[mit-badge]: https://img.shields.io/badge/license-MIT-blue.svg
[mit-url]: https://github.com/brk0v/trixter/blob/master/LICENSE

---

# Trixter – Chaos Monkey TCP Proxy

A high‑performance, runtime‑tunable TCP chaos proxy — a minimal, blazing‑fast alternative to [Toxiproxy](https://github.com/Shopify/toxiproxy) written in Rust with **Tokio**. It lets you inject latency, throttle bandwidth, slice writes (to simulate small MTUs/Nagle‑like behavior), corrupt bytes in flight by injecting random bytes, randomly terminate connections, and hard‑timeout sessions – all controllable per connection via a simple REST API.

---

## Why Trixter?
- **Zero-friction**: one static binary, no external deps.
- **Runtime knobs**: flip chaos on/off without restarting.
- **Per-conn control**: target just the flows you want.
- **Minimal overhead**: adapters are lightweight and composable.

## Features

* **Fast path**: `tokio::io::copy_bidirectional` on a multi‑thread runtime;
* **Runtime control** (per active connection):
  * **Latency**: add/remove delay in ms.
  * **Throttle**: cap bytes/sec.
  * **Slice**: split writes into fixed‑size chunks.
  * **Corrupt**: inject random bytes with a tunable probability.
  * **Chaos termination**: probability \[0.0..=1.0] to abort on each read/write.
  * **Hard timeout**: stop a session after N milliseconds.
* **REST API** to list connections and change settings on the fly.
* **Targeted kill**: shut down a single connection with a reason.
* **Deterministic chaos**: seed the RNG for reproducible scenarios.
* **RST on chaos**: resets (best-effort) when a timeout/termination triggers.

---

## Quick start

### 1. Run an upstream echo server (demo)

Use any TCP server. Examples:

```bash
nc -lk 127.0.0.1 8181
```

### 2. Run `trixter` chaos proxy

with `docker`:

```bash
docker run --network host -it --rm ghcr.io/brk0v/trixter \
    --listen 0.0.0.0:8080 \
    --upstream 127.0.0.1:8181 \
    --api 127.0.0.1:8888 \
    --delay-ms 0 \
    --throttle-rate-bytes 0 \
    --slice-size-bytes 0 \
    --corrupt-probability-rate 0.0 \
    --terminate-probability-rate 0.0 \
    --connection-duration-ms 0 \
    --random-seed 42
```

or build from scratch:

```bash
cd trixter/trixter
cargo build --release
```

or install with `cargo`:

```bash
cargo install trixter
```

and run:

```bash
RUST_LOG=info \
./target/release/trixter \
  --listen 0.0.0.0:8080 \
  --upstream 127.0.0.1:8181 \
  --api 127.0.0.1:8888 \
  --delay-ms 0 \
  --throttle-rate-bytes 0 \
  --slice-size-bytes 0 \
  --corrupt-probability-rate 0.0 \
  --terminate-probability-rate 0.0 \
  --connection-duration-ms 0 \
  --random-seed 42
```

### 3. Test

Now connect your app/CLI to `localhost:8080`. The proxy forwards to `127.0.0.1:8181`.

---

## REST API

Base URL is the `--api` address, e.g. `http://127.0.0.1:8888`.

### Data model

```json
{
  "conn_info": {
    "id": "pN7e3y...",
    "downstream": "127.0.0.1:59024",
    "upstream": "127.0.0.1:8181"
  },
  "delay": { "secs": 2, "nanos": 500000000 },
  "throttle_rate": 10240,
  "slice_size": 512,
  "terminate_probability_rate": 0.05,
  "corrupt_probability_rate": 0.02
}
```

Notes:

* `id` is unique per connection; use it to target a single connection.
* `corrupt_probability_rate` and `terminate_probability_rate` report the current per-operation flip probability (`0.0` when it is off).

### Health check

```bash
curl -s http://127.0.0.1:8888/health
```

### List connections

```bash
curl -s http://127.0.0.1:8888/connections | jq
```

### Kill a connection

```bash
ID=$(curl -s http://127.0.0.1:8888/connections | jq -r '.[0].conn_info.id')

curl -i -X POST \
  http://127.0.0.1:8888/connections/$ID/shutdown \
  -H 'Content-Type: application/json' \
  -d '{"reason":"test teardown"}'
```

### Kill all connections

```bash
curl -i -X POST \
  http://127.0.0.1:8888/connections/_all/shutdown \
  -H 'Content-Type: application/json' \
  -d '{"reason":"test teardown"}'
```

### Set laten