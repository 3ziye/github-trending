<p align="center">
  <img src="sce_sys/icon0.png" width="128" alt="ProsperoEden icon">
</p>

<h1 align="center">ProsperoEden</h1>

<p align="center">
  <strong>An unofficial Eden emulator port for PlayStation 5 homebrew</strong>
</p>

**ProsperoEden is an unofficial PlayStation 5 port of [Eden](https://github.com/eden-emulator/mirror)** - an accurate, high-performance emulator. All credit for the emulator core belongs to the Eden project and its contributors. ProsperoEden is not affiliated with or endorsed by the Eden team or Sony.

This is an early alpha. Video, audio, controller input, and saves have been confirmed working. Compatibility and performance will vary between games. The current release is **v1.005.000**. What changed in it, and in every release before, is in the [changelog](docs/CHANGELOG.md#v1005000).

## Source code

The complete ProsperoEden source is in this repository: the PS5 frontend and launcher in `headless/`, and the build and packaging tools in `tools/`. To build it yourself, run `make` on Linux (Ubuntu 26.04; WSL works). It fetches every dependency at its pinned revision and writes the release files to `dist/`; `make help` lists the other targets. See [docs/BUILDING.md](docs/BUILDING.md). A release ZIP built by GitHub Actions can be checked with `gh attestation verify <ZIP> -R blackbearreloaded/ProsperoEden` (GitHub CLI); this covers releases built from now on (after v1.000.090), not earlier ones.

Local-wireless multiplayer through Eden rooms is new in v1.000.110 and experimental. See the
[setup guide and current limitations](docs/MULTIPLAYER.md) and the
[validation status](docs/MULTIPLAYER_IMPLEMENTATION.md); Tailscale forwarding is not yet qualified.

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
- **Resolution and upscaling** - render at 0.5x to 4x of the game's resolution and choose the filter that scales it to your TV (Bilinear, AMD FSR, Bicubic or Nearest) in **Settings > Video**. Textures in a format the PS5's GPU cannot read (ASTC) are kept compressed (as BC3), which takes a quarter of the graphics memory they would need decoded. **ASTC textures** in **Settings > Video**, and in each game's settings, can be set to **Full quality** instead: those textures are then kept decoded, which uses four times the graphics memory for them and can make a game run out of memory above 1x.
- **Output resolution** - the picture is made at 1080p, 1440p or 2160p: **Output resolution** in **Settings > Video**. The menu is drawn at that size too, and the PS5 scales it to your TV.
- **A steadier frame rate in heavy scenes** - some games time their own frames and drop to a lower frame rate (30 to 20, or 60 to 30) as soon as a frame takes a little too long. ProsperoEden lets the game's clock give by up to 15% in those moments, so the game keeps its frame rate and runs a few percent slower instead of losing a third of its frames.
- **120 Hz output** - on a display that shows 120 Hz, games can run on a 120 Hz output: **Refresh rate** in **Settings > Video**, or in one game's settings. A frame that is a little late is then shown 8 ms later instead of 17 ms, and patches for more than 60 FPS need it. The menu stays at 60 Hz.
- **Frame generation** - between two of a game's own pictures ProsperoEden can show one made up from them, so a 30 FPS game looks like 60: **Frame generation** in **Settings > Video**, or in one game's settings. Two methods: **MihawkGen**, which comes with the app, or Lossless Scaling with your own copy of it; see [Frame generation](docs/SETTINGS.md#frame-generation).
- **Post-processing (ReShade FX)** - a look drawn over the game's picture: **Post-processing** in **Settings > Video**, or in one game's settings, with the Vulkan renderer. Six presets come with the app (Anime, Ci