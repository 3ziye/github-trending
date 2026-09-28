<div align="center">

# Lost Odyssey Recomp

**An experimental native PC port of Lost Odyssey for Xbox 360.**

Windows x64 · Direct3D 12 · Vulkan · PowerPC static recompilation

<img src="docs/images/title-screen.png" alt="Lost Odyssey title screen — Press START" width="960">

Optional diagnostics are off by default and can be disabled in Settings. See [Privacy](PRIVACY.md).

### [Latest download](https://github.com/freefrank/LostOdysseyRecomp/releases/latest) · [Installation guide](docs/INSTALLING.md) · [Report an issue](https://github.com/freefrank/LostOdysseyRecomp/issues)

[简体中文](README.zh-CN.md) · [Changelog](CHANGELOG.md) · [Developer tools](tools/README.md) · [Projects](https://github.com/users/freefrank/projects/3) · [Build from source](docs/BUILDING.md)

</div>

> [!IMPORTANT]
> **This project is still in early testing.** Opening areas and selected scenes have been tested; a complete playthrough has not. Rendering and stability issues remain. You must supply your own supported game files.

## Recent releases

| Version | Highlights |
| :--- | :--- |
| [v0.7.9](https://github.com/freefrank/LostOdysseyRecomp/releases/tag/v0.7.9) | Windows D3D12 frame generation (Off/DLSS/FSR), applied on Save without restarting; Ubuntu 22.04 AppImage compatibility and updater improvements. |
| [v0.7.3](https://github.com/freefrank/LostOdysseyRecomp/releases/tag/v0.7.3) | D3D12 binding de-duplication and opt-in rendering diagnostics. |
| [v0.7.2](https://github.com/freefrank/LostOdysseyRecomp/releases/tag/v0.7.2) | D3D12 DLSS/FSR super-resolution routes and DLAA sizing correction. |
| [v0.7.1](https://github.com/freefrank/LostOdysseyRecomp/releases/tag/v0.7.1) | Standalone Flatpak and in-game disc/DLC selection and re-import. |

See the [roadmap](docs/ROADMAP.md) for current plans and the [changelog](CHANGELOG.md) for detailed release history.

## Start playing

### Windows
1. **Download and extract** the v0.7.9 Windows release ZIP (`LostOdysseyRecomp-windows-x64-v0.7.9.zip`) from the [latest release](https://github.com/freefrank/LostOdysseyRecomp/releases/latest) to a writable folder.
2. **Run `LostOdysseyRecomp.exe`** and import your game files when prompted. The importer accepts an extracted folder, `default.xex`, an XDVDFS ISO or a GOD container.
3. **Choose your language and graphics settings.** The game continues after setup and shader preparation.

### Linux (Flatpak or AppImage)
- **Flatpak bundle**: Ensure the Freedesktop 26.08 platform is installed:
  ```bash
  flatpak --system install flathub org.freedesktop.Platform//26.08
  ```
  Download the v0.7.9 standalone `.flatpak` bundle (`LostOdysseyRecomp-linux-x64-v0.7.9.flatpak`) and install:
  ```bash
  flatpak --user install --bundle LostOdysseyRecomp-linux-x64-v0.7.9.flatpak
  flatpak run io.github.freefrank.LostOdysseyRecomp
  ```
- **AppImage**: Download `LostOdysseyRecomp-linux-x64-v0.7.9.AppImage`, make it executable (`chmod +x`), and run directly.

No Python or Visual Studio installation is needed for the release package. Later launches reuse the shader cache. Keep your save and profile folders when updating.

The current branch updater checks GitHub's latest Release: a higher numeric version updates, and an equal numeric version with a different `-suffix` also triggers an update. The updater additionally permits recovery from an empty updater-only folder and stale or malformed local metadata. After a successful update, the helper asks whether to launch the game and defaults to **No**; silent runs complete without launching. After the download completes, the updater installs through ordinary HTTP/I/O handling, ZIP CRC parsing, path protection and rollback; it does not add SHA-256 or size authentication. The v0.7.9 Windows transition package carries the legacy SHA map once so an already published v0.7.3 updater can upgrade automatically; the v0.7.9 updater ignores those values.

| Requirement | Supported configuration |
| :--- | :--- |
| System | Windows x64, AVX-capable CPU, Direct3D 12 or Vulkan graphics driver |
| Game data | Audited Europe, Asia or USA, Europe edition; Disc 1 is required to start |
| Additional discs | Import additional discs or DLC from the built-in importer in `LostOdysseyRecomp.exe`; later-disc progression is not fully verified |

See the [installation guide](docs/INSTALLING.md) for accepted disc versions, file locations and updating.

## In-game screenshots

| Ring combat | City exploration |
| :---: | :---: |
| ![Kaim attacking with the Ring timing interface](docs/images/ring-battle.png) | ![Exploring the industrial city](docs/images/city-exploration.png) |

*Unmodified screenshots from development builds leading up to v0.1.*

## Current features

| Feature | What to expect |
| :--- | :--- |
| Game importer | Folder, XEX, ISO and GOD input; originals stay untouched, and staged copies check final writes before publication |
| First-launch setup | Language and graphics settings before game initialization |
| Language settings | En