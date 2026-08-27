<div align="center">

<p><a href="README.md">中文</a> | <a href="README.en.md">English</a></p>

<h1>Deepseek Harness EAC — 揽尽万象</h1>

<p><strong>EAC = Embracing All Creation（揽尽万象）</strong></p>

<p>
<a href="https://github.com/zouyuxuan122/Deepseek-Harness-EAC"><img src="https://img.shields.io/github/stars/zouyuxuan122/Deepseek-Harness-EAC?style=flat&label=%E2%AD%90&color=08C" alt="GitHub stars"></a>
<a href="https://github.com/zouyuxuan122/Deepseek-Harness-EAC/releases"><img src="https://img.shields.io/badge/Windows-10%2F11-4493F8?style=flat" alt="Windows"></a>
<a href="https://github.com/zouyuxuan122/Deepseek-Harness-EAC"><img src="https://img.shields.io/badge/Desktop-App-47848F?style=flat" alt="Desktop App"></a>
<a href="https://github.com/zouyuxuan122/Deepseek-Harness-EAC/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-2EA44F?style=flat" alt="MIT License"></a>
</p>

<p>把官方 <a href="https://github.com/deepseek-ai/deepseek-harness">deepseek-ai/deepseek-harness</a>（<code>@deepseek-ai/dsh</code>，一切皆插件的 agent harness）
封装为<strong>开箱即用的 Windows 桌面客户端</strong>，并在其上拥抱社区万象：皮肤、插件、工具、记忆——你所能想到的，一键皆可装。</p>

<p><a href="docs/screenshot-preview.jpg"><img src="docs/screenshot-preview.jpg" alt="Deepseek Harness EAC 界面预览"></a></p>

</div>

---

## 目录

