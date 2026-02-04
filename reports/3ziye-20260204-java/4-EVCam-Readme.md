<div align="center">
  <img src="assets/logo.png" alt="EVCam Logo" width="200"/>
  
  # EVCam - 电车记录仪
  
  <p>
    <strong>针对吉利银河系列车型定制开发的车内环视摄像头行车记录仪应用，兼顾随时远程监看的千里眼功能</strong>
  </p>
  
  <p>
    <img src="https://img.shields.io/badge/Android-9.0+-green?style=flat-square&logo=android" alt="Android"/>
    <img src="https://img.shields.io/badge/API-28+-brightgreen?style=flat-square" alt="API"/>
    <img src="https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey?style=flat-square" alt="License"/>
    <img src="https://img.shields.io/badge/Commercial-Contact%20Author-orange?style=flat-square" alt="Commercial"/>
    <img src="https://img.shields.io/badge/Language-Java-red?style=flat-square&logo=openjdk&logoColor=white" alt="Java"/>
  </p>
</div>

---

## 📱 项目简介

该应用支持吉利银河系列车型（银河E5、银河L6/L7等），理论上其它龙鹰一号无高阶智驾车型也可通用，同时支持手机端预览。支持同时从最多 **4 个摄像头**进行视频录制与拍照，支持通过**钉钉机器人**或**微信小程序**远程发送录制、拍照、实时预览指令进行远程监看。

### ✨ 核心特性

- 🎨 **仿FlymeAuto官方UI** - 仿照FlymeAuto官方界面设计，沉浸式状态栏，美观且符合车机使用习惯
- 🎥 **视频录制与照片抓拍** - 支持多摄像头同步录制和实时拍照，可选择参与录制的摄像头
- 👁️ **千里眼远程监看** - 支持钉钉机器人和微信小程序两种方式远程查看摄像头画面
- 📱 **微信小程序控制** - 扫码绑定设备，支持远程拍照、录像、实时预览和文件管理
- 🚗 **不受车速限制** - 随时可开启录制功能，突破官方30km/h车速限制
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
- **微信云开发**: 微信小程序 + 云函数 + 云数据库 + 云存储
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

### 微信小程序配置

如需使用微信小程序远程控制功能：

#### 1. 小程序端配置

1. 在微信开发者工具中打开 `wechat-miniprogram/` 目录
2. 创建云开发环境（微信开发者工具 → 云开发 → 创建环境）
3. 修改 `app.js` 中的云开发环境ID：

```javascript
wx.cloud.init({
  env: 'your-cloud-env-id',  // 替换为您的云开发环境ID
  traceUser: true,
});
```

4. 部署云函数（右键 `cloudfunctions/` 下每个文件夹 → 上传并部署）

#### 2. 车机端配置

创建 `app/src/main/java/com/kooo/evcam/wechat/WechatMiniConfig.java`：

```java
package com.kooo.evcam.wechat;

public class WechatMiniConfig {
    // 微信小程序凭证
    public static final String APP_ID = "你的小程序AppID";
    public static final String APP_SECRET = "你的小程序AppSecret";
    
    // 云开发环境ID
    public static final String CLOUD_ENV = "your-cloud-env-id";
}
```

**注意**: 
- 需要已认证的小程序才能使用云开发
- 云数据库需要创建 `devices`、`commands`、`files` 三个集合
- 详细架构说明参见 `wechat-miniprogram/ARCHITECTURE.md`

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
**文件命名格式**: `yy