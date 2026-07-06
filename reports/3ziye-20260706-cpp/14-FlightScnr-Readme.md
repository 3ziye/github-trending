# FlightScnr: Mini ADS-B Radar Style Flight Scanner

The best part? There is absolutely no coding or soldering required!
<p align="center">
<img width="1353" height="863" alt="image" src="https://github.com/user-attachments/assets/5275eb54-d5cf-4815-b19a-85e70ee04339" />
</p>

[![Youtube Video](https://github.com/user-attachments/assets/0ef2ec23-e1fe-4496-82ae-cd5a6211d24c)](https://youtube.com/shorts/vinE6DK6SSY?si=bhuOrcAyPHRql8ar)
<p align="center">
  <a href="https://buymeacoffee.com/yashmulgaonkar" target="_blank">
    <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me a Coffee" style="height: 35px;">
  </a>
</p>


Open-source firmware that shows **live ADS-B traffic** on a sweeping radar around your preset position. Built for the **[LilyGO T-Encoder Pro](https://www.lilygo.cc/zo4apl)**, inspired by **[ESP32-Plane-Radar](https://github.com/MatixYo/ESP32-Plane-Radar)** and **[deskradar](https://github.com/arvis91/deskradar)**.

Firmware is **[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)** ([LICENSE](LICENSE)) - shareable for hobbyists, not for closed commercial forks.

**Enclosure:** [MakerWorld](https://makerworld.com/en/models/2902669-flightscnr-live-ads-b-traffic-sweeping-radar#profileId-3245055) (separate license - see [below](#enclosure-license)).

## Features

- **Radar** - sweeping display with range rings (2–30 mi presets: 2, 3, 6, 8, 10, 20, 30; default 8), compass rose, optional sweep line, themed colors (Green default), km/mi/nm units, rim dots for out-of-range traffic. Live ADS-B via [adsb.fi](https://adsb.fi), ~2s refresh, up to 64 aircraft.
- **Flight detail** - tap a blip or short-press the knob: callsign, airline logo/name, route, ICAO type, altitude, speed. Knob cycles visible aircraft. Optional route lookup (see [APIs](#optional-apis)).
- **Clock & forecast** - swipe down from radar: NTP time, date, current weather, sunrise/sunset. Swipe right for a 3-day forecast (hi/lo, icons, rain %).
- **Auto timezone** - Fetch Timezone + DST from your radar center ([timeapi.io](https://timeapi.io), no API key needed). Manual UTC offset on-device disables auto until re-enabled on the web portal.
- **Tomorrow.io weather** - optional key + enable checkbox on the web portal; metric or imperial.
- **Auto-idle clock** (default on) - empty radar (no in-range aircraft) switches to the clock; returns when traffic appears.
- **Settings** - three on-device pages (network/API status, display/timeouts, color/beep) plus full config at [http://flightscnr.local/](http://flightscnr.local/). Web **Save** applies live - no reboot.

Screen timeouts (configurable on web or device page 2): flight detail 10/20/30s or manual; clock/forecast 5/10/15s or manual. Settings and about auto-return to radar after 10s 

## Navigation

**From radar:** knob = range preset · tap / short press = flight detail · swipe ↓ clock · ↑ about · ← settings

**From clock:** ← clock settings · → forecast · ↑ radar

**From forecast:** ← clock · ↑ radar

**From flight detail / settings / about:** swipe right (or timeout) → back

**Everywhere:** hold knob **3 s** = Wi‑Fi reset (setup portal). Do **not** hold the screen at power-on - that is BOOT/download mode.

On-device settings: page 2 = brightness, units, compass, sweep, timeouts, idle clock. Page 3 = radar color, beep on/off, tone A–E.

## Setup

1. Power on → join **FlightScnr-AP** if prompted.
2. Open [http://4.3.2.1](http://4.3.2.1) or [http://flightscnr.local](http://flightscnr.local) → enter Wi‑Fi credentials. Reboot the unit.
3. After connect: boot splash (~5 s) → radar.
4. Set radar center, weather key, and optional route APIs at [http://flightscnr.local/](http://flightscnr.local/) (or device IP shown on settings page 1).

To change settings later: same URL, **Save**. To reset Wi‑Fi only: hold knob 3s 

## Screenshots

**Flight detail** - route, airline logo, altitude, speed
<img width="1283" height="582" alt="Flight detail" src="https://github.com/user-attachments/assets/73eca09d-6f75-4bc9-83c2-7e8bcf1104f3" />


**Settings** - network, display, color & audio (3 pages via swipe left)
<img width="1103" height="759" alt="Settings" src="https://github.com/user-attachments/assets/d8b57bbf-a991-4100-881a-8cd8d8bacabf" />


**Clock** - time, weather, sunrise/sunset (→ forecast on swipe right)
<img width="951" height="481" alt="Clock" src="https://github.com/user-attachments/assets/26a35f9c-ac2d-4aea-9466-72e303b03494" />


## Hardware


| Item          | Details                                                                                                                             |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Board**     | [LilyGO T-Encoder Pro](https://www.lilygo.cc/zo4apl) - ESP32-S3, 16 MB flash, 8 MB PSRAM                                            |
| **Display**   | 1.2″ 390×390 AMOLED; auto-detects DX