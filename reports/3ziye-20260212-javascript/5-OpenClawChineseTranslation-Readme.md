# OpenClaw 汉化发行版

[![Release](https://img.shields.io/github/v/release/1186258278/OpenClawChineseTranslation?label=稳定版)](https://github.com/1186258278/OpenClawChineseTranslation/releases)
[![npm](https://img.shields.io/npm/v/@qingchencloud/openclaw-zh?label=npm)](https://www.npmjs.com/package/@qingchencloud/openclaw-zh)
[![Nightly Build](https://github.com/1186258278/OpenClawChineseTranslation/actions/workflows/nightly.yml/badge.svg)](https://github.com/1186258278/OpenClawChineseTranslation/actions/workflows/nightly.yml)
[![Platform](https://img.shields.io/badge/平台-Windows%20|%20macOS%20|%20Linux-blue)](https://github.com/1186258278/OpenClawChineseTranslation/releases)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

> **每小时自动同步** [OpenClaw](https://github.com/openclaw/openclaw) 官方更新，汉化版延迟 < 1 小时！

<p align="center">
  <a href="https://openclaw.qt.cool/"><img src="https://img.shields.io/badge/🔥_汉化官网-openclaw.qt.cool-dc2626?style=for-the-badge" alt="汉化官网"></a>
</p>

---

## 什么是 OpenClaw？

[OpenClaw](https://openclaw.ai/) 是 GitHub 100,000+ Stars 的**开源个人 AI 助手平台**。它运行在你的电脑上，通过 WhatsApp、Telegram、Discord 等聊天应用与你的 AI 助手交互，帮你处理邮件、日历、文件等日常事务。

**本项目 = OpenClaw + 全中文界面**，CLI 命令行和 Dashboard 网页控制台均已深度汉化。

---

## 3 步上手

> **前提条件**：需要 **Node.js >= 22**（[下载 Node.js](https://nodejs.org/)）
>
> 检查版本：`node -v`

### 第 1 步：安装

```bash
npm install -g @qingchencloud/openclaw-zh@latest
```

### 第 2 步：初始化

```bash
openclaw onboard
```

初始化向导会引导你完成：选择 AI 模型 → 配置 API 密钥 → 设置聊天通道

### 第 3 步：打开控制台

```bash
openclaw dashboard
```

浏览器会自动打开全中文的 Dashboard 控制台。完成！

> 想了解每一步的详细说明？查看 **[详细安装指南](docs/INSTALL_GUIDE.md)**（包含 Node.js 安装、模型配置、守护进程、内网访问等）

---

## 汉化效果预览

<p align="center">
  <img src="docs/image/5.png" alt="概览仪表板" width="100%">
  <br>
  <em>概览仪表板 - 网关状态、实例监控、快捷操作一目了然</em>
</p>

<details>
<summary><b>查看更多截图</b></summary>

<p align="center">
  <img src="docs/image/1.png" alt="对话界面" width="100%">
  <br>
  <em>对话界面 - 与 AI 助手实时交互</em>
</p>

<p align="center">
  <img src="docs/image/4.png" alt="渠道管理" width="100%">
  <br>
  <em>渠道管理 - WhatsApp、Telegram、Discord 等全平台支持</em>
</p>

<p align="center">
  <img src="docs/image/2.png" alt="配置中心" width="100%">
  <br>
  <em>配置中心 - 完整汉化</em>
</p>

<p align="center">
  <img src="docs/image/3.png" alt="节点配置" width="100%">
  <br>
  <em>节点配置 - 执行审批、安全策略管理</em>
</p>

<p align="center">
  <img src="docs/image/6.png" alt="技能插件" width="100%">
  <br>
  <em>技能插件 - 1Password、Apple Notes 等丰富扩展</em>
</p>

</details>

---

## 常用命令

```bash
openclaw                    # 启动 OpenClaw
openclaw onboard            # 初始化向导
openclaw dashboard          # 打开网页控制台
openclaw config             # 查看/修改配置
openclaw skills             # 管理技能
openclaw --help             # 查看帮助
```

---

## 更新升级

```bash
npm update -g @qingchencloud/openclaw-zh
```

> 查看当前版本：`openclaw --version`

| 版本 | 安装命令 | 说明 |
|------|----------|------|
| **稳定版** | `npm install -g @qingchencloud/openclaw-zh@latest` | 经过测试，推荐使用 |
| **最新版** | `npm install -g @qingchencloud/openclaw-zh@nightly` | 每小时同步上游，体验新功能 |

---

## Docker 部署（国内推荐）

> **国内用户强烈推荐使用 Docker Hub 镜像**，拉取速度快，无需翻墙！

| 镜像源 | 拉取命令 | 适用 |
|--------|----------|------|
| **Docker Hub（国内推荐）** | `docker pull 1186258278/openclaw-zh:latest` | 国内用户 |
| GitHub Container Registry | `docker pull ghcr.io/1186258278/openclaw-zh:latest` | 海外用户 |

### 一键部署（最简单）

```bash
# Linux/macOS — 加 --china 自动使用国内镜像
curl -fsSL https://cdn.jsdelivr.net/gh/1186258278/OpenClawChineseTranslation@main/docker-deploy.sh | bash -s -- --china
```

```powershell
# Windows PowerShell — 加 -China 自动使用国内镜像
irm https://cdn.jsdelivr.net/gh/1186258278/OpenClawChineseTranslation@main/docker-deploy.ps1 | iex
# 或: .\docker-deploy.ps1 -China
```

### 手动 Docker 部署

```bash
# 国内用户使用 Docker Hub 镜像
IMAGE=1186258278/openclaw-zh:latest
# 海外用户使用: IMAGE=ghcr.io/1186258278/openclaw-zh:latest

# 1. 初始化
docker run --rm -v openclaw-data:/root/.openclaw $IMAGE openclaw setup
docker run --rm -v openclaw-data:/root/.openclaw $IMAGE openclaw config set gateway.mode local

# 2. 启动
docker run -d --name openclaw -p 18789:18789 \
  -v openclaw-data:/root/.openclaw --restart unless-stopped \
  $IMAGE openclaw gateway run
```

访问：`http://localhost:18789`

> 完整指南（远程部署、Nginx 反代、Docker Compose、内网访问等）请查看 **[Docker 部署指南](docs/DOCKER_GUIDE.md)**

---

## 其他安装方式

<details>
<summary><b>一键安装脚本（npm）</b></summary>

**Linux / macOS：**
```bash
curl -fsSL -o install.sh https://cdn.jsdelivr.net/gh/1186258278/OpenClawChineseTranslation@main/install.sh && bash install.sh
```

**Windows PowerShell：**
```powershell
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
Invoke-WebRequest -Uri "https://cdn.jsdelivr.net/gh/1186258278/OpenClawChineseTranslation@main/install.ps1" -OutFile "install.ps1" -Encoding UTF8; powershell -ExecutionPolicy Bypass -File ".\install.ps1"
```

> 如遇中文乱码，直接用 npm 安装：`npm install -g @qingchencloud/openclaw-zh@latest`

</details>

<details>
<summary><b>npm 国内加速安装</b></summary>

```bash
# 使用 npmmirror 镜像源（国内推荐）
npm install -g @qingchencl