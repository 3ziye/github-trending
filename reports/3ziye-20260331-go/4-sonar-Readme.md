<div align="center">

```
███████╗ ██████╗ ███╗   ██╗ █████╗ ██████╗
██╔════╝██╔═══██╗████╗  ██║██╔══██╗██╔══██╗
███████╗██║   ██║██╔██╗ ██║███████║██████╔╝
╚════██║██║   ██║██║╚██╗██║██╔══██║██╔══██╗
███████║╚██████╔╝██║ ╚████║██║  ██║██║  ██║
╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝
```

Know what's running on your machine.

</div>

I got tired of running `lsof -iTCP -sTCP:LISTEN | grep ...` every time a port was already taken, then spending another minute figuring out if it was a Docker container or some orphaned dev server from another worktree. So I built sonar.

It shows everything listening on localhost, with Docker container names, Compose projects, resource usage, and clickable URLs. You can kill processes, tail logs, shell into containers, and more — all by port number.

```
$ sonar list
PORT   PROCESS                      CONTAINER                    IMAGE             CPORT   URL
1780   proxy (traefik:3.0)          my-app-proxy-1               traefik:3.0       80      http://localhost:1780
3000   next-server (v16.1.6)                                                               http://localhost:3000
5432   db (postgres:17)             my-app-db-1                  postgres:17       5432    http://localhost:5432
6873   frontend (frontend:latest)   my-app-frontend-1            frontend:latest   5173    http://localhost:6873
9700   backend (backend:latest)     my-app-backend-1             backend:latest    8000    http://localhost:9700

5 ports (4 docker, 1 user)
```

## Install

```sh
curl -sfL https://raw.githubusercontent.com/raskrebs/sonar/main/scripts/install.sh | bash
```

Downloads the latest binary to `~/.local/bin` and adds it to your PATH if needed. Restart your terminal or `source ~/.zshrc`.

On Windows (PowerShell):

```powershell
irm https://raw.githubusercontent.com/raskrebs/sonar/main/scripts/install.ps1 | iex
```

Custom install location:

```sh
curl -sfL https://raw.githubusercontent.com/raskrebs/sonar/main/scripts/install.sh | SONAR_INSTALL_DIR=/usr/local/bin bash
```

Install a specific version:

```sh
curl -sfL https://raw.githubusercontent.com/raskrebs/sonar/main/scripts/install.sh | SONAR_VERSION=vX.Y.Z bash
```

```powershell
$env:SONAR_VERSION="vX.Y.Z"; irm https://raw.githubusercontent.com/raskrebs/sonar/main/scripts/install.ps1 | iex
```

### Using Go

```sh
go install github.com/raskrebs/sonar@latest
```

> **Note:** `go install` only installs the CLI. The menu bar tray app (`sonar tray`) is a native Swift binary and must be built separately — see [Tray app](#tray-app) below.

Shell completions (tab-complete port numbers):

```sh
sonar completion zsh > "${fpath[1]}/_sonar"   # zsh
sonar completion bash > /etc/bash_completion.d/sonar  # bash
sonar completion fish | source                 # fish
```

## Usage

### List ports

```sh
sonar list                     # show all ports
sonar list --stats             # include CPU, memory, state, uptime
sonar list --filter docker     # only Docker ports
sonar list --sort name         # sort by process name
sonar list --json              # JSON output
sonar list -a                  # include desktop apps
sonar list -c port,cpu,mem,uptime,state  # custom columns
sonar list --health            # run HTTP health checks
sonar list --host user@server  # scan a remote machine via SSH
```

By default, sonar hides desktop apps and system services that listen on TCP ports but aren't relevant to development — things like Figma, Discord, Spotify, ControlCenter, AirPlay, and other macOS `.app` bundles and `/System/Library/` daemons. Use `-a` to include them.

Available columns: `port`, `process`, `pid`, `type`, `url`, `cpu`, `mem`, `threads`, `uptime`, `state`, `connections`, `health`, `latency`, `container`, `image`, `containerport`, `compose`, `project`, `user`, `bind`, `ip`

### Inspect a port

```sh
sonar info 3000
```

Shows everything about a port: full command, user, bind address, CPU/memory/threads, uptime, health check result, and Docker details if applicable.

### Kill processes

```sh
sonar kill 3000                            # SIGTERM
sonar kill 3000 -f                         # SIGKILL
sonar kill-all --filter docker             # stop all Docker containers
sonar kill-all --project my-app            # stop a Compose project
sonar kill-all --filter user -y            # skip confirmation
```

Docker containers are stopped with `docker stop` instead of sending signals.

### View logs

```sh
sonar logs 3000
```

For Docker containers, runs `docker logs -f`. For native processes, discovers log files via `lsof` and tails them. Falls back to macOS `log stream` or Linux `/proc/<pid>/fd`.

### Attach to a service

```sh
sonar attach 3000                          # shell into Docker container, or TCP connect
sonar attach 3000 --shell bash             # specific shell
```

### Watch for changes

```sh
sonar watch                                # poll every 2s, show diffs
sonar watch --stats                        # live resource stats (lik