# 任意门 AnyDoor · 全局定位模拟

<p align="center">
  <a href="https://github.com/zhaoyuxiangyyds-lab/AnyDoor/releases/latest"><img src="https://img.shields.io/github/v/release/zhaoyuxiangyyds-lab/AnyDoor?style=flat-square&color=ff4d7d" alt="Release"></a>
  <a href="https://github.com/zhaoyuxiangyyds-lab/AnyDoor/releases"><img src="https://img.shields.io/github/downloads/zhaoyuxiangyyds-lab/AnyDoor/total?style=flat-square&color=ff4d7d" alt="Downloads"></a>
  <img src="https://img.shields.io/badge/Android-8.1%20~%2016-3ddc84?style=flat-square&logo=android&logoColor=white" alt="Android 8.1-16">
  <img src="https://img.shields.io/badge/Xposed-LSPosed%20%7C%20Vector-blue?style=flat-square" alt="Xposed">
  <a href="LICENSE"><img src="https://img.shields.io/github/license/zhaoyuxiangyyds-lab/AnyDoor?style=flat-square" alt="License"></a>
  <a href="https://github.com/zhaoyuxiangyyds-lab/AnyDoor/stargazers"><img src="https://img.shields.io/github/stars/zhaoyuxiangyyds-lab/AnyDoor?style=flat-square&color=ffc83d" alt="Stars"></a>
</p>

<p align="center"><b>简体中文</b> · <a href="README_EN.md">English</a></p>

**1.4.2 修复 Android 14+ 已连接 WiFi 的 BSSID 屏蔽在部分机型失效**：[下载 APK 与升级说明](../../releases/tag/v1.4.2) · [完整更新记录](CHANGELOG.md)。真机诊断里 `conn=impl-missing` 的机型（连接组件被 jarjar 改名）此前仍会泄露当前已连接 WiFi 的 BSSID，被高德/腾讯反查把定位拉回真实附近；现改为直接从初始化器实例取到 `ConnectivityService` 再挂钩，环境检查应显示 `conn=ok`。升级后请完整重启手机。

<sub>更早：1.4.1 修复模拟位置几秒后跳回真实位置、作用域内应用闪退（[v1.4.1](../../releases/tag/v1.4.1)） · [完整更新记录](CHANGELOG.md)。持续取位的应用（高德、微信、得力e+、分身类）此前会短暂显示虚拟位置后又跳回真实位置——已改在 `onReportLocation` 下发总入口统一改写并去掉模拟标记，不再依赖各 ROM 的内部类名。**目标应用无需加入作用域、也不要设为豁免**，只勾「系统框架」「电话」「蓝牙」即可。升级后请完整重启一次手机。 · [完整更新记录](CHANGELOG.md)。`requestCellInfoUpdate`（Android 10+）、`ServiceState` 里的小区标识、Android 12+ 经 `NetworkCapabilities` 下发的已连接 WiFi BSSID 之前都没有被屏蔽，应用自带的网络定位 SDK 仍能拿到真实环境——这是“系统定位已改、个别应用 / 小程序仍是原位置”的主要来源，本版补齐。路线规划现在列出高德的多条备选路线并支持途经点，并修复地图上路线折线几乎不可见的问题。**未在真机复测**；升级后请完整重启一次手机。

1.4 补齐 WiFi/基站屏蔽对新接口的覆盖、路线备选与途经点；1.3.6 新增「系统直推」；1.3.5 修复 ColorOS/OxygenOS 等 ROM 上 `OP_MOCK_LOCATION` 被拒导致测试定位源注册失败；1.3.4 修复真实定位连续使用卡住与 Android 15/16 WiFi 屏蔽失效。见 [更新记录](CHANGELOG.md)。</sub>


> 一个基于 Xposed 的安卓**全局虚拟定位**工具，界面美观、功能齐全，专为**中国网络环境**优化。
> 在系统服务内部改写通过系统定位接口下发的位置，并抹掉「模拟位置」标记；室内没有 GPS 信号也能持续输出坐标。

任意门是为了替代那些「搜不出地点、没有地图、只能填经纬度」的老式虚拟定位工具而写的。它把定位改在 `system_server` 里，面向使用系统定位接口的应用，开关随时切换、无需每次重启。

<p align="center">
  <img src="docs/screenshots/01-map.png" width="30%" alt="地图选点" />
  <img src="docs/screenshots/02-running.png" width="30%" alt="模拟中" />
  <img src="docs/screenshots/03-address.png" width="30%" alt="地址解析" />
</p>

---

## ✨ 功能特性

