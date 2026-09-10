<div align="center">

<p><a href="README.md">中文</a> | <a href="README.en.md">English</a></p>

<h1>DSH-Desktop-EAC — 揽尽万象</h1>

<p><strong>EAC = Embracing All Creation（揽尽万象）</strong></p>

<p>
<a href="https://github.com/zouyuxuan122/Deepseek-Harness-EAC"><img src="https://img.shields.io/github/stars/zouyuxuan122/Deepseek-Harness-EAC?style=flat&label=%E2%AD%90&color=08C" alt="GitHub stars"></a>
<a href="https://github.com/zouyuxuan122/Deepseek-Harness-EAC/releases"><img src="https://img.shields.io/badge/Windows-10%2F11-4493F8?style=flat" alt="Windows"></a>
<a href="https://github.com/zouyuxuan122/Deepseek-Harness-EAC"><img src="https://img.shields.io/badge/Desktop-App-47848F?style=flat" alt="Desktop App"></a>
<a href="https://github.com/zouyuxuan122/Deepseek-Harness-EAC/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-2EA44F?style=flat" alt="MIT License"></a>
</p>

<p><strong>🚀 全新产品：<a href="https://github.com/zouyuxuan122/Deepseek-Harness-EAC-IDE">Deepseek Harness EAC IDE</a> —— 内置 EAC 的独立 IDE（VS Code 底座 · 鲸鱼品牌 · 开箱即用），<a href="https://github.com/zouyuxuan122/Deepseek-Harness-EAC-IDE/releases">前往下载 →</a></strong></p>

<p>把官方 <a href="https://github.com/deepseek-ai/deepseek-harness">deepseek-ai/deepseek-harness</a>（<code>@deepseek-ai/dsh</code>，一切皆插件的 agent harness）
封装为<strong>开箱即用的 Windows 桌面客户端</strong>，并在其上拥抱社区万象：皮肤、插件、工具、记忆——你所能想到的，一键皆可装。</p>

<p><a href="docs/screenshot-preview.jpg"><img src="docs/screenshot-preview.jpg" alt="DSH-Desktop-EAC 界面预览"></a></p>

</div>

> ### 📦 v5.4 起：唯一的桌面发行版，安装时选「完整版 / 精简版」
>
> 同一个安装包、同一套 5.x 内核：**完整版**带全部内置插件；**精简版**只默认停用外围插件（桌宠 / 手机桥 / 多智能体等），设置里可随时一键启用，无需重装。
> 原 **Lite（Electron 精简版）退役**、**AIO 整合版收编为精简版形态**、**EAC-IDE 进入维护模式**——数据统一 `~/.dsh`。迁移说明见 [docs/SINGLE-EDITION-MIGRATION.md](dsh-desktop/docs/SINGLE-EDITION-MIGRATION.md)。

---

> ### 🚀 官方配套启动器：DSH EAC Launcher
>
> **多实例隔离 · 本地实例导入 · 版本一键升级/回退 · 插件安全体系**（崩溃守卫 crash-guard · 插件快照回滚 · 隔离区 · 健康体检）
>
> 为本项目的多实例与插件玩法而生：每个实例独立程序目录与 `DSH_HOME`，从上游 Release 一键安装任意版本，装插件崩了也能一键回滚。
>
> 👉 **[zouyuxuan122/DSH-EAC-Launcher](https://github.com/zouyuxuan122/DSH-EAC-Launcher)** ｜ [⬇ 下载最新版 v1.1.0](https://github.com/zouyuxuan122/DSH-EAC-Launcher/releases/latest)

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

| 维度 | 官方 DeepSeek Harness 默认体验 | DSH-Desktop-EAC 增强 |
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

> 当前发布线为 5.x（Tauri/Rust 壳）。5.2 起桌面版统一为 Tauri 壳；更早的 v4.4.1 Electron 版已退役（仅 Release 存档）。安装包直接从 Release 下载。

| 文件 | 说明 | 大小 |
| --- | --- | --- |
| [安装版 Setup（v5.3.6）](https://github.com/zouyuxuan122/DSH-Desktop-EAC/releases/download/v5.3.6/Deepseek-Harness-EAC-5.3.6-Setup-x64.exe) | Tauri 壳安装版（NSIS），安装到系统并创建快捷方式；SHA256 校验文件随 [Release](https://github.com/zouyuxuan122/DSH-Desktop-EAC/releases/tag/v5.3.6) 提供 | ~191 MB |
| [便携版（v5.3.6）](https://github.com/zouyuxuan122/DSH-Desktop-EAC/releases/download/v5.3.6/Deepseek-Harness-EAC-5.3.6-portable.zip) | 免安装压缩包，解压到任意目录即可运行；数据跟随程序目录，可直接迁移 | ~228 MB |

更多版本见 [Releases 页面](https://github.com/zouyuxuan122/DSH-Desktop-EAC/releases)。

### AIO 版（Windows x64 · All-in-One）

> **DSHEAC AIO** 是独立于 5.x 主线的 **All-in-One 精致个人终端**：一个安装包备齐 dsh 内核、插件市场与完整桌面体验，开箱即用；与正式版相互隔离（独立 app data 与 `dsh-home`，默认不读取 5.x / v4Lite / 旧 EAC 或 CLI 数据），可并存安装。当前版本 **AIO v1.2.0**（源码分支 `aio-v1`，随 [aio-v1.2.0 Release](https://github.com/zouyuxuan122/DSH-Desktop-EAC/releases/tag/aio-v1.2.0) 一同发布）。

| 文件 | 说明 | 大小 |
| --- | --- | --- |
| [AIO 安装版（v1.2.0）](https://github.com/zouyuxuan122/DSH-Desktop-EAC/releases/download/aio-v1.2.0/DSHEAC-AIO-v1.2.0-Setup-x64.exe) | NSIS 安装版，安装到系统并创建快捷方式；EXE 为 `DSHEAC AIO.exe`，与正式版更新器互相隔离 | ~313 MB |
| [AIO 便携版（v1.2.0）](https://github.com/zouyuxuan122/DSH-Desktop-EAC/releases/download/aio-v1.2.0/DSHEAC-AIO-v1.2.0-Portable-x64.zip) | 免安装解压即用，数据写入 EXE 同级 `.dsh-aio-data`，可直接迁移 | ~147 MB |
| [校验清单 SHA256SUMS-AIO-v1.2.0.txt](https://github.com/zouyuxuan122/DSH-Desktop-EAC/releases/download/aio-v1.2.0/SHA256SUMS-AIO-v1.2.0.txt) | AIO 资产 SH