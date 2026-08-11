# DJOneHub：Mac 来电提醒增强版

这是在 [DJOneHub](https://github.com/ZenGeekLabs/DJOneHub) 基础上做的 macOS 改造版。原项目解决了大疆第一代 4G 模块在 Mac 上的短信、eSIM 与 USB 4G 上网；这一版把重点放在“模块长期插在 Mac 上时，能不能像一张真正的电话卡一样被看见”。

> [!IMPORTANT]
> 📦 **一键安装包已上传**：[Releases](https://github.com/rogerbush007-a11y/DJOneHub-mac-enhanced/releases) 提供三个 macOS 版本与 Windows 实验版，macOS 版双击“安装 DJOneHub.command”一键安装，无需终端命令：
> - `DJOneHub-macOS-arm64-v0.1.7-preview.dmg`：修复新电脑上模块无法获得 IPv4 的问题（自动创建/启用 4G 网卡服务并配置 DHCP）
> - `DJOneHub-macOS-arm64-v0.1.6-preview.dmg`：新增信号自检与自动找回、USB 打开超时保护
> - `DJOneHub-macOS-arm64-v0.1.5-preview.dmg`：新增 4G 网卡 DHCP 自动续租（模块重连后自动恢复 4G 自动联网）
> - `DJOneHub-macOS-universal-v0.1.3-preview.dmg`：支持 Apple Silicon 与 Intel Mac（⚠️ 未在真实 Intel 机型实测，谨慎下载）
> - `DJOneHub-macOS-arm64-v0.1.2-preview.dmg`：菜单栏不含网速显示
> - `DJOneHub-macOS-arm64-v0.1.1-preview.dmg`：保留菜单栏实时网速显示
> - `DJOneHub-Windows-amd64-v0.1.4-preview.exe`：Windows 实验版（⚠️ 未在真实 Windows + 模块环境实测，USB AT/eSIM 不可用，谨慎下载）
>
> 更新内容见 [CHANGELOG.md](CHANGELOG.md)。

## 这次改了什么

![Mac 来电与短信原生提醒，号码和验证码均已遮挡](docs/images/macos-call-and-sms-notifications-redacted.png)

| 改造 | 实现效果 |
| --- | --- |
| 来电提醒 | 有电话打进实体 SIM 时，Mac 显示紧凑的原生来电卡片，网页关掉后也能继续提醒，可直接拒接。 |
| 短信提醒 | 收到新短信会显示同一套原生提醒，验证码不必一直盯着管理网页。 |
| 网页面板 | 首页增加来电监控、通话记录与拒接；短信、信号、工作模式与 4G 控制保留在同一页。 |
| 网络策略 | Wi-Fi 优先，Wi-Fi 不可用时由 USB 4G 兜底；手动关闭 4G 后，短信和来电监听仍保持。 |
| 本地定位 | 默认关闭；启动后在本机显示定位结果并定时刷新，菜单栏出现 GPS 图标，停止后自动移除。 |

### 通话探索（实验）

这部分尚未接入正式功能，记录给希望继续协作的开发者：

| 项目 | 当前结果 |
| --- | --- |
| USB 接口扫描 | 本机枚举到 **9 个 USB 接口**（编号 0–8）；接口 6–8 属于 USB Audio，输入端点为 `0x8a`，输出端点为 `0x06`。 |
| macOS 音频识别 | macOS 已识别模块的 USB 音频输入与输出，显示为单声道 8 kHz；主机侧可以打开设备并采集 PCM。 |
| 控制验证 | 已验证来电状态、接听与挂断控制；音频媒体尚未进入 macOS。 |
| 已排除项 | 临时关闭 GPS 对 USB NMEA 的输出后，媒体数据仍未出现，不是当前阻塞点。 |
| 当前失败项 | 标准 PCM/UAC 路由启用方式被现有固件拒绝；音频模式命令还存在“返回错误但运行时状态改变”的异常，因此不能直接作为正式功能使用。 |

下一步需要：不同模块批次或版本的接口对比、原厂设备工作时的只读接口行为记录，以及匹配的接口资料或已知正常样本。所有进一步测试优先放在备用模块，未知私有命令不做猜测写入。

来电提醒和“在 Mac 上接听电话”是两件事。目前已经完成来电状态监听和拒接；模块还没有暴露出可用的双向通话音频，因此暂不支持 Mac 接听或通话。

![Mac 来电监控面板，号码末四位已遮挡](docs/images/macos-call-panel-redacted.png)

## 原项目基础能力

程序及管理页面均在本机运行，默认只监听 `127.0.0.1:7575`，不会主动把 SIM、短信或卡片资料上传到远程服务器。

> [!IMPORTANT]
> DJOneHub 是非官方第三方项目，与 DJI、Quectel、运营商及 eSIM 卡片厂商不存在隶属、授权或合作关系。

| 功能 | 状态 | 说明 |
| --- | --- | --- |
| 模块自动识别 | 已实现 | 识别大疆第一代 4G 模块，并处理拔出、重新连接和换卡 |
| 模块状态 | 已实现 | 显示运营商、信号、网络制式、SIM 状态和当前工作模式 |
| 短信管理 | 已实现 | 接收、发送、自动轮询、验证码提取及模块旧短信清理 |
| eSIM Profile | 已实现 | 读取、下载、启用、改名和删除兼容 eUICC 卡片中的 Profile |
| Profile 号码资料 | 已实现 | 将手动填写的号码保存到模块通讯录，并按 ICCID 关联 Profile |
| USB 4G 上网 | 已实现 | 切换 USB 网卡模式，让 macOS 使用 SIM 卡流量上网 |
| 网络与流量 | 已实现 | 查看 USB 网卡、默认出口、代理连通性、实时速度和本次流量 |
| AT 调试 | 已实现 | 在网页中直接向模块发送 AT 指令 |
| 深浅色外观 | 已实现 | 支持浅色、深色和跟随系统 |
| Intel Mac | 实验支持 | universal 安装包已提供 arm64 + x86_64 双架构；未在真实 Intel 机型实测，谨慎使用 |
| Windows | 实验支持 | 提供 amd64 单文件 exe；USB 直连 AT/eSIM 依赖 macOS 不可用，需通过串口连接模块；未在真实 Windows 环境实测，谨慎使用 |

## 改造实现说明

这一份私有维护分支在原项目基础上补充了更适合长期插在 Mac 上使用的能力：

- 短信监听与 USB 4G 上网可以同时保持可用；Wi-Fi 正常时优先走 Wi-Fi，断开后由 4G 自动兜底。
- 实体 SIM 来电和新短信会通过常驻的 macOS 小通知显示；来电可直接拒接。
- 4G 拨块可强制禁止 Mac 使用蜂窝数据，同时保留短信与来电监听。
- 4G 被关闭时，网页流量读数会清空，避免把历史数值误认为仍在使用蜂窝网络。

这里的“来电”只包含实时提醒与拒接。模块尚未向 macOS 暴露可用的双向通话音频，因此不能在 Mac 上接听或通话。

所有功能均通过模块已有 USB 接口实现，不修改模块固件。不同 SIM、运营商、macOS 版本和模块批次的实际表现可能不同。

### 改造源码入口

这三个部分是本分支的重点，不在 Release 二进制或截图里，而是直接保存在源码中：

| 功能 | 对应源码 |
| --- | --- |
| 来电状态监听、历史记录与拒接接口 | [`calls.go`](cmd/djonehub-macos/calls.go) |
| 网页面板：来电卡片、拒接按钮、短信与 4G 拨块 | [`index.html`](cmd/djonehub-macos/web/index.html)、[`app.js`](cmd/djonehub-macos/web/app.js)、[`style.css`](cmd/djonehub-macos/web/style.css) |
| 关闭网页后仍显示的原生来电、短信提醒 | [`macOS 通知助手`](macos/DJOneHubNotifier) |

通知助手是独立的 Swift macOS App；在其目录执行 `./build-app.sh` 即可构建。它只访问本机 `127.0.0.1:7575`，不读取 USB 接口，也不会上传短信和号码。

## 接入准备

### 硬件

- 大疆第一代 4G 模块
- 可正常使用的实体 SIM，或与当前实现兼容的实体 eUICC/eSIM 卡片
- 支持数据传输的 USB-C 线缆
- Apple Silicon Mac

模块的 USB 设备标识通常为 `2ca3:4006`。如果连接后 macOS 完全没有发现 USB 设备，请优先确认线缆支持数据传输。

### 系统

- macOS 13 Ventura 或更新版本
- 当前发行包支持 Apple Silicon，即 M1、M2、M3、M4 及后续 Apple 芯片
- Intel Mac 版本尚未发布和真机验证

发行包已经携带运行所需的 `libusb`。普通用户不需要安装 Homebrew、Go、Node.js 或其他开发环境。

### 指示灯

| 状态 | 常见含义 |
| --- | --- |
| 红色常亮 | 未插入 SIM 卡 |
| 红色闪烁 | SIM 卡未被正常识别 |
| 绿色常亮 | SIM 已识别，蜂窝信号通常较好 |
| 绿色闪烁 | SIM 已识别，蜂窝信号可能较弱或仍在注册 |

不同固件的灯光行为可能存在差异，最终应以网页中的 SIM、信号和网络注册状态为准。

## 接入原理

大疆第一代 4G 模块通过不同的 USB 组合模式向 macOS 暴露管理接口或网络接口。DJOneHub 没有修改模块固件，而是根据模块现有 USB 接口实现本机通信，并预设了常用的短信模式和上网模式。

| 模式 | 页面名称 | 主要用途 |
| --- | --- | --- |
| 模式 0 | 短信模式 | 读取状态、收发短信、管理 eSIM 和发送 AT 指令 |
| 模式 1 | 上网模式 | 向 macOS 暴露 USB 网卡，通过 SIM 卡流量上网 |
| 模式 2 | 实验模式 2 | 用途尚未确认，不建议日常使用 |
| 模式 3 | 实验模式 3 | 用途尚未确认，不建议日常使用 |

切换模式时，模块会重新枚举 USB 接口，页面可能短暂显示设备断开。请等待系统重新识别，不要在 eSIM Profile 写入等关键操作过程中拔出模块或切换模式。

## 下载

除 ZIP 外，还提供一键安装的 DMG 安装包：下载后双击“安装 DJOneHub.command”即可完成安装，无需终端命令。版本按喜好选择：

- `DJOneHub-macOS-universal-v0.1.3-preview.dmg`：Apple Silicon 与 Intel Mac 通用（⚠️ **风险提示**：Intel 版未在真实机型上实际测试，可能有兼容性问题，谨慎下载）。
- `DJOneHub-macOS-arm64-v0.1.7-preview.dmg`：Apple Silicon，修复新电脑上插入调试好的模块无法获得有效 IPv4、无法上网的问题（自动识别/启用/创建 4G 网卡服务并续租 DHCP）。
- `DJOneHub-macOS-arm64-v0.1.6-preview.dmg`：Apple Silicon，新增信