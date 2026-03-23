# BambuHelper

Dedicated Bambu Lab printer monitor built with ESP32-S3 Super Mini and a 1.54" 240x240 color TFT display (ST7789).

Connects to your printer via MQTT over TLS and displays a real-time dashboard with arc gauges, animations, and live stats.

### Supported Printers

| Connection Mode | Printers | How it connects |
|---|---|---|
| **LAN Direct** | P1P, P1S, X1, X1C, X1E, A1, A1 Mini | Local MQTT via printer IP + LAN access code |
| **Bambu Cloud (All printers)** | Any Bambu printer | Cloud MQTT via access token - no LAN mode needed |

> **Tip:** Use "Bambu Cloud (All printers)" if you don't want to enable LAN mode on your printer (e.g. to keep Bambu Handy working), if your ESP32 is on a different network than the printer, or if your printer only supports cloud mode (H2C, H2D, H2S, P2S).

### Cloud Mode Security Notice

When using Bambu Cloud, BambuHelper connects through Bambu Lab's cloud MQTT service. Here's what you need to know:

- **No credentials are stored** - BambuHelper never asks for your email or password. You extract an access token from your browser and paste it into the web interface.
- **Only the access token is stored** in the ESP32's flash memory. This token expires after ~3 months, at which point you simply paste a new one.
- **Read-only access** - BambuHelper only reads printer status. It never sends commands or modifies printer settings.
- **Same approach as other community projects** - this is the same authentication method used by the [Home Assistant Bambu Lab integration](https://github.com/greghesp/ha-bambulab) (15,000+ users), [OctoPrint-Bambu](https://github.com/jneilliii/OctoPrint-BambuPrinter), and other trusted third-party tools.

## Screenshots

| Dashboard | Web Interface - Settings | Web Interface - Gauge Colors |
|---|---|---|
| ![Dashboard](img/interface1.jpg) | ![Settings](img/screen1.png) | ![Gauge Colors](img/screen2.png) |

## Features

- **Live dashboard** - progress arc, temperature gauges, fan speed, layer count, time remaining
- **H2-style LED progress bar** - full-width glowing bar inspired by Bambu H2 series
- **Anti-aliased arc gauges** - smooth nozzle and bed temperature arcs with color zones
- **Animations** - loading spinner, progress pulse, completion celebration
- **Web config portal** - dark-themed settings page for WiFi, network, printer, display, and power settings
- **Network configuration** - DHCP or static IP, with optional IP display at startup
- **Display auto-off** - configurable timeout after print completion, auto-off when printer is off
- **NVS persistence** - all settings survive reboots
- **Auto AP mode** - creates WiFi hotspot on first boot or when WiFi is lost
- **Smart redraw** - only redraws changed UI elements for smooth performance
- **Customizable gauge colors** - per-gauge arc/label/value colors with preset themes
- **Multi-printer support** - monitor up to 2 printers simultaneously with auto-rotating display
- **Smart rotation** - automatically shows the printing printer; cycles between both when both are printing
- **Physical button** - optional push button or TTP223 touch sensor to cycle printers and wake display
- **Exponential backoff** - reconnect attempts to offline printers gradually slow down to conserve resources

## Hardware

| Component | Specification |
|---|---|
| MCU | ESP32-S3 Super Mini |
| Display | 1.54" TFT SPI ST7789 (240x240) |
| Connection | SPI |

Display: 1.54": https://a.aliexpress.com/_EG9y7wc

ESP32-S3 SuperMini: https://a.aliexpress.com/_Eyk9GdA

Optional: TTP223 touch button or standard push button for multi-printer switching (auto printer switching works without button anyway, change settings in web interface)

Optional: Passive buzzer for print finish/error notifications: https://aliexpress.com/item/1005008825917787.html

Optional case seen on picture: https://makerworld.com/en/models/2501721

### Default Wiring

| Display Pin | ESP32-S3 GPIO |
|---|---|
| MOSI (SDA) | 11 |
| SCLK (SCL) | 12 |
| CS | 10 |
| DC | 9 |
| RST | 8 |
| BL | 13 |
| GND | GND |
| VCC | 3.3V |

Adjust pin assignments in `platformio.ini` build_flags to match your wiring.

Touch TTP223 button is optional, it is used to switch between printers, you may use standard push button and connect it between pin 4 and GND. Then pick correct button setting in web interface under Multi-Printer support

![wiring](img/wiring.png)

### Assembly Video

[![Assembly Video](https://img.youtube.com/vi/hsyamsU5UZE/maxresdefault.jpg)](https://youtu.be/hsyamsU5UZE)

## Flashing

1. Download the latest `BambuHelper-WebFlasher.bin` from [Releases](../../releases)
2. Open [ESP Web Flasher](https://espressif.github.io/esptool-js/) in Chrome or Edge
3. Connect your ESP32-S3 via USB
4. Click **Connect** and select your device
5. Set flash address to **0x0**
6. Select the downloaded `.bin` file
7. Click **Program**

## Setup

### Configuration Guide

[![Configuration Guide](https://img.youtube.com/vi/n2RdbeHTMz0/maxresdefault.jpg)](https://youtu.be/n2R