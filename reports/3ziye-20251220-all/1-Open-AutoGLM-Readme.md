# Open-AutoGLM

[Readme in English](README_en.md)

<div align="center">
<img src=resources/logo.svg width="20%"/>
</div>
<p align="center">
    👋 加入我们的 <a href="resources/WECHAT.md" target="_blank">微信</a> 社区
</p>
<p align="center">
    🎤 进一步在我们的产品 <a href="https://autoglm.zhipuai.cn/autotyper/" target="_blank">智谱 AI 输入法</a> 体验“用嘴发指令”
</p
><p align="center">
    <a href="https://mp.weixin.qq.com/s/wRp22dmRVF23ySEiATiWIQ" target="_blank">AutoGLM 实战派</a> 开发者激励活动火热进行中，跑通、二创即可瓜分数万元现金奖池！成果提交 👉 <a href="https://zhipu-ai.feishu.cn/share/base/form/shrcnE3ZuPD5tlOyVJ7d5Wtir8c?from=navigation" target="_blank">入口</a>
</p>

## 懒人版快速安装

你可以使用Claude Code，配置 [GLM Coding Plan](https://bigmodel.cn/glm-coding) 后，输入以下提示词，快速部署本项目。

```
访问文档，为我安装 AutoGLM
https://raw.githubusercontent.com/zai-org/Open-AutoGLM/refs/heads/main/README.md
```

## 项目介绍

Phone Agent 是一个基于 AutoGLM 构建的手机端智能助理框架，它能够以多模态方式理解手机屏幕内容，并通过自动化操作帮助用户完成任务。系统通过
ADB(Android Debug Bridge)来控制设备，以视觉语言模型进行屏幕感知，再结合智能规划能力生成并执行操作流程。用户只需用自然语言描述需求，如“打开小红书搜索美食”，Phone
Agent 即可自动解析意图、理解当前界面、规划下一步动作并完成整个流程。系统还内置敏感操作确认机制，并支持在登录或验证码场景下进行人工接管。同时，它提供远程
ADB 调试能力，可通过 WiFi 或网络连接设备，实现灵活的远程控制与开发。

> ⚠️
> 本项目仅供研究和学习使用。严禁用于非法获取信息、干扰系统或任何违法活动。请仔细审阅 [使用条款](resources/privacy_policy.txt)。

## 模型下载地址

| Model                         | Download Links                                                                                                                                                         |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AutoGLM-Phone-9B              | [🤗 Hugging Face](https://huggingface.co/zai-org/AutoGLM-Phone-9B)<br>[🤖 ModelScope](https://modelscope.cn/models/ZhipuAI/AutoGLM-Phone-9B)                           |
| AutoGLM-Phone-9B-Multilingual | [🤗 Hugging Face](https://huggingface.co/zai-org/AutoGLM-Phone-9B-Multilingual)<br>[🤖 ModelScope](https://modelscope.cn/models/ZhipuAI/AutoGLM-Phone-9B-Multilingual) |

其中，`AutoGLM-Phone-9B` 是针对中文手机应用优化的模型，而 `AutoGLM-Phone-9B-Multilingual` 支持英语场景，适用于包含英文等其他语言内容的应用。

## Android 环境准备

### 1. Python 环境

建议使用 Python 3.10 及以上版本。

### 2. 手机调试命令行工具

根据你的设备类型选择相应的工具：

#### 对于 Android 设备 - 使用 ADB

1. 下载官方 ADB [安装包](https://developer.android.com/tools/releases/platform-tools?hl=zh-cn)，并解压到自定义路径
2. 配置环境变量

- MacOS 配置方法：在 `Terminal` 或者任何命令行工具里

  ```bash
  # 假设解压后的目录为 ~/Downloads/platform-tools。如果不是请自行调整命令。
  export PATH=${PATH}:~/Downloads/platform-tools
  ```

- Windows 配置方法：可参考 [第三方教程](https://blog.csdn.net/x2584179909/article/details/108319973) 进行配置。

#### 对于鸿蒙设备 (HarmonyOS NEXT版本以上) - 使用 HDC

1. 下载 HDC 工具：
   - 从 [HarmonyOS SDK](https://developer.huawei.com/consumer/cn/download/) 下载
2. 配置环境变量

- MacOS/Linux 配置方法：

  ```bash
  # 假设解压后的目录为 ~/Downloads/harmonyos-sdk/toolchains。请根据实际路径调整。
  export PATH=${PATH}:~/Downloads/harmonyos-sdk/toolchains
  ```

- Windows 配置方法：将 HDC 工具所在目录添加到系统 PATH 环境变量

### 3. Android 7.0+ 或 HarmonyOS 设备，并启用 `开发者模式` 和 `USB 调试`

1. 开发者模式启用：通常启用方法是，找到 `设置-关于手机-版本号` 然后连续快速点击 10
   次左右，直到弹出弹窗显示“开发者模式已启用”。不同手机会有些许差别，如果找不到，可以上网搜索一下教程。
2. USB 调试启用：启用开发者模式之后，会出现 `设置-开发者选项-USB 调试`，勾选启用
3. 部分机型在设置开发者选项以后, 可能需要重启设备才能生效. 可以测试一下: 将手机用USB数据线连接到电脑后, `adb devices`
   查看是否有设备信息, 如果没有说明连接失败.

**请务必仔细检查相关权限**

![权限](resources/screenshot-20251209-181423.png)

### 4. 安装 ADB Keyboard(仅 Android 设备需要，用于文本输入)

**注意：鸿蒙设备使用原生输入方法，无需安装 ADB Keyboard。**

如果你使用的是 Android 设备：

下载 [安装包](https://github.com/senzhk/ADBKeyBoard/blob/master/ADBKeyboard.apk) 并在对应的安卓设备中进行安装。
注意，安装完成后还需要到 `设置-输入法` 或者 `设置-键盘列表` 中启用 `ADB Keyboard` 才能生效(或使用命令`adb shell ime enable com.android.adbkeyboard/.AdbIME`[How-to-use](https://github.com/senzhk/ADBKeyBoard/blob/master/README.md#how-to-use))

## iPhone 环境准备

### 1. Python 环境

建议使用 Python 3.10 及以上版本。

### 2. 设置 WebDriverAgent 

WebDriverAgent 是 iOS 自动化的核心组件,需要在 iOS 设备上运行。

注意：需要提前安装好Xcode、并注册好苹果开发者账号（不需要付费）

#### 1. 克隆 WebDriverAgent

```bash

git clone https://github.com/appium/WebDriverAgent.git
cd WebDriverAgent
```
在 Xcode 中打开WebDriverAgent.xcodeproj

#### 2. 设置 Signing & Capabilities

![设置签名](resources/setup-xcode-wda.png)

把Bundle ID改成 YOUR_NAME.WebDriverAgentRunner。

#### 3. 开始UI测试

需要在Finder勾选过“在WiFi中显示这台iPhone”，且Mac与iPhone处于同一WiFi网络之下，可以不用连接数据线，即可在设备中选择到。

**注意：** 不建议插数据线运行，因为插数据线还必须要同时运行iproxy才可以把端口映射出来，不及直接WiFi运行稳定。

先从项目Target选择WebDriverAgentRunner，然后再选择你的设备。

![选择设备](resources/select-your-iphone-device.png)

选好后，长按"▶️"运行按钮选择“Test”后开始编译并部署到你的iPhone上。

![信任设备](resources/start-wda-testing.png)

这时需要你在iPhone上输入解锁密码，在设置 -> 通用 -> VPN与设备管理 中信任开发者App，还需要在 设置 -> 开发者  中，打开UI自动化设置。



![信任设备](resources/trust-dev-app.jpg)

![启用UI自动化](resources/enable-ui-automation.jpg)

## 部署准备工作

### 1. 安装依赖

```bash
pip install -r requirements.txt 
pip install -e .
```

### 2. 配置 ADB 或 HDC

#### 对于 Android 设备

确认 **USB数据线具有数据传输功能**, 而不是仅有充电功能

确保已安装 ADB 并使用 **USB数据线** 连接设备：

```bash
# 检查已连接的设备
adb devices

# 输出结果应显示你的设备，如：
# List of devices attached
# emulator-5554   device
