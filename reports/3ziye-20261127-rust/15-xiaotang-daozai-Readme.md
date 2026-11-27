<div align="center">

<img src="assets/daozai-logo.png" width="112" alt="岛仔" />

# 岛仔 · Daozai

**一座小岛，装下桌面日常。**

Windows 桌面信息岛，抬眼就能看消息、歌词、日程、天气、系统性能、蓝牙电量和 AI 额度。

[![最新版本](https://img.shields.io/github/v/release/Renly1994/xiaotang-daozai?color=7955b8&label=最新版本)](https://github.com/Renly1994/xiaotang-daozai/releases/latest)
[![Windows](https://img.shields.io/badge/Windows-10%20%2F%2011-0078D4)](#下载安装)
[![开源许可](https://img.shields.io/badge/License-MIT-3cbf91)](LICENSE)
[![Rust 与 egui](https://img.shields.io/badge/Rust-egui-8b6ca8)](#从源码构建与参与开发)

**[下载 Windows 版](https://github.com/Renly1994/xiaotang-daozai/releases/latest)** · [使用指南](docs/USAGE.md) · [更新记录](CHANGELOG.md) · [反馈问题](https://github.com/Renly1994/xiaotang-daozai/issues)

</div>

岛仔是一款开源的 Windows 桌面小工具。平时收起在屏幕边缘，鼠标靠近就展开；切歌、看日程、复制验证码、记一条待办，都能顺手完成。小岛里的伙伴会眨眼、打盹、喝水，也会跟着音乐唱歌。

你可以选刘海或胶囊，放在屏幕顶部、底部、左侧或右侧，只保留自己需要的功能。岛仔使用 Rust 和 egui 构建，不依赖 Electron。

## 星标增长曲线

横轴是日期，纵轴是 GitHub 累计星标数。点击图表可以打开 Star History 查看。

<a href="https://www.star-history.com/?repos=Renly1994%2Fxiaotang-daozai&amp;type=date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Renly1994/xiaotang-daozai&amp;type=date&amp;theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Renly1994/xiaotang-daozai&amp;type=date" />
    <img alt="岛仔 GitHub 星标增长曲线" src="https://api.star-history.com/chart?repos=Renly1994/xiaotang-daozai&amp;type=date" />
  </picture>
</a>

## 微信里有新消息，看一眼岛边

![微信和 QQ 未读：收起时显示图标，展开后点击切换对应窗口](docs/images/readme/notifications.webp)

- **微信、QQ 未读提醒**：收起时亮起图标和红点，展开后在面板旁查看，点击切换到对应窗口。
- **微信多开分开看**：不同账号分别显示，点击对应账号的未读图标即可切换。
- **按需显示通知正文**：默认隐藏正文；开启预览后仍遮罩识别出的验证码。
- **微信提醒不读取聊天正文**：根据任务栏闪动提示新消息。微信缩在托盘时，可选开启「托盘一键唤起微信」。
- **企业微信、飞书和钉钉**：在消息提醒设置里分别开启，并确认对应客户端允许任务栏闪动。新消息会在岛上提醒，点一下即可打开对应窗口。

在 **设置 → 消息提醒** 开启「微信」。QQ 可从「QQ 与其他应用 → 连接…」选择「只连接 QQ」，并在 QQ 中启用 Windows 系统通知。

## 换个皮肤，也换个位置

![五款皮肤：经典黑、奶油、毛玻璃浅色、毛玻璃深色、悬浮云；刘海和胶囊两种形态](docs/images/readme/appearance.webp)

**五款皮肤 × 两种形态，自由搭配。** 经典黑、奶油、毛玻璃·浅、毛玻璃·深和「悬浮云」，都能搭配刘海或胶囊。毛玻璃透出身后的桌面；悬浮云随专辑封面换色，光晕跟着鼠标移动。

![顶部、左侧和右侧停靠，以及侧边收起与展开状态](docs/images/readme/docking.webp)

- **四边停靠**：顶部和底部横向排列，底部向上展开，会跟随自动隐藏的任务栏。左右侧边收起为竖向胶囊，鼠标靠近后从屏幕边缘展开。
- **大小与位置可调**：岛体大小支持 80%–140%，上下停靠可左右移动，侧边可上下调整。展开后按住日期时间，可以切换停靠边或把小岛拖到另一块屏幕。
- **OLED 像素偏移**（默认关闭）：收起静止时沿停靠边缓慢移动几个像素，帮助减轻 OLED 静态显示留下的痕迹。
- **多屏与自动避让**：跟随主屏或固定到指定显示器。前台浏览器或自定义应用的窗口遮住岛时，岛会收成贴边细线。切到插件浮窗时，如果名单里的宿主窗口仍遮住岛，岛会继续避让。
- **按习惯显示**：支持极简模式、12／24 小时制，以及功能页面开关与拖动排序。

在 **设置 → 外观／位置** 里分别调整皮肤、形态和停靠。岛上单行歌词支持顶部和底部停靠。

在 **设置 → 通用** 开启「在截图和录屏中隐藏岛仔」后，桌面照常显示小岛，兼容的截图和录屏工具会略过它。该选项需要 Windows 10 2004 或更新版本。

## 插件集市

官方和社区一起为小岛扩展功能。插件可以更换外观材质、增加功能页，也可以扩展页面切换和无线设备兼容。

![岛仔插件集市，展示液态玻璃、我的日子和现货金价](docs/images/readme/plugin-market.webp)

集市里有**液态玻璃、我的日子、现货金价、实时工资、便签本、世界时钟、页面快捷切换和无线设备兼容包**等插件。

[浏览岛仔插件仓](https://github.com/Renly1994/xiaotang-daozai-plugins)

## 听歌时，歌词就在抬眼处

![音乐播放控制、展开歌词与收起状态下的岛上单行歌词](docs/images/readme/music.webp)

播放、暂停、切歌、调节音量和拖动进度，都能在岛上操作。展开看歌词，也可以收起后只留一行歌词，让桌面继续做自己的事。

- 通过 Windows 媒体会话读取播放信息，并针对网易云音乐、QQ 音乐、酷狗、汽水音乐和波点音乐补充兼容。
- 网易云优先按歌曲 ID 找词，改善译名、合唱署名和 Live／Remix 等不同版本的匹配。
- 切歌、暂停和拖动进度时更快同步到岛上，改善了网易云和酷狗部分版本的进度适配。

播放器需提供可用的媒体信息；歌词取决于歌曲元数据与歌词来源，个别歌曲或播放器版本可能无法显示。

## 日程、待办和专注，放在一起

![日历与会议安排、每周重复待办、番茄专注与饮水提醒](docs/images/readme/daily.webp)

| 想做的事 | 岛仔能帮你 |
| --- | --- |
| 看今天的安排 | 月历与当日时间线，合并多个日历和正式邮件邀请，提前提醒会议 |
| 记住每周的事 | 待办支持单次提醒、每周指定日期重复或每天重复；下一次到来时恢复为待办 |
| 专心做一件事 | 专注与休息计时，收起时也能查看进度 |
| 记得喝水 | 自定义每日目标、单次饮水量、提醒间隔与时段，记录错误可撤销 |

日历可接入 **飞书、钉钉、企业微信、iCloud、自定义 CalDAV 和兼容的 Exchange ActiveSync**，也能导入 `.ics` 文件。相同日程合并去重；支持全天、跨天和重复日程。

日程可按日期浏览，月历能看农历和节气。新建本机日程时可直接选日期和时间。在 **设置 → 通用** 可把公历、农历或两者一起放到岛上常驻。

本机新建或导入的日程保存在本机；远程日历为只读同步。程序退出、电脑关机或睡眠期间无法持续提醒。

## 文件先放岛上，刚复制的字也能找回

![文件置物架与剪贴板历史：拖入文件、重新复制文字、固定常用内容](docs/images/readme/shelf.webp)

**文件置物架**：拖入文件临时收集，点击打开、定位原文件，或拖出到其他应用。移除记录不会删除原文件。

**文字剪贴板**：找回最近复制的 30 条文字，点一下重新复制，常用内容可以固定。历史保存在本机，重启后仍可查看；可在 **设置 → 待办与置物 → 剪贴板** 中关闭。密码管理器标记为敏感的内容不记录。

在置物架或剪贴板页点「保持展开」，鼠标移开后面板仍会留在桌面，方便连续拖放或复制。

## 验证码少切一次窗口，邮件也能直接读

![验证码大卡点击复制与邮件正文阅读](docs/images/readme/mail.webp)

连接多个邮箱，在岛上查看来信、识别验证码并点击复制。邮件支持正文阅读与独立全文窗口，网页链接交给默认浏览器打开；正式日历邀请可进入日程。支持已读／未读切换、全部已读、移到回收站及恢复；默认仅在本机整理，可在邮件设置中开启「同步邮件操作到邮箱」。

支持 **QQ、163、126、腾讯企业邮、iCloud、Gmail 和自定义 IMAP**。验证码可设置在 30／60／300 秒后自动隐藏，覆盖列表、正文与通知；主动查看后会再次隐藏。

- 在 **设置 → 邮箱** 开启「仅提醒验证码邮件」，普通来信照常收取，可在邮件列表里查看。
- 开启「验证码高亮」后，可以再打开「避让时弹出验证码」。小岛自动避让时，新验证码也可短暂显示为横幅，点击即可复制。
- Gmail 收信可按需开启「使用 Windows 手动代理」。

## AI 还剩多少额度，抬眼就知道

![AI 额度面板：Codex 额度、WorkBuddy 积分与 DeepSeek 余额](docs/images/readme/ai-quota.webp)

支持 **Codex、Claude、Kimi、Grok Bot、Gemini、GLM Coding Plan、WorkBuddy、DeepSeek、Kiro、豆包、OpenCode Go、MiniMax Coding Plan 和 Antigravity**。

订阅额度、重置时间、套餐积分与 API 余额，按服务展示。多个账号可分别命名、选择配色，常用账号直接放在收起的小岛上。

- **GLM / ZCode**：填写 Coding Plan 套餐 Key 查询额度。本机 ZCode 的旧连接可在 AI 额度设置中重新连接；Start Plan 体验额度在 ZCode 官方客户端查看。
- **Claude**：只读取桌面版本地用量历史与缓存，或接收 Claude Code 官方状态栏输出；岛仔不使用 Claude 登录令牌，也不请求 Claude 额度接口。数据随官方客户端使用更新，桌面版缓存有效时自动显示重置时间，读取不到时显示未知。
- **Kiro**：只