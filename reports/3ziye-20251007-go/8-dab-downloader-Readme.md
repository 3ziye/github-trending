# 🎵 DAB Music Downloader

[![Go Version](https://img.shields.io/badge/go-%3E%3D1.19-blue.svg)](https://golang.org/dl/)
[![License](https://img.shields.io/badge/license-Educational-green.svg)](#license)
[![Release](https://img.shields.io/github/v/release/PrathxmOp/dab-downloader)](https://github.com/PrathxmOp/dab-downloader/releases/latest)
[![Discord Support](https://img.shields.io/badge/Support-Discord-blue.svg?logo=discord&logoColor=white)](https://discord.gg/q9RnuVza2)
![Development Status](https://img.shields.io/badge/status-unstable%20development-orange.svg)

> A powerful, modular music downloader that delivers high-quality FLAC files with comprehensive metadata support through the DAB API.

## Table of Contents
- [⚠️ IMPORTANT: Development Status](#️-important-development-status)
- [✨ Key Features](#-key-features)
- [📸 Screenshots](#-screenshots)
- [🚀 Quick Start](#-quick-start)
  - [Option 1: Using `auto-dl.sh` Script (Recommended)](#option-1-using-auto-dlsh-script-recommended)
  - [Option 2: Pre-built Binary](#option-2-pre-built-binary)
  - [Option 3: Build from Source](#option-3-build-from-source)
  - [Option 4: Docker (Containerized)](#option-4-docker-containerized)
- [🔄 CRITICAL: Staying Updated](#-critical-staying-updated)
  - [🚨 Daily Update Routine (Recommended)](#-daily-update-routine-recommended)
  - [Versioning Format](#versioning-format)
  - [Option 1: Pre-built Binary Updates](#option-1-pre-built-binary-updates)
  - [Option 2: Source Code Updates](#option-2-source-code-updates)
  - [Option 3: Docker Updates](#option-3-docker-updates)
  - [🔔 Get Update Notifications](#-get-update-notifications)
- [📋 Usage Guide](#-usage-guide)
  - [🔍 Search and Discover](#-search-and-discover)
  - [📀 Download Content](#-download-content)
  - [🎧 Spotify Integration](#-spotify-integration)
  - [🎵 Navidrome Integration](#-navidrome-integration)
- [⚙️ Configuration](#️-configuration)
  - [First-Time Setup](#first-time-setup)
  - [Configuration File](#configuration-file)
- [⚙️ Command-Line Flags](#️-command-line-flags)
  - [Global Flags (Persistent Flags)](#global-flags-persistent-flags)
  - [Command-Specific Flags](#command-specific-flags)
    - [`album` command](#album-command)
    - [`artist` command](#artist-command)
    - [`search` command](#search-command)
    - [`spotify` command](#spotify-command)
    - [`navidrome` command](#navidrome-command)
- [📁 File Organization](#-file-organization)
- [🔧 Advanced Features](#-advanced-features)
  - [Debug Tools](#debug-tools)
  - [Quality & Metadata](#quality--metadata)
- [🐛 Troubleshooting](#-troubleshooting)
- [💬 Support & Community](#-support--community)
- [🏗️ Project Architecture](#️-project-architecture)
- [🤝 Contributing](#-contributing)
  - [Development Areas Needing Help](#development-areas-needing-help)
- [⚖️ Legal Notice](#️-legal-notice)
- [📄 License](#-license)
- [🌟 Support the Project](#-support-the-project)
- [Changelog](#changelog)
- [Update Guide](#update-guide)

## ⚠️ **IMPORTANT: Development Status**

🚧 **This project is currently in active, unstable development.** 🚧

- **Frequent Breaking Changes**: Features may work one day and break the next
- **Regular Updates Required**: You'll need to update frequently to get the latest fixes
- **Expect Issues**: Something always seems to break when i fix something else
- **Pre-Stable Release**: We're working toward a stable v1.0, but we're not there yet

**📢 We strongly recommend:**
- [Discord Support Group](https://discord.gg/q9RnuVza2) for real-time updates
- ✅ Checking for updates daily if you're actively using the tool
- ✅ Being prepared to troubleshoot and report issues
- ✅ Having patience as we work through the bugs

💬 **Need Help?** Join our [Discord Support Group](https://discord.gg/q9RnuVza2) for instant community support and the latest stability updates!



## ✨ Key Features

🔍 **Smart Search** - Find artists, albums, and tracks with intelligent filtering  
📦 **Complete Discographies** - Download entire artist catalogs with automatic categorization  
🏷️ **Rich Metadata** - Full tag support including genre, composer, producer, ISRC, and copyright  
🎨 **High-Quality Artwork** - Embedded album covers in original resolution  
- **Concurrent Downloads** - Fast parallel processing with real-time progress tracking  
- **Intelligent Retry Logic** - Robust error handling for reliable downloads  
- **Spotify Integration** - Import and download entire Spotify playlists and albums  
- **Format Conversion** - Convert downloaded FLAC files to MP3, OGG, Opus with configurable bitrates (requires FFmpeg)  
- **Navidrome Support** - Seamless integration with your music server  
- **Customizable Naming** - Define your own file and folder structure with configurable naming masks

## 📸 Screenshots

![img1](./screenshots/ScreenShot1.png)
![img1](./screenshots/ScreenShot2.png)

## 🚀 Quick Start

### Option 1: Using `auto-dl.sh` Script (Recommended)

This script simplifies the process of downloading and keeping `dab-down