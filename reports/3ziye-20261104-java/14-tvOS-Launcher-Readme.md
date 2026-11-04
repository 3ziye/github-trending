# tvOS Launcher (`v2.1.0`)

> 🇹🇷 **Türkçe dokümantasyon ve kurulum rehberi için:** **[README_TR.md (Türkçe)](README_TR.md)**  
> 📦 **Download Latest APK (`v2.1.0`):** **[GitHub Releases](https://github.com/techgenius1/tvOS-Launcher/releases/latest)**

![tvOS Launcher Header](screenshots_en/Header_EN.jpg)

A fast, lightweight, tvOS 26 & macOS–inspired home screen for Android TV & Google TV — built in pure Java with zero third-party runtime dependencies (**~30 MB private RAM / ~38 MB total PSS, `0.0%` background CPU**). Designed to stay buttery-smooth even on 1 GB RAM TV boxes while bringing a **resizable Liquid Glass Dock (`50%–150%`)**, rotating **Night Scenes**, **Custom Wallpapers (`Custom 1..5`) + Wallpaper Folder Shuffle**, a **Built-In Lock Screen / Idle Screensaver**, an **App Icon Changer & Interactive Icon Editor**, **Automatic GitHub App Updates**, a **built-in PC-free CleanYourTV Debloater (341 TV models + Manual System App Debloater + Stock Launcher Disabler)**, a **Customizable Glass Control Panel (`Quick Settings`) overlay**, a **Recent Apps Switcher**, **multi-tap (`1x / 2x / 3x`) Remote Button Remapping + Send Key Code + Home Button Fix**, and **Dual-Mode Secure Local ADB Setup (Self-Repair & Volume Hold Fix without keeping port 5555 open)** to any Android TV.

---

## 🆕 What's New in `v2.1.0` (Changes Since `v2.0.5`)

- **Dual-Mode ADB Security Architecture & One-Tap ADB Toggle (`Settings → Advanced` & First-Time Setup)**:
  - **Secure Mode (Grant Once & Close ADB — Default & Recommended)**: Grants `WRITE_SECURE_SETTINGS` and `DUMP` once during setup and immediately closes network ADB (`adb_enabled = 0`) so port `5555` is never left open on your LAN. When Secure Mode is selected, the launcher strictly never connects to or probes ADB port `5555` in the background (even if ADB is enabled on the TV), repairing Accessibility (`ServiceRepair`) and running the **Volume Button Hold Fix** 100% in-process.
  - **Persistent ADB Mode (Opt-In with Confirmation Popup)**: Optional mode for users who want network ADB kept open for runtime ADB tools like CleanYourTV. Selecting Persistent Mode while ADB is off prompts to enable USB Debugging and switch automatically; turning ADB off automatically returns to Secure Mode.
  - **One-Tap Turn On / Turn Off ADB Button**: Toggle USB Debugging (`adb_enabled`) on or off directly from `Settings → Advanced` without enabling Wireless Debugging (`adb_wifi_enabled`).
  - **Device Admin Removed & Keep Alive Enabled by Default**: Completely removed `BIND_DEVICE_ADMIN` (screen-off uses Android 9+ `GLOBAL_ACTION_LOCK_SCREEN`) so the launcher never blocks uninstallation, while keeping **Keep Alive** enabled by default (powered by `WRITE_SECURE_SETTINGS` in Secure Mode without touching ADB, or Local ADB in Persistent Mode).
- **Refined First-Time Setup Wizard & Dedicated Default Home Troubleshooting Screen**:
  - **Clear Usage Mode Selection**: Presented the permission setup options clearly as **Usage Modes** (*Mode: Secure Auto Setup & Close ADB*, *Mode: Persistent ADB Setup*, and *Mode: Manual Setup*).
  - **Dedicated "Make tvOS Launcher Default Home" Setup Page**: Moved default home configuration to its own dedicated setup step right after permissions, with sequential **Step 1 – Step 4** troubleshooting options and a **Continue** button (running Step 1 stays on the page so you can proceed to Step 2 or Step 3).
  - **Smart ADB Prompt for Secure Mode Users**: If you selected Secure ADB Mode and tap an ADB-requiring troubleshooting step (such as *Step 2: Disable System Launchers*), a friendly dialog explains that ADB is needed for that step and lets you either **Enable ADB Now** or **Skip This Step** (noting you can change ADB mode in Settings anytime).
- **Universal Volume Button Hold Fix (`Mode 1` & `Mode 2` in `Settings → Button Mapper`)**:
  - Works seamlessly in **both Secure Mode (ADB Off) and Persistent ADB Mode** with two selectable engines:
    - **Mode 1 (Standard — Default)**: Uses `AudioService` + `InputManagerService` (`InputReader` hardware `KeyDowns` state via `DUMP` permission) in Secure Mode and `getevent` in Persistent ADB Mode for smooth volume hold repeat (`320ms` initial delay, `85ms` repeat) and instant key-release stopping (`<= 45ms`) on Android 9–14 Smart TVs without runaway volume.
    - **Mode 2 (HY320 / Projector)**: Enhanced `AudioService` Binder dump watcher (`280ms` repeat delay + IR pulse-burst handling) tailored for Magcubic HY320 and Android 9–12 projectors.
- **Built-In Lock Screen & Idle Timer (`Settings → Control Panel → Ambient Mode`)**:
  - Choose between **Ambient Mode (System Default)** or the new **Built-In Lock Screen** when opening Ambient Mode or after an automatic **Idle Timer (`Off / 5 / 10 / 15 / 30 / 60 min`)**.
  - Includes a dedicated **Lock Screen Settings** sub-menu to pick any **Night Scene, Classic Wallpaper, Custom 1–5, or Folder Shuffle**, configure **Clock Position (`Left / Center / Right`)**, and display the glass clock