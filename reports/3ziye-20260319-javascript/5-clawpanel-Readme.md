<p align="center">
  <img src="public/images/logo-brand.png" width="360" alt="ClawPanel">
</p>

<p align="center">
  内置 AI 助手的 OpenClaw 管理面板 — 一键安装、配置、诊断、修复
</p>

<p align="center">
  <strong>🇨🇳 中文</strong> | <a href="README.en.md">🇺🇸 English</a>
</p>

<p align="center">
  <a href="https://github.com/qingchencloud/clawpanel/releases/latest">
    <img src="https://img.shields.io/github/v/release/qingchencloud/clawpanel?style=flat-square&color=6366f1" alt="Release">
  </a>
  <a href="https://github.com/qingchencloud/clawpanel/releases/latest">
    <img src="https://img.shields.io/github/downloads/qingchencloud/clawpanel/total?style=flat-square&color=8b5cf6" alt="Downloads">
  </a>
  <a href="https://github.com/qingchencloud/clawpanel/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/license-AGPL--3.0-blue.svg?style=flat-square" alt="License">
  </a>
  <a href="https://github.com/qingchencloud/clawpanel/actions/workflows/ci.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/qingchencloud/clawpanel/ci.yml?style=flat-square&label=CI" alt="CI">
  </a>
</p>

---

<p align="center">
  <img src="docs/feature-showcase.gif" width="800" alt="ClawPanel 功能全景">
</p>

<p align="center">
  <a href="https://claw.qt.cool/#video">
    <img src="https://img.shields.io/badge/%E2%96%B6%20%E6%BC%94%E7%A4%BA%E8%A7%86%E9%A2%91-50%E7%A7%92%E5%BF%AB%E9%80%9F%E4%BA%86%E8%A7%A3-6366f1?style=for-the-badge" alt="演示视频">
  </a>
</p>

ClawPanel 是 [OpenClaw](https://github.com/1186258278/OpenClawChineseTranslation) AI Agent 框架的可视化管理面板。**内置智能 AI 助手**，帮你一键安装 OpenClaw、自动诊断配置、排查问题、修复错误。8 大工具 + 4 种模式 + 交互式问答，从新手到老手都能轻松管理。

> 🌐 **官网**: [claw.qt.cool](https://claw.qt.cool/)  |  📦 **下载**: [GitHub Releases](https://github.com/qingchencloud/clawpanel/releases/latest)

### ⚡ OpenClaw 独立安装包（零依赖，无需 Node.js/npm）

不想折腾 Node.js 环境？直接下载 [OpenClaw 独立安装包](https://github.com/qingchencloud/openclaw-standalone/releases/latest)，**内置运行时，解压即用**：

- **Windows**: 下载 `.exe` 安装向导，双击即装
- **macOS / Linux / 树莓派**: `curl -fsSL https://dl.qrj.ai/openclaw/install.sh | bash`
- **全平台**: [GitHub Releases](https://github.com/qingchencloud/openclaw-standalone/releases/latest)

> ClawPanel 安装 OpenClaw 时会**自动优先使用独立安装包**，无需手动操作。此方案仅供不使用 ClawPanel 的用户独立安装。

### 🔥 开发板 / 嵌入式设备支持

ClawPanel 提供**纯 Web 版部署模式**（零 GUI 依赖），天然兼容 ARM64 开发板和嵌入式设备：

- **Orange Pi / 树莓派 / RK3588** 等 ARM64 板子 — `npm run serve` 即可运行
- **Docker ARM64 镜像** — `docker run ghcr.io/qingchencloud/openclaw:latest` 开箱即用
- **Armbian / Debian / Ubuntu Server** — 一键部署脚本自动检测架构
- 无需 Rust / Tauri / 图形界面，**只要有 Node.js 18+ 就能跑**

> 📖 详见 [Armbian 部署指南](docs/armbian-deploy.md) | [Web 版开发说明](#web-开发版无需-rusttauri)

## 社区交流

一群对 AI Agent 充满热情的开发者和玩家，欢迎加入交流。

<table align="center">
  <tr>
    <td align="center">
      <a href="https://qt.cool/c/OpenClaw"><img src="docs/qr-qq.png" width="140" alt="QQ 群二维码"></a><br>
      <a href="https://qt.cool/c/OpenClaw"><strong>QQ 群</strong></a>
    </td>
    <td align="center">
      <a href="https://qt.cool/c/OpenClawWx"><img src="docs/qr-wechat.png" width="140" alt="微信群二维码"></a><br>
      <a href="https://qt.cool/c/OpenClawWx"><strong>微信群</strong></a>
    </td>
    <td align="center">
      <a href="https://qt.cool/c/OpenClawDY"><img src="docs/qr-dy.png" width="140" alt="抖音群二维码"></a><br>
      <a href="https://qt.cool/c/OpenClawDY"><strong>抖音群</strong></a>
    </td>
    <td align="center">
      <a href="https://qt.cool/c/feishu"><img src="https://qt.cool/c/feishu/qr.png" width="140" alt="飞书群二维码"></a><br>
      <a href="https://qt.cool/c/feishu"><strong>飞书群</strong></a>
    </td>
  </tr>
</table>

<p align="center">
  <a href="https://discord.gg/U9AttmsNHh"><strong>Discord</strong></a>
  &nbsp;·&nbsp;
  <a href="https://yb.tencent.com/gp/i/LsvIw7mdR7Lb"><strong>元宝派</strong></a>
  &nbsp;·&nbsp;
  <a href="https://github.com/qingchencloud/clawpanel/discussions"><strong>Discussions</strong></a>
  &nbsp;·&nbsp;
  <a href="https://github.com/qingchencloud/clawpanel/issues/new"><strong>反馈 Issue</strong></a>
  &nbsp;·&nbsp;
  <a href="https://qt.cool/c/feishu"><strong>飞书群</strong></a>
</p>

## 下载安装

前往 [Releases](https://github.com/qingchencloud/clawpanel/releases/latest) 页面下载最新版本，根据你的系统选择对应安装包：

### macOS

| 芯片 | 安装包 | 说明 |
|------|--------|------|
| Apple Silicon (M1/M2/M3/M4) | `ClawPanel_x.x.x_aarch64.dmg` | 2020 年末及之后的 Mac |
| Intel | `ClawPanel_x.x.x_x64.dmg` | 2020 年及之前的 Mac |

> 不确定芯片类型？点击左上角  → 关于本机，查看「芯片」一栏。

安装方式：打开 `.dmg` 文件，**先将 ClawPanel 拖入「应用程序」文件夹**，再双击打开。

> **⚠️ 首次打开提示"已损坏"或"无法验证开发者"？** 由于应用未签名，macOS 会拦截。请在终端执行以下命令解除限制：
>
> ```bash
> sudo xattr -rd com.apple.quarantine /Applications/ClawPanel.app
> ```
>
> 或者前往「系统设置 → 隐私与安全性」，找到 ClawPanel 点击「仍要打开」。
>
> 提示 `No such file`？说明没有拖入应用程序文件夹。请先拖入，或改用：
> ```bash
> sudo xattr -rd com.apple.quarantine ~/Downloads/ClawPanel.app
> ```

### Windows

| 格式 | 安装包 | 说明 |
|------|--------|------|
| EXE 安装器 | `ClawPanel_x.x.x_x64-setup.exe` | 推荐，双击安装 |
| MSI 安装器 | `ClawPanel_x.x.x_x64_en-US.msi` | 企业部署 / 静默安装 |

### Linux

