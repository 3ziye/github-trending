# Nest Thermostat Firmware Setup

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-donate-yellow.svg)](https://buymeacoffee.com/codykociemba)

> **⚠️ WARNING: EXPERIMENTAL SOFTWARE**
>
> This project is currently in the **experimental/testing phase**. Do NOT use this firmware on any thermostat that is critical for your heating or cooling needs. Flashing this firmware may brick your device or cause unexpected behavior. Only proceed if you have a backup thermostat or can afford to have your device non-functional during testing.

## A Note from the Developer

This project has blown up way more than I ever expected! I want to be transparent: this was thrown together in a couple of days, so it's still very new and a work in progress. Thank you all so much for your support and enthusiasm!

**Support the Project:**
Developing and maintaining open-source projects takes a lot of time (and late nights). If this project helped you reclaim your device or you just want to support the effort to keep this hardware usable, consider buying me a coffee. It keeps the code flowing and the development going!

<a href="https://buymeacoffee.com/codykociemba" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

**Self-Hosted Open Source Option Available:** A self-hosted open source solution has been posted on the [`open-source-prototype`](https://github.com/codykociemba/NoLongerEvil-Thermostat/tree/open-source-prototype) branch. Check out the [discussion here](https://github.com/codykociemba/NoLongerEvil-Thermostat/discussions/34) for more details.

**Hardware Alternative:** If you're interested in the hardware side of things, check out [https://sett.homes](https://sett.homes) for a drop-in PCB replacement option.

**Important:** The README instructions below are for the hosted version only. If you're adventurous, feel free to dive into the self-hosted branch. Otherwise, you may want to wait until it's been fully fleshed out if you don't want to deal with bugs.

---

This directory contains the tools and firmware needed to flash custom firmware to Nest Thermostat devices using the OMAP DFU (Device Firmware Update) interface.

## Prerequesites

You will need to have, ideally, a linux computer available. MacOS can also be used but some people are having difficulties. Windows should be able to be used with MingW or CygWin but YMMV.

⚠️ This firmware is only for Nest Generation 1 and 2. On the back plate you should see a bubble level, which should be green. If it's blue, that's gen 3 and not supported yet.

## Overview

This firmware loader uses the OMAP bootloader interface to flash custom bootloader and kernel images to Nest Thermostat devices. The device must be put into DFU mode to accept new firmware.

**Important:** After flashing this firmware, your device will no longer contact Nest/Google servers. It will operate independently and connect to the NoLongerEvil platform instead, giving you complete control over your thermostat.

## How it Works

The custom firmware flashes the device with modified bootloader and kernel components that redirect all network traffic from the original Nest/Google servers to a server we specify. This server hosts a reverse-engineered replica of their API, allowing the thermostat to function independently while giving you complete control over your device data and settings.

By intercepting the communication layer, the thermostat believes it's communicating with the official Nest infrastructure, but instead connects to the NoLongerEvil platform. This approach ensures full compatibility with the device's existing software while breaking free from Google's cloud dependency.

## Quick Start

### 1. Clone the Repository

```bash
git clone --recurse-submodules https://github.com/codykociemba/NoLongerEvil-Thermostat.git
cd NoLongerEvil-Thermostat
```

### 2. Install Prerequisites

Before building, you'll need to install some required packages:

#### Linux (Debian/Ubuntu)

```bash
sudo apt-get update
sudo apt-get install build-essential libusb-1.0-0-dev gcc pkg-config
```

#### macOS

First, install Xcode Command Line Tools:

```bash
xcode-select --install
```

Then install libusb using Homebrew (the build script will attempt to install this automatically if missing):

```bash
# Install Homebrew if you don't have it
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install libusb
brew install libusb pkg-config
```

### 3. Build the omap_loader tool

```bash
chmod +x build.sh
./build.sh
```

The build script will automatically detect your operating system (Linux, macOS, or Windows) and build the appropriate binary.

### 4. Start the firmware installer

**IMPORTANT: You must start the installer script BEFORE rebooting the device.**

#### Linux

```bash
chmod +x install.sh
./install.sh
```

#### macOS

```bash
chmod +x insta