# AMDNR — DLSS 5 Neural Rendering on AMD (OptiScaler build) — v0.3.5.2


**English** | [中文](README.zh-CN.md) | [Português](README.pt-BR.md) | [Español](README.es.md) | [العربية](README.ar.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Русский](README.ru.md) | [Polski](README.pl.md)

> **We need your support.** Join the Discord server — <https://discord.gg/AMDNR> — for
> help, bug reports and test builds; every report with a log makes the next build better.

DLSS 5 Neural Rendering running on AMD GPUs, built into OptiScaler so it works in any
Direct3D 12 game OptiScaler already hooks. On top of the neural pass: model interleave for a
large frame-rate gain, residual composition, XeSS frame generation unlocked up to 6X (up to 10X
opt-in in D3D12 games), and FSR Ray Regeneration for games that use DLSS Ray Reconstruction. Since 0.3.5,
**AMDNR Anywhere** (preview) brings Neural Rendering to games that have no upscaler of their own, through the
AMDNR Launcher, with nothing written into the game folder (see "AMDNR Anywhere").

**Discord: <https://discord.gg/AMDNR>** — support, bug reports (`#bug-report`), test
builds.

**Support the project: <https://ko-fi.com/3zinr>**

> **The danielblnc runtime is Daniel Blanco's work.** The AMD neural runtime in the `*Runtime.zip` files
> (`dlssnr_amd_pass1..3.dll`) is **DLSS-NR on AMD by Daniel Blanco (danielblnc)** -
> <https://github.com/danielblnc/DLSS-NR-on-AMD>. Copyright (c) 2026 Daniel Blanco, all rights reserved.
> AMDNR ships it unmodified, with his permission; it is not AMDNR's work. Please support his project.
> Full credits for everyone else are at the end of this page.

> **New in 0.3.5:** **AMDNR Anywhere** (preview): Neural Rendering for games that have no DLSS, XeSS or FSR 2 of
> their own - one **PLAY ANYWHERE** button in the AMDNR Launcher, nothing written into the game folder; RX 9000
> (RDNA 4) in this release (see "AMDNR Anywhere"). **Ray Regeneration has its own tab**, right after Upscaling, and
> its status lines say per card and per API what runs and why not; on RX 7000 it is, since 0.3.5.1, offered again as a preview, on by default (AMD's
> denoiser has no RDNA 3 provider, so the picture is upscaled without a denoiser; the Upscaling tab's box or
> `[FSR-RR] FfxDenoiserAllowPreRdna4=false` turns it off and the game keeps its own denoiser). **The neural pass can run after upscaling**
> (`[DlssNr] AmdPlacement=post`, Neural > Performance > Placement; the default `pre` is unchanged). **The Frame Gen
> tab says why nothing generates** and names the five steps (see the frame-generation FAQ). **Faster on RX 7000 and
> Z1 Extreme-class handhelds:** about 10 percent less network time, same picture bit for bit (the 0.3.5 module set in
> `LmxxfNrRuntime.pak`). **lmxxf 0.37 by Kien (MIT) is on by default on RX 9000:** about 20 percent less network
> time on an RX 9070 XT (experimental on the RX 9060 / 9060 XT; `[DlssNr] AmdLmxxfL37=false` turns it off). On RDNA 3
> handhelds, **FSR 4 (INT8)** is an experimental opt-in, and custom style slots now keep the whole look. Dynamic-resolution games no longer rebuild the network at every
> step, the carried edit no longer vanishes when you move on a handheld with Model interleave, Uncharted: Legacy of
> Thieves no longer crashes on RX 9000, and many more fixes. **All three files change: replace `OptiScaler.dll`,
> `LmxxfNrRuntime.dll` and `LmxxfNrRuntime.pak` together; launcher users: it updates for you.** Details:
> `CHANGELOG.md`.

> **New in 0.3.4.2 (hotfix):** the menu in Assetto Corsa: the menu key toggles once per press, clicks shorter than a
> frame are no longer lost, and the runtime chooser answers to `1` / `2` / `Enter` / `Esc`, has a title-bar X and
> closing the menu counts as Decide later. The runtime chooser no longer opens the menu by itself (one notice
> instead), the **Ray Regeneration** section of the Neural tab no longer hides - it is always there and one dim line
> says why it is not running - and the Wine / Proton text says that Ray Regeneration is a known issue there. AMDNR
> also **accepts one more danielblnc runtime layout**, so a newer danielblnc build can be driven without an AMDNR
> update. **Neural Rendering is byte-identical to 0.3.4.1 except that one accepted-layout row**
> (the neural pass, both runtimes and the pak are unchanged): coming from 0.3.4.1 or
> 0.3.4, replace `OptiScaler.dll` only; launcher users: it updates for you. Details: `CHANGELOG.md`.

> **New in 0.3.4.1 (hotfix):** Ray Regeneration is less soft on Windows (0.25 sharpening when the game sends none;
> to turn it off: Image > Sharpness, tick Override, slider 0); no false "Upscaler failed to run!" popup in Control
> Resonant; on Linux / Proton the menu works (confirmed by a player, also with frame generation on) and Ray
> Regeneration adds no default sharpening there (see "Linux / Proton"). **AMDNR Launcher 0.3.4.1**, built from your
> Discord feedback: nin