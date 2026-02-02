<p align="center">
  <img src="img/antigravity_logo.png" alt="Antigravity Logo" width="120"/>
</p>

<h1 align="center">Antigravity-Proxy</h1>

<p align="center">
  <b>🚀 专为 Antigravity 编辑器打造：在中国也能无需 TUN 模式稳定走代理</b>
</p>

<p align="center">
  <a href="https://github.com/yuaotian/antigravity-proxy/actions"><img src="https://github.com/yuaotian/antigravity-proxy/actions/workflows/build.yml/badge.svg" alt="Build Status"/></a>
  <a href="LICENSE.txt"><img src="https://img.shields.io/badge/license-BSD--2--Clause-blue.svg" alt="License"/></a>
  <img src="https://img.shields.io/badge/platform-Windows%20x86%20%7C%20x64-lightgrey.svg" alt="Platform"/>
  <img src="https://img.shields.io/badge/C%2B%2B-17-00599C.svg" alt="C++17"/>
  <img src="https://img.shields.io/badge/hook-MinHook-orange.svg" alt="MinHook"/>
</p>

<p align="center">
  <a href="README_EN.md">🇬🇧 English Version</a>
</p>

---

## 📖 目录 / Table of Contents

- [📖 项目介绍 / Introduction](#-项目介绍--introduction)
- [⚡ Antigravity 快速开始 / Quick Start](#-antigravity-快速开始--quick-start)
- [🔧 故障排查自查手册 / Troubleshooting Guide](#-故障排查自查手册--troubleshooting-guide)
- [✨ 功能特性 / Features](#-功能特性--features)
- [🔧 工作原理 / How It Works](#-工作原理--how-it-works)
- [🛠️ 编译构建 / Build](#️-编译构建--build)
- [📝 使用方法 / Usage](#-使用方法--usage)
- [🐧 WSL 环境使用指南 / WSL Guide](#-wsl-环境使用指南--wsl-guide)
- [🚀 进阶玩法 / Advanced Usage](#-进阶玩法--advanced-usage)
- [📄 许可证 / License](#-许可证--license)
- [👤 关于作者 / Author](#-关于作者--author)

---

## 📖 项目介绍 / Introduction

**Antigravity-Proxy** 是专门为 **Antigravity 编辑器**量身定制的 Windows 代理注入组件（DLL）。

它的目标很简单：让中国用户使用 Antigravity 时，**不用开 Clash TUN 模式**，也能把网络流量稳定交给你的 SOCKS5/HTTP 代理。

> 项目名 **Antigravity-Proxy** = Antigravity + Proxy：只把 Antigravity 相关进程的流量“拽”进代理里（别担心，不会全局接管）。

### 🎯 解决的痛点 / Problem Solved

你是否遇到过这些情况？

- 🔴 使用 Antigravity 时**不走系统代理**，只能被迫开启 Clash TUN 模式
- 🔴 开启 TUN 模式后**全局流量都被代理**，影响本地开发
- 🔴 TUN 模式需要**管理员权限**，某些环境不允许

**Antigravity-Proxy 就是来专治这个的。** 它可以：

- ✅ **仅代理指定程序**（默认面向 Antigravity 相关进程），不影响其他流量
- ✅ **无需 TUN 模式**，避免全局接管
- ✅ **透明代理**，目标程序完全无感知

### 🌟 核心价值 / Core Value

| 传统方案 | Antigravity-Proxy |
|---------|-------------------|
| 需要 TUN 模式 | 无需 TUN |
| 全局代理 | 精准代理指定进程 |
| 需要管理员权限 | 普通用户即可 |
| 配置复杂 | 放入 DLL 即用 |

---


## ⚠️ 环境要求 / Prerequisites

> 在使用本工具前，请确保系统已安装必要的运行库，否则可能无法正常启动目标程序。

### 常见问题：0xc0000142 错误

如果启动程序时遇到 **错误代码 0xc0000142**（如下图所示），通常是由于系统缺少 Windows 运行库导致的。

<p align="center">
  <img src="img/error/win_error_0xc0000142.png" alt="0xc0000142 错误截图" width="400"/>
</p>

### 解决方案

请安装 **微软常用运行库合集**，该工具已包含在本仓库中：

📦 **下载路径**: [`microsoft\微软常用运行库合集-2025.exe`](microsoft/微软常用运行库合集-2025.exe)

**安装步骤：**
1. 进入本仓库的 `microsoft` 目录
2. 运行 `微软常用运行库合集-2025.exe`
3. 按照安装向导完成安装
4. 重新启动目标程序

---

## ⚡ Antigravity 快速开始 / Quick Start

> 只想让 Antigravity 立刻能用？看这一节就够了。

### Step 1: 准备代理 / Prepare a Proxy

启动你的代理软件（例如 Clash/Mihomo），确保本机有可用的 SOCKS5 或 HTTP 代理端口（如 `127.0.0.1:7890`）。

<details>
<summary><b>📋 常用代理软件端口速查表（点击展开）</b></summary>

#### 各代理软件默认端口

| 代理软件 | SOCKS5 端口 | HTTP 端口 | 混合端口 | 备注 |
|----------|-------------|-----------|----------|------|
| **Clash / Clash Verge** | 7891 | 7890 | 7890 | 混合端口同时支持 SOCKS5 和 HTTP |
| **Clash for Windows** | 7891 | 7890 | 7890 | 设置 → Ports 可查看/修改 |
| **Mihomo (Clash Meta)** | 7891 | 7890 | 7890 | 同 Clash 配置格式 |
| **V2RayN** | 10808 | 10809 | - | 设置 → 参数设置 → Core 基础设置 |
| **V2RayA** | 20170 | 20171 | - | 后台管理页面可修改 |
| **Shadowsocks** | 1080 | - | - | 仅 SOCKS5，无 HTTP |
| **ShadowsocksR** | 1080 | - | - | 仅 SOCKS5，无 HTTP |
| **Surge (Mac/iOS)** | 6153 | 6152 | - | 增强模式下端口可能不同 |
| **Qv2ray** | 1089 | 8889 | - | 首选项 → 入站设置 |
| **sing-box** | 自定义 | 自定义 | 自定义 | 需在配置文件中手动指定 |
| **NekoBox** | 2080 | 2081 | - | 设置 → 入站 |
| **Clash Meta for Android** | 7891 | 7890 | 7890 | 同 Clash 规则 |

> 💡 **推荐使用 SOCKS5 协议**：本工具对 SOCKS5 的支持更完善，建议优先使用。

#### 如何确认代理端口是否开启？

**方法 1：查看代理软件界面**
- 大多数代理软件会在主界面或设置中显示当前监听端口

**方法 2：命令行测试**
```powershell
# 测试 SOCKS5 端口 (默认 7891)
Test-NetConnection -ComputerName 127.0.0.1 -Port 7891

# 测试 HTTP 端口 (默认 7890)
Test-NetConnection -ComputerName 127.0.0.1 -Port 7890
```

**方法 3：curl 测试（需安装 curl）**
```bash
# 通过 SOCKS5 代理访问
curl -x socks5://127.0.0.1:7891 https://www.google.com -I

# 通过 HTTP 代理访问
curl -x http://127.0.0.1:7890 https://www.google.com -I
```

#### 常见端口问题及解决

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| 端口被占用 | 其他程序使用了该端口 | `netstat -ano | findstr :7890` 查找占用进程 |
| 连接被拒绝 | 代理软件未启动或端口错误 | 确认代理软件已启动，检查端口配置 |
| 代理无响应 | 防火墙阻止 | 检查 Windows 防火墙设置 |

</details>

### Step 2: 准备文件 / Get the Files

准备两份文件：
- `version.dll`
- `config.json`

（可以从 Release 下载，或自行编译生成。）

### Step 3: 部署到 Antigravity / Deploy to Antigravity

把 `version.dll` 和 `config.json` 复制到 **Antigravity 主程序目录**（与 `Antigravity.exe` 同级）。然后启动 Antigravity，搞定。

#### Windows 常见目录 + 快速跳转

一般情况下 Antigravity 会装在：

例如：`C:\Users\<用户名>\AppData\Local\Programs\Antigravity`

如果你找不到这个目录：在桌面/开始菜单找到 Antigravity 图标，**右键 → 打开文件所在的位置**，跳出来的那个目录就是它的主程序目录。

想从命令行一键跳过去（少点鼠标，多点快乐）：

```powershell
cd "$env:LOCALAPPDATA\Programs\Antigravity"
```

```bat
cd /d "%LOCALAPPDATA%\Programs\Anti