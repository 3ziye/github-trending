<p align="center">
  <a href="https://github.com/GeneralZyonix/morphe-download-helper/releases">
    <img src="docs/branding/readme-banner-patch-pass-current.png" alt="Morphe Download Helper — find the original APK and hand it to Morphe" width="100%">
  </a>
</p>

<p align="center">
  <a href="https://github.com/GeneralZyonix/morphe-download-helper/releases"><img src="https://img.shields.io/github/v/release/GeneralZyonix/morphe-download-helper?label=release" alt="Latest release"></a>
  <a href="https://github.com/GeneralZyonix/morphe-download-helper/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT license"></a>
  <img src="https://img.shields.io/badge/Android-6.0%2B-3ddc84.svg" alt="Android 6.0+">
  <img src="https://img.shields.io/badge/analytics-none-22d3ee.svg" alt="No analytics">
</p>

**Morphe Download Helper** is an unofficial Android helper that finds the original APK
[Morphe Manager](https://github.com/MorpheApp/morphe-manager) needs, verifies that it matches
the requested package/version/build, and hands it back through Morphe's open
`DOWNLOAD_ORIGINAL_APK` intent contract.

It is a downloader, not a patcher. It never installs, modifies, or uploads an app on its own.

> **Unofficial:** this project is not affiliated with, endorsed by, or maintained by the
> Morphe project. Morphe ships no helper of its own and does not endorse any helper.

## Why use it?

- **Exact-build matching.** The helper validates package name, version name, version code,
  ABI, and archive type before handing a file to Morphe.
- **Many sources, one flow.** Morphe's resolver link, APKMirror, APKPure, APKCube,
  Uptodown, F-Droid, Aptoide, Appteka, and GitHub releases are tried in your chosen order.
- **Patch discovery.** Search an app on the Patches tab to see which community patch
  sources support it, then add one through Morphe's own confirmation.
- **Fast source resolution.** Parallel metadata checks, APKCube no-match preflight,
  APKPure endpoint racing, and a short-lived not-found cache cut the usual waiting.
- **Repeat requests are instant.** An exact repeat request is served from the helper's
  validated local cache after rechecking package/version/build.
- **Fast large downloads.** Multi-connection downloading is on by default for compatible
  servers and files of 5 MB or more.
- **Transparent failures.** Every source shows a status, a reason, and how long it took.
- **Private by default.** No analytics, no accounts, and logs stay on your device.

## Download

Grab one of the two current builds from the
[Releases page](https://github.com/GeneralZyonix/morphe-download-helper/releases):

> **3.3.0 is the latest stable release.** It adds manual APK import,
> mobile-data controls, file details, a configurable update interval, Dutch,
> and the APKMirror source fixes from the 3.3.0 release candidates.

> **Important: one-time reinstall for 3.3.0.** Builds before 3.3.0-rc.3 were
> signed with temporary CI debug keys. Export your settings, uninstall the
> helper once, then install 3.3.0. Full instructions: [SIGNING.md](SIGNING.md).

| Build | Launcher icon | Best for |
| --- | --- | --- |
| **Icon** - `MorpheDownloadHelper-v3.3.0-universal.apk` | Always shown | Normal use. The icon appears immediately after installation. There is no hide toggle. |
| **No-icon** - `MorpheDownloadHelper-v3.3.0-universal-noicon.apk` | Never shown | A clean app drawer. Open the helper from Morphe or Android Settings → Apps → Morphe Download Helper → Open. |

Both builds have the same package name, version, signing key, and features. Install one or
the other, not both. The in-app updater stays on the build you installed. When switching
from the icon build to the no-icon build, do a fresh install or remove the old home-screen
shortcut if your launcher keeps it.

> Release APKs are signed with the Android debug key so they can be sideloaded, and the
> release build is non-debuggable. A proper release keystore can be added later for
> Play Store-style signing continuity.

## Screenshots

| Home | Downloads | Settings |
| --- | --- | --- |
| ![Home](docs/screenshots/main-3.0.0.png) | ![Downloads](docs/screenshots/download-3.0.0.png) | ![Settings](docs/screenshots/settings-general-3.0.0.png) |

See the **[settings guide with screenshots](docs/SETTINGS.md)** for every section and what
each option does. The **[Patches tab guide](docs/PATCHES.md)** explains community source
discovery and its network requirements.

## Setup

New to the helper? Follow the **[illustrated setup guide](GUIDE.md)**. In short:

1. Install the icon or no-icon APK.
2. Open Morphe → **Settings** → **Files** → **APK download helper**.
3. Turn on **Morphe Download Helper** and confirm **Trust**.
4. Optionally enable **Open helper right away**.
5. Pick an app in Morphe and choose **Help me find an APK** or **Use a helper app**.

The in-app **Visual guide** and **Help** buttons repeat these steps with screenshots.

## How it works

1. Morphe sen