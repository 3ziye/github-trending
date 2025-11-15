![License](https://img.shields.io/badge/license-GPLv3-blue.svg)
![C](https://img.shields.io/badge/C-ESP--IDF-orange.svg)
![Platform](https://img.shields.io/badge/platform-ESP32--S3-red.svg)
![Status](https://img.shields.io/badge/status-experimental-orange.svg)

# 🛜 ESPectre 👻

**Motion detection system based on Wi-Fi spectre analysis (CSI), with Home Assistant integration.**

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
- [License](#-license)
- [Author](#-author)

---

## 🎯 In 3 Points

1. **What it does**: Detects movement at home using Wi-Fi (no cameras, no microphones)
2. **What you need**: A ~€10 device (ESP32-S3) + Home Assistant or MQTT server + ESP-IDF development tools
3. **Setup time**: 30-45 minutes (first time, including ESP-IDF setup)

---

## 🔬 Mathematical Approach

**This project currently does NOT use Machine Learning models.** Instead, it employs a **mathematical approach** that extracts **10 features** from CSI (Channel State Information) data using statistical and signal processing techniques.

### Key Points

- ✅ **No ML training required**: Works out-of-the-box with mathematical algorithms
- ✅ **10 extracted features**: Statistical, spatial, and temporal features
- ✅ **Real-time processing**: Low latency detection on ESP32-S3 hardware
- ✅ **Foundation for ML**: These features can serve as the basis for collecting labeled datasets to train ML models for advanced tasks (people counting, activity recognition, gesture detection)

The mathematical approach provides excellent movement detection without the complexity of ML model training, while the extracted features offer a solid foundation for future ML-based enhancements.

---

## 🛒 What You Need

### Hardware (Total: ~€10)

- ✅ **2.4GHz Wi-Fi Router** (the one you already have at home works fine)
- ✅ **ESP32-S3 DevKit bundle with external antennas** (~€10) - Available on Amazon, AliExpress, or electronics stores

![3 x ESP32-S3 DevKit bundle with external antennas](images/home_lab.jpg)
*ESP32-S3 DevKit with external antennas (recommended for better reception)*

### Software (All Free)

- ✅ **MQTT Broker** (required for operation):
  - **Home Assistant** with built-in MQTT broker (on Raspberry Pi, PC, NAS, or cloud)
  - OR standalone **Mosquitto** MQTT server (can run on any device, including Raspberry Pi)
- ✅ **ESP-IDF v6.1** (development framework for building firmware)

### Required Skills

- ✅ **Basic command line knowledge** required for building and flashing firmware
- ❌ **NO** router configuration needed
- ✅ Follow the setup guide in SETUP.md

---

## 🚀 Quick Start

**Setup time**: ~30-45 minutes (first time)  
**Difficulty**: Intermediate (requires ESP-IDF setup)

1. **Setup & Installation**: Follow the complete guide in [SETUP.md](SETUP.md)
2. **Calibration & Tuning**: Optimize for your environment with [CALIBRATION.md](CALIBRATION.md)

---

## 📖 How It Works (Simple Version)

When someone moves in a room, they "disturb" the Wi-Fi waves traveling between the router and the sensor. It's like when you move your hand in front of a flashlight and see the shadow change.

The ESP32-S3 device "listens" to these changes and understands if there's movement.

### Advantages

- ✅ **No cameras** (total privacy)
- ✅ **No wearables needed** (no bracelets or sensors to wear)
- ✅ **Works through walls** (Wi-Fi passes through walls)
- ✅ **Very cheap** (~€10 total)

<details>
<summary>📚 Technical Explanation (click to expand)</summary>

### What is CSI (Channel State Information)?

**Channel State Information (CSI)** represents the physical characteristics of the wireless communication channel between transmitter and receiver. Unlike simple RSSI (Received Signal Strength Indicator), CSI provides rich, multi-dimensional data about the radio channel.

#### What CSI Captures

**Per-subcarrier information:**
- **Amplitude**: Signal strength for each OFDM subcarrier (up to 64)
- **Phase**: Phase shift of each subcarrier
- **Frequency response**: How the channel affects different frequencies

**Environmental effects:**
- **Multipath propagation**: Reflections from walls, furniture, objects
- **Doppler shifts**: Changes caused by movement
- **Temporal variations**: How the chan