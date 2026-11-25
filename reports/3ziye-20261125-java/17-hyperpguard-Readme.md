<div align="center">

# HyperPGuard

![license](https://img.shields.io/badge/license-GPL--3.0-blue)
![language](https://img.shields.io/badge/language-Java-orange)
![release](https://img.shields.io/github/v/release/vivibibi30/hyperpguard?label=release&color=green)
![android](https://img.shields.io/badge/Android-10--16-green)
![status](https://img.shields.io/badge/status-按需维护-2da44e?style=flat-square)

在采集入口、本地存储、对外接口、网络出口四个层面，按应用给行为加开关

</div>

[简体中文](README.md) · [English](README.en.md)

以下内容基于对本机预装组件的静态分析与运行时观察：这些组件会采集设备标识、应用使用记录、位置、通话行为等信息，并通过网络或跨进程接口发出。本模块在这些通道上按应用分组拦截，开关与 LSPosed 作用域联动。具体行为以各自机型和系统版本上的观察为准。

> **维护节奏**：本项目由个人维护，开发与验证主要依赖 AI 辅助与自费的真机测试，长期成本由作者个人承担。更新频率已主动下调：只在出现影响使用的缺陷、发现新的上报通道或系统大版本适配时发版；界面、文案与小功能改动会并入下一次实质更新，不单独出包。issue 会看，但不承诺响应时间和实现排期，未确认的功能请求可能长期不做，或并入相近的改动一起处理。

改代码前建议先看 [AGENTS.md](AGENTS.md)（协作约定）与 [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)（结构与扩展步骤）。

本仓库即源码仓：`src/` 下是全部 Java 实现，`build.sh` 是完整构建脚本，用 `javac` + `d8` + `aapt2` + `zipalign` + `apksigner` 打包，不依赖 Gradle；`Releases` 里的 APK 由它构建。`Xposed-Modules-Repo/io.github.vivibibi30.hyperpguard` 只是 LSPosed 的索引仓库，只放 APK 与简介。

> 仅供个人在自有设备上学习研究使用。使用前请阅读 [DISCLAIMER.txt](DISCLAIMER.txt)。名称中的 Hyper 指 HyperOS 平台，本项目与小米、中国联通等厂商无隶属或合作关系。

## 当前支持的版本

- Android 10 – Android 16（对应平台）
- LSPosed 2.2.x（libxposed API 100+）
- Root：KernelSU / Magisk / APatch（「重启」「查看日志」需要）

## 安装

1. 安装 `HyperPGuard`
2. 在 LSPosed 中启用「HyperPGuard」
3. 打开应用，首次会向 LSPosed 请求全部作用域，允许即可；也可在 LSPosed 里手动勾选
4. 在模块里对目标应用点一次「重启」，或点批量行的「全部重启」，让它重新加载

作用域外的应用不会被注入。

覆盖升级后，LSPosed 的作用域不会自动包含新增组件，需要到 LSPosed → 模块 → HyperPGuard → 作用域 里重新确认；漏勾时对应分组会显示「未在作用域，点此加入」，本机没有安装的组件会显示「本机未安装该组件」。

## 使用

**分组开关**：每张卡片右上角是该应用的开关，等同于它在 LSPosed 里的作用域开关。组关闭时组内子项置灰不可操作。

**子项开关**：可以只留某条规则，例如只要 XSOF 拦截就把域名层那项关掉。会影响系统功能的规则一律默认关闭，副标题写明代价。

**自定义规则**：内置表没覆盖的域名可以自己补，支持「域名」「域名/路径」和「类名#方法」三种写法：前两种作用于网络出口，第三种让指定方法直接返回默认值，用于内置 hook 因类名变化失配时应急。添加后会自动热重载已注入的进程；提示失败时再重启对应应用。写法、匹配方式与限制见 [自定义规则使用说明](docs/CUSTOM-RULES.md)。

**热重载**：改完开关不用重启——模块会自动让已注入的进程换用新配置（走 libxposed API 102 的热重载，在进程内重装 hook，不 `force-stop`）。只改开关时不会碰其它进程：改哪个组件就只重载那个组件。主页的「开关热重载」可以关掉这个行为，回到手动「重启」；框架不支持（API < 102）或提示失败时也走「重启」。

**重启**：点「重启」执行 `am force-stop`，应用下次启动重新注入；批量行有「全部重启」。系统常驻组件被停止后通常几秒内会被系统拉起，等于自动完成重启。热重载失败、或刚改过作用域时用这条。

**查看日志 / 分享日志**（设置页）：读取本地 logcat 中本模块的输出，顶部给出拦截统计（域名次数、hook miss），可导出分享。日志不包含电话号码、行为库内容或调用参数。

**记录未拦截访问**：记录「访问了但没被规则命中」的域名，用于补规则，平时保持关闭。

**数据自查**：主页有「安全中心行为库」写入计数和「MiSight 事件库」只读浏览。后者需要 root，读取系统埋点库的事件、触发场景与上传记录，查完即删快照，不导出。

**设置页**：查看/分享日志、清理日志缓冲、隐藏桌面图标、配置导入导出（导出开关与作用域清单，或从剪贴板导入）；底部是「关于」区（GitHub、LSPosed、Issues、版本与检查更新）。

**关于 / 检查更新**：列出 GitHub 仓库、LSPosed 模块页与 Issues 入口，点「检查更新」会向 GitHub API 取最新 release tag 与当前版本比对；不点就不发任何请求。

## 拦截层次

按数据处理顺序分四层，方法层作为类名失配时的兜底：

| 层 | 做法 |
|---|---|
| 采集入口 | 在数据来源处截断：应用列表、使用记录、设备标识、位置与网络环境查询直接返回空 |
| 本地存储 | 拦截行为记录类数据库的写入，写不进去也就无从打包上传 |
| 对外接口 | 拦截跨进程查询接口与风险评分接口，第三方应用拿不到这些记录 |
| 网络出口 | 拦截目标进程内的域名解析与连接，按「域名后缀 + 可选路径」匹配 |
| 兜底 | 反射定位特定方法后返回默认值；类名随版本变化时，网络层仍然生效 |

四层互不依赖：某层因版本变化失效时其余层照常工作，日志能分辨是哪一层命中。

## 覆盖范围

按能力分类，不逐一列出目标组件与包名；需要精确拦截范围时，请在自己的设备上对照界面里每个开关的描述。

| 类别 | 拦的是什么 |
|---|---|
| 统计与埋点 | 统计类组件的上报事件，方法层与域名层各有一条路径 |
| 设备与位置 | 设备标识、基站与 Wi-Fi 扫描、定位查询按应用单独开关，默认关闭 |
| 行为记录 | 截图、通话、屏幕共享等行为记录的写入，以及对外的查询与评分接口 |
| 诊断与反馈 | 系统诊断与售后远程诊断的日志上传；触发条件是用户主动反馈或售后操作，本地记录不等于已上传 |
| 运营商侧 | 设备管理组件的上报域名与方法层，只拦上报，不回收已授予的权限 |
| 输入法 | 统计上报、剪贴板内容记录、语音数据上传 |
| 广告与商店 | 广告使用画像、开屏广告、配置下发与统计上报 |

每个应用在界面里是一张卡片：右上角是它在 LSPosed 里的作用域开关，卡片内是逐项规则，会影响系统功能的规则默认关闭并在副标题写明代价。

## 日志说明

| 前缀 | 含义 |
|---|---|
| `attach <进程>` | 模块注入某进程成功 |
| `X(host)` | 域名规则命中；带路径规则时是 `X(host+path)`，grep 建议用 `grep -F 'X(host'` |
| `X(host+path)` | 域名 + 路径规则命中 |
| `X(strict)` | 整进程断网生效 |
| `? <tag> <host>` | 「记录未拦截访问」记录：访问未被拦截 |
| `hook ok` / `hook miss` | 方法层安装成功 / 类名或签名不匹配 |
| `xsof provider hooked` | XSOF Provider 三个入口已拦截 |
| `xsof aidl hooked=N` | XSOF AIDL 接口拦截数量 |
| `xsof db write hooked=N` | XSOF 写库方法拦截数量 |
| `xsof score hooked=N` | 风险评分方法拦截数量 |
| `analytics scan scanned=N hooked=N` | analytics 签名扫描结果 |

## 如何确认生效

1. 启用模块，并对目标应用点一次「重启」
2. 触发一次它的上报行为（例如打开安全中心、安装一个应用）
3. 点「查看日志」，应看到 `attach <进程>` 与 `X(...)` 记录
4. XSOF 部分应全是 `hooked`，没有 `miss`
5. 只有 `attach` 没有 `X(...)` 时，打开「记录未拦截访问」跑一段时间，把 `?` 开头的域名补进规则

## 构建

需要 JDK 17 与 build-tools 35 及以上，SDK 路径用环境变量指定：

```sh
export ANDROID_JAR=/path/to/android.jar D8=/path/to/d8 AAPT2=/path/to/aapt2
export ZIPALIGN=/path/to/zipalign APKSIGNER=/path/to/apksigner
sh build.sh
```

## 源码结构

```
src/io/github/vivibibi30/hyperpguard/
├── HookEntry.java      入口与按包分发（XposedModule#onPackageReady）
├── Config.java         开关常量、默认值表、配置通道
├── NetGuard.java       网络出口：URL / InetAddress / Socket + 规则匹配
├── PrivacyApis.java    隐私 API：应用列表 / 使用记录 / 标识 / 短信 / XMSF 广播
├── CaptureHooks.java   行为库写入与静默录屏
├── XsofHooks.java      XSOF Provider / AIDL / 写库 / 评分 + MRM
├── MsaHooks.java       MSA 使用画像、开屏广告
├── AnalyticsHooks.java 统计方法层与签名扫描
├── TrackHooks.java     OneTrack 埋点收口
├── ImHooks.java        输入法埋点与剪贴板
├── Hooks.java          公共 hook 工具
├── Logs.java           统一日志标签
├── HotReload.java      开关热重载（libxposed API 102）