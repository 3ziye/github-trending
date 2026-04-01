# Andclaw 🤖

<p align="center">
  <img src="./icon.png" alt="Andclaw Logo" width="120">
</p>

[![Android](https://img.shields.io/badge/Android-9%2B-brightgreen?logo=android)](https://www.android.com/)
[![Kotlin](https://img.shields.io/badge/Kotlin-2.3.10-blue?logo=kotlin)](https://kotlinlang.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Website](https://img.shields.io/badge/官网-andclaw.app-blue?logo=googlechrome&logoColor=white)](https://andclaw.app/)
[![Install](https://img.shields.io/badge/在线安装-立即下载-green?logo=android&logoColor=white)](https://andclaw.app/#/install)

> **让 AI 像人类一样使用你的手机** —— 完全在设备上运行，无需 Root，无需电脑。

<p align="center">
  <a href="https://andclaw.app/"><b>🌐 官方网站</b></a> &nbsp;|&nbsp;
  <a href="https://andclaw.app/#/install"><b>📲 在线安装 APK</b></a>
</p>

---

## 🌟 核心亮点

| 特性 | 说明 |
|------|------|
| **🚫 无需 Root** | 纯无障碍服务实现，不依赖系统权限 |
| **💻 无需电脑** | 完全在手机上独立运行，无需 ADB 或 PC 端配合 |
| **🧠 AI 驱动** | 支持 Kimi Code（Anthropic 格式）、Moonshot 和任意 OpenAI 兼容 API |
| **👁️ 屏幕感知** | 实时读取 UI 层次结构 + WebView/浏览器场景自动截图辅助视觉分析 |
| **🤏 拟人操作** | 模拟点击、滑动、长按、文本输入等手势操作 |
| **📸 多媒体能力** | 拍照、录像、录屏、截图、音量控制 |
| **📱 设备管控** | Device Owner 模式下支持企业级设备管理（静默装卸、Kiosk 等） |
| **🤖 远程控制** | **Telegram Bot** 或 **微信 ClawBot（基于 iLink）** 双通道：远程下发指令；截图/媒体回传能力因通道而异（见下文） |
| **🌍 多语言支持** | 支持中文、英文界面切换 |

## 📋 与其他方案对比

| 特性 | Andclaw | [Open-AutoGLM](https://github.com/zai-org/Open-AutoGLM) | [肉包 Roubao](https://github.com/Turbo1123/roubao) | 豆包手机 |
|-----|:-------:|:--------:|:-------:|:-------:|
| 无需电脑 | ✅ | ❌ 需 PC 运行 Python | ✅ | ✅ |
| 无需专用硬件 | ✅ | ✅ | ✅ | ❌ 需购买 3499 元工程机 |
| 无需 Shizuku / ADB | ✅ 无障碍服务 | ❌ ADB 控制 | ❌ 依赖 Shizuku | ✅ |
| 远程控制 | ✅ Telegram / ClawBot | ❌ | ❌ | ❌ |
| 自定义模型 | ✅ 多 Provider | ✅ | ✅ | ❌ 仅豆包 |
| 开源 | ✅ | ✅ | ✅ | ❌ |
| 原生 Android | ✅ Kotlin | ❌ Python | ✅ Kotlin | ✅ |


**Andclaw 的核心差异**：
- **零外部依赖**：基于 Android 无障碍服务，无需 Shizuku 初始化、无需 ADB 连接、无需电脑
- **远程控制**：支持 **Telegram Bot** 与 **微信 ClawBot（基于 iLink）** 两种通道远程下发指令；截图与多媒体回传在 Telegram 侧为真实文件发送，在 ClawBot 侧当前为**文本降级说明**（详见「远程通道」）
- **UI 层级 + 视觉双模感知**：优先解析 Accessibility 节点树，WebView/浏览器场景自动切换截图分析
- **循环检测 + 截图重试**：同一动作重复 5 次自动截图视觉重试，避免 Agent 死循环

---

## 📱 演示

[![演示视频](docs/demo_cover.png)](https://www.bilibili.com/video/BV1k8w4zeEL7)  
[![演示视频](docs/ScreenShot_2026-03-17_202610_426.png)](https://www.bilibili.com/video/BV1WtwKzLEXd)

### 界面截图

<p align="center">
  <b>主界面</b>：设备管理员模式、网络状态、远程连接通道（Telegram / 飞书 / ClawBot）与对话记录入口<br>
  <img src="docs/screenshots/b726d0df2b63d8b7cc2b83eacec0c2c4.png" alt="Andclaw 主界面：设备管理与远程连接" width="320"><br><br>
  <b>远程连接</b>：单通道配置；图示为 ClawBot（微信）桥接已连接、已登录<br>
  <img src="docs/screenshots/03583636640228432acca1430b1acec2.png" alt="远程连接设置页：ClawBot 与桥接状态" width="320"><br><br>
  <b>AI Agent</b>：本地对话界面与任务执行进度、完成反馈<br>
  <img src="docs/screenshots/8b3b7975a19d1911e651a966ba48504d.png" alt="Andclaw AI Agent 对话界面" width="320">
</p>

---

## 🚀 快速开始

### 环境要求

- **Android 版本**: Android 12 (API 31) 或更高
- **无障碍服务**: 需要在 `设置 > 无障碍` 中手动启用
- **悬浮窗权限**: 用于显示紧急停止按钮
- **API Key**: 从 [Kimi Code](https://www.kimi.com/code/console)、[Moonshot 开放平台](https://platform.moonshot.cn/) 或任意 OpenAI 兼容 API 提供商获取

### 安装方式

**方式一：在线安装使用Chrome浏览器（推荐）**

使用Chrome浏览器直接访问 [andclaw.app/#/install](https://andclaw.app/#/install)，然后按提示操作即可。

**方式二：从源码编译**

1. **克隆仓库**
   ```bash
   git clone https://github.com/andforce/Andclaw.git
   cd Andclaw
   ```

2. **编译安装**
   ```bash
   ./gradlew :app:installDebug
   ```

3. **授予权限**
   - 打开应用后，按提示启用**无障碍服务**
   - 授予**显示在其他应用上层**权限

4. **激活 Device Owner**

   通过 ADB 激活（仅首次设置需要），激活后 Andclaw 获得企业级设备管理能力：

   > ⚠️ **重要**：由于 Android 安全限制，设备必须先**恢复出厂设置**才能启用 Device Owner 模式。不启用 Device Owner 模式，AI操作手机的权限将大幅受限。

   ```bash
   adb shell dpm set-device-owner com.andforce.andclaw/.DeviceAdminReceiver
   ```

   - ✅ **应用管理**：静默安装/卸载应用、隐藏/显示/挂起应用、阻止卸载、自动授予权限、查询已安装应用列表
   - ✅ **设备控制**：远程锁屏、重启、恢复出厂设置、禁用摄像头/状态栏/锁屏、USB 数据传输控制、定位开关
   - ✅ **Kiosk 模式**：单应用锁定（Lock Task）、替换默认桌面、禁止安全模式/恢复出厂

   > 详细能力清单见 [ACTIONS.md](./ACTIONS.md)

6. **创建 Telegram 机器人**

   1. 在 Telegram 中搜索并打开 **@BotFather**
   2. 发送 `/newbot` 创建新机器人
   3. 按提示设置机器人名称和用户名（用户名必须以 `bot` 结尾）
   4. 创建成功后，复制提供的 **Bot Token**（格式如：`123456789:ABCdefGHIjklMNOpqrsTUVwxyz`）
   5. 在 Andclaw 设置页面中填入 Bot Token

---

## 🎯 使用方式

### 1. 文字指令

直接告诉 Andclaw 你想做什么：

| 指令示例 | AI 执行过程 |
|---------|------------|
| "打开bilibili，搜索AI学习相关的视频，并播放" | 识别B站图标 → 点击 → 进入搜索页 → 输入"AI学习" → 点击搜索 → 选择视频 → 播放 |

### 2. AI Agent 工作循环

```
用户指令
    ↓
[1.5s] → 捕获屏幕 UI 树（无障碍服务）
    ↓
浏览器/WebView？──是──→ 自动截图（视觉分析辅助）
    ↓                          ↓
发送给 LLM（系统提示 + 最近 12 条历史 + 屏幕数据 [+ 截图]）
    ↓
AI 返回 JSON 操作决策
    ↓
解析失败？──是──→ 纠正提示重试（1 次）
    ↓
执行操作（点击/滑动/输入/Intent/DPM/拍照/录屏/...）
    ↓
[2.5s] → 重新捕获屏幕  ←──────────────┐
    ↓                                   │
循环检测（同一操作连续 5 次？）             │
    ↓是                                  │
截图 + 视觉重试（最多 3 轮，15 次后停止）    │
    ↓否                                  │
任务完成？──否──────────────────────────-─┘
    ↓
是 → 结束
```

### 3. 支持的操作类型

| 类型 | 说明 |
|------|------|
