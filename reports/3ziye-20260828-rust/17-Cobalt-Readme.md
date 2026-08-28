<p align="center">
  <img src="docs/logo.svg" width="220" alt="Cobalt">
</p>

<p align="center"><strong>Apps and an SDK for Kobo e-readers.</strong></p>

<p align="center">
  <a href="https://github.com/BandarLabs/Cobalt/actions/workflows/ci.yml"><img src="https://github.com/BandarLabs/Cobalt/actions/workflows/ci.yml/badge.svg?branch=main" alt="CI"></a>
  <a href="https://github.com/BandarLabs/Cobalt/actions/workflows/apps.yml"><img src="https://github.com/BandarLabs/Cobalt/actions/workflows/apps.yml/badge.svg?branch=main" alt="Publish apps"></a>
  <a href="https://github.com/BandarLabs/Cobalt/releases/latest"><img src="https://img.shields.io/github/v/release/BandarLabs/Cobalt?color=brightgreen" alt="Latest release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/BandarLabs/Cobalt?color=brightgreen" alt="License"></a>
</p>

Cobalt is an open-source application platform for Kobo. It provides a launcher,
an App Store, a Rust SDK, a runtime with capability isolation, and a Clara BW
simulator.

After one USB installation, users can install, update, and remove signed apps
over Wi-Fi. App releases are independent from Cobalt platform releases, so a
new app can appear in Store without reinstalling or updating Cobalt.

<p align="center">
  <a href="docs/cobalt-tour.mp4">
    <img src="docs/tour.gif" height="600" alt="A real Kobo Clara BW running Audiobook Studio, Gutenbird, Terminal, Components, Hacker News, Sidekick, AI Command Center, Feeds, Tic-tac-toe and audio playback, followed by the full App Store catalog and Sudoku being installed, played, removed and reinstalled over Wi-Fi">
  </a><br>
  <sub>Recorded on a Kobo Clara BW at 3× speed: apps, Store discovery, and the complete Sudoku install lifecycle.</sub>
</p>

> [!IMPORTANT]
> The **Kobo Clara BW N365 (device code 391)**, **Kobo Elipsa 2E N605 (device
> code 389)**, **Kobo Clara HD N249 (device code 376)**, **Kobo Libra 2 N418
> (device code 388)**, **Kobo Clara Colour N367 (device code 393)**, and
> **Kobo Libra Colour N428 (device code 390)** are
> fully hardware-tested on the exact firmware and kernel versions in the
> support matrix. See the
> [device support matrix](docs/DEVICES.md#device-support-matrix) before
> installing.
> The 2025 **Kobo Clara BW P365 (device code 395)** hardware refresh is also
> supported: its measured panel, touch, firmware, and kernel facts match the
> attended-tested N365 Clara BW.
> It is an independent project and is not affiliated with Rakuten Kobo.

> [!TIP]
> **Own an unsupported Kobo? Help test its port.** No coding is required.
> [Join an existing device thread or create a new one](https://github.com/BandarLabs/Cobalt/issues)
> with your exact model, firmware, and whether you can run attended tests.
> Start with read-only checks; run panel tests only against the commit named
> by a maintainer. See
> [Contributing](CONTRIBUTING.md#device-testing).

## Features

- Signed Wi-Fi app installation, updates, and removal
- Shareable app pages with encrypted QR or pairing-code installation
- Separate Settings-based updates for the Cobalt platform
- Apps run as separate unprivileged processes
- Per-app capability checks for network, storage, audio, frontlight, and other
  device services
- Declarative e-ink UI toolkit and browser simulator
- Profile-driven full and partial refresh planning for supported panels
- Static ARMv7 binaries with no device-side package manager
- Recovery-safe app and catalog transactions

## How it differs

[NickelMenu](https://pgaskin.net/NickelMenu/) adds actions to Kobo's stock
menu. [KOReader](https://koreader.rocks/) and
[Plato](https://github.com/baskerville/plato) are reading apps. Cobalt is a
platform for building and installing apps.

Cobalt handles the common parts: screens, app lifecycle, drawing to the e-ink
display, partial refreshes, touch input, device access, process isolation,
testing, and signed installs. App authors can focus on their app instead of
building those parts again.
See the [FAQ](https://bandarlabs.github.io/Cobalt/faq.html) for a fuller
comparison.

## Apps

Every screenshot below is a real capture from a Kobo Clara BW. Store manages
the installable applications; Settings and Terminal remain protected system
utilities.

<table>
<tr>
<td width="33%" valign="top"><a href="examples/launcher/README.md"><img width="230" src="examples/launcher/screenshots/home.png" alt="Cobalt launcher showing a grid of applications"></a><br><b><a href="examples/launcher/README.md">Launcher</a></b><br>Opens installed apps and always keeps a route back to the Kobo reader.</td>
<td width="33%" valign="top"><a href="docs/APP_STORE.md"><img width="230" src="examples/store/screenshots/catalog.png" alt="Cobalt App Store listing installed and available applications"></a><br><b><a href="docs/APP_STORE.md">App Store</a></b><br>Browses signed apps and installs, updates, removes, and reinstalls them over Wi-Fi.</td>
<td width="33%" valign="top"><a href="apps/sudoku/"><img width="2