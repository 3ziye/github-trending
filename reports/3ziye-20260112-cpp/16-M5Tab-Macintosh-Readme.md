# BasiliskII ESP32 — Classic Macintosh Emulator for M5Stack Tab5

A full port of the **BasiliskII** Macintosh 68k emulator to the ESP32-P4 microcontroller, running on the M5Stack Tab5 hardware. This project brings classic Mac OS (System 7.x through Mac OS 8.1) to a portable embedded device with touchscreen input and USB peripheral support.


---

## Screenshots

<p align="center">
  <img src="screenshots/MacOS8.1_Booted.jpeg" width="45%" alt="Mac OS 8.1 Desktop"/>
  <img src="screenshots/MacOS8.1_About.jpeg" width="45%" alt="Mac OS 8.1 About This Macintosh"/>
</p>

<p align="center">
  <img src="screenshots/MacOS8.1_Booting.jpeg" width="45%" alt="Mac OS 8.1 Booting"/>
  <img src="screenshots/MacOS753_About.jpeg" width="45%" alt="System 7.5.3 About This Macintosh"/>
</p>

<p align="center">
  <a href="screenshots.md">
    <img src="https://img.shields.io/badge/🎬_View_Animations-Boot_Sequence_&_Flying_Toasters-blue?style=for-the-badge" alt="View Animations"/>
  </a>
</p>

---

## Overview

This project runs a **Motorola 68040** emulator that can boot real Macintosh ROMs and run genuine classic Mac OS software. The emulation includes:

- **CPU**: Motorola 68040 emulation with FPU (68881)
- **RAM**: Configurable from 4MB to 16MB (allocated from ESP32-P4's 32MB PSRAM)
- **Display**: 640×360 virtual display (2× scaled to 1280×720 physical display)
- **Storage**: Hard disk and CD-ROM images loaded from SD card
- **Input**: Capacitive touchscreen (as mouse) + USB keyboard/mouse support

## Hardware

### [M5Stack Tab5](https://shop.m5stack.com/products/m5stack-tab5-iot-development-kit-esp32-p4)

The Tab5 features a unique **dual-chip architecture** that makes it ideal for this project:

| Chip | Role | Key Features |
|------|------|--------------|
| **ESP32-P4** | Main Application Processor | 400MHz dual-core RISC-V, 32MB PSRAM, MIPI-DSI display |
| **ESP32-C6** | Wireless Co-processor | WiFi 6, Bluetooth LE 5.0 (not used by emulator) |

### Key Specifications

| Component | Details |
|-----------|---------|
| **Display** | 5" IPS TFT, 1280×720 (720p), MIPI-DSI interface |
| **Touch** | Capacitive multi-touch (ST7123 controller) |
| **Memory** | 32MB PSRAM for emulated Mac RAM + frame buffers |
| **Storage** | microSD card slot for ROM, disk images, and settings |
| **USB** | Type-A host port for keyboard/mouse, Type-C for programming |
| **Battery** | NP-F550 Li-ion (2000mAh) for portable operation |

See [boardConfig.md](boardConfig.md) for detailed pin mappings and hardware documentation.

---

## Architecture

### Dual-Core Design

The emulator leverages the ESP32-P4's dual-core RISC-V architecture for optimal performance:

```
┌─────────────────────────────────────────────────────────────────┐
│                        ESP32-P4 (400MHz)                        │
├────────────────────────────┬────────────────────────────────────┤
│         CORE 0             │              CORE 1                │
│    (Video & I/O Core)      │       (CPU Emulation Core)         │
├────────────────────────────┼────────────────────────────────────┤
│  • Video rendering task    │  • 68040 CPU interpreter           │
│  • 8-bit to RGB565 convert │  • Memory access emulation         │
│  • 2×2 pixel scaling       │  • Interrupt handling              │
│  • Touch input processing  │  • ROM patching                    │
│  • USB HID polling         │  • Disk I/O                        │
│  • ~15 FPS refresh rate    │  • 40,000 instruction quantum      │
└────────────────────────────┴────────────────────────────────────┘
```

### Memory Layout

```
┌──────────────────────────────────────────────────────────────┐
│                    32MB PSRAM Allocation                     │
├──────────────────────────────────────────────────────────────┤
│  Mac RAM (4-16MB)          │  Configurable via Boot GUI      │
├────────────────────────────┼─────────────────────────────────┤
│  Mac ROM (~1MB)            │  Q650.ROM or compatible         │
├────────────────────────────┼─────────────────────────────────┤
│  Mac Frame Buffer (230KB)  │  640×360 @ 8-bit indexed color  │
├────────────────────────────┼─────────────────────────────────┤
│  Display Buffer (1.8MB)    │  1280×720 @ RGB565              │
├────────────────────────────┼─────────────────────────────────┤
│  Free PSRAM                │  Varies based on RAM selection  │
└──────────────────────────────────────────────────────────────┘
```

### Video Pipeline

The video system uses an optimized pipeline for converting the Mac's 8-bit indexed framebuffer to the display:

1. **68040 CPU** writes to emulated Mac framebuffer (640×360, 8-bit indexed)
2. **Video Task** (Core 0) reads framebuffer at ~15 FPS
3. **Palette Lookup** converts 8-bit indices to RGB565
4. **2×2 Scaling** doubles pixels horizontally and vertically
5. **DMA Transfer** pushes 1280×720 RGB565 buffer to MIPI-DSI display

---

## Emulation Details

### BasiliskII Components

This port includes the following BasiliskII subsystems, adap