> [!NOTE]
> Grimmory is an independent community fork of Booklore.


Grimmory is a self-hosted application for managing your entire book collection in one place.
Organize, read, annotate, sync across devices, and share without relying on third-party services.

[![Release](https://img.shields.io/github/v/release/grimmory-tools/grimmory?color=818CF8&style=flat-square&logo=github)](https://github.com/grimmory-tools/grimmory/releases)
[![License](https://img.shields.io/github/license/grimmory-tools/grimmory?color=fab005&style=flat-square)](LICENSE)
[![Docker Pulls](https://img.shields.io/docker/pulls/grimmory/grimmory?color=2496ED&style=flat-square&logo=docker&logoColor=white)](https://hub.docker.com/r/grimmory/grimmory)
[![Discord](https://img.shields.io/badge/Discord-5865F2?style=flat-square&logo=discord&logoColor=white)](https://discord.gg/9YJ7HB4n8T)


[Website](https://grimmory.org/) | [Documentation](https://grimmory.org/docs/getting-started) | [Quick Start](#quick-start) | [Discord](https://discord.gg/9YJ7HB4n8T)

![Grimmory Demo](assets/demo.gif)

---

## Features

| Feature | Description |
| :--- | :--- |
| **Smart Shelves** | Custom and dynamic shelves with rule-based filtering, tagging, and full-text search |
| **Metadata Lookup** | Covers, descriptions, reviews, and ratings pulled from Google Books, Open Library, and Amazon, all editable |
| **Built-in Reader** | Read PDFs, EPUBs, and comics in the browser with annotations, highlights, and reading progress tracking |
| **Device Sync** | Connect a Kobo, use any OPDS-compatible app, or sync progress with KOReader |
| **Multi-User** | Separate shelves, progress, and preferences per user with local or OIDC authentication |
| **BookDrop** | Drop files into a watched folder and Grimmory detects, enriches, and queues them for import automatically |
| **One-Click Sharing** | Send any book to a Kindle, an email address, or another user directly from the interface |

### Supported Formats

| Category | Formats |
| :--- | :--- |
| eBooks | EPUB, MOBI, AZW, AZW3, FB2 |
| Documents | PDF |
| Comics | CBZ, CBR, CB7 |
| Audiobooks | M4B, M4A, MP3, OPUS |

---

## Quick Start

> [!TIP]
> For OIDC setup, advanced configuration, or upgrade guides, see the [full documentation](https://grimmory.org/docs/getting-started).

Requirements: [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/).

<details>
<summary><strong>Image Repositories</strong></summary>

| Registry | Image |
| --- | --- |
| Docker Hub | `grimmory/grimmory` |
| GitHub Container Registry | `ghcr.io/grimmory-tools/grimmory` |

</details>

### Step 1: Environment Configuration

Create a `.env` file:

```ini
# Application
APP_USER_ID=1000
APP_GROUP_ID=1000
TZ=Etc/UTC

# Database
DATABASE_URL=jdbc:mariadb://mariadb:3306/grimmory
DB_USER=grimmory
DB_PASSWORD=ChangeMe_Grimmory_2025!

# Optional: enable API docs + export OpenAPI JSON (defaults to false)
API_DOCS_ENABLED=false

# Storage: LOCAL (default) or NETWORK (disables file operations; see Network Storage section)
DISK_TYPE=LOCAL

# MariaDB
DB_USER_ID=1000
DB_GROUP_ID=1000
MYSQL_ROOT_PASSWORD=ChangeMe_MariaDBRoot_2025!
MYSQL_DATABASE=grimmory
```

### Step 2: Docker Compose

Stable images are published from semantic-release tags on `main` as `vX.Y.Z` plus `latest`. Nightly images are built from `develop` and tagged `nightly`.

> [!NOTE]
> Migrating from an existing Booklore container? You can keep your current service name, `container_name`, database name and user, ports, and mounted volumes the same. Replace only the `image:` line with `grimmory/grimmory:<tag>` or `ghcr.io/grimmory-tools/grimmory:<tag>`.

```yaml
services:
  booklore:
    image: grimmory/grimmory:v2.2.1
```

Create a `docker-compose.yml` or copy and adapt [`deploy/compose/docker-compose.yml`](deploy/compose/docker-compose.yml):

```yaml
services:
  grimmory:
    image: grimmory/grimmory:latest
    # Convenience tag:
    # image: grimmory/grimmory:<release-version>
    # Alternative: ghcr.io/grimmory-tools/grimmory:<release-version>
    # To build from source instead: comment out 'image' and uncomment below
    # build: .
    container_name: grimmory
    environment:
      - USER_ID=${APP_USER_ID}
      - GROUP_ID=${APP_GROUP_ID}
      - TZ=${TZ}
      - DATABASE_URL=${DATABASE_URL}
      - DATABASE_USERNAME=${DB_USER}
      - DATABASE_PASSWORD=${DB_PASSWORD}
      - API_DOCS_ENABLED=${API_DOCS_ENABLED}
    depends_on:
      mariadb:
        condition: service_healthy
    ports:
      - "6060:6060"
    volumes:
      - ./data:/app/data
      - ./books:/books
      - ./bookdrop:/bookdrop
    healthcheck:
      test: wget -q -O - http://localhost:6060/api/v1/healthcheck
      interval: 60s
      retries: 5
      start_period: 60s
      timeout: 10s
    restart: unless-stopped

  mariadb:
    image: lscr.io/linuxserver/mariadb:11.4.5
    container_name: mariadb
    environment:
      - PUID=${DB_USER_ID}
      - PGID=${DB_GROUP_ID}
     