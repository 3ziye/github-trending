# tvOS Launcher (`v2.2.0`)

> 🇹🇷 **Türkçe dokümantasyon ve kurulum rehberi için:** **[README_TR.md (Türkçe)](README_TR.md)**  
> 📦 **Download Latest APK (`v2.2.0`):** **[GitHub Releases](https://github.com/techgenius1/tvOS-Launcher/releases/latest)**

![tvOS Launcher Header](screenshots_en/Header_EN.jpg)

A fast, lightweight, tvOS 26 & macOS–inspired home screen for Android TV & Google TV — built in pure Java with zero third-party runtime dependencies (**~5.7 MB APK, ~30 MB private RAM / ~38 MB total PSS, `0.0%` background CPU**). Designed to stay buttery-smooth even on 1 GB RAM TV boxes while bringing a **resizable Multi-Row Liquid Glass Dock (`50%–150%`, `1–3 rows`)**, a **macOS 26–inspired Applications Popup**, rotating **Night Scenes** with **Big Glass Clock or Small Header Clock**, **7 Interactive Home Dashboard Widgets**, **Custom Wallpapers (`Single/Multi, Folder Shuffle & Reddit Wallpapers`)**, a **Built-In Lock Screen / Idle Screensaver**, an **App Icon Changer & Interactive Icon Editor**, **Automatic GitHub App Updates**, a **built-in PC-free CleanYourTV Debloater (On-Demand GitHub Profile Downloader + Manual System App Debloater + Stock Launcher Disabler)**, a **Customizable Glass Control Panel (`Quick Settings`) overlay with Extended Weather**, an **Input Manager (Hide & Rename TV Inputs)**, a **Recent Apps Switcher**, **multi-tap (`1x / 2x / 3x`) Remote Button Remapping with ScanCode Support + Home Button Fix**, a **Universal 3-Mode Volume Button Hold Fix (Standard, HY320 Projector, Onn TV Box)**, **Apple TV UI Sound Effects**, **Caffeine Mode**, and **Dual-Mode Secure Local ADB Setup (with Dynamic Port Discovery)** to any Android TV.

---

## ✨ Highlights & Features

- **Default Home Dashboard (7 Interactive & Customizable Widgets)**
  - When no app is focused, or when hovering over apps or non-app elements without Continue Watching items, displays a horizontally scrollable row of 7 Liquid Glass widget tiles (all enabled by default, with **Hold OK** on any widget to **Move** or **Disable** directly from the Home Screen):
    - 🕌 **Prayer Times**: Daily schedule (Fajr, Sunrise, Dhuhr, Asr, Maghrib, Isha), live countdown to the next prayer, and 10 calculation methods (Diyanet, MWL, ISNA, Egypt, Makkah, Karachi, Tehran, Jafari, Gulf, France).
    - ⚽ **Interactive Football Matches**: Upcoming and live fixtures across all leagues and competitions (Champions League, Europa League, Premier League, LaLiga, Serie A, Bundesliga, Ligue 1, Süper Lig, etc.) involving your favorite teams, dual team logos, live in-play scores, and D-Pad Left/Right fixture browsing.
    - 🎬 **Most Watched (Çok İzlenenler)**: Popular and trending movies and TV series across top streaming platforms powered by JustWatch, synced with your UI language by default with custom multi-country selection.
    - ⛅ **Weather**: Current temperature, condition, location name, and today's forecast.
    - 🏏 **Live Cricket Scores**: Real-time international and league cricket match scores and status updates.
    - 📰 **Live News**: Curated breaking headlines and top news stories.
    - 🍿 **Top Movies & Series**: Highest-rated trending movies and series recommendations.
  - Fully available and configurable on both **Night Scenes** and **Classic Appearance**.

- **Dual Appearance Modes (`Night Scenes` & `Classic`) + Multi-Row Dock**
  - **Night Scenes**: Layered foreground/background depth scenes (*Night*, *Golden Hour*, *Waterline*, *Fog*, *Rainforest Dawn*) or custom wallpapers with a giant glass clock (*iPhone Duo*, *iPhone Rounded*, *Tall Glass*) or an optional **Small Clock** in the top-left header, personalized greeting, date, live weather, and a macOS-inspired dynamically resizing **Liquid Glass Dock (`50%` to `150%`, configurable `1 to 3 rows`)** with supersampled anti-aliased squircle icons, adaptive white/black focus rings, and always-on-top floating app name callouts.
  - **macOS 26 Applications Popup (`Other Apps`)**: Dedicated frosted-glass Applications modal with a live search bar and a 5-column scrollable grid. Moving apps to *Other Apps* shrinks the main dock cleanly without pulling apps back out.
  - **Classic Appearance**: Clean app grid with an Apple tvOS–styled centered glass dock, squircle app cards, symmetrical edge spacing, and built-in photography or ambient backdrops.
  - **Big Clock for Classic Appearance**: Brings the authentic iOS/tvOS-style big glass clock, greeting, date, and top-right weather shortcut to Classic mode by default (disabling the top mini-clock), with configurable **Clock Alignment (`Left / Center / Right`)**.
  - **Dynamic & Custom Wallpaper Clock Alignment**: Dynamic alignment for default night scenes that adapts per wallpaper, plus independent Left / Center / Right alignment for custom wallpapers.

- **Expanded Custom Wallpaper Engine (`1–60 Min Intervals`)**
  - **Single & Multi-Wallpaper**: Unlimited wallpaper selection from internal storage or USB drives.
  - **Folder Shuffle**: Automatically cycle