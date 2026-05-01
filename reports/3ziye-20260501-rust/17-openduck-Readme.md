# OpenDuck

An open-source implementation of the ideas pioneered by [MotherDuck](https://motherduck.com) — differential storage, hybrid (dual) execution, and transparent remote databases for DuckDB — available for anyone to run, extend, and build on.

MotherDuck showed that DuckDB can work beautifully in the cloud: `ATTACH 'md:mydb'`, and remote tables appear local. Queries split transparently across your laptop and the cloud. Storage is layered and snapshot-based. OpenDuck takes those architectural ideas — [differential storage](https://motherduck.com/blog/differential-storage-building-block-for-data-warehouse/), [dual execution](https://motherduck.com/videos/bringing-duckdb-to-the-cloud-dual-execution-explained/), the attach-based UX — and makes them open. Open protocol, open backend, open extension.

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
cd extensions/openduck && make
```

This produces the loadable binary at:

```
extensions/openduck/build/release/extensio