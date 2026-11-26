<p align="center"><img src="docs/readme/banner.png" alt="麦田 · 给多平台博主的开源工作台" /></p>

<p align="center">
  <a href="https://maitian.mdldm.club/?utm_source=github&utm_medium=readme&utm_campaign=maitian-readme"><img src="https://img.shields.io/badge/官网-maitian.mdldm.club-7B5CFF" alt="官网" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-2ea44f" alt="MIT" /></a>
  <img src="https://img.shields.io/badge/macOS%20%7C%20Windows-1c1a16?logo=apple" alt="macOS | Windows" />
  <img src="https://img.shields.io/badge/Node.js-%E2%89%A5%2022.5-5FA04E?logo=nodedotjs&logoColor=white" alt="Node 22.5+" />
  <a href="https://chromewebstore.google.com/detail/eaaipbilkhibicihiollecmbpneikpnj"><img src="https://img.shields.io/badge/Chrome-麦田发布助手-F2B21B?logo=googlechrome&logoColor=white" alt="麦田发布助手" /></a>
  <a href="https://github.com/CzzzzzzJ/mdldm-maitian/stargazers"><img src="https://img.shields.io/github/stars/CzzzzzzJ/mdldm-maitian?style=social" alt="Stars" /></a>
</p>

<p align="center">
  <a href="#一行装好">一行装好</a> ·
  <a href="#看它跑一遍">看它跑一遍</a> ·
  <a href="#怎么配合">怎么配合</a> ·
  <a href="#各平台的坑实战总结">各平台的坑</a> ·
  <a href="docs/faq.md">常见问题</a> ·
  <a href="SHOWCASE.md">用户案例</a> ·
  <a href="CONTRIBUTING.md">参与贡献</a> ·
  <a href="#作者">作者</a>
</p>

