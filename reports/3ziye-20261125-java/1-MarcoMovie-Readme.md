<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/images/brand-horizontal-dark.png" />
    <source media="(prefers-color-scheme: light)" srcset="docs/images/brand-horizontal-light.png" />
    <img src="docs/images/brand-horizontal-light.png" width="520" alt="Marco Movie — 金属胶片丝带 M 标志与品牌字标" />
  </picture>
  <h1>Marco Movie</h1>
  <p>支持 Android 电视、手机、平板，HarmonyOS NEXT（手机 / 平板 / 智慧屏），Apple TV（tvOS）及 Windows / macOS / iOS 多端自适应的播放器。</p>
  <p>作者：<a href="https://github.com/Pilipala9919">Pilipala</a> · Android 手机：0.7.0 · Android 电视：0.6.2 · Android Lite：0.5.9 · Windows：0.7.1 · macOS：0.5.20 · iOS：0.7.0 · Apple TV：0.1.1 · HarmonyOS NEXT：0.1.2 · 各端独立更新</p>
  <p><a href="https://marcotv.wlj9919.top/movie/">镜像下载与产品展示</a> · <a href="https://github.com/Pilipala9919/MarcoMovie/releases">GitHub 下载</a> · <a href="docs/USER_GUIDE.md">使用指南</a> · <a href="docs/BUILD.md">构建说明</a> · <a href="docs/PRIVACY.md">隐私说明</a></p>
</div>

> **本产品仅为播放与内容管理工具，不内置、不提供、不托管、不售卖任何影视资源，也不提供影视资源配置地址、账号或会员权益。内容及配置需由用户自行合法获取，并确保拥有相应访问和使用权。**

## 产品介绍

Marco Movie 希望让大屏电视、随身手机、平板电脑与桌面端上的浏览、搜索和播放同样自然顺手：在大屏电视上（Android TV、Apple TV `tvOS` 及 HarmonyOS NEXT 鸿蒙智慧屏）以大幅竖版海报与清晰焦点反馈配合遥控器操作；在手机与平板上（Android、iOS / iPadOS 及 HarmonyOS NEXT 手机/平板）采用完全独立的触控界面（竖屏底部 Dock、横屏侧边 Dock、原生键盘搜索、剪贴板一键导入、全屏手势播放）；并提供 `tvos/` 原生 Apple TV 客户端、`flutter/ohos/` 原生鸿蒙 Stage 宿主及 `flutter/` 跨平台工程覆盖 Windows、macOS、iPhone 与 iPad。应用没有预装片库；第一次打开时，用户需要自行导入有权使用的配置。

这是一个覆盖 Android、Apple TV（tvOS）、HarmonyOS NEXT（纯血鸿蒙）、iOS / iPadOS、Windows 与 macOS 的多平台客户端项目。界面、配置管理、播放控制和本地搜索匹配在设备上运行；本项目不运营影视内容服务。功能和设备兼容性仍在持续完善。

## 能做什么

