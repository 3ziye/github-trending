# MicYou

<p align="center">
  <img src="./img/app_icon.png" width="128" height="128" />
</p>

<p align="center">
  <a href="./README_zh-cn.md">简体中文</a> | <a href="./README_zh-tw.md">繁體中文</a> | <b>English</b>
</p>

<p align="center">
  <a href="https://github.com/LanRhyme/MicYou/blob/master/LICENSE">
    <img alt="LICENSE" src="https://img.shields.io/badge/license-MIT-green"></a>
  <a href="https://github.com/LanRhyme/MicYou/stargazers">
    <img alt="Github Stars" src="https://img.shields.io/github/stars/LanRhyme/MicYou?style=flat&logo=github&logoColor=white"><a>
  <a href="https://github.com/LanRhyme/MicYou/releases/latest">
    <img alt="GitHub Release" src="https://img.shields.io/github/v/release/LanRhyme/MicYou?logo=github"></a>
  <a href="https://qm.qq.com/q/V16hPpWPKO">
    <img alt="QQ" src="https://img.shields.io/badge/QQ-995452107-12B7F5?style=flat&logo=qq&logoColor=white"><a>
  <a href="https://aur.archlinux.org/packages/micyou-bin">
    <img alt="AUR Version" src="https://img.shields.io/aur/version/micyou-bin?logo=archlinux&label=micyou-bin"></a>
  <a href="https://crowdin.com/project/micyou" target="_blank" rel="noopener noreferrer">
    <img alt="Crowdin" src="https://badges.crowdin.net/micyou/localized.svg"></a>
</p>

<h6 align="center">Built in</h6>

<p align="center">
  <img alt="Kotlin" src="https://img.shields.io/badge/kotlin-%237F52FF.svg?style=for-the-badge&logo=kotlin&logoColor=white" />
  <img alt="Jetpack Compose" src="https://img.shields.io/badge/Jetpack_Compose-4285F4?style=for-the-badge&logo=jetpackcompose&logoColor=white">
</p>

<h6 align="center">Platform we support</h6>

<p align="center">
  <img alt="Android" src="https://img.shields.io/badge/Android-3DDC84?style=for-the-badge&logo=android&logoColor=white" />
  <img alt="Windows" src="https://custom-icon-badges.demolab.com/badge/Windows-0078D6?&style=for-the-badge&logo=windows11&logoColor=white" />
  <img alt="Linux" src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" />
  <img alt="macOS" src="https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=apple&logoColor=F0F0F0" />
</p>

MicYou is a powerful tool that turns your Android device into a high-quality wireless microphone for your PC. Built with Kotlin Multiplatform and Jetpack Compose/Material 3.

Based on the [AndroidMic](https://github.com/teamclouday/AndroidMic) project.

## Features

- **Multiple Connection Modes**: Support for Wi-Fi, USB (ADB/AOA), and Bluetooth.
- **Audio Processing**: Built-in Noise Suppression, Auto Gain Control (AGC), and Dereverberation.
- **Cross-Platform**:
  - **Android Client**: Modern Material 3 interface, dark/light theme support.
  - **Desktop Server**: Receive audio on Windows/Linux/macOS.
- **Virtual Microphone**: Works seamlessly with VB-Cable to act as a system microphone input.
- **Customizable**: Adjust sample rate, channel count, and audio format.

## Screenshots

### Android App
|                        Main Screen                        |                           Settings                            |
|:---------------------------------------------------------:|:-------------------------------------------------------------:|
| <img src="img/android_screenshot_main.png" width="300" /> | <img src="img/android_screenshot_settings.png" width="300" /> |

### Desktop App
<img src="img/desktop_screenshot.png" width="600" />

## Getting Started

### 1. Download ADB
- Download from [Android Developers](https://developer.android.com/tools/releases/platform-tools?hl=zh_cn)
- Install via package manager
  - `winget install -e --id Google.PlatformTools`
  - `sudo apt install android-tools-adb`
  - `sudo pacman -S android-tools`
  - ...

In most cases ADB will be added to your environment variables automatically. If not, please add it manually.

### 2. Enable USB Debugging
Using OneUI 8 as an example

1. Go to Settings, tap `About phone`
2. Tap `Software information`, find `Build number`, tap it **7** times. When you see "No need, developer mode has been enabled", it means the developer mode has been successfully enabled.
3. Go back to Settings, tap `Developer options`, find `USB debugging`, and enable it.

### 3. USB connection
Use a stable data cable, and set the connection mode to `USB` on both the desktop app and the Android app.

### 4. Wi-Fi connection
Ensure your Android device and PC are on the same network, and set the connection mode to `Wi-Fi` on both the desktop app and the Android app.

### Android
1. Download and install the APK on your Android device.
2. Ensure your device is on the same network as your PC (for Wi-Fi) or connected via USB.

### Windows
1. Run the desktop application.
2. Configure the connection mode to match the Android app.

### macOS

> [!IMPORTANT]
> If you are using an Apple Silicon Mac, Bluetooth mode cannot be used without Rosetta 2 translation.

To ensure your experience, you need to install some dependencies via Homebrew:

~~~bash
brew install bla