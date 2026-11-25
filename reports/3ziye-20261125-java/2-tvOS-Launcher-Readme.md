# tvOS Launcher (`v2.2.5`)

> 🇹🇷 **Türkçe dokümantasyon ve kurulum rehberi için:** **[README_TR.md (Türkçe)](README_TR.md)**  
> 📦 **Download Latest APK (`v2.2.5`):** **[GitHub Releases](https://github.com/techgenius1/tvOS-Launcher/releases/latest)**

![tvOS Launcher Header](screenshots_en/Header_EN.jpg)

A fast, lightweight, tvOS 26 & macOS–inspired home screen for Android TV & Google TV — built in pure Java with zero third-party runtime dependencies (**~5.7 MB APK, `0.0%` background CPU, baked Liquid Glass rendering with 60 FPS navigation**). Designed to stay buttery-smooth from **Android 6.0 (API 23)** to **Android 14+** even on 1 GB RAM TV boxes while bringing a **resizable Multi-Row Liquid Glass Dock (`50%–150%`, `1–3 rows`)**, a **macOS 26–inspired Applications Popup**, a **Native Liquid Glass Universal Search Modal with a Home Screen Search Shortcut**, rotating **Night Scenes** with **Custom Foreground Depth Cutouts** and **Big Glass Clock or Small Header Clock**, **7 Interactive Home Dashboard Widgets** (with **Prayer Times Country/City Selector + Weather Sync** and **Live News Country Selector**), **Custom Wallpapers (`Single/Multi, Folder Shuffle & Reddit Wallpapers`)**, a **Built-In Lock Screen / Idle Screensaver**, an **App Icon Changer & Interactive Icon Editor**, **Automatic GitHub App Updates**, a **built-in PC-free CleanYourTV Debloater (On-Demand GitHub Profile Downloader + Manual System App Debloater + Stock Launcher Disabler)**, a **Customizable Glass Control Panel (`Quick Settings`) overlay with Extended Weather & Native Power Menu**, an **Input Manager (Hide & Rename TV Inputs)**, a **Recent Apps Switcher**, **multi-tap (`1x / 2x / 3x`) Remote Button Remapping with ScanCode Support + Direct-Boot Home Button Fix**, a **Universal 3-Mode Volume Button Hold Fix (Standard, HY320 Projector, Onn TV Box)**, **Apple TV UI Sound Effects**, **Caffeine Mode**, and **Dual-Mode Secure Local ADB Setup (with Dynamic Port Discovery)** to any Android TV.

---

## ✨ Highlights & Features

- **Native Liquid Glass Universal Search & Home Screen Search Shortcut**
  - Redesigned **Search** in a centered macOS 26–style Liquid Glass modal matching the *Other Apps* UI, complete with voice dictation and keyboard support.
  - Filters **Movies & TV** results to your actually installed streaming apps and active region, plus **Search in Apps** quick launchers and **In-App Results** from installed TV apps' search providers.
  - Toggleable **Search shortcut** button next to the Weather & Control Panel buttons on the Home Screen (**Settings → Home Dashboard / Quick & Home**).

- **Default Home Dashboard (7 Interactive & Customizable Widgets)**
  - Displays a horizontally scrollable row of 7 Liquid Glass widget tiles with native Liquid Glass detail popups (all enabled by default, with **Hold OK** on any widget to **Move** or **Disable** directly from the Home Screen, and zero-flash Home button handling):
    - 🕌 **Prayer Times**: Daily schedule (Fajr, Sunrise, Dhuhr, Asr, Maghrib, Isha), live countdown to the next prayer, 10 calculation methods, and a **Country/City selector** (worldwide search, 20 popular cities, or automatic **Sync with Weather location** configured during Initial Setup or Settings).
    - ⚽ **Interactive Football Matches**: Upcoming and live fixtures across all leagues and competitions (Champions League, Europa League, Premier League, LaLiga, Serie A, Bundesliga, Ligue 1, Süper Lig, etc.) involving your favorite teams, dual team logos, live in-play scores, and D-Pad Left/Right fixture browsing.
    - 🎬 **Most Watched (Çok İzlenenler)**: Popular and trending movies and TV series across top streaming platforms powered by JustWatch, synced with your UI language by default with custom multi-country selection.
    - ⛅ **Weather**: Current temperature, condition, location name, and today's & tomorrow's forecast.
    - 🏏 **Live Cricket Scores**: Real-time international and league cricket match scores and status updates.
    - 📰 **Live News**: Curated breaking headlines and top news stories with a **Country selector** (auto-synced with your UI language by default).
    - 🍿 **Top Movies & Series**: Highest-rated trending movies and series recommendations.
  - Fully available and configurable on both **Night Scenes** and **Classic Appearance**.

- **Dual Appearance Modes (`Night Scenes` & `Classic`) + Multi-Row Dock**
  - **Night Scenes**: Layered foreground/background depth scenes (*Night*, *Golden Hour*, *Waterline*, *Fog*, *Rainforest Dawn*) or custom wallpapers (including **Custom Foreground PNG Depth Cutouts** so the giant glass clock sits behind your custom foreground subject) with a giant glass clock (*iPhone Duo*, *iPhone Rounded*, *Tall Glass*) or an optional **Small Clock** in the top-left header, personalized greeting, date, live weather, background-threaded scene crossfades, and a macOS-inspired dynamically resizing **Liquid Glass Dock (`50%` to `150%`, configurable `1 to 3 rows`)** with supersample