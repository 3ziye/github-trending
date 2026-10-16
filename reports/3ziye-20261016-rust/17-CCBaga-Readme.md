<!--
[INPUT]: 已实现功能、开发配置、跨平台 PR 回归、双应用使用方式与 MIT/第三方许可边界。
[OUTPUT]: 面向公开仓库的英文产品首页、中文入口、旅居人员用途声明、安装与开发入口、架构和贡献导航。
[POS]: 项目公开入口，连接产品功能、使用说明与模块导航。
[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
-->
<div align="center">
  <img src="docs/brand-logos.svg" width="320" height="149" alt="CCBaga-A and CCBaga-B logos, side by side" />
  <h1>CCBaga</h1>
  <p><strong>English</strong> · <a href="README.zh-CN.md">简体中文</a></p>
  <p><strong>A native macOS, Linux and Windows toolkit for a cleaner workspace and an environment you can verify.</strong></p>
  <p>Claude identities · Browser fingerprints · System settings · Network Skill</p>
  <p>
    <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-e8a181?style=flat-square" alt="MIT license" /></a>
    <img src="https://img.shields.io/badge/macOS-12%2B-111827?style=flat-square&amp;logo=apple&amp;logoColor=white" alt="macOS 12 and later" />
    <img src="https://img.shields.io/badge/Linux-x86__64-111827?style=flat-square&amp;logo=linux&amp;logoColor=white" alt="Linux x86_64" />
    <img src="https://img.shields.io/badge/Windows-10%2F11-111827?style=flat-square&amp;logo=windows&amp;logoColor=white" alt="Windows 10 and 11" />
    <img src="https://img.shields.io/badge/core-Rust%20%2B%20Tauri-111827?style=flat-square&amp;logo=rust&amp;logoColor=white" alt="Rust and Tauri" />
  </p>
  <p>
    <a href="#features">Features</a> ·
    <a href="#installation">Installation</a> ·
    <a href="#updates">Updates</a> ·
    <a href="#quick-start">Quick start</a> ·
    <a href="docs/usage.md">Usage guide</a> ·
    <a href="#architecture">Architecture</a> ·
    <a href="#development">Development</a> ·
    <a href="CONTRIBUTING.md">Contributing</a>
  </p>
</div>

![CCBaga: native control, observable environments](docs/readme-hero.png)

**Intended use:** CCBaga is intended solely for people residing or traveling abroad to manage their own Claude identities. Use that violates Anthropic's official terms of service is prohibited.

CCBaga brings local maintenance and environment setup into one focused desktop workflow. Inspect Claude data before removing it, rotate your companion browser's fingerprint and restart it, align system settings with a selected region, and compare real browser readings with the machine and network exit.

Two applications work together: **CCBaga-A** owns native operations; **CCBaga-B** runs an isolated Fingerprint Chromium profile. Browser measurements return to the host through a local session. Changing a setting and verifying its effect are separate steps.

## Features

<table>
  <tr>
    <td width="33%"><strong>Local Claude identities</strong><br /><br />Archive the current local identity, switch to a saved identity or start with an empty workspace. Choose what stays shared and what moves with each identity.</td>
    <td width="33%"><strong>Fingerprint &amp; restart</strong><br /><br />Generate a fresh seed, apply the selected region's language and timezone, then restart the companion browser.</td>
    <td width="33%"><strong>Real environment checks</strong><br /><br />Compare browser and machine readings with the actual network exit. Passing measured checks produces a green page and a large checkmark.</td>
  </tr>
  <tr>
    <td><strong>Native system settings</strong><br /><br />Apply timezone, preferred language and region settings. Open desktop controls for location and permissions; see platform-specific limits.</td>
    <td><strong>AI-guided network setup</strong><br /><br />Three simple steps, a coding-agent selector and a copyable Skill installation prompt. Give the AI your files and connection details; it handles the commands.</td>
    <td><strong>Claude Code CLI tools</strong><br /><br />Detect the installation method and version. Uninstall or reinstall through native, npm/bun, Homebrew or WinGet workflows.</td>
  </tr>
</table>

**One region selector. Four everyday actions.** Easy setup puts browser cache cleanup, fingerprint rotation, timezone/language reset and identity archiving on the same page. The sidebar keeps advanced controls in Network, Claude identities, Browser and Computer.

The interface supports **English and Chinese**, with shared YAML catalogs. Switching the interface language does not change the computer or browser language.

The bilingual **Usage guide** covers common actions and data boundaries. See the [full guide](docs/usage.md).

## Installation

**Platforms:** macOS 12 or later on Apple Silicon; Linux x86_64 with GTK 3 and WebKitGTK 4.1; Windows 10/11 x86_64. Intel macOS and Linux ARM64 are not supported.

Linux x86_64 packages include DEB, RPM and AppImage built on Ubuntu 22.04 (glibc 2.35), plus a separate package for current Arch/pacman systems. All include the companion browser. See [Linux setup](docs/linux.md) for installation and platform limits. Official versions are published exclusively by the project owner, **liseami**.

Windows x86_64 uses one NSIS setup installer containing both A and B. The installer is not Authenticode 