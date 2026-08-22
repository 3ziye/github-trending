# dsh-web-ui · DSH Web UI

中文 | [English](README.en.md)

<p align="center">
  <img src="docs/dsh-web-ui-banner.png" alt="dsh-web-ui" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/github/v/release/zhu1090093659/dsh-web-ui?style=flat-square" alt="Version">
  &nbsp;
  <img src="https://img.shields.io/github/stars/zhu1090093659/dsh-web-ui?style=flat-square" alt="Stars">
  &nbsp;
  <img src="https://img.shields.io/github/forks/zhu1090093659/dsh-web-ui?style=flat-square" alt="Forks">
  &nbsp;
  <img src="https://img.shields.io/npm/v/@linxin666%2Fdsh-web-ui-all?style=flat-square&label=npm" alt="npm">
  &nbsp;
  <img src="https://img.shields.io/badge/license-Apache--2.0-blue?style=flat-square" alt="License">
  <br>
  <img src="https://github.com/zhu1090093659/dsh-web-ui/actions/workflows/ci.yml/badge.svg?style=flat-square&branch=main" alt="CI">
  &nbsp;
  <img src="https://img.shields.io/badge/coverage-pending-lightgrey?style=flat-square" alt="Coverage">
</p>

<p align="center">
  <strong>DeepSeek Harness（DSH）Web GUI 的插件与皮肤全家桶 · 一切皆开发，一切皆插件</strong><br>
  <em>梁神模式 · 任务看板 · Git 图谱 · 右侧面板 · 移动端远程 · SSH 运维 · 图像理解 · 鲸鱼娘宠物 · 皮肤中心</em>
</p>

<div align="center">

