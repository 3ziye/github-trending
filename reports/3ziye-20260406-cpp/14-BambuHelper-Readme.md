# BambuHelper

Dedicated Bambu Lab printer monitor built with ESP32-S3 Super Mini and a 1.54" 240x240 color TFT display (ST7789).

Connects to your printer via MQTT over TLS and displays a real-time dashboard with arc gauges, animations, live stats, and optional buzzer notifications.

Beta support for CYD 320x240 displays is also available.

### Supported Printers

| Connection Mode | Printers | How it connects |
|---|---|---|
| **LAN Direct** | P1P, P1S, X1, X1C, X1E, A1, A1 Mini | Local MQTT via printer IP + LAN access code |
| **LAN Direct (Developer Mode)** | H2S, H2C, H2D | LAN-only mode + Developer Mode required - see note below |
| **Bambu Cloud (All printers)** | Any Bambu printer | Cloud MQTT via access token - no LAN mode needed |

> **H2 series LAN mode:** H2S, H2C, and H2D printers require both **LAN-only mode** and **Developer Mode** enabled in printer settings for local MQTT to work. Without Developer Mode, the printer accepts connections but does not respond to status requests. If you prefer not to enable Developer Mode, use Bambu Cloud mode instead.

> **Tip:** Use "Bambu Cloud (All printers)" if you don't want to enable LAN/Developer mode on your printer (for example to keep Bambu Handy working), if your ESP32 is on a different network than the printer, or if your printer only supports cloud mode (P2S).

### Cloud Mode Security Notice

When using Bambu Cloud, BambuHelper connects through Bambu Lab's cloud MQTT service. Here is what you need to know:

- **No credentials are stored** - BambuHelper never asks for your email or password. You extract an access token from your browser and paste it into the web interface.
- **Only the access token is stored** in the ESP32's flash memory. This token expires after about 3 months, at which point you simply paste a new one.
- **Read-only access** - BambuHelper only reads printer status. It never sends commands or modifies printer settings.
- **Same approach as other community projects** - this is the same authentication method used by the [Home Assistant Bambu Lab integration](https://github.com/greghesp/ha-bambulab), [OctoPrint-Bambu](https://github.com/jneilliii/OctoPrint-BambuPrinter), and other trusted third-party tools.

## Screenshots

| Dashboard | Web Interface - Settings | Web Interface - Gauge Colors |
|---|---|---|
| ![Dashboard](img/interface1.jpg) | ![Settings](img/screen1.png) | ![Gauge Colors](img/screen2.png) |

## CYD Display Support (Beta)

| Preview | Notes |
|---|---|
| ![CYD display](img/CYD.png) | **CYD / ESP32-2432S028** support is available and currently **beta**. This is the larger `320x240` display version. Flashing is done the same way as the standard `240x240` build, but on [ESP Web Flasher](https://espressif.github.io/esptool-js/) you should set **Baudrate: 115200** before clicking **Connect**. This low baudrate note is for **CYD only**. The standard ESP32-S3 240x240 version does not require this change. Tested behavior so far: The first connection attempt may fail - click **Disconnect** in the web tool, then **Connect** again and it should work on the second try. **Do not physically unplug the USB cable between attempts** - just use the buttons in the web flasher. [Use this firmware](https://github.com/Keralots/BambuHelper/releases/download/v2.5/BambuHelper-cyd-v2.5-Full.bin) If the display colors appear reversed (white background instead of dark), go to the web interface under **Display** and enable **Invert display colors (fix white background)**. |

## Features

- **Live dashboard** - progress arc, temperature gauges, fan speed, layer count, time remaining
- **H2-style LED progress bar** - full-width glowing bar inspired by Bambu H2 series
- **Anti-aliased arc gauges** - smooth nozzle and bed temperature arcs with color zones
- **Animations** - loading spinner, progress pulse, completion celebration
- **Web config portal** - dark-themed settings page for WiFi, network, printer, display, power, and buzzer settings
- **Network configuration** - DHCP or static IP, with optional IP display at startup
- **Display auto-off** - configurable timeout after print completion, auto-off when printer is off
- **NVS persistence** - all settings survive reboots
- **Auto AP mode** - creates WiFi hotspot on first boot or when WiFi is lost
- **Smart redraw** - only redraws changed UI elements for smooth performance
- **Customizable gauge colors** - per-gauge arc/label/value colors with preset themes
- **Multi-printer support** - monitor up to 2 printers simultaneously with auto-rotating display (ESP32-S3 only - CYD/C3 limited to 1 printer due to RAM)
- **Smart rotation** - automatically shows the printing printer; cycles between both when both are printing
- **Physical button** - optional push button or TTP223 touch sensor to cycle printers and wake display
- **Optional buzzer** - passive buzzer notifications for print finished, connected, and error events
- **OTA updates** - firmware can be updated from the web interface
- **CYD display