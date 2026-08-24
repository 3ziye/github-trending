# MAKO - Frame Generation on SteamOS/Linux

<p align="center">
  <img src="plugin/assets/mako-logo.webp" width="256" alt="MAKO logo" />
</p>

<p align="center">
  <a href="https://github.com/eugeniosegala/MAKO/actions/workflows/tests.yml"><img src="https://img.shields.io/github/actions/workflow/status/eugeniosegala/MAKO/tests.yml?branch=main&amp;style=flat-square&amp;label=tests" alt="Tests status" /></a>
  <a href="https://github.com/eugeniosegala/MAKO/releases/latest"><img src="https://img.shields.io/github/v/release/eugeniosegala/MAKO?filter=plugin-%2A&amp;display_name=tag&amp;sort=semver&amp;style=flat-square&amp;label=Decky&amp;color=1d4ed8" alt="Latest MAKO Decky release" /></a>
  <a href="https://github.com/eugeniosegala/MAKO/releases?q=render-v"><img src="https://img.shields.io/github/v/release/eugeniosegala/MAKO?filter=render-%2A&amp;display_name=tag&amp;sort=semver&amp;style=flat-square&amp;label=Renderer&amp;color=1d4ed8" alt="Latest MAKO Renderer release" /></a>
  <a href="LICENSE.md"><img src="https://img.shields.io/badge/license-GPL--3.0--or--later-0f766e?style=flat-square" alt="GPL-3.0-or-later license" /></a>
  <img src="https://img.shields.io/badge/platform-SteamOS%20%7C%20Linux-6b8e23?style=flat-square" alt="SteamOS and Linux" />
</p>

<!-- prettier-ignore -->
> [!IMPORTANT]
> **[Decky LSFG-VK Experimental](https://github.com/eugeniosegala/decky-lsfg-vk-experimental) and [LSFG-VK Experimental](https://github.com/eugeniosegala/lsfg-vk-experimental) are now MAKO.** This repository is their new home and continuation. Future development, releases, documentation, and issue tracking happen here.

> **Independent project:** MAKO is independently developed and maintained for Steam Deck and Steam Machine. **MAKO Decky** provides per-game controls and integration, while **MAKO Renderer** supplies the Vulkan frame-generation layer. The project builds on work by **[PancakeTAS and the lsfg-vk contributors](https://github.com/PancakeTAS/lsfg-vk)** and **[xXJSONDeruloXx, the original Decky LSFG-VK developer](https://github.com/xXJSONDeruloXx/decky-lsfg-vk)**, whom MAKO gratefully thanks. Frame generation is available today, with scaling planned. MAKO requires `Lossless.dll` from a licensed [Lossless Scaling](https://store.steampowered.com/app/993090/Lossless_Scaling/) installation but does not bundle, copy, or modify it. Test it per game; MAKO is not an official Lossless Scaling, Decky Loader, or lsfg-vk release.

## Downloads

| Component | Recommended for | Releases |
| --- | --- | --- |
| **MAKO Decky** | Steam Deck, Steam Machine, and Decky Loader users | [Latest MAKO Decky release (ZIP under Assets)](https://github.com/eugeniosegala/MAKO/releases/latest) |
| **MAKO Renderer** | Direct Vulkan-layer installation without Decky | [Latest MAKO Renderer release (Linux archive under Assets)](https://github.com/eugeniosegala/MAKO/releases/tag/render-v2.1.0) |

<!-- prettier-ignore -->
> [!NOTE]
> Check the Downloads table regularly for updates. MAKO Decky and MAKO Renderer are published independently.

Published Renderer packages currently target x86_64 Linux hosts and include layers for both 64-bit and 32-bit x86 game processes. Native AArch64/Armada packages are not included in this release.

## ✨ Highlights

|  | Highlight | What it brings |
| :-: | --- | --- |
| 🖼️ | **Full-quality frame generation** | Uses the Lossless Scaling frame-generation models from the user's licensed installation, with quality and performance controls per profile. |
| 👻 | **Significantly reduced ghosting** | The full-quality v2 model with Performance Mode disabled can show noticeably less ghosting than the older layer. Supported AMD GPUs also gain extra protection against ghosting and corrupted moving edges. Results remain game-dependent. |
| 🎯 | **Adaptive Frame Generation** | Optionally targets 30–240 FPS while MAKO Renderer varies generated frames up to a selected 2x–4x ceiling. |
| 🌈 | **HDR foundation** | MAKO Renderer includes HDR10/PQ and linear-scRGB groundwork. MAKO Decky keeps HDR exposure disabled while activation, presentation, colour, and performance are validated across games. |
| 🧩 | **64-bit and 32-bit x86 Vulkan** | Ships architecture-matched host and Flatpak layers so Vulkan can select the correct library for each game process. |
| 🛡️ | **Gamescope recovery** | Bounded presentation recovery preserves native presentation and resumes generation only after the game cadence becomes stable again. |
| ⏯️ | **Live frame-generation switch** | Turns frame generation on or off without discarding the selected Fixed or Adaptive settings. |
| 🗂️ | **Dedicated game/process profiles** | Capture a running game once and keep its renderer and compatibility settings. MAKO automatically selects it by Steam app ID or process, with isolated per-profile controls including ALSA audio. |
| 🎮 | **Per-game Heroic and EmuDeck support** | Enables MAKO only for the Heroic games and EmuDeck titles you choose, using the same private configur