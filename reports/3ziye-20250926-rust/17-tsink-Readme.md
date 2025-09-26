# tsink

<div align="center">

<p align="right">
  <img src="https://raw.githubusercontent.com/h2337/tsink/refs/heads/master/logo.svg" width="250" height="250">
</p>

**A high-performance embedded time-series database for Rust**

</div>

## Overview

tsink is a lightweight, high-performance time-series database engine written in Rust. It provides efficient storage and retrieval of time-series data with automatic compression, time-based partitioning, and thread-safe operations.

### Key Features

- **🚀 High Performance**: Gorilla compression achieves ~1.37 bytes per data point
- **🔒 Thread-Safe**: Lock-free reads and concurrent writes with configurable worker pools
- **💾 Flexible Storage**: Choose between in-memory or persistent disk storage
- **📊 Time Partitioning**: Automatic data organization by configurable time ranges
- **🏷️ Label Support**: Multi-dimensional metrics with key-value labels
- **📝 WAL Support**: Write-ahead logging for durability and crash recovery
- **🗑️ Auto-Retention**: Configurable automatic data expiration
- **🐳 Container-Aware**: cgroup support for optimal resource usage in containers
- **⚡ Zero-Copy Reads**: Memory-mapped files for efficient disk operations

## Installation

Add tsink to your `Cargo.toml`:

```toml
[dependencies]
tsink = "0.3.1"
```

## Quick Start

### Basic Usage

```rust
use tsink::{DataPoint, Row, StorageBuilder, Storage, TimestampPrecision};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Create storage with default settings
    let storage = StorageBuilder::new()
        .with_timestamp_precision(TimestampPrecision::Seconds)
        .build()?;

    // Insert data points
    let rows = vec![
        Row::new("cpu_usage", DataPoint::new(1600000000, 45.5)),
        Row::new("cpu_usage", DataPoint::new(1600000060, 47.2)),
        Row::new("cpu_usage", DataPoint::new(1600000120, 46.8)),
    ];
    storage.insert_rows(&rows)?;

    // Note: Using timestamp 0 will automatically use the current timestamp
    // let row = Row::new("cpu_usage", DataPoint::new(0, 50.0));  // timestamp = current time

    // Query data points
    let points = storage.select("cpu_usage", &[], 1600000000, 1600000121)?;
    for point in points {
        println!("Timestamp: {}, Value: {}", point.timestamp, point.value);
    }

    storage.close()?;
    Ok(())
}
```

### Persistent Storage

```rust
use tsink::{StorageBuilder, Storage};
use std::time::Duration;

let storage = StorageBuilder::new()
    .with_data_path("./tsink-data")              // Enable disk persistence
    .with_partition_duration(Duration::from_secs(3600))  // 1-hour partitions
    .with_retention(Duration::from_secs(7 * 24 * 3600))  // 7-day retention
    .with_wal_buffer_size(8192)                  // 8KB WAL buffer
    .build()?;
```

### Multi-Dimensional Metrics with Labels

```rust
use tsink::{DataPoint, Label, Row};

// Create metrics with labels for detailed categorization
let rows = vec![
    Row::with_labels(
        "http_requests",
        vec![
            Label::new("method", "GET"),
            Label::new("status", "200"),
            Label::new("endpoint", "/api/users"),
        ],
        DataPoint::new(1600000000, 150.0),
    ),
    Row::with_labels(
        "http_requests",
        vec![
            Label::new("method", "POST"),
            Label::new("status", "201"),
            Label::new("endpoint", "/api/users"),
        ],
        DataPoint::new(1600000000, 25.0),
    ),
];

storage.insert_rows(&rows)?;

// Query specific label combinations
let points = storage.select(
    "http_requests",
    &[
        Label::new("method", "GET"),
        Label::new("status", "200"),
    ],
    1600000000,
    1600000100,
)?;

// Query all label combinations for a metric
let all_results = storage.select_all("http_requests", 1600000000, 1600000100)?;
for (labels, points) in all_results {
    println!("Labels: {:?}, Points: {}", labels, points.len());
}
```

## Architecture

tsink uses a linear-order partition model that divides time-series data into time-bounded chunks:

```
┌─────────────────────────────────────────┐
│             tsink Storage               │
├─────────────────────────────────────────┤
│                                         │
│  ┌───────────────┐  Active Partition    │
│  │ Memory Part.  │◄─ (Writable)         │
│  └───────────────┘                      │
│                                         │
│  ┌───────────────┐  Buffer Partition    │
│  │ Memory Part.  │◄─ (Out-of-order)     │
│  └───────────────┘                      │
│                                         │
│  ┌───────────────┐                      │
│  │ Disk Part. 1  │◄─ Read-only          │
│  └───────────────┘   (Memory-mapped)    │
│                                         │
│  ┌───────────────┐                      │
│  │ Disk Part. 2  │◄─ Read-only          │
│  └───────────────┘                      │
│         ...                             │
└─────────────────────────────────────────┘
```

### Partition 