# Morphe Download Helper

<p align="center">
  <img src="docs/icon.png" alt="Morphe Download Helper app icon" width="150">
</p>

An unofficial Android helper app that downloads the original APK requested by
[Morphe Manager](https://github.com/MorpheApp/morphe-manager) and hands it back through
Morphe's open `DOWNLOAD_ORIGINAL_APK` intent contract.

> **Unofficial:** this project is not affiliated with, endorsed by, or maintained by the
> Morphe project. Morphe ships no helper of its own and does not endorse any helper.

## Setup Guide

New to the helper? Follow the **[illustrated setup guide](GUIDE.md)** to enable it in Morphe,
trust it, and optionally make Morphe open it automatically.

## Report an issue

Found a bug or want a feature? Use the issue forms:

- [Report a bug](https://github.com/GeneralZyonix/morphe-download-helper/issues/new?template=bug_report.yml)
- [Request a feature](https://github.com/GeneralZyonix/morphe-download-helper/issues/new?template=feature_request.yml)

Please include:

- Helper version
- Android version and device
- Morphe version
- The app and version being patched
- The helper log if possible — open the helper and tap **Share log**, then attach
  `helper.log` to the issue

## Features

- Receives the package, version, version codes, file type, ABIs, and fallback URL from Morphe.
- Follows the same resolver link Morphe's own download dialog uses.
- Falls back to APKMirror, APKPure, F-Droid, Aptoide, and Appteka for SnapTube.
- Uses APKPure's numeric `versionCode` endpoint, so the exact requested build is downloaded
  instead of the latest version.
- Supports APK, APKM, APKS, and XAPK when Morphe allows split archives.
- Opens Uptodown or APKPure in an inline WebView when a site needs a browser check.
- Returns a `content://` URI with read permission so Morphe can validate and use the file.
- Rejects downloaded APKs whose package or version does not match the request.
- Shows a dark, modern UI with a source list and clear limitations.
- Shows per-source failure details and offers **Retry all sources**, **Retry failed sources**, **Copy details**, and the same **Download sources** manager used on the main screen.
- Uses GitHub automatically: immediately when Morphe's resolver points to a release, or as
  the final fallback when normal APK sources fail. There is no separate GitHub button.
- Remembers successful GitHub repositories, and lets you pin a repository to a
  package with an optional asset filter and **Try this repo first**.
- Keeps a structured, human-readable diagnostic log that can be shared from the app.
- Built-in update checker with a changelog screen: notify me, or install silently through
  Shizuku. Forks that use a different package name are supported with a configurable
  manager package, with an optional battery-optimization exemption.
- Optional **VirusTotal hash check** before handing an APK to Morphe. Hash lookup is the
  default; uploading unknown files, always uploading, or falling back to upload when the
  lookup quota is exceeded are separate opt-in settings.
- Settings for the download folder, retention, source order, and individual sources.
- Saves downloaded APKs to `Downloads/Morphe Helper` by default on Android 10+, with
  internal, external, and custom-folder options.
- Appteka is limited to SnapTube by default and carries a hazard warning. It is not
  recommended for other apps because Appteka hosts modded APKs.

## Screenshots

| Launcher | Setup | Download |
| --- | --- | --- |
| ![Launcher screen](docs/screenshots/main-v1.4.png) | ![Helper setup](docs/screenshots/setup-v1.4.png) | ![Download screen](docs/screenshots/download-v1.4.png) |

## Download

Grab the latest universal APK from the
[Releases page](https://github.com/GeneralZyonix/morphe-download-helper/releases).

The app is written in Java and contains no native libraries, so **one universal APK works on
all CPU architectures** (arm64-v8a, armeabi-v7a, x86, x86_64) and on **Android 6.0+**
(minSdk 23). Separate per-ABI APKs are not needed.

> Release APKs are currently signed with the Android debug key so they can be sideloaded.
> A proper release keystore can be added later for Play Store-style signing continuity.

## How it works

Morphe sends an intent with the action
`app.morphe.manager.action.DOWNLOAD_ORIGINAL_APK`. The helper:

1. Reads the request extras, including the package, version, numeric version codes, ABIs,
   file type, and fallback URL.
2. If a numeric `versionCode` is available, tries APKPure's direct endpoint first, then its API.
3. If APKPure does not have the build, asks Morphe's resolver API for the page Morphe would show.
4. Tries the patch bundle's fallback URL, then APKMirror by package and version.
5. Falls back to APKPure, F-Droid, Aptoide, and Appteka (SnapTube only by default).
6. If a source needs a browser check, opens it in an inline WebView and captures the final
   download link. APKPure's WebView is the last resort.
7. Returns `RESULT_OK`, a `content: