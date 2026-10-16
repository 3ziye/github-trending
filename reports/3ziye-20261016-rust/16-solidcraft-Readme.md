# SolidCraft

**An open-source parametric 3D CAD application built in pure Rust.**

Sketch, constrain, and build solids with a parametric feature timeline. Change a dimension
and watch your model rebuild. Run it on your desktop, in your browser, or let AI agents
model through the built-in MCP server.

![SolidCraft 0.8: model a Raspberry Pi 4 case from an empty design: a sketch dimensioned with parameters, extrude, fillets and shell, a rim rounded in one pick, standoffs patterned on the board's mounting holes, port cut-outs, vent slots, "Pi 4" engraved in a font, a PETG material with its mass in Properties, and a height change in Parameters](docs/screenshots/demo-0.8.gif)

*A Raspberry Pi 4 case from an empty design: a sketch dimensioned with the board's parameters, extrude, fillet, shell, the rim rounded in one pick, an M2.5 standoff patterned on the 58 × 49 mm hole rectangle, port cut-outs, vent slots, "Pi 4" engraved in DejaVu Sans Bold and a PETG material defined in the design, with its mass in Properties, then height 24 → 32 mm in Parameters and it all rebuilds. 9× playback. [Full video](https://github.com/bherbruck/solidcraft/raw/refs/heads/main/docs/screenshots/demo-0.8.mp4), recorded with the [demo script](examples/demo/record_ui.sh).*

## Download

[![Download for Windows][badge-windows]][windows-msi]
[![Download for macOS][badge-macos]][macos-dmg]
[![Download for Linux][badge-linux]][linux-appimage]
[![Get it from the Snap Store][badge-snap]][snap-store]
[![Try it in your browser][badge-web]][web-app]

- **Windows:** download and run the [installer][windows-msi].
  Also for [ARM64][windows-arm64-msi] and [32-bit][windows-x86-msi] PCs, or as a
  [portable zip][windows-portable] that runs without installing.
  With [WinGet](https://learn.microsoft.com/windows/package-manager/winget/):
  `winget install bherbruck.SolidCraft`.
- **macOS:** open the [disk image][macos-dmg] and drag SolidCraft into Applications
  (Apple silicon and Intel).
- **Linux:** download the [AppImage][linux-appimage], allow it to run as a program and open it.
  Or install the [.deb][linux-deb] (Ubuntu, Debian, Mint) or [.rpm][linux-rpm] (Fedora,
  openSUSE), or use [Flatpak](https://bherbruck.github.io/solidcraft/guide/getting-started.html#linux-flatpak).
  With Snap: `sudo snap install solidcraft` ([Snap Store][snap-store], or the [.snap file][linux-snap]).
  For ARM64: [AppImage][linux-arm64-appimage], [.deb][linux-arm64-deb], [.rpm][linux-arm64-rpm].
- **Web:** [try it in your browser][web-app], no install.

The downloads aren't signed yet. On Windows, if SmartScreen warns you, choose **More info**, then
**Run anyway**. On macOS, the first time, right-click SolidCraft in Applications and choose **Open**.

Older versions, checksums and other formats are on the [releases page](https://github.com/bherbruck/solidcraft/releases).
Install details, upgrading from earlier builds and building from source are in
[Getting started](https://bherbruck.github.io/solidcraft/guide/getting-started.html).

[badge-windows]: https://img.shields.io/badge/Windows-Download-0078D6?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik0yIDJoOS41djkuNUgyek0xMi41IDJIMjJ2OS41aC05LjV6TTIgMTIuNWg5LjVWMjJIMnpNMTIuNSAxMi41SDIyVjIyaC05LjV6Ii8%2BPC9zdmc%2B
[badge-macos]: https://img.shields.io/badge/macOS-Download-333333?style=for-the-badge&logo=apple&logoColor=white
[badge-linux]: https://img.shields.io/badge/Linux-AppImage-E95420?style=for-the-badge&logo=linux&logoColor=white
[badge-snap]: https://img.shields.io/badge/Snap-Snap_Store-82BEA0?style=for-the-badge&logo=snapcraft&logoColor=white
[badge-web]: https://img.shields.io/badge/Web-Try_in_browser-2EA44F?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSIyIj48Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIxMCIvPjxwYXRoIGQ9Ik0yIDEyaDIwTTEyIDJhMTUgMTUgMCAwIDEgMCAyME0xMiAyYTE1IDE1IDAgMCAwIDAgMjAiLz48L3N2Zz4%3D
[windows-msi]: https://github.com/bherbruck/solidcraft/releases/latest/download/solidcraft-windows-x64.msi
[windows-arm64-msi]: https://github.com/bherbruck/solidcraft/releases/latest/download/solidcraft-windows-arm64.msi
[windows-x86-msi]: https://github.com/bherbruck/solidcraft/releases/latest/download/solidcraft-windows-x86.msi
[windows-portable]: https://github.com/bherbruck/solidcraft/releases/latest/download/solidcraft-windows-x64-portable.zip
[macos-dmg]: https://github.com/bherbruck/solidcraft/releases/latest/download/solidcraft-macos-universal.dmg
[linux-appimage]: https://github.com/bherbruck/solidcraft/releases/latest/download/solidcraft-linux-x86_64.AppImage
[linux-deb]: https://github.com/bherbruck/solidcraft/releases/latest/download/solidcraft-linux-x86_64.deb
[linux-rpm]: https://github.com/bherbruck/solidcraft/releases/latest/download/solidcr