[是什么](#是什么) · [功能插件](#功能插件) · [皮肤](#皮肤) · [快速开始](#快速开始) · [常见问题](#常见问题) · [已知限制](#已知限制) · [社区](#社区)

</div>

## 是什么

dsh-web-ui 继承 DeepSeek Harness（DSH）「一切皆开发、一切皆插件」的核心理念，也是这一理念在 Web GUI 上最完整的落地：它不只是一个插件包，更是一个可拓展性极强的插件生态。面向 DeepSeek V4 Pro 的「梁神模式」agent 预设，以及任务看板、Git 图谱、右侧面板、移动端远程、SSH 运维、图像理解、鲸鱼娘宠物和皮肤中心——每一样都是独立成包的模块，可插拔、可替换、可再开发；可以一次装齐全家桶，拼出完整的开发工作台，也可以只挑一两个，安静地融入原生界面。所有插件都走官方 profile 机制挂载到 `dsh web`，不改 DSH 源码；聚合包还能把外部插件（如 `dsh-better-sidebar`）拼进全家桶，详见 [dsh-web-ui-all README](packages/dsh-web-ui-all/README.zh.md)。

「一切皆插件」还贯彻到了皮肤本身：皮肤中心 v2 重构后，一款皮肤不再是耦合官方 DSH 的 npm 包，而是一个纯资产目录——一份 skin.json 清单加上样式、贴图与可选特效脚本，交由皮肤中心这一唯一加载器即时加载。皮肤与官方彻底解耦、只与皮肤中心耦合：官方升级不再牵动任何皮肤，新增一款皮肤也只需落一个目录，无需发布、无需安装。插件负责逻辑，皮肤负责外观，边界从此清晰。

![DSH Web UI 主界面](docs/screenshots/13-hero-main.png)

| 能力 | 原生 dsh web | dsh-web-ui 全家桶 |
| --- | --- | --- |
| Agent 预设 | 官方预设（Standard / Minimal 等） | 梁神模式：面向 V4 Pro 的两阶段锚定预设 |
| 任务看板 | 无 | 多列看板 + cron 定时真实执行 |
| Git 可视化 | 无 | 分支泳道 + 提交历史图谱 |
| 文件预览与变更 | 无 | 右侧面板：better-sidebar（资源管理器 / 编辑器 / 终端 / Git / 浏览器）；旧 aionui 面板已停止支持（默认关闭，设置卡可临时切回） |
| 移动端远程 | 无 | 扫码配对，SSE 实时同步；同一链接也可配对 PC 浏览器远程使用完整 Web GUI |
| 远程服务器运维 | 无 | SSH 面板：终端 / 传输 / 隧道 / 集群 |
| 图像理解 | 无 | `describe_image` 视觉工具 |
| 主题皮肤 | 默认主题 | 皮肤中心 17 款，先试穿再应用 |

## 功能插件

### 梁神模式

DeepSeek V4 Pro 对首轮工具目录很敏感。社区评测里，官方 Standard / PTC 预设只有 91 / 92 分，Minimal 能到 99 / 96，但 Minimal 只有两个工具。梁神模式把这两步拼起来：新建会话时在预设选择器里选「梁神模式」，首轮按 Minimal 开局（只暴露持久 `bash` 与 `str_replace_editor`，只放行你自己的消息），轨迹锚定后自动切到 PTC Mode，完整工具注册表、workspace 指令和 skill 目录随后恢复。Windows 原生环境实测（DeepSeek V4 Pro）98 / 99，均值 98.5，不是抽卡，也不需要牺牲完整工具能力。

![梁神模式两阶段锚定效果对比（示意图，模拟渲染）](docs/images/liangshen-mode.png)

原理、稳定化控制与限制详见 [dsh-liangshen README](packages/dsh-liangshen/README.zh.md)。

### 任务看板

侧边栏点「任务看板」进入。任务按五列摆开：待规划、待办、进行中、已完成、已失败。点卡片上的「执行」，任务交给真实的 DSH 智能体会话去跑，跑完状态自动回写；想复盘就跳回执行会话看完整过程。

任务也支持 Host 定时跑：详情里配 cron 表达式（比如每天 23:00 自动升级 DSH、每周一 09:00 生成周报），关闭浏览器后仍会到点执行和结算。可选的空闲睡眠保护支持 Windows、macOS 和带 systemd-logind 的 Linux，允许屏幕熄灭，同时阻止整机因空闲睡眠；该设置默认关闭。

| 多列看板 | 定时执行 |
| --- | --- |
| ![任务看板](docs/screenshots/09-task-board.png) | ![任务定时执行](docs/screenshots/10-task-board-detail-cron.png) |

### Git 图谱

输入框上方有分支选择器，可以切分支、翻提交历史；Git 图谱把分支泳道和提交历史画出来，仓库再大也能顺着时间线找到变更。

![Git 图谱](docs/screenshots/04-git-graph.png)

### 移动端远程

侧边栏底部的手机图标打开配对面板。扫码（或复制链接）配对后，手机进独立移动端界面，远程操作当前的 dsh web 工作区：看会话、开新会话、收发消息、切模型和思考强度、调权限预设，都和桌面端同步。同一份配对链接也能配对 **PC 浏览器**（手机配对流扩展到桌面 Web GUI）：在另一台电脑打开桌面 URL 形态的链接，完整 Web GUI 便在那台设备上运行，流量走配对门控的 `/remote/api` 通道——未配对设备只有横幅提示、拿不到任何数据。配对令牌一次性、限时，「停止」随时吊销所有设备；二维码默认走局域网，开 cloudflared 公网隧道后手机（和 PC）在任何网络都能配对。PC 远程桌面应优先使用插件自己的设备配对通道，安全上不建议为隧道域名设置 `--trusted-host`；该 flag 会让 SDK 的 `/api` 绕过配对门控（详见[插件 README](packages/dsh-remote-web-ui/README.zh.md)）。

> **实时消息与隧道**：移动端靠 SSE（Server-Sent Events）收实时消息。Cloudflare quick tunnel（trycloudflare.com）和 Tailscale Serve 不透传 SSE，普通 HTTP 正常、实时推送到不了；这种网络下插件自动降级轮询，收发消息正常，只是新消息可能晚几秒。要即时推送就用支持 SSE 的隧道（Cloudflare named tunnel、自定义 TCP 端口转发等）。

| 工作区列表 | 会话列表与新建会话 |
| --- | --- |
| ![移动端工作区](docs/screenshots/20-mobile-workspaces.png) | ![移动端会话列表](docs/screenshots/21-mobile-sessions.png) |
| 聊天（折叠的深度思考与工具调用） | 模型与思考强度选择 |
| ![移动端聊天](docs/screenshots/22-mobile-chat.png) | ![模型选择](docs/screenshots/23-mobile-model-sheet.png) |

### 远程连接

侧边栏「SSH」入口打开远程运维面板。主机支持密钥 / 密码认证，可从 `~/.ssh/config` 一键导入；配置都在 `~/.dsh/dsh-ssh.json`。对已配置主机可执行真实操作：

- **Web 终端**：xterm.js 远程终端，实时输出，窗口大小自适应；
- **文件传输**：SFTP 上传 / 下载，有进度条，能浏览远程目录；
- **端口转发**：本地隧道直连远程内网服务（数据库、API、管理后台），只监听 127.0.0.1；
- **集群执行**：一条命令并发跑多台主机，按别名 / 环境 / 标签过滤；
- **Agent 直连**：Agent 和面板共用同一份主机配置，对话里说一句「连一下 xxx 看看状态」，智能体就去执行远程命令。

### 图像理解

给纯文本模型补上视觉：对话里提到图片（本地路径、http(s) URL、会话附件）时，`describe_image` 把图片发给配置好的 OpenAI 兼容视觉端点（Qwen-VL、GLM-4V、GPT-4o、本地 Ollama 都行）回答，**进会话的只有返回的文本，图片本身不进会话记录**。纯文本模型输入框没有图片入口，插件在输入框加了个图片按钮：选图后生成附件引用插进草稿，模型就能用 `describe_image` 分析；工具还支持 `prompt` 参数传自定义指令（O