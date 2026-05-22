# Codex++

<p align="center">
  <img src="docs/images/codex-plus-plus.png" alt="Codex++ 图标" width="160">
</p>

<p align="center">
  中文 | <a href="README_EN.md">English</a>
</p>

<p align="center">
  <img alt="Release" src="https://img.shields.io/github/v/release/BigPizzaV3/CodexPlusPlus">
  <img alt="Stars" src="https://img.shields.io/github/stars/BigPizzaV3/CodexPlusPlus">
  <img alt="License" src="https://img.shields.io/github/license/BigPizzaV3/CodexPlusPlus">
  <img alt="Rust" src="https://img.shields.io/badge/rust-1.85%2B-orange">
  <img alt="Tauri" src="https://img.shields.io/badge/tauri-2.x-24C8DB">
</p>

Codex++ 是面向 Codex App 的外部增强启动器和管理工具。它不修改 Codex App 原始安装文件，而是通过外部 launcher 启动 Codex，并使用 Chromium DevTools Protocol 注入增强脚本。

## 快速使用

从 [GitHub Releases](https://github.com/BigPizzaV3/CodexPlusPlus/releases) 下载最新版安装包：

- Windows：`CodexPlusPlus-*-windows-x64-setup.exe`
- macOS Intel：`CodexPlusPlus-*-macos-x64.dmg`
- macOS Apple Silicon：`CodexPlusPlus-*-macos-arm64.dmg`

安装后会有两个入口：

- `Codex++`：静默启动入口，不显示管理界面，只负责启动 Codex 并注入增强功能。
- `Codex++ 管理工具`：Tauri 控制面板，用于启动、检查、修复、更新、配置中转注入、管理增强功能和用户脚本。

Windows 安装包会创建桌面和开始菜单快捷方式。macOS DMG 会安装 `/Applications/Codex++.app` 和 `/Applications/Codex++ 管理工具.app`。

## 赞助商
<a href="mailto:1727532@qq.com">想显示在下方？</a>
<p align="center">
</p>
<table>
  <tr>
    <th width="180">🏆 赞助商 🏆</th>
    <th>介绍</th>
  </tr>
  <tr>
    <td align="center">
      <a href="https://jojocode.com/">
        <img src="docs/images/sponsor-jojocode.svg" alt="JOJO Code" width="150">
      </a>
    </td>
    <td><a href="https://jojocode.com/"><strong>JOJO Code｜Codex++ 官方中转站</strong></a><br>感谢 JOJO Code 赞助了本项目！JOJO Code 是 Codex++ 官方中转站，面向日常开发和团队协作场景，提供稳定可用的 Codex API 接入体验，适合快速接入、长期使用和项目级工作流。</td>
  </tr>
  <tr>
    <td align="center">
      <a href="https://aigocode.com/invite/CodexPlusPlus">
        <img src="docs/images/sponsor-aigocode.png" alt="AIGoCode" width="150">
      </a>
    </td>
    <td><a href="https://aigocode.com/invite/CodexPlusPlus"><strong>AIGoCode</strong></a><br>感谢 AIGoCode 赞助了本项目！AIGoCode 是一个集成了 Claude Code、Codex 以及 Gemini 最新模型的一站式平台，为你提供稳定、高效且高性价比的AI编程服务。本站提供灵活的订阅计划，支持多风险，国内直连，无需魔法，极速响应。AIGoCode 为 CodexPlusPlus 的用户提供了特别福利，通过<a href="https://aigocode.com/invite/CodexPlusPlus">此链接注册</a>的用户首次充值可以获得额外10%奖励额度！</td>
  </tr>
  <tr>
    <td align="center">
      <a href="https://www.packyapi.com/">
        <img src="docs/images/sponsor-packycode.png" alt="PackyCode" width="150">
      </a>
    </td>
    <td><a href="https://www.packyapi.com/"><strong>PackyCode</strong></a><br>感谢 PackyCode 赞助了本项目！PackyCode 是一家稳定、高效的API中转服务商，提供 Claude Code、Codex、Gemini 等多种中转服务。PackyCode 为本软件的用户提供了特别优惠，使用此链接注册并在充值时填写"CodexPlusPlus"优惠码，首次充值可以享受9折优惠！</td>
  </tr>
  <tr>
    <td align="center">
      <a href="https://www.0029.org/?promo=AFF11F">
        <img src="docs/images/sponsor-0029.svg" alt="0029 云桥" width="150">
      </a>
    </td>
    <td><a href="https://www.0029.org/?promo=AFF11F"><strong>0029云桥｜codex api中转站(gpt5.5 gpt-image-2)</strong></a><br>支持个人和企业接入。包月套餐/按量计费，Pro/Plus 号池，全站接口稳定可用，7×24 小时技术支持！</td>
  </tr>
  <tr>
    <td align="center">
      <a href="https://rawchat.cn">
        <img src="docs/images/sponsor-rawchat.svg" alt="RawChat" width="150">
      </a>
    </td>
    <td><a href="https://rawchat.cn"><strong>RawChat｜Codex 中转站</strong></a><br>老牌中转站，支持包月套餐。低倍率调用，高缓存命中，Pro/Plus 号池，全天专人维护。</td>
  </tr>
  <tr>
    <td align="center">
      <a href="https://coder.visioncoder.cn">
        <img src="https://coder.visioncoder.cn/logo.png" alt="VisionCoder" width="110">
      </a>
    </td>
    <td><a href="https://coder.visioncoder.cn"><strong>VisionCoder 开发平台</strong></a><br>感谢 VisionCoder 对本项目的支持。VisionCoder 开发平台是一个可靠高效的 API 中继服务提供商，提供 Claude Code、Codex、Gemini 等主流 AI 模型，帮助开发者和团队更轻松地集成 AI 功能，提升工作效率。VisionCoder 还为我们的用户提供 <a href="https://coder.visioncoder.cn">Token Plan</a> 限时活动：购买 1 个月，赠送 1 个月。</td>
  </tr>
</table>



## 交流与支持

欢迎扫码加入 Codex++ 交流群，反馈问题、交流使用体验或提出新功能建议：

<img src="docs/images/discussion-group-qr.jpg" alt="Codex++ 交流群二维码" width="260">

如果 Codex++ 帮到了你，可以请我喝杯咖啡，或者随手赞赏支持一下继续维护。

<p align="center">
  <img src="docs/images/sponsor-alipay.jpg" alt="支付宝赞赏码" width="220">
  <img src="docs/images/sponsor-wechat.jpg" alt="微信赞赏码" width="220">
</p>

## 主要功能

- Rust 后端和静默 launcher，启动时不依赖额外运行时。
- Tauri + React 管理工具，支持深色/浅色切换。
- 外部 CDP 注入，不改 `app.asar`，不向 Codex 安装目录写入 DLL。
- 中转注入模式：支持多个中转配置，写入 `CodexPlusPlus` provider，并可切回官方 ChatGPT 登录态。
- 传统增强模式：插件入口解锁、特殊插件强制安装、会话删除、Markdown 导出、项目移动、Timeline 等。
- 用户脚本独立管理，可在启动时注入自定义脚本。
- Provider 同步：启动前同步本地会话 metadata，切换供应商后旧会话仍可见。
- Zed 打开入口：识别远程 SSH 上下文后，可从 Codex 直接打开对应文件到 Zed Remote Development。
- GitHub Release 自动更新，管理工具和静默启动器都会检测可用更新。
- Windows 单实例、无黑框启动、管理员权限清单、系统桌面路径识别。
- macOS x64/arm64 分架构 DMG，静默入口隐藏 Dock 图标。

## 痛点与解决

API Key 登录模式下，Codex 原生插件入口会提示需要登录 ChatGPT，导致插件功能无法正常使用：

![API Key 模式下插件入口不可用](docs/images/pain-plugin-disabled.png)

Codex 原生会话列表只有归档入口，没有真正的删除按钮：

![原生会话列表缺少删除能力](docs/images/pain-no-delete-button.png)

Codex++ 启动后会解锁插件入口，并在会话列表悬停时显示删除按钮