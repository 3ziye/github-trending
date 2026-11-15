# 肉呆去广告

关掉国产安卓手机系统里的广告、热搜、资讯推荐和营销推送。

介绍页：**https://rddmwmddr.github.io/android-ad-cleaner/**

如果大家有其他需求可以加VX和电报群：

https://t.me/+A5X3Mxzs-Cg3NjYx

<img width="1080" height="1596" alt="IMG_7235" src="https://github.com/user-attachments/assets/6197911c-7b6d-47eb-a698-107b99865aee" />


## 下载桌面客户端

插上手机，点几下按钮。不需要 Python，也不需要 AI 工具。

> **v0.4.4 · 2026-11-13**：这一版给一加 16 与真我 GT5 Pro 补了机型脚本，修好了长列表页只关最后一段、vivo 锁屏段一直没生效等几处问题；引擎里把各机型脚本里重复的段体与导航收成共用一份，用起来不变。0.4.1 及以前没有应用内更新，要先手动装一次 0.4.2；从 0.4.2 起可以在 App 里检查、下载并安装更新，手机版仍需在系统弹窗里确认；0.2.7 起的客户端左下角会提示新版；请重新下载，已有备份会保留。详见 [更新记录](CHANGELOG.md)，错误日志上报说明见 [这里](docs/12-错误日志上报.md)。官网：https://ahuamiao.com/sites/other/android-ad-removal-intro.html

此前版本已处理 Windows 本地页面超时、荣耀截图越界、通知渠道误操作风险、vivo 快应用与备份问题。各 Issue 的处理范围和待验证项见 [社区问题处理记录](docs/09-社区问题处理.md)。0.4.2 起 Mac / Windows 客户端也能连纯血鸿蒙手机，这条通道还没有在鸿蒙真机上复测，见 [鸿蒙接入说明](harmony/README.md)。

