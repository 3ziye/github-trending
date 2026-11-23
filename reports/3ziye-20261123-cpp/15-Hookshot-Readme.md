<h1 align="center">
  <br>
  <a>
  <img src="assets/hookshot.png" alt="Hookshot" width="200">
</a>

  <br>
  <b>Hookshot</b>
  <br>
</h1>

<h4 align="center">The Legend of Zelda: Ocarina of Time (Nintendo Switch 2) running natively on Windows & Linux, with no emulator.
</h4>


<p align="center">
  <a href="#features">Features</a> |
  <a href="#project-status">Status</a> |
  <a href="#install-and-play">Install and play</a> |
  <a href="#in-game-menu">In-game menu</a> |
  <a href="#mods">Mods</a> |
  <a href="#save-editor">Save editor</a> |
  <a href="#if-something-goes-wrong">Problems</a> |
  <a href="#build-from-source">Build from source</a> |
  <a href="#how-it-works">How it works</a> |
  <a href="#want-to-help">Want to help?</a> |
  <a href="#credits">Credits</a> |
  <a href="#license">License</a>
</p>

[Documentation](docs/README.md) · [Common issues and answers](docs/common-issues.md) · [Report a bug](https://git.notrexed.dev/Hookshot/Hookshot/issues/new/choose)

Hookshot is a static recompilation. The game's code is translated to C and compiled into a Windows or Linux program,
the console's system software is reimplemented, and the Switch 2 graphics are rebuilt on Vulkan. All of this happens
**on your PC, from your own copy of the game**.
<br>

> [!WARNING]
> Some users report the file in releases to be a Trojan - it is not. Feel free to run it through any antivirus software


Discord: https://discord.gg/rexed
<br>

> [!IMPORTANT]
> This repository **does not contain the game, keys or an executable**, and it does not explain how to get them. You
> need your own copy. Everything the build creates (`hookshot.exe`, the generated code, the shader caches and your
> saves) comes from your game and stays on your PC. Never share those files.

## Features

**Runs natively**
- The game's own code, translated to C and compiled for your PC: no emulator. Windows (Hookshot Builder, one setup
  file) and Linux and Steam Deck (one AppImage).
- High frame rates (60, 90, 120, 144, 165, 240 or uncapped, and 30), with the game kept at real-time speed.
- Any screen shape: ultrawide, 16:10 and 4:3, with the HUD at the screen's edges or in the middle 16:9.

**Graphics**
- Upscaling and anti-aliasing: NVIDIA DLSS and DLAA, AMD FSR 4 and FSR 3.1, Intel XeSS, or none.
- Frame generation: DLSS Frame Generation (up to what your card allows) and FSR 3.1 frame generation on every GPU, with
  the HUD kept still.
- Render and output resolution, view distance (foliage, detail, grass, shadows), shadow resolution, anisotropic
  filtering, HDR, CRT monitor and TV filters, and a fullscreen monitor choice.
- An FPS counter with a frame-time graph and a details page; <kbd>F12</kbd> saves a screenshot.

**Mods and saves**
- [**Mods**](#mods): RomFS mods, ExeFS code patches and Atmosphère cheats, in the emulators' folder layout. Turn them
  on and off and put them in order on the in-game **Mods** tab or the Builder's **Mods + Editor** page. Mods that each
  grow files load together.
- [**Save editor**](#save-editor): the Builder's **Mods + Editor** page edits your save: stats, inventory, story
  progress and every save entry, with a backup each time it saves.
- In-game tools on the **Debug** tab: the inventory editor, rupees, teleport, travel, switch age, free camera, no-clip
  flight, set time and more.
- Saves are backed up outside the game folder at every start and as you save, and come back if they go missing.

**Controls**
- Controllers and keyboard and mouse, with every control remappable (the ocarina notes too) and mouse look.
- Motion aiming with a controller's gyroscope, an item wheel, and item cycling.
- One Vibration setting for every controller: a DualSense on a USB cable plays the game's fine haptics through its voice
  coils, and Switch controllers get their own HD rumble.
- **NFC**: amiibo from your own dumps.

**Everything else**
- An in-game menu (<kbd>F1</kbd>) drawn in the game's own style, in several languages.
- Audio output device choice, and a microphone test with level and gain for the ocarina.
- Crash reports from the game's own window, with your graphics card filled in.

## Project status

Experimental. Players have reported on many PCs, from Kokiri Forest to the dungeons: the table says what works and
what does not yet. Open problems are collected in tracking issues, linked below.

| What | Status |
|---|---|
| Kokiri Forest: reaching gameplay and walking around | ✅ Works |
| Sound, controller, keyboard and saves | ✅ Works |
| In-game menu, frame generation and upscaling | ✅ Works |
| Flicker (the picture flashing too bright while moving) | ✅ Fixed in v2.0.2 (#645) |
| Ground fog vanishing when looking down | ✅ Fixed in v2.0.2 (#638) |
| Models with missing pieces (doors, fences, parts of trees) | ✅ Fixed where tested, more play needed |
| Stutter when entering new areas | ⚠️ Still happens the first time you visit a place. The next visits are smooth |
| Performance | ⚠️ Depends on the PC: some reach a steady 60 fps,