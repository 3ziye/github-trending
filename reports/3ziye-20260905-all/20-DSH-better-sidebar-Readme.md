# dsh-better-sidebar

<!-- Hero -->
<div align="center">
  <b style="font-size: 1.15em;">一个服务化的侧边栏框架，一套开箱即用的完整工作台</b><br /><br />
  <a href="https://www.npmjs.com/package/dsh-better-sidebar"><img alt="npm version" src="https://img.shields.io/npm/v/dsh-better-sidebar" /></a>
  <a href="https://www.npmjs.com/package/dsh-better-sidebar"><img alt="npm downloads" src="https://img.shields.io/npm/dm/dsh-better-sidebar" /></a>
  <a href="https://github.com/omdsh-dev/DSH-better-sidebar/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/omdsh-dev/DSH-better-sidebar/actions/workflows/ci.yml/badge.svg" /></a>
  <a href="https://github.com/omdsh-dev/DSH-better-sidebar/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/omdsh-dev/DSH-better-sidebar" /></a>
  <a href="https://opensource.org/licenses/MIT"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" /></a>
  <a href="https://dshfind.com/zh/plugins/omdsh-dev/DSH-better-sidebar?ref=badge"><img alt="dshfind" src="https://dshfind.com/api/badge/omdsh-dev/DSH-better-sidebar?lang=zh" /></a><br /><br />
  <a href="https://www.npmjs.com/package/@deepseek-ai/dsh?activeTab=versions"><img alt="支持的 DSH 版本（v0.18.0 正式版）：0.1.2-rc.1+" src="https://img.shields.io/badge/DSH-0.1.2--rc.1%2B-4d6bfe" /></a>
  <a href="https://github.com/topics/dsh-better-sidebar"><img alt="插件生态：GitHub topic dsh-better-sidebar" src="https://img.shields.io/badge/%E6%8F%92%E4%BB%B6%E7%94%9F%E6%80%81-topic%20dsh--better--sidebar-4d6bfe" /></a><br /><br />
  <img alt="文件管理" src="https://img.shields.io/badge/-文件管理-4d6bfe" /> <img alt="编辑预览" src="https://img.shields.io/badge/-编辑预览-4d6bfe" /> <img alt="内嵌浏览器" src="https://img.shields.io/badge/-内嵌浏览器-4d6bfe" /> <img alt="真实终端" src="https://img.shields.io/badge/-真实终端-4d6bfe" /> <img alt="文件变动" src="https://img.shields.io/badge/-文件变动-4d6bfe" /> <img alt="后台任务" src="https://img.shields.io/badge/-后台任务-4d6bfe" /> <img alt="侧边对话" src="https://img.shields.io/badge/-侧边对话-4d6bfe" /> <img alt="插件接入" src="https://img.shields.io/badge/-插件接入-4d6bfe" /><br /><br />
  <b>右侧栏 + 底部面板双工作台</b>，并把 <code>ctx.betterSidebar</code> 服务开放给所有插件——<br />
  通过 <code>registerTab</code> / <code>registerFileViewer</code> 注册新的侧边栏页面与文件预览器。
</div>

<div align="center">
  🌏 <a href="./README.md"><b>中文</b></a> · <a href="./README_EN.md">English</a>
</div>

<div align="center">
  <img alt="dsh-better-sidebar 工作台截图" src="https://github.com/user-attachments/assets/991c4b70-d45a-461f-a8c8-0a28b4218e60" />
  <video src="https://github.com/user-attachments/assets/23187822-047e-45cc-b480-fe997bd55b86" muted autoplay loop playsinline controls width="100%"></video>
</div>

## 📑 目录

