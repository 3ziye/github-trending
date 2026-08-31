# DLSS 5 DX11 Bridge

A ReShade add-on that lets a DLSS 5 Neural Rendering add-on — which only hooks
DirectX 12 — run inside a game that renders with DirectX 11.

Tested on Baldur's Gate 3 (DX11 build), with DLAA and with every DLSS quality
preset. Nothing here is specific to that game.

## What it does

A DLSS 5 add-on works by detouring `NVSDK_NGX_D3D12_CreateFeature` and
`NVSDK_NGX_D3D12_EvaluateFeature` and inserting its neural-rendering pass into
them. A D3D11 game never calls those functions, so the add-on sits idle forever
showing "waiting for game DLSS".

This bridge intercepts the game's own `NVSDK_NGX_D3D11_EvaluateFeature_C`,
forwards it untouched, and then reproduces the same DLSS contract on a second
NGX session running on its own D3D12 device. That D3D12 evaluate is a genuine
NGX call, so the DLSS 5 add-on detours it and does its work. The result is
copied back into the game's own output texture.

The DLSS 5 add-on is not modified or patched in any way. It simply starts
receiving the calls it was always waiting for.

Per frame:

1. copy the game's Color and MotionVectors into shared textures
2. convert the game's depth into a shared `R32_FLOAT` texture with a compute
   shader — `CopyResource` cannot, the formats are in different typeless
   families. Which view format is legal depends on the game's depth format, so
   it is read from the texture rather than assumed
3. signal a fence shared between the D3D11 and D3D12 queues
4. run the D3D12 evaluate, which is where the DLSS 5 add-on inserts itself
5. signal back, and copy the result into the game's output

Every size, offset and scalar is read from the game's own NGX parameter block
and forwarded verbatim, so upscaling presets work as well as DLAA.

## Requirements

In the game folder, alongside the game executable:

| File | Where from |
| --- | --- |
| `dxgi.dll` — ReShade 6.8+ **with add-on support** | reshade.me, full version |
| a DLSS 5 Neural Rendering ReShade add-on | its own author |
| `nvngx_dlssnr.dll` | shipped with that add-on |
| `dlss5-dx11-bridge.addon64` | this package |

The DLSS 5 add-on's own neural-rendering toggle has to be enabled, either in
its ReShade overlay panel or in `ReShade.ini`.

The bridge itself needs a D3D11 game with native DLSS, a GPU and driver that
support D3D12, and `ID3D11Device5` for cross-API shared fences.

## Install

Drop `dlss5-dx11-bridge.addon64` next to ReShade. On first run it writes
`dlss5-dx11-bridge.cfg` with working defaults; nothing needs configuring.

To remove it, delete the file.

Nothing on disk is patched. The only writes to foreign code are 14 bytes at
three function entry points, in memory, restored around every call.

## Configuration

`dlss5-dx11-bridge.cfg` is re-read while the game runs, so values can be
changed without restarting. Changes that only take effect on a new NGX feature
trigger a rebuild automatically.

| Key | Default | Meaning |
| --- | --- | --- |
| `stage` | 3 | How much of the bridge runs. `0` fully inert, `1` the input copies only, `2` also the depth conversion, `3` everything. Useful for isolating a problem: if `stage=0` still misbehaves, the bridge is not the cause. |
| `mode` | 2 | `0` never writes to the game, `1` transport only with no DLSS, `2` the full path. |
| `skip_game` | 1 | Do not forward the game's own DLSS evaluate. Its result is overwritten anyway, so running it is wasted work. Suppressed only while the bridge is healthy and already delivering. |
| `flags` | 107 | `DLSS.Feature.Create.Flags` for the bridge's feature. |
| `subrects` | 1 | Fallback for `DLSS.Enable.Output.Subrects`, used only when the game does not set one of its own. |
| `reset_every` | 0 | `1` forces the NGX Reset flag every frame, discarding temporal history. Diagnostic only. |
| `pixels` | 0 | `1` reads pixels back to the CPU for debugging. Stalls the GPU hard. |

## Log

`dlss5-dx11-bridge.log` records the contract read from the game, which
resource-sharing direction the driver accepted, the result of every NGX call,
and a timing line every 600 frames:

```
[bridge] 600 frames: bridge CPU 0.84 ms/frame | frame interval 16.00 ms (62.5 fps) | spread 5.74-29.93 ms | bridge is 5% of the frame | d3d12 43200/43202 (2 behind)
```

- **bridge CPU** is time spent inside this add-on, mostly waiting on the GPU
  rather than working. Read it next to the frame interval, not on its own.
- **spread** is the widest and narrowest gap between consecutive frames in the
  window. The average hides it, and it is what a driver-side frame generator
  responds to.
- **d3d12 N/M** is how far the D3D12 side is running behind. One to a few is
  ordinary pipelining. A gap that grows while the log then stops is the
  transport stalling; a small gap before a log stops dead means it is not.

## Performance

- The transport costs nothing measurable. With the D3D12 device, queue and
  allocators created but the evaluate disabled (`stage=2`), frame time matches
  the add-on being fully inert (`stage=0`).
- 