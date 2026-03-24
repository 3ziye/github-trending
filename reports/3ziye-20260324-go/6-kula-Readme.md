<div align="center">

<img width="128" height="128" alt="image" src="https://github.com/user-attachments/assets/77d5850a-c3a4-47fe-b33e-dcaeeb3c8e4d" />

# K U L A

**Lightweight, self-contained Linux® server monitoring tool.**

![Go](https://img.shields.io/badge/made%20for-linux-yellow?logo=linux&logoColor=ffffff)
![Go](https://img.shields.io/badge/go%20go-power%20rangers-blue?logo=go&logoColor=ffffff)
![JS](https://img.shields.io/badge/some%20-js-orange?logo=javascript&logoColor=ffffff)
![JS](https://img.shields.io/badge/and%20a%20pinch%20of-bash-green?logo=linux&logoColor=ffffff)
[![License: GPL v3](https://img.shields.io/badge/License-AGPLv3-red.svg)](https://www.gnu.org/licenses/agpl-3.0)

[🌏 Website](https://kula.ovh) | [👀 Demo](https://demo.kula.ovh/) | [🐋 Docker Hub](https://hub.docker.com/r/c0m4r/kula)

Zero dependencies. No external databases. Single binary. Just deploy and go.

<img width="1011" height="834" alt="image" src="https://github.com/user-attachments/assets/771b3e95-8713-44d2-8309-cd9e1f722a7e" />

</div>

---

## 📦 What It Does

Kula collects system metrics every second by reading directly from `/proc` and `/sys`, 
stores them in a built-in tiered ring-buffer storage engine, and serves them through a real-time Web UI dashboard and a terminal TUI.

| Metric | What's Collected |
|--------|-----------------|
| **CPU** | Total usage (user, system, iowait, irq, softirq, steal) + core count |
| **GPU** | Load, Power consumption, VRAM |
| **Load** | 1 / 5 / 15 min averages, running & total tasks |
| **Memory** | Total, free, available, used, buffers, cached, shmem |
| **Swap** | Total, free, used |
| **Network** | Per-interface throughput (Mbps), packets/s, errors, drops; TCP errors/s, resets/s, established connections; socket counts |
| **Disks** | Per-device I/O (read/write bytes/s, reads/s, writes/s IOPS); filesystem usage |
| **System** | Uptime, entropy, clock sync, hostname, logged-in user count |
| **Processes** | Running, sleeping, blocked, zombie counts |
| **Self** | Kula's own CPU%, RSS memory, open file descriptors |
| **Thermal** | CPU, GPU and Disk temperatures |

Note: Monitoring NVIDIA GPUs might require additional setup. Check [GPU monitoring](https://github.com/c0m4r/kula/wiki/GPU-monitoring).

---

## 🪩 How It Works

```
    ╭──────────────────────────────────────────────╮
    │                  Linux Kernel                │
    │      /proc/stat  /proc/meminfo  /sys/...     │
    ╰───────────────────────┬──────────────────────╯
                            │ Read every 1s
                            ▼
    ╭──────────────────────────────────────────────╮
    │                   Collectors                 │
    │        (CPU, Mem, Net, Disk, System)         │
    ╰───────────────────────┬──────────────────────╯
                            │ Live Data
         ╭──────────────────┼─────────────────────╮
         ▼                  ▼                     ▼
╭─────────────────╮  ╭────────────────╮  ╭─────────────────╮
│ Storage Engine  │  │   Web Server   │  │   TUI Terminal  │
╰───┬─────────┬───╯  ╰──────┬─────────╯  ╰─────────────────╯
    │         │             │
    │         ╰──(History)──┤              ╭───────────────╮
    │                       ╰──(HTTP/WS)─► |   Dashboard   |
    ▼                                      ╰───────────────╯
╭──────────┬──────────┬──────────╮
│  Tier 1  │  Tier 2  │  Tier 3  │
│    1s    │    1m    │    5m    │
│  250 MB  │  150 MB  │  50 MB   │
╰──────────┴──────────┴──────────╯
 Ring-buffer binary files
 with circular overwrites
```

### Storage Engine

Kula is powered by a custom-built, high-performance **ring-buffer** storage system that writes metrics directly into fixed-size binary files. Because the files have a strict maximum capacity, new data seamlessly wraps around to overwrite the oldest entries. On startup, Kula restores the latest-sample cache and reconstructs any pending aggregation buffers so it can resume serving recent data and continue tier rollups after a restart.

To maximize efficiency, Kula employs a multi-tiered architecture that intelligently downsamples older data:

- **Tier 1** — Raw 1-second samples (default 250 MB)
- **Tier 2** — 1-minute metrics aggregation (Avg/Min/Max) (default 150 MB)
- **Tier 3** — 5-minute metrics aggregation (Avg/Min/Max) (default 50 MB)

### HTTP server

The HTTP server on backend exposes a REST API and a WebSocket endpoint for live streaming. 
Authentication is optional. When enabled, Kula uses Argon2id password hashing, secure session cookies, token-only session validation with sliding expiration, and hashed-at-rest session persistence. Authenticated API access can also use a bearer session token via the `Authorization` header.

### Dashboard

The frontend is a single-page application embedded in the binary. Built on Chart.js with custom SVG gauges, 
it connects via WebSocket for live updates and falls back to history API for longer time ranges. Features include:

- Interactive zoom with 