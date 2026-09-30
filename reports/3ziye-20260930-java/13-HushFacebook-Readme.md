![Hushfacebook. Keep the people. Cut the noise.](assets/readme-hero.png)

<p align="center">
  <a href="https://github.com/SysAdminDoc/Hushfacebook/releases"><img src="https://img.shields.io/badge/version-0.5.0-0866FF" alt="Version 0.5.0"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-GPL--3.0-blue" alt="License GPL-3.0"></a>
  <img src="https://img.shields.io/badge/platform-Android%2011%2B-3DDC84" alt="Platform Android 11+">
  <img src="https://img.shields.io/badge/Facebook-580.0.0.51.74-0866FF" alt="Facebook 580.0.0.51.74">
  <img src="https://img.shields.io/badge/for-Morphe%20Manager%201.32.0%2B-8A2BE2" alt="For Morphe Manager 1.32.0 or newer">
</p>

<p align="center">
  <a href="https://ko-fi.com/X8K126YVER">
    <img height="42" src="https://storage.ko-fi.com/cdn/kofi2.png?v=3" alt="Buy me a coffee on Ko-fi" />
  </a>
</p>

# Hushfacebook

Hushfacebook is a Morphe patch bundle for Android that takes the clutter out of Facebook and puts useful controls back in your hands.

The latest release is [v0.5.0](https://github.com/SysAdminDoc/Hushfacebook/releases/tag/v0.5.0), with 51 patches. It includes all changes since v0.4.0, among them eight new patches such as Hide the Reels tab dot, Keep the reel speed and Hold a reel for 2x, and the Suggested for you groups row hidden again, as the [changelog](CHANGELOG.md) describes.

[Add to Morphe](https://morphe.software/add-source?github=SysAdminDoc%2FHushfacebook) | [Download a release](https://github.com/SysAdminDoc/Hushfacebook/releases/latest) | [Browse the patches](#patches)

## Why use it

- **A quieter feed.** Sponsored and suggested posts disappear, along with ads in Stories, Reels, and Watch.
- **Less tracking.** Selected ad telemetry and background ad downloads stop. Common trackers also come off links you open or share.
- **Media you can keep.** Save videos from stories, Reels, your feed and Watch at the best quality Facebook streams, or cap them at a lower one to save space. A save shows its progress and you can cancel it.
- **Controls that recover.** Every runtime feature has a switch. Pause mode, automatic safe mode, settings backups, and privacy-filtered diagnostics help when Facebook changes.

The project brings the Facebook patches from Morphe sources into one maintained bundle. Most started with [Andrew Liang's patches](https://github.com/andrewliang25/morphe-patches) and were rewritten here with fixes. The feed filter also removes promoted posts using the approach from [FroggoMorphePatches](https://github.com/SapitoSucio/FroggoMorphePatches). Its build, settings screen, and release checks share a foundation with the sister project [Hushfeed](https://github.com/SysAdminDoc/hushfeed). See [Where the patches come from](#where-the-patches-come-from) for the full provenance.

This project has no connection to Meta or to the Morphe project. Neither endorses it, and neither wrote it.

## Install

1. Install [Morphe Manager](https://github.com/MorpheApp/morphe-manager) 1.32.0 or newer.
2. Add Hushfacebook as a patch source: https://morphe.software/add-source?github=SysAdminDoc%2FHushfacebook
3. Get Facebook 580.0.0.51.74 from [APKMirror](https://www.apkmirror.com/apk/facebook-2/facebook/) and take the bundle labelled (arm64-v8a) (240-640dpi) (Android 11+), a .apkm file. That's build 475019344, the one these patches are checked against. APKMirror has several other arm64-v8a builds of the same version, and Morphe Manager warns about those ([Unsupported Version](#unsupported-version) explains why). Facebook 577.0.0.50.72 works too, in its (arm64-v8a) (360-480dpi) (Android 11+) bundle.
4. In Morphe Manager, pick that file, keep the default patch selection or change it, and patch.

There are 51 patches for `com.facebook.katana`. They're checked against the arm64-v8a builds for Android 11 and newer, and that's the only range Hushfacebook supports. Meta's builds for Android 9 (arm64-v8a) and Android 8 (armeabi-v7a) keep all of their code except a small startup part in a compressed archive, which the patcher can't read, so not one of the patches applies to them.

Facebook releases a new version about once a week, and each one renames most of its code. Every patch here finds what it changes by names Facebook keeps (its GraphQL model classes, log strings, enum names, manifest components) rather than by the names that change, which is why most of them carry over from one build to the next. When one doesn't, patching stops with a message naming what it couldn't find, instead of producing an app that quietly does nothing. Four patches work down a list of separate targets instead: Block background ad prefetch, Block ad telemetry, Disable Audience Network and Hide suggested and promoted posts. They stop only when a build has none of the list. If it has some, they apply to what's there and name each missing target in the patch log. Facebook 580 dropped six of the feed units the suggested posts patch looks for, so patching 580 lists those six. Pl