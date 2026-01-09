<div align="center">
  <img src="logo.svg" alt="Stoolap Logo" width="360">

  <h3>A Modern Embedded SQL Database in Pure Rust</h3>

  <p>
    <a href="https://stoolap.io">Website</a> •
    <a href="https://stoolap.io/docs">Documentation</a> •
    <a href="https://github.com/stoolap/stoolap/releases">Releases</a> •
    <a href="BENCHMARKS.md">Benchmarks</a>
  </p>

  <p>
    <a href="https://github.com/stoolap/stoolap/actions/workflows/ci.yml"><img src="https://github.com/stoolap/stoolap/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
    <a href="https://codecov.io/gh/stoolap/stoolap"><img src="https://codecov.io/gh/stoolap/stoolap/branch/main/graph/badge.svg" alt="codecov"></a>
    <a href="https://crates.io/crates/stoolap"><img src="https://img.shields.io/crates/v/stoolap.svg" alt="Crates.io"></a>
    <a href="https://github.com/stoolap/stoolap/releases"><img src="https://img.shields.io/github/v/release/stoolap/stoolap" alt="GitHub release"></a>
    <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache%202.0-blue.svg" alt="License"></a>
  </p>
</div>

---

## Why Stoolap?

Stoolap is a **feature-rich embedded SQL database** with capabilities that rival established databases like PostgreSQL and DuckDB - all in a single dependency with zero external requirements.

### Performance

```
┌───────────────────────────────────────────────────────────────┐
│   STOOLAP vs SQLite:    44 wins / 9 losses    (83% win rate)  │
│   STOOLAP vs DuckDB:    50 wins / 3 losses    (94% win rate)  │
└───────────────────────────────────────────────────────────────┘
```

See [BENCHMARKS.md](BENCHMARKS.md) for detailed comparisons.

### Unique Features

| Feature | Stoolap | SQLite | DuckDB | PostgreSQL |
|---------|:-------:|:------:|:------:|:----------:|
| **AS OF Time-Travel Queries** | ✅ | ❌ | ❌ | ❌* |
| **MVCC Transactions** | ✅ | ❌ | ✅ | ✅ |
| **Cost-Based Optimizer** | ✅ | ❌ | ✅ | ✅ |
| **Adaptive Query Execution** | ✅ | ❌ | ❌ | ❌ |
| **Semantic Query Caching** | ✅ | ❌ | ❌ | ❌ |
| **Parallel Query Execution** | ✅ | ❌ | ✅ | ✅ |
| **Pure Rust (Memory Safe)** | ✅ | ❌ | ❌ | ❌ |
| **No C/C++ Required** | ✅ | ❌ | ❌ | ❌ |

*PostgreSQL requires extensions for temporal queries

---

## Quick Start

### Installation

Add to your `Cargo.toml`:

```toml
[dependencies]
stoolap = "0.2"
```

Or build from source:

```bash
git clone https://github.com/stoolap/stoolap.git
cd stoolap
cargo build --release
```

### Library Usage

```rust
use stoolap::api::Database;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // In-memory database
    let db = Database::open_in_memory()?;

    // Or persistent storage
    // let db = Database::open("file:///path/to/data")?;

    // Create table
    db.execute("CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )", ())?;

    // Insert with parameters
    db.execute("INSERT INTO users (id, name, email) VALUES (?, ?, ?)",
        (1, "Alice", "alice@example.com"))?;

    // Query with iteration
    for row in db.query("SELECT * FROM users WHERE id = ?", (1,))? {
        let row = row?;
        println!("User: {} <{}>",
            row.get::<String>(1)?,  // name
            row.get::<String>(2)?   // email
        );
    }

    Ok(())
}
```

### Command Line Interface

```bash
# Interactive REPL (in-memory)
./stoolap

# Persistent database
./stoolap --db "file:///var/lib/stoolap/data"

# Execute query directly
./stoolap -q "SELECT version()"

# Execute SQL file
./stoolap --db "file://./mydb" < schema.sql
```

---

## Features

### MVCC Transactions

Full multi-version concurrency control with isolation levels:

```sql
-- Read Committed (default)
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;

-- Snapshot Isolation (repeatable reads)
BEGIN TRANSACTION ISOLATION LEVEL SNAPSHOT;
SELECT * FROM accounts;  -- Consistent view throughout transaction
COMMIT;
```

### Time-Travel Queries

Query historical data at any point in time - a feature typically only found in enterprise databases:

```sql
-- Query data as it existed at a specific timestamp
SELECT * FROM orders AS OF TIMESTAMP '2024-01-15 10:30:00';

-- Query data as of a specific transaction
SELECT * FROM inventory AS OF TRANSACTION 1234;

-- Compare current vs historical data
SELECT
    c.price AS current_price,
    h.price AS old_price,
    c.price - h.price AS change
FROM products c
JOIN products AS OF TIMESTAMP '2024-01-01 00:00:00' h ON c.id = h.id
WHERE c.price != h.price;
```

### Smart Indexes

Automatic index type selection based on data characteristics:

```sql
-- B-tree (auto-selected for INTEGER, FLOAT, TIMESTAMP)
-- Best for: range queries, sorting, prefix matching
CREATE INDEX idx_date ON orders(created_at);
SELECT * FROM orders WHERE created_at BETWEEN '2024-01-01' AND '2024-12-31';

-- Hash (auto-selected for TEXT, JS