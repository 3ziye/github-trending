# Sing-Box Launcher

[![GitHub](https://img.shields.io/badge/GitHub-Leadaxe%2Fsingbox--launcher-blue)](https://github.com/Leadaxe/singbox-launcher)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Go Version](https://img.shields.io/badge/Go-1.24%2B-blue)](https://golang.org/)
[![Version](https://img.shields.io/badge/version-0.2.0-blue)](https://github.com/Leadaxe/singbox-launcher/releases)

Cross-platform GUI launcher for [sing-box](https://github.com/SagerNet/sing-box) - universal proxy client.

**Repository**: [https://github.com/Leadaxe/singbox-launcher](https://github.com/Leadaxe/singbox-launcher)

**🌐 Languages**: [English](README.md) | [Русский](README_RU.md)

## 📑 Table of Contents

- [📸 Screenshots](#-screenshots)
- [🚀 Features](#-features)
- [💡 Why this launcher?](#-why-this-launcher)
- [📋 Requirements](#-requirements)
- [📦 Installation](#-installation)
- [📖 Usage](#-usage)
  - [First Launch](#first-launch)
  - [Main Features](#main-features)
  - [Config Wizard (v0.2.0)](#config-wizard-v020)
  - [System Tray](#system-tray)
- [⚙️ Configuration](#️-configuration)
  - [Config Template (config_template.json)](#config-template-config_templatejson)
  - [Enabling Clash API](#enabling-clash-api)
  - [Subscription Parser Configuration](#subscription-parser-configuration)
- [🔄 Subscription Parser - Detailed Logic](#-subscription-parser---detailed-logic)
- [🏗️ Project Architecture](#️-project-architecture)
- [🐛 Troubleshooting](#-troubleshooting)
- [🔁 Auto-restart & Stability](#-auto-restart--stability)
- [🔨 Building from Source](#-building-from-source)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [🙏 Acknowledgments](#-acknowledgments)
- [📞 Support](#-support)
- [🔮 Future Plans](#-future-plans)

## 📸 Screenshots

### Core Dashboard
![Core Dashboard](https://github.com/user-attachments/assets/660d5f8d-6b2e-4dfa-ba6a-0c6906b383ee)

### Clash API
![Clash API Dashboard](https://github.com/user-attachments/assets/389e3c08-f92e-4ef1-bea1-39074b9b6eca)

![Clash API in Tray](https://github.com/user-attachments/assets/9801820b-501c-4221-ba56-96f3442445b0)

### Config Wizard
![Config Wizard](https://github.com/user-attachments/assets/07d290c1-cdab-4fd4-bd12-a39c77b3bd68)

## 🚀 Features

- ✅ **Cross-platform**: Windows (fully tested), macOS and Linux (testing needed - help welcome!)
- 🎯 **Simple Control**: Start/stop VPN with one button
- 🧙 **Config Wizard** (v0.2.0): Visual step-by-step configuration without editing JSON
- 📊 **Clash API Integration**: Manage proxies via Clash-compatible API
- 🤖 **Auto-loaders**: Automatic proxy loading from Clash API on startup
- 🔄 **Automatic Configuration Update**: Parse subscriptions and update proxy list
- 🔁 **Auto-restart**: Intelligent crash recovery with stability monitoring
- 📈 **Diagnostics**: IP check, STUN, file verification
- 🔔 **System Tray**: Run from system tray with proxy selection
- 📝 **Logging**: Detailed logs of all operations

## 💡 Why this launcher?

### ❌ The Problem

Most Windows users run sing-box like this:

- 📁 `sing-box.exe` + `config.json` in the same folder  
- ⚫ Black CMD window always open  
- ✏️ To switch a node: edit JSON in Notepad → kill the process → run again  
- 📝 Logs disappear into nowhere  
- 🔄 Manual restart every time you change config

### ✅ The Solution

This launcher solves all of that. Everything is controlled from one clean GUI:

### 🎯 What it gives you

- 🚀 **One-click start/stop for TUN mode**  
- 📝 **Full access to `config.json` inside the launcher**  
  (edit → save → sing-box restarts automatically)
- 🔄 **Auto-parsing of any subscription type**  
  (vless / vmess / trojan / ss / hysteria / tuic)  
  + filters by tags and regex
- 🌐 **Server selection with ping via Clash Meta API**  
- 🔧 **Diagnostics tools**: IP-check, STUN test, process killer  
- 📊 **System tray integration + readable logs**

**🔗 Links:**
- **GitHub:** https://github.com/Leadaxe/singbox-launcher  
- **Example config:** https://github.com/Leadaxe/singbox-launcher/blob/main/bin/config.example.json

## 📋 Requirements

### Windows
- Windows 10/11 (x64)
- [sing-box](https://github.com/SagerNet/sing-box/releases) (executable file)
- [WinTun](https://www.wintun.net/) (wintun.dll) - MIT license, can be distributed

### macOS & Linux

**⚠️ Testing Needed**: macOS and Linux support is implemented but not yet fully tested. We're looking for help with testing and feedback!

**Requirements:**
- macOS 10.15+ (Catalina or newer) or modern Linux distribution (x64)
- [sing-box](https://github.com/SagerNet/sing-box/releases) (executable file)

If you can help test on macOS or Linux, please open an issue or pull request on GitHub!

## 📦 Installation

### Windows

1. Download the latest release from [GitHub Releases](https://github.com/Leadaxe/singbox-launcher/releases)
2. Extract the archive to any folder (e.g., `C:\Program Files\singbox-launcher`)
3. Place `config.json` in the `bin\` folder:
   - Copy `config.example.json` to `config.json`