<div align="center">

# Silent Hill: Downpour — PC Port (DownpourRecomp)

### Play *Silent Hill: Downpour* natively on Windows, in 1080p, with keyboard + mouse — no emulator required.

[![Latest release](https://img.shields.io/github/v/release/LittleBitUA/DownpourRecomp?style=for-the-badge&label=Download&color=blue)](https://github.com/LittleBitUA/DownpourRecomp/releases/latest)
[![Total downloads](https://img.shields.io/github/downloads/LittleBitUA/DownpourRecomp/latest/total?style=for-the-badge&color=brightgreen)](https://github.com/LittleBitUA/DownpourRecomp/releases)
[![License](https://img.shields.io/github/license/LittleBitUA/DownpourRecomp?style=for-the-badge&color=lightgrey)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%2010%2F11-0078D6?style=for-the-badge&logo=windows)](https://github.com/LittleBitUA/DownpourRecomp/releases/latest)
[![Stars](https://img.shields.io/github/stars/LittleBitUA/DownpourRecomp?style=for-the-badge&color=yellow)](https://github.com/LittleBitUA/DownpourRecomp/stargazers)

![Murphy close-up — Silent Hill: Downpour running natively on PC](docs/screenshots/murphy-closeup.png)

## [⬇  Download v1.1.6 for Windows](https://github.com/LittleBitUA/DownpourRecomp/releases/latest)

</div>

---

> [!NOTE]
> **v1.1.6 ships today** as a critical hotfix on three fronts. **(1) Pre-update save backup** — after a community report of save-data loss during the v1.1.4 → v1.1.5 auto-update (root cause not pinned down; our PowerShell update script provably never deletes user data, but one user lost everything anyway), every auto-update now snapshots `user/` + `downpour.toml` + `launcher.ini` into a zip in `%TEMP%` BEFORE applying the new binaries. Worst case, you can hand-restore from `%TEMP%\dpr_user_backup_v<your-version>.zip`. **(2) Use Raw Input toggle** — new Mouse-tab checkbox lets you fall back to the v1.1.1 `WM_MOUSEMOVE` + Windows-pointer-ballistics path. High-DPI gaming mice (16k+ DPI) where the raw-input path felt worse after every cvar tuning attempt can recover the v1.1.1 feel by unticking this. **(3) Launcher sliders** — Mouse Sensitivity, Smoothing, Acceleration Curve, Stick Decay, Raw Input Scale, Stick Scale and other ranged numeric fields now have a draggable trackbar next to the numeric edit field — like every other modern game's mouse settings.
>
> If you're already on v1.1.x: launch `PlayDownpour.exe` and click the pill banner — v1.1.6 installs in place. The backup safety net activates automatically.
>
> **Previously: v1.1.5** — cosmetic title fix. The Win11 taskbar / Alt-Tab caption kept saying "v1.0" through every release because the title string was hardcoded at v1.0 ship time. v1.1.5 composes the title dynamically from `kLauncherVersion` so every future release auto-updates the title everywhere.
>
> **Previously: v1.1.4** — real root-cause fix for the v1.1.2-era "mouse very slow" reports. The SDK had a hardcoded `kBaseScale = 1500` multiplier that combined with the raw-input scale to saturate the controller stick on sub-millimetre mouse motion — which is why setting `mnk_sensitivity` from 0.6 → 6.0 produced zero observable change (the stick was already capped at int16 max regardless). v1.1.4 replaces the constant with a new tunable cvar `mnk_stick_scale` (default `150`, 10× lower), and tunes `mnk_raw_input_scale` default `0.5 → 0.20` to compensate. Sensitivity finally does what users expect: 1mm of mouse = ~5% stick, 1cm = ~50%, 3cm+ = saturation.
>
> **Previously: v1.1.3 ships today** as a mouse-calibration hotfix on v1.1.2. The hardcoded raw-input divider in v1.1.2 was too aggressive for default Windows pointer settings (pointer ballistics was inflating WM_MOUSEMOVE deltas more than expected). v1.1.3 exposes the magnitude as a tunable cvar `mnk_raw_input_scale` (default 0.5, surfaced in launcher Settings → Mouse) so each user can dial mouselook to their preferred feel.
>
> If you're already on v1.1.x, launch `PlayDownpour.exe` and click the pill banner — v1.1.3 installs in place. If mouselook still feels off after upgrading, open Settings → Mouse → "Raw Input Scale" and adjust (lower = slower, higher = faster).
>
> **Previously: v1.1.2 ships today.** Community-feedback follow-up: WM_INPUT raw-mouse plumbing in the SDK (mouselook now feels native, not stick-emulator-tier), VSync no longer silently overridden by the tearing swap-chain path on NVIDIA setups, and fresh installs on < 8 GiB VRAM GPUs default to 1x SSAA instead of 2x so RTX 3050 / Steam Deck / Iris Xe installs don't slideshow on first boot. Tested against the **USA** and **Europe** Xbox 360 releases of Silent Hill: Downpour (title id `4B4E0823`, base XEX hash `7A3D5809776EE6AB`).
>
> If you're already on v1.1.x (or v1.0), just launch `PlayDownpour.exe` — the update banner will appear at the top of the window. Click it; the new build is installed in place. Your saves, settings, and warm shader cache are preserved.

> [!TIP]
> ## 🐭 Mouse tuning guide
>
> If mouselook feels too slow, too fa