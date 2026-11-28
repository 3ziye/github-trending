<p align="center">
  <img src="GestaltX/Assets.xcassets/AppIcon.appiconset/AppIcon.png" alt="GestaltX" width="112" height="112">
</p>

<h1 align="center">GestaltX</h1>

[![Version](https://img.shields.io/badge/version-1.0.6-blue)](https://github.com/huamidev/GestaltX)
[![Platform](https://img.shields.io/badge/iOS-27.x-black?logo=apple)](#compatibility)
[![SwiftUI](https://img.shields.io/badge/Swift-SwiftUI-orange?logo=swift)](https://github.com/huamidev/GestaltX)
[![License](https://img.shields.io/badge/license-GPLv3-blue)](LICENSE)

[English](README.md) · [简体中文](README_ZH-CN.md) · [日本語](README_JA.md) · [한국어](README_KO.md) · [Türkçe](README_TR.md)

A MobileGestalt editor for iPhone and iPad. Developed by [huamidev](https://github.com/huamidev).

## Features

| Category | Presets and tools |
| --- | --- |
| Display | Dynamic Island capability and layout, Always-On Display, AOD Vibrancy, high-luminance AOD, AOD flipbook, HDR photo display, wallpaper parallax, Liquid Glass low-power rendering, experimental PWM and DisplayPort flags |
| Device | Model name, boot/shutdown chime, charge limit, tap to wake, Camera Control settings, Action Button settings, Collision SOS, Audio Mix, Spatial FaceTime audio |
| iPad | Apple Pencil settings, Stage Manager capability, iPad app compatibility |
| Intelligence | Independent region-code options, Apple Intelligence capability flag, on-device Siri, Audio Intelligence, Personal Translator, Photos Clean Up, Handwriting Synthesis, always-listening Hey Siri, and sales-region options for activation attempts on China-mainland devices |
| Advanced | Apple internal feature flags, the system-wide InternalBuild flag with explicit enable confirmation, internal settings bundle, Security Research Device flag |
| Field editor | Read, search, add, edit, and remove `CacheExtra` fields; local plist import/export; String, Integer, Real, Boolean, Data, Date, Array, and Dictionary values |
| Changes | Automatic reading and manual re-read, staged before/after review, verified writes, per-preset restore |
| Backups | Automatic initial backup before device editing, backup before every write, original-value records; open, export, restore, and delete |
| Logs & respring | Actual exploit-stage logs and manual NeoSpring respring |

Usually, changing the region code is enough to try enabling AI; there is no need to change Sales Region. Selecting United States for Region Code sets `RegionCode` to `LL` and keeps the sales-region suffix. You can also choose China (Mainland), Hong Kong, Taiwan, Japan or the United Kingdom. Sales Region and Region Code can be applied together: the sales suffix follows Sales Region, while the code follows Region Code.

*If you previously changed Sales Region, restore your device’s original sales region and apply it first.*

Disabling a preset or using its Revert button restores the recorded original values and types. Keys that were originally absent are removed. If an older change has no original record, use Remove Added Fields only when you know those fields were added.

Presets modify capability flags; actual effects depend on the device and OS. China-mainland devices can use the Apple Intelligence and region options to attempt activation; availability also depends on the model, OS version, and Apple services.

### Apple Intelligence, Face ID and dictation

The [YumEdit 1.2.1 approach](https://github.com/H4CNPE/YumEdit/tree/v1.2.1) avoids spoofing the product, board and CPU. In Intelligence, **Apple Intelligence Capability** sets the generative-model flag to `1`, while the separate **Siri AI Mode** preset sets `SiriMode` to `2`. Neither changes hardware identity nor the device-specific On-Device Siri capability. These are experimental flags, not a guarantee of resource downloads or working Apple Intelligence. YumEdit later replaced this activation approach with an experimental two-stage workflow; GestaltX does not implement temporary hardware spoofing.

If a previous hardware spoof broke Face ID or dictation, choose an original device backup in **Backups → Restore Hardware Identity**. Alternatively, import a verified original plist and use **Intelligence → Restore Hardware Identity**. Save or discard pending changes first. Recovery requires a verified same-device backup with the same `CacheData`, `CacheUUID` and cache version, whose product and board match the kernel-reported hardware. It restores only product, board, CPU and the original regulatory model number, preserving current AI, Siri, region and unrelated settings. Unlike YumEdit's region activation, recovery does not substitute a US regulatory model. Missing, incompatible or already-spoofed backups are rejected; original hardware values are never guessed.

Recovery currently recognizes iPhone 11 through iPhone 15/15 Plus (including the second- and third-generation SE), checking the original CPU against the known chip for the physical product. Other products are rejected rather than guessing their chip. A backup is c