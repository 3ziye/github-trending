<div align="center">

<img src="docs/brand/icon.png" width="96" alt="Aerial 图标">

# Aerial

**给国产电视的一块干净桌面。**

参照 Apple TV 做的 Android TV 桌面：没有广告，没有推荐流，只有你的 App、壁纸和航拍屏保。<br>
适合小米、TCL、创维、索尼等国产电视，也能装在盒子和投影仪上。开机自动进入，待机也不会被清理。

**中文** · [English](README.en.md)

<a href="https://aerial.qust.me"><img alt="官网" src="https://img.shields.io/badge/%E5%AE%98%E7%BD%91-1f6feb?style=for-the-badge&logo=safari&logoColor=white"></a>
<a href="https://github.com/pengchujin/aerial-tv/releases/latest"><img alt="下载 APK" src="https://img.shields.io/badge/%E4%B8%8B%E8%BD%BD%20APK-34a853?style=for-the-badge&logo=android&logoColor=white"></a>
<a href="#安装"><img alt="安装" src="https://img.shields.io/badge/%E5%AE%89%E8%A3%85-d97757?style=for-the-badge&logo=gnubash&logoColor=white"></a>

<a href="https://github.com/pengchujin/aerial-tv/releases/latest"><img alt="版本" src="https://img.shields.io/github/v/release/pengchujin/aerial-tv?style=flat-square&label=%E7%89%88%E6%9C%AC&color=2997ff"></a>
<a href="LICENSE"><img alt="许可证 MIT" src="https://img.shields.io/badge/%E8%AE%B8%E5%8F%AF%E8%AF%81-MIT-555555?style=flat-square"></a>
<img alt="Android TV 5.0+" src="https://img.shields.io/badge/Android%20TV-5.0%2B-3ddc84?style=flat-square&logo=android&logoColor=white">
<a href="#lite"><img alt="Lite 4.0–4.4 测试版" src="https://img.shields.io/badge/Lite-4.0%E2%80%934.4%20%E6%B5%8B%E8%AF%95%E7%89%88-f5a623?style=flat-square&logo=android&logoColor=white"></a>

![Aerial 首页](site/img/home.jpg)

| 电视自带的桌面 | 换上 Aerial 之后 |
|:---:|:---:|
| <img src="site/img/stock-xiaomi.jpg" alt="电视自带的桌面：满屏剧集推荐、会员和限免角标"> | <img src="site/img/home.jpg" alt="Aerial 首页"> |

</div>

## 功能

<p align="center">
  <img src="site/img/focus.jpg" width="49%" alt="第一排的玻璃底板">
  <img src="site/img/grid.jpg" width="49%" alt="往下滚动后的应用网格，中间有一个文件夹">
</p>

- **首页**：常用的一排 App 放在屏幕下方的玻璃底板上，往下是全部 App。小米「应用中心」「米家」这类藏起来的系统 App 也在。
- **整理**：长按 OK 键（或按菜单键）可以移动、放进文件夹、隐藏、卸载，或者设成「开机时打开」（开机、待机醒来直接进这个 App 或信号源）。固定到主屏幕的 HDMI 可以选接的是 Apple TV、PlayStation、Switch、Xbox、电脑等，换成对应的图标，也能在手机上起名字。
- **用手机整理**：扫电视上的二维码，手机上就是和电视一样的图标网格：按住拖动排序，点一下改名、换图标、放进文件夹或隐藏，也能把 HDMI 等信号源加到主屏幕。
- **控制中心**：在第一排按上键到右上角打开，有信号源、网络、设置、音量、亮度和个性化。
- **屏保**：Apple TV 的 114 段航拍影片，电视支持时播 4K 或 4K 杜比视界，也可以换成照片、时钟或从手机添加的本地视频（[说明](docs/SCREENSAVER_VIDEOS.md)）。
- **壁纸**：必应每日精选、14 张内置壁纸、用手机扫码传的照片和视频，或者航拍：停在主屏幕 10 秒后在磁贴后面播放，按任意键停在当前画面。
- **个性化**：每排 4、5 或 6 个 App，单排或双排、时钟大小和位置、App 名称、焦点样式、按键声音，都能改。

<p align="center">
  <img src="site/img/folder.jpg" width="49%" alt="打开的文件夹">
  <img src="site/img/control-center.jpg" width="49%" alt="控制中心">
</p>

<p align="center">
  <img src="site/img/screensaver-aerial.jpg" width="49%" alt="航拍屏保">
  <img src="site/img/columns.jpg" width="49%" alt="个性化：每排 App 选 6 个">
</p>

## 安装

不用 root，不动系统应用，随时能还原。电脑和电视连同一个网络。

