![DLSS5 Feeder](dlss5-feeder-logo-dark.png)

[![AI-DECLARATION: copilot](https://img.shields.io/badge/䷼%20AI--DECLARATION-copilot-fee2e2?labelColor=fee2e2)](AI-DECLARATION.md)

**[↓ Jump to the Table of Contents](#contents)**

> ## ⚠️ Careful of fake malicious websites
> 
> We got information that some **malicious** websites were making users download ZIP using similar name as this project, e.g. `DLSS5-Feeder-v0.7.0.zip.`
> 
> The only official release of DLSS 5 Feeder is on this GitHub, so be careful! 
> 
> *Thank to NIGos for the [report](https://github.com/jlrouzies-fr/DLSS5-Feeder/issues/88).*

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
> | neural consumer | driver **616.56** | driver **616.64** |
> |---|---|---|
> | *(none — DLAA only, no neural pass)* | — | ✅ 300/300 |
> | **Deep Fried Chicken** 1.4.8-alpha | — | ✅ 300/300 |
> | `renodx-dlss5` **v4.55** (classic engine) | — | ✅ 300/300 |
> | `renodx-dlss5` **"latest"** (classic engine) | — | ✅ 300/300 |
> | `renodx-dlss5` **v4.6** (lazy-adoption engine) | — | ❌ 1/300 |
> | `renodx-dlss5` **v4.7** (lazy-adoption engine) | ✅ 300/300 | ❌ 0/300 |
>
> Blank cells are combinations nobody has run. Measured with `--test` on one RTX 5090 through the
> 64-bit helper. On 616.64+ the evaluate faults inside NVIDIA's own `nvngx_dlssnr.dll`
> ([#54](https://github.com/jlrouzies-fr/DLSS5-Feeder/issues/54)) — **any one of these works:** Deep
> Fried Chicken, a classic-engine `renodx-dlss5`, or driver 616.56.
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
                                                    depth + MV     DLSS DLAA + DLSS 5 neural rendering
                                                                   ↓
                                    neural output written back over the frame → later effects → present
```

**[↓ Jump to the Contents](#contents)**

---

## Before you install: four things

None of this is hard, and the [automated installer](#install-the-automated-way) verifies most of it for you.

### 1. You might not need this project at all

If your game is **64-bit** and uses **DirectX 9, 11 or 12**, there is now a simpler option:
ShortFuse's **renodx-dlss** add-on does the whole job by itself. Use that instead — it is one
add-on rather than two, and there is nothing for this project to add.

| Your game | What to use |
| --- | --- |
| 64-bit, DirectX 9 / 11 / 12 | **renodx-dlss** on its own — you do not need DLSS5-Feeder |
| **32-bit** (any graphics API) | **DLSS5-Feeder** |
| **Vulkan** | **DLSS5-Feeder** |
| **DirectX 9**, and you want the best handling of motion | **DLSS5-Feeder** |

renodx-dlss is not on GitHub. It comes from the RenoDX Discord, `#DLSS5` channel:
<https://discord.com/invite/renodx>

<details>
<summary>Why DLSS5-Feeder is still the only option for those three</summary>

- **32-bit games.** renodx-dlss is 64-bit only, and NVIDIA ships no 32-bit NGX runtime at all, so
  an in-process approach is impossible there by construction. This project's cross-process helper
  is the only route.
- **Vulkan games.** Covered here through the bundled layer.
- **Real motion vectors on D3D9.** renodx-dlss evaluates only the finished backbuffer there, with
  no temporal inputs. This project drives a full temporal eval