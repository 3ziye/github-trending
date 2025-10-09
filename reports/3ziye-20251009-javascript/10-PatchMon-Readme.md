# PatchMon - Linux Patch Monitoring made Simple

[![Website](https://img.shields.io/badge/Website-patchmon.net-blue?style=for-the-badge)](https://patchmon.net)
[![Discord](https://img.shields.io/badge/Discord-Join%20Server-blue?style=for-the-badge&logo=discord)](https://patchmon.net/discord)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge&logo=github)](https://github.com/9technologygroup/patchmon.net)
[![Roadmap](https://img.shields.io/badge/Roadmap-View%20Progress-green?style=for-the-badge&logo=github)](https://github.com/users/9technologygroup/projects/1)
[![Documentation](https://img.shields.io/badge/Documentation-docs.patchmon.net-blue?style=for-the-badge&logo=book)](https://docs.patchmon.net/)

---

## Please STAR this repo :D

## Purpose

PatchMon provides centralized patch management across diverse server environments. Agents communicate outbound-only to the PatchMon server, eliminating inbound ports on monitored hosts while delivering comprehensive visibility and safe automation.

![Dashboard Screenshot](https://raw.githubusercontent.com/PatchMon/PatchMon/main/dashboard.jpeg)

## Features

### Dashboard
- Customisable dashboard with per‑user card layout and ordering

### Users & Authentication
- Multi-user accounts (admin and standard users)
- Roles, Permissions & RBAC

### Hosts & Inventory
- Host inventory/groups with key attributes and OS details
- Host grouping (create and manage host groups)

### Packages & Updates
- Package inventory across hosts
- Outdated packages overview and counts
- Repositories per host tracking

### Agent & Data Collection
- Agent version management and script content stored in DB

### Settings & Configuration
- Server URL/protocol/host/port
- Signup toggle and default user role selection

### API & Integrations
- REST API under `/api/v1` with JWT auth
- **Proxmox LXC Auto-Enrollment** - Automatically discover and enroll LXC containers from Proxmox hosts ([Documentation](PROXMOX_AUTO_ENROLLMENT.md))

### Security
- Rate limiting for general, auth, and agent endpoints
- Outbound‑only agent model reduces attack surface

### Deployment & Operations
- Docker installation & One‑line self‑host installer (Ubuntu/Debian)
- systemd service for backend lifecycle
- nginx vhost for frontend + API proxy; optional Let’s Encrypt integration


## Getting Started

### PatchMon Cloud (coming soon)

Managed, zero-maintenance PatchMon hosting. Stay tuned.

### Self-hosted Installation

#### Docker (preferred)

For getting started with Docker, see the [Docker documentation](https://github.com/PatchMon/PatchMon/blob/main/docker/README.md)

#### Native Install (advanced/non-docker)

Run on a clean Ubuntu/Debian server with internet access:

#### Debian:
```bash
apt update -y
apt upgrade -y
apt install curl -y
```

#### Ubuntu:
```bash
apt-get update -y
apt-get upgrade -y
apt install curl -y
```

#### Script
```bash
curl -fsSL -o setup.sh https://raw.githubusercontent.com/PatchMon/PatchMon/refs/heads/main/setup.sh && chmod +x setup.sh && bash setup.sh
```

#### Minimum specs for building : #####
CPU : 2 vCPU
RAM : 2GB
Disk : 15GB

During setup you’ll be asked:
- Domain/IP: public DNS or local IP (default: `patchmon.internal`)
- SSL/HTTPS: `y` for public deployments with a public IP, `n` for internal networks
- Email: only if SSL is enabled (for Let’s Encrypt)
- Git Branch: default is `main` (press Enter)

The script will:
- Install prerequisites (Node.js, PostgreSQL, nginx)
- Clone the repo, install dependencies, build the frontend, run migrations
- Create a systemd service and nginx site vhost config
- Start the service and write a consolidated info file at:
  - `/opt/<your-domain>/deployment-info.txt`
  - Copies the full installer log to `/opt/<your-domain>/patchmon-install.log` from /var/log/patchmon-install.log

After installation:
- Visit `http(s)://<your-domain>` and complete first-time admin setup
- See all useful info in `deployment-info.txt`

## Forcing updates after host package changes
Should you perform a manual package update on your host and wish to see the results reflected in PatchMon quicker than the usual scheduled update, you can trigger the process manually by running:
```bash
/usr/local/bin/patchmon-agent.sh update
```

This will send the results immediately to PatchMon.

## Communication Model

- Outbound-only agents: servers initiate communication to PatchMon
- No inbound connections required on monitored servers
- Secure server-side API with JWT authentication and rate limiting

## Architecture

- Backend: Node.js/Express + Prisma + PostgreSQL
- Frontend: Vite + React
- Reverse proxy: nginx
- Database: PostgreSQL
- System service: systemd-managed backend

```mermaid
flowchart LR
    A[End Users / Browser<br>Admin UI / Frontend] -- HTTPS --> B[nginx<br>serve FE, proxy API]
    B -- HTTP --> C["Backend<br>(Node/Express)<br>/api, auth, Prisma"]
    C -- TCP --> D[PostgreSQL<br>Database]

    E["Agents on your servers (Outbound Only)"] --