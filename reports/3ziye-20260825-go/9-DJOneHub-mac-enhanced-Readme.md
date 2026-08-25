# DJOneHub

> 让大疆第一代 4G 模块成为 Mac 上长期可用的实体 SIM 终端。

DJOneHub 是一个非官方开源项目。它通过模块已有 USB 接口提供短信、4G、GPS、eSIM、来电及通话控制，不修改模块固件。

## 文档导航

- [当前版本与更新](#v129v125--v129-更新汇总)
- [版本演进](#版本演进)
- [下载与安装](#下载与平台状态)
- [完整使用说明](#完整使用说明)
- [常用命令](#常用命令)
- [日志卸载与故障排查](#日志与本地数据)
- [从源码构建](#从源码构建)

主页同时保留当前版本说明和早期使用文档。标有“历史”的内容用于说明版本演进；当前安装与操作请以 v1.2.9 章节为准。

## v1.2.9：v1.2.5 — v1.2.9 更新汇总

[下载 v1.2.9](https://github.com/rogerbush007-a11y/DJOneHub-mac-enhanced/releases/tag/v1.2.9)

### 通话与首次启用

- 独立 macOS App 集中管理拨号、接听、拒接、挂断、DTMF、通话记录、录音入口、短信、通讯录与设置；来电、短信提醒不需要网页常驻。
- 新模块、原始 DJI 配置、旧 UAC 与其他工具留下的完整 USB 配置均可识别。启用前先备份，验证失败自动回滚。
- 旧 UAC `…1,1,1,1,1,0,1` 已具备 USB Audio，不再强写 ADB 位，只补 IMS / VoLTE，避免模块返回 `OK` 但配置保持原样时误报失败。
- USB 模式切换、模块重启和重新枚举期间的临时 `USBCFG ERROR` 会自动重试；重新连接后会读取实际配置，不会沿用旧“已就绪”状态。

### 语音运行时

- 首次在「设置 → 语音运行时」确认后，App 从固定上游获取指定版本并校验 SHA-256，缓存到本机；后续模块重启或重插可复用缓存。
- 下载包含 Raw → GitHub Contents API → Raw 重试链路，并使用独立等待窗口，避免上游短暂失败或通用接口超时造成初始化中断。
- 模块侧语音运行时不包含在源码、DMG、ZIP 或 Release 中。

### iPhone / iPad 模式与发布包

- 「设置 → 连接模式」可切换 iPhone / iPad 模式：仅关闭 USB Audio，保留 USB 4G、AT 与短信，避免移动设备占用系统音频输出；接回运行 DJOneHub 的 Mac 后会恢复完整音频接口。
- 修复安装包误带入旧通知 App、设置页遗留固定版本号及连接模式入口缺失的问题。
- v1.2.9 同步提供 macOS Universal（Apple Silicon + Intel）和 Windows x64（含 `DJOneHub.exe`）安装包；Windows 仍未完成真实模块验证。

| 功能 | 说明 |
| --- | --- |
| 电话 | 拨号、接听、拒接、挂断、DTMF、通话记录和录音入口。 |
| 短信 | 收发短信、验证码预览；读取后可自动清理模块存储。 |
| 通讯录 | 可同步本机通讯录，用姓名或号码拨号、发短信。 |
| 网络与 GPS | USB 4G、Wi-Fi 优先、4G 兜底、GPS/GNSS 状态与菜单栏提示。 |
| iPhone / iPad 模式 | 关闭 USB Audio、保留上网和短信；下次接回 Mac 自动恢复完整模式。 |
| 模块工具 | eUICC Profile、AT 调试、网络诊断和初始化状态。 |

## 版本演进

DJOneHub 从本机网页工具逐步演进为独立 macOS App。早期能力没有从仓库历史中删除，相关标签、安装包和完整说明仍可访问。

| 版本 | 主要变化 | 历史入口 |
| --- | --- | --- |
| 初始预览 | 模块状态、短信、eSIM、USB 4G、AT 调试和本机网页管理。 | [最初提交](https://github.com/rogerbush007-a11y/DJOneHub-mac-enhanced/commit/1b8a33ff2ae115b4bb14919e695274cbed6e1f3f) |
| v0.1.1-preview | 增加一键 DMG 安装包，保留菜单栏实时网速。 | [Release](https://github.com/rogerbush007-a11y/DJOneHub-mac-enhanced/releases/tag/v0.1.1-preview) |
| v0.1.2-preview | 移除菜单栏网速显示，保留 GPS 与 4G 状态。 | [Release](https://github.com/rogerbush007-a11y/DJOneHub-mac-enhanced/releases/tag/v0.1.2-preview) |
| v0.1.3-preview | 提供 Apple Silicon 与 Intel 通用安装包。 | [Release](https://github.com/rogerbush007-a11y/DJOneHub-mac-enhanced/releases/tag/v0.1.3-preview) |
| v0.1.4-preview | 增加 Windows x86-64 实验版。 | [Release](https://github.com/rogerbush007-a11y/DJOneHub-mac-enhanced/releases/tag/v0.1.4-preview) |
| v0.1.5-preview | 模块重连后自动续租 USB 4G DHCP。 | [Release](https://github.com/rogerbush007-a11y/DJOneHub-mac-enhanced/releases/tag/v0.1.5-preview) |
| v0.1.6-preview | 增加信号自检、自动找回和 USB 打开超时保护。 | [Release](https://github.com/rogerbush007-a11y/DJOneHub-mac-enhanced/releases/tag/v0.1.6-preview) |
| v0.1.7-preview | 在新 Mac 上自动创建、启用模块网卡并续租 DHCP。 | [Release](https://github.com/rogerbush007-a11y/DJOneHub-mac-enhanced/releases/tag/v0.1.7-preview) |
| v1.2.4 | 重构为独立 App，整合拨号、通话、短信、通讯录、设置和系统提醒。 | [Release](https://github.com/rogerbush007-a11y/DJOneHub-mac-enhanced/releases/tag/v1.2.4) · [发布说明](docs/RELEASE_NOTES_v1.2.4.md) |
| v1.2.5 — v1.2.8 | 增加语音运行时确认下载、移动设备模式，并持续修复首次启用与下载恢复。 | [Releases](https://github.com/rogerbush007-a11y/DJOneHub-mac-enhanced/releases) |
| v1.2.9 | 修复 USB 配置识别、安装包混入旧通知 App 和连接模式入口问题。 | [Release](https://github.com/rogerbush007-a11y/DJOneHub-mac-enhanced/releases/tag/v1.2.9) |

v0.1.7-preview 时期的 487 行完整主页已原样保存在 [`docs/history/README-v0.1.7-preview.md`](docs/history/README-v0.1.7-preview.md)，可用于核对早期安装方式、界面和设计边界。

## 接入原理与架构演进

大疆第一代 4G 模块会通过不同 USB 组合向主机暴露管理串口、USB 网卡和音频接口。DJOneHub 围绕模块已有接口工作，不刷写或替换模块固件。

早期 v0.1.x 主要通过本机网页管理模块：短信模式负责状态、短信、eSIM 和 AT，上网模式负责 USB 4G。切换模式时模块重新枚举，网页会短暂离线。

从 v1.2.4 起，核心能力逐步收拢到独立 macOS App：

1. Go 后台负责 USB/AT、短信、网络、GPS、eSIM 和通话状态。
2. 原生 macOS App 负责电话、短信、通讯录、设置和系统通知。
3. Mac 双向通话使用模块 USB Audio，并按用户确认加载经过 SHA-256 校验的模块侧语音运行时。
4. v1.2.6 增加 iPhone / iPad USB 组合；模块接回 Mac 后恢复完整音频接口。
5. 每次高风险 USB 配置调整前保存实际配置，验证失败时恢复，避免把短暂重枚举误判为永久故障。

本机 HTTP 服务只监听 `127.0.0.1:7575`。SIM、短信、联系人、录音和卡片资料不应离开用户设备。

## 界面预览

> 以下均为真实界面截图；号码、联系人、头像、验证码和时间已遮蔽。

### 电话

<p align="center">
  <img src="docs/images/v1.2.4/dial-pad-empty.png" alt="拨号界面" width="31%" />
  <img src="docs/images/v1.2.4/call-dialing.png" alt="正在拨号" width="31%" />
  <img src="docs/images/v1.2.4/call-active.png" alt="通话中" width="31%" />
</p>

拨号、接听、拒接、挂断、DTMF、通话记录与录音入口统一在电话页。

<p align="center">
  <img src="docs/images/v1.2.4/call-history.png" alt="通话记录" width="48%" />
  <img src="docs/images/v1.2.4/incoming-call-notification.png" alt="来电通知" width="38%" />
</p>

### 短信与通讯录

<p align="center">
  <img src="docs/images/v1.2.4/sms-compose.png" alt="短信编辑" width="45%" />
  <img src="docs/images/v1.2.4/contacts.png" alt="通讯录" width="45%" />
</p>

短信支持收发、验证码预览和自动清理；通讯录可同步本机联系人并用于检索。

<p align="center">
  <img src="docs/images/v1.2.4/sms-notification.png" alt="短信通知" width="44%" />
</p>

### 设置与版本

<p align="center">
  <img src="docs/images/v1.2.4/about.png" alt="关于页" width="42%" />
</p>

## 下载与平台状态

| 平台 | 包 | 当前状态 |
| --- | --- | --- |
| macOS 13+ | `DJOneHub-macOS