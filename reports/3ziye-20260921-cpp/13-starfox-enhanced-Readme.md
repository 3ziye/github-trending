# Star Fox Enhanced

A native C++/SDL3 port of [UltraStarFox](https://github.com/Sunlitspace542/ultrastarfox),
with **Original Star Fox** and **Star Fox EX** experiences, high-frame-rate
presentation, widescreen support, and optional visual enhancements.

**[Download 0.0.6.7](https://github.com/kandowontu/starfox-enhanced/releases/tag/v0.0.6.7)** ·
[Changelog](https://github.com/kandowontu/starfox-enhanced/blob/main/docs/RELEASE-0.0.6.7.md) ·
[Settings and controls](https://github.com/kandowontu/starfox-enhanced/blob/main/docs/SETTINGS-AND-CONTROLS.md) ·
[Build guide](https://github.com/kandowontu/starfox-enhanced/blob/main/docs/BUILDING.md) ·
[Report a bug](https://github.com/kandowontu/starfox-enhanced/issues)

> This is an alpha release, not a cycle-accurate SNES emulator. A supported,
> unmodified retail ROM supplied by you is required. No retail ROM is included.

## Get started

1. Download the package for your platform. Desktop users should extract it
   into a writable folder before launching; no source build is necessary.
2. Launch the game. On desktop, place your supported `.sfc`/`.smc` ROM beside
   the executable, or set `STARFOX_RETAIL_ROM` to its path. Mobile apps provide
   a first-launch file picker.
3. The game validates your ROM and creates `Starfox-Assets.BIN` locally.
   Keep that companion with the application; it may need rebuilding after
   updates to the embedded assets.
4. Choose **Original** or **Star Fox EX**, adjust your options, then select
   **Start Game** from the main menu.

For devices needing prepared assets, the release includes a standalone Windows
[asset builder](https://github.com/kandowontu/starfox-enhanced/blob/main/platform/mobile/ASSET_BUILDER.md). It accepts the same ROMs;
mobile users can also select a ROM directly.

### Supported ROMs

- Star Fox Japan: 1.0 / 1.1
- Star Fox USA: 1.0 / 1.1 / 1.2
- Starwing Europe: 1.0 / 1.1
- Starwing Germany: 1.0

A 512-byte copier header is accepted. Known revisions are checksum-verified
and canonicalized before the source-built patches are applied. Hacks, betas,
competition cartridges, Star Fox 2 and unknown revisions are not supported.

## Platforms

| Package | Notes |
|---|---|
| Windows x64 / x86 | Extract and run `starfox_pc.exe`. |
| Linux x64 | Native SDL3 runtime. |
| macOS universal | Unsigned application for Intel and Apple Silicon. |
| iOS arm64 | Unsigned device bundle; [signing/sideloading instructions](https://github.com/kandowontu/starfox-enhanced/blob/main/platform/apple/IOS_INSTALL.md). |
| Android arm64 | Installable development APK; see the upgrade notice below. |
| Nintendo Switch | Homebrew NRO; [setup and optional forwarder](https://github.com/kandowontu/starfox-enhanced/blob/main/platform/switch/README.md). |
| PS Vita | Homebrew VPK; [setup](https://github.com/kandowontu/starfox-enhanced/blob/main/platform/vita/README.md). |
| Xbox UWP x64 | Developer Mode required; [setup](https://github.com/kandowontu/starfox-enhanced/blob/main/platform/uwp/README.md). |

Build success does not guarantee identical behavior on every device.
See the [release notes](https://github.com/kandowontu/starfox-enhanced/blob/main/docs/RELEASE-0.0.6.7.md) for verification limits.

**Android upgrades:** 0.0.6 uses a permanent signing key. Older APKs used
temporary keys, so upgrading from those builds requires a one-time reinstall.
**Back up saves and settings before uninstalling.** Later public builds will
retain the permanent signing certificate.

## Features and settings

- **Original and EX:** original routes and frontend flow, plus EX's shipped
  campaigns, native options and mechanics.
- **Smooth presentation:** 20–480 FPS choices, defaulting to 60. Game pace is
  independent of render FPS; Original Speed preserves source-style slowdown.
- **Display:** 4:3, 16:10, 16:9, 21:9 and 32:9; GPU or software presentation.
- **Languages:** English, English (Europe), Japanese, German, French and Spanish, including menus
  and dialogue. EX translations include authored additions.
- **2D Options:** artwork filtering, 2D Bloom, World Effects and their intensity.
  The artwork filter also covers textures on 3D polygons.
- **3D Options:** anti-aliasing, VSync, 1–4× Render Upscale, 3D Bloom, 3D Smoothing,
  Enhanced Lighting, HDR Effect, Ray Tracing (hardware DXR shadows, default Off),
  Chromatic Aberration, Model Effects
  and Model Effect Intensity. HDR Effect is brightness/contrast
  processing, **not HDR display output**.
  Ray Tracing replaces original shadows rather than drawing a second set;
  there is no separate Enhanced Shadows toggle.
- **Preview:** a fixed reference scene shows graphics changes live. Hold **Tab**
  to hide the menu temporarily. Preview defaults off each launch.
- **Customization:** draggable HUD layouts, controller/keyboard remapping,
  crosshair colors, separate music/SFX volumes, rumble and optional God Mode.

Model and world effects are independent; CEL-DRAWN is model-only and BLUEPRINT
is world-only. Most vis