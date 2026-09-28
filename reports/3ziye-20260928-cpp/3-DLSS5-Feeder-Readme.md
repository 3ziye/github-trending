![DLSS5 Feeder](docs/images/dlss5-feeder-logo-dark.png)

[![AI-DECLARATION: copilot](https://img.shields.io/badge/䷼%20AI--DECLARATION-copilot-fee2e2?labelColor=fee2e2)](AI-DECLARATION.md) [![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?logo=buymeacoffee&logoColor=black)](https://buymeacoffee.com/jlrouzies)

**[↓ Jump to the Table of Contents](#contents)**

> ## ⚠️ Careful of fake malicious websites
> 
> We got information that some **malicious** websites were making users download ZIP using similar name as this project, e.g. `DLSS5-Feeder-v0.7.0.zip.`
> 
> The only official release of DLSS 5 Feeder is on this GitHub, so be careful! 
>
> This now includes **copies of this repository on GitHub itself**: same source tree, but the README replaced by a "Download" button leading to a ZIP on a personal `github.io` page, sold as "double-click to run, it detects your game". This project has no executable installer, only a PowerShell script you can read, and the only download is <https://github.com/jlrouzies-fr/DLSS5-Feeder/releases>. If you got a ZIP anywhere else, delete it and scan your machine.
> 
> *Thank to NIGos for the [report](https://github.com/jlrouzies-fr/DLSS5-Feeder/issues/88), and to the reporter of [#115](https://github.com/jlrouzies-fr/DLSS5-Feeder/issues/115).*

> ## ℹ️ Does not work with your game? Read this part
> 
> Please note that I cannot test every games reported in the issues (as I simply do not own them or don't have time to try all).
>
> If you are really looking for a specific game to work, see to get like a Claude Pro subscription, install it and ask it the following:
>
> "Here is my game folder: [GAME PATH] ; I am using https://github.com/jlrouzies-fr/DLSS5-Feeder but sadly it doesn't work well. Can you help clone it, check the different logs, and implement a fix? Then if you implement a legitimate fix, make a pull request."
>  

> ## ⚠️ Nvidia Driver can cause issues with some addons
>
> **Some combinations of driver, NGX runtime and neural consumer do not work — it is usually the
> combination, not the game.** Check yours in fifteen seconds, with no game running:
> `host64\dlss5-feed-host64.exe --test` (`300/300 evaluates succeeded` means you are fine). The
> scenarios we know about:
>
> | neural consumer | driver **616.56** | driver **616.64** | driver **617.14** |
> |---|---|---|---|
> | *(none — DLAA only, no neural pass)* | — | ✅ 300/300 | — |
> | **Deep Fried Chicken** 1.4.8-alpha | — | ✅ 300/300 | — |
> | `renodx-dlss5` **v4.55** (classic engine) | — | ✅ 300/300 | — |
> | `renodx-dlss5` **"latest"** (classic engine) | — | ✅ 300/300 | — |
> | `renodx-dlss5` **v4.6** (lazy-adoption engine) | — | ❌ 1/300 | — |
> | `renodx-dlss5` **v4.7** (lazy-adoption engine) | ✅ 300/300 | ❌ 0/300 | ❌ 0/300 |
> | `renodx-dlss5` **v6.1.0** | — | — | ✅ 300/300 |
> | `renodx-dlss5` **v7.0.0-rc8** | — | — | ✅ 300/300 |
> | `renodx-dlss5` **v8.0.1** (beta 8) | — | — | ✅ 300/300 |
>
> Blank cells are combinations nobody has run. Measured with `--test` on one RTX 5090 through the
> 64-bit helper; every ✅ on 617.14 also created and evaluated the neural feature. On 616.64+ the
> v4.6/v4.7 evaluate faults inside NVIDIA's own `nvngx_dlssnr.dll`
> ([#54](https://github.com/jlrouzies-fr/DLSS5-Feeder/issues/54)) — **any one of these works:** a
> `renodx-dlss5` **v6.1 or newer** (what the installer now downloads), Deep Fried Chicken, a
> classic-engine `renodx-dlss5`, or driver 616.56.
>
> **The neural model runs on RTX 50 only.** NVIDIA's signed `nvngx_dlssnr.dll` 310.8.0, and the
> modified 310.8.Lecram build the installer downloads, create the neural feature on RTX 50-series
> GPUs only. On an RTX 20/30/40 DLSS still runs but the neural pass does not (`feature 18 create
> failed with 0xbad00001` in `ReShade.log`, [#131](https://github.com/jlrouzies-fr/DLSS5-Feeder/issues/131)):
> get the modified `nvngx_dlssnr.dll` made for your GPU from the
> [RenoDX Discord](https://discord.com/invite/renodx). `Verify-DLSS5Feeder.ps1` says so at the end.
>
> Use **0.14.0-beta.2 or newer**, and run `Verify-DLSS5Feeder.ps1` in the game folder before reporting anything.

## Description

**DLSS 5 neural rendering in games that ship without any DLSS — D3D11, D3D12, Vulkan, OpenGL, 32-bit, even DirectX 10 and DirectX 9.**

DLSS 5's neural-rendering add-on only works by hooking a game's own DLSS calls. A game that has no
DLSS never makes those calls, so the add-on sits idle. **DLSS5-Feeder makes the calls itself.** It
builds a complete DLSS DLAA "contract" out of what ReShade already has — the frame being processed,
the depth buffer, and estimated optical-flow motion vectors — runs a genuine DLSS evaluate, lets the
DLSS 5 neural-rendering add-on hook into that evaluate, and copies the neural result back into the
frame. All inside ReShade's effect chain.

```
game frame → ReShade effects → [motion vectors] → [DLSS5_Feed] → DLSS5-Feeder:
                                                    depth + MV    