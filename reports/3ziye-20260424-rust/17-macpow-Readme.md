# 💻🔋 macpow – Real-time power tree TUI for Apple Silicon

[![CI](https://github.com/k06a/macpow/actions/workflows/ci.yml/badge.svg)](https://github.com/k06a/macpow/actions/workflows/ci.yml)
[![Crates.io](https://img.shields.io/crates/v/macpow)](https://crates.io/crates/macpow)
[![Homebrew](https://img.shields.io/badge/homebrew-v0.1.17-orange?logo=homebrew)](https://github.com/k06a/homebrew-tap)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Apple%20Silicon-black?logo=apple)](https://github.com/k06a/macpow)

Real-time power consumption monitor for Apple Silicon Macs (M1–M5+).

<p align="center">
  <img src="./screenshot.png" width="75%" alt="macpow screenshot">
</p>

**macpow** reads directly from macOS hardware interfaces — IOReport, SMC, IORegistry, CoreAudio, and Mach/kernel APIs — to show per-component power draw, temperatures, frequencies, CPU utilization, and per-process energy attribution. No sudo required.

### Legend

| Symbol | Meaning |
|--------|---------|
| `0.123 W` | Measured power (direct hardware reading) |
| `≈0.123 W` | Estimated power (model-based calculation) |
| `≤0.123 W` | Upper-bound power estimate |
| `▸` | Pinned resource (sparkline chart visible) |
| `▓▓▓░░░░░░░` | CPU core utilization bar (filled = busy) |
| `37°C` | Fresh temperature reading |
| `~37°C` | Stale temperature (sensor read failed, showing last known value) |
| `pending…` | Data source still initializing |
| `[dead]` | Process has exited (energy total preserved) |
| **Bold white** | Section headers and measured values |
| <span style="color:green">Green</span> | Low power (< 1W) or info-only rows |
| <span style="color:goldenrod">Yellow</span> | Moderate power (1–5W) |
| <span style="color:orange">Orange</span> | High power (5–10W) |
| <span style="color:red">Red</span> | Very high power (> 10W) |
| Gray | Dimmed/inactive items |

## Features

- **SoC breakdown** — CPU (E/P cores with per-core power, utilization bars, temperatures), GPU, ANE, DRAM, GPU SRAM, Media Engine, Camera (ISP), Fabric — all from IOReport Energy Model
- **CPU utilization** — per-core usage % with visual bars from Mach `host_processor_info`
- **Real frequencies** — CPU and GPU MHz from DVFS voltage-states tables, not percentages
- **Temperatures** — per-component and per-core from SMC sensors (CPU, GPU, ANE, DRAM, SSD, Battery); universal bank-based key mapping for all Apple Silicon generations (M1–M5+, including Ultra dual-die); stale value caching with `~` indicator when sensors temporarily read invalid
- **Memory** — used/total GB via `host_statistics64` Mach API
- **Display** — brightness estimate + IOReport SoC display controller; external display power via IOReport DISPEXT
- **Keyboard** — backlight brightness and estimated power via IORegistry PWM
- **Battery** — voltage, amperage, charge %, time remaining, temperature, drain/charge rate
- **SSD** — model, interconnect (Apple Fabric/PCIe), power estimation from IORegistry disk counters
- **Peripherals** — Thunderbolt/PCIe (IOReport measured), Ethernet (link speed, per-interface traffic), WiFi (signal/mode/channel, per-interface traffic), Bluetooth devices with battery levels, USB devices (speed/power/I/O counters)
- **Per-process energy** — dynamically-sized top processes by session energy (from `proc_pid_rusage`), with per-process disk I/O rates, network traffic (via nettop), RAM footprint, dead process detection
- **Fans** — RPM and cubic power model per fan
- **Collapsible tree** — fold/unfold with arrows, `+`/`-` for all
- **Sparkline charts** — pin any resource with Space, inline 1-line history column at wide terminals
- **Time-based SMA** — toggle 0s/5s/10s smoothing window
- **Latency control** — toggle UI refresh rate: 500ms / 2s / 5s
- **Mouse support** — click to select rows
- **JSON mode** — pipe structured data for scripts and dashboards
- **No sudo** — runs entirely with user-level permissions

## Install

### With cargo

```bash
cargo install macpow
```

### From source

```bash
git clone https://github.com/k06a/macpow.git
cd macpow
cargo build --release
./target/release/macpow
```

### Homebrew

```bash
brew tap k06a/tap
brew install macpow
```

### With pixi (conda-forge)

```bash
pixi global install macpow
# execute without installing
pixi exec macpow
```

## Usage

```
macpow                    # TUI mode (default)
macpow --json             # JSON output to stdout
macpow --interval 500     # Set sampling interval in ms (default: 250)
macpow --dump             # Dump IOReport channel names (diagnostics)
```

### Keybindings

| Key | Action |
|-----|--------|
| `q` / `Esc` | Quit |
| `Up` / `Down` / `j` / `k` | Move cursor |
| `Left` / `Right` / `h` | Collapse / expand tree node |
| `+` / `=` | Expand all nodes |
| `-` | Collapse all nodes |
| `Space` | Pin/unpin resource chart |
| `a` | Cycle SMA window: 0s / 5s / 10s |
| `l` | Cycle refresh interval: 250ms / 500ms / 1s / 2s |
| `r` | Reset