# DSHA

<p align="center">
  <b>DeepSeek Harness 安卓启动器</b><br>
  在手机上跑完整的 <a href="https://github.com/deepseek-ai/deepseek-harness">deepseek-harness</a> —— 免 ROOT，免 Termux，装完即用
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT"></a>
  <a href="https://github.com/qiannianhuanxiang/DSHA/releases/latest"><img src="https://img.shields.io/github/v/release/qiannianhuanxiang/DSHA?color=blue" alt="release"></a>
  <a href="https://github.com/qiannianhuanxiang/DSHA/stargazers"><img src="https://img.shields.io/github/stars/qiannianhuanxiang/DSHA?style=flat" alt="stars"></a>
  <img src="https://img.shields.io/badge/Android-8.0%2B-3DDC84?logo=android&logoColor=white" alt="android">
  <img src="https://img.shields.io/badge/arch-arm64--v8a-lightgrey" alt="arch">
</p>

<p align="center">
  <a href="README.en.md">English</a> · <b>简体中文</b> · <a href="CHANGELOG.md">更新记录</a> · <a href="docs/security-model.md">安全模型</a> · <a href="AGENTS.md">AGENTS.md（给 AI / 开发者）</a>
</p>

> 🤖 下一个 AI / 开发者请先读 **[AGENTS.md](AGENTS.md)**（项目结构、启动契约、踩过的坑），不要先全库扫描。

---

## DSHA目前正在进行大规模重构，更新较慢👀


## 这是什么

DeepSeek Harness（`@deepseek-ai/dsh`）是 DeepSeek 官方的 agent harness，类 Claude Code。
它是为 glibc Linux 写的，直接在安卓上跑会撞上一堆事：原生模块编译不过、`link(2)` 被
SELinux 挡住、沙箱起不来、前端按桌面布局排版。

**DSHA 把这些全部封在一个 APK 里。** 装 APK、填 API key(或跳过)、点启动 —— 不需要 Termux、
不需要 ROOT、不需要敲一行命令。里面是一个完整的 Ubuntu 24.04 环境：`apt` 能用、
交互式 PTY 能用、需要编译的原生模块能装，跟你在服务器上用是同一套东西。

---

## 为什么是 DSHA

|  | 说明 |
|---|---|
| 🚫 **零命令行门槛** | 内置离线 Ubuntu rootfs，APK 装完就能用。不装 Termux、不配 pkg、不敲命令 |
| 🐧 **完整 glibc 环境** | 不是裁剪版：`apt` / PTY / 原生模块 / Python / git 都在。上游插件不用改就能跑 |
| ⚡ **proroot 零 ptrace 开销** | 传统 proot 每个系统调用两次上下文切换；proroot 走 LD_PRELOAD + 二进制补丁做进程内路径翻译。真机实测关键项合计 **+58%** |
| 🔌 **ADB 免 Shizuku 直连** | 内置无线配对与保活，agent 可以直接操作这台手机（点击、截屏、装应用） |
| 💾 **卸载重装数据不丢** | 对话与设置放在 `Documents/dshdata`，文件管理器里可见可备份；API key 走 Android Keystore 加密 |
| 🩺 **坏了能自己说清哪坏了** | 23 项自检 + 一键修补 + 15 个自愈脚本；Web 起不来时直接点名是哪个插件 |

---

## 30 秒上手