- [为什么选择 EAC](#为什么选择-eac)
- [快速开始（安装）](#快速开始)
- [功能一览](#功能一览)
- [社区与支持](#社区与支持)
- [开发者文档](#开发者文档)
- [致谢](#致谢)
- [Star 趋势](#star-趋势)
- [许可证](#许可证)

---

## 为什么选择 EAC

| 维度 | 官方 DeepSeek Harness 默认体验 | Deepseek Harness EAC 增强 |
| --- | --- | --- |
| 安装与启动 | 需自行准备 Node.js，并通过 CLI 启动 | 内置 Node.js、npm CLI 和 dsh，提供安装版与便携版，双击即用 |
| 桌面体验 | 主要在终端或浏览器中使用 | 原生桌面窗口、系统托盘、快捷方式维护、进程清理和任务通知 |
| CLI 共存 | CLI 与 Web 通常使用同一插件环境 | 桌面端使用独立 `web-desktop` profile，与 CLI 共享会话和 API Key，插件互不干扰 |
| 插件可靠性 | 主要通过包管理器安装并手动排查问题 | 安装和启动前自动快照，异常时支持体检、修复、重试、回滚和事故报告 |
| 界面定制 | 默认使用官方界面 | 内置 10 款皮肤，支持字体、字号、颜色和移动端布局调整 |
| 项目工具 | 依赖外部编辑器和终端 | 内置文件树、行级 diff、一键还原、持久终端及 HTML/本地端口预览 |
| 上下文与人设 | 手动执行 `/compact`、编辑人设文件 | 自动压缩、人设卡管理和 `soul.md` 热重载 |
| 模型与 MCP | 主要通过配置文件或 CLI 管理 | 可视化配置视觉模型和 MCP，并支持从 Claude Code、Codex 导入配置 |
| 插件生态 | 通过 CLI 或包管理器安装插件 | 内置插件市场，可搜索并一键安装、卸载和管理插件 |
| 会话效率 | 以常规会话流程为主 | 支持临时对话、对话节点导航和第三方模型思考强度调整 |
| 消息接入 | 默认不包含 EAC 消息桥接 | 支持一键接入微信 ClawBot / OpenClaw |
| 更新维护 | 通过包管理器或手动方式更新 | dsh agent 与桌面客户端分别自动检查更新，失败时保留或回退原版本 |

> EAC 不修改官方 dsh 内核，完整保留插件架构和官方能力；默认共享
> `DSH_HOME` 中的会话与 API Key，同时隔离桌面端插件环境。

---

## 快速开始

### 系统要求

- Windows 10/11（x64）
- macOS 13+（Apple Silicon / arm64，桌面版）
- 无需预装 Node.js 或任何其他运行时

### Windows

> 正式版当前为 v4.4.1（Electron 壳）；下方 Lite 版为 Tauri（Rust）壳，体积更小、启动更快。安装包直接从 Release 下载。

| 文件 | 说明 | 大小 |
| --- | --- | --- |
| [安装版 Setup](https://github.com/zouyuxuan122/Deepseek-Harness-EAC/releases/download/v4.4.1/Deepseek-Harness-EAC-Setup-v4.4.1-x64.exe) | 安装到系统，创建快捷方式 | ~246 MB |
| [便携版 exe](https://github.com/zouyuxuan122/Deepseek-Harness-EAC/releases/download/v4.4.1/Deepseek-Harness-EAC-Portable-v4.4.1-x64.exe) | 免安装单文件，可放任意目录运行 | ~212 MB |
| [Lite 版 Setup](https://github.com/zouyuxuan122/Deepseek-Harness-EAC/releases/download/v4.5-lite/Deepseek.Harness.EAC.v4Lite_4.5.0_x64-setup.exe) | **Lite 精简版**（Tauri 壳，与上方正式版相互独立、可并存）：主程序为 `Deepseek Harness EAC v4Lite.exe`，数据目录 `~/.dsh-v4lite`，SHA256 校验文件随 Release 提供 | ~73 MB |

更多版本见 [Releases 页面](https://github.com/zouyuxuan122/Deepseek-Harness-EAC/releases)。

> 💡 **升级说明（老用户必读）**：
> - 直接下载上方最新安装包覆盖安装即可；
> - 插件、皮肤、会话与配置全部保留——数据在 `%APPDATA%\Deepseek Harness EAC\`
>   与 `~/.dsh`，升级过程不触碰。

### macOS（Apple Silicon / arm64）

> macOS 桌面版与 Windows/Linux 同源同版本，随 [v5.1.0 Release](https://github.com/zouyuxuan122/Deepseek-Harness-EAC/releases/tag/v5.1.0) 一同发布。

| 文件 | 说明 | 大小 |
| --- | --- | --- |
| [安装镜像 .dmg](https://github.com/zouyuxuan122/Deepseek-Harness-EAC/releases/download/v5.1.0/Deepseek.Harness.EAC_5.1.0_macos-arm64.dmg) | 双击挂载后拖入 Applications | ~136 MB |
| [应用包 .app.zip](https://github.com/zouyuxuan122/Deepseek-Harness-EAC/releases/download/v5.1.0/Deepseek.Harness.EAC_5.1.0_macos-arm64.app.zip) | 解压后直接运行 | ~157 MB |
| [校验和 SHA256SUMS-macos.txt](https://github.com/zouyuxuan122/Deepseek-Harness-EAC/releases/download/v5.1.0/SHA256SUMS-macos.txt) | macOS 资产 SHA256 | — |

- 桌面配置目录：`~/Library/Application Support/deepseek-harness-eac/`；dsh 数据仍在 `~/.dsh`（与 CLI 共享，会话互通）。
- 未签名、未公证（个人自用定位）：首次打开若被 Gatekeeper 拦截，右键 →「打开」。
- 客户端自更新在 macOS v1 暂不提供（上游 Release 暂无 macOS 资产）；dsh agent（内核）更新完整保留。

### Linux（x64）

> Linux 桌面端由 CI（Ubuntu 22.04）持续构建与验证，以独立版本线发布（最近维护版 v4.4.0）。Windows/macOS 走统一版本线（当前 v5.1.0），Linux 并入统一版本线待发布管线就绪后补发。

| 文件 | 说明 |
| --- | --- |
| [.deb（Debian/Ubuntu）](https://github.com/zouyuxuan122/Deepseek-Harness-EAC/releases/download/v4.4.0-linux/Deepseek-Harness-EAC-4.4.0-amd64.deb) | 安装后可从应用菜单启动 |
| [AppImage](https://github.com/zouyuxuan122/Deepseek-Harness-EAC/releases/download/v4.4.0-linux/Deepseek-Harness-EAC-4.4.0-x86_64.AppImage) | 免安装：`chmod +x` 后直接运行 |
| [.rpm（Fedora/openSUSE）](https://github.com/zouyuxuan122/Deepseek-Harness-EAC/releases/download/v4.4.0-linux/Deepseek-Harness-EAC-4.4.0.x86_64.rpm) | — |
| [.pacman（Ar