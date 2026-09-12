<h1 align="center">
  <img src="docs/images/readme-logo-black-v020.png" width="64" alt="DSH Desktop logo" valign="middle" />
  DSH Desktop
</h1>

<p align="center">
  A local-first, cross-platform desktop app for
  <a href="https://github.com/deepseek-ai/deepseek-harness">DeepSeek Harness</a>.
</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.zh.md">简体中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ru.md">Русский</a> · <a href="README.es.md">Español</a> · <a href="README.pt.md">Português</a>
</p>

<p align="center">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-171513.svg" /></a>
  <img alt="macOS" src="https://img.shields.io/badge/macOS-Apple%20Silicon%20%7C%20Intel-171513.svg" />
  <img alt="Windows" src="https://img.shields.io/badge/Windows-x64-171513.svg" />
</p>

![DSH Desktop overview with portable presets, model providers, phone control, and editable PPT generation](docs/images/dsh-desktop-hero-v021.png)

<p align="center"><strong>Use official DeepSeek models or mainstream third-party providers, manage portable Agent presets, continue Harness sessions from your phone, and turn source material into editable PPTX decks.</strong></p>

DSH Desktop packages the local DeepSeek Harness experience as an installed desktop application. It starts Harness automatically, keeps profiles, plugins, workspaces, model settings, and sessions outside the application directory, and opens the full Harness interface as soon as the local runtime is ready.

> [!IMPORTANT]
> DSH Desktop is an early preview built on the rapidly evolving `@deepseek-ai/dsh@0.1.2-rc.1`. macOS releases are code-signed and notarized by Apple. Windows x64 installers are code-signed; Windows security warnings may still decrease gradually as the publisher builds download and installation reputation.

## Download

We offer stable and preview releases: download the **stable release**, recommended for everyday use, from our [official website](https://www.dshdesktop.com/#download). To try a **preview release**, choose a version marked **Pre-release** on [GitHub Releases](https://github.com/dataelement/dsh-desktop/releases).

Preview releases include our newest features and closely track the latest official DeepSeek Harness versions. They may be incompatible with community plugins and are **not recommended for general users**. Early adopters are welcome to try them and share feedback in our community; we roll out updates to the wider community only after validation by early adopters.

Installed builds check for updates shortly after startup and every six hours. When a new version is available, DSH Desktop asks before downloading it; installation begins only after you choose **Restart and install**. You can also check manually from the application menu or skip one version without hiding future releases.

## Community

<p align="center">
  Scan the QR code below with WeChat to join the DSH Desktop community group.<br />
  <img src="docs/images/wechat-group-20260815.png" width="220" alt="DSH Desktop WeChat group QR code" /><br />
  Prefer Discord? <a href="https://discord.gg/he2gAKCpj">Join the DSH Desktop Discord community</a>.
</p>

## What DSH Desktop adds

DeepSeek Harness already provides the Agent runtime and Web UI. DSH Desktop adds the native host capabilities needed for a practical desktop product:

- Starts and stops Harness without requiring a separate CLI or browser tab
- Uses the native system directory picker to add and manage project workspaces
- Supports official DeepSeek models and mainstream third-party model providers
- Imports and exports complete custom Agent presets as portable [`.dshpreset` packages](docs/preset-packages.md), with conflict checks and a trust warning before installation
- Turns source material into editable PPTX decks through the built-in PPT mode
- Preserves profiles, plugins, workspaces, sessions, and model settings across app upgrades
- Detects startup and frontend plugin failures, keeps diagnostics in `harness.log`, and offers guided recovery actions
- Provides a non-destructive Safe Mode that temporarily blocks third-party plugins
- Lets a paired phone continue sessions over the local network or an optional temporary public tunnel
- Checks for desktop updates and keeps download and installation under user control
- Adapts native menus, titlebar behavior, window focus, theme, and application branding for macOS and Windows

## PPT generation

Enable the **PPT** button, choose a template, and describe the deck you need. The built-in catalog includes **16 templates and 192 layouts** with editable PPTX output. Previews use English; decks can use English or Chinese, with corresponding font settings. Preview language does not determine output language.

PPT is preinstalled, and its automatic instructions apply only to sessions where the PPT button is enabled. See the [PPT runtime guide](packages/ppt-runtime/README.md) for templates, validation