1. 到 [Releases](https://github.com/qiannianhuanxiang/DSHA/releases/latest) 下最新 APK 装上（仅 arm64）
2. 首次启动解压内置环境（几分钟，只有一次）
3. 「配置」页填 DeepSeek API key →「启动」页点启动 → 自动打开 Web UI

就这样。想跑得更细可以走「分步安装」，每步都能单独重装、单独更新。

---

## 能力全景

DSHA 不只是「能跑起来」。下面每一项都是实装的功能。

<details open>
<summary><b>① 环境与装机</b></summary>

| 能力 | 说明 |
|---|---|
| 内置离线 rootfs | Ubuntu 24.04 arm64 打进 APK，无网也能完成环境部署 |
| 分步安装 | rootfs / 基础工具 / Node.js / harness 四步独立，可单独重装与更新，不重复下载 |
| 多源并行测速 | 清华、阿里云、华为云、腾讯云、南大、哈工大、npmmirror… 测完弹窗自选 |
| 双装机路径 | 预构建包与源码构建都支持，源码路径会自动处理 node-pty 等原生模块的编译问题 |
| 安装即校验 | 每步装完立刻验产物，不把「装了一半」当成功 |
| 断点续装 | 中途失败或退出后回到该步继续，不从头再来 |

</details>

<details open>
<summary><b>② 运行时与性能</b></summary>

| 能力 | 说明 |
|---|---|
| proroot / proot 双运行时 | 默认 proroot（零 ptrace 开销），「配置」页一键切回 proot |
| 实测提升 | vivo V2352A / Android 14：关键项合计 +58%，tar 打包 +94%（备份走这条），stat 密集 +82%（node 模块解析） |
| 三层兜底 | 运行时文件缺失自动降回 proot；连续 3 次启动失败强制切回并告知；装机路径始终用 proot |
| Node.js 24 + pnpm | 与上游一致的运行环境 |
| 前台服务常驻 | 通知栏可见运行状态，系统不会随手回收 |
| 看门狗 | Web 掉了自动拉起，不用手动重启 |

</details>

<details open>
<summary><b>③ 数据安全与迁移</b></summary>

| 能力 | 说明 |
|---|---|
| 数据不随卸载消失 | 会话 / 设置 / 附件放 `内部存储/Documents/dshdata`，原位留私有软链 |
| API key 加密存储 | Android Keystore（AES/CBC），密钥不出 Keystore；备份里那份也加密 |
| 全量备份 | 手动备份保留 10 份轮换，自动备份**双槽交替**（永远留着上一份完整的） |
| 分范围备份 | 备份时可选**全量 / 只对话 / 只插件**。部分备份恢复时只覆盖对应内容 —— 拿只含对话的包恢复，配置与插件保持现状 |
| 换机不丢对话 | 对话等热数据在手机上是指向公开目录的符号链接，`tar` 默认只存链接、换设备恢复就是空的；备份会额外把它们解引用快照一份 |
| 备份自带说明 | 包里放 `DSHA-README.txt`：里面有什么、怎么手动取数据、哪些东西换设备后用不了 |
| 恢复前体检 | 只读走一遍整个包，靠 gzip 的 CRC 发现截断与损坏，并预览「多少会话 / 多大 / 来自哪个版本」 |
| 恢复极宽容 | 老备份一律放行；缺失插件后台自动补装；跨设备的 `link:` 路径自动重写；本机路径插件的源码随包内联 |
| 恢复后自动适配 | 跑一遍版本迁移（下线已换掉的内置插件、补回新的）并重新对齐桥 token |
| 凭据不进备份 | 本机桥 token 排除在外 —— 备份落在公共目录，不该带走这台机器的凭据 |
| 会话损坏隔离 | 坏掉的会话文件挪到 `corrupt-backup`，随时可取回，不让一个坏文件卡住整个 Web |

</details>

<details open>
<summary><b>④ 设备能力（让 agent 真正操作这台手机）</b></summary>

| 能力 | 说明 |
|---|---|
| ADB 无线直连 | 内置配对与保活，**不需要 Shizuku**。agent 可以点击、滑动、截屏、装应用、读日志 |
| Shizuku 通道 | 作为备用路径保留，已授权的用户可继续用 |
| App 桥（127.0.0.1:3090） | agent 可以发系统通知、读设备信息、请求用户确认 |
| 危险命令守门人 | 覆盖关键路径、递归删除等命令会拦下来问你，**三条渠道**（通知 / 前台弹窗 / 悬浮条）任选其一批准 |
| 流式悬浮条 | AI 输出像歌词一样实时贴在屏幕顶部；显示正在执行的命令原文，思考过程可选；底色 / 透明度 / 行数 / 停留时间都能调，带预览 |
| 内置终端 | 直接进 Ubuntu shell，`apt install` 什么都行 |
| 免 ROOT 文件访问 | 注入 MT 管理器文件提供器，在文件管理器里直接浏览、编辑 App 私有目录 |

</details>

<details open>
<summary><b>⑤ 可靠性：坏了能自己说清哪坏了</b></summary>

| 能力 | 说明 |
|---|---|
| 23 项自检 + 一键修补 | 桥 / ADB / 插件 / 会话 / 备份 / 运行时 / 公开数据 / 守卫补丁 / Web 鉴权… 逐项体检，能自动修的当场修 |
| 插件故障人话诊断 | Web 起不来时直接说「是插件 X，它要的服务不存在，点这里修」，而不是甩一屏 Node 堆栈 |
| 15 个自愈与补丁脚本 | pnpm 空壳还原、bundle 解析修复、profile 引导修复、`.l2s` 链摊平、会话修复、依赖修复、写文件补丁… |
| 脚本增量热更新 | 关键脚本可从 GitHub 增量更新并**离线验签**（公钥内置，签名不符整批拒绝），不必等新 APK |
| 失败原因落盘 | 备份、安装、启动的失败原因写进文件，自检直接读 —— 不让「没反应」变成无从排查 |
| CI 守门人 | 每次推送跑 Fast checks：清单一致性 + 离线验签 + 300 条纯逻辑断言 + assets 脚本真编译；发布时证书指纹不符直接中止 |

</details>

<details open>
<summary><b>⑥ 网络与访问</b></summary>

| 能力 | 说明 |
|---|---|
| 内嵌 WebView | GeckoView，不受系统 WebView 版本拖累 |
| 局域网访问 | 手机开着 dsh，电脑 / 平板直接在浏览器里用。t