> **一句话**：麦田是 Agent 驱动的自媒体发布工作台——你对 AI 说一句「整理发布」，一期视频填好七个平台，数据每天自己回来。
> **一行装好**：`bash -c "$(curl -fsSL https://raw.githubusercontent.com/CzzzzzzJ/mdldm-maitian/main/scripts/install.sh)"`（Windows 见[下文](#一行装好)）· 用麦田做出了东西？[来晒案例](SHOWCASE.md)

一个人做内容，要发六七个平台，每个平台的文案、封面、发布形式都不一样；发完还想知道哪期起来了、哪个平台涨粉、哪个平台真的带来了付费。麦田就是我自己每天在用的那套工作台：

1. **发得出去**：一期视频分批填好 B站、抖音、小红书、视频号、YouTube、X、Instagram，提前排进「分发计划」，到点发布、自动取链接。
2. **看得清楚**：每期在每个平台的播放、互动，各平台粉丝，每天自动采、长期留存；手机上看大屏，飞书群推卡片。
3. **算得出钱**：接上你自己的站点，看哪一期、哪个平台带来了注册和收入。

> 跑在一台常开的 Mac 或 Windows 电脑上，用你自己登录好的浏览器操作各平台，**不存任何平台密码**。国内四家只填写不发布，最后一下由你自己点。

## 看它跑一遍

<p align="center"><img src="https://github.com/CzzzzzzJ/mdldm-maitian/releases/download/media/maitian-publish.gif" alt="一期视频的发布流程：Agent 写文案 → 进分发计划 → 插件分批填写各平台 → 国内平台你来点发布 → 到点回填链接" /></p>
<p align="center"><sub>一期视频从写文案到上线（47 秒，各平台发布页为示意，数据是作者第 4 期的真实文案和封面）· <a href="https://github.com/CzzzzzzJ/mdldm-maitian/releases/download/media/maitian-publish.mp4">高清 MP4</a></sub></p>

<p align="center"><img src="docs/screenshots/board.jpg" alt="麦田大屏：最新一期轮播、粉丝、数据分析、各平台卡片（演示数据）" /></p>
<p align="center"><sub>大屏（演示数据，<code>node src/demo.mjs</code> 就能看到）</sub></p>

| 日历：分发计划 | 单期复盘：同龄对比 | 每期转化漏斗 |
|---|---|---|
| <img src="docs/screenshots/calendar.jpg" alt="日历" /> | <img src="docs/screenshots/episode.jpg" alt="单期复盘" /> | <img src="docs/screenshots/convert.jpg" alt="转化漏斗" /> |

## 怎么配合

<p align="center"><img src="docs/readme/flow.png" alt="发布 skill → 麦田发布助手 → 麦田" /></p>

| 部分 | 做什么 | 在哪 |
|---|---|---|
| 发布 skill | 让 AI 助手（Claude Code / Codex）看片、写各平台文案、生成发布工程并校验 | 本仓库 [`skills/maitian-publish`](skills/maitian-publish/SKILL.md) |
| 麦田发布助手 | Chrome 插件，各平台适配器：打开上传页、传视频和封面、填文案、设定时 | [Chrome 应用商店](https://chromewebstore.google.com/detail/eaaipbilkhibicihiollecmbpneikpnj)（装进麦田的专用 Chrome，自动更新） |
| 麦田（本仓库） | 分发计划、调度、防重、等你点发布、取链接、采数据、网页大屏、飞书通知 | 本仓库 |

链路：成片 → skill 写「发布素材.md」→ 生成 `publish.json` → `hub plan` 进分发计划 → `hub run` 分批填写 → 国内平台你点发布 → 到点取链接 → 每天采数据 → 大屏和飞书卡片。

## 安装

三种方式，按自己习惯挑一种。

### Agent 自动安装

不动手也能装：把下面这段话复制给你的 AI 助手（Claude Code / Codex 等）。它会读专门的[安装指引](agent-install.md)，自行装好麦田本体，并把发布 skill 装进**它自己**的 skill 目录——各 Agent 的 skill 目录不同，所以让 Agent 按指引自行安装，不依赖一行安装脚本里写死的 Claude 路径：

```text
请帮我接入麦田的发布能力：阅读 https://raw.githubusercontent.com/CzzzzzzJ/mdldm-maitian/main/agent-install.md 并严格按其中的步骤完成安装与授权。
```

### 一行装好

```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/CzzzzzzJ/mdldm-maitian/main/scripts/install.sh)"
```

下载麦田和发布助手到 `~/maitian/`、接上发布 skill、打开安装向导；向导问完几个问题，生成配置、装好开机自启、打开各平台登录页。需要 macOS、Node.js ≥ 22.5、Google Chrome。

Windows（社区贡献，感谢 [ajin558](https://github.com/ajin558)；开机自启暂未适配）：

```powershell
powershell -ExecutionPolicy Bypass -Command "irm https://raw.githubusercontent.com/CzzzzzzJ/mdldm-maitian/main/scripts/install-windows.ps1 | iex"
```

同样下载到 `%USERPROFILE%\maitian\`、接上发布 skill、打开安装向导，安装目录里另有 4 个双击启动器（演示 / 登录 / 体检 / 启动）。需要 Windows 10/11、Node.js ≥ 22.5、Google Chrome；缺 Git / Node 时脚本会用 winget 自动补装。开机自启暂未适配（向导里的 launchd 步骤会自动跳过），可用任务计划程序指向安装目录的 `4-start.bat` 代替。

<p align="center"><img src="https://github.com/CzzzzzzJ/mdldm-maitian/releases/download/media/maitian-install.gif" width="720" alt="一行安装演示" /></p>

### 手动安装

或者手动：

需要：macOS、Node.js ≥ 22.5（用到内置 `node:sqlite`）、Google Chrome；可选 NAS（放成片）、飞书群机器人、cloudflared。

```bash
git clone https://github.com/CzzzzzzJ/mdldm-maitian.git && cd mdldm-maitian
node src/demo.mjs                       # 先用假数据看看效果：http://localhost:8788/?key=demo
node src/init.mjs                       # 安装向导：检查环境、生成 config.json、装开机自启；在专用 Chrome 里从应用商店添加麦田发布助手、登录各平台
node src/hub.mjs doctor                 # 登录完检查各平台登录态和上传页（不上传、不填写）
```

打开向导最后给出的地址（`http://localhost:8787/?key=<web.key>`），之后浏览器会记住口令。手动安装也可以：`cp config.example.json config.json` 填好