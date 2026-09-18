# DLSS5oneclick

<p>
  <a href="https://github.com/faisalkindi/DLSS5oneclick/releases/latest"><img src="https://img.shields.io/github/v/release/faisalkindi/DLSS5oneclick?style=flat-square&color=2878D0&label=Download" alt="Download"></a>
  <img src="https://img.shields.io/github/downloads/faisalkindi/DLSS5oneclick/total?style=flat-square&color=16A34A&label=Downloads" alt="Downloads">
  <img src="https://img.shields.io/github/stars/faisalkindi/DLSS5oneclick?style=flat-square&color=EAB308&label=Stars" alt="Stars">
  <a href="https://ko-fi.com/kindiboy"><img src="https://img.shields.io/badge/Support-Ko--fi-FF5E5B?style=flat-square&logo=ko-fi&logoColor=white" alt="Ko-fi"></a>
</p>

One button that sets up the **leaked DLSS 5 neural-rendering build** in any DirectX 11/12 game, with or without DLSS of its own. Single native Windows exe, no runtime. Everything it installs is downloaded from the projects that made it; the only third-party content inside the exe is three SIL-OFL fonts.

Download: [latest release](https://github.com/faisalkindi/DLSS5oneclick/releases/latest) → `dlss5oneclick.exe`.

## Two paths, picked automatically

| The game | What gets installed |
|---|---|
| **Ships its own DLSS** (an `nvngx_dlss.dll` this tool did not place, or Streamline `sl.*.dll`, `nvngx_dlssg/dlssd.dll`, anywhere up to four folders deep, or under an Unreal project's `Plugins` tree) | ReShade add-on build + the DLSS 5 add-on (`renodx-dlss5.addon64`, `nvngx_dlssnr.dll`). The add-on hooks the game's own NGX calls directly. **DX11 games** also get [dlss5-bridge](https://github.com/NIGos/dlss5-bridge), which replays the D3D11 DLSS calls on a private D3D12 device so the add-on can see them. No Feeder, no LumeniteFX; a Feeder left over from an earlier run is removed. |
| **Has no DLSS** | The full Feeder path below: ReShade + shader headers + DLSS5-Feeder + LumeniteFX + the DLSS 5 add-on + config. |

**Engine choice for games with native DLSS** (two cards at the top of the window, the second one greyed out with a reason when the game has no DLSS): the default engine is ReShade + the RenoDX add-on. A second engine — [Dagherbou's OptiScaler_DLSSNR fork](https://github.com/Dagherbou/OptiScaler_DLSSNR) (OptiScaler with a built-in Neural Rendering pass, colour composition from RenoDX under MIT) — can be picked in the GUI or with `--engine=opti`: the tool extracts the fork's release into the game as `dxgi.dll`, adds `nvngx_dlssnr.dll`, and records a manifest so Remove takes it out cleanly. In game, Insert opens the OptiScaler overlay; Neural Rendering is off by default there. The two engines cannot share a game (both load as dxgi.dll). Note the fork targets the unpatched model: on the driver's own DLL that means RTX 50; with the `310.8.SF` model this tool installs, older RTX generations may work but are untested there.

**Standalone AIO engine (experimental, since 0.13.15).** A third card, for 64-bit games ReShade can reach from `dxgi.dll`: [kibblerz's DLSS5 ReShade AIO](https://github.com/kibblerz/DLSS5-Reshade-AIO) (Apache-2.0) is one ReShade add-on that runs neural rendering, DLSS super resolution / DLAA and frame generation itself, so it takes the place of the Feeder and the RenoDX add-on together — frame generation in a game that never had it. Pick it in the GUI or with `--engine=aio`: the tool installs ReShade, extracts the 64-bit AIO zip beside the exe (recorded in a manifest so Remove takes it out), adds `nvngx_dlssnr.dll`, and places `nvngx_dlss.dll` and `nvngx_dlssg.dll` from NVIDIA's repository when the game has none. In game: turn the game's own upscaling, anti-aliasing and frame generation off, run windowed (the add-on's own recommendation), then Home → Add-ons → Standalone DLSS-NR + SR. Switching a game back to the ReShade engine removes the AIO first, so ReShade never loads two neural consumers. The 32-bit package is not wired.

**RTX 20/30 multi-frame generation (OptiScaler engine, since 0.13.20, experimental).** On a Turing or Ampere card the OptiScaler route shows one tick, *Unlock multi-frame generation on this RTX 20/30 card (3X–4X)*. It installs [ShyVortex's OptiScaler build](https://github.com/ShyVortex/OptiScaler-DLSSNR-PreSR-Multipass) — wilsjo2's pre-SR fork plus [sdli1995's `dlssg_sm86`](https://github.com/sdli1995/dlssg_for_sm86) Turing/Ampere unlock and the Streamline runtime it needs, same zip layout — in place of the build chosen above, and writes `[DLSSG] AmpereMfgUnlock=true`; untick and the chosen build comes back. The game must ship DLSS frame generation of its own. RTX 40 keeps its own tick; RTX 50 needs neither. `--ampere-mfg` on the command line. Not run in a game by the author; one report of it failing on Forza Horizon 6 on RTX 20.

**RenoDX HDR mod (optional, since 0.8.0; engine-independent since 0.8.1).** The [RenoDX](https://github.com/clshortfuse/renodx) project publishes game-specific HDR / tone-mapping mods as ReShade add-ons (`renodx-<game>.addon64`). When the tool recognises the game (Steam a