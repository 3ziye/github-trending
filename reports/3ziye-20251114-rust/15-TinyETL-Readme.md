# TinyETL
**Fast, zero-config ETL in a single binary**

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/alrpal/tinyetl/actions)
[![Coverage](https://img.shields.io/badge/coverage-60%25-brightgreen)](https://github.com/alrpal/tinyetl/actions)
[![Version](https://img.shields.io/badge/version-0.1.0-blue)](https://github.com/alrpal/tinyetl/releases)
[![Rust Edition](https://img.shields.io/badge/rust-2021-orange)](https://doc.rust-lang.org/edition-guide/rust-2021/index.html)
[![Binary Size](https://img.shields.io/badge/binary-15MB-green)](https://github.com/alrpal/tinyetl/releases)

![TinyETL Demo](examples/tinyetl_preview2-normal-framerate.gif)

Transform and move data between any format or database **instantly**. No dependencies, no config files, just one command.

```bash
# MySQL → Parquet with inline transformation 
tinyetl "mysql://user:@host/db#orders" orders.parquet \
  --transform "total_usd=row.amount * row.exchange_rate"

# Stream 100k+ rows/sec from CSV → SQLite
tinyetl large_dataset.csv results.db --batch-size 50000

# Download & convert web data
tinyetl "https://api.data.gov/export.json" analysis.parquet
```

## Why TinyETL?

✅ **Single 12.5MB binary** — no dependencies, no installation headaches  
✅ **180k+ rows/sec streaming** — handles massive datasets efficiently  
✅ **Zero configuration** — automatic schema detection and table creation (override with schema and config files in yaml)  
   *Note: Auto-inferred schemas default all columns to nullable for safety*

✅ **Lua transformations** — powerful data transformations  
✅ **Universal connectivity** — CSV, JSON, Parquet, Avro, MySQL, PostgreSQL, SQLite, DuckDB, native MSSQL (currently slow). Coming soon: ODBC, Snowflake, Databricks, OneLake

✅ **Cross-platform** — Linux, macOS, Windows ready

## Quick Install

**Download the binary** (recommended):

Visit the [releases page](https://github.com/alrpal/tinyetl/releases/latest) and download the appropriate binary for your platform:
- Linux x64, Linux ARM64
- macOS Intel, macOS Apple Silicon  
- Windows x64, Windows ARM64

<!--
**Linux x64:**
```bash
curl -L https://github.com/alrpal/tinyetl/releases/latest/download/tinyetl-linux-x64.tar.gz | tar xz
chmod +x tinyetl
sudo mv tinyetl /usr/local/bin/  # Optional: add to PATH
```

**Linux ARM64:**
```bash
curl -L https://github.com/alrpal/tinyetl/releases/latest/download/tinyetl-linux-arm64.tar.gz | tar xz
chmod +x tinyetl
sudo mv tinyetl /usr/local/bin/  # Optional: add to PATH
```

**macOS Intel:**
```bash
curl -L https://github.com/alrpal/tinyetl/releases/latest/download/tinyetl-macos-intel.tar.gz | tar xz
chmod +x tinyetl
sudo mv tinyetl /usr/local/bin/  # Optional: add to PATH
```

**macOS Apple Silicon:**
```bash
curl -L https://github.com/alrpal/tinyetl/releases/latest/download/tinyetl-macos-apple-silicon.tar.gz | tar xz
chmod +x tinyetl
sudo mv tinyetl /usr/local/bin/  # Optional: add to PATH
```

**Windows x64:**
```powershell
# Download and extract using PowerShell
Invoke-WebRequest -Uri "https://github.com/alrpal/tinyetl/releases/latest/download/tinyetl-windows-x64.zip" -OutFile "tinyetl.zip"
Expand-Archive -Path "tinyetl.zip" -DestinationPath "."
# Move tinyetl.exe to a directory in your PATH
```

**Windows ARM64:**
```powershell
# Download and extract using PowerShell  
Invoke-WebRequest -Uri "https://github.com/alrpal/tinyetl/releases/latest/download/tinyetl-windows-arm64.zip" -OutFile "tinyetl.zip"
Expand-Archive -Path "tinyetl.zip" -DestinationPath "."
# Move tinyetl.exe to a directory in your PATH
```
-->

**Or install with Cargo** (builds from source):
```bash
cargo install tinyetl
```

**Verify installation**:
```bash
tinyetl --version
```

## Get Started in 30 Seconds

```bash
# File format conversion (auto-detects schemas)
tinyetl data.csv output.parquet
tinyetl data.json analysis.db

# Database to database 
tinyetl "postgresql://user:@host/db#users" "mysql://user:@host/db#users"

# Transform while transferring
tinyetl sales.csv results.db --transform "profit=row.revenue - row.costs; margin=profit/revenue"

# Process large datasets efficiently  
tinyetl huge_dataset.csv output.parquet --batch-size 100000

# Download and convert web data
tinyetl "https://example.com/api/export" local_data.json --source-type=csv

# Run complex ETL jobs from configuration files
tinyetl run my_etl_job.yaml
```

## Usage
<div style="overflow-x: auto;">

```
Usage: tinyetl [OPTIONS] <SOURCE> <TARGET>
       tinyetl run <CONFIG_FILE>

Direct Transfer:
  <SOURCE>  Source connection string (file path or connection string)
  <TARGET>  Target connection string (file path or connection string)

Config File Mode:
  run <CONFIG_FILE>  Run ETL job from YAML configuration file

Options:
      --infer-schema             Auto-detect columns and types
      --schema-file <FILE>       Path to schema file (YAML) to override auto-detection
      --batch-size <BATCH_SIZE>  Number of rows per batch [default: 10000]
      --previe