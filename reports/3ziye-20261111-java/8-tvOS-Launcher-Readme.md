# tvOS Launcher (`v2.1.5`)

> 🇹🇷 **Türkçe dokümantasyon ve kurulum rehberi için:** **[README_TR.md (Türkçe)](README_TR.md)**  
> 📦 **Download Latest APK (`v2.1.5`):** **[GitHub Releases](https://github.com/techgenius1/tvOS-Launcher/releases/latest)**

![tvOS Launcher Header](screenshots_en/Header_EN.jpg)

A fast, lightweight, tvOS 26 & macOS–inspired home screen for Android TV & Google TV — built in pure Java with zero third-party runtime dependencies (**~30 MB private RAM / ~38 MB total PSS, `0.0%` background CPU**). Designed to stay buttery-smooth even on 1 GB RAM TV boxes while bringing a **resizable Liquid Glass Dock (`50%–150%`)**, rotating **Night Scenes**, **Default Home Dashboard widgets**, **Custom Wallpapers (`Single/Multi, Folder Shuffle & Reddit Wallpapers`)**, a **Built-In Lock Screen / Idle Screensaver**, an **App Icon Changer & Interactive Icon Editor**, **Automatic GitHub App Updates**, a **built-in PC-free CleanYourTV Debloater (341 TV models + Manual System App Debloater + Stock Launcher Disabler)**, a **Customizable Glass Control Panel (`Quick Settings`) overlay with Extended Weather**, a **Recent Apps Switcher**, **multi-tap (`1x / 2x / 3x`) Remote Button Remapping + Send Key Code + Home Button Fix**, a **Universal 3-Mode Volume Button Hold Fix (Standard, HY320 Projector, Onn TV Box)**, **Caffeine Mode**, and **Dual-Mode Secure Local ADB Setup (Self-Repair & Volume Hold Fix without keeping port 5555 open)** to any Android TV.

---

## ✨ Highlights & Features

- **Default Home Dashboard (4 Customizable Widgets)**
  - When no app is focused, or when hovering over apps or non-app elements without Continue Watching items, displays a customizable row of 4 horizontal Liquid Glass widget tiles:
    - 🕌 **Prayer Times**: Daily schedule (Fajr, Sunrise, Dhuhr, Asr, Maghrib, Isha), live countdown to the next prayer, and 10 calculation methods (Diyanet, MWL, ISNA, Egypt, Makkah, Karachi, Tehran, Jafari, Gulf, France).
    - ⚽ **Football Matches**: Today's and upcoming fixtures, live match scores, favorite team tracking, and league schedules.
    - 🎬 **Most Watched (Çok İzlenenler)**: Popular and trending movies and TV series across top streaming platforms powered by JustWatch, synced with your UI language by default with custom multi-country selection.
    - ⛅ **Weather**: Current temperature, condition, location name, and today's forecast.
  - Fully available and configurable on both **Night Scenes** and **Classic Appearance**.
  - Toggle each widget individually and configure whether to show widgets whenever the currently selected app has no Continue Watching content.

- **Dual Appearance Modes (`Night Scenes` & `Classic`)**
  - **Night Scenes**: Layered foreground/background depth scenes (*Night*, *Golden Hour*, *Waterline*, *Fog*, *Rainforest Dawn*) or custom wallpapers with a giant glass clock (*iPhone Duo*, *iPhone Rounded*, *Tall Glass*), personalized greeting, date, live weather, and a macOS-inspired dynamically resizing **Liquid Glass Dock (`50%` to `150%`)** with floating app name callouts.
  - **Classic Appearance**: Clean app grid with an Apple tvOS–styled centered glass dock, squircle app cards, symmetrical edge spacing, and built-in photography or ambient backdrops.
  - **Big Clock for Classic Appearance**: Brings the authentic iOS/tvOS-style big glass clock, greeting, date, and top-right weather shortcut to Classic mode by default (disabling the top mini-clock), with configurable **Clock Alignment (`Left / Center / Right`)**.
  - **Dynamic & Custom Wallpaper Clock Alignment**: Dynamic alignment for default night scenes that adapts per wallpaper, plus independent Left / Center / Right alignment for custom wallpapers. Digits feature authentic Liquid Glass shading matching the dock with adaptive background luminance sampling.

- **Expanded Custom Wallpaper Engine**
  - **Single & Multi-Wallpaper**: Unlimited wallpaper selection from internal storage or USB drives (no 5-wallpaper limit).
  - **Folder Shuffle**: Automatically cycles through all wallpapers in any chosen folder.
  - **Reddit Wallpapers**: Pull high-resolution wallpapers directly from selected subreddits (e.g. `wallpapers`, `EarthPorn`) with customizable auto-change intervals and an instant "Next Wallpaper" skip action.

- **Universal Continue Watching for All Media Apps**
  - Supports all installed media apps (YouTube, SmartTube, Netflix, Prime Video, Disney+, Apple TV+, Tivimate, HBO Max, Stremio, Nuvio, etc.) using Android TV `TvContract` EPG / Watch Next content provider, `MediaSessionManager` active session tracking, and notification listeners.
  - **Dock-Linked Focused App Filtering**: The shelf only displays content for the media app currently focused on the dock.
  - **Integrated Stremio & Nuvio Dock Popups**: Popups directly above dock tiles with local caching, QR code sign-in, and multi-profile switching.
  - **Instant App Switching (No Re-Animation)**: Switching between two apps that both have Continue Watching con