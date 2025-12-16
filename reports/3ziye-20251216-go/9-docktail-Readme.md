# 🍸 DockTail

**Unleash your Containers as Tailscale Services**

<p align="center">
  <img src="assets/header.jpeg" alt="DockTail Header" width="100%">
</p>

Automatically expose Docker containers as Tailscale Services using label-based configuration - zero-config service mesh for your dockerized services.

```
 ┌────────────────────────────────────────────────────────┐
 │                     Docker Host                        │
 │                                                        │
 │  ┌──────────────────┐         ┌──────────────────┐     │
 │  │     DockTail     │────────▶│ Tailscale Daemon │     │
 │  │   (Container)    │  CLI    │   (Host Process) │     │
 │  └────────┬─────────┘         └────────┬─────────┘     │
 │           │                            │               │
 │           │ Docker Socket              │ Proxies to    │
 │           │ Monitoring                 │ localhost     │
 │           ▼                            ▼               │
 │  ┌──────────────────┐         ┌──────────────────┐     │
 │  │   App Container  │◀────────│  localhost:9080  │     │
 │  │   Port 80        │  Mapped │  localhost:9081  │     │
 │  │  ports: 9080:80  │◀────────│                  │     │
 │  └──────────────────┘         └──────────────────┘     │
 │                                                        │
 └────────────────────────────────────────────────────────┘
                          │
                          │ Tailscale Network
                          ▼
               ┌─────────────────────┐
               │  Tailnet Clients    │
               │  Access services:   │
               │  web.tailnet.ts.net │
               └─────────────────────┘
```

## Features

- [x] Automatically discover and advertise Docker containers as Tailscale Services
- [x] HTTP, HTTPS and TCP protocols for running services
- [x] Support Tailscale HTTPS (auto TLS certificate)
- [x] Automatically drain Tailscale service configurations on container stop
- [x] Runs entirely in a **stateless Docker container**
- [x] Tailscale Funnel support (public internet access)
- [ ] More? => Create an Issue :)

> [!WARNING]
> This project is still being developed and it is **not** yet recommended to use for mission critical services.

## Quick Start

### Admin Console Setup

Before installing the DockTail, configure your Tailscale admin console at https://login.tailscale.com/admin/services:

1. **Create service definitions** (Services → Add service):
   - Create a service for each application you want to expose
   - Example: Service name `web`, `api`, `db`, etc.
   - Note: DockTail will automatically configure and advertise these services

2. **(Optional) Configure service tags**:
   - Navigate to Access Controls
   - Add tags for service identification (e.g., `tag:homelab-service`)
   - Tag your Docker host (e.g., `tag:homelab`)

3. **(Recommended) Enable auto-approval**:
   - Navigate to Access Controls and edit your ACL policy
   - Add auto-approvers to skip manual approval for service advertisements:
   ```json
   {
     "autoApprovers": {
       "services": {
         "tag:homelab-service": ["tag:homelab"]
       }
     }
   }
   ```
   - This allows devices tagged `tag:homelab` to automatically advertise services tagged `tag:homelab-service`

See [Tailscale Services documentation](https://tailscale.com/kb/1552/tailscale-services) for detailed setup instructions.

### Installation

#### Option 1: Docker Compose

Create a `docker-compose.yaml`:

```yaml
version: '3.8'

services:
  docktail:
    image: ghcr.io/marvinvr/docktail:latest
    container_name: docktail
    restart: unless-stopped
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - /var/run/tailscale/tailscaled.sock:/var/run/tailscale/tailscaled.sock
```

#### Option 2: Docker Run

```bash
docker run -d \
  --name docktail \
  --restart unless-stopped \
  -v /var/run/docker.sock:/var/run/docker.sock:ro \
  -v /var/run/tailscale/tailscaled.sock:/var/run/tailscale/tailscaled.sock \
  ghcr.io/marvinvr/docktail:latest
```

### Usage

**🚨 CRITICAL:** Container ports MUST be published to host. Tailscale serve only supports `localhost` proxies.

**Basic example:**
```yaml
services:
  myapp:
    image: nginx:latest
    ports:
      - "8080:80"  # REQUIRED! HOST:CONTAINER format
    labels:
      - "docktail.service.enable=true"
      - "docktail.service.name=myapp"
      - "docktail.service.port=80"  # CONTAINER port (RIGHT side of "8080:80")
```

Access from any device in your tailnet:
```bash
curl http://myapp.your-tailnet.ts.net
```

**With HTTPS (auto TLS cert from Tailscale):**
```yaml
services:
  myapp:
    image: nginx:latest
    ports:
      - "8080:80"
    labels:
      - "docktail.service.enable=true"
      - "docktail.service.name=myapp"
      - "docktail.service.port=80"                   # Container port
      - "docktail.service.protocol=http"             # Container speaks HTTP
      - "docktail.service.service-port=443"          # Tailsca