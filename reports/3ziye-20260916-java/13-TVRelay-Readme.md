# TVRelay

[![Latest release](https://img.shields.io/github/v/release/hmartinez94/TVRelay?sort=semver)](../../releases)
[![License: PolyForm Noncommercial](https://img.shields.io/badge/license-PolyForm%20Noncommercial-blue)](LICENSE)

🌐 [Official site](https://hmartinez94.github.io/TVRelay/) — a friendlier overview than this README, if that's more your speed.

Google TV's home screen recommends a movie, you click it, and it opens whatever app the recommendation happened to come from - usually not the one you actually wanted to watch it in. TVRelay intercepts that click and opens the title in **Nuvio**, **Stremio**, **WuPlay**, **Jellyfin**, **Wholphin**, or **Moonfin** instead, with a one-tap confirmation so a stray click never redirects you by accident.

<img src=".github/screenshots/watch-now-overlay.jpg" alt="A Google TV recommendation page for the movie Obsession, with a 'Watch now in Nuvio' button from TVRelay floating over it" width="720">

*A real recommendation page, with TVRelay's confirm button floating over it.*

Free, no account, no subscription, no license check. It doesn't host or provide any content itself; it only reads the title of the thing you clicked, looks that title up, and hands you off to an app you already chose in Settings.

## Contents

- [How it works](#how-it-works)
- [Requirements](#requirements)
- [Installation](#installation)
- [Setup](#setup)
  - [Fire TV (Fire Stick)](#fire-tv-fire-stick)
- [Metadata provider](#metadata-provider-tmdb--thetvdb)
- [Limitations](#limitations)
- [Troubleshooting](#troubleshooting)
- [Building from source](#building-from-source)
- [Legal notice](#legal-notice)
- [Credits](#credits)

## How it works

Android's Accessibility API lets an app observe what's on screen for assistive purposes - TVRelay uses it narrowly, watching only for clicks on the Google TV launcher. When a click's payload includes a movie/show title, TVRelay looks it up (via [TMDB](https://www.themoviedb.org/) by default, or optionally TheTVDB) and offers to open it in your chosen player. Every other click - app icons, menus, anything that isn't a recommendation - is left completely alone, and nothing is read, stored, or sent anywhere beyond that one lookup.

Not every recommendation card exposes a title this way; see [Limitations](#limitations).

## Requirements

- A device with the **Google TV** launcher (Chromecast with Google TV, or Google TV editions from Sony, TCL, Hisense, etc.). Fire TV doesn't run this launcher out of the box - it uses a separate "Fire TV mode" instead; see [Setup → Fire TV](#fire-tv-fire-stick).
- **Nuvio**, **Stremio**, **WuPlay**, **Jellyfin**, **Wholphin**, and/or **Moonfin** installed on the device - whichever one you plan to pick in Settings. See [Limitations](#limitations) for how the three Jellyfin-server clients (Jellyfin, Wholphin, Moonfin) differ from Nuvio/Stremio/WuPlay - and how Moonfin differs from the other two.

## Installation

TVRelay isn't on Google Play yet - install the APK from this repository's [Releases](../../releases) page.

### Option A: via Downloader

1. On the TV, install the **Downloader** app (by AFTVnews) from Google Play.
2. Open it and enter the code **9525208** in the URL field - or open [aftv.news/9525208](http://aftv.news/9525208) directly in any browser.
3. Downloader fetches the APK and offers to install it right away.
4. If Android TV shows a warning about installing from an unknown source, temporarily allow installation from that source.

### Option B: from your phone, using Send Files to TV

1. On the TV, install **[Send Files to TV](https://play.google.com/store/apps/details?id=com.jstenpal.sendfilestotv)** from Google Play.
2. Open the app on the TV. It will show an address or a QR code to connect from your phone.
3. From your phone's browser, go to that address and select the APK downloaded from [Releases](../../releases).
4. Once the file has transferred, the TV will let you start the installation.
5. If Android TV shows a warning about installing from an unknown source, temporarily allow installation from that source.

### Option C: via ADB

1. Download the APK from [Releases](../../releases).
2. Enable developer options on the TV: **Settings → Device Preferences → About → tap "Build" 7 times**.
3. Enable **USB debugging** or **Network debugging**, depending on the device.
4. From your computer, install the app and enable its accessibility service in one go:
   ```
   adb connect <tv-ip>:5555
   adb install app-release.apk
   adb shell appops set com.hmartinez94.tvrelay ACCESS_RESTRICTED_SETTINGS allow
   adb shell settings put secure enabled_accessibility_services com.hmartinez94.tvrelay/com.hmartinez94.tvrelay.TvRelayAccessibilityService
   adb shell settings put secure accessibility_enabled 1
   ```
   The last three lines turn on the permission that lets TVRelay see launcher clicks at all, bypassing a restriction some Android versions place on sideloaded apps (see [Setup](#setup) below) - safe to run on