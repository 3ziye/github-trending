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
        <img src="docs/images/sponsor-jojocode.svg" alt="JOJO Code" height="80">
      </a>
    </td>
    <td><a href="https://jojocode.com/"><strong>JOJO Code｜Codex++ 官方中转站</strong></a><br>感谢 JOJO Code 赞助了本项目！JOJO Code 是 Codex++ 官方中转站，面向日常开发和团队协作场景，提供稳定可用的 Codex API 接入体验，适合快速接入、长期使用和项目级工作流。</td>
  </tr>
  <tr>
    <td align="center">
      <a href="https://aigocode.com/invite/CodexPlusPlus">
        <img src="docs/images/sponsor-aigocode.png" alt="AIGoCode" height="80">
      </a>
    </td>
    <td><a href="https://aigocode.com/invite/CodexPlusPlus"><strong>AIGoCode</strong></a><br>感谢 AIGoCode 赞助了本项目！AIGoCode 是一个集成了 Claude Code、Codex 以及 Gemini 最新模型的一站式平台，为你提供稳定、高效且高性价比的AI编程服务。本站提供灵活的订阅计划，支持多风险，国内直连，无需魔法，极速响应。AIGoCode 为 CodexPlusPlus 的用户提供了特别福利，通过<a href="https://aigocode.com/invite/CodexPlusPlus">此链接注册</a>的用户首次充值可以获得额外10%奖励额度！</td>
  </tr>
  <tr>
    <td align="center">
      <a href="https://www.packyapi.com/">
        <img src="docs/images/sponsor-packycode.png" alt="PackyCode" height="80">
      </a>
    </td>
    <td><a href="https://www.packyapi.com/"><strong>PackyCode</strong></a><br>感谢 PackyCode 赞助了本项目！PackyCode 是一家稳定、高效的API中转服务商，提供 Claude Code、Codex、Gemini 等多种中转服务。PackyCode 为本软件的用户提供了特别优惠，使用此链接注册并在充值时填写"CodexPlusPlus"优惠码，首次充值可以享受9折优惠！</td>
  </tr>
  <tr>
    <td align="center">
      <a href="https://apikey.fun/register?aff=CODEX">
        <img src="docs/images/sponsor-apikey-fun.png" alt="APIKEY.FUN" height="80">
      </a>
    </td>
    <td><a href="https://apikey.fun/register?aff=CODEX"><strong>APIKEY.FUN</strong></a><br>感谢 APIKEY.FUN 赞助了本项目！APIKEY.FUN 是一家致力于提供开放、稳定、高性价比的全球主流大模型的 AI 中转站。平台支持 Claude、OpenAI、Gemini 等热门模型的 API 中转服务，价格低至官方原价的 7%。通过专属链接<a href="https://apikey.fun/register?aff=CODEX">注册 APIKEY</a>，可享受最高充值永久 95 折优惠。</td>
  </tr>
  <tr>
    <td align="center">
      <a href="https://runapi.co/register?aff=AWJq">
        <img src="docs/images/sponsor-runapi.png" alt="RunAPI" height="80">
      </a>
    </td>
    <td><a href="https://runapi.co/register?aff=AWJq"><strong>RunAPI</strong></a><br>感谢 RunAPI 赞助了本项目！RunAPI 是高效稳定的 API OpenRouter 平替平台，一个 API Key 即可访问 OpenAI、Claude、Gemini、DeepSeek、Grok 等 150+ 主流模型，低至 1 折，极其稳定，可以无缝兼容 Claude Code、OpenClaw 等工具。</td>
  </tr>
  <tr>
    <td align="center">
      <a href="https://www.0029.org/?promo=AFF11F">
        <img src="docs/images/sponsor-0029.svg" alt="0029 云桥" height="80">
      </a>
    </td>
    <td><a href="https://www.0029.org/?promo=AFF11F"><strong>0029云桥｜codex api中转站(gpt5.5 gpt-image-2)</strong></a><br>支持个人和企业接入。包月套餐/按量计费，Pro/Plus 号池，全站接口稳定可用，7×24 小时技术支持！</td>
  </tr>
  <tr>
    <td align="center">
      <a href="https://rawchat.cn">
        <img src="docs/images/sponsor-rawchat.svg" alt="RawChat" height="80">
      </a>
    </td>
    <td><a href="https://rawchat.cn"><strong>RawChat｜Codex 中转站</strong></a><br>老牌中转站，支持包月套餐。低倍率调用，高缓存命中，Pro/Plus 号池，全天专人维护。</td>
  </tr>
  <tr>
    <td align="center">
      <a href="https://coder.visioncoder.cn">
        <img src="https://coder.visioncoder.cn/logo.png" alt="VisionCoder" height="80">
      </a>
    </td>
    <td><a href="https://coder.visioncoder.cn"><strong>VisionCoder 开发平台</strong></a><br>感谢 VisionCoder 对本项目的支持。VisionCoder 开发平台是一个可靠高效的 API 中继服务提供商，提供 Claude Code、Codex、Gemini 等主流 AI 模型，帮助开发者和团队更轻松地集成 AI 功能，提升工作效率。VisionCoder 还为我们的用户提供 <a href="https://coder.visioncoder.cn">Token Plan</a> 限时活动：购买 1 个月，赠送 1 个月。</td>
  </tr>
  <tr>
    <td align="center">
      <a href="https://aihub2api.cloud/register?promo=CODEXPLUSPLUS">
        <img src="docs/images/sponsor-aihub2api.png" alt="AIHub2API" 