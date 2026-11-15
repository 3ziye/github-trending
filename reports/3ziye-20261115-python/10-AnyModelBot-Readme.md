<p align="center">
  <a href="https://github.com/modelflare-ai/AnyModelBot/releases">
    <img src="docs/assets/brand/logo-eyes.webp" width="120" height="120" alt="AnyModelBot 的 Eyes 标志：两只竖向胶囊形的眼睛，会左右张望">
  </a>
</p>

<h1 align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/brand/wordmark-dark.svg">
    <img src="docs/assets/brand/wordmark-light.svg" height="40" alt="AnyModelBot">
  </picture>
</h1>

<p align="center"><b>跑在你自己电脑上的 AI 机器人团队。任意模型，按量付费。</b></p>

<p align="center">
  <a href="https://anymodel.bot/">官网</a> |
  <a href="https://github.com/modelflare-ai/AnyModelBot/releases">下载</a> |
  简体中文 |
  <a href="./README_en.md">English</a> |
  <a href="./README_ja.md">日本語</a> |
  <a href="./README_ko.md">한국어</a> |
  <a href="./README_ru.md">Русский</a> |
  <a href="./README_es.md">Español</a> |
  <a href="./README_pt.md">Português (Brasil)</a> |
  <a href="https://modelflare.dev/?utm_source=anymodelbot&utm_campaign=amb_readme">Modelflare</a> |
  <a href="https://modelflare.dev/pricing?utm_source=anymodelbot&utm_campaign=amb_readme">价格</a> |
  <a href="./docs/development.md">开发文档</a> |
  <a href="https://github.com/modelflare-ai/AnyModelBot/issues">问题反馈</a>
</p>

<div align="center">

[![Release][release-shield]][releases-link]
[![Downloads][downloads-shield]][releases-link]
[![Stars][stars-shield]][stars-link]
[![License][license-shield]][license-link]
[![CI][ci-shield]][ci-link]

[![Platform][platform-shield]][releases-link]
[![Pricing][pricing-shield]][pricing-link]
[![Modelflare][modelflare-shield]][modelflare-link]
[![X][x-shield]][x-link]

</div>

<p align="center">
  <img src="docs/assets/hero/hero-demo.gif" alt="AnyModelBot 演示：登录 Modelflare、选择模型、让机器人整理一个文件夹，并批准一次文件移动" width="100%">
</p>

# 🤖 AnyModelBot

AnyModelBot 是跑在 Windows / macOS / Linux 上的 AI 机器人团队。每个机器人有自己的人设、默认模型、工作区和记忆；可在应用内聊天，也可接入微信、飞书、Telegram、Slack、Discord。它能读写文件、执行命令、在授权后操作桌面；要写到工作区以外，会先问你。

