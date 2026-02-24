# sql-tap

[![Sponsor](https://img.shields.io/badge/Sponsor-❤-ea4aaa?style=flat-square&logo=github)](https://github.com/sponsors/mickamy)

Real-time SQL traffic viewer — proxy daemon + TUI / Web client.

sql-tap sits between your application and your database (PostgreSQL, MySQL, or TiDB), capturing every query and
displaying it in an interactive terminal UI. Inspect queries, view transactions, and run EXPLAIN — all without changing
your application code.

![tui](./docs/tui.gif)
![web](./docs/web.png)

## Installation

### Homebrew

```bash
brew install --cask mickamy/tap/sql-tap
```

### Go

```bash
go install github.com/mickamy/sql-tap@latest
go install github.com/mickamy/sql-tap/cmd/sql-tapd@latest
```

### Build from source

```bash
git clone https://github.com/mickamy/sql-tap.git
cd sql-tap
make install
```

### Docker

**PostgreSQL**

```dockerfile
FROM postgres:18-alpine
ARG SQL_TAP_VERSION=0.0.1
ARG TARGETARCH
ADD https://github.com/mickamy/sql-tap/releases/download/v${SQL_TAP_VERSION}/sql-tap_${SQL_TAP_VERSION}_linux_${TARGETARCH}.tar.gz /tmp/sql-tap.tar.gz
RUN tar -xzf /tmp/sql-tap.tar.gz -C /usr/local/bin sql-tapd && rm /tmp/sql-tap.tar.gz
ENTRYPOINT ["sql-tapd", "--driver=postgres", "--listen=:5433", "--upstream=localhost:5432", "--grpc=:9091"]
```

**MySQL**

```dockerfile
FROM mysql:8
ARG SQL_TAP_VERSION=0.0.1
ARG TARGETARCH
ADD https://github.com/mickamy/sql-tap/releases/download/v${SQL_TAP_VERSION}/sql-tap_${SQL_TAP_VERSION}_linux_${TARGETARCH}.tar.gz /tmp/sql-tap.tar.gz
RUN tar -xzf /tmp/sql-tap.tar.gz -C /usr/local/bin sql-tapd && rm /tmp/sql-tap.tar.gz
ENTRYPOINT ["sql-tapd", "--driver=mysql", "--listen=:3307", "--upstream=localhost:3306", "--grpc=:9091"]
```

## Quick start

**1. Start the proxy daemon**

```bash
# PostgreSQL: proxy listens on :5433, forwards to PostgreSQL on :5432
DATABASE_URL="postgres://user:pass@localhost:5432/db?sslmode=disable" \
  sql-tapd --driver=postgres --listen=:5433 --upstream=localhost:5432

# MySQL: proxy listens on :3307, forwards to MySQL on :3306
DATABASE_URL="user:pass@tcp(localhost:3306)/db" \
  sql-tapd --driver=mysql --listen=:3307 --upstream=localhost:3306

# TiDB: proxy listens on :4001, forwards to TiDB on :4000
DATABASE_URL="user:pass@tcp(localhost:4000)/db" \
  sql-tapd --driver=tidb --listen=:4001 --upstream=localhost:4000
```

**2. Point your application at the proxy**

Connect your app to the proxy port instead of the database port. No code changes needed — sql-tapd speaks the native
wire protocol.

**3. Launch the TUI**

```bash
sql-tap localhost:9091
```

All queries flowing through the proxy appear in real-time.

## Usage

### sql-tapd

```
sql-tapd — SQL proxy daemon for sql-tap

Usage:
  sql-tapd [flags]

Flags:
  -driver    database driver: postgres, mysql, tidb (required)
  -listen    client listen address (required)
  -upstream  upstream database address (required)
  -grpc      gRPC server address for TUI (default: ":9091")
  -http      HTTP server address for web UI (e.g. ":8080")
  -dsn-env   env var holding DSN for EXPLAIN (default: "DATABASE_URL")
  -nplus1-threshold  N+1 detection threshold (default: 5, 0 to disable)
  -nplus1-window     N+1 detection time window (default: 1s)
  -nplus1-cooldown   N+1 alert cooldown per query template (default: 10s)
  -version   show version and exit
```

Set `DATABASE_URL` (or the env var specified by `-dsn-env`) to enable EXPLAIN support. Without it, the proxy still
captures queries but EXPLAIN is disabled.

### Web UI

Add `--http=:8080` to serve a browser-based viewer:

```bash
DATABASE_URL="postgres://user:pass@localhost:5432/db?sslmode=disable" \
  sql-tapd --driver=postgres --listen=:5433 --upstream=localhost:5432 --http=:8080
```

Open `http://localhost:8080` in your browser to view queries in real-time. The web UI supports:

- Real-time query stream via SSE
- Click to inspect query details
- EXPLAIN / EXPLAIN ANALYZE
- Text filter
- Copy query (with or without bound args)
- N+1 detection (toast + row highlight)

### sql-tap

```
sql-tap — Watch SQL traffic in real-time

Usage:
  sql-tap [flags] <addr>

Flags:
  -version  Show version and exit
```

`<addr>` is the gRPC address of sql-tapd (e.g. `localhost:9091`).

## Keybindings

### List view

| Key               | Action                                 |
|-------------------|----------------------------------------|
| `j` / `↓`         | Move down                              |
| `k` / `↑`         | Move up                                |
| `Ctrl+d` / `PgDn` | Half-page down                         |
| `Ctrl+u` / `PgUp` | Half-page up                           |
| `/`               | Incremental text search                |
| `f`               | Structured filter (see below)          |
| `s`               | Toggle sort (chronological/duration)   |
| `Enter`           | Inspect query / transaction            |
| `Space`           | Toggle transaction expand / collapse   |
| `Esc`             | Clear search / filter                  |
| 