<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/readme/logo-dark.svg">
    <img src=".github/readme/logo-light.svg" alt="Overdrive" width="440">
  </picture>
</p>

<p align="center">
  <b>English</b> ·
  <a href="README.ru.md">Русский</a>
</p>

<p align="center">
  <b>Your PS5 game store.</b><br>
  Back from the dead, rebuilt from its own binary, with every line of source in the open.
</p>

<p align="center">
  <a href="https://github.com/MyLuxy/overdrive/releases/latest"><img src="https://img.shields.io/github/v/release/MyLuxy/overdrive?style=for-the-badge&label=release&labelColor=0b0b0d&color=2a2a2f" alt="Latest release" width="197"></a>
  <a href="https://github.com/MyLuxy/overdrive/releases"><img src="https://img.shields.io/github/downloads/MyLuxy/overdrive/total?style=for-the-badge&label=downloads&labelColor=0b0b0d&color=2a2a2f" alt="Downloads" width="183"></a>
  <a href="https://github.com/sponsors/MyLuxy"><img src="https://img.shields.io/badge/sponsor-%E2%9D%A4-db61a2?style=for-the-badge&logo=githubsponsors&logoColor=white&labelColor=0b0b0d" alt="Sponsor MyLuxy on GitHub" width="180"></a>
</p>

<p align="center">
  <a href="#install-in-four-steps">Install</a> ·
  <a href="#features">Features</a> ·
  <a href="#updates">Updates</a> ·
  <a href="#troubleshooting">Troubleshooting</a> ·
  <a href="#build-it-yourself">Build it yourself</a>
</p>

> [!NOTE]
> The original Overdrive project has been shut down so I decompiled the last released build,
> recovered the complete source and rebuilt it.

<p align="center">
  <img src=".github/readme/discover.jpg" alt="Overdrive's Discover page, with a featured game and the Popular now row" width="100%">
</p>
<p align="center">
  <img src=".github/readme/browse.jpg" alt="Browse library: 1,845 games with filters, sorting, scores and sizes" width="49.5%">
  <img src=".github/readme/downloads.jpg" alt="Downloads page with activity and storage for internal storage and a USB drive" width="49.5%">
</p>

## Features

- **1,800+ games** to discover, with **Top rated**, **New releases** and a featured spotlight
- **Browse the whole library** with filters, sorting, scores and download sizes at a glance
- **Downloads straight to the console**, to internal storage or any USB drive, with live speed and storage stats
- **Favorites**, **search** with an on-screen keyboard, and a **Files** page to see and clean up what's on your drives
- **13 languages**: English, Deutsch, Español, Français, Português (Brasil), Русский, Bahasa Indonesia, 日本語, 简体中文, العربية, اردو, हिन्दी, বাংলা
- **Updates itself**: a new version installs from the console, no PC needed
- Made for the controller: <kbd>L1</kbd> <kbd>R1</kbd> to switch sections, <kbd>✕</kbd> to select, <kbd>○</kbd> to go back

## Install in four steps

<p align="center">
  <img src=".github/readme/install-steps.svg" alt="1 Download Overdrive.exfat · 2 Copy it into a homebrew folder on a USB drive · 3 Plug it in: ShadowMount+ installs it · 4 Play" width="100%">
</p>

### Before you start

You need a **jailbroken PS5** running two payloads: **[ShadowMount+](https://github.com/drakmor/ShadowMountPlus)**,
which installs `.exfat` images by itself, and **[kstuff](https://github.com/EchoStretch/kstuff-lite/releases)**.
If ShadowMount+ shows its notification when the console starts, you are ready. You also need a
**USB drive** and a **PC**.

<p align="center">
  <a href="https://github.com/MyLuxy/overdrive/releases/latest/download/Overdrive.exfat"><img src="https://img.shields.io/badge/Download-Overdrive.exfat-f2f2f3?style=for-the-badge&labelColor=0b0b0d" alt="Download Overdrive.exfat" width="347"></a>
</p>

<table>
<tr>
<td width="64" align="center" valign="top"><img src=".github/readme/step-1.svg" alt="1" width="40"></td>
<td>

**Download `Overdrive.exfat`** with the button above, or from the
[latest release](https://github.com/MyLuxy/overdrive/releases/latest). It is the only file you
need. Leave it as it is: don't unzip it and don't change the `.exfat` at the end of its name.

</td>
</tr>
<tr>
<td align="center" valign="top"><img src=".github/readme/step-2.svg" alt="2" width="40"></td>
<td>

**Copy it onto a USB drive, inside a folder called `homebrew`.** Plug the drive into your PC,
create a new folder named exactly `homebrew` (all lowercase) at the top level of the drive, and
copy `Overdrive.exfat` into it:

```text
USB drive
└── homebrew
    └── Overdrive.exfat
```

The drive must be formatted as **exFAT**, which is how most drives come and what the PS5 reads.

</td>
</tr>
<tr>
<td align="center" valign="top"><img src=".github/readme/step-3.svg" alt="3" width="40"></td>
<td>

**Plug the drive into the PS5.** ShadowMount+ checks for new files every few seconds: it finds
Overdrive, mounts it and installs it, and a notification tells you when it's done. There is
nothing to click.

</td>
</tr>
<tr>
<td align="center" valign="top"><img src=".github/readme/step-4.svg" alt="4" width="40"></td>
<td