| 设备 | 下载 | 说明 |
|---|---|---|
| Mac · Apple 芯片（M1 及以后） | [AndroidAdCleaner-0.4.4-mac-arm64.dmg](https://github.com/rddmwmddr/android-ad-cleaner/releases/download/v0.4.4/AndroidAdCleaner-0.4.4-mac-arm64.dmg) | 已签名、通过苹果公证，双击就能打开 |
| Mac · Intel 芯片（macOS 11 及以上） | [AndroidAdCleaner-0.4.4-mac-intel.dmg](https://github.com/rddmwmddr/android-ad-cleaner/releases/download/v0.4.4/AndroidAdCleaner-0.4.4-mac-intel.dmg) | 同上 |
| Windows 10 / 11 · 安装版 | [AndroidAdCleaner-0.4.4-windows-setup.exe](https://github.com/rddmwmddr/android-ad-cleaner/releases/download/v0.4.4/AndroidAdCleaner-0.4.4-windows-setup.exe) | 弹「Windows 已保护你的电脑」时点「更多信息」→「仍要运行」；和旧版共用安装标识，会原地升级 |
| Windows 10 / 11 · 免安装 | [AndroidAdCleaner-0.4.4-windows-portable.zip](https://github.com/rddmwmddr/android-ad-cleaner/releases/download/v0.4.4/AndroidAdCleaner-0.4.4-windows-portable.zip) | 解压后双击 `AndroidAdCleaner.exe`；不会替换、也不会卸载已安装的旧版 |
| 安卓手机 · 手机版（安卓 11 及以上） | [AndroidAdCleaner-0.4.4-android-arm64.apk](https://github.com/rddmwmddr/android-ad-cleaner/releases/download/v0.4.4/AndroidAdCleaner-0.4.4-android-arm64.apk) | 不用连电脑，安装和授权见[手机版教程](docs/手机版教程/README.md) |

不知道 Mac 是哪种芯片：左上角苹果图标 → 关于本机，「芯片」写 Apple M 开头的选 Apple 芯片。所有版本：[Releases](https://github.com/rddmwmddr/android-ad-cleaner/releases)；国内下载走 [Gitee](https://gitee.com/rddmw/android-ad-cleaner/releases)，不用登录（Windows 安装版只在 GitHub 上）。国内走 Gitee 时拿到的是 Windows 免安装版，它不会替换已安装的旧版：要顶掉旧版，用安装版覆盖安装，或先在 Windows「设置」的应用列表里卸载旧的「安卓去广告」（0.3.2 及更早版本装的名字）再删掉旧快捷方式；卸载只删程序目录，数据与备份保留；免安装版启动时若发现旧版还在，也会在界面里提示一次。用法：[docs/08-桌面客户端.md](docs/08-桌面客户端.md)。

> 手机版是不用连电脑的安卓 App（见下面[用法五](#五种用法)）：安装包在上面的表里，安装、授权与还原步骤见[手机版教程](docs/手机版教程/README.md)；想自己构建看 [android/](android/README.md)。

| | |
|---|---|
| <img src="images/gui-1-connect.png" alt="连接手机"><br>**1 连接手机**：插线即认出手机，内置开启 USB 调试的图文教程 | <img src="images/gui-3-detect.png" alt="检测"><br>**2 检测**：型号、系统版本、机型脚本、快应用、广告组件 |
| <img src="images/gui-4-choose.png" alt="选择"><br>**3 选择要关的**：营销通知按渠道勾选，服务类默认不勾 | <img src="images/gui-6-run.png" alt="执行"><br>**4 执行**：进度条和实时日志 |
| <img src="images/gui-7-done.png" alt="完成"><br>**5 完成**：每一步的结果，最后提醒关闭开发者模式 | <img src="images/gui-8-feedback.png" alt="反馈"><br>**反馈**：自动附诊断信息，一键提交 GitHub Issue |

---


- 不 root，不解锁，不刷机，系统更新不受影响。
- 只拨系统和 App 自带的开关。挂起广告包这一步要机主点头，一条命令可以还原。
- 搜索、负一屏卡片、应用商店的安装和更新、天气预警、快递提醒，这些功能保留。

<p align="center"><img src="images/store-before.png" width="560" alt="改之前：软件商店首页满屏推荐"></p>
<p align="center">改之前：OPPO 软件商店首页。轮播图、必备、必玩、福利标签，全是推广位。</p>

---

## 处理哪些东西

| 类别 | 例子 | 怎么处理 |
|---|---|---|
| 系统广告 | 个性化广告、广告跟踪（OAID）、智能推荐服务 | 系统设置里的开关 |
| 热搜和资讯 | 下拉搜索的热榜、负一屏资讯、浏览器信息流 | 各 App 设置里的开关，浏览器切到简洁首页 |
| 推广位 | 商店的轮播、开屏、悬浮活动、签到福利 | 商店「服务管理」里的开关 |
| 营销推送 | 各 App 的「内容与营销」「活动优惠」通知 | 按渠道关，同一个 App 的订单、快递、更新通知保留 |
| 广告组件 | `com.opos.ads`、`com.miui.systemAdSolution` 等 | `pm suspend` 挂起，要机主同意 |
| 快应用 | 广告里一点就跳进去的「免安装小程序」 | `quickapp` 检测，`quickapp off` 关闭，见 [docs/07-快应用.md](docs/07-快应用.md) |

## 不做的事

- 不卸载、不停用系统应用（`pm uninstall`、`pm disable-user` 都不用）。
- 不改 system 分区，不装模块。
- 不替你同意任何 App 的用户协议。遇到协议页，点「取消」或「以后再说」。
- 不截账号页和手机号页。

---

## 五种用法

<p align="center"><img src="images/ways.png" width="460" alt="用法示意"></p>

> 用法一要先在手机上打开开发者模式和 USB 调试，带截图的教程：[docs/00-打开开发者模式.md](docs/00-打开开发者模式.md)。

| 用法 | 适合谁 | 要准备什么 | 文档 |
|---|---|---|---|
| **一：AI 智能体替你跑** | 有电脑，想省事 | 电脑、数据线、一个能执行命令的 AI 工具 | [docs/02-用AI智能体.md](docs/02-用AI智能体.md) |
| **二：聊天 AI 带你点** | 只有手机 | DeepSeek、豆包、ChatGPT 任意一个 | [docs/03-用聊天AI.md](docs/03-用聊天AI.md) |
| **三：照清单手动关** | 想自己掌握每一步 | 只要手机 | [docs/清单/](docs/清单/) |
| **四：桌面客户端** | 不想敲命令 | Mac（Apple / Intel 芯片）或 Windows 10/11、数据线 | [下载](#下载桌面客户端) · [说明](docs/08-桌面客户端.md) |
| **五：手机版 App** | 不想连电脑 | 安卓 11 及以上、Wi-Fi；安装包在[下载表](#下载桌面客户端)里 | [教程](docs/手机版教程/README.md) |


用法一的开场白，复制给 AI：

```text
请克隆 https://github.com/rddmwmddr/android-ad-cleaner ，读仓库里的 AGENTS.md，
然后帮我给连着电脑的这台手机去广告。每一步改之前告诉我要改什么。
```

---

## 实测过的机型

**机型脚本**：一台机型的自动操作步骤，记着「打开哪个 App、点哪几个字进设置页、关哪几个开关、留哪几个」。电脑照着它在手机上点，几分钟做完。设置页因型号和系统版本而不同，所以每个机型一份。

| 品牌 | 机型（型号） | 系统 | 脚本 | 清单 | 营销通知 |
|---|---|---|---|---|---|
| 魅族 | 21 Pro（MEIZU 21 Pro） | Flyme 12.6.0.0A<br>Android 16 | ⚠️ 10-30 | ✅ | ✅ 8 |
| 华为 | ALN-AL00 | HarmonyOS 4.2.0.223<br>Androi