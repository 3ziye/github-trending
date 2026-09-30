![Hushfeed. Take back your feed with focused controls for filtering, gestures, playback, downloads and privacy.](assets/readme-hero.png)

<p align="center">
  <a href="CHANGELOG.md"><img alt="version" src="https://img.shields.io/badge/version-0.65.0-6f42c1.svg" /></a>
  <a href="LICENSE"><img alt="license" src="https://img.shields.io/badge/license-GPLv3-blue.svg" /></a>
  <a href="https://www.android.com/"><img alt="platform" src="https://img.shields.io/badge/platform-Android-3ddc84.svg" /></a>
  <a href="https://github.com/MorpheApp/morphe-manager"><img alt="Morphe" src="https://img.shields.io/badge/works%20with-Morphe-00b894.svg" /></a>
  <a href="https://github.com/SysAdminDoc/hushfeed/discussions"><img alt="Discussions" src="https://img.shields.io/github/discussions/SysAdminDoc/hushfeed?color=0969da" /></a>
  <a href="https://www.apkmirror.com/apk/tiktok-pte-ltd/tik-tok-including-musical-ly/"><img alt="TikTok 47.0.3 and 47.1.3" src="https://img.shields.io/badge/TikTok-47.0.3%20%7C%2047.1.3-ff0050.svg" /></a>
</p>

# Hushfeed

Hushfeed is a [Morphe](https://github.com/MorpheApp/morphe-manager) patch bundle for people who want TikTok to behave differently. It can cut feed clutter, guard risky taps, improve downloads and expose controls TikTok leaves buried or unavailable. Every selected patch is configured from one native settings screen inside the app.

**[Add Hushfeed to Morphe](https://morphe.software/add-source?github=SysAdminDoc%2Fhushfeed)** | [Download the latest bundle](https://github.com/SysAdminDoc/hushfeed/releases/latest) | [Tour the settings](#settings-tour) | [Browse all 98 patches](#patches)

> [!IMPORTANT]
> Hushfeed changes often while TikTok moves underneath it. Hushfeed targets the global TikTok package, `com.zhiliaoapp.musically`, versions [47.0.3](https://www.apkmirror.com/apk/tiktok-pte-ltd/tik-tok-including-musical-ly/tiktok-47-0-3-release/tiktok-47-0-3-3-android-apk-download/) and [47.1.3](https://www.apkmirror.com/apk/tiktok-pte-ltd/tik-tok-including-musical-ly/tiktok-47-1-3-release/tiktok-47-1-3-android-apk-download/). Use one of those exact APKs when patching. See [Supported target](#supported-target) for the verified build details.

Hushfeed v0.65.0 contains 98 patches for TikTok 47.0.3 and 47.1.3. Mute feed videos now works on 47.1.3 and on photo posts, holding the Home tab opens Hushfeed's settings, and every save says it's been taken the moment you ask. It needs Morphe Manager 1.32.0 or newer.

## Pick what changes

- **Feed:** Start with the reversible Calm feed preset, or hide ads, Shop, livestreams, stories, photo posts, unwanted creators and videos matching your own rules. Remove feed ads also catches paid partnerships and creator commission posts, including location-affiliate videos. A profile you open only loses its ads, so your view and like limits never thin it out, and your own posts are never hidden. TikTok can also open on Following, Friends, Inbox or Profile instead of For You.
- **Touch controls:** Add second-tap protection to Follow, Like, comment and story likes, quick reposts and sending from the share sheet. Remap or disable long press and double tap, and keep For You in place when you tap Home or pull down. A long press on Comment, Share or Favorites can play at the hold speed instead of opening TikTok's menu. TikTok's own play and pause, previous and next buttons can sit on the feed too, the ones it otherwise keeps for screen reader users.
- **Playback:** Choose speed and quality, stop loops, resume a video after scrolling or move to the next one automatically.
- **Downloads:** Save watermark-free video, original photos, separate audio and SRT subtitles with filenames and folders you control. The save button also works on videos whose creator turned downloading off. A save of several files shows a running count with a Cancel, and the result says what landed.
- **Comments and inbox:** Filter comment text or accounts, translate comments and decide which Inbox rows appear. A creator's poll in the comments can show how the vote stands before you pick. Tapping more under a video can open its comments with the whole caption on top. Compact comment header removes the count, sort and close row and the suggestion area above it. Close comments with Back or a downward swipe. It's optional and needs a restart.
- **Privacy and diagnostics:** Turn off supported telemetry, hide view and typing reports, back up settings and export a useful diagnostic report.

Compact comment header keeps headers that switch between different lists, so those tabs remain reachable.

**Easier comment likes**, under Comments, extends the heart's touch area into nearby blank space. The icon and row spacing don't change. Text and neighboring controls keep their own space. It's off by default and needs a restart.

Feed screen has separate options to hide the **Full screen button** and **location labels** over videos, including badges listing multiple places. They don't remove the videos or chang