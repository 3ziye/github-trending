# ZenDesktop Premium 🪟✨

[![GitHub License](https://img.shields.io/github/license/Liset999/ZenDesktop?color=blue&style=flat-square)](LICENSE)
[![Platform Windows](https://img.shields.io/badge/Platform-Windows%2011-0078d4?style=flat-square&logo=windows)](https://microsoft.com/windows)
[![Engine Windhawk](https://img.shields.io/badge/Engine-Windhawk%20C%2B%2B-ff69b4?style=flat-square)](https://windhawk.net)

**ZenDesktop Premium v4.0.0** is a high-performance desktop styling suite for Windows 11. It blends 4 native Win32/C++ Windhawk mods with the robust external **ExplorerBlurMica** program, unified under a bespoke Python GUI frontend panel for real-time customizations with **zero background process bloat, zero UI lag, and 0% CPU overhead**.

[简体中文](#-简体中文) | [English](#-english-features)

---

## 🌟 English Features

### 1. 🎛️ Taskbar Acrylic Styler (`local@zen-taskbar-acrylic`)
A native Windows 11 Taskbar beautification module offering fine-grained, premium transparency & blur presets:
* **Clear**: 100% full transparency (only taskbar icons remain).
* **Acrylic (High / Standard / Low)**: Real-time high-fidelity WinUI 3 acrylic glass effect.
* **Apple Liquid Glass**: Hyper-transparent 3D droplet glass with a subtle chromatic dispersion border (featuring diagonal red→orange→green→blue→purple gradient stops), Fresnel specular edge reflections, and a precise 2px corner radius compensation (perfectly matching floating macOS-like Dock layout).

### 2. 🔔 Notification Center Acrylic Styler (`local@zen-notificationcenter-acrylic`)
A premium notification and action center acrylic glass styler co-created by **Lanbo** and **m417z**:
* Brings high-fidelity real-time acrylic and frosted glass effects to the Windows 11 Notification Center, calendar panel, and Quick Settings/System Tray panels.
* Perfectly synchronized with your desktop theme presets, retaining flawless WinUI shadows and smooth animations.

### 3. 🚀 Start Menu Acrylic Styler (`local@zen-startmenu-acrylic`)
Syncs the Start Menu panel seamlessly with your taskbar theme, rendering native acrylic blur overlays over both redesigned and classic Start menu layouts. Features **Apple Liquid Glass** preset with a clear liquid body and expanded folder plates.

### 4. 🖱️ Desktop Icon Toggle and Auto-Hide (`local@zen-desktop-toggle-icons`)
A process-native desktop subclassing module. **Double-click empty desktop space to instantly hide/show icons, and state is preserved across system or explorer restarts.**
* **Persistent Hide State**: Uses local registry keys to ensure desktop icons remain hidden even after system restarts.
* **Full-Screen Window Guard**: Suspends capture tracking when running full-screen games, video players, or active presentations.
* **Zero-Latency Filtering**: Blocks synthetic `WM_MOUSEMOVE` messages triggered by `SysListView32` when toggling visibility to eliminate screen flicker.

### 5. 📁 File Explorer Transparency (`ExplorerBlurMica` - External Program)
* **Author Acknowledgement**: Developed by **Maplespe** ([Maplespe/ExplorerBlurMica](https://github.com/Maplespe/ExplorerBlurMica)).
* Adds exquisite visual effects like Blur, Acrylic, and Mica to Windows 10/11 File Explorer.
* Visual customization via config editor and registered as a native shell extension DLL (`regsvr32`).

### 6. 🎛️ ZenDesktop Customizer (`ZenDesktopCustomizer.py` - Frontend Panel)
* Developed by **Lanbo**, this CustomTkinter GUI wrapper provides a unified dashboard to configure taskbar, start menu, and notification center options.
* Integrates quick actions for ExplorerBlurMica (Register/Enable, Configure Visuals, and Uninstall/Disable) via elevated actions.

---

## 📥 Installation & Deployment Guide

> [!IMPORTANT]
> The suite utilizes **pure local compilation** (`local@` prefix), which means your system compiles the C++ code natively. It is 100% offline-ready, safe, and completely bypasses official Windhawk mod server connection failures!

### Step 1: Install Windhawk
Install Windhawk on your Windows 11 PC using the provided setup.

### Step 2: One-Key Local Registry & Mod Deployment
1. Right-click **`deploy.bat`** and select **Run as Administrator** (以管理员身份运行).
2. The script will automatically stop the Windhawk service, register the 4 premium local mods, enable local compilation, reset compiler caching keys, and restart Windhawk safely.

### Step 3: Fast Native Compilation
1. Open the **Windhawk** user interface. You will see 4 newly registered local mods in your home dashboard.
2. Click into each mod and click **Save / Compile** (保存并编译). The engine will compile the native C++ code in ~10 seconds.

### Step 4: Run Visual Control Center
1. Launch **`run_customizer.bat`** to start the frontend configuration GUI.
2. Go to the **资源管理器 (Explorer)** tab, click **注册/启用透明效果 (Register & Enable)** to apply File Explorer blur.
3. Use other tabs to customize Taskbar, Start Menu, and Notification Center styles.

---

## 🇨🇳 简体中文

### 💎 v4.0.0 核心更新与优势
* **四合一 Mod + 资源管理器透明程序**：弃用了以前不稳