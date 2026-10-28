![HushGram. Keep the moments. Cut the noise.](assets/readme-hero.png)

<p align="center">
  <img src="https://img.shields.io/badge/version-0.0.17-E1306C" alt="Version 0.0.17">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-GPL--3.0-blue" alt="License GPL-3.0"></a>
  <img src="https://img.shields.io/badge/platform-Android%209%2B-3DDC84" alt="Platform Android 9+">
  <img src="https://img.shields.io/badge/Instagram-453.0.0.55.79-E1306C" alt="Instagram 453.0.0.55.79">
  <img src="https://img.shields.io/badge/for-Morphe%20Manager%202.2.0%2B-8A2BE2" alt="For Morphe Manager 2.2.0 or newer">
</p>

<p align="center">
  <a href="https://ko-fi.com/X8K126YVER">
    <img height="42" src="https://storage.ko-fi.com/cdn/kofi2.png?v=3" alt="Buy me a coffee on Ko-fi" />
  </a>
</p>

<p align="center">
  <sub><em>If HushGram makes Instagram better for you, a coffee helps me keep testing patches and maintaining them as Instagram changes.</em></sub>
</p>

# <img src="assets/icon.png" width="36" alt=""> HushGram

HushGram is a set of [Morphe](https://morphe.software) patches for Instagram on Android. You bring the Instagram APK, Morphe Manager patches it on your phone, and you get an Instagram with a settings screen full of switches the stock app doesn't have. Hide ads, suggested posts and Meta AI. Strip tracking tags from the links you share. Watch stories and lives without landing on the viewer list. Save reels, stories, photos and voice messages, lock your chats, rearrange the tab bar and a lot more.

Most switches start off, so a freshly patched Instagram looks like Instagram until you turn something on. It's the Instagram member of a small family. [Hushfacebook](https://github.com/SysAdminDoc/Hushfacebook) does the same job for Facebook, and HushGram is built on its foundation.

The latest release is [v0.0.16](https://github.com/SysAdminDoc/HushGram/releases/tag/v0.0.16), with 117 patches. Add it to Morphe Manager with [this link](https://morphe.software/add-source?github=SysAdminDoc%2FHushGram).

The source on main is HushGram v0.0.17. It hasn't been released yet.

What changed in each version is in the [changelog](CHANGELOG.md).

This project has no connection to Meta or to the Morphe project. Neither endorses it, and neither wrote it.

## Install

1. Install [Morphe Manager](https://github.com/MorpheApp/morphe-manager) 2.2.0 or newer.
2. Add HushGram as a patch source by opening [this link](https://morphe.software/add-source?github=SysAdminDoc%2FHushGram) on your phone. Or in Manager open **Sources**, tap **+**, choose **Remote** and enter `github.com/SysAdminDoc/HushGram`. Use HushGram as your only Instagram source, since mixing in another one can stop patching.
3. Get Instagram 453.0.0.55.79 from APKMirror. Take [the bundle labelled (arm64-v8a) (480-640dpi) (Android 9.0+), build 385914283](https://www.apkmirror.com/apk/instagram/instagram-instagram/instagram-453-0-0-55-79-release/). The version's other builds work too (see [Supported Instagram builds](#supported-instagram-builds)).
4. Uninstall the Instagram you got from the Play Store. The patched app is signed with your own key, so Android won't install it over Meta's. Uninstalling signs you out, so have your password and two-factor codes ready. On a rooted phone, Manager's Root Mount can lay HushGram over the Play Store app instead, and you stay signed in.
5. In Morphe Manager, pick the Instagram file, keep the default patch selection or change it, and patch.
6. Open HushGram settings and turn on what you want. It's at the top of Instagram's Settings and activity. A long press on the Instagram logo at the top of your feed opens it too.

Prefer a local source? Download the `.mpp` file from the [latest release](https://github.com/SysAdminDoc/HushGram/releases/latest) and add it through **Sources > + > Local**. It won't update itself, and it's a patch bundle, not an Instagram APK.

When a patch can't find its target in your Instagram file, patching stops with a message saying what's missing instead of handing you an app that quietly does nothing. Please report a stop like that.

## Before you sign in

> [!WARNING]
> Meta's [Terms of Use](https://help.instagram.com/581066165581870) don't allow modified versions of its apps, and Meta can disable accounts that break them. Nobody outside Meta knows what gets an account suspended, so nobody can promise yours won't be.
>
> - **Assume Meta can tell.** A patched Instagram has a different signing certificate, and Instagram 450 carries Play Integrity and Keystore attestation code. `Restore trust on re-signed builds` keeps parts of the app working on a re-signed build, but it doesn't make the APK Meta-signed.
> - **Try a spare account first** if you'd rather not put the one you care about on the line. People whose accounts were suspended on patched Instagram often describe a new or long-idle account signing in on a fresh install. That's what they saw, not a proven cause.
> - **Keep the sign-in you have.** Upda