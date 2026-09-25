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
| **Ships its own DLSS** (an `nvngx_dlss.dll` this tool did not place, or Streamline `sl.*.dll`, `nvngx_dlssg/dlssd.dll`, anywhere up to four folders deep, or under an Unreal project's `Plugins` tree) | ReShade add-on build + **ShortFuse's DLSS add-on** (`renodx-dlss.addon64`, from the author of RenoDX) + the DLSS 5 model (`nvngx_dlssnr.dll`). The add-on hooks the game's own NGX calls in D3D11 and D3D12 itself (its own DX11 and DX12 NGX hooks), so no bridge is installed with it; its DX11 path has been installed and checked here as files, not yet reported from a game. If that does not work in a game, the next setup down is the RenoDX DLSS 5 add-on (`renodx-dlss5.addon64`), which in **DX11 games** also gets [dlss5-bridge](https://github.com/NIGos/dlss5-bridge) to replay the D3D11 DLSS calls on a private D3D12 device. No Feeder, no LumeniteFX; a Feeder left over from an earlier run is removed. |
| **Has no DLSS** | The full Feeder path below: ReShade + shader headers + DLSS5-Feeder + LumeniteFX + the DLSS 5 add-on + config. |

**The setup is picked for you (since 0.14.0).** The Setup page shows one line: the setup Install will use and why (the game has its own DLSS or not, DirectX version, 32/64-bit, card generation), and one **Install** button. For a 64-bit game with its own DLSS the order it tries is:

1. ReShade + ShortFuse's DLSS add-on (the default),
2. ReShade + the RenoDX DLSS 5 add-on, newest stable build,
3. the same add-on at 4.70 (the build every reporter had working when 5.2.1 broke four games, and the last with Enable Upscaling),
4. the same add-on at 4.55 (the build the Feeder's host names as passing where newer ones fault in the driver),
5. the OptiScaler engine.

A game with no DLSS of its own gets the Feeder with the DLSS 5 add-on (newest stable, then 4.70, then 4.55), and a Vulkan game with DLSS goes to OptiScaler. Games whose reports settled it start further down: Cyberpunk 2077 on OptiScaler (#95), Dragon's Dogma 2 on 4.70 (#96). A game already on ReShade whose list starts on OptiScaler (Cyberpunk set up by an older version) keeps its ReShade setup and has OptiScaler as its last step instead.

Once a game is installed, **"Not working? Try the next setup"** moves it one step down the list and installs that. When the engine changes, the old one is taken out first, and the RenoDX HDR mod goes back in if it was there. A switch that would take ReShade out of a game carrying ReShade add-ons this tool did not install is refused before anything is removed. Which step a game is on is read from what is in its folder: the add-on and the build this tool recorded beside it, or the OptiScaler manifest. So **Install and Update refresh the setup a game already has** (a pinned 4.70 or 4.55 included) instead of moving it, and only "Try the next setup" or Advanced changes it. Everything below (engines, add-on choice, builds, frame generation, model resolution) is under **Show advanced options**, closed by default; the app remembers whether you left it open. Opening it means the controls decide; **Hide advanced options** goes back to the automatic setup. An install made before 0.14.0 with Neural Upstream or the standalone AIO is left as it is and shown under Advanced. Release candidates (`-rc`, beta) are never the "newest stable" build. On the OptiScaler engine a game keeps the model resolution in its `OptiScaler.ini`. A new install on an RTX 20/30 card gets 75%, except on the pre-SR and RTX 20/30 builds, which flicker below 100%.

**Engine choice for games with native DLSS** (under Advanced; two cards at the top of the window, the second one greyed out with a reason when the game has no DLSS): the default engine is ReShade + the RenoDX add-on. A second engine — [Dagherbou's OptiScaler_DLSSNR fork](https://github.com/Dagherbou/OptiScaler_DLSSNR) (