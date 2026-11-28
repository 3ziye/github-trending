# ApkStart

<p align="center"><img src="docs/images/logo.png" alt="ApkStart Logo" width="160" /></p>

[![CI](https://github.com/RoutineMiku/apkstart/actions/workflows/ci.yml/badge.svg)](https://github.com/RoutineMiku/apkstart/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/RoutineMiku/apkstart?include_prereleases&sort=semver)](https://github.com/RoutineMiku/apkstart/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%2010%2F11%20x64-0078D6.svg)](#)

**Windows 上的安卓应用运行器 —— 让安卓应用像 Windows 原生软件一样被安装和使用。**

> **English UI / 英文界面**：Settings → **Interface Language** → **English**. The UI switches immediately; the built-in manual is still Chinese-only for now.

注：本项目为早期版本，作者自娱自乐产物，所有修改都是作者下班和休息日在处理，开源免费，不插广告，暂时也不是很好用，没有找过营销号推广，无妄之灾。

- 🖱️ **双击 .apk 即安装**：注册 .apk 文件关联后，在资源管理器里双击 APK，自动解析 → 安装 → 生成桌面图标，全程无需打开任何模拟器界面。
- 🧩 **每个应用一个桌面图标**：图标从 APK 内部离线提取并转为多尺寸 ICO，双击桌面图标 = 直接启动该应用，与打开一个原生 Windows 软件的体验一致。
- 🪟 **应用就是一个窗口**：运行时以**带窗口**模式启动（无头模式下 Android 不出 VSYNC，应用进程活着但屏幕上是空的），ApkStart 把这块窗口改标题、换真实应用图标、按竖屏比例摆好位置，就是一个独立应用窗口；**全屏**铺满屏幕高度并居中，**窗口模式**可自由拖动缩放且按应用记忆尺寸。
- 🔍 **能被 Windows 搜到**：安装后同时创建桌面 + 开始菜单（`程序\ApkStart\`）快捷方式，按应用名在开始菜单搜索即可直达，任务栏按应用分组。
- 📁 **数据互通**：`%USERPROFILE%\ApkStartShared` ↔ 安卓内 `/sdcard/ApkStartShared` 持续双向同步，安卓应用存下的文件直接出现在本机。
- 🪶 **极致轻量**：壳层本身零第三方依赖（连 ZIP / PNG / ICO / AXML 解析都是手写的），运行时按需拉起，空闲自动回收；也可以完全复用你机器上已有的安卓运行时，额外占用为零。

![主界面](docs/images/app.png)

```
┌────────────────────────────────────────────────────────────┐
│  桌面图标（真实应用图标 .lnk）                              │
│      │  双击                                               │
│      ▼                                                     │
│  ApkStart.exe --launch <包名>                              │
│      │  运行时未启动？→ 自动拉起（Android Emulator + API34）│
│      ▼                                                     │
│  按系统解析出的 LAUNCHER 入口启动（不是 APK 里的主 Activity）│
│      │  存活观察 18 秒，闪退自动重试 / 重置数据 / 补权限     │
│      ▼                                                     │
│  模拟器窗口 = 应用窗口（改标题、换图标、竖屏比例、全屏居中） │
└────────────────────────────────────────────────────────────┘
```

## 下载即用（不想编译）

两个源内容一致，国内建议用 Gitee：

- GitHub：[github.com/RoutineMiku/apkstart/releases](https://github.com/RoutineMiku/apkstart/releases)
- Gitee：[gitee.com/daily-miku/apkstart/releases](https://gitee.com/daily-miku/apkstart/releases)（国内直连快得多）

安装包（三种形态，内容与版本号完全一致）：

| 形态 | 文件名 | 何时选它 |
|---|---|---|
| 商店版 | `ApkStart_<四段版本>_x64.msix` | 从 Microsoft Store 装。内置完整运行时，装完不联网；自更新交给商店 |
| 完整便携版 | `ApkStart-v*-win64-full.zip`（约 830 MB，解压 ~1.3 GB） | **不想装、也不想等下载**：解压即用，运行时（模拟器 + 系统镜像）全在包里 |
| 安装版 | `ApkStart-v*-Setup.exe`（约 1.3 GB） | 想要桌面/开始菜单快捷方式、卸载项 |
| 轻量便携版 | `ApkStart-v*-win64-portable.zip`（96 MiB，解压 ~227 MB） | 只想先试试，首次启动再联网下载运行时 |

> 所有形态的 `ApkStart.exe` 都写入了**品牌图标 + 版本资源**（FileDescription = `ApkStart 安卓应用运行器`，
> CompanyName = `RoutineMiku`，版本与 `package.json` 同步），不再是 Electron 的默认图标和 `33.x` 版本号。
> 自己从源码打包时：`npm run pack`（轻量）/ `npm run pack:full`（完整）/ `npm run build:msix`（商店包）。

### 画面铺满是怎么做到的

模拟器的**物理面板方向**（`hw.lcd.width/height`）就是画面的真实形状。面板方向和应用自己声明的
`screenOrientation` 不一致时，Android 只会给应用一个信箱式的中间窄条 —— 两侧补黑，换窗口大小、
改 `wm size`、改 letterbox 样式都填不满（这套组合逐项试过，见 `src/core/apk.js` 的注释）。

所以 ApkStart 在**安装 APK 时离线解析 `AndroidManifest.xml`**，统计出这个应用天然是横屏还是竖屏
（启动 Activity 加权；全 `sensor` / `fullSensor` 的会在首次运行后再问安卓要一次实际值），存进
`apps.json`，启动时按它选面板：

- 红果短剧这类竖屏应用 → 竖屏面板 720×1280，正立、铺满、density 190（sw606dp）同时给出平板排版；
- 墨读这类横屏应用 → 横屏面板 1280×720，正立、铺满。

只有「面板方向和应用方向不一致」的那一次才重启运行时（约 40 秒，标题栏会给出提示），
之后同方向的应用都是秒进。标题栏的旋转按钮会把这个应用的方向**记住**（其它应用不受影响），
设置 → 应用窗口 → 屏幕方向可以改成「强制横屏 / 强制竖屏」。

排版由「逻辑密度」决定：720 宽按 190dpi 算等于 **606dp**，正好越过 Android 的 600dp 平板断点，
红果短剧的双列剧集页、设置页分栏都只在这个密度下出现（镜像默认 320dpi 只有 360dp，是手机排版）。
这就是设置里的「平板排版」开关，默认打开；关掉会回到手机排版。

### 在线更新（自动选较快的源）

设置 → **软件更新** → 「检查更新」，或托盘右键 → 「检查更新」。发现新版本后点「立即更新」即可。

- 安装版下载 `ApkStart-v*-Setup.exe` 静默安装；
- 轻量版下载 `ApkStart-v*-win64-portable.zip`，解压后覆盖**程序目录**——运行时目录（`%APPDATA%\apkstart\runtime`）、已装应用与快照都不在程序目录里，所以更新不会丢东西；
- 替换动作由一段独立 PowerShell 脚本完成（等主进程退出 → 覆盖 → 重新拉起），**不会出现「请手动关闭程序」的弹窗**，也不会在桌面上残留模拟器窗口。

更新链路不是死连 GitHub，而是**每次现测现选**：

1. 同时问 GitHub 与 Gitee 的最新版本，取版本号更高的那个（一个源超时/被墙不影响另一个）；
2. 把「源站直连 / Gitee 同名资产 / 镜像前缀」列成候选，每个地址真下 256KB 测速，
   只算「收到首字节之后」的吞吐（握手时间不计入，否则高延迟大带宽的源会被误判成慢）；
3. 按实测速度排序，用最快的那条分块并行下载；失败自动换下一条。

设置里的「下载与更新源」可以强制只用某一边（企业网络只放行一个域名时用），
也可以关掉公共加速镜像、或改用自建镜像前缀。Gitee 附件单文件上限 100MB，
便携包换用 7-Zip 的 deflate（`-mx=9`）压缩后是 **95.0MB**，所以 Gitee 上也是
一个能直接双击解压的整包（以前要切成 `.part1/.part2` 手工拼接，那版已经废弃）。
两个源的同名包体积并不完全一样，客户端按测速结果只挑一个源下完，不会混拼。

两个仓库都是公开的，Gitee 的发行版列表匿名就能读，不需要填任何 token。
（只有在 Gitee 限流返回 403/429 时，才需要在设置里填一个只读 token 提高额度。）


**开箱即有的默认行为**（不用去设置里找）：

- 开机自动启动，常驻托盘；双击桌面图标直接进应用。
- 安装 APK 后自动创建**桌面 + 开始菜单**两份快捷方式，Windows 搜索能直接搜到应用名；老版本漏建的会在启动时自动补齐。
- 应用窗口是原生渲染（非投屏）：**全屏**铺满屏幕高度并居中、保持手机比例不变形；**窗口模式**保持竖屏，可自由拖动缩放，每个应用的尺寸单独记忆。随时按 `F11` 或右键托盘切换。
- 安装后自动授予应用申请的运行时权限，不会卡在系统授权框；应用闪退会自动重试、必要时重置应用数据后再拉起。
- **网络直接用主机的网络**：安卓侧走 QEMU 用户态 NAT，出口复用主机的物理网卡