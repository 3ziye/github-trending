
<div align="right">
  <strong><a href="README_CN.md">🇨🇳 简体中文 (Chinese)</a></strong>
</div>

<p align="center">
  <!-- Replace with your actual app icon path or image URL -->
  <img src="doc/images/icon.png" width="128" alt="App Icon">
</p>

<h1 align="center">Slay the Spire 2 Android Launcher</h1>

<p align="center">
  An unofficial, open-source mobile compatibility layer and launcher environment for <i>Slay the Spire 2</i>, based on the Godot/Mono runtime.
</p>

<p align="center">
  <a href="https://github.com/ModinMobileSTS/Sts2MobileLauncher/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License">
  </a>
  <img src="https://img.shields.io/badge/Platform-Android_7.0+-brightgreen.svg" alt="Platform">
  <img src="https://img.shields.io/badge/Godot-4.5_Mono-478CBF.svg" alt="Godot">
</p>

## Screenshots

<p align="center">
  <!-- Please replace the src with actual screenshot paths -->
  <img src="doc/images/screenshot_1.jpg" width="24%" alt="Home Dashboard">
  <img src="doc/images/screenshot_2.jpg" width="24%" alt="Steam Download">
  <img src="doc/images/screenshot_3.jpg" width="24%" alt="MOD Management">
  <img src="doc/images/screenshot_4.jpg" width="24%" alt="In-game Footage">
</p>

## About the Project

This project is an experimental, unofficial Android port and launcher framework for *Slay the Spire 2*. It **DOES NOT** contain any base game files. Instead, it provides an Android shell that allows players to import and run their legally owned PC game files on mobile devices, featuring support for Mod loading, local save snapshots, Steam Cloud and WebDAV save synchronization, and launcher update checks from the About page. When an update is found, the launcher can open either the GitHub release page or the Bilibili dynamic feed.

**The core architecture consists of three layers:**
1. **Android Launcher Shell (`android/`):** Handles game data importing, Steam login and game downloading, local save snapshots, Steam Cloud/WebDAV save syncing, and local file/MOD management. Once everything is ready, it boots up the Godot game process.
2. **Android Compatibility Pack (`port-mod/` submodule):** Acts as a low-level hook (based on Harmony), loaded at the very beginning of the game boot process. It intercepts and fixes various PC-to-Android incompatibilities (e.g., input adaptation, path redirection, PC-specific shader replacement, Mod loader bridging).
3. **Base Game (Provided by User):** Supplied by the user either by importing the PC version's `SlayTheSpire2.zip` or by legally downloading it via the SteamPipe API after logging into their Steam account within the app.

---

## Legal Disclaimer

- **Unofficial Project:** This is an open-source technical research project created by the player community. It is not affiliated with Mega Crit, *Slay the Spire 2*, or the Godot Engine, nor does it represent their views.
- **No Game Assets Provided:** This repository **ABSOLUTELY DOES NOT** contain or distribute any copyrighted commercial game assets (including but not limited to audio, images, PCK files, core logic DLLs, etc.).
- **Legal Use:** Please comply with relevant software licenses, platform rules, and local laws. You must **legally own** a PC copy of *Slay the Spire 2* to use this tool to run the game on your own device.
- **No Pirated APK Distribution:** Do not use standalone APKs bundled with commercial game assets for public release or commercial monetization.

---

## Credits & References

The creation of this project relies heavily on the explorations of the open-source community. Special thanks to the following projects for their inspiration and code references:

- **[StS2-Launcher_Mod_Manager](https://github.com/iunius612/StS2-Launcher_Mod_Manager)**
  Provided underlying concepts for stripping the Godot/Mono runtime, Android compatibility patch load orders, and design references for some build scripts.
- **[SlayTheAmethystModded](https://github.com/ModinMobileSTS/SlayTheAmethystModded)**
  An unofficial mobile launcher for STS1. The reverse-engineered integration and source code for `steam-protocol`, `steam-content` (SteamPipe game downloads), and Steam Cloud saves in this project are primarily ported/adapted from it.
- **[STS2-RitsuLib](https://github.com/BAKAOLC/STS2-RitsuLib) / [BaseLib-StS2](https://github.com/Alchyr/BaseLib-StS2)**
  Served as vital test baseline reference libraries for troubleshooting Android MOD compatibility.
- **[Google Material Symbols](https://fonts.google.com/icons)**
  Provides the official rounded icon outlines used by the launcher UI, generated into Android vector drawables from the bundled font.

*(For detailed third-party open-source licenses, please see [THIRD_PARTY_LICENSES.md](THIRD_PARTY_LICENSES.md))*

---

## Core Security Notes

For the safety of your device and accounts, please pay strict attention to the following when using and compiling this app:

1. **ADB & `Debuggable` Risks:**
   The current default release build