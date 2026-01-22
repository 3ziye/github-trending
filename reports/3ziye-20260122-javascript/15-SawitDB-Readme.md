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
- **True Multi-Threading (NEW)**: Worker Pool architecture separates IO (Main Thread) from CPU (Worker Threads).
- **Advanced SQL (NEW)**: Support for `JOIN` (Left/Right/Full/Cross), `JAVING`, `DISTINCT`, and more.
- **NPM Support (NEW)**: Install via `npm install @wowoengine/sawitdb`.
- **AKAD Transactions (v3.0)**: ACID-compliant transactions with `MULAI AKAD`, `SAHKAN`, `BATALKAN`.
- **TEROPONG Views (v3.0)**: Virtual tables with `PASANG TEROPONG` and `BUANG TEROPONG`.
- **KENTONGAN Triggers (v3.0)**: Event hooks for INSERT/UPDATE/DELETE.
- **SOP Procedures (v3.0)**: Stored scripts with `SIMPAN SOP` and `JALANKAN SOP`.
- **CABANG Replication (v3.0)**: Primary-Replica synchronization via Change Data Capture.
- **DB Event & CDC (v3.0)**: Change Data Capture with `CPO` adapter and custom event hooks (`OnTableCreated`, `OnTableInserted`, etc).
- **BLUSUKAN Full-Text Search (v3.0)**: Inverted Index search with `BLUSUKAN KE ... CARI`.
- **POS RONDA Security (v3.0)**: Role-Based Access Control with `BERI IZIN` and `CABUT IZIN`.

## Filosofi

### Filosofi (ID)
SawitDB dibangun dengan semangat "Kemandirian Data". Kami percaya database yang handal tidak butuh **Infrastruktur Langit** yang harganya triliunan tapi sering *down*. Berbeda dengan proyek negara yang mahal di *budget* tapi murah di kualitas, SawitDB menggunakan arsitektur **Single File** (`.sawit`) yang hemat biaya. Backup cukup *copy-paste*, tidak perlu sewa vendor konsultan asing. Fitur **`fsync`** kami menjamin data tertulis di *disk*, karena bagi kami, integritas data adalah harga mati, bukan sekadar bahan konferensi pers untuk minta maaf.

### Philosophy (EN)
SawitDB is built with the spirit of "Data Sovereignty". We believe a reliable database doesn't need **"Sky Infrastructure"** that costs trillions yet goes *down* often. Unlike state projects that are expensive in budget but cheap in quality, SawitDB uses a cost-effective **Single File** (`.sawit`) architecture. Backup is just *copy-paste*, no need to hire expensive foreign consultants. Our **`fsync`** feature guarantees data is written to *disk*, because for us, data integrity is non-negotiable, not just material for a press conference to apologize.

## File List

- `src/WowoEngine.js`: Core Database Engine Entry Point.
- `src/SawitServer.js`: Server Class.
- `src/SawitClient.js`: Client Class.
- `src/modules/`: Core modules (QueryParser, BTreeIndex, WAL, Pager).
- `src/services/`: Logic services (TableManager, IndexManager, QueryExecutor).
- `src/service