<div align="center">

# 📦 FanBox

<img src="assets/promo-banner.jpg" alt="FanBox · Coding Agent 的驾驶舱" width="100%">

<br><br>

> *"AI 帮你一个下午起十个项目，然后它们就再也找不到了。FanBox 帮你把它们找回来。"*
> *"AI spins up ten projects in an afternoon. FanBox helps you find them again."*

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/alchaincyf/fanbox?label=Release&color=blue)](https://github.com/alchaincyf/fanbox/releases/latest)
[![Platform](https://img.shields.io/badge/macOS-Apple%20Silicon-black?logo=apple)](https://github.com/alchaincyf/fanbox/releases/latest)
[![Runtime](https://img.shields.io/badge/Runtime-no--build-blueviolet)](#architecture)

<br>

**FanBox：Coding Agent 的驾驶舱。指挥 Claude Code、Codex 在本地干活，看清它碰过的每个文件、改过的每一行，随时接手。**<br>
**FanBox — the cockpit for coding agents: command Claude Code or Codex, see every file and line they change, and take over anytime.**

<br>

一边浏览、预览、编辑本地文件；一边在内嵌真实终端里跑 Claude Code 或任何 coding agent。<br>
 agent 每写一个文件，对应卡片就会亮起来——*找回文件 → 运行 agent → 看清改了什么*，全部在一个窗口完成。<br>
<br>
Browse, preview and edit local files on one side; run Claude Code or any coding agent in a real embedded terminal on the other.<br>
Every time the agent writes a file, its card lights up — *find files → run agents → see what changed*, all in one window.

<br>

[⬇ 下载 dmg / Download dmg](https://github.com/alchaincyf/fanbox/releases/latest) · [Screenshots / 截图](#three-skins) · [Features / 功能](#what-it-does) · [Install / 安装](#install) · [Credits / 致谢](#credits)

</div>

---

<p align="center">
  <img src="assets/screenshot-volt.png" alt="FanBox · Volt skin · file browser on the left, README preview at the bottom, embedded terminal on the right" width="100%">
</p>

<p align="center"><sub>▲ 真机截图：浏览 fanbox 仓库本身，README 原地预览，内嵌终端正在跑 git。本页所有截图均由 Playwright 从实时 App 中直接拍摄，未修图。<br>Real capture: browsing the fanbox repo itself, README previewed in place, git running in the embedded terminal. All screenshots in this README are taken from the live app via Playwright, unedited.</sub></p>

---

<a id="why-fanbox"></a>
## Why FanBox · 为什么要做 FanBox

AI 帮你一个下午起十个项目，但它们散在各处、名字认不出、改了啥看不见。每天的真实流程是：Finder 里翻半天 → 切到 iTerm 启 agent → 再切浏览器看效果，三个窗口来回跳。

AI helps you start ten projects in an afternoon — then they scatter everywhere, the names stop making sense, and you can't see what got changed. The daily reality: dig through Finder → switch to iTerm to launch an agent → switch to the browser to check results. Three windows, endless hopping.

FanBox 把这条链路收进一个窗口：**左边文件 × 右边/下边终端 × 原地预览**，一个有机整体。它不跟 Finder 拼文件操作，不跟 VS Code 拼编辑，专注「找回 + 预览 + 轻改 + 指挥 agent」这一条链路做到顺手。

FanBox folds that loop into one window: **files on the left × terminal on the right/bottom × preview in place**. It doesn't compete with Finder on file ops or VS Code on editing. It does one chain well: *find → preview → light edits → command the agent*.

不做云、不做远程、不做账号。本地、零配置、运行时零依赖。

No cloud, no remote, no accounts. Local-first, zero config, zero runtime dependencies.

<a id="three-skins"></a>
## Three skins · 三套皮肤

界面在 [huashu-design](https://github.com/alchaincyf/huashu-design) 辅助下完成设计，三套皮肤不是换个主题色——配色、字体、图标、代码高亮、终端 ANSI 主题整体随之变化。

The UI was designed with [huashu-design](https://github.com/alchaincyf/huashu-design). The three skins are not theme-color swaps — palette, typography, icons, code highlighting and terminal ANSI themes all change together:

| | |
|---|---|
| <img src="assets/screenshot-volt.png" alt="Volt skin / 终端皮肤"> | **终端 · Volt** · 荧光绿 × 炭黑 × 等宽字，工业仪器面板感（默认）<br>**Volt** · neon green × charcoal × monospace, industrial instrument panel (default) |
| <img src="assets/screenshot-archive.png" alt="Archive skin / 档案皮肤"> | **档案 · Archive** · 奶油纸 × 赤陶橙 × 衬线，温暖纸感档案馆<br>**Archive** · cream paper × terracotta × serif, a warm paper archive |
| <img src="assets/screenshot-index.png" alt="Index skin / 索引皮肤"> | **索引 · Index** · 黑白 × 信号红/绿 × 巨号字，编辑式索引日报<br>**Index** · black & white × signal red/green × oversized type, editorial index daily |

<a id="what-it-does"></a>
## What it does · 能做什么

### Files · find & preview / 文件 · 找回与预览

- **⌘K 全局模糊搜索 / Global fuzzy search** — 记得名字片段就行；`⌘↵` 用编辑器整包打开项目；`内容:关键词` 切全文搜索。  
  A fragment of the name is enough; `⌘↵` opens the project in your editor; `content:keyword` switches to full-text search.
- **强色实体图标 / Bold solid icons** — 每种文件「长得像它自己」：PDF 红、JS 黄、Markdown 蓝；照片视频按真实比例呈现。  
  Every file type "looks like itself": red PDFs, yellow JS, blue Markdown; photos and videos render at true aspect ratio.
- **原地预览 / Preview in place** — Markdown 渲染、HTML 实时成品、代码语法高亮、图片/视频/PDF 内嵌（HEIC 直接显示）、压缩包内容清单、透明图棋盘格垫底。  
  Rendered Markdown, live HTML, syntax-highlighted code, inline images/video/PDF (HEIC included), archive content listing, checkerboard backing for transparent images.
- **缩略图加速 / Thumbnail speed** — 大文件夹滚动和点击都在 0.1 秒内。  
  Scrolling and clicking through large folders stays under 0.1s.
- **项目徽章 / Project badges** — 文件夹卡片标 node / web / py / rs / go 徽章，一下午起的十个项目一眼认出类型。  
  Folder c