<h1><img width="100" src="docs/icons/avatar.png" alt="bearinmind patches" align="absmiddle"> bearinmind patches</h1>

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Built for Morphe](https://img.shields.io/badge/Built%20for-Morphe-1E5AA8?style=flat-square)](https://morphe.software)

I'll continue to support patches for apps I use & apps that I get requests for (either for specific features or premium unlocking). Below is a short description of how to install my patches on morphe!

Install Morphe Manager if you have not yet: https://morphe.software

[Click here to add bearinmind patches to Morphe Manager](https://morphe.software/add-source?github=bearinmindcat/morphe-patches)

Select the app you want to patch inside Morphe Manager, follow all instructions shown.

## Patches

<!-- PATCHES_START -->
> **[v2.5.2](https://github.com/bearinmindcat/morphe-patches/releases/tag/v2.5.2)**&nbsp;&nbsp;•&nbsp;&nbsp;`main`&nbsp;&nbsp;•&nbsp;&nbsp;52 patches total
<details>
<summary><img src="docs/icons/pin-google.png" width="20" height="20" align="top"> Google Maps&nbsp;&nbsp;-&gt;&nbsp;&nbsp;<img src="docs/icons/pin-ungoogled.png" width="20" height="20" align="top"> Ungoogled Maps&nbsp;&nbsp;•&nbsp;&nbsp;28 patches</summary>
<br>

<p>
<img src="docs/screenshots/com.google.android.apps.maps/1-account-menu.png" width="19%" alt="Account menu" title="Account menu">
<img src="docs/screenshots/com.google.android.apps.maps/2-customization.png" width="19%" alt="Customization" title="Customization">
<img src="docs/screenshots/com.google.android.apps.maps/3-offline-maps.png" width="19%" alt="Offline maps" title="Offline maps">
<img src="docs/screenshots/com.google.android.apps.maps/4-navigation.png" width="19%" alt="Navigation" title="Navigation">
<img src="docs/screenshots/com.google.android.apps.maps/5-navigation-zoomed-out.png" width="19%" alt="Navigation zoomed out" title="Navigation zoomed out">
</p>

**Supported version(s):** 26.36.04.973607363

| Patch | Description | Options |
|----------|----------------|-----------|
| [120 refresh rate](#120-refresh-rate) | Lifts the 60 Hz limit Maps puts on itself, on the app and on the map, so it can run at your screen's full refresh rate (such as 120 Hz). Uses more battery, most of all while navigating. Off by default: switch it on on the Customization screen. |  |
| [Account sheet cleanup](#account-sheet-cleanup) | Removes the "More from this app" label from the account sheet, and keeps the sheet open when you come back from Settings or Customization or tap "Your profile", instead of dropping back to the map. |  |
| [Add microG support](#add-microg-support) | Builds microG Maps, a separate app (org.ungoogled.android.apps.maps.microg) that signs in to your Google account through microG: saved places and lists, Timeline, location sharing, contributions and push messages. Remove sign-in prompts, Trim account menu and Remove permissions are left out of this build, Offline saved places keeps only its Local saved screen, which copies your account's saved lists to the phone (Pull from Google account), and its icon carries microG's C. Needs microG: MicroG-RE or ReVanced GmsCore. Not for root (mount) installs. |  |
| [Any media app](#any-media-app) | Navigation's Default media app (Settings > Navigation) offers every music and podcast app that works with Android Auto, such as Poweramp, not only Spotify, YouTube Music and Pandora. |  |
| [Avoid Flock cameras](#avoid-flock-cameras) | Steers driving directions around Flock cameras: when Google's route passes one, a camera-free way is worked out with BRouter, an OpenStreetMap router, and Maps asks Google again for a route through it, so Google still times and navigates the trip, and keeps it through reroutes. A detour longer than half again the distance is dropped. Off until turned on in Waze & external data source, with Flock cameras; your route's start and end go to brouter.de. Trips with stops are left as they are. |  |
| [Better offline maps](#better-offline-maps) | Reworks the offline area picker: zooming out really selects more instead of being shrunk to Google's size cap, the box can be resized by dragging its edges and corners, a large area is split into several downloads whose true total size is shown, and areas already downloaded are drawn on the map. Can be turned off on the Customization screen. |  |
| [Black theme](#black-theme) | AMOLED-black theme. Pins Maps' own dark mode and its separate navigation colour scheme, and remaps colour resources, drawable fills and draw-time paints so no surface is left grey. |  |
| [Blue pin](#blue-pin) | Chromium-coloured flat map pin on every in-app product logo and the search bar's leading icon. |  |
| [Bypass Play Services checks](#bypass-play-services-checks) | Makes Maps' bundled Play services signature and availability checks always pass, so it runs re-signed and with Play services disabled or absent, and lets it load tiles, 