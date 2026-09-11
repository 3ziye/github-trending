<div align="center">

<img src="docs/assets/logos/strata-tokyo-night.svg" alt="Strata logo" width="160">

# Strata

**Navigate every layer.** A fast, keyboard-first file manager for modern Linux desktops.

[![CI](https://github.com/lgse/strata/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/lgse/strata/actions/workflows/ci.yml)
[![Latest release](https://img.shields.io/github/v/release/lgse/strata?display_name=tag&sort=semver)](https://github.com/lgse/strata/releases/latest)
[![License: MIT](https://img.shields.io/github/license/lgse/strata)](LICENSE)
[![Linux](https://img.shields.io/badge/platform-Linux-FCC624?logo=linux&logoColor=black)](#technical-specifications)

<picture>
  <source media="(prefers-reduced-motion: no-preference)" srcset="docs/assets/strata-demo.gif">
  <img src="docs/assets/strata-columns.png" alt="Strata browsing files and showing settings, themes, Icons view, and folder creation" width="1280">
</picture>

<sub>The animation respects reduced-motion preferences. View the [static preview](docs/assets/strata-columns.png).</sub>

</div>

Strata combines spatial Miller-column navigation with familiar Icons and List views, instant fuzzy filename search, rich previews, and native Linux desktop integration. It is designed for Omarchy and works on compatible GTK4 Linux environments.

## Contents

- [Features](#features)
- [Installation](#installation)
  - [Interactive installation](#interactive-installation)
  - [AI-assisted installation](#ai-assisted-installation)
  - [Manual installation](#manual-installation)
- [Usage and desktop integration](#usage-and-desktop-integration)
  - [Desktop entry](#desktop-entry)
  - [Make Strata the Omarchy file manager](#make-strata-the-omarchy-file-manager)
  - [Network shares](#network-shares)
- [Theming](#theming)
  - [Follow Omarchy Quattro](#follow-omarchy-quattro)
  - [Bundled themes](#bundled-themes)
  - [Custom themes](#custom-themes)
- [Release channels](#release-channels)
- [Under the hood](#under-the-hood)
- [Technical specifications](#technical-specifications)
- [Development and documentation](#development-and-documentation)
- [Contributors](#contributors)
- [License](#license)

## Features

- **Three browser modes:** navigable Columns, an Icons grid, and a sortable List table.
- **Keyboard-first control:** Vim-style movement, navigation history, location entry, pane filtering, fuzzy search, file operations, and quick previews. An optional footer and F1 shortcut reference help you learn each mode; the footer also highlights when files are available to paste. See [keyboard navigation and paste destinations](docs/keyboard-navigation.md).
- **Fast recursive search:** press <kbd>Ctrl</kbd>+<kbd>K</kbd> to find files and directories by name or path while the tree is still being indexed. Global search covers Home and all mounted local drives, regardless of the current folder. Hover the search field to see the included locations. The dialog warns when results are incomplete; folder-scoped filtering/search remains separate. URI-native remote shares are not yet included.
- **Rich previews and thumbnails:** bounded previews for text, source code, images, camera RAW, PDF, audio, and video, with native parser-backed formats isolated from the application.
- **Responsive filesystem work:** cancellable directory loading, bounded streaming, incremental monitoring, stable selection, and virtualized large directories.
- **Everyday file operations:** create folders, rename, cut, copy, paste, trash, permanent delete, sorting, hidden files, pins, and history.
- **Remote locations:** browse GIO/GVfs locations such as authenticated SMB shares from the location field.
- **Adaptive appearance:** compact or airy density, six bundled themes, custom themes, and live Omarchy Quattro theme following.
- **Updates in the app:** opt-in automatic checks, release notes, verified downloads, and in-place installation for release binaries.
- **System file chooser:** opt in through **Settings → General → System file chooser**, the installer, or `strata --install-portal`; see [portal setup](docs/portal-file-chooser.md).

## Installation

Arch Linux and Omarchy are the primary supported environments. Current binaries require **glibc 2.39 or newer** and the runtime libraries listed below.

### Interactive installation

The interactive installer detects the Linux architecture, glibc version, Arch
Linux, and Omarchy 3 or 4. It installs the latest verified stable release and
offers optional desktop-menu, default-folder-handler, "Open file location", system
file chooser, SMB, broader image/RAW, and Omarchy keybind integration:

```bash
curl -fsSL https://raw.githubusercontent.com/lgse/strata/main/install.sh | bash
```

The installer shows every privileged package operation before asking to run it.
It verifies both the published SHA-256 digest and GitHub Actions provenance before
installing anything from the release archive. The binary is installed per-user at
`~/.local/bin/