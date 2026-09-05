# dsh-web · DeepSeek Harness（DSH）Web GUI 插件聚合生态包

中文 | [English](README.en.md)

<p align="center">
  <img src="docs/dsh-web-banner.png" alt="dsh-web" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/github/v/release/zhu1090093659/dsh-web?style=flat-square" alt="Version">
  &nbsp;
  <img src="https://img.shields.io/github/stars/zhu1090093659/dsh-web?style=flat-square" alt="Stars">
  &nbsp;
  <img src="https://img.shields.io/github/forks/zhu1090093659/dsh-web?style=flat-square" alt="Forks">
  &nbsp;
  <a href="https://www.npmjs.com/package/@linxin666/dsh-web-all"><img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fdsh-market.com%2Fapi%2Fnpm-badge%2Fversion&style=flat-square&label=npm" alt="npm"></a>
  &nbsp;
  <a href="https://www.npmjs.com/package/@linxin666/dsh-web-all"><img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fdsh-market.com%2Fapi%2Fnpm-badge%2Ftotal&style=flat-square" alt="downloads"></a>
  &nbsp;
  <a href="https://dshfind.com/zh/plugins/zhu1090093659/dsh-web?ref=badge"><img src="https://dshfind.com/api/badge/zhu1090093659/dsh-web?metric=downloads&amp;lang=zh" alt="dshfind"></a>
  &nbsp;
  <a href="https://dsh-market.com"><img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fdsh-market.com%2Fapi%2Ftelemetry%2Fbadge%2Fusers&style=flat-square&label=users" alt="users"></a>
  &nbsp;
  <a href="https://www.npmjs.com/package/@deepseek-ai/dsh"><img src="https://img.shields.io/badge/DSH-%3E%3D0.1.2--rc.1-4c6ef5?style=flat-square&amp;labelColor=454a54" alt="DSH"></a>
  &nbsp;
  <img src="https://img.shields.io/badge/license-Apache--2.0-blue?style=flat-square" alt="License">
</p>

<p align="center">
  <strong>DeepSeek Harness（DSH）Web 的插件聚合生态包 · 一切皆插件</strong><br>
  <em>创意工坊 · 任务看板 · 移动端远程 · SSH 运维 · 图像理解</em>
</p>

<div align="center">

