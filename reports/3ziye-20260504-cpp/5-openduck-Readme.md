# OpenDuck

OpenDuck makes DuckDB work like a cloud database without giving up its embedded-DB feel. You attach a remote database in one line — `ATTACH 'openduck:mydb'` — tables resolve transparently, a single query can split its work across your laptop and a remote worker, and storage underneath is layered, snapshot-based, and concurrency-safe. It's a DuckDB extension plus a small Rust gateway/worker speaking an open gRPC + Arrow IPC protocol, so you self-host the whole thing or plug your own backend in.

The architecture follows the path [MotherDuck](https://motherduck.com) pioneered with [differential storage](https://motherduck.com/blog/differential-storage-building-block-for-data-warehouse/), [dual execution](https://motherduck.com/videos/bringing-duckdb-to-the-cloud-dual-execution-explained/), and the `md:` attach scheme. OpenDuck reimplements those ideas as an open protocol and an open backend you can run yourself.

```python
import duckdb

con = duckdb.connect(config={"allow_unsigned_extensions": "true"})
con.execute("LOAD '/path/to/openduck.duckdb_extension';")
con.execute("ATTACH 'openduck:mydb?endpoint=http://localhost:7878&token=xxx' AS cloud;")

con.sql("SELECT * FROM cloud.users").show()                    # remote, transparent
con.sql("SELECT * FROM local.t JOIN cloud.t2 ON ...").show()   # hybrid, one query
```

## What OpenDuck does

### Differential storage

Append-only layers with PostgreSQL metadata. DuckDB sees a normal file; OpenDuck persists data as immutable sealed layers addressable from object storage. Snapshots give you consistent reads. One serialized write path, many concurrent readers.

### Hybrid (dual) execution

A single query can run partly on your machine and partly on a remote worker. The gateway splits the plan, labels each operator `LOCAL` or `REMOTE`, and inserts bridge operators at the boundaries. Only intermediate results cross the wire.

```
[LOCAL]  HashJoin(l.id = r.id)
  [LOCAL]  Scan(products)          ← your laptop
  [LOCAL]  Bridge(R→L)
    [REMOTE] Scan(sales)           ← remote worker
```

### DuckDB-native catalog

The extension implements DuckDB's `StorageExtension` and `Catalog` interfaces. Remote tables are first-class catalog entries, they participate in JOINs, CTEs, and the optimizer like local tables.

### Open protocol

OpenDuck's protocol is intentionally minimal and defined in [`execution.proto`](proto/openduck/v1/execution.proto). The data plane is two RPCs: one to execute a query and stream Arrow IPC batches back, another to cancel a running execution. Two additional RPCs handle worker lifecycle (registration and heartbeat) so the gateway can route queries by database affinity and compute context.

Because the protocol is open and simple, you're not locked into a single backend. Any service that speaks gRPC and returns Arrow can serve as an OpenDuck-compatible backend. Run the included Rust gateway, replace it with your own implementation, or plug in an entirely different execution engine — the client and extension don't care what's on the other side.

## Architecture

```
┌─────────────────────────────────────────────┐
│  DuckDB process (client)                    │
│                                             │
│  LOAD openduck                              │
│  ATTACH 'openduck:mydb' AS cloud            │
│                                             │
│  ┌─────────────────────────────────────┐    │
│  │ OpenDuckCatalog                     │    │
│  │  └─ OpenDuckSchemaEntry             │    │
│  │      └─ OpenDuckTableEntry (users)  │    │
│  │      └─ OpenDuckTableEntry (events) │    │
│  └──────────────┬──────────────────────┘    │
│                 │ gRPC + Arrow IPC          │
└─────────────────┼───────────────────────────┘
                  │
      ┌───────────▼───────────┐
      │  Gateway (Rust)       │
      │  - token auth         │
      │  - worker registry    │
      │  - affinity routing   │     ┌──────────────┐
      │  - plan splitting     │────▶│  Worker 1    │
      │  - backpressure       │◀────│  (DuckDB)    │
      │                       │     │  RegisterWorker
      │                       │     └──────────────┘
      │                       │     ┌──────────────┐
      │                       │────▶│  Worker N    │
      │                       │◀────│  (DuckDB)    │
      │                       │     │  Heartbeat   │
      └───────────────────────┘     └──────────────┘
              │
    ┌─────────┴─────────┐
    ▼                   ▼
┌──────────┐    ┌──────────────┐
│ Postgres │    │ Object store │
│ metadata │    │ sealed layers│
└──────────┘    └──────────────┘
```

## Quick start

### 1. Build the backend

```bash
cargo build --workspace
```

### 2. Build the DuckDB extension

The openduck extension is not yet published to DuckDB's extension repository, so you need to build it from source. See [`extensions/openduck/README.md`](extensions/openduck/README.md) for full prerequisites (vcpkg, bison on macOS).

```bash