### 1. 打开电视的 ADB 调试

| 电视 | 怎么打开 |
|---|---|
| **小米 / Redmi** | 设置 → 关于 → 连续按「产品型号/产品类型」进入开发者模式，再到 设置 → 账号与安全，打开「ADB 调试」和「安装未知来源的应用」 |
| **TCL / 雷鸟** | 设置 → 关于 → 本机信息，快速按遥控器「上下左右」，在底部的「更多」里打开 ADB |
| **海尔 / 模卡** | 按电视机身上的信号源键，再用遥控器按「左左上右」，在工厂菜单里打开「ADB 调试开关」，别动其他选项 |
| **OPPO（含 S1）** | 设置 → 系统 → 关于本机 → 设备型号，按「上上右右」再按确认；再到 设置 → 系统 → 开发者选项，打开「USB 调试」。IP 在 设置 → 网络 → 已连接的网络 最下面 |
| **其他 Android TV** | 设置 → 设备偏好设置 → 关于 → 连按「内部版本号」7 次，再在开发者选项里打开「USB 调试」 |

电视的 IP 在「设置 → 网络 → 已连接的网络」里。第一次连接时，有 USB 调试开关的电视会问是否允许调试，选「始终允许」；只有无线调试的电视不弹这个窗，见下一段。

**只有无线调试、没有 USB 调试 / 网络调试（ADB 调试）开关的 Android 11+ 电视，第一次要先配对**（例如索尼 BRAVIA 的 Android 14，#747）：这类电视不提供旧的明文端口，不能直接 `adb connect <IP>:5555`。在电视上打开 设置 → 系统 → 开发者选项 → **无线调试** → **使用配对码配对设备**，把配对码屏幕上的 IP:端口和 6 位配对码输入电脑：

```bash
adb pair 192.168.1.20:37115   # 电视配对码屏幕上的端口（示例，以电视显示为准）
# 提示 Enter pairing code 时输入电视上的 6 位配对码
adb connect 192.168.1.20:39201   # 无线调试主页面上的另一组 IP:端口（示例）
```

连上后照常安装。想让以后直接用 `<电视IP>:5555`，连上时再运行一次 `adb tcpip 5555`；配过对的电脑不用再配对。`install.sh` 和[安装说明](site/agent.md)里的 Agent 会引导这一步。部分 TCL 固件（Q10M、Q10L、鹤 6 Ultra 等）没有配对码入口，只能先按下面的分品牌说明用数据线连电脑授权。

更细的分品牌说明（包括打不开 ADB 的机型）见 [docs/devices/adb-by-brand.md](docs/devices/adb-by-brand.md)。

### 2. 安装

**让 Agent 装（推荐）**：把下面这段发给能在电脑上运行命令的 Agent（WorkBuddy、豆包电脑版、千问电脑版、Trae、Claude Code、Codex 等）：

```text
请帮我把开源电视桌面 Aerial 装到我的电视上，并设为开机进入的桌面。
电视 IP：<电视IP>
保持 ADB 常开：要

安装说明在这里：https://aerial.qust.me/agent.md
（打不开时用 https://raw.githubusercontent.com/pengchujin/aerial-tv/main/site/agent.md ）

请先完整读完安装说明再动手，然后在我的电脑上亲自运行命令，不要只把步骤告诉我。需要我在电视上操作时提醒我。
最后按说明里的「验收」，把这几条命令的原始输出原样贴给我：
- adb shell "cmd package resolve-activity --brief -a android.intent.action.MAIN -c android.intent.category.HOME"
- adb shell settings get secure enabled_accessibility_services
- 按主页键后的 adb shell "dumpsys window | grep mCurrentFocus"
```

手机上的豆包、网页版聊天只会把步骤告诉你，不会执行；要用能跑命令的电脑版 / 工作版（豆包电脑版或豆包工作版、WorkBuddy、千问电脑版、Trae、Claude Code、Codex 等）。Agent 说装好了，看它贴出的 `mCurrentFocus` 输出里有没有 `app.orchard.tv`。

**没有电脑**：有用户用手机上的甲壳虫 ADB 助手、超级小爱装成功过，本仓库没有逐一实测。步骤和上面的 Windows 步骤一样，装好后建议再用电脑跑一遍验收。

**一行命令（macOS / Linux）**：

```bash
curl -fsSL https://aerial.qust.me/install.sh | KEEP_ADB=1 TV=192.168.1.20 bash
```

只有无线调试的电视（见第 1 步）先 `export ADB_PAIR=<配对屏 IP:端口> ADB_CODE=<6 位配对码> ADB_CONNEC