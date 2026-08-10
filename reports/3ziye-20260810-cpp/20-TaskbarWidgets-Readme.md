<p align="center">
  <img src="assets/branding/logo.png" alt="Taskbar Widgets logo" width="112" height="112" />
</p>

<h1 align="center">Taskbar Widgets</h1>

<p align="center">
  Useful, live widgets that feel at home on the Windows 11 taskbar.
</p>

<p align="center">
  <a href="https://github.com/pfcdev/TaskbarWidgets/releases/latest"><img alt="Latest release" src="https://img.shields.io/github/v/release/pfcdev/TaskbarWidgets?sort=semver&display_name=tag&style=flat-square" /></a>
  <a href="https://github.com/pfcdev/TaskbarWidgets/releases"><img alt="Total release downloads" src="https://img.shields.io/github/downloads/pfcdev/TaskbarWidgets/total?style=flat-square&label=downloads&color=8B5CF6" /></a>
  <img alt="Windows 11 x64" src="https://img.shields.io/badge/Windows%2011-x64-0078D4?style=flat-square&logo=windows11&logoColor=white" />
  <a href="LICENSE"><img alt="MIT License" src="https://img.shields.io/badge/license-MIT-22c55e?style=flat-square" /></a>
</p>

<p align="center">
  <a href="https://github.com/pfcdev/TaskbarWidgets/releases/latest/download/TaskbarWidgetsSetup-x64.exe"><img alt="Download the latest installer" src="https://img.shields.io/badge/DOWNLOAD-LATEST%20INSTALLER-2563EB?style=for-the-badge&logo=windows11&logoColor=white" /></a>
</p>

<p align="center">
  <a href="https://github.com/pfcdev/TaskbarWidgets/releases/latest">Release notes</a>
  ·
  <a href="https://github.com/pfcdev/TaskbarWidgets/releases/latest/download/TaskbarWidgets-portable-x64.zip">Portable ZIP</a>
  ·
  <a href="README.tr.md">Türkçe</a>
</p>

<p align="center">
  <img src="assets/social/taskbar-widgets-v0.5.34-ultrawide-promo-v4-matte.png" alt="Taskbar Widgets collection on Windows 11" />
</p>

Taskbar Widgets is a free, open-source app for **Windows 11 x64**. It puts useful
information and controls directly on your taskbar without replacing the Windows
shell. Choose only the widgets you want, arrange them by dragging, and manage
everything from one Settings app.

## What's new in 0.5.34

- Rebuilt Media Player with a compact native layout, artwork-derived color
  gradient, and filled previous, play or pause, and next controls.
- Added a real-time, session-aware WASAPI FFT visualizer that reacts to the
  active media stream and settles during silence.
- Added visualizer bar count, sensitivity, peak level, position, centered mode,
  and optional baseline controls.
- Added configurable control placement, pause artwork overlay, inactive or
  paused auto-hide, and smooth scrolling for long track titles.
- Improved live media-state updates and rendering consistency across multiple
  taskbars and monitor scaling levels.

> [!IMPORTANT]
> Taskbar Widgets is beta software and integrates with private Windows 11 XAML
> surfaces. A Windows update may temporarily affect compatibility. If the
> current taskbar layout is unsupported, the integration disables itself instead
> of forcing a potentially unstable layout.

## See it in action

<table>
  <tr>
    <td align="center">
      <img src="assets/readme/widget-gallery/collage-productivity.png" alt="Codex Status, Discord Voice and Parking Lot widgets" /><br />
      <strong>Work and communication</strong>
    </td>
    <td align="center">
      <img src="assets/readme/widget-gallery/collage-media-weather.png" alt="Weather and Media Player widgets" /><br />
      <strong>Weather and media</strong>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="assets/readme/widget-gallery/collage-system-monitoring.png" alt="CPU, memory, storage and network widgets" /><br />
      <strong>Live system monitoring</strong>
    </td>
    <td align="center">
      <img src="assets/readme/widget-gallery/collage-utilities.png" alt="Steam Downloads and Parking Lot widgets" /><br />
      <strong>Downloads and quick file parking</strong>
    </td>
  </tr>
</table>

## Get started

1. [Download the latest installer](https://github.com/pfcdev/TaskbarWidgets/releases/latest/download/TaskbarWidgetsSetup-x64.exe).
2. Run the installer and leave **Start Taskbar Widgets** selected on the final page.
3. Open the notification-area icon and choose **Open Settings**.
4. Enable the widgets you want, then drag them directly along the taskbar.

The app starts with Windows when that option is selected during installation.
You can later enable or disable all widgets from the notification-area menu
without uninstalling anything.

> [!NOTE]
> Unsigned beta releases may show a Windows SmartScreen warning. The release page
> includes a SHA-256 checksum so you can verify the installer before running it.

## One Settings app, every widget

<p align="center">
  <img src="docs/images/settings-library.png" alt="Taskbar Widgets Settings showing the Widget Library" />
</p>

The Widget Library is the central place to:

- enable, disable and configure widgets;
- choose a taskbar position for each widget;
- switch between side-by-side and rotation layouts;
- install Community widgets and review their permissions;
-