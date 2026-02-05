# OpenClaw 汉化发行版

[![Release](https://img.shields.io/github/v/release/1186258278/OpenClawChineseTranslation?label=稳定版)](https://github.com/1186258278/OpenClawChineseTranslation/releases)
[![npm](https://img.shields.io/npm/v/@qingchencloud/openclaw-zh?label=npm)](https://www.npmjs.com/package/@qingchencloud/openclaw-zh)
[![Nightly Build](https://github.com/1186258278/OpenClawChineseTranslation/actions/workflows/nightly.yml/badge.svg)](https://github.com/1186258278/OpenClawChineseTranslation/actions/workflows/nightly.yml)
[![Test Scripts](https://github.com/1186258278/OpenClawChineseTranslation/actions/workflows/test-scripts.yml/badge.svg)](https://github.com/1186258278/OpenClawChineseTranslation/actions/workflows/test-scripts.yml)
[![Platform](https://img.shields.io/badge/平台-Windows%20|%20macOS%20|%20Linux-blue)](https://github.com/1186258278/OpenClawChineseTranslation/releases)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

<table>
<tr>
<td>

### 🔄 实时同步官方更新

| 特性 | 说明 |
|:---:|:---|
| ⏰ **每小时同步** | CI/CD 自动从上游 [OpenClaw](https://github.com/openclaw/openclaw) 拉取最新代码 |
| 🚀 **自动构建发布** | 同步后立即构建 npm 包 + Docker 镜像，无需等待 |
| 📦 **双版本可选** | `nightly`（最新功能）/ `stable`（稳定版） |

> 💡 **延迟 < 1 小时**：官方发布新功能后，汉化版最快 1 小时内可用！

</td>
</tr>
</table>

<p align="center">
  <a href="https://openclaw.qt.cool/"><img src="https://img.shields.io/badge/🔥_官方网站-openclaw.qt.cool-dc2626?style=for-the-badge" alt="官方网站"></a>
  &nbsp;&nbsp;
  <a href="https://1186258278.github.io/OpenClawChineseTranslation/"><img src="https://img.shields.io/badge/📦_GitHub_Pages-备用入口-333?style=for-the-badge" alt="GitHub Pages"></a>
</p>

---

<a id="nav"></a>
## 📑 快速导航

| 🚀 快速上手 | 📦 部署方式 | 🔧 使用维护 | 🔌 插件扩展 | 💡 帮助 |
|:---:|:---:|:---:|:---:|:---:|
| [什么是 OpenClaw](#intro) | [一键安装](#install) | [快速开始](#start) | [插件市场](#plugins) | [常见问题](#faq) |
| [汉化效果预览](#preview) | [npm 安装](#npm) | [更新升级](#upgrade) | [安装插件](#plugin-install) | [参与贡献](#contribute) |
| [汉化内容](#content) | [Docker 部署](#docker) | [手动汉化安装](#manual) | [可用插件](#plugin-list) | [关于我们](#about) |

---

<a id="intro"></a>
## 🦞 什么是 OpenClaw？ <sub>[↑ 返回目录](#nav)</sub>

[OpenClaw](https://openclaw.ai/) 是由 Peter Steinberger ([@steipete](https://twitter.com/steipete)) 创建的**开源个人 AI 助手平台**，在 GitHub 上拥有超过 **100,000+ Stars**。

### 核心特性

| 特性 | 说明 |
|------|------|
| 🖥️ **运行在你的机器上** | Mac、Windows 或 Linux，数据始终在本地，隐私优先 |
| 💬 **任意聊天应用** | WhatsApp、Telegram、Discord、Slack、Signal、iMessage 都能用 |
| 🧠 **持久记忆** | 记住你的偏好、上下文，成为专属于你的 AI |
| 🌐 **浏览器控制** | 自动浏览网页、填写表单、提取数据 |
| ⚡ **完整系统访问** | 读写文件、运行脚本、执行命令 |
| 🔌 **技能插件系统** | 社区技能扩展，甚至可以自己编写新技能 |

### 它能做什么？

> *"清理你的收件箱、发送邮件、管理日历、办理航班值机……全部通过你常用的聊天应用完成。"*

正如用户评价：

- *"这是我第一次感觉自己活在未来。"* — @davemorin
- *"一切 Siri 本该成为的样子，而且远不止如此。"* — @crossiBuilds
- *"它正在运行我的公司。"* — @therno
- *"开源构建了一个比 Apple（3.6万亿美元公司）睡了多年的 Siri 更好的版本。"* — @Hesamation

---

<a id="preview"></a>
## 📸 汉化效果预览 <sub>[↑ 返回目录](#nav)</sub>

<p align="center">
  <img src="docs/image/5.png" alt="概览仪表板" width="100%">
  <br>
  <em>📊 概览仪表板 - 网关状态、实例监控、快捷操作一目了然</em>
</p>

<details>
<summary><b>🖼️ 查看更多截图</b></summary>

<p align="center">
  <img src="docs/image/1.png" alt="对话界面" width="100%">
  <br>
  <em>💬 对话界面 - 与 AI 助手实时交互</em>
</p>

<p align="center">
  <img src="docs/image/4.png" alt="渠道管理" width="100%">
  <br>
  <em>📱 渠道管理 - WhatsApp、Telegram、Discord 等全平台支持</em>
</p>

<p align="center">
  <img src="docs/image/2.png" alt="配置中心" width="100%">
  <br>
  <em>⚙️ 配置中心 - 30+ 配置项完整汉化</em>
</p>

<p align="center">
  <img src="docs/image/3.png" alt="节点配置" width="100%">
  <br>
  <em>🖥️ 节点配置 - 执行审批、安全策略管理</em>
</p>

<p align="center">
  <img src="docs/image/6.png" alt="技能插件" width="100%">
  <br>
  <em>🔌 技能插件 - 1Password、Apple Notes 等丰富扩展</em>
</p>

</details>

---

<a id="install"></a>
## ⚡ 一键安装汉化版 <sub>[↑ 返回目录](#nav)</sub>

### Windows (PowerShell)

```powershell
# 下载并执行安装脚本（注意：需要 UTF-8 编码）
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
Invoke-WebRequest -Uri "https://cdn.jsdelivr.net/gh/1186258278/OpenClawChineseTranslation@main/install.ps1" -OutFile "install.ps1" -Encoding UTF8; powershell -ExecutionPolicy Bypass -File ".\install.ps1"
```

> **如果遇到中文乱码问题**，请使用以下命令：
> ```powershell
> # 方法1：直接通过 npm 安装（推荐）
> npm install -g @qingchencloud/openclaw-zh@latest
> 
> # 方法2：使用 PowerShell 7+（支持 UTF-8）
> pwsh -Command "irm https://cdn.jsdelivr.net/gh/1186258278/OpenClawChineseTranslation@main/install.ps1 | iex"
> ```

### Linux / macOS

```bash
# 下载并执行安装脚本
curl -fsSL -o install.sh https://cdn.jsdelivr.net/gh/1186258278/OpenClawChineseTranslation@main/install.sh && bash install.sh
```

> 💡 使用 jsDelivr CDN 加速 | 🔒 [查看脚本源码](https://github.com/1186258278/OpenClawChineseTranslation/blob/main/install.sh)

---

<a id="npm"></a>
## 📦 其他安装方式 <sub>[↑ 返回目录](#nav)</sub>

### 版本选择

我们提供两个版本源，根据需求选择：

| 版本 | npm 标签 | 更新频率 | 适用场景 |
|------|----------|----------|----------|
| **稳定版** | `@latest` | 手动发布 | 生产环境，经过测试，推荐使用 |
| **最新版** | `@nightly` | 每小时自动 | 测试新功能，追踪上游最新代码 |

### 方式 1: npm / pnpm / yarn 安装

```bash
# npm 安装（推荐）
npm insta