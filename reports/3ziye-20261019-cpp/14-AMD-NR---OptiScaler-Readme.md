# AMDNR — DLSS 5 Neural Rendering on AMD (OptiScaler build) — v0.3.5.6

**English** | [中文](README.zh-CN.md) | [Português](README.pt-BR.md) | [Español](README.es.md) | [العربية](README.ar.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Русский](README.ru.md) | [Polski](README.pl.md)

> **We need your support.** Join the Discord server — <https://discord.gg/AMDNR> — for
> help, bug reports and test builds; every report with a log makes the next build better.

DLSS 5 Neural Rendering running on AMD GPUs, built into OptiScaler so it works in any
Direct3D 12 game OptiScaler already hooks. On top of the neural pass: model interleave for a
large frame-rate gain, residual composition, XeSS frame generation unlocked up to 6X (up to 10X
opt-in in D3D12 games), and FSR Ray Regeneration for games that use DLSS Ray Reconstruction. Since 0.3.5,
**AMDNR Anywhere** (preview) brings Neural Rendering to games that have no upscaler of their own, through the
AMDNR Launcher, with nothing written into the game folder (see "AMDNR Anywhere"). Since 0.3.5.6 the upscaler list
also offers two experimental, opt-in choices made by other authors, **Model E** (HelixSR) and **Model L** (d4r), which
the AMDNR Launcher fetches from their own releases (see "Model E and Model L").

**Discord: <https://discord.gg/AMDNR>** — support, bug reports (`#bug-report`), test
builds.

**Support the project: <https://ko-fi.com/3zinr>**

> **The danielblnc runtime is Daniel Blanco's work.** The AMD neural runtime in the `*Runtime.zip` files
> (`dlssnr_amd_pass1..3.dll`) is **DLSS-NR on AMD by Daniel Blanco (danielblnc)** -
> <https://github.com/danielblnc/DLSS-NR-on-AMD>. Copyright (c) 2026 Daniel Blanco, all rights reserved.
> AMDNR ships it unmodified, with his permission; it is not AMDNR's work. Please support his project.
> Full credits for everyone else are at the end of this page.

> **New in 0.3.5.6** (2026-10-17, release Alpha0.3.5.6, with AMDNR Launcher 0.3.5.25):
> - **Two new upscaler choices, experimental and opt-in:** **Model E** (HelixSR by lonewolf0622) and **Model L** (d4r
>   by countervolts), fetched by the launcher from their authors' own releases when you choose them. AMDNR does not
>   host or ship their files or NVIDIA's. Model L is RX 9070 / RX 9070 XT only and runs with the lmxxf runtime or with
>   Neural Rendering off; danielblnc's runtime pairs with Model E. Read "Model E and Model L" before you enable them.
> - **Full Model Look is the default NR style:** a fuller look on both runtimes, run after upscaling on the cards that
>   can afford it - the cost gate and the TDR guard move it back before upscaling where they must, and say so. Picking
>   a look in NR style also sets its Neural placement and Full network, and the menu tells you when your own placement
>   setting holds the look back.
> - **Extra detail on faces**, always on, on both runtimes (`[DlssNr] AmdFaceDetail=false` turns it off).
> - **Less ghosting with lmxxf:** trails behind moving objects are shorter, before and after upscaling, and the flash
>   after a scene cut is about half as strong. Ghosting is reduced, not gone.
> - **RX 7000 and handhelds:** Neural Rendering now runs one network size smaller by default (lmxxf Fast mode), which
>   costs less time per frame. `[DlssNr] AmdLmxxfFastMode=false` turns it off; RX 9000 keeps it off.
> - **New and renamed controls:** Game exposure (Auto / On / Off), Anti-halo (formerly Halo protection), and on
>   danielblnc **Refine passes** (passes 2 and 3 run one network size smaller). **NR resolution** now goes up to 200% on
>   both runtimes.
> - **The menu shows only what your runtime can use:** a control a runtime cannot run is hidden on that runtime (its
>   ini key keeps working), and the runtime entry names the lmxxf version that really runs (e.g. `lmxxf 0.41`).
> - **Fixes:** danielblnc's false "timeouts" (tested in Silent Hill 2) - a wait that gives up no longer turns Neural
>   Rendering off, the text claiming the driver reset the GPU is gone (there was no reset), and the "runtime failed"
>   note is written only after a real failure. FSR 3 / FSR 4 should no longer drop back to FSR 2.1.2 when another
>   upscaler choice fails or is not ready: your own FSR pick is kept. XeFG frame generation's memory is counted
>   correctly (the 6X setting included).
> - **Replace every file of the zip together** (`OptiScaler.dll` and `LmxxfNrRuntime.dll` must come from the same
>   release); launcher users: it updates for you. What is still open: "Known limits (0.3.5.6)". Details: `CHANGELOG.md`.

> **Between 0.3.5 and 0.3.5.6** (0.3.5.1 to 0.3.5.5R4): danielblnc 0.6.0 is driven and is now the recommended
> danielblnc runtime (it also runs on RX 6000, with AMD's HIP SDK installed); lmxxf 0.41 by Kien (MIT) is the default
> set on RX 9000; the NVIDIA look (the default NR style from 0.3.5.3 to 0.3.5.5R4); a freeze guard that lowers or stops
> NR after a counted GP