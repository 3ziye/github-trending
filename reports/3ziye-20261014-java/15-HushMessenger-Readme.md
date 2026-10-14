![HushMessenger. Keep the conversation. Cut the friction.](assets/readme-hero.png)

<p align="center">
  <a href="https://github.com/SysAdminDoc/HushMessenger/releases/tag/v0.23.0"><img src="https://img.shields.io/badge/version-0.23.0-0084FF" alt="Version 0.23.0"></a>
  <a href="CHANGELOG.md"><img src="https://img.shields.io/badge/development-0.23.3-F3A6B8" alt="Development version 0.23.3"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-GPL--3.0-blue" alt="License GPL-3.0"></a>
  <img src="https://img.shields.io/badge/platform-Android%209%2B%20arm64-3DDC84" alt="Platform Android 9 or newer, arm64">
  <img src="https://img.shields.io/badge/Messenger-583.0.0.29.95-0084FF" alt="Messenger 583.0.0.29.95">
</p>

<p align="center">
  <a href="https://ko-fi.com/X8K126YVER">
    <img height="42" src="https://storage.ko-fi.com/cdn/kofi2.png?v=3" alt="Buy me a coffee on Ko-fi" />
  </a>
</p>

<p align="center">
  <sub><em>If HushMessenger makes Messenger better for you, a coffee helps me keep testing patches and maintaining them as Messenger changes.</em></sub>
</p>

# HushMessenger

HushMessenger is a set of [Morphe](https://morphe.software) patches for Facebook Messenger. You bring the Messenger APK, Morphe patches it on your phone, and you get a Messenger with a settings screen full of switches that stock Messenger doesn't have. Hide the ads, the suggested people, the stories row and Meta AI. Stop sending read receipts and typing indicators. Watch stories without showing up in the viewer list. Keep a log of messages so an unsend can't take them back. Send photos at their real quality, use your own font, let Material You color the app, and more.

Every switch starts off, so a freshly patched Messenger behaves like stock until you turn something on. The current release has 50 patches. What changed in each version is in the [changelog](CHANGELOG.md).

**[Add HushMessenger to Morphe Manager](https://morphe.software/add-source?github=SysAdminDoc%2FHushMessenger)**

> [!IMPORTANT]
> Keep your signing key. A patched update only installs over your copy when it's signed with the same key, and with the same key your sign-in and chats survive each update. See [Morphe's backup and keystore guide](https://github.com/MorpheApp/morphe-manager/blob/main/docs/backup-and-keystore.md).

## Install

1. **Get the APK.** HushMessenger patches arm64 Messenger 583.0.0.29.95 only. Download one from [APKMirror's 583.0.0.29.95 page](https://www.apkmirror.com/apk/facebook-2/messenger/facebook-messenger-583-0-0-29-95-release/) and check its version code against the [supported builds](#supported-messenger-builds). A 32-bit build shares the version name and won't work.
2. **Add the source.** Open the link above on your phone with Morphe Manager (1.34.0 or newer) installed. Or in Manager open **Sources**, tap **+**, choose **Remote** and enter `github.com/SysAdminDoc/HushMessenger`. The card should show **50 patches**. If it shows an older version, tap its refresh button.
3. **Patch Messenger.** The default selection includes every switch. Three patches start unselected because they change the app package itself: **Clone install under another package name**, **Spoof package version** and **Custom new-message sound**. To add one, turn on **Settings → Advanced → Expert mode** in Manager and use **Choose patches**.
4. **Keep one source.** Don't add the remote source and a local copy together, and don't mix in Messenger patches from other sources.

Prefer a local source? Download [`patches-0.23.0.mpp`](https://github.com/SysAdminDoc/HushMessenger/releases/tag/v0.23.0) and add it through **Sources > + > Local**. It won't update itself. The `.mpp` file is a patch bundle, not a Messenger APK. Morphe Desktop 1.18.1 can load the same source too.

## Settings

Long-press Messenger's icon on your home screen and tap **Patch controls**. The **HushMessenger** row in Messenger's Menu tab and side menu opens the same screen, and so does the **HushMessenger settings** icon in your app drawer. **App > Hide app drawer icon** hides that icon without touching Messenger. Inside Messenger, a long press on the Messenger logo at the top of Chats or on the Menu tab's title opens settings too, even while changes are paused. On a Root Mount install there's no drawer icon, and the long-press shortcuts appear once Messenger has started.

**Pause all changes** turns every switch off at once without forgetting your choices. Changes to the Meta AI and bottom tabs, bubbles, your font and **Restore old emoji drawer** need **Restart Messenger**. Inbox options show up with the next chat list Messenger builds. While a restart is waiting, a bar at the top of settings says how many and has the button, and after the restart settings open again on the page you left. The button is also on the App tab and in the icon's long-press menu. If Messenger crashes three times near startup, safe mode pauses the controls. Open settings and tap **Resume**.

The **Controls** t