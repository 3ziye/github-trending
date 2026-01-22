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
- **🆔 OIDC SSO**: Support for Single Sign-On via OIDC providers (Authentik, Keycloak, etc.).
- **⚡ High Performance**: Optimized for large playlists (7000+ channels) using virtual scrolling and batch rendering.
- **⚙️ Management**: 
  - Support for Xtream Codes and M3U playlists.
  - Manage hidden content categories.
  - Playback preferences (volume memory, auto-play).
- **🎛️ Hardware Transcoding**: GPU-accelerated transcoding with NVIDIA NVENC, AMD AMF, Intel QuickSync, and VAAPI support.
- **🔊 Smart Audio**: Configurable 5.1→Stereo downmix presets (ITU, Night Mode, Cinematic) with automatic passthrough for compatible sources.
- **📦 Stream Processing**: Auto-detection of stream codecs with smart remux/transcode decisions.
- **🐳 Docker Ready**: Easy deployment containerization.

## Screenshots

<div align="center">
  <img src="public/img/screenshots/screenshot-dashboard.png" width="45%" alt="Dashboard" />
  <img src="public/img/screenshots/screenshot-1.png" width="45%" alt="Live TV" />
  <img src="public/img/screenshots/screenshot-2.png" width="45%" alt="TV Guide" />
  <img src="public/img/screenshots/screenshot-3.png" width="45%" alt="Movies" />
  <img src="public/img/screenshots/screenshot-4.png" width="45%" alt="Series" />
  <img src="public/img/screenshots/screenshot-settings.png" width="45%" alt="Settings" />
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


### Hardware Acceleration Setup

To enable hardware transcoding (NVENC, QSV, VAAPI), you must expose your host's GPU to the container.

**1. Intel (QSV) & AMD (VAAPI)**
Update your `docker-compose.yml` to map the DRI devices and add necessary groups (often required for permission):
```yaml
    devices:
      - /dev/dri:/dev/dri # Required for VAAPI/QuickSync/AMF (Linux)
    # group_add:       # Optional: Needed mainly if you run as non-root
    #   - "video"      # Run on host: getent group video
    #   - "render"     # Run on host: getent group render
```

**2. NVIDIA (NVENC)**
Ensure you have the [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html) installed on your host, then update your `docker-compose.yml`:
```yaml
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]
```

**Verify:**
After restarting the container, go to **Settings -> Transcoding**. The **Hardware Detection** status should list your GPU (e.g., "NVIDIA GPU Detected" or "VAAPI Available").

### SSO / OIDC Setup

Enable Single Sign-On (SSO) with your preferred OIDC provider (Authentik, Keycloak, etc.) by configuring these variables in your `.env` file or Docker environment:

```env
OIDC_ISSUER_URL=https://your-idp.com/application/o/nodecast/
OIDC_CLIENT_ID=your_client_id
OIDC_CLIENT_SECRET=your_client_secret
OIDC_CALLBACK_URL=http://localhost:3000/api/auth/oidc/callback # Adjust for your domain
```

**Note:** New users signing in via SSO are automatically assigned the **Viewer** role. You must manually promote them to Admin if desired.

### Usage

1.  Go to **Settings** -> **Content S