- **真·全局生效**：在 `system_server` 的 `LocationManagerService` 内改写定位，覆盖所有 App，而不是只 hook 单个应用。
- **反检测**：结果 `isFromMockProvider = false`；可选屏蔽 **WiFi 扫描 / 基站 / 原始 GNSS**，防止定位 SDK（高德、腾讯、百度）用周围环境反推真实位置。
- **持续输出**：同时通过测试定位源（mock provider）持续推送坐标，室内无 GPS 信号也有定位。
- **好用的地图界面**（WebView + Leaflet + 高德瓦片）：
  - 地点搜索（高德，中国可用）、点图选点、粘贴经纬度
  - **方向键微调** & **悬浮摇杆**（可在任意 App 上层实时走动）
  - **路线模拟**：设起点终点，按 **步行 / 跑步 / 骑行 / 驾车** 沿真实道路自动移动（高德路径规划）；可在高德给出的多条**备选路线**里点选，也可加**途经点**让路线改走别的路；速度随机波动、路口随机停顿、到达后原路返回或循环；也可手动画路径点
  - **计步同步**：模拟行走时同步伪造计步传感器（微信运动、Keep 等），可设步幅、直接"刷步数"
  - 收藏夹、历史记录、随机漂移、深浅色主题
- **一键隐私加固**：屏蔽 WiFi / 基站 / GNSS / 蓝牙环境 + 伪造 IMEI / IMSI / ICCID / Android ID / 序列号 + 屏蔽气压计；不依赖是否在模拟位置。说明里明确写了[做不到的部分](#-隐私加固的边界)。
- **坐标系自动纠偏**：内部统一 WGS-84（GPS 原始坐标），显示与高德瓦片按 GCJ-02 纠偏；支持粘贴 WGS84 / 火星 GCJ-02 / 百度 BD-09 坐标。
- **一键环境自检**：检测框架是否激活、作用域是否正确、权限是否到位，并可一键配置。

---

## 📋 环境要求

| 项目 | 要求 |
|------|------|
| 系统 | Android 8.1 ~ 16（SDK 27+）。已在 **华为 EMUI 9 / Android 9** 真机实测通过；较新版本使用 API 31+ 的 `ProviderProperties`；1.3.3 尚未进行各安卓版本真机回归，OEM 与目标应用兼容性需实测 |
| Root | 需要 Root |
| Xposed 框架 | **LSPosed** / **Vector**(JingMatrix) 等任意 Xposed 框架 |
| 架构 | 纯 Java，无 native，各架构通用 |

> ⚠️ 未 Root、无 Xposed 框架的设备无法使用本工具的全局功能。

---

## 🚀 安装与配置

### 1. 安装 APK
从 [Releases](../../releases) 下载 `AnyDoor.apk` 安装，或[自行编译](#-从源码编译)。

### 2. 在 Xposed 框架中启用模块
打开 LSPosed / Vector 管理器 → 模块 → 启用「任意门」，**作用域必须勾选**：

- ✅ **系统框架**（`android` / `system`）— 全局生效的关键
- ✅ **电话和通讯录**（`com.android.phone`）— 屏蔽基站定位、伪造 IMEI 等标识用
- ✅ **蓝牙**（`com.android.bluetooth`）— 隐私加固里屏蔽蓝牙扫描用（可选）
- ✅ **任意门自身**（`io.github.zhaoyuxiangyyds_lab.anydoor`）— 模块自检（目标应用的强化模式需单独勾选）

> 命令行框架（如 Vector CLI）可执行：
> ```sh
> cli scope set io.github.zhaoyuxiangyyds_lab.anydoor android/0 system/0 com.android.phone/0 com.android.bluetooth/0 io.github.zhaoyuxiangyyds_lab.anydoor/0
> ```

### 3. 重启一次手机
系统框架 hook 需要重启才能注入 `system_server`。**首次启用和每次升级都需要完整重启**，之后开关模拟无需再重启。

### 4. 打开 App，进入「环境检查」
确认应用／系统模块版本一致、系统配置已同步，并在目标应用请求定位后观察下发计数。尚未请求定位时，下发计数为 0 不代表失败。若「模拟位置权限」「悬浮窗权限」未授予，点 **一键 Root 配置** 即可。

### 5. 配置高德 Key（中国搜索地点必需）
中国网络下地点搜索走高德 REST API，需要一个**免费**的高德 Key（约 2 分钟，一次配置永久有效）：

1. 打开 [高德开放平台控制台](https://console.amap.com/dev/key/app) 并登录（首次需注册 [lbs.amap.com](https://lbs.amap.com/)）
2. 应用管理 → 创建应用 → 添加 Key
3. **服务平台务必选「Web服务」**（不是 Android / iOS / Web端JS API，否则会报 `INVALID_USER_KEY`）
4. 复制生成的 32 位 Key，填入 App 的 **设置 → 高德 Key**

> 首次搜索时 App 也会弹窗引导你申请。填 Key 之前，点图选点 / 粘坐标 / 摇杆 / 路线都能正常用，只有「按名字搜地点」需要 Key。

---
