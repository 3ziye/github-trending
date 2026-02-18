<div align="center">
  <img src="assets/logo.png" alt="EVCam Logo" width="200"/>
  
  # EVCam - 电车记录仪
  
  <p>
    <strong>针对吉利银河系列车型定制开发的车内环视摄像头行车记录仪应用，兼顾随时远程监看的千里眼功能</strong>
  </p>
  
  <p>
    <img src="https://img.shields.io/badge/Android-9.0+-green?style=flat-square&logo=android" alt="Android"/>
    <img src="https://img.shields.io/badge/API-28+-brightgreen?style=flat-square" alt="API"/>
    <img src="https://img.shields.io/badge/License-GPLv3-blue?style=flat-square" alt="License"/>
    <img src="https://img.shields.io/badge/Language-Java-red?style=flat-square&logo=openjdk&logoColor=white" alt="Java"/>
  </p>
</div>

---

## 📱 项目简介

该应用支持吉利银河系列车型（银河E5、银河L6/L7等），理论上其它龙鹰一号无高阶智驾车型也可通用，同时支持手机端预览。支持同时从最多 **4 个摄像头**进行视频录制与拍照，支持通过**钉钉机器人**远程发送录制、拍照、实时预览指令进行远程监看。

### ✨ 核心特性

- 🎨 **仿FlymeAuto官方UI** - 仿照FlymeAuto官方界面设计，沉浸式状态栏，美观且符合车机使用习惯
- 🎥 **视频录制与照片抓拍** - 支持多摄像头同步录制和实时拍照，可选择参与录制的摄像头
- 👁️ **千里眼远程监看** - 支持钉钉机器人远程查看摄像头画面
-  **不受车速限制** - 随时可开启录制功能，突破官方30km/h车速限制
- 🔄 **自启动与后台保活** - 开机自启动 + 前台服务 + WorkManager + 无障碍服务多重保活机制
- 💾 **多存储位置支持** - 支持内部存储和U盘存储，自动清理超出限制的旧文件
- 🎬 **分段录制** - 支持1/3/5分钟自动分段，方便管理和回放
- ⏱️ **时间戳水印** - 可选在视频和照片上添加时间角标
- 🖼️ **悬浮窗快捷入口** - 可配置大小和透明度的悬浮按钮，实时显示录制状态
- 🌙 **息屏录制（锁车录制）** - 支持熄屏后继续录制，实现锁车监控
- 🔧 **多车型适配** - 支持银河E5、E5-多按钮、银河L6/L7、L7-多按钮、手机及自定义车型

---

## 🛠️ 技术栈

- **开发语言**: Java
- **最低版本**: Android 9.0 (API 28)
- **目标版本**: Android 14+ (API 36)
- **摄像头API**: Camera2 API
- **视频编码**: MediaRecorder（硬编码）/ OpenGL + MediaCodec（软编码）
- **构建工具**: Gradle 8.x (Kotlin DSL)
- **UI组件**: Material Design Components
- **图片加载**: Glide 4.16.0
- **网络库**: OkHttp 4.12.0
- **钉钉集成**: DingTalk Stream SDK 1.3.12
- **后台任务**: WorkManager 2.9.0

### 🚗 支持车型

| 车型 | 摄像头数量 | 录制模式 | 备注 |
|------|-----------|---------|------|
| 银河E5 | 4 | MediaRecorder | 默认车型 |
| 银河E5-多按钮 | 4 | MediaRecorder | 简化操作界面 |
| 银河L6/L7 | 4 | OpenGL+MediaCodec | 自动适配编码模式 |
| 银河L7-多按钮 | 4 | OpenGL+MediaCodec | 简化操作界面 |
| 手机 | 2 | MediaRecorder | 前后摄像头 |
| 自定义车型 | 1/2/4 | 可选 | 完全自定义配置 |

---

## 📦 快速开始

### 环境要求

- **JDK**: 17 或更高版本（推荐 JDK 25）
- **Android Studio**: Hedgehog (2023.1.1) 或更高版本
- **Gradle**: 8.0+
- **测试设备**: Android 9.0+ 的真机（建议具有多个摄像头）

### 克隆项目

```bash
git clone https://github.com/your-username/EVCam.git
cd EVCam
```

### 配置 JDK（Windows）

项目提供了便捷的批处理脚本用于配置 JDK 25：

```batch
# 使用提供的脚本构建（自动设置 JAVA_HOME）
build-with-jdk25.bat
```

或者手动配置环境变量：

```batch
set JAVA_HOME=C:\Program Files\Java\jdk-25.0.2
set PATH=%JAVA_HOME%\bin;%PATH%
```

### 钉钉机器人配置

如需使用远程控制功能，需要配置钉钉机器人：

