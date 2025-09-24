<p align="center">
  <img src="./images/icon.png" alt="AndroidIDE" width="80" height="80"/>
</p>

<h2 align="center"><b>AndroidIDE-Rv2</b></h2>
<p align="center">
  An IDE to develop real, Gradle-based Android applications on Android devices.
<p><br>

<p align="center">
<!-- Latest release -->
<img src="https://img.shields.io/github/v/release/Mohammed-baqer-null/AndroidIDE-Rv2?include_prereleases&amp;label=latest%20release" alt="Latest release">
<!-- Build and test -->
<!-- <img src="https://github.com/Mohammed-baqer-null/AndroidIDE-Rv2/actions/workflows/asm_build.yml/badge.svg" alt="Builds and tests"> -->
<!-- Crowdin -->
<a href="https://crowdin.com/project/androidide"><img src="https://badges.crowdin.net/androidide/localized.svg" alt="Crowdin"></a>
<!-- License -->
<img src="https://img.shields.io/badge/License-GPLv3-blue.svg" alt="License"></p>

<p align="center">
  <a href="https://docs.androidide.com/">Explore the docs »</a> &nbsp; &nbsp;
</p>

<p align="center">
  <a href="https://github.com/Mohammed-baqer-null/AndroidIDE-Rv2/issues/new?labels=bug&template=BUG.yml&title=%5BBug%5D%3A+">Report a bug</a> &nbsp; &#8226; &nbsp;
  <a href="https://github.com/Mohammed-baqer-null/AndroidIDE-Rv2/issues/new?labels=feature&template=FEATURE.yml&title=%5BFeature%5D%3A+">Request a feature</a> &nbsp; &#8226; &nbsp;
  <a href="https://t.me/rv2ide">Join us on Telegram</a>
</p>


## New Features

- [x] NDK support (Only for `aarch64` android devices)
- [x] Install via shizuku (implemented by [MiyazKaori](https://github.com/MiyazKaori))
- Check out the [New Features](https://github.com/Mohammed-Baqer-null/AndroidIDE-Rv2/tree/dev/whatsnew#whats-new) implemented by [Mohammed-baqer-null](https://github.com/Mohammed-baqer-null)

## Features

- [x] Gradle support.
- [x] `JDK 11` and `JDK 17` available for use.
- [x] Terminal with necessary packages.
- [x] Custom environment variables (for Build & Terminal).
- [x] SDK Manager (Available via terminal).
- [x] API information for classes and their members (since, removed, deprecated).
- [x] Log reader (shows your app's logs in real-time)
- [ ] Language servers
    - [x] Java
    - [x] XML
    - [ ] Kotlin
- [ ] UI Designer
    - [x] Layout inflater
    - [x] Resolve resource references
    - [x] Auto-complete resource values when user edits attributes using the attribute editor
    - [x] Drag & Drop
    - [x] Visual attribute editor
    - [x] Android Widgets
- [ ] String Translator
- [ ] Asset Studio (Drawable & Icon Maker)
- [x] Git

## Installation

[<img src="https://github.com/Kunzisoft/Github-badge/raw/main/get-it-on-github.svg"
    alt="Get it on F-Droid"
    height="80">](https://github.com/Mohammed-baqer-null/AndroidIDE-Rv2/releases)

> _Please install AndroidIDE-Rv2 from trusted sources only i.e._
> - [_GitHub Releases_](https://github.com/Mohammed-baqer-null/AndroidIDE-Rv2/releases)

- Download the AndroidIDE-Rv2 APK from the mentioned trusted sources.
- Follow the
  instructions [here](https://docs.androidide.com/tutorials/get-started.html) to
  install the build tools.

## Limitations

- For working with projects in AndroidIDE, your project must use Android Gradle Plugin v7.2.0 or
  newer. Projects with older AGP must be migrated to newer versions.
- SDK Manager is already included in Android SDK and is accessible in AndroidIDE-Rv2 via its Terminal.
  But, you cannot use it to install some tools (like NDK) because those tools are not built for
  Android.
- No official NDK support because we haven't built the NDK for Android.

The app is still being developed actively. It's in beta stage and may not be stable. if you have any
issues using the app, please let us know.

## Contributing

See the [contributing guide](./CONTRIBUTING.md).

For translations, visit the [Crowdin project page](https://crowdin.com/project/androidide).

## Thanks to

- [Rosemoe](https://github.com/Rosemoe) for the
  awesome [CodeEditor](https://github.com/Rosemoe/sora-editor)
- [Termux](https://github.com/termux) for [Terminal Emulator](https://github.com/termux/termux-app)
- [Bogdan Melnychuk](https://github.com/bmelnychuk)
  for [AndroidTreeView](https://github.com/bmelnychuk/AndroidTreeView)
- [George Fraser](https://github.com/georgewfraser) for
  the [Java Language Server](https://github.com/georgewfraser/java-language-server)
- [Itsaky](https://github.com/itsaky) The original developer
  of [AndroidIDE](https://github.com/AndroidIDEOfficial/AndroidIDE.git) whose project I forked and now maintain.
  
Thanks to all the developers who have contributed to this project.

<p>This project is supported by:</p>
<p>
  <a href="https://m.do.co/c/54add371d1d7">
    <img src="https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/SVG/DO_Logo_horizontal_blue.svg" width="201px">
  </a>
</p>

## Contact Us

- [Website](https://m.androidide.com)
- [Telegram](https://t.me/rv2ide