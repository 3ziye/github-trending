<h1 align="center">Gridex</h1>

<p align="center">
  <strong>AI-native database IDE for macOS, Windows, and Linux.</strong><br>
  One app for PostgreSQL, MySQL, SQLite, Redis, MongoDB, SQL Server, and ClickHouse — with a built-in MCP server and AI chat.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/macOS-14%2B-blue" alt="macOS 14+">
  <img src="https://img.shields.io/badge/Windows-10%2B-0078D4" alt="Windows 10+">
  <img src="https://img.shields.io/badge/Linux-Qt%206-77BB44" alt="Linux Qt 6">
  <img src="https://img.shields.io/badge/Swift-5.10-orange" alt="Swift 5.10">
  <img src="https://img.shields.io/badge/license-Apache%202.0-blue" alt="License">
  <a href="https://discord.gg/UuV2Ktc6"><img src="https://img.shields.io/badge/chat-Discord-5865F2?logo=discord&logoColor=white" alt="Join Discord"></a>
</p>

<p align="center">
  <img src="assets/show-case.png" alt="Gridex overview" width="100%">
</p>

---

## Download

<p align="center">
  <a href="https://cdn.gridex.app/macos/Gridex-0.0.11-universal.dmg"><img src="https://img.shields.io/badge/Download-macOS-000000?style=for-the-badge&logo=apple&logoColor=white" alt="Download for macOS"></a>
  &nbsp;
  <a href="https://cdn.gridex.app/windows/Gridex-stable-Setup.exe"><img src="https://img.shields.io/badge/Download-Windows-0078D4?style=for-the-badge&logo=windows&logoColor=white" alt="Download for Windows"></a>
  &nbsp;
  <a href="https://cdn.gridex.app/linux/Gridex-latest-x86_64.AppImage"><img src="https://img.shields.io/badge/Download-Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="Download for Linux"></a>
</p>

<p align="center">
  <sub>
    <b>macOS</b> — universal DMG (Apple Silicon + Intel), signed &amp; notarized, auto-update via Sparkle ·
    <b>Windows</b> — Velopack installer, Windows 10/11 ·
    <b>Linux</b> — x86_64 AppImage, Qt 6, self-update from JSON feed
  </sub>
</p>

<p align="center">
  <sub>Looking for a specific version, delta updates, or checksums? See <a href="https://github.com/gridex/gridex/releases">all releases</a> or the <a href="https://gridex.app/download">download page</a>.</sub>
</p>

---

## Supported Databases

<p align="center">
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL">
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white" alt="Redis">
  <img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white" alt="MongoDB">
  <img src="https://img.shields.io/badge/SQL_Server-CC2927?style=for-the-badge&logo=microsoftsqlserver&logoColor=white" alt="SQL Server">
  <img src="https://img.shields.io/badge/ClickHouse-FFCC01?style=for-the-badge&logo=clickhouse&logoColor=black" alt="ClickHouse">
</p>

<p align="center">
  <em>Seven drivers in one native binary. All share the same <code>DatabaseAdapter</code> protocol (~50 methods) so every feature — grid, query editor, ER diagram, backup, MCP — works identically across engines.</em>
</p>

---

## Why Gridex

- **Native.** AppKit on macOS, WinUI 3 on Windows, Qt 6 on Linux. No Electron, no web views for the grid.
- **Multi-database.** Seven drivers on macOS, six on Linux/Windows (ClickHouse macOS-only for now), each with the right primitives (SCAN for Redis, aggregations for MongoDB, stored procedures for SQL Server, sequences for Postgres, MergeTree mutations for ClickHouse).
- **AI that sees your schema.** Claude, GPT, Gemini, and Ollama can read your tables, run read-only queries, and write SQL scoped to the connection you pick.
- **MCP server built in.** Plug Gridex into Claude Desktop, Cursor, or any MCP client over stdio — 13 tools with a 3-tier permission model and audit trail.
- **Credentials stay local.** macOS Keychain / Windows Credential Manager. No cloud sync, no telemetry, no proxy.

---

## Driver Highlights

| Database | Driver | Highlights |
|----------|--------|------------|
| **PostgreSQL** | [PostgresNIO](https://github.com/vapor/postgres-nio) | Parameterized queries, mTLS, sequences, full schema inspection |
| **MySQL** | [MySQLNIO](https://github.com/vapor/mysql-nio) | Charset handling, parameterized queries, TLS, auto-reconnect with keepalive |
| **SQLite** | System `libsqlite3` | File-based, WAL mode, zero config |
| **Redis** | [RediStack](https://github.com/swift-server/RediStack) | Key browser, SCAN filter, Server INFO dashboard, Slow Log viewer, `rediss://` TLS |
| **MongoDB** | [MongoKitten](https://github.com/orlandos-nl/MongoKitten) | Document editor, NDJSON backup/restore, aggregation pipeline |
| **SQL Server** | [CosmoSQLClient](https://github.com/vkuttyp/CosmoSQLClient-Swift) | TDS 7.4 (no FreeTDS), native `BACKUP DATABASE`,