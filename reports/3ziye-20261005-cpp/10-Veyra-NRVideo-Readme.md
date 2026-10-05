# Veyra

<p align="center"><img src="assets/veyra-app-icon.png" alt="Veyra" width="160"></p>

<p align="center">
  <a href="https://github.com/Likely7/Veyra-NRVideo/blob/main/assets/veyra-2.0.0-promo.mp4">
    <img src="assets/veyra-2.0.0-promo.webp" alt="Veyra 2.0 promo (click to play the video)" width="960">
  </a>
</p>



<p align="center"><img src="docs/images/2.0.0/professional-mode.png" alt="Veyra 2.0.0 professional mode" width="1200"></p>

English | [简体中文](README_CN.md)

A Windows enhancement player for videos, images, capture cards and streaming. Super-resolution, NR, colour grading, RTX Video HDR and frame generation share one engine. Community enhancements remain experimental.

[Download 2.0.3 portable](https://github.com/Likely7/Veyra-NRVideo/releases/tag/v2.0.3) · [Full changelog: English / 中文](docs/RELEASE_NOTES_2.0.3.md) · [Issues](https://github.com/Likely7/Veyra-NRVideo/issues)

## Highlights

- **Rebuilt interface:** Home, Cinema, Professional List, Nodes, Colour, Export and Settings; Simplified/Traditional Chinese, English and Japanese.
- **Node editing and layered NR:** executable connections, independent NR/colour parameters, separate List/Node configurations, sessions and presets.
- **PC / Xbox streaming:** Moonlight/Sunshine-compatible PC streaming and unofficial experimental Xbox support, alongside PS5, capture cards and screen capture.
- **New export workflow:** editable ordered queue, trimming, MP4/MKV, multiple audio/embedded subtitle tracks, cancellation/retry and completion sound.
- **Enhancement and compatibility:** four NR runtime choices (NVIDIA original for RTX 50, Lecram, SF-v2 and AMD lmxxf), DLSS/XeSS/FSR options, capture improvements and a persistent OBS Game Capture switch with restart confirmation. Full details are in the Release.

## New in 2.0.3

- **GPU packages:** choose NVIDIA or AMD. AMD NR assets and NVIDIA-only NR/NGX/VFG/CUDA components are separated. Both keep the existing shared FidelityFX 2.3.0 components and cross-vendor FSR3.1/XeSS; FSR4 stays gray on NVIDIA.
- **Visible compatibility:** four NR versions, SR backends, FG backends, RTX HDR and optical flow retain unsupported entries with a disabled reason in List/Node mode. Restoring old configurations disables unavailable stages and preserves their parameters.
- **VFG and field fixes:** all 2–8X multipliers and Low/Medium/High; Xbox audio startup and bounded recovery; bitrate draft/validation/frozen exports; opaque RTSS-compatible UI; removed false NVIDIA App crash detection; fixed the minimal window's right-edge gap. Nine unrelated VFG NPP libraries are omitted. RX9000 inference and Xbox hardware long sessions remain unverified; HDR/Dolby PRs are deferred.


- Restore NVIDIA original NR as a third choice; existing Lecram/SF-v2 settings remain valid.
- Optional startup resume reopens the last movie at its saved position or starts the saved capture card configuration. Choose Cinema or Professional as your startup page.
- Both playback bars offer 1× / 1.5× / 2× / 3× movie speed with preserved audio pitch.
- Automatic RTSS compatibility, Xbox negotiation/shutdown fixes, VRR capture timing repair and GPU-reset export recovery. Fullscreen VRAM fallback is optional and **off by default**; the reported 5060 Ti leak itself remains unconfirmed.

## Install and upgrade

Download **Veyra-2.0.3-NVIDIA-win64-portable.7z** or **Veyra-2.0.3-AMD-win64-portable.7z** for Veyra's active GPU. Extract with 7-Zip into a new writable folder and run **veyra_qml_ui.exe**. You need one GPU package to run the application; source assets are only for rebuilding. Windows 11 x64 and DirectX 12 are required; Qt and approved runtimes are included, while GPU/capture drivers are installed separately. Backend hardware requirements vary; most local tests used an RTX 5070.

Start with effects off, check picture/sound, then enable effects individually. High resolution, layered NR and frame generation increase GPU/VRAM requirements.

**The 1.4.4 UI guide is obsolete.** Version 2.0 uses separate settings. Retain the old version for rollback; do not overwrite the new package with old `veyra.ini`, an entire `runtime_local` folder or mixed DLLs.

## Using 2.0

### Sources and pages

Home offers files, capture card, PS5, PC, Xbox and screen capture. Files/images can also be dropped into the window. Move to the bottom edge to reveal navigation between Home, Cinema, Professional, Colour, Export and Settings.

- Cinema prioritises the picture with a floating source/transport/audio/fullscreen bar, optionally hidden in settings.
- Professional List has Picture, Frame generation, Colour, Sound and Display tabs. The order strip locates effects; bottom panels report source/output, GPU stage time and load.
- Click a file's picture to pause/resume; left/right arrows seek five seconds. Double-click or use the fullscreen button. The fullscreen top-edge bar switches Cinema/Professional; **Home** opens quick controls in fullscreen List mode, **Ctrl+L** locks contr