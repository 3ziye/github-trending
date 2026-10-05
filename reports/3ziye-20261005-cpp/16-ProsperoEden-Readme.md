<p align="center">
  <img src="sce_sys/icon0.png" width="128" alt="ProsperoEden icon">
</p>

<h1 align="center">ProsperoEden</h1>

<p align="center">
  <strong>An unofficial Eden emulator port for PlayStation 5 homebrew</strong>
</p>

**ProsperoEden is an unofficial PlayStation 5 port of [Eden](https://github.com/eden-emulator/mirror)** - an accurate, high-performance emulator. All credit for the emulator core belongs to the Eden project and its contributors. ProsperoEden is not affiliated with or endorsed by the Eden team or Sony.

This is an early alpha. Video, audio, controller input, and saves have been confirmed working. Compatibility and performance will vary between games. The current release is **v1.000.070**.

> [!WARNING]
> **ProsperoEden includes an exact-title one-shot helper built from upstream
> [PS5-Lapy-JB-Daemon](https://github.com/mpereiraesaa/PS5-Lapy-JB-Daemon).** The PS5 jailbreak
> environment must provide a local ELF loader on TCP port 9021. If a resident Lapy service is
> already running, ProsperoEden gives it the first bounded opportunity; otherwise it sends the
> packaged helper over that local connection. No separate Lapy payload is required for normal use.
> The packaged helper's corrected donor lifecycle passed five automated launch/elevate/close cycles
> on both firmware 6.02 and 12.70. Other supported firmware remains experimental and should be
> tested cautiously; the helper also refuses unknown runtime layouts instead of guessing.

## Source code

The complete ProsperoEden source is in this repository: the PS5 frontend and launcher in `headless/`, and the build and packaging tools in `tools/`. To build it yourself, run `make` on Linux (Ubuntu 26.04; WSL works). It fetches every dependency at its pinned revision and writes the release files to `dist/`; `make help` lists the other targets. See [docs/BUILDING.md](docs/BUILDING.md).

## Project foundation

> [!IMPORTANT]
> **Built on the [PS5 Native App Boilerplate](https://github.com/blackbearreloaded/ps5-native-app-boilerplate), the same native foundation used by ProsperoLight.**
> It provides the native PS5 application structure, runtime, packaging, and homebrew deployment foundation.

> [!IMPORTANT]
> **Graphics are powered by [ps5-opengl](https://github.com/blackbearreloaded/ps5-opengl).**
> This OpenGL implementation provides the native PS5 rendering layer used by the Eden graphics backend.

> [!IMPORTANT]
> **Vulkan is powered by Mihawk's [PS5 Mesa](https://github.com/mihawk-99/PS5_Mesa) and [PS5 Vulkan](https://github.com/mihawk-99/PS5_Vulkan).**
> Mihawk's Mesa/RADV driver for the PS5 runs ProsperoEden's Vulkan renderer. Many thanks to Mihawk for this work and for [all of the PS5 projects](https://github.com/mihawk-99) behind it.

> [!IMPORTANT]
> **Thanks to [ps5-vulkan](https://github.com/mpereiraesaa/ps5-vulkan) by mpereiraesaa**, an experimental Vulkan graphics and compute API for native PS5 homebrew.

## Features

- **Vulkan renderer (recommended)** - the default backend, running on Mihawk's PS5 Mesa (RADV) driver.
- **OpenGL renderer** - still available through ps5-opengl. Switch between them in **Settings > Video**.
- **Resolution and upscaling** - render at 0.5x to 4x of the game's resolution and choose the filter that scales it to your TV (Bilinear, AMD FSR, Bicubic or Nearest) in **Settings > Video**.
- **Output resolution** - the picture is made at 1080p, 1440p or 2160p: **Output resolution** in **Settings > Video**. The menu is drawn at that size too, and the PS5 scales it to your TV.
- **120 Hz output** - on a display that shows 120 Hz, games can run on a 120 Hz output: **Refresh rate** in **Settings > Video**, or in one game's settings. A frame that is a little late is then shown 8 ms later instead of 17 ms, and patches for more than 60 FPS need it. The menu stays at 60 Hz.
- **Game files anywhere** - keys, firmware, and games can live in any folder the PS5 can read: internal storage, an M.2 or external drive, or a USB device.
- **Folder browser** - pick the game files folder in **Settings > Game files**. It shows how many keys, firmware files, and games each folder holds. Hold L1/R1 to page quickly.
- **Library** - game covers, **Continue Playing**, and **Recently Played**, which keep working after you move your files.
- **Launcher** - an animated interface drawn with OpenGL, with sound effects (their level is in **Settings > Audio**) and a loading screen while a game starts. The home screen shows which controllers are connected.
- **Profiles** - everyone who plays has their own save data, settings and recently played games: **Settings > Profiles**; see [Profiles](#profiles).
- **Settings per game** - a game can differ from Settings in its video, performance, audio, controls and language, and has its own Handheld / Docked mode (Triangle in the Library); see [Settings per game](#settings-per-game).
- **Button mapping** - choose which DualSense button presses each of the game's buttons, for every controller