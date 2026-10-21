![Hushfacebook. Keep the people. Cut the noise.](assets/readme-hero.png)

<p align="center">
  <a href="https://github.com/SysAdminDoc/Hushfacebook/releases"><img src="https://img.shields.io/badge/version-0.16.0-0866FF" alt="Version 0.16.0"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-GPL--3.0-blue" alt="License GPL-3.0"></a>
  <img src="https://img.shields.io/badge/platform-Android%2011%2B-3DDC84" alt="Platform Android 11+">
  <img src="https://img.shields.io/badge/Facebook-583.0.0.39.55-0866FF" alt="Facebook 583.0.0.39.55">
  <img src="https://img.shields.io/badge/for-Morphe%20Manager%201.34.0%2B-8A2BE2" alt="For Morphe Manager 1.34.0 or newer">
</p>

<p align="center">
  <a href="https://ko-fi.com/X8K126YVER">
    <img height="42" src="https://storage.ko-fi.com/cdn/kofi2.png?v=3" alt="Buy me a coffee on Ko-fi" />
  </a>
</p>

# Hushfacebook

Hushfacebook is a set of [Morphe](https://morphe.software) patches for the Facebook app on Android. You bring the Facebook APK, Morphe Manager patches it on your phone, and you get a Facebook with a settings screen of its own. Sponsored and suggested posts go away, and so do the ads in Stories, Reels, search and Marketplace. You can save reels, videos, stories and photos, open links in your own browser, hide the Reels tab and send Facebook less about what you do.

Each row in the [patch table](#patches) says how its switch starts. The ad filters and a handful of others start on, and most of the rest start off until you turn them on. On a computer, [HushFacebook Web](https://github.com/SysAdminDoc/HushFacebookWeb) is a separate userscript for Facebook in the browser.

This project has no connection to Meta or to the Morphe project. Neither endorses it, and neither wrote it.

The latest release is [v0.15.0](https://github.com/SysAdminDoc/Hushfacebook/releases/tag/v0.15.0), with 93 patches. It includes all changes since v0.14.0, among them feed videos that open on their own, comments at full height or from a double tap, switches that hide the status bar, the Messenger button and the counts under posts and reels, settings in Simplified Chinese and a working Tap the bar to seek on 583, as the [changelog](CHANGELOG.md) describes.

[Add to Morphe](https://morphe.software/add-source?github=SysAdminDoc%2FHushfacebook) | [Download a release](https://github.com/SysAdminDoc/Hushfacebook/releases/latest) | [Browse the patches](#patches)

> [!IMPORTANT]
> Back up your signing key after your first patch. Android only installs an update over your patched Facebook when it's signed with the same key, and without that key you'd have to uninstall, which deletes Facebook's data. [Keep your signing key](#keep-your-signing-key) shows how.

## Install

1. Install [Morphe Manager](https://github.com/MorpheApp/morphe-manager) 1.34.0 or newer.
2. Add Hushfacebook as a patch source: https://morphe.software/add-source?github=SysAdminDoc%2FHushfacebook
3. Download Facebook 583.0.0.39.55 from [APKMirror](https://www.apkmirror.com/apk/facebook-2/facebook/). Take the bundle labelled (arm64-v8a) (480-640dpi) (Android 11+), build 475614366, which is a .apkm file. A phone with a 32-bit processor takes the (armeabi-v7a) (320dpi) (Android 11+) bundle, build 475614365, instead.
4. In Morphe Manager, tap **Select other apps**, then **Open APK file**, and pick that file. Android may ask for file access the first time.
5. Patch with the default selection and install. If Meta's own Facebook is on the phone, Android makes you uninstall it first, as [Package conflict](#package-conflict) explains.

The default selection is every patch but three, so you don't need Expert mode. To add `AMOLED black theme`, `Material You theme` or `Disable Play Store updates`, turn on **Settings → Advanced → Expert mode** in Manager before you open the file, then pick them on the **Hushfacebook** tab. If you saved an Expert mode selection before, Manager keeps using it, so tap **Enable recommended patches** once to pick up the patches that joined the default selection since. If you also use another Facebook patch source, check that the two don't patch the same thing ([Patching stops on one patch](#patching-stops-on-one-patch)).

### Keep your signing key

Morphe Manager signs the patched Facebook with a key it makes on your phone, and every update has to carry that same key. Back it up right after your first patch, under **Settings → System → Import & export → Signing key** in Manager, then tap **Export**. The button only shows up once you've patched something. Keep the `Morphe.keystore` file somewhere private, because anyone who has it can sign an APK your phone will take as an update.

On a new phone, import the key in the same place before you patch anything. Reinstalling Manager or clearing its storage makes a new key, and Morphe's settings backup doesn't include it. With a different key, the only way forward is to uninstall the patched Facebook, which deletes its data. A Root Mount install sits over 