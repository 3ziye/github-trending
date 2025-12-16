# Coolpack

A general-purpose build pack that automatically detects your application type, generates optimized Dockerfiles, and builds production-ready container images.

## Features

- **Auto-detection** - Automatically detects language, framework, and package manager
- **Optimized Dockerfiles** - Generates multi-stage builds with security best practices
- **BuildKit caching** - Framework-specific cache mounts for faster rebuilds
- **Non-root containers** - Runs as unprivileged user by default
- **Native dependency support** - Automatically installs required system packages
- **Static site support** - Serves static builds with Caddy (default) or nginx

## Supported Frameworks

More coming soon, we will support a bunch of them, not just Javascript based.

| Framework | Output Types |
|-----------|--------------|
| Next.js | Server (SSR) / Static |
| Nuxt | Server (SSR) / Static |
| Remix / React Router | Server (SSR) / Static |
| Astro | Server (SSR) / Static |
| SvelteKit | Server (SSR) / Static |
| Solid Start | Server (SSR) / Static |
| TanStack Start | Server (SSR) / Static |
| Vite | Static |
| Gatsby | Static |
| Angular | Server (SSR) / Static |
| Express | Server |
| Fastify | Server |
| NestJS | Server |
| AdonisJS | Server |

## Installation

### Quick Install

```bash
curl -fsSL https://raw.githubusercontent.com/coollabsio/coolpack/main/install.sh | bash
```

### From Source

```bash
git clone https://github.com/coollabsio/coolpack.git
cd coolpack
./build.sh
```

The binary will be created at `./coolpack`.

### Requirements

- Docker with BuildKit support (for building images)
- Go 1.21+ (only for building from source)

## Quick Start

```bash
# Navigate to your project
cd my-app

# See what Coolpack detects
coolpack plan

# Generate Dockerfile
coolpack prepare

# Build container image
coolpack build

# Run the container (development only)
coolpack run
```

## Commands

### `coolpack plan [path]`

Analyze and display the build plan without generating any files.

```bash
coolpack plan                    # Current directory
coolpack plan ./my-app           # Specific path
coolpack plan --json             # Output as JSON
coolpack plan --out              # Save to coolpack.json
coolpack plan --out custom.json  # Save to custom file
coolpack plan --packages curl --packages wget  # Add custom packages
coolpack plan --build-env NEXT_PUBLIC_API_URL=https://api.example.com  # Add build env
```

**Flags:**
| Flag | Description |
|------|-------------|
| `--json` | Output as JSON |
| `-o, --out` | Write plan to file (default: `coolpack.json`) |
| `--packages` | Additional APT packages to install |
| `--build-env` | Build-time env vars (KEY=value or KEY) |

### `coolpack prepare [path]`

Generate a Dockerfile in the `.coolpack/` directory.

If a `coolpack.json` file exists in the project root, it will be used instead of running detection.

```bash
coolpack prepare
coolpack prepare --static-server nginx     # Use nginx instead of Caddy
coolpack prepare --build-cmd "npm run build:prod"
coolpack prepare --plan coolpack.json      # Use specific plan file
coolpack prepare --packages curl           # Add custom APT packages
```

**Flags:**
| Flag | Description |
|------|-------------|
| `-i, --install-cmd` | Override install command |
| `-b, --build-cmd` | Override build command |
| `-s, --start-cmd` | Override start command |
| `--static-server` | Static server: `caddy` (default), `nginx` |
| `--output-dir` | Override static output directory (e.g., `dist`, `build`) |
| `--spa` | Enable SPA mode (serves index.html for all routes) |
| `--no-spa` | Disable SPA mode (overrides auto-detection) |
| `--build-env` | Build-time env vars (KEY=value or KEY) |
| `--packages` | Additional APT packages to install |
| `--plan` | Use plan file instead of detection |

### `coolpack build [path]`

Generate Dockerfile and build the container image.

If a `coolpack.json` file exists in the project root, it will be used instead of running detection.

```bash
coolpack build
coolpack build -n my-app -t v1.0.0
coolpack build --build-env NEXT_PUBLIC_API_URL=https://api.example.com
coolpack build --no-cache
coolpack build --plan coolpack.json        # Use specific plan file
coolpack build --packages ffmpeg           # Add custom APT packages
```

**Flags:**
| Flag | Description |
|------|-------------|
| `-n, --name` | Image name (defaults to directory name) |
| `-t, --tag` | Image tag (default: `latest`) |
| `--no-cache` | Build without Docker cache |
| `-i, --install-cmd` | Override install command |
| `-b, --build-cmd` | Override build command |
| `-s, --start-cmd` | Override start command |
| `--static-server` | Static server: `caddy` (default), `nginx` |
| `--output-dir` | Override static output directory (e.g., `dist`, `build`) |
| `--spa` | Enable SPA mode (serves index.html for all routes) |
| `--no-spa` | Disable SPA mode (overrides auto-detection) |
| `--build-env` | Build-time env vars |
| `--packages` | Additional APT package