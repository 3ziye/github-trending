# ExtendDB

> **ExtendDB is an independent open source project managed by Amazon Web Services. It is not Amazon DynamoDB and does not contain any DynamoDB source code.** "DynamoDB" is a trademark of Amazon.com, Inc. ExtendDB is a clean-room implementation that speaks the DynamoDB wire protocol. Behavioral differences from the real service are documented in [Differences from DynamoDB](docs/differences-from-dynamodb.md).

A DynamoDB-compatible API adapter, ExtendDB speaks the DynamoDB wire protocol — any AWS SDK, CLI, or tool that works with DynamoDB works with ExtendDB, unchanged.

## Use Cases

- **Local development** — run DynamoDB workloads on your laptop with zero cloud dependency
- **CI/CD pipelines** — deterministic integration tests against a DynamoDB-compatible backend
- **Self-hosted deployments** — run DynamoDB workloads on your own infrastructure (on-premises, private cloud, edge)
- **Multi-cloud** — use DynamoDB semantics on any cloud that runs PostgreSQL
- **Air-gapped environments** — DynamoDB functionality with no internet connectivity

## Features

- Full DynamoDB wire protocol: CRUD, Query, Scan, Batch, Transactions, Streams, TTL, Import/Export
- SigV4 authentication with IAM compatibility: users, groups, roles, policies, permissions boundaries
- Web management console for account and credential administration
- TLS with automatic self-signed certificate generation (replaceable with CA-signed certs)
- CSRF protection, security headers, session management
- JSON metrics endpoint with DynamoDB CloudWatch-style metric names and dimensions
- Daemon mode with syslog logging, plus `--foreground` for container and supervisor environments
- PostgreSQL storage — use standard backup, replication, and HA tools

## Quick Start

```bash
# Build
cargo build --release

# Initialize (creates databases, admin credentials, TLS cert, config file)
./target/release/extenddb init

# Start
./target/release/extenddb serve --config extenddb.toml

# Use with any AWS SDK (TLS with self-signed cert — trust via AWS_CA_BUNDLE)
export AWS_CA_BUNDLE=~/.extenddb/tls/cert.pem
aws dynamodb list-tables --endpoint-url https://127.0.0.1:8000 --region us-east-1
```

See [Getting Started](docs/getting-started.md) for the full walkthrough, or use the platform installer scripts:

```bash
scripts/install-linux.sh   # Linux
scripts/install-macos.sh   # macOS
```

## Prerequisites

- Rust 1.88+ (`rustup update`)
- PostgreSQL 14+ (see `docs/local-postgres-setup.md`)
- Python 3.10+ (for test suites and documentation)

### Python Environment

```bash
python3 -m venv ~/venvs/extenddb-venv
source ~/venvs/extenddb-venv/bin/activate
pip install -r requirements.txt
```

## Authentication Modes

ExtendDB ships with builtin IAM-like authentication enabled by default. All requests must be signed with valid SigV4 credentials created via the management API.

| Mode | Config | Description |
|------|--------|-------------|
| Builtin IAM-like | `auth.provider = "builtin"` | Full SigV4 signature verification with local credential store and IAM policy evaluation. This is the default and only supported mode. |

## Configuration

`extenddb init` generates `extenddb.toml` automatically. See `extenddb.sample.toml` for all keys, defaults, and descriptions.

Environment variable overrides use the `EXTENDDB__` prefix:

```bash
export EXTENDDB__SERVER__PORT=9000
export EXTENDDB__AUTH__PROVIDER=builtin
```

Runtime settings (no restart required):

```bash
extenddb settings --config extenddb.toml set log_level debug
```

## TLS

TLS is mandatory. `extenddb init` generates a self-signed certificate at `~/.extenddb/tls/cert.pem`. The server refuses to start with TLS disabled.

To use the self-signed cert with AWS CLI and SDKs, set `AWS_CA_BUNDLE`:

```bash
export AWS_CA_BUNDLE=~/.extenddb/tls/cert.pem
```

Replace with a CA-signed certificate for production:

```toml
[server.tls]
cert_path = "/etc/extenddb/tls/cert.pem"
key_path = "/etc/extenddb/tls/key.pem"
```

## Running in Containers

By default `extenddb serve` daemonizes itself, which doesn't play well with container runtimes and process supervisors that expect PID 1 to stay attached. Pass `--foreground` (alias `--no-daemon`) to keep the process in the foreground and stream logs to stderr instead of syslog:

```bash
extenddb serve --config extenddb.toml --foreground
```

Use this with Docker, Kubernetes, `systemd Type=simple`, runit, s6, or any other supervisor that captures stdout/stderr. `extenddb status` and `extenddb stop` continue to work as in daemon mode, since the PID file is still written.

## Monitoring

```bash
# Health check
curl --cacert ~/.extenddb/tls/cert.pem https://127.0.0.1:8000/health

# JSON metrics (DynamoDB CloudWatch-style)
curl --cacert ~/.extenddb/tls/cert.pem https://127.0.0.1:8000/metrics

# Syslog (Linux)
journalctl -t extenddb -f

# Syslog (macOS)
log stream --predicate 'processImagePath ENDSWITH "extenddb"' --level info
```

## Management Console

Web-based administration at `ht