<div align="center">
  <img src="./figures/walrus1.png"
       alt="walrus"
       width="30%">
    <div>Walrus: A high performance Write Ahead Log (WAL) in Rust</div>

[![Crates.io](https://img.shields.io/crates/v/walrus-rust.svg)](https://crates.io/crates/walrus-rust)
[![Documentation](https://docs.rs/walrus-rust/badge.svg)](https://docs.rs/walrus-rust)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)


</div>

## Features

- **High Performance**: Optimized for concurrent writes and reads
- **Topic-based Organization**: Separate read/write streams per topic
- **Configurable Consistency**: Choose between strict and relaxed consistency models
- **Memory-mapped I/O**: Efficient file operations using memory mapping
- **Persistent Read Offsets**: Read positions survive process restarts
- **Coordination-free Deletion**: Atomic file cleanup without blocking operations
- **Comprehensive Benchmarking**: Built-in performance testing suite

## Benchmarks

Run quick benchmarks with:

```bash
pip install pandas matplotlib # we need these to show graphs
make bench-and-show-reads
```

## Quick Start

Add Walrus to your `Cargo.toml`:

```toml
[dependencies]
walrus-rust = "0.1.0"
```

### Basic Usage

```rust
use walrus_rust::{Walrus, ReadConsistency};

// Create a new WAL instance with default settings
let wal = Walrus::new()?;

// Write data to a topic
let data = b"Hello, Walrus!";
wal.append_for_topic("my-topic", data)?;

// Read data from the topic
if let Some(entry) = wal.read_next("my-topic")? {
    println!("Read: {:?}", String::from_utf8_lossy(&entry.data));
}
```

### Advanced Configuration

```rust
use walrus_rust::{Walrus, ReadConsistency, FsyncSchedule};

// Configure with custom consistency and fsync behavior
let wal = Walrus::with_consistency_and_schedule(
    ReadConsistency::AtLeastOnce { persist_every: 1000 },
    FsyncSchedule::Milliseconds(500)
)?;

// Write and read operations work the same way
wal.append_for_topic("events", b"event data")?;
```

## Configuration Options

### Read Consistency Modes

Walrus supports two consistency models:

#### `ReadConsistency::StrictlyAtOnce`
- **Behavior**: Read offsets are persisted after every read operation
- **Guarantees**: No message will be read more than once, even after crashes
- **Performance**: Higher I/O overhead due to frequent persistence
- **Use Case**: Critical systems where duplicate processing must be avoided

```rust
let wal = Walrus::with_consistency(ReadConsistency::StrictlyAtOnce)?;
```

#### `ReadConsistency::AtLeastOnce { persist_every: u32 }`
- **Behavior**: Read offsets are persisted every N read operations
- **Guarantees**: Messages may be re-read after crashes (at-least-once delivery)
- **Performance**: Better throughput with configurable persistence frequency
- **Use Case**: High-throughput systems that can handle duplicate processing

```rust
let wal = Walrus::with_consistency(
    ReadConsistency::AtLeastOnce { persist_every: 5000 }
)?;
```

### Fsync Scheduling

Control when data is flushed to disk:

#### `FsyncSchedule::Milliseconds(u64)`
- **Behavior**: Background thread flushes data every N milliseconds
- **Default**: 1000ms (1 second)
- **Range**: Minimum 1ms, recommended 100-5000ms

```rust
let wal = Walrus::with_consistency_and_schedule(
    ReadConsistency::AtLeastOnce { persist_every: 1000 },
    FsyncSchedule::Milliseconds(2000)  // Flush every 2 seconds
)?;
```

### Environment Variables

- **`WALRUS_QUIET`**: Set to any value to suppress debug output during operations

```bash
export WALRUS_QUIET=1  # Suppress debug messages
```

## File Structure and Storage

Walrus organizes data in the following structure:

```
wal_files/
├── wal_1234567890.log          # Log files (10MB blocks, 100 blocks per file)
├── wal_1234567891.log
├── read_offset_idx_index.db    # Persistent read offset index
└── read_offset_idx_index.db.tmp # Temporary file for atomic updates
```

### Storage Configuration

- **Block Size**: 10MB per block (configurable via `DEFAULT_BLOCK_SIZE`)
- **Blocks Per File**: 100 blocks per file (1GB total per file)
- **Max File Size**: 1GB per log file
- **Index Persistence**: Read offsets stored in separate index files

## API Reference

### Core Methods

#### `Walrus::new() -> std::io::Result<Self>`
Creates a new WAL instance with default settings (`StrictlyAtOnce` consistency).

#### `Walrus::with_consistency(mode: ReadConsistency) -> std::io::Result<Self>`
Creates a WAL with custom consistency mode and default fsync schedule (1000ms).

#### `Walrus::with_consistency_and_schedule(mode: ReadConsistency, schedule: FsyncSchedule) -> std::io::Result<Self>`
Creates a WAL with full configuration control.

#### `append_for_topic(&self, topic: &str, data: &[u8]) -> std::io::Result<()>`
Appends data to the specified topic. Topics are created automatically on first write.

#### `read_next(&self, topic: &str) -> std::io::Result<Option<Entry>>`
Reads the next entry from the topic. Returns `None` if