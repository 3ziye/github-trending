## ⚠️ Not compatible with Nvidia Smooth Motion / Optiscaler. Disable them to avoid issues.

# DLSS5-Feeder

**DLSS 5 neural rendering in games that ship without any DLSS — D3D11, D3D12, Vulkan, 32-bit, even DirectX 9.**

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

## Contents

- [Status](#status)
- [Install for a 64-bit game](#install-for-a-64-bit-game)
- [Install for a 32-bit game](#install-for-a-32-bit-game-beta)
- [Install for a DirectX 9 game](#install-for-a-directx-9-game-beta)
- [Install for a Vulkan game](#install-for-a-vulkan-game)
- [Motion vectors: choosing a provider](#motion-vectors-choosing-a-provider)
- [How it works](#how-it-works)
  - [The 32-bit path](#the-32-bit-path)
  - [The DirectX 9 path](#the-directx-9-path)
  - [The Vulkan path](#the-vulkan-path)
- [Requirements](#requirements)
- [Configuration](#configuration)
- [Logs and troubleshooting](#logs-and-troubleshooting)
- [Building](#building)
- [Limitations and roadmap](#limitations-and-roadmap)
- [Credits](#credits)
- [License](#license)

## Status

Proven working in six games covering every supported path:

| Game | Bitness / API | Result |
| --- | --- | --- |
| **Metro 2033 Redux** | 64-bit D3D11 | 4K DLAA + NR, HDR backbuffer |
| **The Lord of the Rings: War in the North – Legacy Edition** | 64-bit D3D12 | 4K, same-device path, 120 fps |
| **Splinter Cell: Blacklist** | 32-bit D3D11 | 60 fps, cross-process host |
| **BioShock Remastered** | 32-bit D3D11 (D3D9→D3D11 wrapper) | 4K, Luma HDR |
| **Fable Anniversary** | 32-bit **D3D9** via dgVoodoo2 | 1440p, 60 fps |
| **DOOM (2016)** | 64-bit **Vulkan** | 4K, D3D12 evaluate via cross-API interop |

In each, the DLSS 5 add-on reports `feature 18 created … inline feature 18 evaluation succeeded`,
driven entirely by ReShade depth + estimated motion vectors.

It is not game-specific: any D3D11, D3D12 or Vulkan game with a working ReShade depth buffer and a
motion vector provider should work — 64-bit directly, 32-bit via a bundled 64-bit helper process,
D3D9 via a wrapper.

**This is beta software.** Expect the temporal quality of *estimated* motion vectors (some ghosting
in fast motion, softness on thin moving geometry), and the HUD is processed along with the scene.

> ### 0.6.0-beta: read this before installing
>
> **The motion-vector provider is now chosen with a preprocessor definition** (`DLSS5_MV_PROVIDER`)
> instead of being whichever shader happens to write `texMotionVectors`. Five providers are
> supported and the recommended one is **[LumeniteFX](https://github.com/umar-afzaal/LumeniteFX)
> Kernel** — see [Motion vectors: choosing a provider](#motion-vectors-choosing-a-provider).
>
> **If you installed a release up to 0.5.2 and followed the old instructions, your feed has most
> likely been running on zero motion vectors.** ReshadeMotionEstimation (DRME), which those releases
> recommended, **does not compile on ReShade 6.8** (`error X3020: cannot sample from texture that is
> also used as render target`). ReShade still lists it as an enabled technique, so nothing looked
> wrong — but it wrote nothing. This release detects that and says so in the overlay and the log.

## Install for a 64-bit game

1. **ReShade with add-on support** — from **https://reshade.me**, run the installer, pick your game's
   `.exe`, choose **Direct3D 10/11/12**, and tick **"Enable loading of add-ons"** (the full /
   unsigned build). This puts `dxgi.dll` next to the game.
2. **DLSS5-Feeder** — from the
   **[latest release](https://github.com/jlrouzies-fr/DLSS5-Feeder/releases/latest)** download
   **`dlss5-feed.addon64`** and **`DLSS5_Feed.fx`**. Put `dlss5-feed.addon64` next to the game `.exe`
   (same folder as `dxgi.dll`), and `DLSS5_Feed.fx` into `reshade-shaders\Shaders\`.
3. **Motion vectors** — the recommended provider is
   **[LumeniteFX](https://github.com/umar-afzaal/LumeniteFX)** (its own repository; nothing of it
   is bundled here). Green **Code ▸ Download ZIP**, then copy
   - everything in its `Shaders\` — the `lumenite_*.fx` files **and** the `include\` folder —
     into `reshade-shaders\Shaders\`
   - `Textures\lumenite_bluenoise256.png` int