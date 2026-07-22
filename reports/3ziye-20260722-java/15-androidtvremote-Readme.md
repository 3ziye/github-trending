# Remote for Android TV

[![Android CI](https://github.com/harimoradiya/TV-Remote-for-Android-TV/actions/workflows/android.yml/badge.svg)](https://github.com/harimoradiya/TV-Remote-for-Android-TV/actions/workflows/android.yml)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![App Model](https://img.shields.io/badge/App--Model-100%25_Free-brightgreen.svg)]()
[![Ads](https://img.shields.io/badge/Ads-None-brightgreen.svg)]()
[![Google Play](https://img.shields.io/badge/Google_Play-Get_it_on-green?logo=googleplay&logoColor=white)](https://play.google.com/store/apps/details?id=com.hari.androidtvremote)

A fast, privacy-focused, and completely free Android TV remote control app that lets users control Android TV and compatible Smart TVs over the same Wi-Fi network.

No ads. No subscriptions. No premium locks. Just a simple and reliable TV remote experience.

<p align="center">
  <a href="https://play.google.com/store/apps/details?id=com.hari.androidtvremote">
    <img src="https://play.google.com/intl/en_us/badges/static/images/badges/en_badge_web_generic.png" width="200" alt="Get it on Google Play" />
  </a>
</p>

---

## Why I Built This

I built TV Remote for Android TV to make everyday TV control simpler when a physical remote is missing, out of battery, or inconvenient to use. My goal is to provide a fast, clean, and reliable remote experience without advertisements, subscriptions, or feature restrictions.

This project is designed for people who want a practical TV remote that respects their time and privacy.

---

## Feel the Remote

TV Remote for Android TV is designed to feel familiar from the first tap. The interface focuses on the controls people use most: navigation, select, back, home, volume, power, and keyboard input.

The goal is simple: pick up your phone, connect to your TV, and control it naturally.

---

## Features

- **Local Network Auto-Discovery**: Automatic discovery of compatible Android TVs on the same local Wi-Fi network using **ConnectSDK** (Chromecast, Cast services).
- **Smooth Navigation**: D-pad control and gesture touchpad controls.
- **Universal Input controls**: Select, Back, Home, and TV Menu buttons.
- **Volume and Power Controls**: Control your TV volume and trigger power-off/standby (on supported TVs).
- **IME Keyboard Sync**: Sync typing from your mobile device directly to your Android TV search fields and text boxes.
- **Customizable App Strip**: Reorder quick-launch applications shown at the top strip of the remote (fully unlocked for all users).
- **Appearance Customization**: Dynamically extract wallpaper colors (Material You) and customize basic color themes.
- **Zero Monetization**: Free of AdMob SDK, billing client integrations, tracking libraries, and paywalls.

---

## Screenshots

<p align="center">
  <img src="docs/images/discovery.png" width="260" alt="TV discovery screen" />
  <img src="docs/images/home.png" width="260" alt="Home screen" />
  <img src="docs/images/remote.png" width="260" alt="Remote control screen" />
 
</p>

---

## Technology Stack

- **Kotlin**: Language of choice for clean, modern Android development.
- **Jetpack Compose**: Modern declarative toolkit for building high-performance UIs.
- **Material Design 3**: Google's latest design system for fluid, responsive components and colors.
- **Coroutines & Flow**: Async programming and reactive data streams.
- **Jetpack DataStore**: Safe, async preference storage.
- **ConnectSDK**: Service discovery library supporting Chromecast/Cast protocol.
- **Protobuf**: Android TV pairing and messaging protocol parsing.
- **BouncyCastle**: Encryption provider for SSL/TLS pairing certificates.
- **Java-WebSocket**: Communication layer for remote commands.
- **Retrofit & OkHttp**: Rest client for APIs and backend configurations.
- **NanoHTTPD**: Lightweight embedded HTTP server to support media casting.

---

## Architecture Overview

The project uses clean architectural design patterns with structured separation of concerns:
- **UI & Presentation**: Jetpack Compose screens and themes. State management is driven by a single unified `TvRemoteViewModel` exposed as `StateFlow`.
- **Navigation**: Structured graph defined in `AppNavGraph.kt`.
- **Low-Level Android TV Lib**: Lower-level pairing, certificate generation, connection handshake, and protocol message delivery are managed cleanly in `androidLib/`.
- **Services**: `CastService` and `KeepAliveService` ensure background connection stability and notifications are handled cleanly without memory leaks.

---

## Requirements

- Android SDK version 24 (Android 7.0) or higher.
- Java Development Kit (JDK) 17.
- A physical Android TV or Android TV emulator.
- Both devices (Phone and TV) must be connected to the exact same Wi-Fi subnet.

---

## Installation and Build Instructions

To build the project yourself:

1. Clone the repository:
   ```bash
   git clone https://github.com/harimoradiya/TV-Rem