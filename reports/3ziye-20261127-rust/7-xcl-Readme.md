<p align="center">
  <img src="assets/readme/banner.svg" width="100%" alt="XCL – console games you own, running natively on Windows: no CPU emulation, RDNA2 shaders recompiled to DXIL, Direct3D 12">
</p>

<p align="center">
  <a href="https://discord.gg/xcl"><img alt="Discord: join the server" src="https://img.shields.io/badge/Discord-join%20the%20server-7c5cff?style=for-the-badge"></a>
  <a href="https://github.com/xcl-dev/xcl/actions/workflows/ci.yml"><img alt="CI" src="https://img.shields.io/github/actions/workflow/status/xcl-dev/xcl/ci.yml?branch=main&style=for-the-badge&label=CI"></a>
  <a href="LICENSE"><img alt="License: GPL-2.0-only" src="https://img.shields.io/badge/license-GPL--2.0--only-7c5cff?style=for-the-badge"></a>
  <img alt="Windows 10 / 11 x64" src="https://img.shields.io/badge/Windows-10%20%2F%2011%20x64-2f80ed?style=for-the-badge">
  <img alt="Direct3D 12, Shader Model 6.6" src="https://img.shields.io/badge/D3D12-SM%206.6-1fb9d8?style=for-the-badge">
  <img alt="Rust" src="https://img.shields.io/badge/Rust-stable--msvc-1fb9d8?style=for-the-badge">
</p>

<p align="center">
  <b><a href="#games">Games</a></b> ·
  <b><a href="#highlights">Highlights</a></b> ·
  <b><a href="#how-it-works">How it works</a></b> ·
  <b><a href="#quick-start">Quick start</a></b> ·
  <b><a href="#what-works">What works</a></b> ·
  <b><a href="#controls">Controls</a></b> ·
  <b><a href="#building-and-usage">Building and usage</a></b> ·
  <b><a href="#tests">Tests</a></b> ·
  <b><a href="#contributing">Contributing</a></b>
</p>

# XCL – Xbox Series X|S → Windows compatibility layer

XCL is a compatibility layer that runs Xbox Series X|S (GDK) games you own on a Windows PC - in the spirit of Wine/Proton. There is no CPU emulation: the game's x64 code runs natively, and XCL provides its own, independently written implementations of the console system libraries the PC does not have (`kernelx.dll`, XGameRuntime, `d3d12_xs.dll`, …). The console's GPU code (RDNA2 machine code) is recompiled into PC shaders (HLSL → DXIL).

> [!IMPORTANT]
> XCL works only on unpacked game files you already own. It does not download, decrypt or unpack game packages (XVC / MSIXVC) and contains nothing for circumventing DRM. The repository holds no code, headers or binaries from the console SDK, no keys and no game data; the Windows components XCL relies on (XGameRuntime, XAudio2, D3D12, DXC) come from your own system or the public Windows SDK and are not distributed with XCL.

<p align="center"><img src="assets/readme/divider.svg" width="100%" alt=""></p>

## Games

<p align="center">
  <img src="assets/readme/status.svg" width="100%" alt="A newer retail game, about 60 % of the way to playable (estimate): ~4 s to its first frame, 30 fps in its menus, ~5 fps in its 3D world, 100 % of its shaders translate">
</p>

| Game | State | What works | Limits |
|---|---|---|---|
| **Minecraft Preview**<br><sub>`Microsoft.MinecraftBeta` 1.18.3064.0</sub> | ✅&nbsp;playable | fully playable | – |
| **Unicorn Overlord**<br><sub>`SEGAofAmericaInc.Pa253b0c1Y` 1.0.0.6</sub> | ✅&nbsp;playable | fully playable | – |
| **Fortnite**<br><sub>`436609B6.FortniteClient` 2.0.1461.7919</sub> | ✅&nbsp;works | works fully, as far as the game allows without its online services | the game itself is online-only (multiplayer servers) |
| **XDefiant**<br><sub>`Ubisoft.XDefiant-Game` 1.0.0.186</sub> | ✅&nbsp;works | works fully, as far as the game allows without its servers | the game's own servers have been shut down |
| **A newer retail game** | 🚧&nbsp;**≈&nbsp;60&nbsp;%**<br><sub>estimate</sub> | starts in ~4 s, runs at a steady 30 fps without a crash, shows its menus and goes on past the first one to its settings; fits a 32 GB machine (~15 GB committed in the menus). With the NVIDIA integration branch ([#2057](https://github.com/xcl-dev/xcl/pull/2057)) it goes on into its 3D world: **~5 fps there** on an RTX 5090 (14 fps on average over a whole 5-minute run, its menus and loading included) | not playable yet: the picture of the world is incomplete (its minimap and other mesh pipelines are refused), and it does not keep running there for long |

## Highlights

<table>
  <tr>
    <td width="33%" valign="top" align="center">
      <img src="assets/readme/icon-native.svg" width="56" alt=""><br>
      <p align="left"><b>No CPU emulation</b> – the game's x64 code runs natively, in the spirit of Wine / Proton.</p>
    </td>
    <td width="33%" valign="top" align="center">
      <img src="assets/readme/icon-shader.svg" width="56" alt=""><br>
      <p align="left"><b>100 % of a retail game's shaders translate</b> – all 26 698 RDNA2 programs (26 503 records) of its shader pack become HLSL; random samples compile to DXIL with 0 errors.</p>
    </td>
    <td width="33%" valign="top" align="center">
      <img src="assets/readme/icon-dll.svg" width="56" alt=""><br>
      <p align="left"><b>The game's own console DLLs run on the PC</b> – its Bink 2 video codec decodes the game's movies,