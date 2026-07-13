# Sony Head Tracker

Use the motion sensors already inside compatible Sony headphones and earbuds as
a real-time head tracker on Windows or macOS.

[![Build](https://github.com/NicholasSlattery/sony-head-tracker/actions/workflows/build.yml/badge.svg)](https://github.com/NicholasSlattery/sony-head-tracker/actions/workflows/build.yml)
[![Latest release](https://img.shields.io/github/v/release/NicholasSlattery/sony-head-tracker)](https://github.com/NicholasSlattery/sony-head-tracker/releases/latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Platform: Windows 11](https://img.shields.io/badge/platform-Windows%2011-0078D6.svg)](#build)
[![Platform: macOS 14+](https://img.shields.io/badge/platform-macOS%2014%2B-000000.svg)](docs/MACOS.md)
[![Language: C++20](https://img.shields.io/badge/C%2B%2B-20-00599C.svg)](#build)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20me%20a%20coffee-support-yellow?style=for-the-badge)](https://buymeacoffee.com/nicholasslattery)
> **Unofficial** open-source bridge. Not affiliated with or endorsed by
> Sony.

https://github.com/user-attachments/assets/851e4ff7-3134-45e9-90b4-a0fa42258730

Sony Head Tracker connects to the Android Head Tracker sensor exposed by
supported Sony Bluetooth devices, reads live orientation and gyroscope data, and
sends yaw, pitch, and roll to [OpenTrack](https://github.com/opentrack/opentrack)
or your own applications.

No webcam, infrared tracker, additional hardware, firmware modification, or
custom kernel driver is required.

Originally developed and tested for the Sony WH-1000XM5, the project now supports
any compatible Sony headset that exposes the standard
[Android Head Tracker HID protocol](https://source.android.com/docs/core/interaction/sensors/head-tracker-hid-protocol).

If you arrived searching for **Sony WH-1000XM5 head tracking on Windows**, how to
**use WH-1000XM5 with OpenTrack**, or an **XM5 head tracker for Assetto Corsa** or
other sims, you are in the right place: the WH-1000XM5 is the reference device,
and the same bridge now works across the wider Sony range.

## What you can do with it

- Use compatible Sony headphones for head tracking in racing and flight
  simulators.
- Send live yaw, pitch, and roll to OpenTrack.
- Read orientation, quaternion, and gyroscope data through a local JSON stream.
- Inspect sensor activity through the included native diagnostics interfaces.
- Test additional Sony models with the read-only compatibility probe.

## Featured in

- [PC Gamer — This free software aims to turn Sony headphones into a head tracker for '200+ PC games'](https://www.pcgamer.com/hardware/gaming-headsets/this-free-software-aims-to-turn-sony-headphones-into-a-head-tracker-for-200-pc-games/)
- [Tom's Hardware — You can now use your Sony headphones as a free real-time head tracker for race and flight simulators on PC](https://www.tomshardware.com/video-games/pc-gaming/you-can-now-use-your-sony-headphones-as-a-real-time-head-tracker-for-race-and-flight-simulators-on-pc-several-hundred-games-already-supported-enthusiast-creates-open-source-app-that-translates-live-sensor-data-into-in-game-camera-controls)
- [TechLinked — Sony Headphones Become Head Trackers](https://youtu.be/ITmMIqiJwOg?si=M28zLj3hcO0RshHZ&t=405)
- [GSMArena — Developer turns Sony's headphones into real-time head tracker for PC simulators](https://www.gsmarena.com/developer_turns_sonys_headphones_into_realtime_head_tracker_for_pc_simulators-news-73610.php)
- [Hackaday — Flight Sim Tracking From Spatial Audio](https://hackaday.com/2026/07/06/flight-sim-tracking-from-spatial-audio/)
- [Techspot — A free app lets Sony headphones do head tracking for racing and flight sims](https://www.techspot.com/news/113019-free-app-sony-headphones-do-head-tracking-racing.html)
- [SoundGuys — This free app turns Sony WH-1000XM5 into head trackers for PC gaming](https://www.soundguys.com/sony-headphones-windows-head-tracking-159435/)


## Quick start

### Windows 11

1. Download `sony-head-tracker.exe` from the
   [latest release](https://github.com/NicholasSlattery/sony-head-tracker/releases/latest)
   (or [build it yourself](#build), it is one `cl` command).
2. [Pair your compatible Sony headphones or earbuds](#pair-the-headphones)
   through Windows 11.
3. Open the application. It automatically discovers compatible head-tracking
   sensors, displays live orientation data, and streams tracking output while it
   is open.
4. **Starting the app for the first time on a fresh boot? Press Repair Tracker
   first.** Windows very often pairs a Sony headset but does not create the
   head-tracker sensor node until something nudges it, so on a cold boot the app
   frequently shows nothing at first. Press the **Repair Tracker** button and
   approve the single administrator prompt. This is the normal first step, not a
   sign that anything is broken, and it is exactly what the button is for. After
   the app reopens, your headset should appear.
5. For 