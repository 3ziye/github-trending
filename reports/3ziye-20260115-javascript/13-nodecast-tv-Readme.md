<p align="center">
  <img src="public/img/logo-banner.png" alt="nodecast-tv" height="60" />
</p>

# What is nodecast-tv?

nodecast-tv is a modern, web-based IPTV player featuring Live TV, EPG, Movies (VOD), and Series support. Built with performance and user experience in mind.

## Features

- **📺 Live TV**: Fast channel zapping, category grouping, and search.
- **📅 TV Guide (EPG)**: Interactive grid guide with 24h timeline, search, and dynamic resizing.
- **🎬 VOD Support**: Dedicated sections for Movies and TV Series with rich metadata, posters, and seasonal episode lists.
- **❤️ Favorites System**: Unified favorites for channels, movies, and series with instant synchronization.
- **🔐 Authentication**: User login system with admin and viewer roles ([details](https://github.com/technomancer702/nodecast-tv/pull/23)).
- **⚡ High Performance**: Optimized for large playlists (7000+ channels) using virtual scrolling and batch rendering.
- **⚙️ Management**: 
  - Support for Xtream Codes and M3U playlists.
  - Manage hidden content categories.
  - Playback preferences (volume memory, auto-play).
- **🔊 Audio Transcoding**: Optional FFmpeg-based audio transcoding for Dolby/AC3/EAC3 compatibility.
- **📦 Stream Remux**: Lightweight FFmpeg remux for raw MPEG-TS streams from IPTV middleware.
- **🐳 Docker Ready**: Easy deployment containerization.

## Screenshots

<div align="center">
  <img src="public/img/screenshots/screenshot-2.png" width="45%" alt="Screenshot 2" />
  <img src="public/img/screenshots/screenshot-1.png" width="45%" alt="Screenshot 1" />
  <img src="public/img/screenshots/screenshot-3.png" width="45%" alt="Screenshot 3" />
  <img src="public/img/screenshots/screenshot-4.png" width="45%" alt="Screenshot 4" />
</div>

## Getting Started

### Prerequisites

- Node.js (v14 or higher)
- npm

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/yourusername/nodecast-tv.git
    cd nodecast-tv
    ```

2.  Install dependencies:
    ```bash
    npm install
    ```

3.  Start the development server:
    ```bash
    npm run dev
    ```

4.  Open your browser at `http://localhost:3000`.

### Docker Deployment

You can run nodecast-tv easily using Docker.

1.  Create a `docker-compose.yml` file (or copy the one from this repo):

    ```yaml
    services:
      nodecast-tv:
        build: https://github.com/technomancer702/nodecast-tv.git#main
        container_name: nodecast-tv
        ports:
          - "3000:3000" # Host:Container
        volumes:
          - ./data:/app/data
        restart: unless-stopped
        environment:
          - NODE_ENV=production
          - PORT=3000 # Optional: Internal container port
    ```

2.  Run the container:
    ```bash
    docker-compose up -d
    ```

The application will be available at `http://localhost:3000`.

### Usage

1.  Go to **Settings** -> **Content Sources**.
2.  Add your IPTV provider details (Xtream Codes or M3U URL).
3.  Click "Refresh Sources".
4.  Navigate to **Live TV**, **Movies**, or **Series** to browse your content.


## Browser Codec Support

nodecast-tv is a web-based application, which means **video decoding is handled by your browser**, not by the server. The server simply proxies the stream data - it does not transcode or re-encode video.

This means codec support depends entirely on what your browser can decode natively:

| Codec | Chrome | Firefox | Safari | Edge |
|-------|--------|---------|--------|------|
| **H.264 (AVC)** | ✅ | ✅ | ✅ | ✅ |
| **H.265 (HEVC)** | ❌¹ | ❌ | ✅ | ⚠️² |
| **VP9** | ✅ | ✅ | ⚠️³ | ✅ |
| **AV1** | ✅ | ✅ | ❌ | ✅ |
| **AAC Audio** | ✅ | ✅ | ✅ | ✅ |
| **AC3/EAC3 (Dolby)** | ❌ | ❌ | ✅ | ❌ |
| **MP3 Audio** | ✅ | ✅ | ✅ | ✅ |

**Notes:**
1. Chrome may support HEVC on macOS with hardware decoder
2. Edge requires the paid "HEVC Video Extensions" from Microsoft Store ($0.99)
3. Safari VP9 support varies by device/version

**If a stream doesn't play:**
- The stream codec may not be supported by your browser
- Try a different browser (Safari for HEVC/Dolby, Chrome/Edge for VP9/AV1)
- Check if your IPTV provider offers alternative stream formats
- For Dolby audio issues, enable **"Force Audio Transcode"** in Settings → Streaming

### Audio Transcoding

For streams with Dolby Digital (AC3/EAC3) audio that browsers can't decode natively:

1. Install FFmpeg support: `npm install ffmpeg-static` (included as optional dependency)
2. Enable **"Force Audio Transcode"** in Settings → Streaming
3. Audio will be transcoded to AAC while video passes through unchanged

**Note:** For ad-stitched live streams (like Pluto TV), transcoding may struggle to keep up. These streams typically use AAC audio already, so the built-in HLS discontinuity handling manages audio transitions without transcoding.

## Supported Stream Types

nodecast-tv is optimized for **HLS (HTTP Live Streaming)**.

-   **✅ HLS (`.m3u8`)**: Fully supported and recommended. Best for adaptive bitrate and network resilience.
-   **✅ MPEG-TS (`