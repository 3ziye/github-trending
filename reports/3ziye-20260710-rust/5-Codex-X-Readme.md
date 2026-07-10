<p align="center">
  <a href="README.md"><img src="https://img.shields.io/badge/中文-当前-blue" alt="中文" /></a>
  <a href="README.en.md"><img src="https://img.shields.io/badge/English-Switch-lightgrey" alt="English" /></a>
</p>

<div align="center">
  <img src="apps/desktop/src-tauri/icons/icon.png" alt="Codex-X Logo" width="150" />

  # Codex-X

  **Codex 提示词注入 · Provider 切换 · TOML / Auth 可视化管理器**

  一款面向 **OpenAI Codex 桌面端 / Codex CLI** 的跨平台桌面工具，内置 `gpt5.5-unrestricted.md` 与 `gpt5.4-unrestricted.md`，支持一键写入 / 禁用指令提示词、第三方 Provider 切换、官方 Auth 管理、TOML 可视化编辑与本地会话 Provider Sync。

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

Codex-X 不是普通的配置文件编辑器，而是一个面向 Codex CLI 的 **可视化增强管理器**。

它把几个高频操作做成了桌面软件：

- 给 Codex 写入 / 禁用指令提示词模板
- 切换官方 OpenAI 与第三方 Codex API Provider
- 查看 / 编辑 `~/.codex/config.toml`
- 查看 / 编辑官方 `~/.codex/auth.json`
- 检查并修复本地历史会话的 Provider 元数据

## 软件预览

<details open>
<summary><b>应用界面预览</b>：主界面 / Provider / TOML / Auth</summary>

<p align="center">
  <img src="docs/screenshots/app/preview.png" alt="Codex-X 应用界面预览：主界面、Provider、TOML、Auth" width="920" />
</p>

</details>

<details>
<summary><b>提示词注入效果：安全测试场景</b></summary>

<div align="center">
<table>
  <tr>
    <td align="center" width="50%">
      <b>SQL 注入测试</b><br />
      <sub>部署后测试：如何对目标进行 SQL 注入测试？</sub><br />
      <img src="docs/screenshots/prompt-effects/security/sql-injection.png" alt="SQL 注入测试效果图" width="420" />
    </td>
    <td align="center" width="50%">
      <b>NSFW 响应测试</b><br />
      <sub>用于观察提示词注入后的边界响应变化</sub><br />
      <img src="docs/screenshots/prompt-effects/security/nsfw.png" alt="NSFW 响应测试效果图" width="420" />
    </td>
  </tr>
</table>
</div>

</details>

<details>
<summary><b>提示词注入效果：逆向工程场景</b></summary>

<div align="center">
<table>
  <tr>
    <td align="center" width="50%">
      <b>APK 逆向分析</b><br />
      <sub>Android APK 静态 / 动态分析思路</sub><br />
      <img src="docs/screenshots/prompt-effects/reverse/apk-reverse-1.png" alt="APK 逆向分析效果图" width="420" />
    </td>
    <td align="center" width="50%">
      <b>APK 逆向分析 2</b><br />
      <sub>补充 APK 逆向流程与定位方式</sub><br />
      <img src="docs/screenshots/prompt-effects/reverse/apk-reverse-2.png" alt="APK 逆向分析效果图 2" width="420" />
    </td>
  </tr>
  <tr>
    <td align="center" colspan="2">
      <b>EXE 逆向分析</b><br />
      <sub>Windows 可执行文件分析与调试方向</sub><br />
      <img src="docs/screenshots/prompt-effects/reverse/exe-reverse.png" alt="EXE 逆向分析效果图" width="620" />
    </td>
  </tr>
</table>
</div>

</details>

## 功能特性

<div align="center">
<table>
  <tr>
    <th align="center" width="180">功能</th>
    <th align="center">说明</th>
  </tr>
  <tr>
    <td align="center">⚡ 供应商 API</td>
    <td>可视化管理官方 OpenAI / 第三方 Codex Provider，支持 Base URL、API Key、Model、Wire API 与一键切换。</td>
  </tr>
  <tr>
    <td align="center">🧩 <b>提示词注入</b></td>
    <td><b>特色功能</b>：内置 <code>gpt5.4-unrestricted.md</code> / <code>gpt5.5-unrestricted.md</code>，一键写入 Codex 配置；启用后可达到上方效果图中的 SQL 注入测试、APK / EXE 逆向等响应效果。</td>
  </tr>
  <tr>
    <td align="center">💬 会话管理</td>
    <td>读取 Codex 本地 SQLite 与 rollout JSONL，会话列表可视化展示，并支持 Provider Sync / 修复历史 thread 元数据。</td>
  </tr>
  <tr>
    <td align="center">📝 TOML 配置</td>
    <td>查看当前 <code>~/.codex/config.toml</code>，并在 Provider 编辑页直接编辑完整 TOML，保存后同步到 Codex 配置目录。</td>
  </tr>
  <tr>
    <td align="center">🧠 Skills / MCP</td>
    <td>新增技能和 MCP 管理页：读取 Codex 当前可用的 Skills / MCP，支持导入已有、从 ZIP 安装 Skill、启用 / 禁用单个 Skill 或 MCP，并可检查 Skill 更新状态。</td>
  </tr>
  <tr>
    <td align="center">🔐 Auth 管理</td>
    <td>读取 / 编辑官方 <code>~/.codex/auth.json</code>，区分 ChatGPT 登录态 Auth 与第三方 API Key。</td>
  </tr>
  <tr>
    <td align="center">📦 跨平台发布</td>
    <td>提供 macOS Apple Silicon / Intel <code>.dmg</code>、Windows <code>.msi</code> / portable <code>.zip</code>、Linux <code>.deb</code> / <code>.rpm</code>，支持应用内检测更新。</td>
  </tr>
</table>
</div>

## 核心亮点

### 1. 内置双指令提示词模板

Codex-X 当前内置两套提示词模板：

- `examples/gpt5.5-unrestricted.md`
- `examples/gpt5.4-unrestricted.md`

你可以在【指令提示词】页面直接点击启用 / 禁用。启用后，Codex-X 会把对应 `.md` 写入 Codex 配置目录，并更新 `config.toml` 中的 `model_instructions_file`。

<div align="center">
<table>
  <tr>
    <th align="center">对比项</th>
    <th alig