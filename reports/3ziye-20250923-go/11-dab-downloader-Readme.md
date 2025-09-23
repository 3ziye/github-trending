# 🎵 DAB Music Downloader

[![Go Version](https://img.shields.io/badge/go-%3E%3D1.19-blue.svg)](https://golang.org/dl/)
[![License](https://img.shields.io/badge/license-Educational-green.svg)](#license)
[![Release](https://img.shields.io/github/v/release/PrathxmOp/dab-downloader)](https://github.com/PrathxmOp/dab-downloader/releases/latest)
[![Signal Support](https://img.shields.io/badge/Support-Signal%20Group-blue.svg)](https://signal.group/#CjQKIARVUX48EP6g9DSPb2n1v6fAkxGQvdJJSWc4KLa4KFVyEhDCRiJon09heXcckPnkX6k2)
![Development Status](https://img.shields.io/badge/status-unstable%20development-orange.svg)

> A powerful, modular music downloader that delivers high-quality FLAC files with comprehensive metadata support through the DAB API.

## ⚠️ **IMPORTANT: Development Status**

🚧 **This project is currently in active, unstable development.** 🚧

- **Frequent Breaking Changes**: Features may work one day and break the next
- **Regular Updates Required**: You'll need to update frequently to get the latest fixes
- **Expect Issues**: Something always seems to break when i fix something else
- **Pre-Stable Release**: We're working toward a stable v1.0, but we're not there yet

**📢 We strongly recommend:**
- ✅ Joining our [Signal Support Group](https://signal.group/#CjQKIARVUX48EP6g9DSPb2n1v6fAkxGQvdJJSWc4KLa4KFVyEhDCRiJon09heXcckPnkX6k2) for real-time updates
- ✅ Checking for updates daily if you're actively using the tool
- ✅ Being prepared to troubleshoot and report issues
- ✅ Having patience as we work through the bugs

💬 **Need Help?** Join our [Signal Support Group](httpss://signal.group/#CjQKIARVUX48EP6g9DSPb2n1v6fAkxGQvdJJSWc4KLa4KFVyEhDCRiJon09heXcckPnkX6k2) for instant community support and the latest stability updates!

**👤 Solo Developer Project:** This tool is developed and maintained by a single developer. While I work hard to push frequent updates and fixes (often multiple commits per day), expect some instability as I can't test every scenario across all systems.

## ✨ Key Features

🔍 **Smart Search** - Find artists, albums, and tracks with intelligent filtering  
📦 **Complete Discographies** - Download entire artist catalogs with automatic categorization  
🏷️ **Rich Metadata** - Full tag support including genre, composer, producer, ISRC, and copyright  
🎨 **High-Quality Artwork** - Embedded album covers in original resolution  
⚡ **Concurrent Downloads** - Fast parallel processing with real-time progress tracking  
🔄 **Intelligent Retry Logic** - Robust error handling for reliable downloads  
🎧 **Spotify Integration** - Import and download entire Spotify playlists and albums  
🎵 **Format Conversion** - Convert downloaded FLAC files to MP3, OGG, Opus with configurable bitrates (requires FFmpeg)  
📊 **Navidrome Support** - Seamless integration with your music server  

## 📸 Screenshots

![img1](./screenshots/ScreenShot1.png)
![img1](./screenshots/ScreenShot2.png)

## 🚀 Quick Start

### Option 1: Using `auto-dl.sh` Script (Recommended)

This script simplifies the process of downloading and keeping `dab-downloader` updated. It fetches the latest version and places it in your current directory.

**Direct execution with curl:**
```bash
curl -fsSL https://raw.githubusercontent.com/PrathxmOp/Support-group-junk/main/Scripts/auto-dl.sh | bash
```

**Alternative methods:**

**Using wget (if curl is not available):**
```bash
wget -qO- https://raw.githubusercontent.com/PrathxmOp/Support-group-junk/main/Scripts/auto-dl.sh | bash
```

**Download first, then execute (safer approach):**
```bash
curl -fsSL -o auto-dl.sh https://raw.githubusercontent.com/PrathxmOp/Support-group-junk/main/Scripts/auto-dl.sh
chmod +x auto-dl.sh
./auto-dl.sh
```

### Option 2: Pre-built Binary

1. Download the latest release from our [GitHub Releases](https://github.com/PrathxmOp/dab-downloader/releases/latest)
2. Extract the archive.
3. Grant execute permissions to the binary:
   ```bash
   chmod +x ./dab-downloader-linux-arm64 # Or the appropriate binary for your system
   ```
4. Run the executable:
   ```bash
   ./dab-downloader-linux-arm64 # Or the appropriate binary for your system
   ```
5. Follow the interactive setup on first launch

### Option 3: Build from Source

**Prerequisites:**
- Go 1.19 or later ([Download here](https://golang.org/dl/))

```bash
# Clone the repository
git clone https://github.com/PrathxmOp/dab-downloader.git
cd dab-downloader

# Install dependencies and build
go mod tidy
go build -o dab-downloader
```

### Option 4: Docker (Containerized)

To run dab-downloader using a pre-built Docker image from Docker Hub:

1.  **Ensure Docker is installed:** Follow the official Docker installation guide for your system.
2.  **Configure with Docker Compose:**
    *   Make sure your `docker-compose.yml` file is configured to use the `prathxm/dab-downloader:latest` image (as updated by the latest changes).
    *   Create `config` and `music` directories if they don't exist:
        ```bash
        mkdir -p config music