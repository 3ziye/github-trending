<div align="center">

# Lost Odyssey Recomp

**An experimental native PC port of Lost Odyssey for Xbox 360.**

Windows x64 · Direct3D 12 · Vulkan · PowerPC static recompilation

<img src="docs/images/title-screen.png" alt="Lost Odyssey title screen — Press START" width="960">

Optional diagnostics are off by default and can be disabled in Settings. See [Privacy](PRIVACY.md).

### [Latest download](https://github.com/freefrank/LostOdysseyRecomp/releases/latest) · [Installation guide](docs/INSTALLING.md) · [Report an issue](https://github.com/freefrank/LostOdysseyRecomp/issues)

[简体中文](README.zh-CN.md) · [Changelog](CHANGELOG.md) · [Projects](https://github.com/users/freefrank/projects/3) · [Build from source](docs/BUILDING.md)

</div>

> [!IMPORTANT]
> **This project is still in early testing.** Opening areas and selected scenes have been tested; a complete playthrough has not. Rendering and stability issues remain. You must supply your own supported game files.

## v0.6.7 release

Published release [v0.6.7](https://github.com/freefrank/LostOdysseyRecomp/releases/tag/v0.6.7) on 2026-09-20T20:09:28Z from source `f92c24d` via Release CI [35533399325](https://github.com/freefrank/LostOdysseyRecomp/actions/runs/35533399325) as the latest public release. It adds an in-game Graphics menu Widescreen switch and expanded 21:9 resolution presets (1720×720, 2560×1080, 3440×1440, 3840×1600, 5120×2160), with closest vertical height matching when toggling aspect ratio, automatic detection for existing configurations, and synchronization with first-launch setup across 5 languages. Issue #17 is resolved and closed.

> [!WARNING]
> **Ultrawide support remains EXPERIMENTAL across diverse hardware and aspect ratio combinations.**

See the [changelog](CHANGELOG.md#v067--2026-09-20) and [development status](docs/STATUS.md) for validation limits.

## v0.6.6 release

Published release [v0.6.6](https://github.com/freefrank/LostOdysseyRecomp/releases/tag/v0.6.6) (reissued 2026-09-20 from source `c6cbd1f` via Release CI [35527543573](https://github.com/freefrank/LostOdysseyRecomp/actions/runs/35527543573)). It introduces initial native ultrawide (21:9) support (Issue #17), a shadow-map rendering repair across all aspect ratios and high internal resolutions, and Linux AppImage updater rollback-preserving cleanup.

The shadow fix repairs effective-height render-target caching and depth-only rasterization modes 4 and 5; shadows were confirmed fixed in user testing of the affected scene. Reissue packages have been verified and uploaded; the initial `c953bb5` packages are superseded, and players who downloaded the earlier build should redownload to get the fix.

See the [changelog](CHANGELOG.md#v066--2026-09-20) and [development status](docs/STATUS.md) for validation limits.

## v0.6.3 release

Published at [GitHub Release v0.6.3](https://github.com/freefrank/LostOdysseyRecomp/releases/tag/v0.6.3) on 2026-09-19T23:56:08Z. It restores bounded sampled comparison for large vertex-cache hits to reduce CPU comparison cost while keeping small vertex buffers and index-cache source validation exact. `LoVertexCacheTest` passed 3,668,957 focused checks; no release-binary performance or full-game result is claimed. It also includes the Issue #54 language-menu safety correction, Issue #53 file-I/O locking and bounded diagnostics, deterministic I/O lifetime regression coverage, and platform-native asynchronous F1 render-state archives. The Windows ZIP and Linux AppImage, plus their sidecars, passed package hash and public delivery checks. Linux native GPU, Steam Deck, AppImage runtime and broader gameplay remain pending. See the [changelog](CHANGELOG.md#v063--2026-09-19).

## v0.6.2 release

Published release: [v0.6.2](https://github.com/freefrank/LostOdysseyRecomp/releases/tag/v0.6.2). The Windows ZIP and Linux AppImage include the shader set; this release has no separate shader package. v0.6.2 packages experimental geometric motion-vector replay and the accepted main-path TAA policy. The normal TAA path uses 0.5 jitter scale, stationary motion snapping, stationary color clipping and multi-surface history with RGBA8 history at `31/33`; experimental FP16 history and moving bilinear fallback remain off. On Vulkan with an RTX 5080, the same Uhra 4K scene was accepted by the user at about 60 FPS. This is scene- and machine-limited evidence, not whole-game or cross-platform acceptance.

The candidate comparison measured 60.34/59.00 FPS against 54.61 FPS for a separate Release build and 54.57 FPS for the previous RelWithDebInfo main binary in hidden muted A-B-A-B captures without pacing. The 1080p-internal to 4K moving-camera limitation, broader scene coverage, D3D12 replay PSO follow-up, Linux native GPU and Steam Deck validation remain open.

## v0.6.1 release

Published release: [v0.6.1](https://github.com/freefrank/LostOdysseyRecomp/releases/tag/v0.6.1). It checks for updates before importing game data on Windows and Linux. A newer release opens an app