<p align="center">
  <a href="README.md"><img src="https://img.shields.io/badge/中文-当前-blue" alt="中文" /></a>
  <a href="README.en.md"><img src="https://img.shields.io/badge/English-Switch-lightgrey" alt="English" /></a>
</p>

<div align="center">
  <img src="apps/desktop/src-tauri/icons/icon.png" alt="Codex-X Logo" width="150" />

  # Codex-X

  **Codex 可视化提示词注入 · Provider · 会话 · Skills / MCP 管理工具**

  一款面向 **OpenAI Codex 桌面端 / Codex CLI** 的跨平台桌面工具。把提示词模板、自定义 Prompt、第三方 API 供应商、会话同步、Skills / MCP 和 TOML 配置都放进可视化界面里，不用反复手改文件。

  <p>
    <img src="https://img.shields.io/github/v/release/yynxxxxx/Codex-X?label=version&color=blue" alt="version" />
    <img src="https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-555" alt="platform" />
    <img src="https://img.shields.io/badge/built%20with-Tauri%202-24C8DB" alt="tauri" />
    <img src="https://img.shields.io/badge/license-MIT-green" alt="license" />
  </p>

  <p>
    <img src="https://img.shields.io/badge/React-18-61DAFB?logo=react&logoColor=white" />
    <img src="https://img.shields.io/badge/TypeScript-5-3178C6?logo=typescript&logoColor=white" />
    <img src="https://img.shields.io/badge/Rust-stable-000000?logo=rust&logoColor=white" />
    <img src="https://img.shields.io/badge/SQLite-Ready-003B57?logo=sqlite&logoColor=white" />
    <img src="https://img.shields.io/badge/Vite-Ready-646CFF?logo=vite&logoColor=white" />
  </p>
</div>

---

## Codex-X 是什么？

当你同时使用 Codex 桌面端、CLI、第三方 API、Skills / MCP 和多套提示词时，配置很容易散落在不同文件里。Codex-X 把这些高频操作集中到一个桌面界面中，让当前状态看得见、常用操作点一下就能完成。

你可以用它：

- 像管理插件一样管理提示词：分类、导入 Markdown、自定义编辑、一键启用 / 禁用
- 内置 5 套提示词模板，同时支持用户把自己的提示词变成可视化模板库
- 保存、测试并切换 OpenAI Official 与第三方 API，还能从 cc-switch 导入现有供应商
- 同步、检查、搜索和删除本地会话，按项目路径整理 Codex 历史记录
- 集中管理 Skills 与 MCP，查看当前 `config.toml`、`auth.json` 和操作备份

## 软件预览

<details open>
<summary><b>新版 UI：指令提示词管理中心</b></summary>

<p align="center">
  <img src="docs/screenshots/app/new-ui/prompts.png" alt="Codex-X 新版指令提示词管理界面" width="920" />
</p>

</details>

<div align="center">
<table>
  <tr>
    <td align="center" width="50%">
      <b>分类管理</b><br />
      <sub>把提示词按破甲 / 逆向、软件开发、写作辅助等分类维护</sub><br />
      <img src="docs/screenshots/app/new-ui/prompt-categories.png" alt="Codex-X 提示词分类管理" width="420" />
    </td>
    <td align="center" width="50%">
      <b>自定义提示词</b><br />
      <sub>直接添加、编辑或导入自己的 Markdown 提示词</sub><br />
      <img src="docs/screenshots/app/new-ui/prompt-form.png" alt="Codex-X 添加自定义提示词" width="420" />
    </td>
  </tr>
</table>
</div>

<details>
<summary><b>Skills / MCP 可视化管理</b></summary>

<p align="center">
  <img src="docs/screenshots/app/new-ui/skills-mcp.png" alt="Codex-X Skills 与 MCP 管理界面" width="920" />
</p>

</details>

## 功能特性

