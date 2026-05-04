# ZenCrop v2.2.4

[中文文档](doc/README_zh.md)

An independent, **enhanced** reimplementation of [PowerToys Crop And Lock](https://github.com/microsoft/PowerToys/tree/main/src/modules/CropAndLock/).

---
## 🔥 V2.2.0 & V2.2.1 Massive Update: The Ultimate Thumbnail Mode

We've completely rewritten the **Thumbnail Mode (Ctrl+Alt+C)**, breaking through the limits of the Windows DWM API to deliver features you won't find anywhere else:

- **Strict Proportional Scaling**: Resize the cropped thumbnail freely via window edges or third-party tools like **AltSnap**. ZenCrop mathematically locks the aspect ratio so your crop never stretches and never shows black bars.
- **Engine-Defeating Invisible Rendering**: Hide the original target window from your screen and taskbar entirely! Using a groundbreaking "1-pixel anchor" hack combined with COM interface manipulation, we trick modern engines (Chromium, Electron, WinUI) into rendering at a full 60 FPS in the background without pausing. Meanwhile, **V2.2.1** brings back the ZenCrop taskbar icon for the *Thumbnail window itself*, making it effortlessly easy to manage and bring to the front when buried behind other apps.

📖 *Deep dive: [ZenCrop Thumbnail Scaling & Hiding Technology](doc/thumbnail_scaling_hiding_technology_en.md)*
---

## 🚀 Why ZenCrop over PowerToys?

While the official PowerToys module suffers from an ["all-white/black screen" known issue](https://learn.microsoft.com/en-us/windows/powertoys/crop-and-lock#known-issues) when trying to reparent modern Windows applications (UWP/WinUI/XAML apps like Calculator or Settings), **ZenCrop has completely solved this.**

ZenCrop successfully supports interactive cropping of applications that the original PowerToys Crop And Lock explicitly cannot handle, utilizing two distinct cutting-edge rendering engines:

**1. Native Viewport Cropping Technology:**
- **Windows Calculator, Settings, Microsoft To Do** (Modern UWP apps)
- Completely bypasses the "all-white screen" rendering bug by manipulating the window region instead of forcing a cross-process DWM visual tree attachment.
📖 *Deep dive: [ZenCrop Viewport Technology Implementation Report](doc/viewport_technology_report_en.md)*

**2. Deep Visual Tree Radar & Advanced Reparenting:**
- **Windows 11 Paint** (Modern `DesktopChildSiteBridge` WinUI 3 apps)
- **Magpie** and other traditional Win32 apps nesting modern XAML components (`DesktopWindowContentBridge`)
- Intelligently circumvents fragile DWM composition rules, applies smart dark-mode background camouflage to prevent washed-out colors, and utilizes inverse coordinate compensation to perfectly align the crop without triggering fallback titlebars or crashes.
📖 *Deep dive: [WinUI 3 Reparenting Technical Report](doc/WinUI3_Reparenting_Fix.md)*

## Background

PowerToys Crop And Lock is a module in the Microsoft PowerToys toolkit that allows users to crop any window into a sub-window and pin it on screen. However, the original project is deeply tied to the PowerToys framework, making it difficult to use independently or customize.

ZenCrop is rebuilt from scratch, runs completely standalone without PowerToys, and provides a lighter solution while preserving and exceeding the core functionality.

## Features

- **Smart Reparent Mode**: Crops a target window into an independent child window. ZenCrop automatically detects modern UWP/WinUI applications (like Calculator or Settings) and seamlessly falls back to a special **Viewport** mode. This prevents the "all-white" rendering bug associated with standard reparenting, ensuring all apps remain interactive.
- **Thumbnail Mode**: Displays a live DWM thumbnail of the target window with a cornflower blue border. *New in V2.2.0 & V2.2.1:* the target window is stealthily hidden from the taskbar and screen while keeping Chromium/Electron engines rendering at 60 FPS, and the thumbnail itself displays its own taskbar icon for easy window management. Supports strict proportional scaling via native window edge dragging or third-party tools like AltSnap.
📖 *Deep dive: [ZenCrop Thumbnail Scaling & Hiding Technology](doc/thumbnail_scaling_hiding_technology_en.md)*
- **Always On Top**: Press `Alt+T` to pin any window on top of all others, with a customizable border (color, opacity, thickness, rounded corners)
- **Customizable Hotkeys**: All hotkeys can be customized in Settings — click the input field and press your desired key combo
- **Crop On Top**: Optionally auto-pin cropped windows on top (configurable in Settings)
- **Smart Window Detection**: The crop overlay automatically follows the mouse, dynamically highlighting the window under the cursor — crop any window on screen
- **Smart Content Detection**: UI Automation-based element detection — the overlay automatically identifies the UI element under the cursor (browser title bar, address bar, content area, etc.) and suggests a crop region with a red dashed border
- **Click to Accept**: Single-click accepts the smart suggestion; drag to ma