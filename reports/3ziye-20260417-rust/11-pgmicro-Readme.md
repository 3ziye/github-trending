<p align="center">
  <img src="pgmicro-logo.png" alt="pgmicro" width="600"/>
</p>

# pgmicro

An in-process reimplementation of PostgreSQL, backed by a SQLite-compatible storage engine.

pgmicro is built as an experimental fork of [Turso](https://github.com/tursodatabase/turso) — a full from-scratch rewrite of SQLite in Rust — with PostgreSQL added as a native dialect. The result is a fast, embeddable, single-file database that speaks PostgreSQL.

## Why?

AI agents are driving an explosion of databases. Many of them are ephemeral, low-touch, short-lived, and small — a scratch database for a task, a session store that lives for minutes, a per-user sandbox.

SQLite has traditionally been king in these environments, and it's easy to see why: it's just a file (or even in-memory), no server to manage, no ports to configure. But many developers prefer PostgreSQL — whether out of familiarity, taste, or because PostgreSQL is legitimately more powerful in areas like its type system, JSON operators, and query capabilities.

Other approaches to bring PostgreSQL in-process try to compile PostgreSQL itself to WebAssembly. But PostgreSQL's architecture — particularly its process-per-connection model, shared memory assumptions, and reliance on a full OS environment — makes this fundamentally constrained. You end up fighting the architecture rather than benefiting from it.

pgmicro takes a different path entirely.

## How is pgmicro different?

pgmicro does not translate PostgreSQL to SQLite syntax. It does not embed or compile PostgreSQL. Instead, it **parses the PostgreSQL language and compiles it directly to SQLite bytecode**.

Here's how it works:

```
                        pgmicro architecture
                        ====================

  PostgreSQL SQL                          SQLite SQL
       │                                      │
       ▼                                      ▼
 ┌─────────────┐                       ┌───────────-──┐
 │ libpg_query │                       │ Turso Parser │
 │ (PG parser) │                       │ (SQLite)     │
 └─────┬───────┘                       └──────┬─────-─┘
       │ PG parse tree                        │ SQLite AST
       ▼                                      │
 ┌─────────────┐                              │
 │  Translator │──── Turso AST ──────────────►│
 │ (parser_pg) │                              │
 └─────────────┘                              ▼
                                    ┌──────────────────┐
                                    │  Turso Compiler  │
                                    │ (translate/*.rs) │
                                    └────────┬─────────┘
                                             │ VDBE bytecode
                                             ▼
                                    ┌──────────────────┐
                                    │  Bytecode Engine │
                                    │  (vdbe/*.rs)     │
                                    └────────┬─────────┘
                                             │
                                             ▼
                                    ┌────────────────────┐
                                    │  SQLite Storage    │
                                    │ (B-tree, WAL, etc) │
                                    └────────────────────┘
```

The key pieces:

- **PostgreSQL parser**: We use [`libpg_query`](https://github.com/pganalyze/libpg_query) (via the [`pg_query`](https://crates.io/crates/pg_query) Rust crate), which extracts PostgreSQL's *actual* parser from the PostgreSQL source code. This means pgmicro parses PostgreSQL syntax with 100% fidelity — it's the same parser PostgreSQL itself uses. We did not write a PostgreSQL parser.

- **Translator** (`parser_pg/`): A translation layer that converts the PostgreSQL parse tree into Turso's internal AST. This handles the mapping of PostgreSQL-specific syntax (e.g., `$$dollar quoting$$`, `::` casts, `SERIAL` types, PostgreSQL-style `CREATE TABLE`) into the representation that Turso's compiler understands.

- **Turso engine**: The full [Turso](https://github.com/tursodatabase/turso) database engine — a complete, from-scratch reimplementation of SQLite in Rust. It compiles the AST to bytecode and executes it against a SQLite-compatible B-tree storage format. Your data lives in a standard `.db` file.

- **PostgreSQL catalog**: Virtual tables (`pg_class`, `pg_attribute`, `pg_type`, `pg_namespace`, etc.) that expose schema metadata in the way PostgreSQL tools expect, enabling compatibility with `psql` and other PostgreSQL clients.

- **Dialect switching**: Turso supports dynamic dialect switching at the connection level. A single database can be accessed via both PostgreSQL and SQLite syntax — useful for tooling, migration, and interop.

## Installation

### CLI

Run directly with npx (no install needed):

```
npx pg-micro
```

Or install globally:

```
npm install -g pg-micro
pg-micro myapp.db
```

### JavaScript/TypeScript SDK

```