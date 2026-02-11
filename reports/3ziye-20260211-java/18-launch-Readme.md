# VM 虚拟化与真实代码的博弈
so进阶课程欢迎咨询 微信：xx1193776794
<img width="1817" height="2052" alt="image" src="https://github.com/user-attachments/assets/f8281464-206b-4c97-a7bd-80eab0739088" />
# Launch - Android 设备环境检测与指纹采集

<div align="center">

![Version](https://img.shields.io/badge/version-1.1.2-blue)
![Android](https://img.shields.io/badge/Android-API%2028+-green)
![License](https://img.shields.io/badge/license-Open%20Source-orange)
![Architecture](https://img.shields.io/badge/arch-ARM32%20|%20ARM64%20|%20x86%20|%20x86__64-brightgreen)

**一款开源的 Android 安全检测与设备指纹采集工具**

收集全网特征检测，欢迎各位大佬提供，本 app 无混淆加密，可以查看各种检测点进行对抗

</div>

---

## 📱 项目简介

Launch 是一个专业的 Android 设备安全检测与指纹采集工具，旨在帮助开发者：
- 🛡️ 检测设备环境安全性（Root/Hook/模拟器/调试等）
- 🔐 采集设备指纹信息并进行篡改检测
- 📊 验证机型合法性，识别改机行为
- 🔍 提供多层检测架构，对抗常见 Hook 框架

代码**无混淆无加密**，方便安全研究人员学习和对抗各种检测手段。

---

## ✨ 核心特性

### 🛡️ 环境安全检测

#### Root 检测（2024-2025 最新版本）
- ✅ **Magisk** - 检测文件、挂载点、进程、Zygisk
- ✅ **KernelSU** - 检测文件、内核特征、OverlayFS
- ✅ **APatch** - 检测 SuperKey、KPM 模块
- ✅ **SukiSU** - 检测 SUSFS 隐藏框架（2025 最新）
- ✅ **传统 SU** - su 文件、管理器应用
- ✅ **隐藏模块** - Shamiko、Zygisk-Assistant、HideMyApplist

#### Hook 框架检测
- 🎣 **Xposed** - 框架文件、类加载、堆栈
- 🎣 **LSPosed / EdXposed** - 文件、进程、内存特征
- 🎣 **Frida** - 端口扫描、D-Bus 协议、内存特征、线程检测
- 🎣 **ReZygisk** - 开源 Zygisk 实现检测（2024-2025 新型）
- 🎣 **通用 Hook** - GOT/PLT Hook、Inline Hook、时序异常

#### 模拟器检测
- 📱 **Build 属性** - 检测 generic、test-keys 等特征
- 📱 **硬件特征** - QEMU、VirtualBox、传感器、电池
- 📱 **特定模拟器** - 夜神、雷电、逍遥、BlueStacks、Genymotion
- 📱 **多开/分身** - Virtual Xposed、平行空间等

#### 调试检测
- 🔍 **调试器** - TracerPid、ptrace、调试端口
- 🔍 **调试工具** - IDA、GDB、LLDB 服务端
- 🔍 **时间差** - 指令执行时间异常
- 🔍 **断点检测** - 软件断点、硬件断点

#### 网络检测
- 🌐 **VPN** - 网络接口检测
- 🌐 **代理** - 系统代理、WiFi 代理
- 🌐 **抓包工具** - 证书检测

### 🔐 设备指纹采集

#### 多层采集架构（抗 Hook）
```
Layer 1: Java API 层    → 易被 Xposed/LSPosed Hook
Layer 2: Native libc 层 → 可被 Frida PLT/GOT Hook
Layer 3: Syscall 层     → 直接系统调用，最难 Hook ⭐
```

#### 采集项目
- 📋 **设备标识** - ANDROID_ID、Serial、IMEI、MAC
- 📋 **Build 信息** - FINGERPRINT、MODEL、BRAND 等
- 📋 **硬件信息** - CPU、内存、存储、屏幕、传感器
- 📋 **软件信息** - 系统属性、内核版本、Boot ID
- 📋 **网络信息** - WiFi、IP、运营商

#### 篡改检测
- ✅ 三层数据一致性比对（Java vs Native vs Syscall）
- ✅ N/A 值智能处理
- ✅ 多数据源 fallback 机制
- ✅ 可信度评分

### 📱 机型合法性检测

#### 5 维度评分系统（0-100 分）
| 维度 | 权重 | 检测内容 |
|-----|-----|---------|
| Build 一致性 | 25% | 多层获取结果比对 |
| ROM 特征匹配 | 20% | ROM 属性与品牌匹配 |
| 厂商服务匹配 | 25% | 服务包与品牌匹配 |
| 硬件一致性 | 20% | 硬件参数与机型匹配 |
| FINGERPRINT 格式 | 10% | 格式规范性 |

#### 支持品牌（15+）
- Xiaomi（小米）、Huawei（华为）、Honor（荣耀）
- OPPO、OnePlus（一加）、realme
- vivo、Samsung（三星）、Meizu（魅族）
- Lenovo（联想）、ZTE（中兴）、Sony（索尼）
- Google（谷歌）、ASUS（华硕）、LG、HTC

#### 异常检测
- 🚫 Brand 与 ROM 不匹配（如小米机型有华为服务）
- 🚫 Build.FINGERPRINT 格式异常
- 🚫 硬件参数与声称机型严重不符
- 🚫 厂商服务包混乱（多家厂商服务共存）

---

## 🏗️ 技术架构

### 多层检测架构

```
┌─────────────────────────────────────────────────────────┐
│                    环境检测多层架构                       │
├─────────────────────────────────────────────────────────┤
│                                                         │
│   Layer 1: Java API 层                                  │
│   ├── PackageManager.getPackageInfo()                   │
│   ├── File.exists() / File.canRead()                    │
│   └── 易被 Xposed/LSPosed Hook                          │
│                                                         │
│   Layer 2: Native libc 层                               │
│   ├── access() / stat() / fopen()                       │
│   ├── __system_property_get()                           │
│   └── 可被 Frida PLT/GOT Hook                           │
│                                                         │
│   Layer 3: 直接 Syscall 层 (最可信) ⭐                   │
│   ├── SYS_faccessat - 文件存在检测                       │
│   ├── SYS_openat + SYS_read - 文件读取                   │
│   ├── SYS_getdents64 - 目录遍历                          │
│   └── 绕过 libc，直接 SVC 中断                           │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### 架构设计

- **UI 层**: Material Design 风格，3 个 Fragment 分屏展示
- **业务层**: 检测器（Detector）模块化设计
- **Native 层**: C++ 实现核心检测逻辑
- **Syscall 层**: 汇编实现直接系统调用（ARM64/ARM32/x86/x86_64）

### 项目结构

```
app/src/main/
├── java/com/xff/launch/
│   ├── MainActivity.java              # 主页面
│   ├── SplashActivity.java            # 启动页
│   ├── ui/
│   │   ├── environment/               # 环境检测页面
│   │   ├── fingerprint/               # 指纹采集页面
│   │   └── deviceinfo/                # 机型信息页面
│   ├── detector/
│   │   ├── RootDetector.java          # Root 检测器
│   │   ├── HookDetector.java          # Hook 检测器
│   │   ├── EmulatorDetector.java      # 模拟器检测器
│   │   ├── VendorDatabase.java        # 厂商特征数据库
│   │   └── DeviceLegitimacyDetector.java  # 合法性检测器
│   └── model/                         # 数据模型
├── cpp/
│   ├── native-lib.cpp                 # JNI 入口
│   ├── syscall/
│   │   └── syscall_wrapper.h          # Syscall 封装（支持 4 架构）
│   └── detector/
│       ├── root_detector.cpp          # Native Root 检测
│       ├── hook_detector.cpp          # Native Hook 检测
│