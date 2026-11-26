<div align="center">

<img src="assets/logo.svg" width="96" height="96" alt="Obsidian Prism Logo" />

# Obsidian Prism · 黑曜棱镜

**为 Google Antigravity 打造的原生光学界面套件**

四套深浅配色 · 会呼吸的 512K 上下文试管 · 推理等级滑块 · 像素伙伴 · 自定义动静态壁纸（Beta）· Chat 对话模式（Beta）

[**简体中文**](./README.md) · [**English**](./README.en.md) · [**更新日志 (CHANGELOG)**](./CHANGELOG.md) · [**下载安装包 (Releases)**](https://github.com/RMvdesi/obsidian-prism/releases) · [**问题反馈 (Issues)**](https://github.com/RMvdesi/obsidian-prism/issues)

<p>
  <a href="https://github.com/RMvdesi/obsidian-prism/releases"><img src="https://img.shields.io/github/v/release/RMvdesi/obsidian-prism?style=flat-square&color=3186ff&label=Release" alt="Latest Release" /></a>
  <img src="https://img.shields.io/badge/Version-1.0.8--beta.3-0f172a?style=flat-square" alt="Version 1.0.8-beta.3" />
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20Universal-1e293b?style=flat-square" alt="Platform" />
  <a href="https://github.com/RMvdesi/obsidian-prism/actions"><img src="https://img.shields.io/github/actions/workflow/status/RMvdesi/obsidian-prism/ci.yml?branch=main&style=flat-square&label=CI" alt="CI Status" /></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/License-GPL--3.0-2563eb?style=flat-square" alt="License: GPL-3.0" /></a>
  <a href="./NOTICE"><img src="https://img.shields.io/badge/Attribution-Required%20(NOTICE)-8b5cf6?style=flat-square" alt="Attribution Required" /></a>
</p>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/screenshots/hero-dark.webp" />
  <source media="(prefers-color-scheme: light)" srcset="assets/screenshots/hero-light.webp" />
  <img src="assets/screenshots/hero-dark.webp" width="100%" alt="Obsidian Prism v1.0.8-beta.3 界面演示" />
</picture>

<sub>以上画面由离线渲染舞台直接运行本仓库前端源码逐帧录制，示例工作区与对话内容均为虚构。</sub>

</div>

> **非官方社区项目与商标免责声明 (Non-Affiliation Disclaimer)**
>
> **Obsidian Prism is an independent open-source project and is not affiliated with or endorsed by Google LLC.**
> 本项目为独立的开源社区工程，与 Google LLC 无任何隶属、赞助或官方背书关系；文中提及的 “Antigravity” 与 “Google” 仅作兼容性说明用途。

---

## 亮点

- **四套配色，一键换装**：深空黑曜、暖炭玄岩两套深色，白昼冷晶、暖白画册两套浅色，可跟随系统亮暗自动切换。
- **看得见的上下文**：输入框旁的小试管实时显示 512K 上下文用量，点开就能看到用量拆分和配额剩余预测。
- **推理等级，一拨就换**：模型菜单里内置星空滑块；选中 Orchestrator 时，滑块会变成一条会折射光线的切工水晶。
- **读得懂的思考过程与标题**：模型的思考内容支持实时转译成中文（沉浸 / 双语对照）与一键诊断，支持手动 HTTP/SOCKS5 代理、可选工具摘要与会话标题自动翻译。
- **自定义动静态背景壁纸（Beta）**：位于设置「Beta 内容」分类，默认关闭零占用，支持纯本机只读加载自定义图片与 MP4/WebM 动态视频背景（实验性功能，交互与表现可能随版本持续调整）。
- **桌面上的像素伙伴**：Clawd、小紫猫和三只迷你蟹会在输入框上方玩叠叠乐，还藏着一个彩虹彩蛋。
- **更顺手的工作台**：内置浏览器和大文件检视台、右键快捷菜单、长代码块折叠、会话大纲快速跳转。
- **Chat 对话模式（Beta）**：在写代码之外，多了一个专门聊天、整理资料的空间，和工程设置互不干扰。
- **轻、快、守规矩**：动画空闲时自动降到 0fps；本地服务只监听本机；设置改动 10 毫秒内生效，随时一键卸载还原。

---

## 界面预览

### 1. 四套配色

<p align="center">
  <img src="assets/screenshots/palettes.webp" width="100%" alt="四套深浅配色方案" />
</p>

| 主题预设 | 配置键值 | 侧栏底色 | 主画布 | 说明 |
| :--- | :--- | :--- | :--- | :--- |
| **深空黑曜** | `palette: "obsidian"` | `#09090B` | `#0E0E11` | 冷调深灰底色，高对比度代码阅读配色 |
| **暖炭玄岩** | `palette: "warm"` | `#10100F` | `#141413` | 暖炭褐底色，低蓝光夜间配色 |
| **白昼冷晶** | `lightPreset: "crystal"` | `#E8EEF6` | `#F4F7FB` | 冷调浅灰蓝侧栏与高明度工作区 |
| **暖白画册** | `lightPreset: "alabaster"` | `#EBE6DC` | `#F6F4EE` | 暖白纸色背景，柔和对比度浅色配色 |

### 2. 光学细节：上下文试管 · 推理滑块 · 切工水晶

点击底部试管可展开用量浮窗，查看上下文切片、5 小时配额与模型池余量；模型菜单里的推理等级滑块随档位点亮星辰，Orchestrator 则显示为切工水晶条。

<p align="center">
  <img src="assets/screenshots/optics.webp" width="100%" alt="512K 上下文试管、推理等级滑块与 Orchestrator 切工水晶" />
</p>

### 3. 像素伙伴

输入框上方的像素伙伴可以拖拽、叠成 5 层高塔；满足特定条件时，小紫猫会披上彩虹极光（无操作时自动休眠，可在设置中关闭）。

<p align="center">
  <img src="assets/screenshots/companions.webp" width="100%" alt="像素伙伴叠叠乐与彩虹彩蛋" />
</p>

### 4. Chat 对话模式（Beta）

默认关闭，可在 **设置 → 外观 → Beta 内容** 中开启。开启后侧栏顶部可在 Code 与 Chat 之间切换，用文件夹整理日常对话，权限按项目隔离，不改动全局工程设置。

<p align="center">
  <img src="assets/screenshots/chat-mode.webp" width="100%" alt="Chat 对话模式（Beta）" />
</p>

### 5. 更多能力

- **外观设置中心**：集成在 **设置 → 外观**，双栏光学布局、**8 种界面语言**（简中/繁中/英/日/韩/西/法/德）、**36 项**端到端可校验配置（含侧栏导航折叠 `sidebarNavFold`、滚底动效 `scrollBottomMotion` 与「正式版 / Beta 尝鲜版」双更新通道）、三档场景预设（完整光效 / 专注编码 / 静默省电）、配置备份恢复与面板内一键更新。
- **思考转译与标题翻译**：按需加载模块，关闭态默认零注入并支持热插拔；内置免配置机器翻译与本地/兼容模型流式转译，支持 OS 系统代理自动检测与手动 HTTP/SOCKS5 代理、可选工具摘要与会话标题自动翻译、卡片顶部「一键诊断」及源码路径/行号跳转。
- **自定义静态 / 动态视频壁纸（Beta）**：实验性按需加载模块，默认关闭零占用；纯本机只读加载图片（JPG/PNG/WebP/GIF/AVIF）与动态视频（MP4/WebM），支持透明度/模糊/护眼遮罩调节、Browser Hole 自动避让及失焦/隐藏自动 `0fps` 暂停。
- **Omni 检视台与行内 Diff 预览**：裸链接、本地路径一键在侧栏打开，文件变更支持行内 Diff 预览；超大视频、音频、PDF、表格、字体流式预览，右键菜单复制路径、定位文件、插入引用。
- **Smoked Obsidian 切面与工作台增强**：统一烟熏黑曜消息气泡、变更条、Artifact 卡片与石墨键帽；代码块顶栏吸顶、长代码块手动折叠、左侧会话导轨独立大纲入口与悬停大纲、`Alt+↑` / `Alt+↓` 上下轮跳转，以及会话区右键 `/btw` 侧边提问与 `/compact`、`/plan`、`/learn`、`/grill-me` 原生斜杠快捷指令。

<details>
<summary><strong>技术细节：性能、安全边界、遥测与配置（点击展开）</strong></summary>

**Obsidian Prism (`v1.0.8-beta.3`)** 在不改动宿主业务逻辑、不触碰外部插件锁文件的前提下，通过模块化按需加载插件架构为 Antigravity 桌面端提供 Smoked Obsidian 视觉界面、工作台交互与行内 Diff 增强、侧边栏内置浏览器与多格式流式检视台、模型配额遥测、思考过程转译及实验性动静态壁纸（Beta）：

- **四套深浅配色与细节微调**：内置深色（`obsidian` 深空黑曜、`warm` 暖炭玄岩）与浅色（`crystal` 白昼冷晶、`alabaster` 暖白画册）共四套主