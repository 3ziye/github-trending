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

<p align="center"><b>跑在你自己电脑上的 AI 机器人。任意模型，按量付费。</b></p>

<p align="center">
  <a href="https://anymodel.bot/">官网</a> |
  <a href="https://github.com/modelflare-ai/AnyModelBot/releases">下载</a> |
  简体中文 |
  <a href="./README_en.md">English</a> |
  <a href="./README_ja.md">日本語</a> |
  <a href="./README_ko.md">한국어</a> |
  <a href="./README_ru.md">Русский</a> |
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

AnyModelBot 是一个本地优先的 AI 智能体应用，支持 Windows、macOS 和 Linux。一个机器人就是一个人设，带着自己的默认模型、工作区和记忆。你可以在应用里和它聊天，也可以在微信、飞书、Telegram、Slack、Discord 里找它。它能读写文件、执行命令、操作你的桌面，一旦要越出自己的工作区，就会先问你。

对话、记忆、文件和 API Key 都留在你的设备上。模型可以来自 [Modelflare](https://modelflare.dev/?utm_source=anymodelbot&utm_campaign=amb_readme)（一个账户，任意模型，按 token 计费），也可以填你自己的官方 API Key，直连 OpenAI、Anthropic、Google 等厂商。AnyModelBot 本身没有订阅。

和 xAI 的 Grok Bot、OpenAI 的 dots、Anthropic 的 Claude Duet 一样，它是一个常驻的个人 AI 智能体：在后台替你干活，需要你拍板时再来问你。不同的是，AnyModelBot 开源（MIT），跑在你自己的电脑或服务器上，GPT、Claude、Gemini、Grok 等任意模型都能用，按量付费，不绑定某一家的订阅（[详细对比](#-对比-grok-bot--openai-dots--claude-duet)）。

装好就是一个开箱即用的 Super Agent：后台任务、定时规则和「需要你」都不用另外配置。它的设计参考了 DeepSeek 的 [Super Agent 原型](https://github.com/deepseek-ai/dsh-superagent-prototype)，智能体运行在 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 上（[详细介绍](./docs/blog/superagent.md)）。

📥 [下载](#-下载) · 🌠 [截图](#-截图) · 🌟 [核心功能](#-核心功能) · 🆚 [对比](#-对比-grok-bot--openai-dots--claude-duet) · 🔐 [工作原理与隐私](#-工作原理与隐私)

⭐ 喜欢 AnyModelBot？点个 Star，第一时间收到新版本。

---

<a href="https://modelflare.dev/sign-up?utm_source=anymodelbot&utm_campaign=amb_readme">
  <img src="docs/assets/modelflare/modelflare-banner-zh.webp" width="100%" alt="Modelflare 横幅：满血、稳定不掺水，低成本享受全球 SOTA 模型；GPT 特惠分组 0.015 倍、Claude 特惠分组 0.03 倍；OpenAI 分组缓存命中率保障 65% · 75% · 85%，未达标补偿差额">
</a>

最省事的用法是 **[Modelflare](https://modelflare.dev/?utm_source=anymodelbot&utm_campaign=amb_readme)**：一个账户就够，不用分别申请各家的 Key（想直连厂商，见[任意模型](#-任意模型通过-modelflare-或官方-api)）。满血、稳定不掺水，低成本享受全球 SOTA 模型。Modelflare 由美国公司 Havenbyte LLC 运营，已有 20 万+ 注册开发者。一个 API Key 就能调用 13 家供应商的 70+ 个文本、图片和视频模型，GPT、Claude、Gemini、Grok、DeepSeek、Kimi、GLM 都在里面，兼容 OpenAI、Anthropic、Gemini 等常用接口协议。请求会在多个供应商之间路由并自动回退，每一次请求都记录用量和费用，价格表公开，按 token 计费。

**缓存补偿**是一大亮点：OpenAI 的价格优先、稳定、高级三个分组，分别保证每天 65%、75%、85% 的缓存命中率；符合条件的请求没达到目标，Modelflare 会补偿差额。

**特惠活动**：单笔充值达到指定金额，就能解锁 0.015 倍价格倍率的 GPT 特惠分组和 0.03 倍的 Claude 特惠分组，适合个人开发、功能验证和轻量使用。这是限时活动，门槛和规则以 Modelflare 页面为准，通过[专属链接](https://modelflare.dev/sign-up?utm_source=anymodelbot&utm_campaign=amb_readme)注册即可参与。

**[注册 Modelflare →](https://modelflare.dev/sign-up?utm_source=anymodelbot&utm_campaign=amb_readme)** ·
[价格表](https://modelflare.dev/pricing?utm_source=anymodelbot&utm_campaign=amb_readme) ·
[API 文档](https://docs.modelflare.dev/?utm_source=anymodelbot&utm_campaign=amb_readme) ·
[信任中心](https://modelflare.dev/trust?utm_source=anymodelbot&utm_campaign=amb_readme) ·
[X](https://x.com/modelflare_dev)

**AnyModelBot 怎么用 Modelflare**

- **登录一次就行。** 首次启动会打开浏览器，登录（或注册）Modelflare。之后应用自己把这台设备连上，不用复制 Key。在 Docker 或服务器上运行？在任意设备的浏览器里登录，再把登录后的链接贴回应用。
- **所有模型，一个选择器。** 你的 Modelflare 模型会自动列出，每个模型旁边都有上下文长度、能力标记和参考价。
- **用多少付多少。** 余额、低余额提醒和每日用量都在应用里看。选模型之前，先看公开价格表，和官方价格对比一下。
- **一条诚实的边界。** 模型请求会经过 Modelflare 转发给你选定的供应商，Modelflare 会保留请求日志；保留什么、保留多久，见[信任中心](https://modelflare.dev/trust?utm_source=anymodelbot&utm_campaign=amb_readme)。除此之外的内容都留在你的设备上（[详情](#-工作原理与隐私)）。

---

# 📥 下载

选择你的平台。每个 Release 页面都列出全部安装包和 `SHA256SUMS` 校验文件。

| 平台 | 架构 | 安装包 | |
| :--- | :--- | :--- | :--- |
| ![Windows][win-badge] | x64 | `anymodel-bot-<version>-win-x64.exe` | [下载][releases-link] |
| ![Windows][win-badge] | arm64 | `anymodel-bot-<version>-win-arm64.exe` | [下载][releases-link] |
| ![macOS][mac-badge] | Apple 芯片 | `anymodel-bot-<version>-mac-arm64.dmg` | [下载][releases-link] |
| ![mac