# WhatCable

> **What can this USB-C cable actually do?**

**Website: [whatcable.uk](https://whatcable.uk)** (overview, screenshots, and CLI docs)

A small macOS menu bar app that tells you, in plain English, what each USB-C cable plugged into your Mac can actually do, and **why your Mac might be charging slowly**.

USB-C hides a lot under one connector. Anything from a USB 2.0 charge-only cable to a 240W / 40 Gbps Thunderbolt 4 cable, all looking identical in your drawer. macOS already exposes the relevant info via IOKit; WhatCable surfaces it as a friendly menu bar popover.

<a href="https://www.producthunt.com/products/whatcable?embed=true&utm_source=badge-top-post-badge&utm_medium=badge&utm_campaign=badge-whatcable" target="_blank" rel="noopener noreferrer"><img alt="WhatCable - Know what your USB-C cable can really do | Product Hunt" width="250" height="54" src="https://api.producthunt.com/widgets/embed-image/v1/top-post-badge.svg?post_id=1153432&theme=light&period=daily&t=1779720313376"></a>

[![Latest release](https://img.shields.io/github/v/release/darrylmorley/whatcable)](https://github.com/darrylmorley/whatcable/releases/latest)
[![Platform](https://img.shields.io/badge/platform-macOS%2014%2B-blue)](https://github.com/darrylmorley/whatcable)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![WhatCable Pro](https://img.shields.io/badge/WhatCable%20Pro-%C2%A34.99-orange)](https://whatcable.uk/pro)

![WhatCable popover](docs/screenshot.webp)

## What it shows

Per port, in plain English:

- **At-a-glance headline:** Thunderbolt / USB4, USB device, Display connected, Charging only, Slow USB / charge-only cable, Nothing connected
- **Charging diagnostic:** when something's plugged in, a banner identifies the bottleneck:
  - *"Cable is limiting charging speed"* (cable rated below the charger)
  - *"Charging at 30W (charger can do up to 96W)"* (Mac is asking for less, e.g. battery near full)
  - *"Charging well at 96W"* (everything matches)
  - *"Battery full, not charging"* (plugged in, battery full, so the Mac isn't drawing power)
- **Data-speed diagnostic:** a plain-English verdict on what's limiting the link, the Mac port, the cable, or the device. For example *"Cable is limiting data speed"*, *"Device runs at 10 Gbps, this is the fastest it supports, not a cable problem"*, or *"Running slower than expected"* when the link came up degraded. Shown inline, in the CLI, and in JSON.
- **Cable e-marker info:** the cable's actual speed (USB 2.0, 5 / 10 / 20 / 40 / 80 Gbps), current rating (3 A / 5 A up to 60W / 100W / 240W), and the chip's vendor
- **Cable trust signals:** an orange card appears when the e-marker reports values that look unusual against the USB-PD spec, like a zero vendor ID, a reserved bit pattern in the speed / current / cable-latency fields, or a VID that isn't in USB-IF's published list. Wording is hedged on purpose: a flag means "this looks unusual," not "this cable is fake."
- **Charger PDO list:** every voltage profile the charger advertises (5V / 9V / 12V / 15V / 20V…) with the currently negotiated profile highlighted in real time
- **Connected device identity:** vendor name and product type, decoded from the PD Discover Identity response
- **Attached USB devices:** storage, hubs, and peripherals listed under the physical port they're plugged into, with their negotiated speed
- **Thunderbolt fabric:** when a Thunderbolt / USB4 link is active, shows per-lane speed, generation (TB3, TB4, TB5), and the full switch topology for multi-hop connections through docks
- **Cable identification:** if the cable's e-marker fingerprint matches a known cable in the bundled database, the brand and model are shown alongside the raw specs
- **Active transports:** USB 2 / USB 3 / Thunderbolt / DisplayPort
- **Desktop widget:** small, medium, and large WidgetKit widgets showing live cable status on your desktop
- **⌥-click** the menu bar icon (or flip the toggle in Settings) to reveal the underlying IOKit properties for engineers

Click the **gear icon** in the popover header to open Settings, where you can:

- Hide empty ports
- Launch at login
- Run as a regular Dock app instead of a menu bar icon
- Adjust the font size
- Show technical details (the same raw IOKit data that ⌥-click reveals)
- Switch language (English, Armenian, Brazilian Portuguese, French, German, Hindi, Italian, Japanese, Latvian, Norwegian, Polish, Russian, Simplified Chinese, Traditional Chinese, or follow your system default)
- Get notifications when cables are connected or disconnected
- Contribute anonymised port and power diagnostics to improve hardware coverage (opt-in, manual)

Right-click the menu bar icon for **Refresh**, a **Keep window open** toggle (handy for screenshots and demos), **Settings…**, **Contribute Diagnostic Data…**, **Check for Updates…**, **About**, **WhatCable on GitHub**, and **Quit**.

## WhatCable Pro

WhatCable is free and open source. If you find it useful, you can suppo