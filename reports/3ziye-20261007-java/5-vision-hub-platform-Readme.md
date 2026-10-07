# Vision Hub Platform

> **English** | [中文](README_CN.md)

Vision Hub Platform is an open-source platform for visual algorithm management, video stream access, task orchestration, frame capture, AI-powered image analysis, and event records. The repository includes the backend services, media service, frontend console, and an all-in-one Docker Compose deployment so users can quickly start a complete visual intelligence platform.

The platform does not bundle an inference engine or depend on a specific model provider. You can configure an OpenAI-compatible vision model API, register cameras or video streams, bind algorithms to devices, and run scheduled analysis tasks from the console.

## Features

- **Algorithm Management** - Manage visual algorithms, prompts, output formats, model bindings, and test settings.
- **Model Configuration** - Configure OpenAI-compatible model APIs, including endpoint, API key, model id, context length, and maximum output tokens.
- **Prompt Templates** - Seed and reuse industry-specific prompt templates for common visual inspection scenarios.
- **Device Access** - Manage device metadata, stream URLs, status checks, and video previews.
- **Task Orchestration** - Bind tasks, algorithms, devices, and detection regions, then run scheduled frame analysis by sampling interval.
- **Media Service** - A standalone media service handles stream connections, frame capture, and snapshots.
- **Event Records** - Alarm results from algorithm execution are converted into searchable event records.
- **One-Command Deployment** - Docker Compose starts the frontend, Web API, media service, MySQL, Redis, Kafka, and MinIO.

## Open-Source Scope

This edition focuses on the core capabilities of a visual algorithm platform:

- visual algorithm management
- model and prompt configuration
- device access and stream preview
- task management with algorithm-device binding
- frame capture and algorithm execution logs
- alarm event records

Scene governance, organization management, and device organization trees are not included in this open-source edition. For commercial edition capabilities or enterprise adoption support, refer to [Enterprise Adoption Support](#enterprise-adoption-support).

## Architecture

```text
vision-hub-platform/
├── backend/   # Java / Spring Boot backend services
├── frontend/  # Vue 3 management console
└── docker/    # Docker Compose deployment
```

Core components:

| Component | Description |
| --- | --- |
| vision-hub-web-server | Web API, task management, algorithm invocation, and event records |
| vision-hub-media-server | Video stream connection, frame capture, and snapshots |
| frontend | Vue 3 management console |
| MySQL | Business data and initial schema |
| Redis | Runtime cache for tasks, devices, and algorithms |
| Kafka | Algorithm result messages |
| MinIO | Object storage for snapshots, uploads, and result images |

## Requirements

Docker Compose deployment only requires:

- Docker
- Docker Compose

Running from source requires:

- JDK 17+
- Maven 3.8+ or the included Maven Wrapper
- Node.js 18+
- MySQL 8+
- Redis
- Kafka
- MinIO
- An OpenAI-compatible vision model API

## Quick Start

### Option 1: Docker Compose (Recommended)

```bash
cd docker
cp .env.example .env
# Edit .env to change passwords, ports, and secrets before deployment.
docker compose up -d --build
```

Open:

```text
http://localhost
```

Default console account (change the password as soon as possible after first deployment):

```text
Username: unicom
Password: ZJ_Unicom
```

Default ports:

| Service | Port | Description |
| --- | --- | --- |
| Frontend console | 80 | nginx, proxies `/api` to the Web service |
| Web API | 18080 | Swagger UI: `/swagger-ui/index.html` |
| Media service | 18081 | Stream connection and frame capture |
| MySQL | 3306 | Password from `.env` |
| Redis | 6379 | Password from `.env` |
| Kafka | 9092 | Single-node KRaft mode |
| MinIO | 9000 / 9001 | API / Console |

Useful commands:

```bash
docker compose ps
docker compose logs -f vision-hub-web-server
docker compose logs -f vision-hub-media-server
docker compose down
docker compose down -v
```

`docker compose down` stops services while keeping data volumes. `docker compose down -v` removes MySQL, Redis, Kafka, and MinIO data volumes, so use it carefully when resetting an environment.

### Option 2: Build from Source

1. Create the database and import the schema:

   ```bash
   mysql -u root -p -e "CREATE DATABASE vision_hub DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
   mysql -u root -p vision_hub < backend/vision-hub-web/vision-hub-web-server/src/main/resources/sql/schema.sql
   ```

2. Configure backend environment variables:

   ```bash
   export DB_URL="jdbc:mysql://localhost:3306/vision_hub?useUnicode=true&characterEncoding=utf8&useSSL=false&serverTimezone=Asia/Shanghai&allowPublicKeyRetrieval=true&nullCatalogMeansCurrent=true"
   export DB_USERNAME="root"
   export DB_PASSWORD="ZJ_Unicom"
   expor