# OmarchyTV

**An Omarchy-style home screen for Android TV, featuring a native Omarchy TUI Grok Bot assistant, 32 MIT themes with TV wallpapers, a desktop link to your Omarchy PC / Mac, a native MCP server, and an Android smartphone wireless installer.**

Created by **[Marco Porro](https://www.marcoporro.it)** ([x.com/MarcoPorro](https://x.com/MarcoPorro) · [www.marcoporro.it](https://www.marcoporro.it))

Official Synchronized Repositories: **[GitHub (`github.com/piermark/omarchytv`)](https://github.com/piermark/omarchytv)** · **[GitLab (`gitlab.com/piermark/omarchytv`)](https://gitlab.com/piermark/omarchytv)**

Published: **2 November 2026 (latest release: LG webOS & Samsung Tizen 2.13.11)** · Version **2.13.8** (`versionCode 25` — Android TV) / **2.13.11** (LG webOS) & **2.13.11** (Samsung Tizen), experimental · PC/Mac Plugin & Mobile Companion downloads **2.13.0-beta** (latest published) · Cinemarchy **0.1.0-alpha** · License **MIT**

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

## Release Downloads & Checksums (`v2.13.0-beta`, pre-release)

I sign every Android APK with the OmarchyTV release certificate (`SHA-256: 90aa68d9f45e623eadfd349ab1eb66042356f95ff6347a4568c3f3a78f8ea33d`), so `adb install -r` upgrades over `2.12.0-beta` and keeps your settings. All checksums are also in `SHA256SUMS` on the release.

| Artifact | Download | Platform | Version | Size | SHA-256 |
|---|---|---|---|---|---|
| **`omarchytv-release-2.13.8.apk`** | **[GitHub](https://github.com/piermark/omarchytv/releases/download/v2.13.8/omarchytv-release-2.13.8.apk)** · **[GitLab](https://gitlab.com/piermark/omarchytv/-/releases/v2.13.8)** | Android TV / Google TV / Fire OS (`com.omarchytv.home`, `minSdk 24`, `targetSdk 34`) | `2.13.8` (`versionCode 25`) | `8.3 MB` | `7511649fba969b2f8127d45dcf00ceb1011812340780842b11892a733dec1bc2` |
| **`omarchytv-webos-2.13.11-testing.ipk`** | **[GitHub](https://github.com/piermark/omarchytv/releases/download/v2.13.11/omarchytv-webos-2.13.11-testing.ipk)** · **[GitLab](https://gitlab.com/piermark/omarchytv/-/releases/v2.13.11)** | LG webOS TV (`com.omarchytv.home`, experimental) | `2.13.11` | `6.2 MB` | `b8f5d9eb263ffe35ad2ce35d03f6c6662ed02a1bd738b7569c3a01b60cab13e9` |
| **`OmarchyTV-tizen-2.13.11-unsigned.wgt`** | **[GitHub](https://github.com/piermark/omarchytv/releases/download/v2.13.11/OmarchyTV-tizen-2.13.11-unsigned.wgt)** · **[GitLab](https://gitlab.com/piermark/omarchytv/-/releases/v2.13.11)** | Samsung Tizen TV (unsigned testing build, sign it with your own Samsung certificate in Tizen Studio; see [INSTALL-TIZEN.md](tizen/INSTALL-TIZEN.md)) | `2.13.11` | `6.2 MB` | `5916dd07d8e20ec1fa78dd8f927dc63283d2899257a27c0eca4a91c79a391174` |
| **`omarchytv-mobile-2.13.0-beta.apk`** | **[Git