对话、记忆、文件和 API Key 留在你的设备上。模型可走 [Modelflare](https://modelflare.dev/?utm_source=anymodelbot&utm_campaign=amb_readme)（登录后按用量付费），或使用自己的官方 API Key 直连厂商。AnyModelBot 本身没有订阅费。

装好即可用：后台任务、定时规则和待你确认的事项都已内置。

**0.1.37：** 「关于我」所有机器人共用，关于你的事说一次都知道；一句「交给 B」让机器人之间互相发消息，做完核对后再告诉你。 [更新日志](./CHANGELOG.md#0137---2026-11-15)

📥 [下载](#-下载与运行) · 🌠 [截图](#-截图) · 🌟 [核心功能](#-核心功能) · 🆚 [对比](#-对比-grok-bot--openai-dots--claude-duet) · 🔐 [工作原理与隐私](#-工作原理与隐私)

⭐ 喜欢 AnyModelBot？点个 Star，第一时间收到新版本。

---

<a href="https://modelflare.dev/sign-up?utm_source=anymodelbot&utm_campaign=amb_readme">
  <img src="docs/assets/modelflare/modelflare-banner-zh.webp" width="100%" alt="Modelflare 横幅：点击注册 Modelflare">
</a>

最省事的用法是 **[Modelflare](https://modelflare.dev/?utm_source=anymodelbot&utm_campaign=amb_readme)**：登录即可使用模型，不用分别申请各家的 Key（想直连厂商，见[任意模型](#-任意模型通过-modelflare-或官方-api)）。可用模型、价格和当前活动以 [Modelflare](https://modelflare.dev/?utm_source=anymodelbot&utm_campaign=amb_readme) 和 [价格表](https://modelflare.dev/pricing?utm_source=anymodelbot&utm_campaign=amb_readme) 为准。

**Bot 额度**：新用户注册即送 Bot 额度，订阅 Modelflare 套餐另送套餐额度 10% 的 Bot 额度，具体以 Modelflare 页面为准。Bot 额度只能在 AnyModelBot 里使用，应用里的请求会先用它，剩余额度可在「设置 → 模型」查看。

**[注册 Modelflare →](https://modelflare.dev/sign-up?utm_source=anymodelbot&utm_campaign=amb_readme)** ·
[价格表](https://modelflare.dev/pricing?utm_source=anymodelbot&utm_campaign=amb_readme) ·
[API 文档](https://docs.modelflare.dev/?utm_source=anymodelbot&utm_campaign=amb_readme) ·
[信任中心](https://modelflare.dev/trust?utm_source=anymodelbot&utm_campaign=amb_readme) ·
[X](https://x.com/modelflare_dev)

**AnyModelBot 怎么用 Modelflare**

- **登录一次就行。** 首次启动会打开浏览器，登录（或注册）Modelflare。之后应用自己把这台设备连上，不用复制 Key，授权完成后会自动回到应用；还没有默认模型时，会先选好一个支持工具、花费低的模型。在 Docker 或服务器上运行？在任意设备的浏览器里登录，再把登录后的链接贴回应用。
- **所有模型，一个选择器。** 你的 Modelflare 模型会自动列出，每个模型旁边都有上下文长度、能力标记和参考价。
- **用多少付多少。** 余额和充值入口集中在「设置 → 模型」（有 Bot 额度时还显示剩余额度和百分比），低余额提醒和每日用量也都在应用里看。选模型之前，先看公开价格表，和官方价格对比一下。
- **一条诚实的边界。** 模型请求会经过 Modelflare 转发给你选定的供应商，Modelflare 会保留请求日志；保留什么、保留多久，见[信任中心](https://modelflare.dev/trust?utm_source=anymodelbot&utm_campaign=amb_readme)。除此之外的内容都留在你的设备上（[详情](#-工作原理与隐私)）。

---

# 📥 下载与运行

选择你的平台。每个 Release 页面都列出全部安装包和 `SHA256SUMS` 校验文件。

| 平台 | 架构 | 安装包 | |
| :--- | :--- | :--- | :--- |
| ![Windows][win-badge] | x64 | `anymodel-bot-<version>-win-x64.exe` | [下载][releases-link] |
| ![Windows][win-badge] | arm64 | `anymodel-bot-<version>-win-arm64.exe` | [下载][releases-link] |
| ![macOS][mac-badge] | Apple 芯片 | `anymodel-bot-<version>-mac-arm64.dmg` | [下载][releases-link] |
| ![macOS][mac-badge] | Intel | `anymodel-bot-<version>-mac-x64.dmg` | [下载][releases-link] |
| ![Linux][linux-badge] | x64 | `anymodel-bot-<version>-linux-x86_64.AppImage` | [下载][releases-link] |
| ![Linux][linux-badge] | arm64 | `anymodel-bot-<version>-linux-arm64.AppImage` | [下载][releases-link] |

<p align="center">
  <img src="docs/assets/download/install-windows.gif" alt="在 Windows 上安装 AnyModelBot：运行安装程序、打开应用，来到 Modelflare 登录页" width="100%">
</p>

**首次打开。** Windows 出现系统风险提示时，点「更多信息 → 仍要运行」。macOS 版已完成 Developer ID 签名和苹果公证，将应用拖入「应用