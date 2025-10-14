# 🏴‍☠️ PIrateRF - Software-Defined Radio Transmission Platform

![PIrateRF](./assets/piraterf.png)

**PIrateRF** transforms your **Raspberry Pi Zero W** into a portable RF signal generator that spawns its own WiFi hotspot. Control everything from FM broadcasts to digital modes through your browser - hack the airwaves from anywhere! 📡⚡

**[🎬 Click here for PIrateRF Promo Video](https://www.youtube.com/watch?v=hnYkvDLOi70)**

**[📺 Click here for PIrateRF Showcase Video](https://www.youtube.com/watch?v=7DeMhe47aNQ)**

---

**⚠️ LEGAL NOTICE**

PIrateRF is designed for amateur radio experimentation and education - including safe indoor testing without external antennas. Built for engineers who understand that good RF practices matter more than arbitrary administrative boundaries. Users are responsible for compliance with all local RF regulations and licensing requirements. I am not responsible for any of your stupid fuckin' decisions!

**All demonstration images and testing in this documentation were performed indoors without an antenna, with a maximum range of approximately 5 meters.**

---

## 📋 Table of Contents

- [🎯 11 Different Transmission Modes](#-11-different-transmission-modes)
- [🚀 Quick Setup Guide](#-quick-setup-guide)
  - [Prerequisites](#prerequisites)
  - [Option 1: Pre-Built Image (Recommended)](#option-1-pre-built-image-recommended)
  - [Option 2: Manual Build Setup](#option-2-manual-build-setup)
    - [🚨 IMPORTANT: Pi Zero Setup First!](#-important-pi-zero-setup-first)
    - [1. Initial Setup](#1-initial-setup)
    - [2. Complete Pi Setup](#2-complete-pi-setup)
    - [3. Connect and Use](#3-connect-and-use)
- [🎉 Pirate Crew Mode](#-pirate-crew-mode)
- [🔌 Antenna Setup](#-antenna-setup)
- [📡 Transmission Modes Explained](#-transmission-modes-explained)
  - [🎵 FM Station](#-fm-station)
  - [🎙️ Live Microphone Broadcast](#️-live-microphone-broadcast)
  - [📟 FT8](#-ft8)
  - [📠 RTTY](#-rtty)
  - [📊 FSK](#-fsk)
  - [📱 POCSAG](#-pocsag)
  - [📻 Morse Code](#-morse-code)
  - [🎛️ Carrier Wave](#️-carrier-wave)
  - [🌊 Frequency Sweep](#-frequency-sweep)
  - [📺 SSTV](#-sstv)
  - [🎨 Spectrum Paint](#-spectrum-paint)
- [🛠️ Development Commands](#️-development-commands)
  - [Local Development](#local-development)
  - [Pi Management](#pi-management)
- [📁 Project Structure](#-project-structure)
- [🏴‍☠️ Legal and Safety Notice](#️-legal-and-safety-notice)
  - [Amateur Radio License Required](#amateur-radio-license-required)
  - [Frequency Regulations](#frequency-regulations)
  - [Hardware Requirements (for proper use)](#hardware-requirements-for-proper-use)
  - [Geographic Restrictions](#geographic-restrictions)
  - [🏠 Indoor Testing & Experimentation](#-indoor-testing--experimentation)
- [📡 Standard Operating Frequencies](#-standard-operating-frequencies)
  - [HF Amateur Bands (3-30 MHz)](#hf-amateur-bands-3-30-mhz)
  - [VHF/UHF Amateur Bands](#vhfuhf-amateur-bands)
  - [FT8 Standard Frequencies (USB mode)](#ft8-standard-frequencies-usb-mode)
  - [RTTY Standard Frequencies (USB mode)](#rtty-standard-frequencies-usb-mode)
  - [SSTV Standard Frequencies](#sstv-standard-frequencies)
  - [FM Repeater Standard Splits](#fm-repeater-standard-splits)
- [🔗 Core Dependencies](#-core-dependencies)
- [📝 License](#-license)
- [TODO](#todo)

## 🎯 11 Different Transmission Modes

- **🎵 FM Station** - Full FM broadcasting with RDS metadata, playlists, and audio processing
- **🎙️ Live Microphone Broadcast** - Real-time microphone streaming with configurable modulation (AM/DSB/USB/LSB/FM/RAW)
- **📟 FT8** - Long-range digital mode for weak-signal communication on HF bands
- **📠 RTTY** - Radio teletype using Baudot code and FSK modulation
- **📊 FSK** - Frequency Shift Keying for digital data transmission
- **📱 POCSAG** - Digital pager messaging system
- **📻 Morse Code** - CW transmission with configurable WPM
- **🎛️ Carrier Wave** - Simple carrier generation for testing
- **🌊 Frequency Sweep** - RF sweeps for antenna testing and analysis
- **📺 SSTV** - Slow Scan Television image transmission
- **🎨 Spectrum Paint** - Convert images to RF spectrum art

All controlled through a **standalone WiFi access point** - connect any device and start transmitting like the RF rebel you were meant to be! Perfect for international waters operations and regions with more... flexible spectrum policies.

## 🚀 Quick Setup Guide

### Prerequisites

- **Raspberry Pi Zero 1 W** (original model) with 4GB+ SD card
  - **⚠️ Pi Zero 2 W does NOT work** - rpitx requires the BCM2835 chip (Pi Zero 1 W) for predictable clock timing. The Pi Zero 2 W uses BCM2710A1 which breaks rpitx's timing assumptions.

### Option 1: Pre-Built Image (Recommended)

Skip all the build bullshit and get straight to RF chaos:

1. **Download** the pre-built image: [PIrateRF Image v2025-10-06](https://archive.org/download/piraterf-2025-10-06-12-19-14-20251006092641/piraterf_2025-10-06_12-19-14.img)
2. **Flash** to SD card using:
   - **Raspberry Pi Imager** (recommended): Select "U