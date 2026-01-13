# Sub2API

<div align="center">

[![Go](https://img.shields.io/badge/Go-1.25.5-00ADD8.svg)](https://golang.org/)
[![Vue](https://img.shields.io/badge/Vue-3.4+-4FC08D.svg)](https://vuejs.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-336791.svg)](https://www.postgresql.org/)
[![Redis](https://img.shields.io/badge/Redis-7+-DC382D.svg)](https://redis.io/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)](https://www.docker.com/)

**AI API Gateway Platform for Subscription Quota Distribution**

English | [中文](README_CN.md)

</div>

---

## Demo

Try Sub2API online: **https://v2.pincc.ai/**

Demo credentials (shared demo environment; **not** created automatically for self-hosted installs):

| Email | Password |
|-------|----------|
| admin@sub2api.com | admin123 |

## Overview

Sub2API is an AI API gateway platform designed to distribute and manage API quotas from AI product subscriptions (like Claude Code $200/month). Users can access upstream AI services through platform-generated API Keys, while the platform handles authentication, billing, load balancing, and request forwarding.

## Features

- **Multi-Account Management** - Support multiple upstream account types (OAuth, API Key)
- **API Key Distribution** - Generate and manage API Keys for users
- **Precise Billing** - Token-level usage tracking and cost calculation
- **Smart Scheduling** - Intelligent account selection with sticky sessions
- **Concurrency Control** - Per-user and per-account concurrency limits
- **Rate Limiting** - Configurable request and token rate limits
- **Admin Dashboard** - Web interface for monitoring and management

## Tech Stack

| Component | Technology |
|-----------|------------|
| Backend | Go 1.25.5, Gin, Ent |
| Frontend | Vue 3.4+, Vite 5+, TailwindCSS |
| Database | PostgreSQL 15+ |
| Cache/Queue | Redis 7+ |

---

## Documentation

- Dependency Security: `docs/dependency-security.md`

---

## Deployment

### Method 1: Script Installation (Recommended)

One-click installation script that downloads pre-built binaries from GitHub Releases.

#### Prerequisites

- Linux server (amd64 or arm64)
- PostgreSQL 15+ (installed and running)
- Redis 7+ (installed and running)
- Root privileges

#### Installation Steps

```bash
curl -sSL https://raw.githubusercontent.com/Wei-Shaw/sub2api/main/deploy/install.sh | sudo bash
```

The script will:
1. Detect your system architecture
2. Download the latest release
3. Install binary to `/opt/sub2api`
4. Create systemd service
5. Configure system user and permissions

#### Post-Installation

```bash
# 1. Start the service
sudo systemctl start sub2api

# 2. Enable auto-start on boot
sudo systemctl enable sub2api

# 3. Open Setup Wizard in browser
# http://YOUR_SERVER_IP:8080
```

The Setup Wizard will guide you through:
- Database configuration
- Redis configuration
- Admin account creation

#### Upgrade

You can upgrade directly from the **Admin Dashboard** by clicking the **Check for Updates** button in the top-left corner.

The web interface will:
- Check for new versions automatically
- Download and apply updates with one click
- Support rollback if needed

#### Useful Commands

```bash
# Check status
sudo systemctl status sub2api

# View logs
sudo journalctl -u sub2api -f

# Restart service
sudo systemctl restart sub2api

# Uninstall
curl -sSL https://raw.githubusercontent.com/Wei-Shaw/sub2api/main/deploy/install.sh | sudo bash -s -- uninstall -y
```

---

### Method 2: Docker Compose

Deploy with Docker Compose, including PostgreSQL and Redis containers.

#### Prerequisites

- Docker 20.10+
- Docker Compose v2+

#### Installation Steps

```bash
# 1. Clone the repository
git clone https://github.com/Wei-Shaw/sub2api.git
cd sub2api

# 2. Enter the deploy directory
cd deploy

# 3. Copy environment configuration
cp .env.example .env

# 4. Edit configuration (set your passwords)
nano .env
```

**Required configuration in `.env`:**

```bash
# PostgreSQL password (REQUIRED - change this!)
POSTGRES_PASSWORD=your_secure_password_here

# Optional: Admin account
ADMIN_EMAIL=admin@example.com
ADMIN_PASSWORD=your_admin_password

# Optional: Custom port
SERVER_PORT=8080

# Optional: Security configuration
# Enable URL allowlist validation (false to skip allowlist checks, only basic format validation)
SECURITY_URL_ALLOWLIST_ENABLED=false

# Allow insecure HTTP URLs when allowlist is disabled (default: false, requires https)
# ⚠️ WARNING: Enabling this allows HTTP (plaintext) URLs which can expose API keys
#             Only recommended for:
#             - Development/testing environments
#             - Internal networks with trusted endpoints
#             - When using local test servers (http://localhost)
# PRODUCTION: Keep this false or use HTTPS URLs only
SECURITY_URL_ALLOWLIST_ALLOW_INSECURE_HTTP=false

# Allow private IP addresses for upstream/pricing/CRS (for internal deployments)
SECURITY_URL_ALLOWLIST_ALLOW_PRIVATE_HOSTS=false
```

```bash
# 5. Start all ser