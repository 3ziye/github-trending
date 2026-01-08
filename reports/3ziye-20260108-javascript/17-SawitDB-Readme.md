# SawitDB

![SawitDB Banner](docs/sawitdb.jpg)

<div align="center">

[![Docs](https://img.shields.io/badge/Docs-Read%20Now-blue?style=for-the-badge&logo=googledocs)](https://wowoengine.github.io/SawitDB/)
[![NPM](https://img.shields.io/npm/v/@wowoengine/sawitdb?style=for-the-badge&logo=npm)](https://www.npmjs.com/package/@wowoengine/sawitdb)
[![Go Version](https://img.shields.io/badge/Go%20Version-Visit%20Repo-cyan?style=for-the-badge&logo=go)](https://github.com/WowoEngine/SawitDB-Go)
[![Changelog](https://img.shields.io/badge/Changelog-Read%20Updates-orange?style=for-the-badge&logo=github)](CHANGELOG.md)

</div>


**SawitDB** is a unique database solution stored in `.sawit` binary files.

The system features a custom **Hybrid Paged Architecture** similar to SQLite but supercharged with **Object Caching**, using fixed-size 4KB pages to ensure efficient memory usage and near-instant access. What differentiates SawitDB is its unique **Agricultural Query Language (AQL)**, which replaces standard SQL keywords with Indonesian farming terminology.

**Now available on NPM!** Connect via TCP using `sawitdb://` protocol.

**🚨 Emergency: Aceh Flood Relief**
Please support our brothers and sisters in Aceh.

[![Kitabisa](https://img.shields.io/badge/Kitabisa-Bantu%20Aceh-blue?style=flat&logo=heart)](https://kitabisa.com/campaign/donasipedulibanjiraceh)

*Organized by Human Initiative Aceh*

## Features

- **Hybrid Paged Architecture**: Data is stored in 4096-byte binary pages, but hot data is cached as native Objects for zero-copy reads.
- **Single File Storage**: All data, schema, and indexes are stored in a single `.sawit` file.
- **High Stability**: Uses 4KB atomic pages. More stable than a coalition government.
- **Data Integrity (Anti-Korupsi)**: Implements strict `fsync` protocols. Data cannot be "corrupted" or "disappear" mysteriously like social aid funds (Bansos). No "Sunat Massal" here.
- **Crash Recovery**: Uses **Write-Ahead Logging (WAL)**. Guarantees data always returns after a crash. Unlike a fugitive (Buronan) who is "hard to find".
- **Zero Bureaucracy (Zero Deps)**: Built entirely with standard Node.js. No unnecessary "Vendor Pengadaan" or "Mark-up Anggaran".
- **Transparansi**: Query language is clear. No "Pasal Karet" (Ambiguous Laws) or "Rapat Tertutup" in 5-star hotels.
- **Speed**: Faster than printing an e-KTP at the Kelurahan.
- **Network Support (NEW)**: Client-Server architecture with Multi-database support and Authentication.
- **NPM Support (NEW)**: Install via `npm install @wowoengine/sawitdb`.

## Filosofi

### Filosofi (ID)
SawitDB dibangun dengan semangat "Kemandirian Data". Kami percaya database yang handal tidak butuh **Infrastruktur Langit** yang harganya triliunan tapi sering *down*. Berbeda dengan proyek negara yang mahal di *budget* tapi murah di kualitas, SawitDB menggunakan arsitektur **Single File** (`.sawit`) yang hemat biaya. Backup cukup *copy-paste*, tidak perlu sewa vendor konsultan asing. Fitur **`fsync`** kami menjamin data tertulis di *disk*, karena bagi kami, integritas data adalah harga mati, bukan sekadar bahan konferensi pers untuk minta maaf.

### Philosophy (EN)
SawitDB is built with the spirit of "Data Sovereignty". We believe a reliable database doesn't need **"Sky Infrastructure"** that costs trillions yet goes *down* often. Unlike state projects that are expensive in budget but cheap in quality, SawitDB uses a cost-effective **Single File** (`.sawit`) architecture. Backup is just *copy-paste*, no need to hire expensive foreign consultants. Our **`fsync`** feature guarantees data is written to *disk*, because for us, data integrity is non-negotiable, not just material for a press conference to apologize.

## File List

- `src/WowoEngine.js`: Core Database Engine (Class: `SawitDB`).
- `bin/sawit-server.js`: Server executable.
- `cli/local.js`: Interactive CLI tool (Local).
- `cli/remote.js`: Interactive CLI tool (Network).
- [CHANGELOG.md](CHANGELOG.md): Version history and release notes.
- `cli/test.js`: Unit Test Suite.
- `cli/benchmark.js`: Performance Benchmark Tool.
- `examples/`: Sample scripts.

## Installation

Install via NPM:

```bash
npm install @wowoengine/sawitdb
```

## Quick Start (Network Edition)

### 1. Start the Server
```bash
node src/SawitServer.js
```
The server will start on `0.0.0.0:7878` by default.

### 2. Connect with Client
Use [SawitClient](#client-api) or any interactive session.

---

## Dual Syntax Support

SawitDB introduces the **Generic Syntax** alongside the classic **Agricultural Query Language (AQL)**, making it easier for developers familiar with standard SQL to adopt.

| Operation | Agricultural Query Language (AQL) | Generic SQL (Standard) |
| :--- | :--- | :--- |
| **Create DB** | `BUKA WILAYAH sales_db` | `CREATE DATABASE sales_db` |
| **Use DB** | `MASUK WILAYAH sales_db` | `USE sales_db` |
| **Show DBs** | `LIHAT WILAYAH` | `SHOW DATABASES` |
| **Drop DB** | `BAKAR WILAYAH sales_db` | `DROP DATABASE sales_db` |
| **