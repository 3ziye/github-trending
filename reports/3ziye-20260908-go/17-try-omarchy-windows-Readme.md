<p align="center">
  <img src="app/OmarchyIcon.svg" width="128" height="128" alt="Try Omarchy logo">
</p>

<h1 align="center">Try Omarchy for Windows</h1>

Run the full [Omarchy](https://omarchy.org) desktop in a window on Windows 10 or 11. No VMware, no VirtualBox, no dual boot: QEMU on the Windows Hypervisor Platform (WHPX), a prebuilt Arch image with Omarchy baked in, and the desktop rendered on your actual GPU (virgl + Venus Vulkan via [WINQ-EMU](https://github.com/cmspam/winq-emu)) with CPU rendering as the automatic fallback. No partitions, no bootloader, no changes to your Windows install: everything lives in one folder chosen on first run, with `%LOCALAPPDATA%\TryOmarchy` as the default.

Download, boot, Hyprland.

![The Omarchy desktop running in the Try Omarchy window on Windows](docs/images/hero.jpg)

![Live capture on the Ryzen 5 test laptop: fastfetch, the Omarchy menu, and a screensaver inside the Try Omarchy window](docs/images/demo.gif)

**Status: working end to end on real hardware.** One app switches on Windows' virtualization, downloads the GPU runtime and the image, boots, and supervises; the desktop renders on the GPU and falls back to CPU rendering automatically. Landing page: [tryomarchy.com](https://tryomarchy.com). See the [changelog](CHANGELOG.md) for release history.

Try Omarchy for Windows is maintained under [Omacom](https://github.com/omacom),
alongside [Try Omarchy for macOS](https://github.com/omacom/try-omarchy).
The Omarchy mark in the app icon is sourced from the
[official Omarchy brand kit](https://omarchy.org/brand/) and remains subject to
Omarchy's trademark rights.

## What works today

- **The full Omarchy 4.0.2 desktop on new or reset guests**: Hyprland, the bar, notifications, all 22 themes, the screensavers. On our mid-range Ryzen 5 test laptop the desktop is up about 6 seconds after launch, and every launch after setup goes straight there. No Linux login screens, no console text, branded window.
- **GPU acceleration**: Hyprland renders on the host GPU via virgl, `vulkaninfo` shows Venus, smooth video and audio (verified on a Radeon iGPU laptop); `-cpu host` (AVX2 and all) via WINQ-EMU's patched WHPX.
- **One app, zero prerequisites**: `TryOmarchy.exe` (~8 MB, no console window). First run lets you keep the default Local AppData location or choose another local drive or folder, switches on Windows' Hypervisor Platform (one permission prompt, one restart), then downloads the SHA256-verified GPU runtime and image and boots into Omarchy's setup form. Once setup is complete it keeps a stable launcher in the chosen data folder and can add optional Start-menu and Desktop shortcuts. After that it supervises everything: GPU/CPU auto-detect, the known WHPX launch wedge, in-guest reboot relaunch, poweroff cleanup.
- **Feels like an app, not a VM**: the window is branded "Try Omarchy", the Windows key acts as Super only while the window is focused (Start menu and Win+Shift+S keep working everywhere else), Ctrl+Alt+F goes fullscreen.
- **Two-way text and image clipboard sharing** between Windows and Omarchy (own compositor-native bridge over wl-clipboard, no SPICE) and **folder sharing** over virtio-9p: standard installs offer to create `Omarchy Shared` in your Windows home, then pin it in Omarchy's Files sidebar and link it into the Linux home. The tray can open the Windows folder at any time. File clipboard and drag-and-drop are not supported yet; use the shared folder to move files.
- First boot offers an instant trial account or Omarchy's normal personalized account setup, with SDDM autologin after either path. Instant mode keeps `omarchy` as both the local username and lock-screen password, shows that on the setup splash, and repeats it once on the first desktop. Sudo remains passwordless in this disposable local trial.
- Reproducible x86_64 guest image build (containerized, package-locked, pinned Omarchy revision) and a headless QMP control plane for automated testing.

See [app compatibility](docs/COMPATIBILITY.md) for package support and current VM limitations. The [v1 checklist](docs/V1-READINESS.md) tracks the remaining release work.

| First run | Screensaver |
|---|---|
| ![Omarchy first-run setup inside the Try Omarchy window](docs/images/first-run.jpg) | ![Omarchy pixel-logo screensaver](docs/images/screensaver.jpg) |

## Essential keys

- **Windows key** acts as Super, but only while the Try Omarchy window is focused. Everywhere else it stays your normal Windows key, so the Start menu and Win+Shift+S keep working.
- **Ctrl+Alt+F** fullscreens the VM window itself on your Windows desktop (SUPER+F, below, is the in-Omarchy one).
- **Ctrl+Alt+G** grabs or releases raw keyboard input. If the host steals a shortcut you meant for Omarchy, grab first. Same trick if you're driving the VM over VNC or RDP and focus gets weird.
- Hyprland is keyboard-first by design and the first hour is the adjustment period. Learn two keys and the rest follows: **SUPER+SPACE** opens the