- [✨ 功能一览](#-功能一览)
- [🚀 安装](#-安装)
- [🖼️ 特性巡礼](#-特性巡礼)
- [🌐 插件生态](#-插件生态)
- [🆕 最近更新](#-最近更新)
- [⌨️ 快捷键](#-快捷键)
- [🔌 服务化扩展](#-服务化扩展)
- [🛠️ 开发与构建](#-开发与构建)
- [🔐 安全](#-安全) · [⚠️ 已知限制](#-已知限制) · [🖥️ 平台支持](#-平台支持)
- [💬 社区](#-社区) · [🤝 参与贡献](#-参与贡献) · [⭐ Star History](#-star-history) · [🔗 友情链接](#-友情链接)

## ✨ 功能一览

- **🗂️ 文件工作台**：资源管理器（懒加载目录树；软链接按目标类型展示——目录软链接可展开、失效链接标红）+ CodeMirror 编辑器；图片 / Markdown（含 Mermaid 图表，strict 安全渲染 + 点击放大；README 级内嵌 HTML——徽章墙 / `<details>` 折叠 / 表格内联标签经 DOMPurify 消毒真实渲染；浮动目录大纲一键跳转）/ HTML / PDF
- **🌐 内嵌浏览器**：多开网页 tab，后退 / 前进 / 刷新；内容运行在沙箱 iframe；外链默认按协议分流——HTTP 在侧边栏打开、HTTPS 走系统浏览器（设置页可分别调整）
- **💻 真实终端**：xterm.js + node-pty 真实 shell，断线重连回放；可选为模型注入 `terminal_*` 工具
- **📂 模型侧边栏打开（可选）**：全局设置开启后注入 `sidebar_open` 工具——模型可主动在侧边栏打开文件 / 文件夹（树以该目录为根）/ HTTP(S) 网页
- **🌿 文件变动**：Git 视角（真 diff / 历史 / 暂存·提交·还原 / worktree·子仓库选择）与本轮文件视角（模型读 / 写 / 编辑实时追踪，按文件分组、按类型筛选）**双视角合一**；统一 diff 渲染（改蓝配对 + 行内字符级高亮 + 语法着色 + 上下文折叠），底部可拖拽预览面板，可一键展开为独立 diff tab（默认自由浮窗，可在设置改为面板下半 split）
- **🧩 后台任务页**：subagent 拓扑 + 后台任务（退出码 / 实时输出 / 强制终止）
- **💬 侧边对话(beta)**：Codex 风格的侧边线程——继承主会话完整上下文（含进行中的回合与工具调用）独立运行，不进入主会话；线程内可持续追问，一键「保存为新会话」提升为顶层会话
- **🪟 双工作台**：右侧栏 + 底部面板；拖 Tab 拆分 / 合并分栏（可跨面板），移动端自动合并全宽抽屉
- **🪟 自由窗口**：把标签栏的任一 tab 拖到主会话区域——成为可移动 / 缩放 / 置顶的悬浮窗口（默认 390×780），拖回侧边栏 pane 即停靠，随会话持久化；`features` 含 `'floatWindows'`，插件 tab 无差别支持
- **📌 固定终端**：右键终端 Tab 可「固定到工作区 / 固定到全局」——固定后切换会话不消失，在 TabBar 内联呈现（跨会话虚拟 Tab，点击就地激活，PTY 按 home 会话 id+tab 直连宿主 PTY，无需切回宿主会话）；Agent 终端被 reconcile 移除时豁免保留
- **🔁 会话隔离**：布局 / Tab / 面板按会话持久化，陈旧状态自动净化
- **⚙️ 声明式设置**：设置页「侧边卡片」逐项独立开关，二级设置经齿轮弹窗
- **⚡ 按需加载**：启动只拉 ~325KB 核心，终端 / 编辑器 / Mermaid 图表等重依赖用到才按需拉取（[设计文档](docs/plans/2026-08-12-lazy-chunks-design.md)）
- **🌏 多语言**：界面文案跟随 DSH 语言（zh / en）实时切换；安装 `@huanlin/dsh-plugin-better-locale` 后支持日语（ja）等第三语言覆盖（见下方「🌏 第三语言覆盖」）

> 🔌 **核心理念**：服务优先——内置的 8 tab + 6 viewer 与第三方插件通过同一套 `ctx.betterSidebar` API 注册，能力完全对等；官方不再内置、可由生态提供的功能，交由生态插件实现（已有 **28+ 生态插件**，见下方「🌐 插件生态」）。接入文档见「🔌 服务化扩展」与 [外部插件接入指南](./docs/external-plugin-guide.md)。

## 🚀 安装

**前置**：已装好 DSH（`dsh web` 能正常运行），Node.js ≥ 20、pnpm ≥ 10。

**支持的 DSH 版本**：
<a href="https://www.npmjs.com/package/@deepseek-ai/dsh?activeTab=versions"><img alt="支持的 DSH 版本（v0.18.0 正式版）：0.1.2-rc.1+" src="https://img.shields.io/badge/DSH-0.1.2--rc.1%2B-4d6bfe" /></a>

> 📌 **正式版**：`v0.18.0` 起适配 DSH **0.1.2-rc.1+**（npm dis