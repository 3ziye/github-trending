# DLSS 5 Bridge

> [!WARNING]
> **Unofficial download site:** `dlss5bridge.com` is not operated or endorsed by this project.
> Get DLSS 5 Bridge from [this repository's GitHub releases](https://github.com/NIGos/dlss5-bridge/releases).
> Its ZIP contains an unofficial `.exe` installer. [Hybrid Analysis](https://hybrid-analysis.com/sample/5c3cc8dec5827d57f4cfe0968415eeb44ed3f865253bccbca95689989e462837/6aa123764f15cef3a90c2e95)
> classifies it as **Malicious** and records attempts to add Microsoft Defender exclusions for other executables.
> **Do not run installers from that site.** A user's reported compromise has not been independently verified;
> see [#30](https://github.com/NIGos/dlss5-bridge/issues/30).
> [Verify your download before loading it](VERIFYING-DOWNLOADS.md): official SHA-256 values and an optional PowerShell checker.

**A bridge for DLSS 5 Neural Rendering add-ons in DirectX 11 and Vulkan games,
with an optional optical-flow path for games without DLSS.**

A ReShade add-on that mirrors a DirectX 11 or Vulkan game's DLSS onto a private
DirectX 12 session, where a compatible neural rendering add-on can process it.
For games without DLSS, it can build substitute inputs from ReShade's depth
and NVIDIA Optical Flow, or a ReShade motion-vector shader. The game's files
are not patched.

This bridge does not do neural rendering itself. It needs a separate compatible
**DLSS 5 Neural Rendering add-on**, such as RenoDX's `renodx-dlss5.addon64`, distributed in
[its Discord channel](https://discord.com/channels/1408098019194310818/1542647972695904317),
together with its `nvngx_dlssnr.dll`. The bridge only gives that add-on a
place to work.

If it is useful to you, you can help cover the AI tooling used in its
development:

[![Support on Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/nigos)

Releases and their notes: [github.com/NIGos/dlss5-bridge/releases](https://github.com/NIGos/dlss5-bridge/releases).

**Release status (11 September 2026).** [v1.4.12](https://github.com/NIGos/dlss5-bridge/releases/tag/v1.4.12)
remains the stable release. `main` contains the cumulative 1.4.13 prerelease
changes and the [D3D11 depth/MV conversion fix](https://github.com/NIGos/dlss5-bridge/pull/34).
The latest test build, [v1.4.13-pre7](https://github.com/NIGos/dlss5-bridge/releases/tag/v1.4.13-pre7),
also fixes a Vulkan Frame Generation startup failure
reported in [Endfield](https://github.com/NIGos/dlss5-bridge/issues/27#issuecomment-5606803978):
it supplies the command buffer's device when NGX cannot infer one alongside
the Bridge's private device, and clears obsolete hooks when an NGX module unloads.
Pre7 includes all pre6 changes and has verified GitHub Actions build provenance.
It is still unsigned; follow the
[download verification instructions](VERIFYING-DOWNLOADS.md) before loading it.
Pre6 separated D3D11 temporal histories and the BG3 reporter confirmed that
shimmering was fixed. Pre7 additionally avoids rebuilding shared textures when
split-screen views have different heights. The official build passes the
unequal-height Gym test with neural rendering active; confirmation of the
stutter/shutdown fix in BG3 is still pending. Neural rendering reaching only one
BG3 viewport remains open ([#12](https://github.com/NIGos/dlss5-bridge/issues/12)).
The [BG3 FG reporter](https://github.com/NIGos/dlss5-bridge/issues/28#issuecomment-5609017168)
confirmed neural output, but also tested local hook changes and newer Streamline
files; flickering/ghosting and general hook coexistence remain under investigation.
The [Endfield reporter](https://github.com/NIGos/dlss5-bridge/issues/27#issuecomment-5609207523)
confirmed DLAA + MFG 4x + neural rendering working together on pre5.
The Endfield mirror slowdown
remains unresolved; the FG startup fix does not establish an FPS improvement.

Some neural add-ons support additional graphics APIs directly. Whether you need
this bridge depends on the add-on build and the game. See the compatibility
notes below; support for NGX D3D12 calls alone does not guarantee compatibility.

## What it does

The DLSS 5 add-on is not modified. It receives genuine NGX D3D12 calls on a
private D3D12 device, and its result is copied back into the game's output.
Three routes; the substitute is off by default:

| Route | Game | Contract |
| --- | --- | --- |
| **D3D11 bridge** | DirectX 11 with DLSS | The game's Color, Depth and MotionVectors are copied into shared textures, evaluated on D3D12 and copied back. The bridge follows the supplied dimensions, regions and parameters, with defaults for missing values. |
| **Vulkan mirror** | Vulkan with DLSS | The game's own, mirrored the same way through imported D3D12 textures. `vk_mirror=1`, the default. |
| **Substitute contract** | Games without DLSS that expose usable depth and motion inputs through ReShade | DLAA at back-buffer size, using NVIDIA Optical Flow or a ReShade motion-vector shader. Requires `synth=1`; availability depends on th