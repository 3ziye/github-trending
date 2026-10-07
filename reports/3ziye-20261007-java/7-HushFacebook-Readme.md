![Hushfacebook. Keep the people. Cut the noise.](assets/readme-hero.png)

<p align="center">
  <a href="https://github.com/SysAdminDoc/Hushfacebook/releases"><img src="https://img.shields.io/badge/version-0.7.2-0866FF" alt="Version 0.7.2"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-GPL--3.0-blue" alt="License GPL-3.0"></a>
  <img src="https://img.shields.io/badge/platform-Android%2011%2B-3DDC84" alt="Platform Android 11+">
  <img src="https://img.shields.io/badge/Facebook-581.0.0.45.58-0866FF" alt="Facebook 581.0.0.45.58">
  <img src="https://img.shields.io/badge/for-Morphe%20Manager%201.34.0%2B-8A2BE2" alt="For Morphe Manager 1.34.0 or newer">
</p>

<p align="center">
  <a href="https://ko-fi.com/X8K126YVER">
    <img height="42" src="https://storage.ko-fi.com/cdn/kofi2.png?v=3" alt="Buy me a coffee on Ko-fi" />
  </a>
</p>

# Hushfacebook

Hushfacebook is a Morphe patch bundle for Android that takes the clutter out of Facebook and puts useful controls back in your hands.

The latest release is [v0.7.2](https://github.com/SysAdminDoc/Hushfacebook/releases/tag/v0.7.2), with 70 patches. It includes all changes since v0.7.1, among them View profile on every Marketplace seller, picture-in-picture for Reels, a switch for each tab in Hide tabs and support for 581's 32-bit build, as the [changelog](CHANGELOG.md) describes.

[Add to Morphe](https://morphe.software/add-source?github=SysAdminDoc%2FHushfacebook) | [Download a release](https://github.com/SysAdminDoc/Hushfacebook/releases/latest) | [Browse the patches](#patches)

## Why use it

- **A quieter feed.** Sponsored and suggested posts disappear, along with ads in Stories, Reels, and Watch.
- **Less tracking.** Selected ad telemetry and background ad downloads stop. Common trackers also come off links you open or share.
- **Media you can keep.** Save videos from stories, Reels, your feed and Watch at the best quality Facebook streams, or cap them at a lower one to save space. Photos save at the biggest size Facebook sends, even where the poster turned saving off. A save shows its progress and you can cancel it.
- **Controls that recover.** Every runtime feature has a switch. Pause mode, automatic safe mode, settings backups, and privacy-filtered diagnostics help when Facebook changes.

The project brings the Facebook patches from Morphe sources into one maintained bundle. Most started with [Andrew Liang's patches](https://github.com/andrewliang25/morphe-patches) and were rewritten here with fixes. The feed filter also removes promoted posts using the approach from [FroggoMorphePatches](https://github.com/SapitoSucio/FroggoMorphePatches). Its build, settings screen, and release checks share a foundation with the sister project [Hushfeed](https://github.com/SysAdminDoc/hushfeed). See [Where the patches come from](#where-the-patches-come-from) for the full provenance.

This project has no connection to Meta or to the Morphe project. Neither endorses it, and neither wrote it.

## Install

1. Install [Morphe Manager](https://github.com/MorpheApp/morphe-manager) 1.34.0 or newer.
2. Add Hushfacebook as a patch source: https://morphe.software/add-source?github=SysAdminDoc%2FHushfacebook
3. Get Facebook 581.0.0.45.58 from [APKMirror](https://www.apkmirror.com/apk/facebook-2/facebook/) and take the bundle labelled (arm64-v8a) (320-640dpi) (Android 11+), a .apkm file. That's build 475215365, the one these patches are checked against. On a phone with a 32-bit processor, take the (armeabi-v7a) (320dpi) (Android 11+) bundle with build number 475215364 instead. APKMirror lists three of those, so check the number. APKMirror has several other arm64-v8a builds of the same version, and Morphe Manager warns about those ([Unsupported Version](#unsupported-version) explains why). Facebook 580.0.0.51.74 works too, in its (arm64-v8a) (240-640dpi) (Android 11+) bundle, and so does 577.0.0.50.72 in its (arm64-v8a) (360-480dpi) (Android 11+) bundle.
4. In Morphe Manager, tap **Select other apps**, then **Open APK file**, and choose that file. To review the selection first, turn on **Settings → Advanced → Expert mode** before opening the file. Without Expert mode, Manager starts patching with its saved or recommended selection.
5. In Expert mode, open the **Hushfacebook** tab and choose its patches. Check the selected count on every other source tab too. If you added another Facebook patch source, [check for overlapping patches](#patching-stops-on-one-patch) before tapping **Patch**. Android may ask for file access when you open Manager's file browser.

There are 79 patches for `com.facebook.katana`. They're checked against the arm64-v8a builds for Android 11 and newer, and since 581 against the 32-bit armeabi-v7a build for Android 11 and newer too. That's the range Hushfacebook supports. Meta's builds for Android 9 (arm64-v8a) and Android 8 (armeabi-v7a), and every 32-bit build of 580, keep all of their code except a small startup part in a compressed archiv