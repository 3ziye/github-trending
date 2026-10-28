# OmarchyTV

**An Omarchy-style home screen for Android TV, featuring a native Omarchy TUI Grok Bot assistant, 26 MIT themes with 4K wallpapers, a desktop link to your Omarchy PC / Mac, a native MCP server, and an Android smartphone wireless installer.**

Created by **[Marco Porro](https://www.marcoporro.it)** ([x.com/MarcoPorro](https://x.com/MarcoPorro) · [www.marcoporro.it](https://www.marcoporro.it))

Official Synchronized Repositories: **[GitHub (`github.com/piermark/omarchytv`)](https://github.com/piermark/omarchytv)** · **[GitLab (`gitlab.com/piermark/omarchytv`)](https://gitlab.com/piermark/omarchytv)**

Published: **25 October 2026 (beta)** · Version **2.12.0-beta** (`versionCode 20` — Android TV, PC/Mac Plugin & Mobile Companion) / **2.11.0-testing** (LG webOS experimental) · License **MIT**

> [!WARNING]
> **BETA SOFTWARE: THINGS MAY NOT WORK.** OmarchyTV has been tested on several devices (Sony KD-55XE9005 on Android 9,
> Google TV Streamer on Android 14, Sharp AQUOS, Noblex/Hisense on Android 11) plus the Android TV emulator. Expect rough edges, missing features on some TVs and bugs. It never roots or uninstalls
> anything, and you can always switch back to the stock home screen (see [INSTALL](launcher/docs/INSTALL.md)), but use it at your own risk.

![OmarchyTV home: Liftoff Sunset wallpaper, terminal + OMARCHY TV logo, weather, app row](docs/screenshots/home-preview.svg)

*Default theme since 2.10.2-beta: Tokyo Night with Tom Ballard's "Liftoff Sunset" wallpaper, used with permission (see [Credits](#credits-and-third-party-software)).*

| Workspace 2 · TV | Workspace 4 · PC | Workspace 5 |
|---|---|---|
| ![TV](docs/screenshots/ws2.svg) | ![PC](docs/screenshots/ws4.svg) | ![Workspace 5](docs/screenshots/ws5.svg) |
| **Logo menu** | **Screensaver (tte effects)** | **Workspace 3** |
| ![Menu](docs/screenshots/menu.svg) | ![Screensaver](docs/screenshots/screensaver.png) | ![Workspace 3](docs/screenshots/ws3.svg) |

*Screenshots from the Android TV emulator (API 28, 1920×1080, English UI). The app
tiles (Netflix, Prime Video, YouTube, CHILI, RaiPlay) are the real app icons captured on a Sony KD-55XE9005 running
OmarchyTV; see [Trademarks](#trademarks).*

---

## Release Downloads & Checksums (`v2.12.0-beta`)

Every Android APK is signed with the official OmarchyTV release certificate (`SHA-256: 90aa68d9f45e623eadfd349ab1eb66042356f95ff6347a4568c3f3a78f8ea33d`), so `adb install -r` upgrades cleanly over `2.11.0-beta` and earlier builds while keeping all user settings.

| Artifact | Downloads (GitHub & GitLab Mirrors) | Platform | Version | Size | SHA-256 |
|---|---|---|---|---|---|
| **`omarchytv-release-2.12.0-beta.apk`** | **[GitHub](https://github.com/piermark/omarchytv/releases/download/v2.12.0-beta/omarchytv-release-2.12.0-beta.apk)** · **[GitLab](https://gitlab.com/-/project/87958120/uploads/6cceb57b0e117e4607982769d2affef5/omarchytv-release-2.12.0-beta.apk)** | Android TV / Google TV (`com.omarchytv.home`, `minSdk 24`, `targetSdk 34`) | `2.12.0-omarchytv` (`versionCode 20`) | `3.8 MB` | `9dedc335fb1150afa6027f4123bd295bec8241a4c654842a6be65caff993f035` |
| **`omarchy-tv-pc-plugin-2.12.0-beta.tar.gz`** | **[GitHub](https://github.com/piermark/omarchytv/releases/download/v2.12.0-beta/omarchy-tv-pc-plugin-2.12.0-beta.tar.gz)** · **[GitLab](https://gitlab.com/-/project/87958120/uploads/b99cf1095f23c74fc75abb9cdd0d3322/omarchy-tv-pc-plugin-2.12.0-beta.tar.gz)** | Omarchy Linux / macOS (`omarchy-tv` + `omarchy-link` + `tools/`) | `2.12.0-beta` | `184 KB` | `2aef33b30e38eba6eb4355ad597bf382bb5e7210be59d7070d6b5f509765bd0c` |
| **`omarchytv-mobile-2.12.0-beta.apk`** | **[GitHub](https://github.com/piermark/omarchytv/releases/download/v2.12.0-beta/omarchytv-mobile-2.12.0-beta.apk)** · **[GitLab](https://gitlab.com/-/project/87958120/uploads/b6ff99262524aaf8186ab44906a91fdf/omarchytv-mobile-2.12.0-beta.apk)** | Android Smartphone Installer & Companion (`com.omarchytv.mobile`, `minSdk 26`, `targetSdk 34`) | `2.12.0-beta` (`versionCode 21200`) | `178 KB` | `42bb62aa6169c52afacc9b477d25f6f95fffe2eeea9f779394606e1a4e5ad0a4` |
| **`omarchytv-webos-2.11.0-testing.ipk`** | **[GitHub](https://github.com/piermark/omarchytv/releases/download/v2.11.0-testing-webos/omarchytv-webos-2.11.0-testing.ipk)** · **[GitLab](https://gitlab.com/piermark/omarchytv/-/releases)** | LG webOS TV (`com.omarchytv.webos`, experimental `testing`) | `2.11.0-testing` | `124 KB` | `04eb928640a0212cad83457ad50b502bc81da440445e33ea2eee95e6eefcc9df` |

All releases are available on both **[GitHub Releases](https://github.com/piermark/omarchytv/releases)** and **[GitLab Releases](https://gitlab.com/piermark/omarchytv/-/releases)**. Full release notes: **[RELEASE-2.12.0-beta.md](RELEASE-2.12.0-beta.md)** and **[CHANGELOG.md](CHANGELOG.md)**.

---

## What's New in `2.12.0-beta` (`versionCode 20`)

1. **Native Grok Bot · Omarchy TUI (`AskActivity`) on the TV Home Shelf:**
   - Clicking the **Grok Bot** tile (`grokbot@tv:~$ > GROK BOT [ omar