1. 创建钉钉企业内部应用（Stream模式）
2. 获取 `Client ID`（原 AppKey/SuiteKey）和 `Client Secret`（原 AppSecret/SuiteSecret）
3. 创建 `app/src/main/java/com/kooo/evcam/dingtalk/DingTalkConfig.java`：

```java
package com.kooo.evcam.dingtalk;

public class DingTalkConfig {
    // 钉钉应用凭证（新版参数）
    public static final String CLIENT_ID = "你的Client ID";
    public static final String CLIENT_SECRET = "你的Client Secret";
    
    // 上传模式配置
    public static final boolean ENABLE_UPLOAD = true; // 是否启用上传
}
```

**注意**: 
- 钉钉已将旧版的 AppKey/AppSecret 更名为 Client ID/Client Secret
- 如果不需要钉钉功能，可以在 `MainActivity.java` 中注释掉相关代码

---

## 🔨 构建与安装

### 构建 Debug 版本

```bash
# Windows
gradlew.bat assembleDebug

# Linux/macOS
./gradlew assembleDebug
```

输出位置: `app\build\outputs\apk\debug\app-debug.apk`

### 构建 Release 版本

项目已配置 AOSP 公共测试签名，可直接构建：

```bash
# Windows
gradlew.bat assembleRelease

# Linux/macOS
./gradlew assembleRelease
```

输出位置: `app\build\outputs\apk\release\app-release.apk`

### 安装到设备

```bash
# 安装 Debug 版本
gradlew.bat installDebug

# 或使用 adb 手动安装
adb install app\build\outputs\apk\debug\app-debug.apk
```

---

## 📖 使用指南

### 首次启动

1. **选择车型** - 首次启动会弹出引导界面，选择您的车型（银河E5/L6/L7/手机/自定义）

2. **授予权限** - 请务必使用"应用管家"或其它权限管理软件，授予EVCam所有需要的权限

3. **摄像头预览** - 权限授予后，应用会自动初始化摄像头并显示预览

4. **检查日志** - 点击底部"显示日志"按钮，查看摄像头初始化状态

### 录制视频

1. 点击 **"开始录制"** 按钮（或点击悬浮窗）
2. 所有选中的摄像头同步开始录制
3. 录制自动按设定时长分段（默认1分钟）
4. 录制过程中可以拍照（点击"拍照"按钮）
5. 点击 **"停止录制"** 结束录制

**视频存储位置**: `/sdcard/DCIM/EVCam_Video/`（或 U盘）  
**文件命名格式**: `yyyyMMdd_HHmmss_{position}.mp4`（例如：`20260125_153045_front.mp4`）

### 拍摄照片

- 在预览或录制状态下，点击 **"拍照"** 按钮
- 照片同时从所有活动摄像头抓拍
- 可选择是否添加时间戳水印

**照片存储位置**: `/sdcard/DCIM/EVCam_Photo/`（或 U盘）  
**文件命名格式**: `yyyyMMdd_HHmmss_{position}.jpg`

### 查看录制内容

应用内置了回放和相册功能：

1. 点击左上角菜单图标（☰）
2. 选择 **"视频回放"** 或 **"照片回放"**
3. 点击缩略图可全屏查看/播放
4. 支持多选删除功能

### 悬浮窗功能

启用悬浮窗后，应用切到后台也能方便地控制录制：

- **红色圆点** - 未录制状态
- **绿色闪烁** - 录制中
- **点击** - 打开应用主界面
- **拖动** - 移动悬浮窗位置

在设置中可调整悬浮窗大小（10档可选）和透明度。

### 息屏录制（锁车录制）

开启息屏录制功能后：
- 熄灭屏幕时自动开始录制
- 点亮屏幕时自动停止录制
- 适合锁车后的安全监控场景

### 钉钉远程控制

配置钉钉机器人后，可通过钉钉发送命令：

- `拍照` - 远程拍照并上传
- `录制 <时长>` - 开始录制指定时长（秒）
- `状态` - 查询应用运行状态
- `预览` - 获取当前摄像头预览截图

### 软件设置

点击菜单 → "软件设置"，可配置：

| 设置项 | 说明 |
|--------|------|
| 车型选择 | 选择车型或自定义摄像头配置 |
| 录制模式 | 自动/MediaRecorder/OpenGL+MediaCodec |
| 分段时长 | 1分钟/3分钟/5分钟 |
| 存储位置 | 内部存储/U盘 |
| 存储限制 | 视频和照片的最大存储空间（GB） |
| 录制摄像头 | 选择哪些摄像头参与录制 |
| 悬浮窗 | 开关、大小、透明度 |
| 时间角标 | 是否在视频/照片上添加时间戳 |
| 开机自启 | 开机后自动启动应用 |
| 启动自动录制 | 启动应用后自动开始录制 |
| 息屏录制 | 熄屏时自动录制 |
| 保活服务 | 防止应用被系统杀死 |
| 防止休眠 | 保持设备唤醒状态 |

### 