| 功能 | 当前能力 |
| --- | --- |
| 电视端导航 | Android TV、Apple TV（Siri Remote 焦点引擎）与鸿蒙智慧屏均配备 10 英尺大屏交互：首页悬浮图标/顶部 Dock、遥控方向键连续焦点移动、分类筛选与按返回键回到原浏览位置 |
| 手机 / 平板专属 UI | 自动识别触屏手机与平板（Android、iOS / iPadOS、HarmonyOS NEXT 手机/平板），进入独立移动端界面：保留系统状态栏、去除遥控器白色焦点框；竖屏底部导航栏、横屏切换侧边导航栏 |
| 大屏与移动端首页 | 电视端提供继续观看横卡、完整分类名称与默认 5–8 列海报墙；手机端提供顶部片源胶囊切换、单行横向滑动分类条、紧凑继续观看条与 3 列触控海报网格（平板横屏 5 列） |
| 内容详情与选集 | 电视端左对齐沉浸影院或分栏滚动；手机端采用左海报右信息紧凑卡片、可折叠简介、横向滑动线路胶囊、每 50 集自动分组标签、正序/倒序切换与触控选集网格；全端（含 Lite 纯文字标签）接入统一纯文字媒体规格徽章（`4K` / `HDR10+` / `DV · ATMOS` 等，零第三方商标图形） |
| 我的收藏与历史 | 详情页一键收藏；整合观看历史与我的收藏，支持单条删除与一键清空；数据保存于本机 |
| 全局搜索 | 在已导入、可搜索的配置项之间并发检索；Android 电视端内置遥控拼音键盘（支持中文、全拼、首拼），Apple TV 支持系统搜索与听写；手机/平板端直接调起系统输入法软键盘 |
| 播放控制与触屏手势 | 电视端（Android TV / Apple TV / 鸿蒙智慧屏）确认键暂停/继续、遥控长按加速快进预览、3 秒片头/片尾跳过倒计时与定时关闭；手机/平板端支持**双击自定义（播放暂停/左右步进）、左右滑快进快退、左半屏亮度、右半屏音量、长按 2.0× 倍速并横滑切换 `1.25×–3.0×` 与上滑锁定**；iOS/iPadOS 26 采用同心液态玻璃空间影院 HUD 与原生半屏面板；桌面端支持 2.5s 鼠标自动隐藏、滚轮调音量、`←`/`→` 加速预览（`Esc` 取消）、`S`/`[`/`]` 倍速与 `D` 弹幕开关 |
| 播放内核 | Android 采用 Media3 + FFmpeg / AV1 / VP9 软解扩展与可选 MPV（[范围与限制](docs/DECODERS.md)）；Apple TV 采用原生 `AVPlayer`（支持 HLS / 4K HDR10 / 杜比视界）；HarmonyOS NEXT 采用原生 ArkTS `AVPlayer` + `XComponent` GPU 硬件纹理；iOS / iPadOS 采用原生 `AVPlayer`（画中画 / AirPlay 2）+ `libmpv` 双引擎自动回退；Windows / macOS 采用 `media_kit`（`libmpv`，Windows 支持三档 HDR 动态色调映射、人声增强与蓝光 `.iso` 流式代理）及可选热切换 `Anime4K v4.0.1` 实时超分 |
| 字幕与弹幕 | 外挂 SRT / VTT / ASS / TTML 字幕及流内音轨/字幕轨切换（字幕严格渲染在弹幕上方）；内置清洁室 30 秒分片弹幕引擎（默认服务地址为空，无碰撞轨道与 ReDoS 防护），仅在用户自行配置兼容服务或导入本地 XML/JSON 弹幕文件后生效，不提供在线弹幕资源 |
| 直播列表 | 读取用户提供的兼容 M3U / TXT 列表与分组；电视端支持遥控快速换台；手机与桌面端提供分组与频道列表点选即播 |
| 配置导入管理 | 电视端（Android TV / Apple TV / 鸿蒙智慧屏）提供同一局域网手机扫码推送、手动输入与备份导入；**手机/平板/桌面端直接提供原生输入框、剪贴板一键粘贴导入与本地 JSON 文件选择**；新增 5 幕独立新手引导（配程序化抽象几何「示例」海报，不内置真实影片或内容源），全端支持配置备份与还原 |
| 跨平台客户端 | 涵盖原生 Android（手机/平板/电视/Lite）、`tvos/` 原生 Apple TV（`tvOS 16.0+` `.ipa`）、`flutter/ohos/` HarmonyOS NEXT 通用包（`API 12+` 手机 / 平板 / 2in1 / 智慧屏单包自适应 `.hap`）及 `flutter/` Windows（x64 `.exe`）、macOS（`.app`）、iOS / iPadOS（`.ipa`），互通 `marco-movie-backup` 备份文件 |
| 多端网络同步 | 全平台（Android 电视 / 手机平板 / Lite、Apple TV、HarmonyOS NEXT、iOS / iPadOS、Windows、macOS）互通 `marco-movie-sync` v2 协议：支持用户自配 WebDAV（坚果云 / NAS / Alist / Nextcloud 等）自动云同步与同一局域网点对点双向免云盘直连同步，合并观看历史进度、我的收藏及可选的公开订阅源配置；严格隔离隐私空间与网盘 / Emby 登录凭据 |
| 软件更新 | 设置内检查更新；镜像优先、GitHub 备用，下载后核对 SHA-256 校验值 |
| 个性化与网盘代理 | 海报配色柔光、极光氛围背景（空态/关于/引导页，按系统减少动态效果自动停帧）、分级转场动效与金属丝带 `M` 品牌加载器、自定义壁纸、界面缩放；全端支持用户本人在夸克 / UC / 百度 / 阿里云盘扫码授权及本机 `127.0.0.1` 6 路并发分片回环代理播放 4K 原画，不内置账号 |

全局搜索的范围是**用户已导入的配置**，不是互联网全网搜索。拼音匹配结合本地字词典和已浏览/搜索过的标题，首拼存在歧义时可改用完整中文。功能存在不代表任意配置或服务都兼容。

## 安装与开始使用

1. 在 [镜像下载页](https://marcotv.wlj9919.top/movie/) 或 [Releases](https://github.com/Pilipala9919/MarcoMovie/releases) 下载对应系统的安装包，并核对随附的 SHA-256 文件。
2. 根据设备选择独立安装包：
   - **Android 设备**：电视/盒子用 `-android-tv.apk`（ARM 32 位），手机/平板用 `-android-mobile.apk`（ARM 32/64 位）；旧 Android 4.0+ 设备选择独立 `-android-lite.apk`。
   - **Apple TV（tvOS 16.0+）**：下载 `-tvos-appletv-unsigned.ipa` 未签名包，通过 Xcode、Sideloadly、自签工具或巨魔（TrollStore tvOS）安装。
   - **HarmonyOS NEXT（API 12+ 手机 / 平板 / 2in1 / 智慧屏）**：下载 `-harmonyos-universal.hap` 通用未签名包，使用 DevEco Studio 自动签名或 `hap-sign-tool` 签名后通过 `hdc install` 安装。
   - **Windows / macOS / iOS**：下载对应 `-windows-x64-setup.exe` / `-windows-x64-portable.zip`、`-macos-desktop.zip` 或 `-ios-iphone-ipad-unsigned.ipa`。最低系统声明不代表已通过每台设备的实测；每次修复与验证范围见[版本记录](CHANGELOG.md)。
3. 打开应用导入配置：
   - **手机 / 平板 / 桌面端**：直接在首页欢迎卡片输入网址，或复制配置链接/JSON 后一键读取剪贴板导入，也可选择本地 JSON 