[是什么](#是什么) · [创意工坊](#创意工坊dsh-marketcom) · [功能插件](#功能插件) · [皮肤](#皮肤) · [快速上手](#快速上手) · [常见问题](#常见问题) · [已知限制](#已知限制) · [社区](#社区)

</div>

## 是什么

dsh-web 是 DeepSeek Harness（DSH）Web GUI 的插件聚合生态包（DSH Web plugin ecosystem），也是「一切皆开发、一切皆插件」理念在 Web 端最完整的落地：任务看板（task board）、移动端远程控制（mobile remote）、SSH 运维终端、图像理解（image understanding）、梁神模式 agent 预设、救助模式（rescue mode）与右侧面板，每一样都是独立成包的插件，可插拔、可替换、可再开发——一次装齐便是完整的 AI 开发工作台，只挑一两个也能安静融入原生界面。所有插件都经官方 profile 机制挂载到 `dsh web`，不改 DSH 源码；聚合包还能把外部插件（如 `dsh-better-sidebar`）拼进全家桶，其他皮肤与宠物资产统一从创意工坊获取，详见 [dsh-web-all README](packages/dsh-web-all/README.zh.md)。

皮肤同样长在插件体系里：v2 皮肤不是独立产品，而是「皮肤」插件的纯资产包（skin.json 清单 + 样式、贴图与可选特效脚本），由该插件这一唯一加载器即时加载，与官方彻底解耦——官方升级不再牵动皮肤，新增皮肤也只需落一个目录，无需发布、无需安装。插件负责逻辑，皮肤资产负责外观；Blue Fantasy 随插件内置，其他皮肤与宠物资产统一走 [创意工坊](#创意工坊dsh-marketcom)（dsh-market.com）。

![DSH Web UI 主界面](docs/screenshots/13-hero-main.png)

| 能力 | 原生 dsh web | dsh-web 全家桶 |
| --- | --- | --- |
| 性能观测与治理 | 无 | HUD 检测面板 + 事件/事件循环/内存指标 + 写批频控 + 渲染降载 + 三档告警 |
| Agent 预设 | 官方预设（Standard / Minimal 等） | 官方与社区预设 |
| 任务看板 | 无 | 多列看板 + cron 定时真实执行 |
| 移动端远程 | 无 | 扫码配对、SSE 实时同步；同一链接也可配对 PC 浏览器 |
| 远程服务器运维 | 无 | SSH 面板：终端 / 传输 / 隧道 / 集群 |
| 图像理解 | 无 | `describe_image` 视觉工具 |
| 文件预览与变更 | 无 | 右侧面板：资源管理器 / 编辑器 / 终端 / Git / 浏览器 |
| Git 可视化 | 无 | 分支选择器 + 提交历史图谱 |
| 主题皮肤 | 默认主题 | Blue Fantasy 随皮肤插件内置，其他皮肤从创意工坊按需安装 |

## 创意工坊（dsh-market.com）

[创意工坊](https://dsh-market.com)（dsh-market.com）是 DSH 的一站式创作空间，统一分发皮肤、宠物与插件：每类按设备点赞热度排序、前三名登上首页颁奖台；皮肤支持实时试穿预览，插件提供一键复制的安装命令。经典的 Blue Fantasy 蓝色幻想随皮肤插件内置，鲸鱼娘宠物与其他皮肤可在工坊浏览预览、查看源码并按需安装。Web GUI 里的「创意工坊」设置卡直接浏览工坊清单——皮肤与宠物一键装进 DSH 主目录，插件经插件管理器安装，装完即可在皮肤与宠物面板中使用。

![创意工坊首页](docs/screenshots/31-market-home.png)

站点也是本仓库的产物：纯静态构建，由 `scripts/market-build` 从三类真值源（`skin.json` / `pet.json` / `community.json`）确定性生成；点赞等动态能力由 Cloudflare Workers 边缘 API 承载（D1 持久化、按设备一票），push 到 `main` 即自动部署。

创意工坊对标 Steam Workshop 的定位：让社区创作被发现、被试穿、被一键装回家，让作者的作品被看见、被点赞——欢迎一起来建设。

## 功能插件

### 任务看板（Task Board）

侧边栏点「任务看板」进入。任务按五列摆开：待规划、待办、进行中、已完成、已失败。点卡片上的「执行」，任务交给真实的 DSH 智能体会话去跑，跑完状态自动回写；想复盘就跳回执行会话看完整过程。

任务也支持 Host 定时跑：详情里配 cron 表达式（比如每天 23:00 自动升级 DSH、每周一 09:00 生成周报），关闭浏览器后仍会到点执行和结算。可选的空闲睡眠保护支持 Windows、macOS 和带 systemd-logind 的 Linux，允许屏幕熄灭，同时阻止整机因空闲睡眠；该设置默认关闭。

| 多列看板 | 定时执行 |
| --- | --- |
| ![任务看板](docs/screenshots/09-task-board.png) | ![任务定时执行](docs/screenshots/10-task-board-detail-cron.png) |

### 移动端远程控制（Mobile Remote）

侧边栏底部的手机图标打开配对面板。扫码（或复制链接）配对后，手机运行的就是官方 Web GUI 本身，竖屏下自动注入触控适配层：鲸鱼按钮展开侧边栏、左滑收起 / 右滑展开、长按会话行展开与桌面省略号相同的操作菜单、Enter 只换行、16px 输入框防聚焦缩放；面向桌面的工具面（SSH 终端、任务看板、Git 图谱等）在手机上自动隐藏——看会话、开新会话、收发消息、切模型和思考强度、调权限预设，和桌面端同一份界面、同一份状态。同一份配对链接也能配对 **PC 浏览器**（手机配对流扩展到桌面 Web GUI）：在另一台电脑打开桌面 URL 形态的链接，完整 Web GUI 便在那台设备上运行，流量走配对门控的 `/remote/api` 通道——未配对设备只有横幅提示、拿不到任何数据。配对令牌一次性、限时，「停止」随时吊销所有设备；二维码默认走局域网，开 cloudflared 公网隧道后手机（和 PC）在任何网络都能配对。PC 远程桌面应优先使用插件自己的设备配对通道，安全上不建议为隧道域名设置 `--trusted-host`；该 flag 会让 SDK 的 `/api` 绕过配对门控（详见[插件 README](packages/dsh-remote-web-ui/README.zh.md)）。

![手机与 Web 同界面（示意图）](docs/assets/phone-and-web.png)

> **实时消息与隧道**：移动端靠 SSE（Server-Sent Events）收实时消息。Cloudflare quick tunnel（trycloudflare.com）和 Tailscale Serve 不透传 SSE，普通 HTTP 正常、实时推送到不了；这种网络下插件自动降级轮询，收发消息正常，只是新消息可能晚几秒。要即时推送就用支持 SSE 的隧道（Cloudflare named tunnel、自定