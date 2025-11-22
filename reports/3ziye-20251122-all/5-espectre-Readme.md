[![License](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://github.com/francescopace/espectre/blob/main/LICENSE)
[![C](https://img.shields.io/badge/C-ESP--IDF-orange.svg)](https://github.com/espressif/esp-idf)
[![Platform](https://img.shields.io/badge/platform-ESP32--S3%20%7C%20ESP32--C6-red.svg)](https://www.espressif.com/en/products/socs)
[![Status](https://img.shields.io/badge/status-experimental-orange.svg)](https://github.com/francescopace/espectre)
[![Changelog](https://img.shields.io/badge/changelog-v1.2.0-blue.svg)](https://github.com/francescopace/espectre/blob/main/CHANGELOG.md)

# 🛜 ESPectre 👻

**Motion detection system based on Wi-Fi spectre analysis (CSI), with Home Assistant integration.**

**📰 Featured Article**: Read the complete story behind ESPectre on Medium **[🇮🇹 Italian](https://medium.com/@francesco.pace/come-ho-trasformato-il-mio-wi-fi-in-un-sensore-di-movimento-40053fd83128?source=friends_link&sk=46d9cfa026790ae807ecc291ac5eac67&utm_source=github&utm_medium=readme&utm_campaign=espectre)**, **[🇬🇧 English](https://medium.com/@francesco.pace/how-i-turned-my-wi-fi-into-a-motion-sensor-61a631a9b4ec?sk=c7f79130d78b0545fce4a228a6a79af3&utm_source=github&utm_medium=readme&utm_campaign=espectre)**

**⚠️ Disclaimer**: This is an experimental project for educational and research purposes. The author assumes no responsibility for misuse or damage resulting from the use of this system. Use responsibly and in compliance with applicable laws.

---

## 📑 Table of Contents

- [In 3 Points](#-in-3-points)
- [Mathematical Approach](#-mathematical-approach)
- [What You Need](#-what-you-need)
- [Quick Start](#-quick-start)
- [How It Works](#-how-it-works-simple-version)
- [What You Can Do With It](#-what-you-can-do-with-it)
- [Sensor Placement Guide](#-where-to-place-the-sensor)
- [System Architecture](#️-system-architecture)
- [FAQ](#-faq-for-beginners)
- [Security and Privacy](#-security-and-privacy)
- [Technical Deep Dive](#-technical-deep-dive)
- [Future Evolutions](#-future-evolutions-ai-approach)
- [References](#-references)
- [Changelog](#-changelog)
- [License](#-license)
- [Author](#-author)

---

## 🎯 In 3 Points

1. **What it does**: Detects movement using Wi-Fi (no cameras, no microphones)
2. **What you need**: A ~€10 device (ESP32-S3 or ESP32-C6) + Home Assistant or MQTT server
3. **Setup time**: 30-45 minutes (first time, including ESP-IDF setup)

---

## 🔬 Mathematical Approach

**This project currently does NOT use Machine Learning models.** Instead, it employs a **mathematical approach** that extracts **10 features** from CSI (Channel State Information) data using statistical and signal processing techniques.

### Key Points

- ✅ **No ML training required**: Works out-of-the-box with mathematical algorithms
- ✅ **10 extracted features**: Statistical, spatial, and temporal features
- ✅ **Real-time processing**: Low latency detection on ESP32 hardware (S3/C6)
- ✅ **Foundation for ML**: These features can serve as the basis for collecting labeled datasets to train ML models for advanced tasks (people counting, activity recognition, gesture detection)

The mathematical approach provides excellent movement detection without the complexity of ML model training, while the extracted features offer a solid foundation for future ML-based enhancements.

---

## 🛒 What You Need

### Hardware

- ✅ **2.4GHz Wi-Fi Router** - the one you already have at home works fine
- ✅ **ESP32-S3 or ESP32-C6** - Available on Amazon, AliExpress, or electronics stores

📖 See [ESP32-PLATFORM-SUPPORT.md](ESP32-PLATFORM-SUPPORT.md) for detailed platform comparison and recommendations

![3 x ESP32-S3 DevKit bundle with external antennas](images/home_lab.jpg)
*ESP32-S3 DevKit with external antennas*

### Software (All Free)

- ✅ **MQTT Broker** (required for operation):
  - **Home Assistant** with built-in MQTT broker (on Raspberry Pi, PC, NAS, or cloud)
  - OR standalone **Mosquitto** MQTT server (can run on any device, including Raspberry Pi)
- ✅ **ESP-IDF v6.1** (development framework for building firmware)

### Required Skills

- ✅ **Basic command line knowledge** required for building and flashing firmware
- ❌ **NO** router configuration needed

---

## 🚀 Quick Start

**Setup time**: ~30-45 minutes (first time)  
**Difficulty**: Intermediate (requires ESP-IDF setup)

1. **Setup & Installation**: Follow the complete guide in [SETUP.md](SETUP.md)
2. **Calibration & Tuning**: Optimize for your environment with [CALIBRATION.md](CALIBRATION.md)

### Web-Based Monitor

ESPectre includes a web-based monitoring interface (`espectre-monitor.html`) for real-time visualization and configuration without command line tools.

![Web Monitor Interface](images/web_monitor_chart.png)
*Real-time CSI monitoring and configuration interface*

---

## 📖 How It Works (Simple Version)

When someone moves in a room, they "disturb" the Wi-Fi waves traveling between the router and the sensor. It's like when you move your hand in fr