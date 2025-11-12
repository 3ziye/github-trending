# Turbo IMS

<div align="center">
  <img src="Turboims.png" width="200" alt="Turbo IMS Logo"/>

  <h3>Enhanced IMS Configuration Tool for Google Pixel Devices</h3>

  [![Android](https://img.shields.io/badge/Android-14%2B-green.svg)](https://www.android.com/)
  [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
  [![Version](https://img.shields.io/badge/Version-3.0-brightgreen.svg)](https://github.com/Turbo1123/TurboIMS/releases)

  English | [简体中文](README_CN.md)
</div>

---

## 📱 About

**Turbo IMS** is an enhanced fork of the original [IMS project by vvb2060](https://github.com/vvb2060/Ims), designed to enable VoLTE, VoWiFi, VoNR, and other advanced IMS features on Google Pixel phones through privileged system configuration.

This enhanced version includes a modernized UI, improved user experience, automatic language detection, and additional convenience features while maintaining full compatibility with the original implementation.

## ✨ New Features in Turbo IMS

### 🎨 **Modern UI Redesign**
- Professional logo and branding
- Clean, Material Design-inspired interface
- Enhanced splash screen with version display
- Improved visual feedback and status indicators

### 🌍 **Automatic Language Detection**
- Automatically detects system language on first launch
- Chinese interface for Chinese users (zh-CN, zh-TW, zh-HK, etc.)
- English interface for all other regions
- Manual language switching available

### 📡 **Quick Network Settings Access**
- One-tap jump to network settings after successful configuration
- Convenient dialog prompts after applying configuration
- Streamlined workflow for testing IMS features

### 🎯 **Per-SIM Configuration**
- Select specific SIM card (SIM 1 or SIM 2)
- Apply configuration to individual SIMs or all SIMs at once
- Clear visual feedback for selected SIM

### 🔄 **Improved User Experience**
- Auto-return to app after configuration
- Clear success/failure notifications
- Android version detection with QPR2 Beta 3+ warnings
- Real-time Shizuku status monitoring

## 🎯 Key Features

### IMS Features Configuration
- ✅ **VoLTE** (4G Voice) - High-definition voice calling over 4G LTE
- ✅ **VoWiFi** (WiFi Calling) - Make calls over WiFi networks
- ✅ **VT** (Video Calling) - IMS-based video calls
- ✅ **VoNR** (5G Voice) - High-definition voice over 5G NR
- ✅ **Cross-SIM Calling** - Dual-SIM interconnection
- ✅ **UT Supplementary Services** - Call forwarding, waiting, etc.
- ✅ **5G NR** (NSA/SA) - Enable 5G standalone/non-standalone networks

### System Requirements
- Google Pixel device (tested on Pixel 6+)
- Android 14 or higher
- [Shizuku](https://github.com/RikkaApps/Shizuku) installed and running
- Shizuku permission granted to Turbo IMS

## 🚀 Installation

### Method 1: Download APK (Recommended)
1. Download the latest APK from [Releases](https://github.com/Turbo1123/TurboIMS/releases)
2. Install the APK on your Pixel device
3. Grant necessary permissions

### Method 2: Build from Source
```bash
# Clone the repository
git clone https://github.com/Turbo1123/TurboIMS.git
cd TurboIMS

# Build debug APK
./gradlew assembleDebug

# Install to connected device
adb install -r app/build/outputs/apk/debug/app-debug.apk
```

## 📖 Usage Guide

### Prerequisites Setup
1. **Install Shizuku**
   - Download from [GitHub](https://github.com/RikkaApps/Shizuku/releases) or Google Play
   - Start Shizuku service (via Wireless debugging or Root)

2. **Grant Permissions**
   - Open Turbo IMS
   - Grant Shizuku permission when prompted

### Configuring IMS Features

1. **Check System Status**
   - Verify Android version is displayed
   - Ensure Shizuku status shows "✅ Ready"

2. **Select SIM Card**
   - Tap "Select SIM Card" button
   - Choose SIM 1, SIM 2, or "Apply to All SIM Cards"

3. **Enable Features**
   - Toggle switches for desired IMS features
   - All features are enabled by default

4. **Apply Configuration**
   - Tap the blue "Apply Configuration" button
   - Wait 3 seconds for configuration to complete
   - App will automatically return to foreground
   - Choose "Go to Network Settings" to verify features

### Important Notes

⚠️ **Android 16 QPR2 Beta 3+ Users**
- Configuration is non-persistent on Android 16 Beta builds
- Settings will reset after reboot
- You must reapply configuration after each restart

✅ **Verifying Configuration**
- Go to Settings → Network & Internet → SIMs
- Check that VoLTE, VoWiFi options are visible
- Make a test call to verify functionality

## 🛠️ Technical Details

### Architecture
- **Privileged Process**: Uses Android Instrumentation to run with system privileges
- **Shizuku Integration**: Leverages Shizuku framework for privilege escalation
- **CarrierConfigManager**: Directly modifies carrier configuration bundles
- **Shell Permission Delegation**: Temporary NETWORK_SETTINGS permission

### Configuration Keys Modified
The app modifies the following carrier configuration keys:
- `KEY_CARRIER_VOLTE_AVAILABLE_BOOL`
- `KEY_CARRIE