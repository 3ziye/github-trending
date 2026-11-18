# OmarchyTV

**An Omarchy-style home screen for Android TV, LG webOS and Samsung Tizen: Omarchy Pulse as the screensaver (the real sky over you, live), an arcade where your phone is the gamepad, a native Omarchy TUI Grok Bot assistant, 32 MIT themes with TV wallpapers, a desktop link to your Omarchy PC / Mac, a native MCP server, and an Android smartphone wireless installer.**

Created by **[Marco Porro](https://www.marcoporro.it)** ([x.com/MarcoPorro](https://x.com/MarcoPorro) · [www.marcoporro.it](https://www.marcoporro.it))

Official Synchronized Repositories: **[GitHub (`github.com/piermark/omarchytv`)](https://github.com/piermark/omarchytv)** · **[GitLab (`gitlab.com/piermark/omarchytv`)](https://gitlab.com/piermark/omarchytv)**

Published: **14 November 2026 (latest release: 2.20.0 — Android TV, LG webOS & Samsung Tizen)** (`versionCode 29`) · Mobile Companion **2.13.0-beta** · Cinemarchy **0.1.0-alpha** · License **MIT**

[![OmarchyTV 2.15: Omarchy Pulse on the TV, the arcade with your phone as the gamepad, games for two](docs/media/omarchytv-2.15.png)](https://github.com/piermark/omarchytv/raw/main/docs/media/omarchytv-2.15.mp4)

*OmarchyTV 2.15 in 50 seconds: click the picture for the video (MP4, 6 MB, with music). Everything new in this release is in [What's New in 2.20.0](#whats-new-in-2200-versioncode-29), and earlier in [What's New in 2.15.1](#whats-new-in-2151-versioncode-28) and [What's New in 2.15.0](#whats-new-in-2150-versioncode-27).*

> [!WARNING]
> **Beta software.** Tested on Sony BRAVIA (Android 9), Google TV Streamer (Android 14), Sharp AQUOS, Noblex/Hisense (Android 11), LG webOS and the Android TV emulator. Some features may be missing on some TVs. It never roots or uninstalls anything, and you can always switch back to your stock home screen (see [INSTALL](launcher/docs/INSTALL.md)).

![OmarchyTV 2.13.8 home on a Sony BRAVIA: Tokyo Roadster theme, Grok Bot companion, SpaceX TV pill, app row](docs/screenshots/home-sony-bravia.png)

*OmarchyTV 2.13.8 on my Sony BRAVIA: Tom Ballard's ([@tcballard](https://x.com/tcballard)) Tokyo Roadster theme and wallpaper (MIT, see [Credits](#credits-and-third-party-software)), Grok Bot companion and the SpaceX TV plugin by Simon Loffler ([@sighmon](https://x.com/sighmon)).*

**Animated wallpapers come alive when you open the launcher or press Home** (artwork and animations by [Erik Johansson](https://github.com/erikrjohansson), MIT). Click a frame to play the clip:

| Eyes Wide (Last Horizon) | Cumulus: Airship | Cumulus: Lighthouse |
|---|---|---|
| [![OmarchyTV home with the animated Eyes Wide wallpaper](docs/media/webos-home-eyes-wide-video.jpg)](https://github.com/piermark/omarchytv/raw/main/docs/media/webos-home-eyes-wide.mp4) | [![OmarchyTV home with the animated Cumulus airship](docs/media/webos-home-cumulus-airship-video.jpg)](https://github.com/piermark/omarchytv/raw/main/docs/media/webos-home-cumulus-airship.mp4) | [![OmarchyTV home with the animated Cumulus lighthouse](docs/media/webos-home-cumulus-lighthouse-video.jpg)](https://github.com/piermark/omarchytv/raw/main/docs/media/webos-home-cumulus-lighthouse.mp4) |

| Workspace 2 · TV | Workspace 4 · PC | Workspace 5 |
|---|---|---|
| ![TV](docs/screenshots/ws2.svg) | ![PC](docs/screenshots/ws4.svg) | ![Workspace 5](docs/screenshots/ws5.svg) |
| **Logo menu** | **Screensaver (tte effects)** | **Workspace 3** |
| ![Menu](docs/screenshots/menu.svg) | ![Screensaver](docs/screenshots/screensaver.png) | ![Workspace 3](docs/screenshots/ws3.svg) |

*Screenshots from the Android TV emulator (API 28, 1920×1080, English UI). The app
tiles (Netflix, Prime Video, YouTube, CHILI, RaiPlay) are the real app icons captured on a Sony KD-55XE9005 running
OmarchyTV; see [Trademarks](#trademarks).*

---

## Release Downloads & Checksums (`v2.20.0`)

I sign every Android APK with the OmarchyTV release certificate (`SHA-256: 90aa68d9f45e623eadfd349ab1eb66042356f95ff6347a4568c3f3a78f8ea33d`), so `adb install -r` upgrades over `2.15.1` and earlier and keeps your settings. All checksums are also in `SHA256SUMS` on the release.

| Artifact | Download | Platform | Version | Size | SHA-256 |
|---|---|---|---|---|---|
| **`omarchytv-release-2.20.0.apk`** | **[GitHub](https://github.com/piermark/omarchytv/releases/download/v2.20.0/omarchytv-release-2.20.0.apk)** · **[GitLab](https://gitlab.com/piermark/omarchytv/-/releases/v2.20.0)** | Android TV / Google TV / Fire OS (`com.omarchytv.home`, `minSdk 24`, `targetSdk 34`) | `2.20.0` (`versionCode 29`) | `14.8 MB` | `d05309e2b7cde2cfaff2d180cd169cb724fec689a94d26ba3733080067a8e20a` |
| **`omarchytv-webos-2.20.0-testing.ipk`** | **[GitHub](https://github.com/piermark/omarchytv/releases/download/v2.20.0/omarchytv-webos-2.20.0-testing.ipk)** · **[GitLab](https://gitlab.com/piermark/omarchytv/-/releases/v2.20.0)** | LG webOS TV (`com.omarchytv.home`, experimental) | `2.20.0` | `12.3 MB` | `7a59997bb9e718aae6686b09d0dd6955d2898e4015624552f2fce68098a18aae` |
| **`OmarchyTV-tize