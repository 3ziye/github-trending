# DIJI-NES

<p align="center">
  <img src="https://img.shields.io/badge/Platform-ESP32--S3-blue" alt="Platform">
  <img src="https://img.shields.io/badge/Framework-Arduino-green" alt="Framework">
  <img src="https://img.shields.io/badge/License-GPLv3-red" alt="License">
</p>

> ⚠️ **学习项目 / Learning Project**
> 
> 这是一个用于学习 NES 模拟器原理和嵌入式系统编程的项目。部分功能仍在开发中。
> 
> This is a learning project for understanding NES emulation and embedded systems programming. Some features are still under development.

---

ESP32-S3 上运行的 NES（任天堂红白机）模拟器，支持显示、音频和控制器。

A NES (Nintendo Entertainment System) emulator running on ESP32-S3 microcontroller with display, audio, and controller support.

---

## ✨ 功能特性 / Features

- **完整 CPU 模拟** - 6502 CPU 全指令集 (~150 操作码)
- **PPU 图形** - 背景渲染、滚动、64 个精灵 (8×8 和 8×16 模式)
- **APU 音频** - 方波、三角波、噪声、DMC 通道，通过 I2S DAC 输出
- **双核架构** - Core 0: 音频 + 显示, Core 1: 模拟
- **50 FPS** - 大部分游戏可达到 50 FPS
- **Mapper 支持** - NROM, MMC1, UxROM, CNROM, MMC3 (部分)
- **存档功能** - 快速存档/读档到 SD 卡

---

## 🎮 兼容性 / Compatibility

| Mapper | 名称   | 状态     |
|--------|--------|----------|
| 0      | NROM   | ✅ 正常   |
| 1      | MMC1   | ✅ 正常   |
| 2      | UxROM  | ✅ 正常   |
| 3      | CNROM  | ✅ 正常   |
| 4      | MMC3   | ⚠️ 部分   | 


### Project Status / 项目状态

本项目目前已支持 **NES 前期与中期的大多数游戏**。

对于 NES 后期作品，尤其是依赖 **分屏滚动（split-screen scrolling）** 与 **MMC3 扫描线 IRQ 时序** 的游戏，相关功能仍在持续改进中，可能出现速度或表现异常。

This emulator currently supports the majority of **early- and mid-era NES titles**.

Later-generation games—especially those relying on **split-screen scrolling** and **MMC3 scanline IRQ timing**—are still a work in progress, and may not run at full speed or behave correctly yet.

---

## 📊 性能 / Performance

| 指标       | 数值          |
|------------|---------------|
| 模拟 FPS   | 50-60 FPS     |
| 音频采样率 | 44100 Hz      |
| Flash 使用 | ~460 KB (7%)  |
| RAM 使用   | ~39 KB (12%)  |

---

## 🛠️ 硬件需求 / Hardware

| 组件       | 规格                                              |
|------------|---------------------------------------------------|
| **MCU**    | ESP32-S3-N16R8 (双核 240MHz, 16MB Flash, 8MB PSRAM) |
| **显示屏** | ST7789 TFT LCD 320×240 (SPI)                       |
| **音频 DAC** | MAX98357A I2S DAC                                 |
| **存储**   | SD 卡 (FAT32, 存放 ROM 文件)                       |
| **输入**   | 8 个按键 (直连 GPIO)                              |

---

## 📌 引脚配置 / Pin Configuration

### SD 卡
| 功能   | GPIO |
|--------|------|
| CS     | 42   |
| SCLK   | 40   |
| MISO   | 39   |
| MOSI   | 41   |

### 控制器按键
| 按键   | GPIO |
|--------|------|
| A      | 48   |
| B      | 47   |
| SELECT | 16   |
| START  | 15   |
| UP     | 17   |
| DOWN   | 3    |
| LEFT   | 8    |
| RIGHT  | 18   |

### I2S 音频
| 功能   | GPIO |
|--------|------|
| BCLK   | 5    |
| LRC    | 4    |
| DOUT   | 6    |

### TFT 显示屏
详见 [lgfx_conf.h](src/lgfx_conf.h) (LovyanGFX 配置)。

⚠️ 注意 / Note
部分 TFT 显示屏需要在该文件中启用 颜色反转（invert） 设置，否则可能出现 颜色反了、发白或对比度异常 的情况。
如遇此问题，请在 lgfx_conf.h 中尝试修改：cfg.invert = true;

Some TFT displays require color inversion (invert) to be enabled in this file.
Otherwise, issues such as inverted colors, washed-out colors, or incorrect contrast may occur.
If you encounter these problems, try modifying the following setting in lgfx_conf.h: cfg.invert = true;


---

## 🚀 Build & Upload / 编译与上传
### Prerequisites / 前置条件

- **VS Code**
- **PlatformIO**（VS Code 扩展）
  https://platformio.org/install/ide?install=vscode
- ESP32-S3 USB 驱动（大多数系统会自动安装）

> > ⚠️ **无需手动安装第三方库**  
> 本项目使用 PlatformIO 管理依赖。所有所需库（包括 **LovyanGFX**）将在首次编译时由 PlatformIO 自动下载。
>
> ⚠️ **No manual third-party library installation required**  
> This project uses PlatformIO for dependency management. All required libraries (including **LovyanGFX**) will be automatically downloaded by PlatformIO during the first build.

---

### Option 1: Using PlatformIO (Recommended)  
### 方式一：使用 PlatformIO（推荐）

1. Open this project folder in **VS Code**  
   使用 **VS Code** 打开本项目目录

2. PlatformIO will automatically detect the project and install the required toolchain  
   PlatformIO 会自动识别项目并安装所需工具链

3. Select the correct serial port for your ESP32-S3 board  
   选择正确的 ESP32-S3 串口设备

4. Click **Upload** in PlatformIO to build and flash the firmware  
   点击 PlatformIO 的 **Upload** 按钮进行编译并烧录

---

### 🛠 常见问题排查 / Troubleshooting

**PlatformIO 卡在 “Resolving dependencies…”**

如果 PlatformIO 在配置项目或解析依赖时卡住，通常是由于 PlatformIO 本地环境损坏、缓存问题或权限异常导致的。
可按下列步骤排查：

- 备份并删除 PlatformIO 主目录（将触发依赖重下载）：

```bash
rm -rf ~/.platformio
```

- 检查并修复目录权限（如果删除失败或出现权限错误）：

```bash
sudo chown -R $(whoami) ~/.platformio
```

- 在终端中验证 PlatformIO 可用并更新元数据：

```bash
platformio update
platformio upgrade
```

- 重新启动 VS Code，必要时重新安装 PlatformIO 扩展。

如果问题仍然存在，参考 PlatformIO 官方文档或查看 VS Code 输出面板中的 PlatformIO 日志以获取详细错误信息。

**PlatformIO stuck at "Resolving dependencies..."**

If PlatformIO gets stuck while configuring the project or resolving dependencies, it is often caused by a corrupted cache, permission issues, or a broken local PlatformIO environment.
Try the steps bel