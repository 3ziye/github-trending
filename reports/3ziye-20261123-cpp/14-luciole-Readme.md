<p align="center">
  <img src="assets/icons/dev.noctalia.luciole.svg" alt="Luciole Logo" width="192" />
</p>

<p align="center">
  <a href="https://github.com/noctalia-dev/luciole/commits">
    <img src="https://img.shields.io/github/last-commit/noctalia-dev/luciole?style=for-the-badge&labelColor=FFF59B&color=FFF59B&logo=git&logoColor=070722&label=commit" alt="Last commit" />
  </a>
  <a href="https://github.com/noctalia-dev/luciole/stargazers">
    <img src="https://img.shields.io/github/stars/noctalia-dev/luciole?style=for-the-badge&labelColor=FFF59B&color=FFF59B&logo=github&logoColor=070722" alt="GitHub stars" />
  </a>
  <a href="https://docs.noctalia.dev/luciole/">
    <img src="https://img.shields.io/badge/docs-FFF59B?style=for-the-badge&logo=gitbook&logoColor=070722&labelColor=FFF59B" alt="Documentation" />
  </a>
  <a href="https://discord.noctalia.dev">
    <img src="https://img.shields.io/badge/discord-FFF59B?style=for-the-badge&labelColor=FFF59B&logo=discord&logoColor=070722" alt="Discord" />
  </a>
</p>

# Luciole

A native Wayland file manager built to stay smooth: quick to start, fluid when scrolling through large folders, and previews that never block the window.

It offers grid, list and Miller column views, tabs, split view and rich file previews, and runs on any Wayland compositor. It also serves as the Open and Save file picker for other applications through xdg-desktop-portal. It pairs naturally with [Noctalia](https://github.com/noctalia-dev/noctalia) and [Umbriel](https://github.com/noctalia-dev/umbriel). Under the hood: C++23, direct Wayland and OpenGL ES, with no Qt or GTK.

> [!IMPORTANT]
> Luciole is young and actively evolving. It is usable today, but settings, shortcuts and behavior may change between releases, and rough edges remain.

<img width="1900" height="1256" alt="image" src="https://github.com/user-attachments/assets/398e2f25-6fe0-4595-a9ba-626f07a0632b" />

## Why Luciole?

We wanted a file manager that responds as fast as we can move. Folders with thousands of files should open and scroll without a stutter, thumbnails should fill in as you go instead of freezing the view, and a second window should not cost a second application.

That shaped how Luciole is built:

- **GPU rendering:** the interface draws directly through OpenGL ES, so scrolling, zooming and resizing stay fluid even with many thumbnails on screen.
- **Nothing blocks the window:** folder listing, file operations and thumbnail decoding run in the background, and image decoding happens in sandboxed helper processes.
- **One process, many windows:** every window shares a single process, so extra windows and tabs stay light on memory.
- **Shared caches:** thumbnails are reused from the standard freedesktop cache, so folders you have already browsed in other file managers appear instantly.

It also aims to be complete enough for everyday work with archives, network shares and large photo folders, while staying consistent with the rest of the Noctalia family.

To understand the values and philosophy guiding the project, read our [ethos](https://noctalia.dev/ethos).

## Features

- **Browsing:** grid, list and optional Miller columns, with tabs, separate windows, split view, adjustable zoom and sortable detail columns
- **Navigation and search:** clickable breadcrumbs, path completion, recursive filename search and instant filtering of the current folder
- **Thumbnails and previews:** images, video, text and PDF pages, plus file and media metadata
- **File operations:** copy, move, links, batch rename, folder merging, conflict choices, Trash and restoration, with [Undo and Redo](docs/user/file-operations.md#undo-and-redo)
- **Archives:** browse, create and extract, with password prompts for [encrypted formats](docs/user/file-operations.md#archives)
- **Places:** an adaptive sidebar with shared bookmarks, mounted drives, LUKS unlock prompts and optional folder trees
- **File picker:** a [portal backend](docs/user/installation.md#use-luciole-as-the-file-picker) that provides Luciole's Open and Save dialogs for applications using the FileChooser portal; [xdg-desktop-portal-umbriel](https://github.com/noctalia-dev/xdg-desktop-portal-umbriel) selects it automatically when installed, and other desktops can enable it in `portals.conf`
- **Desktop integration:** SFTP, SMB and WebDAV locations, Open With, terminal actions and [custom scripts](docs/user/scripts.md)
- **Configuration:** built-in settings, live-reloaded TOML, icon themes and configurable colors

## Install and run

See the [installation guide](docs/user/installation.md) for Arch Linux, Fedora, Debian and Ubuntu packages, source builds and Nix. Then launch Luciole from your application menu, or from a terminal:

```sh
luciole
luciole ~/Downloads
```

## Configuration

Open Settings with Ctrl+, or from the main menu; changes apply immediately. For manual configuration, use `~/.config/luciole/config.toml`. The [configuration guide](docs/user/configuration.md)