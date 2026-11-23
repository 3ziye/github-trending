# Need for Speed: Most Wanted for Android
**English** | [Bahasa Indonesia](README.id.md)

An unofficial native Android port of the original Xbox version of *Need for Speed: Most Wanted* (Black Edition), with touch controls, controller and keyboard support and extended graphics options.

The game's x86 code is statically recompiled ahead of time to C++ with [XboxXBE-Recomp](https://github.com/TGP482/XboxXBE-Recomp), then built for arm64. Drawing goes through Vulkan, and windowing, input and audio through SDL3. No emulator is involved. The Android host (Vulkan renderer, DirectSound, touch controls, settings panel) comes from [Black-Android](https://github.com/RanggaCasper/Black-Android), as [ShaolinMonks-Android](https://github.com/RanggaCasper/ShaolinMonks-Android) carries it.

> [!NOTE]
> This project does not include any game assets. You must provide the files from your own legally acquired copy of the game to install or build.

> [!WARNING]
> Work in progress. See [Status](#status).

## Gameplay

<p align="center">
  <a href="https://youtu.be/x5bczwTuyhw">
    <img src="https://img.youtube.com/vi/0ILO1_gulrg/maxresdefault.jpg" alt="Most Wanted Android gameplay" width="720">
  </a>
  <br>
  <sub>▶ Gameplay on Xiaomi Pad 7</sub>
</p>

## Installation
1. Install the APK.
2. Open **Most Wanted** and allow **all files access** when it asks (on Android 10, the **storage** permission). It is required: the game doesn't start without it.
3. Copy the game into `/storage/emulated/0/MostWanted`, or into a `MostWanted` folder at the top of your SD card: either the disc image (`.iso`) or `default.xbe` with the disc's `NFS` folder beside it. The app creates the folder on the phone's storage once access is allowed, and starts the game as soon as it finds the files.

Saves go in `/storage/emulated/0/MostWanted/hdd` and logs in `/storage/emulated/0/MostWanted/logs`, so they stay if the app is uninstalled. Each start copies a changed save to `/storage/emulated/0/MostWanted/backups/saves` (the last ten are kept), and a save whose writing was cut short (the app closed while the game was saving) is put back from its last good copy. Updating from a version that kept the saves in `Android/data/com.racas.mostwanted/files/hdd` copies them there on the first start; the old copy is left as it was. Settings (`mostwanted.toml`, `android.toml`, `layout.toml`) and the shader cache stay in `Android/data/com.racas.mostwanted/files`.

The supported disc is the USA Black Edition (`default.xbe` SHA-1 `f636a16af04171089f879a4bed646e185c734233`).

## Features
The settings panel opens from the gear at the top left of the screen (or F10 on a keyboard). Android's back button is the controller's Start, which pauses the game.

### Graphics
- **Render Resolution**: 20% to 200% of the screen's height, instead of the original 640x480.
- **V-Sync**, **Max Frame Rate** (unlimited, the display's refresh rate or a custom cap) and an **FPS Counter**.
- **Anisotropic Filtering**, **Anti-Aliasing** (FXAA, SSAA 2x) and **Screen Filters**.

### Touch Controls
A full Xbox controller on the screen:
- The left side of the screen is the **left stick**, wherever your thumb comes down. A drag on the right side of the screen is the **right stick**.
- **A**, **B**, **X**, **Y** in the controller's diamond and colours, **Black** and **White**, the **triggers** (RT gas, LT brake); the face buttons show the game's own controls (A E-brake, B nitrous, X speedbreaker, Y look back), **Start**, **Back** and a **D-pad**.
- **Controls Layout**: *Default* (triggers at the top corners) or *Low Triggers*, with the controls' opacity and overall size.
- **Edit Controls Position**: drag each control where you want it. To resize one, select it and tap **−** or **+**, or pinch it with a second finger.

### Other Input
- **Controller**: any controller SDL3 supports, with rumble. The touch controls hide while a controller is in use.
- **Keyboard**, with every controller button and both sticks rebindable.

### General
- **Language**: English, French, German, Italian or Spanish. The game takes it from the console's language setting, which this sets; it applies at the next start. Indonesian translates the settings panel and plays the game in English.
- **Audio Output**: automatic, mono, stereo or 5.1 surround.
- **Background Pause**: the game and its sound pause while the app is in the background.

### Add-on Cars (Mods Loader)
**Most Wanted Mods Loader** has an icon of its own beside the game's. It puts cars made for the PC version into the game, converting them to the Xbox game's format on the phone:
1. Tap **Get cars on NFSAddons**: the site opens in your browser. Download a Most Wanted car (ZIP, 7z or RAR).
2. Tap **Install from file** and choose it, or open or share the downloaded file with Mods Loader. Packs with several cars install every car in them.
3. Tap **Play**: the cars are in the car select and your garage.

Installed cars are listed in Mods Loader, each with a **Remove** but