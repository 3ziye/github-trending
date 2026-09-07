# MAKO - Frame Generation and Scaling on SteamOS/Linux

<p align="center">
  <img src="plugin/assets/mako-logo.webp" width="256" alt="MAKO logo" />
</p>

<p align="center">
  <a href="https://trendshift.io/repositories/171701?utm_source=trendshift-badge&amp;utm_medium=badge&amp;utm_campaign=badge-trendshift-171701" target="_blank" rel="noopener noreferrer"><img src="https://trendshift.io/api/badge/trendshift/repositories/171701/daily?language=C%2B%2B" alt="eugeniosegala/MAKO | Trendshift" width="250" height="55" /></a>
</p>

<p align="center">
  <a href="https://discord.gg/NAVkyCq7Rc" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/Discord-join-5865F2?style=flat-square&amp;logo=discord&amp;logoColor=white" alt="Join the MAKO Discord community" /></a>
  <a href="https://github.com/eugeniosegala/MAKO/actions/workflows/tests.yml" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/github/actions/workflow/status/eugeniosegala/MAKO/tests.yml?branch=main&amp;style=flat-square&amp;label=tests" alt="Tests status" /></a>
  <a href="LICENSE.md" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/license-GPL--3.0--or--later-0f766e?style=flat-square" alt="GPL-3.0-or-later license" /></a>
  <br />
  <a href="https://github.com/eugeniosegala/MAKO/releases/latest" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/github/v/release/eugeniosegala/MAKO?filter=plugin-%2A&amp;display_name=tag&amp;sort=semver&amp;style=flat-square&amp;label=Decky&amp;color=1d4ed8" alt="Latest MAKO Decky release" /></a>
  <a href="https://github.com/eugeniosegala/MAKO/releases?q=render-v" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/github/v/release/eugeniosegala/MAKO?filter=render-%2A&amp;display_name=tag&amp;sort=semver&amp;style=flat-square&amp;label=Renderer&amp;color=1d4ed8" alt="Latest MAKO Renderer release" /></a>
  <img src="https://img.shields.io/badge/platform-SteamOS%20%7C%20Linux-6b8e23?style=flat-square" alt="SteamOS and Linux" />
</p>

<!-- prettier-ignore -->
> [!IMPORTANT]
> **<a href="https://github.com/eugeniosegala/decky-lsfg-vk-experimental" target="_blank" rel="noopener noreferrer">Decky LSFG-VK Experimental</a> and <a href="https://github.com/eugeniosegala/lsfg-vk-experimental" target="_blank" rel="noopener noreferrer">LSFG-VK Experimental</a> are now MAKO.** This repository is their new home and continuation. Future development, releases, documentation, and issue tracking happen here.

> **Independent project:** MAKO is not an official Lossless Scaling, Decky Loader, or lsfg-vk release. MAKO does not contain or distribute Lossless Scaling, `Lossless.dll`, or extracted proprietary model payloads. LSFG frame generation and LS1 scaling read selected resources at runtime from a lawful, user-supplied <a href="https://store.steampowered.com/app/993090/Lossless_Scaling/" target="_blank" rel="noopener noreferrer">Lossless Scaling</a> installation; the open MAKO Scaler does not require it. MAKO does not alter the user's DLL file, and translated resources remain process-local. Users are responsible for complying with the terms applicable to their copy. See <a href="THIRD_PARTY_NOTICES.md" target="_blank" rel="noopener noreferrer">Third-party notices</a>.

## Downloads

| Component | Recommended for | Releases |
| --- | --- | --- |
| **MAKO Decky** | Steam Deck, Steam Machine, and Decky Loader users (bundles MAKO Renderer) | <a href="https://github.com/eugeniosegala/MAKO/releases/latest" target="_blank" rel="noopener noreferrer">Latest MAKO Decky release (ZIP under Assets)</a> |
| **MAKO Renderer** | Direct Vulkan-layer installation without Decky | <a href="https://github.com/eugeniosegala/MAKO/releases/tag/render-v3.1.0" target="_blank" rel="noopener noreferrer">Latest MAKO Renderer release (Linux archive under Assets)</a> |

## Community

Join the official <a href="https://discord.gg/NAVkyCq7Rc" target="_blank" rel="noopener noreferrer">MAKO Discord</a> for discussion, testing, development, showcases, and live troubleshooting. GitHub remains the source of truth for <a href="https://github.com/eugeniosegala/MAKO/issues/new/choose" target="_blank" rel="noopener noreferrer">bug reports and feature requests</a>.

<!-- prettier-ignore -->
> [!TIP]
> **Want update alerts?** MAKO Decky and MAKO Renderer are published independently. At the top-right of the <a href="https://github.com/eugeniosegala/MAKO" target="_blank" rel="noopener noreferrer">MAKO GitHub repository</a> page, click **Watch** > **Custom**, select **Releases**, then click **Apply**. GitHub will notify you when a new release is published, subject to your GitHub notification settings.

Published Renderer packages currently target x86_64 Linux hosts and include layers for both 64-bit and 32-bit x86 game processes. Native AArch64/Armada packages are not included in this release.

## ✨ Highlights

|  | Highlight | What it brings |
| :-: | ---