<div align="center">
<table>
  <tr>
    <th align="center" width="190">你想做的事</th>
    <th align="center">Codex-X 能帮你</th>
  </tr>
  <tr>
    <td align="center"><b>提示词注入管理</b></td>
    <td align="left">内置 <b>5 套</b>提示词模板，支持分类、GitHub 同步、本地缓存、导入 <code>.md</code>、添加自定义提示词、编辑说明、一键启用 / 禁用。</td>
  </tr>
  <tr>
    <td align="center"><b>启用方式切换</b></td>
    <td align="left">可选择“保留原提示词”追加写入，也可选择“替换原提示词”完整切换；适合在不同模型、不同任务、不同 Prompt 之间快速切换。</td>
  </tr>
  <tr>
    <td align="center"><b>Provider / API</b></td>
    <td align="left">添加、编辑、启用、删除第三方供应商；支持连接检测、模型获取 / 测试、从 cc-switch 导入，并可在 OpenAI Official 与中转 API 之间切换。</td>
  </tr>
  <tr>
    <td align="center"><b>会话管理</b></td>
    <td align="left">搜索本地会话、按项目路径分组、同步当前供应商、检查会话状态，并支持单选 / 多选 / 项目级永久删除。</td>
  </tr>
  <tr>
    <td align="center"><b>Skills / MCP</b></td>
    <td align="left">可视化查看 Skills 与 MCP，导入已有配置，从 ZIP 安装 Skill，逐项启用 / 禁用，并检查更新状态。</td>
  </tr>
  <tr>
    <td align="center"><b>配置与登录</b></td>
    <td align="left">集中查看 Codex 当前使用的 <code>config.toml</code> 与 <code>auth.json</code>，区分官方登录态和第三方 API Key；重要写入前自动备份。</td>
  </tr>
  <tr>
    <td align="center"><b>跨平台使用</b></td>
    <td align="left">提供 macOS Apple Silicon / Intel、Windows MSI / 便携版和 Linux 安装包；安装版可在应用内直接下载、校验并安装更新，便携版继续使用手动下载。</td>
  </tr>
</table>
</div>

## 核心亮点

### 1. 可视化提示词注入中心

<p align="center">
  <img src="https://img.shields.io/badge/当前模板库-5_套-2563eb?style=flat-square" alt="当前模板库 5 套" />
  <img src="https://img.shields.io/badge/离线内置-5_套-16a34a?style=flat-square" alt="离线内置 5 套" />
  <img src="https://img.shields.io/badge/GitHub_同步-自动更新-f59e0b?style=flat-square" alt="GitHub 自动同步" />
  <img src="https://img.shields.io/badge/自定义提示词-支持导入_编辑-7c3aed?style=flat-square" alt="支持自定义提示词" />
</p>

> [!TIP]
> **安装后就能用，联网后自动补齐，也能维护自己的提示词库。**
>
> 安装包离线自带当前全部 5 套模板；软件启动后可同步 GitHub `examples/` 的更新和新增模板。同步成功的在线版本会缓存到本地，临时离线仍可继续使用。你也可以导入自己的 `.md`、新增分类、编辑说明，并像切换插件一样启用或禁用任意提示词。

Codex-X 现在不只是“几套内置 Prompt”的启动器，而是一个可视化提示词注入与管理工具：

- 按分类管理提示词，例如破甲 / 逆向、软件开发、写作辅助，也可以新增自己的分类
- 支持同步 GitHub 模板、导入 Markdown、手动添加提示词、编辑标题 / 文件名 / 内容
- 每个提示词都有独立开关，打开时自动按当前启用方式写入 Codex 指令文件
- 支持“保留原提示词”和“替换原提示词”两种模式，适合日常叠加或完整切换
- 本地缓存可离线使用，后续模板更新不会影响你自己维护的自定义提示词

<div align="center">
<table>
  <tr>
    <th align="center">模板</th>
    <th align="center">适合场景</th>
    <th align="center">获取方式</t