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
  <a href="#project-status">Status</a> |
  <a href="#install-and-play">Install and play</a> |
  <a href="#in-game-menu">In-game menu</a> |
  <a href="#if-something-goes-wrong">Problems</a> |
  <a href="#build-from-source">Build from source</a> |
  <a href="#how-it-works">How it works</a> |
  <a href="#want-to-help">Want to help?</a> |
  <a href="#credits">Credits</a> |
  <a href="#license">License</a>
</p>

Hookshot is a static recompilation. The game's code is translated to C and compiled into a Windows or Linux program,
the console's system software is reimplemented, and the Switch 2 graphics are rebuilt on Vulkan. All of this happens
**on your PC, from your own copy of the game**.
<br>

> [!WARNING]
> Some users report the file in releases to be a Trojan - it is not. Feel free to run it through any antivirus software


Discord: https://discord.gg/DVQQJphbBf
<br>

> [!IMPORTANT]
> This repository **does not contain the game, keys or an executable**, and it does not explain how to get them. You
> need your own copy. Everything the build creates (`hookshot.exe`, the generated code, the shader caches and your
> saves) comes from your game and stays on your PC. Never share those files.

## Project status

Experimental. Most testing so far has been around the start of the game. Players have reported on many PCs since:
the table says what works and what does not yet.

| What | Status |
|---|---|
| Kokiri Forest: reaching gameplay and walking around | ✅ Works |
| Sound, controller, keyboard and saves | ✅ Works |
| In-game menu, frame generation and upscaling | ✅ Works |
| Flicker (the picture flashing too bright while moving) | ✅ Fixed in v2.0.2 ([#645](https://github.com/NotRexed/Hookshot/pull/645)) |
| Ground fog vanishing when looking down | ✅ Fixed in v2.0.2 ([#638](https://github.com/NotRexed/Hookshot/pull/638)) |
| Models with missing pieces (doors, fences, parts of trees) | ✅ Fixed where tested, more play needed |
| Stutter when entering new areas | ⚠️ Still happens the first time you visit a place. The next visits are smooth |
| Performance | ⚠️ Depends on the PC: some reach a steady 60 fps, others stay below it, more so in Hyrule Field |
| Hyrule Field, Castle Town, Kakariko and the dungeons | ⚠️ Players got there, with open bugs: striped shadows in Hyrule Field ([#468](https://github.com/NotRexed/Hookshot/issues/468)), some crashes ([#317](https://github.com/NotRexed/Hookshot/issues/317), [#648](https://github.com/NotRexed/Hookshot/issues/648)) |
| Ultrawide | ⚠️ The 3D keeps its shape, but the HUD is stretched and the picture is softer |
| NVIDIA cards | ✅ Works. The most tested |
| AMD cards | ⚠️ Some tested: reports from the RX 6600, RX 7800 XT and RX 7900 XTX. Known issue: the game loses the GPU in the Deku Tree on the RX 6600 ([#708](https://github.com/NotRexed/Hookshot/issues/708), [#614](https://github.com/NotRexed/Hookshot/issues/614)) |
| Intel cards | ❓ Few reports, many of them black screens or crashes ([#17](https://github.com/NotRexed/Hookshot/issues/17)) |
| Cards without mesh shaders (such as AMD RX 5000 and older) | ❌ Not supported: parts of the picture are missing. A fallback was tried and taken out again for now ([#640](https://github.com/NotRexed/Hookshot/issues/640)) |
| Linux | ✅ Works with the AppImage. Tested on several distributions (CachyOS, Fedora, Bazzite, SteamOS) and cards, with open problems on some AMD cards ([#604](https://github.com/NotRexed/Hookshot/issues/604), [#528](https://github.com/NotRexed/Hookshot/issues/528)) |

## Install and play

The game does not come ready-made: Hookshot Builder builds it on your PC from your copy. You do this once. After that
you start the game from its launcher, which also updates it.

### What you need

- **Your copy of the game at the supported version:** program `0400486024DEC000`, update v131072, build `e0f3ccfa`.
  Other versions do not work. A `.nup` file, or the `romfs` and `exefs` folders.
- 64-bit Windows 10 or 11, or 64-bit Linux with glibc 2.35 or newer (Ubuntu 22.04, Debian 12, Fedora, Arch,
  SteamOS ...) and a CPU with AVX2.
- A graphics card with Vulkan 1.3 and mesh shaders, with an up-to-date driver: NVIDIA GeForce RTX 20 series or newer,
  AMD Radeon RX 6000 series or newer, or Intel Arc. On Linux, Mesa or NVIDIA's driver. Cards without mesh shaders are
  not supported.
- 8 GB of video memory (VRAM) or more is recommended. Cards with less can use the in-game menu's lower Quality presets.
- 16 GB of RAM or more. A run uses about 10 GB.
- About 60 GB free while building.
- An internet connection for the download. Nothing else to install: the builder brings its own compiler and tools.

### On Windows

1. Open the [latest release](h