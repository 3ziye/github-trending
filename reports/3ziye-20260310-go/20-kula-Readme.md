<div align="center">

<img width="128" height="128" alt="image" src="https://github.com/user-attachments/assets/77d5850a-c3a4-47fe-b33e-dcaeeb3c8e4d" />

# K U L A

**Lightweight, self-contained Linux® server monitoring tool.**

![Go](https://img.shields.io/badge/made%20for-linux-yellow?logo=linux&logoColor=ffffff)
![Go](https://img.shields.io/badge/go%20go-power%20rangers-blue?logo=go&logoColor=ffffff)
![JS](https://img.shields.io/badge/some%20-js-orange?logo=javascript&logoColor=ffffff)
![JS](https://img.shields.io/badge/and%20a%20pinch%20of-bash-green?logo=linux&logoColor=ffffff)
[![License: GPL v3](https://img.shields.io/badge/License-AGPLv3-red.svg)](https://www.gnu.org/licenses/agpl-3.0)

[👀 Demo](https://demo.kula.ovh/) | [🐋 Docker Hub](https://hub.docker.com/r/c0m4r/kula)

Zero dependencies. No external databases. Single binary. Just deploy and go.

<img width="1037" height="793" alt="image" src="https://github.com/user-attachments/assets/d50e5653-0e84-4374-9ded-4d8e9f8eedd2" />

</div>

---

## 📦 What It Does

Kula collects system metrics every second by reading directly from `/proc` and `/sys`, 
stores them in a built-in tiered ring-buffer storage engine, and serves them through a real-time Web UI dashboard and a terminal TUI.

| Metric | What's Collected |
|--------|-----------------|
| **CPU** | Total usage (user, system, iowait, irq, softirq, steal) + core count |
| **Load** | 1 / 5 / 15 min averages, running & total tasks |
| **Memory** | Total, free, available, used, buffers, cached, shmem |
| **Swap** | Total, free, used |
| **Network** | Per-interface throughput (Mbps), packets/s, errors, drops; TCP errors/s, resets/s, established connections; socket counts |
| **Disks** | Per-device I/O (read/write bytes/s, reads/s, writes/s IOPS); filesystem usage |
| **System** | Uptime, entropy, clock sync, hostname, logged-in user count |
| **Processes** | Running, sleeping, blocked, zombie counts |
| **Self** | Kula's own CPU%, RSS memory, open file descriptors |

---

## 🪩 How It Works

```
                    ┌──────────────────────────────────────────────┐
                    │              Linux Kernel                    │
                    │     /proc/stat  /proc/meminfo  /sys/...      │
                    └──────────────────┬───────────────────────────┘
                                       │ read every 1s
                                       ▼
                              ┌──────────────────┐
                              │    Collectors    │
                              │  (cpu, mem, net, │
                              │   disk, system)  │
                              └────────┬─────────┘
                                       │ Sample struct
                          ┌────────────┼────────────┐
                          ▼            ▼            ▼
                   ┌────────────┐  ┌────────┐  ┌──────────┐
                   │  Storage   │  │  Web   │  │   TUI    │
                   │  Engine    │  │ Server │  │ Terminal │
                   └─────┬──────┘  └───┬────┘  └──────────┘
                         │             │ 
              ┌──────────┼─────────┐   └───────────┐  HTTP + WebSocket
              ▼          ▼         ▼               ▼
          ┌─────────┬─────────┬─────────┐  ┌───────────────┐
          │ Tier 1  │ Tier 2  │ Tier 3  │  │   Dashboard   │
          │   1s    │   1m    │   5m    │  │   (Browser)   │
          │ 250 MB  │ 150 MB  │  50 MB  │  └───────────────┘
          └─────────┴─────────┴─────────┘
             Ring-buffer binary files
             with circular overwrites
```

### Storage Engine

Data is persisted in **pre-allocated ring-buffer files** per tier. Each tier file has a fixed maximum size — when it fills up, 
new data overwrites the oldest entries. This gives predictable, bounded disk usage with no cleanup needed.

- **Tier 1** — Raw 1-second samples (default 250 MB)
- **Tier 2** — 1-minute aggregates: averaged CPU & network, last-value gauges (default 150 MB)
- **Tier 3** — 5-minute aggregates, same logic (default 50 MB)

### HTTP server

The HTTP server on backend exposes a REST API and a WebSocket endpoint for live streaming. 
Authentication is optional - when enabled, it uses Argon2id hashing with salt and session cookies. 
It is worth adding that Kula truly respects your privacy. It works on closed networks and does not make any calls to external services.

### Dashboard

The frontend is a single-page application embedded in the binary. Built on Chart.js with custom SVG gauges, 
it connects via WebSocket for live updates and falls back to history API for longer time ranges. Features include:

- Interactive zoom with drag-select (auto-pauses live stream)
- Focus mode to show only selected graphs
- Grid / stacked list layout toggle
- Alert system for clock sync, entropy issues, overload
---

## 💾 Installation

Kula was built to have everything in one binary file. You can just upload it to your server 
and not worry about installing anythi