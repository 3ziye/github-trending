# 🎵 Music Auto Tagger | Automated Music Library Organizer

<div align="center">

[![Java](https://img.shields.io/badge/Java-17%2B-orange.svg)](https://www.java.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![MusicBrainz](https://img.shields.io/badge/Data-MusicBrainz-purple.svg)](https://musicbrainz.org/)
[![LrcLib](https://img.shields.io/badge/Lyrics-LrcLib-green.svg)](https://lrclib.net/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[English](README.md) | [简体中文](README_ZH.md)

</div>

**Music Auto Tagger** is an automated music library organizer based on **audio fingerprinting** and **duration sequence fingerprinting**. Designed for NAS and server environments, it monitors your download folder, identifies music files, fetches comprehensive metadata (including lyrics), and organizes them into a clean structure.

> **Core Value**: Say goodbye to messy music folders. Automatically tag, cover, and organize your music library to perfection.

## 📊 Web Monitoring Dashboard

![Web Dashboard](src/main/resources/static/web.png)

The built-in real-time monitoring dashboard provides:
- 📊 Real-time statistics and processing progress
- 📝 Recently processed files with detailed metadata
- 📋 Live system logs with auto-scroll
- ⚙️ System configuration and status overview

## ✨ Key Features

- 🎧 **Audio Fingerprinting**: Uses **Chromaprint (AcoustID)** to accurately identify files even with garbled filenames (e.g., `track01.mp3`).
- 📝 **Authoritative Metadata**: Sources data from **MusicBrainz** to automatically complete Title, Artist, Album, Year, **Composer**, **Lyricist**, and more.
- 📜 **Synced Lyrics**: 🆕 Integrates with **LrcLib** to automatically download and embed **synced lyrics (.lrc)**, perfect for modern players.
- 🖼️ **HD Cover Art**: Automatically downloads and embeds high-quality album art from the Cover Art Archive.
- 📁 **Automated Organization**: Automatically renames and sorts files into a `Artist/Album/Title` structure.
- 🤖 **Unattended Operation**: Works seamlessly with qBittorrent/Transmission to process downloads automatically upon completion.
- ⚡ **Smart Scan Optimization**: 🆕 **Two-tier identification + folder-level caching**
    - **Tier 1: Quick Scan** - Tag & duration sequence matching, passes at 90% accuracy
    - **Tier 2: Fingerprint** - Only triggered when quick scan fails, ensures high recognition rate
    - **Folder-level Caching** - Subsequent files in the same album use cached results, skip all scans
    - **Performance Boost**: Processing a 16-track album requires only 1 full scan + 15 cache lookups
- 💾 **Dual Persistence Modes**:
    - **File Mode (Default)**: Uses a CSV file to track processed files. Zero config, ready out of the box for personal use.
    - **MySQL Mode**: Supports external database connection for massive libraries and high concurrency.
- 🐳 **Docker Ready**: Provides lightweight Docker images compatible with Synology, QNAP, Unraid, and other NAS systems.
- 🔄 **Smart Retry**: Automatically handles network failures with retry logic and isolates failed files for later inspection.
- 📊 **Web Monitoring Dashboard**: 🆕 Built-in real-time monitoring dashboard to visualize processing progress, system status, and runtime logs.
- 🌐 **Multi-language Support**: 🆕 Supports both Chinese and English interfaces, easily switchable via configuration file, providing localized experience for global users.

## ⚠️ Best Practice: How to Get the Most Accurate Results

Since music releases are extremely complex (Singles, EPs, Albums, Compilations, Deluxe Editions, etc.), to ensure the tool accurately categorizes your music into the correct albums, it is **highly recommended** to follow this practice:

> **Please place audio files from the same album (or single) into a separate folder** before processing them with this tool.

❌ **Not Recommended**: Dumping hundreds of songs from different artists and albums into a single directory.
✅ **Recommended**:
  - `/Downloads/Jay_Chou_Fantasy/` (Contains songs from the Fantasy album)
  - `/Downloads/Adele_21/` (Contains songs from the 21 album)

**Reason**: When files are isolated in separate folders, the program can better determine that they belong to the same album based on context, avoiding misidentification of album tracks as "Best Of" compilations or "Single" versions.
## 🚀 Quick Start (Docker Compose)

The easiest way to run the application. No Java installation required.

1.  **Download Config Template**
    Download `config.properties.example` from the repository and rename it to `config.properties`.

2.  **Get API Key (Free)**
    Visit [AcoustID](https://acoustid.org/new-application) to apply for an API Key and add it to your config:
    ```properties
    acoustid.apiKey=YOUR_API_KEY_HERE
    ```

3.  **Create `docker-compose.yml`**
    ```yaml
    version: '3.8'
    services:
      music-tagger:
        image: ghcr.io/lux032/musicautotagger:latest
        container_