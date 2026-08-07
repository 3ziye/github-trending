# minisqlite

A reimplementation of SQLite in Rust: the SQL dialect, the query planner and
executor, transactions, and the storage engine, down to the official on-disk
file format. It opens database files that `sqlite3` wrote and writes files
that `sqlite3` reads back.

It is a library with a deliberately small surface: one type, four methods.
The implementation is about 200,000 lines of Rust across 14 crates, with
5,650 tests, one external dependency (`elsa`, for the page cache), and no
`unsafe` in library code.

```rust
use minisqlite::{Connection, Value};
use std::path::Path;

let mut db = Connection::open(Path::new("app.db"))?; // or Connection::open_in_memory()

db.execute(
    "CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT NOT NULL);
     INSERT INTO users(name) VALUES ('alice'), ('bob');",
)?;

let r = db.query("SELECT id, name FROM users WHERE name LIKE 'a%'")?;
assert_eq!(r.columns, ["id", "name"]);
assert!(matches!(&r.rows[0][1], Value::Text(name) if name == "alice"));
```

That is the whole public API: `Connection::{open, open_in_memory, execute,
query}`, plus the re-exported `Value`, `Row`, `QueryResult`, and `Error`
types. `execute` runs any number of `;`-separated statements; `query` returns
the last statement's result set. `Value` has exactly the five SQLite storage
classes: `Null`, `Integer(i64)`, `Real(f64)`, `Text(String)`, `Blob(Vec<u8>)`.
There is no CLI, no C API, and no prepared-statement interface.

Build and test with a recent stable toolchain (the workspace uses edition
2024):

```console
cargo build --workspace
cargo test  --workspace    # 5,650 tests, about 90 s
cargo bench                # scalability + durability measurement harness
```

## File compatibility

The on-disk format is SQLite's [format 3](https://sqlite.org/fileformat2.html),
in both directions:

```console
$ sqlite3 app.db "CREATE TABLE t(x); INSERT INTO t VALUES ('written by sqlite3')"
$ # ... open app.db with minisqlite, read that row, INSERT 'written by minisqlite' ...
$ sqlite3 app.db "SELECT x FROM t; PRAGMA integrity_check"
written by sqlite3
written by minisqlite
ok
```

This includes the hard cases: WAL databases with a live `-wal` file, UTF-16LE
and UTF-16BE text encodings, auto-vacuum databases with pointer-map pages,
overflow chains, freelists, page sizes from 512 to 65536 bytes, and databases
with reserved bytes at the end of each page. The format tests do not compare
against whatever the engine currently emits; they compare against byte
fixtures transcribed by hand from the file-format spec (see
[Testing](#testing)).

## What is implemented

**Queries.** Joins (`INNER`, `LEFT`, `RIGHT`, `FULL`, `CROSS`, `NATURAL`,
`USING`), `GROUP BY` / `HAVING`, `DISTINCT`, `ORDER BY` / `LIMIT` / `OFFSET`,
compound selects (`UNION [ALL]`, `INTERSECT`, `EXCEPT`), `VALUES`, row values,
scalar / `IN` / `EXISTS` subqueries including correlated ones, `WITH` and
`WITH RECURSIVE`, window functions with the full frame grammar (`ROWS` /
`RANGE` / `GROUPS`, all `EXCLUDE` modes, named `WINDOW` clauses), and the
three built-in collating sequences (`BINARY`, `NOCASE`, `RTRIM`).

**DML.** `INSERT` (`VALUES`, `SELECT`, `DEFAULT VALUES`), `UPDATE` (including
`FROM`), `DELETE`, upsert (`ON CONFLICT ... DO NOTHING / DO UPDATE`, multiple
clauses), `RETURNING`, and the five conflict policies (`OR ABORT / FAIL /
IGNORE / REPLACE / ROLLBACK`) with SQLite's exact undo scopes.

**DDL.** `CREATE` / `DROP` for tables, indexes (`UNIQUE`, partial, on
expressions), views, and triggers (`BEFORE` / `AFTER` / `INSTEAD OF`, `WHEN`,
recursion gated by `PRAGMA recursive_triggers`); `CREATE TABLE ... AS SELECT`;
`ALTER TABLE` (`RENAME TO`, `RENAME COLUMN`, `ADD COLUMN`, `DROP COLUMN`);
`WITHOUT ROWID` tables; generated columns (`VIRTUAL` and `STORED`);
`AUTOINCREMENT` with `sqlite_sequence`.

**Constraints.** `PRIMARY KEY`, `UNIQUE`, `NOT NULL`, `CHECK`, `DEFAULT`, and
foreign keys (`CASCADE`, `SET NULL`, `SET DEFAULT`, `RESTRICT`, `NO ACTION`),
plus deferred constraints rechecked at commit (`DEFERRABLE INITIALLY
DEFERRED`, `PRAGMA defer_foreign_keys`). Constraint errors carry SQLite's
extended result codes and message shapes (`UNIQUE constraint failed: t.x`).

**Transactions.** `BEGIN` / `COMMIT` / `ROLLBACK` and nested `SAVEPOINT` /
`RELEASE` / `ROLLBACK TO`. Statements outside a transaction autocommit.

**Namespaces.** `temp` tables (created lazily, shadow `main` in SQLite's
resolution order), `ATTACH` / `DETACH`, qualified names (`main.t`, `aux.t`),
and cross-database queries, DML, and triggers. An implicit transaction spans
every attached database.

**Functions.** About 90 built-ins: the core string / math / blob scalars
(`printf`/`format`, `substr`, `instr`, `hex`/`unhex`, `quote`, `round`, the
full libm set from `acos` to `trunc`, ...), aggregates (`count`, `sum`,
`total`, `avg`, `min`, `max`, `group_concat`/`string_agg`) with `DISTINCT`,
`FILTER`, and aggregate `ORDER BY`, all eleven window functions, date/time
functions (`date`, `time`, 