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

[OpenClaw](https://openclaw.ai/) 是 GitHub 195,000+ Stars 的**开源个人 AI 助手平台**。它运行在你的电脑上，通过 WhatsApp、Telegram、Discord 等聊天应用与你的 AI 助手交互，帮你处理邮件、日历、文件等日常事务。

**本项目 = OpenClaw + 全中文界面**，CLI 命令行和 Dashboard 网页控制台均已深度汉化。

---

## 🏷️ 合作伙伴

**胜算云** - 国内 AI API 聚合平台，新用户注册送额度，充值尊享 7 折优惠！

| 阶梯 | 春节消耗 | 奖励 |
|------|---------|------|
| 尝鲜礼 | ≥50元 | 5元 模力券 |
| 极客礼 | ≥100元 | 10元 模力券 + Kimi K2.5 七折卡(7天) |
| 大神礼 | ≥500元 | 50元 模力券 + Kimi K2.5 七折卡(7天) |

[查看活动 →](https://www.shengsuanyun.com/activity/4184b48a6be4443cbe13e86e091e43b4?from=CH_4BVI0BM2) · [注册账号 →](https://www.shengsuanyun.com/?from=CH_4BVI0BM2)

---

## 4 步上手

> **前提条件**：需要 **Node.js >= 22**（[下载 Node.js](https://nodejs.org/)）
>
> 检查版本：`node -v`

### 第 1 步：安装

```bash
npm install -g @qingchencloud/openclaw-zh@latest
```

### 第 2 步：初始化（推荐守护进程模式）

```bash
openclaw onboard --install-daemon
```

初始化向导会引导你完成：选择 AI 模型 → 配置 API 密钥 → 设置聊天通道

### 第 3 步：启动网关

```bash
openclaw gateway
```

### 第 4 步：打开控制台

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

# 网关管理
openclaw gateway run        # 前台运行（挂终端，用于调试）
openclaw gateway start      # 后台守护进程（不挂终端，推荐！）
openclaw gateway stop       # 停止网关
openclaw gateway restart    # 重启网关
openclaw gateway status     # 查看网关状态
openclaw gateway install    # 安装为系统服务（开机自启）

# 常用操作
openclaw update             # 检查并更新 CLI
openclaw doctor             # 诊断问题（自动修复）
```

> **Windows 用户注意**：如果 `gateway install` 失败（提示 schtasks 不可用），可使用 `gateway start` 启动后台进程，或使用 Docker 部署方案。

---

## 网关重启

```bash
# 方式 1：使用 gateway 子命令（推荐）
openclaw gateway restart

# 方式 2：先停止再启动
openclaw gateway stop
openclaw gateway start

# 方式 3：守护进程模式（后台运行，不挂终端）
openclaw daemon start       # 启动后台守护
openclaw daemon stop        # 停止守护
openclaw daemon restart    # 重启守护
openclaw daemon status     # 查看状态

# Docker 容器重启
docker restart openclaw
```

---

## 卸载教程

### CLI 卸载

```bash
# 卸载汉化版
npm uninstall -g @qingchencloud/openclaw-zh

# 如果之前安装过原版，也一并卸载
npm uninstall -g openclaw
```

### 数据清理（可选）

```bash
# 删除配置和缓存（不可恢复！）
rm -rf ~/.openclaw

# Docker 清理
docker rm -f openclaw                # 删除容器
docker volume rm openclaw-data       # 删除数据卷
```

### 守护进程卸载

```bash
# macOS
launchctl unload ~/Library/LaunchAgents/com.openclaw.plist
rm ~/Library/LaunchAgents/com.openclaw.plist

# Linux (systemd)
sudo systemctl stop openclaw
sudo systemctl disable openclaw
sudo rm /etc/systemd/system/openclaw.service
sudo systemctl daemon-reload
```

---

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
| **