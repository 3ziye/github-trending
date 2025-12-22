# Seeed Home Assistant Discovery

<p align="center">
  <img src="custom_components/seeed_ha_discovery/icon.png" width="128" alt="Seeed HA Discovery">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/ESP32-C3%20%7C%20C5%20%7C%20C6%20%7C%20S3-blue" alt="ESP32 Support">
  <img src="https://img.shields.io/badge/nRF52840-BLE-purple" alt="nRF52840 Support">
  <img src="https://img.shields.io/badge/Home%20Assistant-2025.12+-green" alt="Home Assistant">
  <img src="https://img.shields.io/badge/Arduino-IDE%20%7C%20PlatformIO-orange" alt="Arduino">
  <img src="https://img.shields.io/badge/HACS-Custom-41BDF5" alt="HACS Custom">
</p>

**Seeed HA Discovery** is a complete solution for easily connecting ESP32/nRF52840 devices to Home Assistant, provided by [Seeed Studio](https://www.seeedstudio.com/).

### 🎯 What Can It Do?

With just a few lines of code in **Arduino IDE** or **PlatformIO** for your **XIAO** series development boards, you can connect to Home Assistant via **WiFi** or **Bluetooth (BLE)**:

| Connection | Supported Devices | Features |
|------------|-------------------|----------|
| 📶 **WiFi** | XIAO ESP32-C3/C5/C6/S3 | Bidirectional communication, WebSocket real-time updates |
| 📡 **Bluetooth (BLE)** | XIAO ESP32-C3/C5/C6/S3, **XIAO nRF52840** | Ultra-low power, BTHome v2 protocol, passive advertising |

> 📡 **XIAO ESP32-C5** supports both 2.4GHz and 5GHz dual-band WiFi for better connectivity options

| Feature | Direction | WiFi | BLE |
|---------|-----------|------|-----|
| 📤 **Report Sensor Data** | Device → HA | ✅ | ✅ |
| 📥 **Receive Control Commands** | HA → Device | ✅ | ✅ (GATT) |
| 📷 **Camera Streaming** | Device → HA | ✅ (ESP32-S3) | ❌ |
| 🔄 **Get HA States** | HA → Device | ✅ (v2.3 New) | ✅ (v2.4 New) |
| 🔋 **Ultra-Low Power** | - | ❌ | ✅ (Broadcast Mode) |

### 💡 No Complex Configuration

- ✅ **No MQTT** - No need to set up an MQTT broker
- ✅ **No Cloud Services** - Pure local network communication, data stays at home
- ✅ **Auto Discovery** - Home Assistant automatically recognizes devices when they come online
- ✅ **Plug and Play** - Copy example code, modify configuration, and run

## ⚡ One-Click Installation

Click the button below to add this integration to your Home Assistant:

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=limengdu&repository=Seeed-Homeassistant-Discovery&category=integration)

> **Prerequisites**: Your Home Assistant must have [HACS](https://hacs.xyz/) installed

## 🔌 Web Firmware Flasher

**Don't want to set up Arduino IDE?** Use our web-based firmware flasher to program your device directly from the browser!

🌐 **[Open Web Flasher](https://limengdu.github.io/Seeed-Homeassistant-Discovery/)**

| Feature | Description |
|---------|-------------|
| 🖥️ **No Software Required** | Flash directly from Chrome/Edge browser |
| 🔍 **Auto Chip Detection** | Automatically detects ESP32-C3/C5/C6/S3 |
| 📦 **Pre-built Firmware** | Ready-to-use examples for quick start |
| 🌍 **Bilingual** | English and Chinese interface |

**Available Firmware:**

| Category | Firmware | Supported Chips |
|----------|----------|-----------------|
| 🏷️ **Seeed Products** | IoT Button V2 | ESP32-C6 |
| 🏷️ **Seeed Products** | CameraStream | ESP32-S3 Sense |
| 🏷️ **Seeed Products** | reTerminal E1001/E1002 | ESP32-S3 |
| 🔧 **Universal** | WiFi Provisioning | C3/C5/C6/S3 |
| 🔧 **Universal** | Button Switch | C3/C5/C6/S3 |
| 🔧 **Universal** | LED Switch | C5/C6/S3 |
| 🔧 **Universal** | HA State Subscribe | C3/C5/C6/S3 |
| 🔧 **Universal** | Temperature & Humidity | C3/C5/C6/S3 |

> 💡 **Tip**: Universal firmware supports auto chip detection - just connect your XIAO board and click flash!

## ✨ Features

### WiFi Version
- 🔍 **Auto Discovery** - Devices are automatically discovered by Home Assistant after connecting to WiFi
- 📡 **Real-time Communication** - Bidirectional real-time communication using WebSocket
- 🎯 **Simple to Use** - Connect sensors to HA with just a few lines of code
- 🌡️ **Sensor Support** - Support for temperature, humidity, and various other sensors (upstream data)
- 💡 **Switch Control** - Support for LED, relay, and other switch controls (downstream commands)
- 📷 **Camera Streaming** - Support XIAO ESP32-S3 Sense camera live feed (v2.2 New)
- 🔄 **HA State Subscription** - Device can subscribe to HA entity states, ideal for display applications (v2.3 New)
- 📱 **Status Page** - Built-in web page to view device status

### BLE Version (v2.0 New)
- 🔋 **Ultra-Low Power** - Passive broadcast mode, suitable for battery-powered devices
- 📡 **BTHome v2** - Uses the BTHome protocol natively supported by Home Assistant
- 🎯 **Zero Configuration** - No additional integration needed, HA automatically recognizes BTHome devices
- 📱 **Support nRF52840** - Not limited to ESP32, also supports XIAO nRF52840
- 🔘 **Event 