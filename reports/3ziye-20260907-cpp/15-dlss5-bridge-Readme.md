# DLSS 5 Bridge

**DLSS 5 Neural Rendering for DirectX 11 games, Vulkan games, and, as an
option, games that have no DLSS at all, through NVIDIA Optical Flow, at lower
quality.**

A ReShade add-on. The DLSS 5 neural rendering add-on only works where a game
runs DLSS on DirectX 12. This bridge gives it that: it mirrors a DirectX 11 or
Vulkan game's own DLSS onto a private DirectX 12 session, and for a game
without DLSS it can build a substitute one from ReShade's depth and the
driver's motion vectors. Nothing in the game is modified.

This bridge does not do neural rendering itself. It needs the separate **DLSS 5
Neural Rendering add-on** (RenoDX's `renodx-dlss5.addon64`), distributed in
[its Discord channel](https://discord.com/channels/1408098019194310818/1542647972695904317),
together with its `nvngx_dlssnr.dll`. The bridge only gives that add-on a
place to work.

If it is useful to you, you can help cover the AI tooling used in its
development:

[![Support on Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/nigos)

Releases and their notes: [github.com/NIGos/dlss5-bridge/releases](https://github.com/NIGos/dlss5-bridge/releases).

**Status.** Newer builds of the DLSS 5 add-on reach DirectX 11 and DirectX 9
on their own; the builds that do not still need this bridge, and it is kept
working for them. Issues are read and fixed, and releases continue. Every
release is run through [ngxGym](https://github.com/NIGos/ngxGym) on D3D11 and
Vulkan before it is published.

## What it does

The DLSS 5 add-on is not modified. It receives genuine NGX D3D12 calls on a
private D3D12 device, and its result is copied back into the game's output.
Three routes, chosen automatically:

| Route | Game | Contract |
| --- | --- | --- |
| **D3D11 bridge** | DirectX 11 with DLSS | The game's own, mirrored per frame: Color, Depth and MotionVectors copied into shared textures, evaluated on D3D12, copied back. Every size, offset and scalar comes from the game's parameter block. |
| **Vulkan mirror** | Vulkan with DLSS | The game's own, mirrored the same way through imported D3D12 textures. `vk_mirror=1`, the default. |
| **Substitute contract** | Any game with no DLSS, or with its DLSS switched off | DLAA at back-buffer size, built from ReShade's depth and the NVIDIA driver's optical flow. `synth=1`, off by default. |

The game's own DLSS always wins. The substitute takes the session only when
the game is not asking, and hands it back on the game's next call.

The substitute is a real DLSS feature fed approximated inputs, and it shows:
text softens and dense foliage smears. It is an option, not a default.

## Requirements

An NVIDIA GPU and driver with D3D12 support. In the game folder, beside the
executable:

| File | From |
| --- | --- |
| `dxgi.dll` — ReShade 6.0 or newer **with add-on support** | reshade.me, full version |
| A DLSS 5 Neural Rendering add-on (`renodx-dlss5.addon64`) | [its Discord channel](https://discord.com/channels/1408098019194310818/1542647972695904317). Any add-on that hooks the NGX D3D12 entry points is driven the same way |
| `nvngx_dlssnr.dll` | shipped with that add-on |
| `dlss5-bridge.addon64` | this project |
| `nvngx_dlss.dll` 3.1.13 or newer | the game, if it has DLSS. **Required only with `synth=1`**, and then also in a game without DLSS: the driver store carries no super-resolution snippet, and the substitute is DLAA, which older snippets accept and degrade. Below 3.x the bridge refuses and names the version. |

The neural add-on's own toggle has to be on, in its panel or in `ReShade.ini`.

**The neural add-on's build matters, and its version number does not identify
one.** Two builds of 2026-08-28 declare the same version; the newer one needs to
see this add-on's D3D12 device through ReShade's proxy, and underneath it
reports active and writes nothing. The log prints a SHA-256 for every add-on
beside this one, says whether that build has been measured here, and keeps the
proxy for a build that needs it.

## Install

Copy `dlss5-bridge.addon64` next to ReShade. On first run it writes
`dlss5-bridge.cfg` with working defaults; nothing needs configuring. To remove
the add-on, delete the file.

The settings file's first line is the version that wrote it. A different version
replaces the file with its own defaults on first run and says so in the log;
the same version never touches it. `# dlss5-bridge keep` as the first line
keeps a file across versions.

**Games without DLSS.** The substitute contract needs three files beside the
game's executable that such a game does not bring: the DLSS 5 add-on and its
`nvngx_dlssnr.dll`, and a **`nvngx_dlss.dll` of version 3.1.13 or newer**,
copied by hand from any game that has DLSS. The NVIDIA driver does not supply
that file, and NGX looks for it only in the executable's folder. Then turn on
the panel switch, or set `synth=1`. If the file is missing, the panel and the
log say so and name it.

**Upgrading from 1.1.0 or earlier:** the files were 