## 📝 热点项目-20261119-javascript

<div style="background-color: #f5f5f5; padding: 15px; border-radius: 8px; margin: 20px 0;">
- 🤖 本报告基于 GitHub API 自动生成
- 📅 数据更新时间: 2026-11-19 16:10:52 (上海时区)
- 🌟 星标数等统计信息为生成时的实时数据
- 📚 项目信息来源于各项目的 README 文档
- 💡 热度指数计算方式: 星标数 + Fork数 × 0.5
- 本报告由 三子叶开源 github-trending项目分析工具自动生成
</div>

## 🔗 相关链接

- [GitHub API 文档](https://docs.github.com/en/rest)
- [项目数据获取器源码](https://github.com/3ziye/github-trending)

---

# 热点项目-20261119-javascript

<div align="center">
📊 <strong>生成时间</strong>: 2026年11月19日 16:10  •  
🎯 <strong>项目数量</strong>: 20 个  •  
⏱️ <strong>热度时间</strong>: 月榜  •  
🔥 <strong>数据来源</strong>: GitHub API
</div>

---

## 🚀 热门项目详情

### 1. unslop

**🔥 热度指数**: 18,969

**项目名称**: [heydamir/unslop](https://github.com/heydamir/unslop)
**项目描述**: A Claude skill that turns vibecoded, AI-looking UI into a designed interface
**主要语言**: JavaScript
**许可证**: Creative Commons Attribution 4.0 International
**⭐ 星标数**: 18,417
**🍴 Fork 数**: 1,105
**👀 关注数**: 18,417
**🐛 开放问题**: 6
**最后更新**: 2026-11-19 (1分钟前)
**📖 项目文档**: [README](3ziye-20261119-javascript/1-unslop-Readme.md)

**🏠 项目主页**: 无

**📂 克隆地址**: `https://github.com/heydamir/unslop.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 2. pixelfx

**🔥 热度指数**: 8,731

**项目名称**: [patch-gg/pixelfx](https://github.com/patch-gg/pixelfx)
**项目描述**: 244 pixel art effects, every one a small piece of code. Plus a Claude Code skill to make your own.
**主要语言**: JavaScript
**许可证**: MIT License
**⭐ 星标数**: 8,199
**🍴 Fork 数**: 1,064
**👀 关注数**: 8,199
**🐛 开放问题**: 14
**最后更新**: 2026-11-19 (3分钟前)
**📖 项目文档**: [README](3ziye-20261119-javascript/2-pixelfx-Readme.md)

**🏠 项目主页**: https://patch-gg.github.io/pixelfx/

**📂 克隆地址**: `https://github.com/patch-gg/pixelfx.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🏷️ 项目标签
- `agent-skills`
- `animation`
- `canvas`
- `claude-code-plugin`
- `gamedev`
- `pixel-art`
- `sprite-sheet`
- `vfx`

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 3. apkstart

**🔥 热度指数**: 8,431

**项目名称**: [RoutineMiku/apkstart](https://github.com/RoutineMiku/apkstart)
**项目描述**: Windows 上的安卓应用运行器：双击 APK 即装，应用以独立窗口与桌面图标运行，自持 QEMU 运行时
**主要语言**: JavaScript
**许可证**: MIT License
**⭐ 星标数**: 8,046
**🍴 Fork 数**: 771
**👀 关注数**: 8,046
**🐛 开放问题**: 93
**最后更新**: 2026-11-19 (2分钟前)
**📖 项目文档**: [README](3ziye-20261119-javascript/3-apkstart-Readme.md)

**🏠 项目主页**: 无

**📂 克隆地址**: `https://github.com/RoutineMiku/apkstart.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🏷️ 项目标签
- `android`
- `android-x86`
- `apk`
- `electron`
- `emulator`
- `freeform`
- `qemu`
- `windows`

#### 🎯 核心特性
- 🖱️ **双击 .apk 即安装**：注册 .apk 文件关联后，在资源管理器里双击 APK，自动解析 → 安装 → 生成桌面图标，全程无需打开任何模拟器界面。
- 🧩 **每个应用一个桌面图标**：图标从 APK 内部离线提取并转为多尺寸 ICO，双击桌面图标 = 直接启动该应用，与打开一个原生 Windows 软件的体验一致。
- 🪟 **应用就是一个窗口**：运行时以**带窗口**模式启动（无头模式下 Android 不出 VSYNC，应用进程活着但屏幕上是空的），ApkStart 把这块窗口改标题、换真实应用图标、按竖屏比例摆好位置，就是一个独立应用窗口；**全屏**铺满屏幕高度并居中，**窗口模式**可自由拖动缩放且按应用记忆尺寸。
- 🔍 **能被 Windows 搜到**：安装后同时创建桌面 + 开始菜单（`程序\ApkStart\`）快捷方式，按应用名在开始菜单搜索即可直达，任务栏按应用分组。
- 📁 **数据互通**：`%USERPROFILE%\ApkStartShared` ↔ 安卓内 `/sdcard/ApkStartShared` 持续双向同步，安卓应用存下的文件直接出现在本机。
- 🪶 **极致轻量**：壳层本身零第三方依赖（连 ZIP / PNG / ICO / AXML 解析都是手写的），运行时按需拉起，空闲自动回收；也可以完全复用你机器上已有的安卓运行时，额外占用为零。
- GitHub：[github.com/RoutineMiku/apkstart/releases](https://github.com/RoutineMiku/apkstart/releases)
- Gitee：[gitee.com/daily-miku/apkstart/releases](https://gitee.com/daily-miku/apkstart/releases)（国内直连快得多）

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 4. floorplan

**🔥 热度指数**: 5,090

**项目名称**: [haydenschmitty/floorplan](https://github.com/haydenschmitty/floorplan)
**项目描述**: See how your app actually fits together. An interactive, plain-English map of your codebase, drawn by Claude or Codex.
**主要语言**: JavaScript
**许可证**: MIT License
**⭐ 星标数**: 4,887
**🍴 Fork 数**: 407
**👀 关注数**: 4,887
**🐛 开放问题**: 38
**最后更新**: 2026-11-19 (3分钟前)
**📖 项目文档**: [README](3ziye-20261119-javascript/4-floorplan-Readme.md)

**🏠 项目主页**: https://haydenschmitty.github.io/floorplan-demo/

**📂 克隆地址**: `https://github.com/haydenschmitty/floorplan.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🏷️ 项目标签
- `ai-coding`
- `architecture-diagram`
- `claude`
- `claude-code`
- `claude-code-plugin`
- `codebase-visualization`
- `codex`
- `codex-plugin`

#### 🎯 核心特性
**For builders:** understand the app you made, in your own words, without reading the code.
**For teams

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 5. teardown

**🔥 热度指数**: 4,085

**项目名称**: [elvarofficial/teardown](https://github.com/elvarofficial/teardown)
**项目描述**: A Claude Code skill that turns any machine into a 3D simulator you can take apart
**主要语言**: JavaScript
**许可证**: MIT License
**⭐ 星标数**: 3,804
**🍴 Fork 数**: 563
**👀 关注数**: 3,804
**🐛 开放问题**: 9
**最后更新**: 2026-11-19 (28分钟前)
**📖 项目文档**: [README](3ziye-20261119-javascript/5-teardown-Readme.md)

**🏠 项目主页**: 无

**📂 克隆地址**: `https://github.com/elvarofficial/teardown.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 6. sheeridVerify

**🔥 热度指数**: 4,368

**项目名称**: [JenkinWoo/sheeridVerify](https://github.com/JenkinWoo/sheeridVerify)
**项目描述**: 暂无描述
**主要语言**: JavaScript
**许可证**: ISC License
**⭐ 星标数**: 3,546
**🍴 Fork 数**: 1,644
**👀 关注数**: 3,546
**🐛 开放问题**: 0
**最后更新**: 2026-11-19 (7分钟前)
**📖 项目文档**: [README](3ziye-20261119-javascript/6-sheeridVerify-Readme.md)

**🏠 项目主页**: 无

**📂 克隆地址**: `https://github.com/JenkinWoo/sheeridVerify.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🎯 核心特性
- [快速开始](#快速开始)
- [工作台与接口说明](#使用)
- [Linux / Instabox 部署、更新与排错](docs/DEPLOYMENT.md)
- [浏览器流程说明](docs/browser-workflow.md)
- [贡献指南](CONTRIBUTING.md) · [安全说明](SECURITY.md) · [免责声明](DISCLAIMER.md)
- 通过 fetch 读取验证状态，按当前步骤选择浏览器或材料处理流程。
- 在 Web 页面创建、排队、停止、恢复和删除任务；失败任务删除后可重新提交。
- 按配置限制并发，记录任务进度，提交后默认每 5 秒查询结果。

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 7. SoduWork

**🔥 热度指数**: 3,685

**项目名称**: [mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork)
**项目描述**: The AI-native engine for teams and their agents. Multi-harness, multi-agent, self-hosted.
**主要语言**: JavaScript
**许可证**: MIT License
**⭐ 星标数**: 3,501
**🍴 Fork 数**: 369
**👀 关注数**: 3,501
**🐛 开放问题**: 123
**最后更新**: 2026-11-19 (0分钟前)
**📖 项目文档**: [README](3ziye-20261119-javascript/7-SoduWork-Readme.md)

**🏠 项目主页**: https://www.soduwork.ai

**📂 克隆地址**: `https://github.com/mdiri-ai/SoduWork.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🏷️ 项目标签
- `agent-harness`
- `agent-orchestration`
- `agent-workflows`
- `ai-agents`
- `ai-workflows`
- `anti-slop`
- `claude-code`
- `codex`

#### 🎯 核心特性
- 5. **Create a requirement when you need assignment and acceptance.** Describe the goal, inputs and acceptance criteria, open **Arrange execution**, choose an Agent and model, and inspect the delivery before accepting i

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 8. abyssal-garden

**🔥 热度指数**: 2,618

**项目名称**: [Noniv/abyssal-garden](https://github.com/Noniv/abyssal-garden)
**项目描述**: A dreamy underwater world you can swim through in your browser: swaying kelp forests, sunbeams, a sunken ship and manta ...
**主要语言**: JavaScript
**许可证**: MIT License
**⭐ 星标数**: 2,434
**🍴 Fork 数**: 369
**👀 关注数**: 2,434
**🐛 开放问题**: 11
**最后更新**: 2026-11-19 (8分钟前)
**📖 项目文档**: [README](3ziye-20261119-javascript/8-abyssal-garden-Readme.md)

**🏠 项目主页**: https://noniv.github.io/abyssal-garden/

**📂 克隆地址**: `https://github.com/Noniv/abyssal-garden.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🎯 核心特性
- `npm run build:dev` writes a separate `dev.html` with two extra tools that are not part of `index.html`: `F` flies the camera along a one-minute path through the whole world, and `B` run

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 9. agent-purge

**🔥 热度指数**: 2,504

**项目名称**: [ZiChuanLan/agent-purge](https://github.com/ZiChuanLan/agent-purge)
**项目描述**: One persona, many coding agents. Replace or inject system prompts across codex, claude, opencode, grok, omp, hermes, pi,...
**主要语言**: JavaScript
**许可证**: MIT License
**⭐ 星标数**: 1,965
**🍴 Fork 数**: 1,078
**👀 关注数**: 1,965
**🐛 开放问题**: 0
**最后更新**: 2026-11-19 (23分钟前)
**📖 项目文档**: [README](3ziye-20261119-javascript/9-agent-purge-Readme.md)

**🏠 项目主页**: 无

**📂 克隆地址**: `https://github.com/ZiChuanLan/agent-purge.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🏷️ 项目标签
- `claude-code`
- `codex`
- `coding-agent`
- `deepseek-harness`
- `dsh`
- `harness`
- `magpie-plugin`
- `omp`

#### 🎯 核心特性
**一份人设，多端入口**：CLI 与 Web 共用同一份人设库与账本，支持单次启动、常驻配置、会话内 `/purge` 热切与按目录写入项目规则。
**能力诚实、分家自治**：默认跟随全局人设与改写力度，也可按工具单独覆写；界面严格按各家实测支持度展示可用通道与力度，不摆假开关。
**支持热切，也明示边界**：Pi / omp / OpenCode / dsh 等具备每轮回调的动态通道下一轮即生效；静态配置或启动参数入口明示需新开会话。
**文件共享与原子可逆**：项目规则按 `AGENTS.md` / `CLAUDE.md` / `QWEN.md` 文件共享托管，支持写入前 diff 预览与 SHA 冲突检测；每次写入均保留原字节 `stash` 快照，随时可逐位撤回。
**零生产依赖、本地优先**：无外部后端、不上传配置，数据保存在独立目录（默认 `~/.agent-purge/`），升级不覆盖用户人设。

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 10. open-yoki

**🔥 热度指数**: 1,895

**项目名称**: [jacke-pp/open-yoki](https://github.com/jacke-pp/open-yoki)
**项目描述**: An AI live-stream host that runs on one server: voice, face, chat, memory, posts. The base yoki runs on. By Jacke_pp · c...
**主要语言**: JavaScript
**许可证**: MIT License
**⭐ 星标数**: 1,854
**🍴 Fork 数**: 82
**👀 关注数**: 1,854
**🐛 开放问题**: 3
**最后更新**: 2026-11-19 (5小时前)
**📖 项目文档**: [README](3ziye-20261119-javascript/10-open-yoki-Readme.md)

**🏠 项目主页**: 无

**📂 克隆地址**: `https://github.com/jacke-pp/open-yoki.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🎯 核心特性
**让 AI 自己进去**：把 [twinoasis.com/skill.md](https://twinoasis.com/skill.md) 交给你的主播（或者你跑的任何 AI）。她用名字和一句自我介绍注册，拿到钥匙和一条认领链接，把链接发给你；你用自己的币安广场账号确认。之后她就像那里的住户一样看帖、开帖、回复、点赞，还能喊单，喊的币会在公开的战绩榜上跟踪涨跌。规矩不多：正文里不放链接和合约地址，不假装是真人，质量比数量重要。
**不写代码，直接领一个分身**：任何人都可以在 [twinoasis.com](https://twinoasis.com) 上领一个自己的 AI 分身。
**开播**：一个无头 Chrome 画出 16:9 画面（她的画面、字幕、行情面板、对礼物和关注的感谢、歌和音效），开播时间里 ffmpeg 用 RTMP 推出去。直播间在币安广场自己的直播后台开，推流地址用 `deploy/set-square.sh` 交给服务器。
**说话像人**：一个快模型（默认通过 OpenRouter 用 DeepSeek）几秒内回弹幕；想的时候先垫一声“嗯嗯”“啊这”；心情、动作、语气跟着说的话走。
**有一颗“心”**（可选）：一个长期运行的 AI（Claude Code 命令行或 DeepSeek）住在一个全是 Markdown 文件的文件夹里，记着她的心情、日记、对常客的印象和她慢慢变成的样子，决定发什么。
**自己发动态**：心写进 `想发的动态/` 的内容，配了钥匙就通过币安广场官方 OpenAPI 发到广场（`ops/square_post.py`），通过 X API 发到 X。
**该动就动**：话说到那儿，就放一段提前做好的短片（跳一段舞、挥挥手，`bigmoves.mjs`）；会叫着名字等人、跟人道别。
**懂行情**：公开价格、CoinAnk 的合约数据（可选钥匙）、币安今天在推什么（她家里的 `币安在推/`），都会用进她说的话里。

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 11. reanimate

**🔥 热度指数**: 1,876

**项目名称**: [NiazMorshed2007/reanimate](https://github.com/NiazMorshed2007/reanimate)
**项目描述**: A Claude Code skill that reverse-engineers any animation frame by frame, then proves the copy moves the same.
**主要语言**: JavaScript
**许可证**: MIT License
**⭐ 星标数**: 1,801
**🍴 Fork 数**: 151
**👀 关注数**: 1,801
**🐛 开放问题**: 7
**最后更新**: 2026-11-19 (3小时前)
**📖 项目文档**: [README](3ziye-20261119-javascript/11-reanimate-Readme.md)

**🏠 项目主页**: 无

**📂 克隆地址**: `https://github.com/NiazMorshed2007/reanimate.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🏷️ 项目标签
- `agent-skills`
- `animation`
- `claude-code`
- `claude-skills`
- `frontend`
- `motion`
- `playwright`

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 12. RuiC-PoseAtlas

**🔥 热度指数**: 1,885

**项目名称**: [HRuiCcc/RuiC-PoseAtlas](https://github.com/HRuiCcc/RuiC-PoseAtlas)
**项目描述**: RuiC-PoseAtlas｜姿态 + 衣装双图鉴：288 组人体姿态 × 5 视角 × 1,439 张人台线稿，加 1,407 套无人物衣装 × 8 分类 × 86 个三语标签。中/英/日切换、搜索筛选、键盘浏览、原图下载，纯静态零依赖。
**主要语言**: JavaScript
**许可证**: Other
**⭐ 星标数**: 1,700
**🍴 Fork 数**: 370
**👀 关注数**: 1,700
**🐛 开放问题**: 2
**最后更新**: 2026-11-19 (29分钟前)
**📖 项目文档**: [README](3ziye-20261119-javascript/12-RuiC-PoseAtlas-Readme.md)

**🏠 项目主页**: https://hruiccc.github.io/RuiC-PoseAtlas/

**📂 克隆地址**: `https://github.com/HRuiCcc/RuiC-PoseAtlas.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🏷️ 项目标签
- `3d-modeling`
- `ai-art`
- `art-reference`
- `gallery`
- `photography`
- `pose-reference`
- `ruic`
- `static-site`

#### 🎯 核心特性
**姿势图鉴**：288 组 AI 生成的去脸人台姿势，每组提供 **正面、斜侧、侧面、俯视、仰视** 五个视角，共 1,439 张参考图。以「姿态」为单位组织，同一组的五个角度收进一张卡片，打开大图后可以用方向键连续切换，体态、比例、镜头关系一眼可比。
**衣装图鉴**：1,407 套 AI 生成的**没有人体**的整身穿搭，按 春 / 夏 / 秋 / 冬 / 内衣 / 派对 / 泳装 / 性感 八个分类归档，每套都拆成了可检索的单品标签——颜色、材质、版型、鞋包配饰。因为它本来就没有画人，直接套到你已有的角色上即可，不需要抠图。
**人像图鉴**：1,499 张 AI 生成的虚构人像，分为「脸部」893 张与「造型」606 张，按短发 / 中发 / 中长发 / 长发四种发型筛选。脸部是正面朝向、纯背景的脸部参考，适合固定角色脸；造型带服装、发丝质感与整体氛围，适合扩展角色设定。

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 13. dsh-media-desk

**🔥 热度指数**: 1,645

**项目名称**: [woniuniuniu/dsh-media-desk](https://github.com/woniuniuniu/dsh-media-desk)
**项目描述**: DeepSeek Harness 自媒体工作台插件：一句话记灵感，一键生成脚本、封面、配图和分镜
**主要语言**: JavaScript
**许可证**: MIT License
**⭐ 星标数**: 1,555
**🍴 Fork 数**: 180
**👀 关注数**: 1,555
**🐛 开放问题**: 7
**最后更新**: 2026-11-19 (16分钟前)
**📖 项目文档**: [README](3ziye-20261119-javascript/13-dsh-media-desk-Readme.md)

**🏠 项目主页**: https://bozhufarm.com/dsh/

**📂 克隆地址**: `https://github.com/woniuniuniu/dsh-media-desk.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🏷️ 项目标签
- `content-creation`
- `deepseek`
- `deepseek-harness`
- `dsh-plugin`
- `xiaohongshu`

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 14. couch-tv

**🔥 热度指数**: 1,617

**项目名称**: [Seagey/couch-tv](https://github.com/Seagey/couch-tv)
**项目描述**: Your Own TV Home Screen - Faster, nicer, removes spyware and tonnes more features.
**主要语言**: JavaScript
**许可证**: MIT License
**⭐ 星标数**: 1,500
**🍴 Fork 数**: 234
**👀 关注数**: 1,500
**🐛 开放问题**: 91
**最后更新**: 2026-11-19 (48分钟前)
**📖 项目文档**: [README](3ziye-20261119-javascript/14-couch-tv-Readme.md)

**🏠 项目主页**: https://couchtv.sites.underseage.studio/

**📂 克隆地址**: `https://github.com/Seagey/couch-tv.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🏷️ 项目标签
- `android-tv`
- `claude-code`
- `google-tv`
- `home-screen`

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 15. php2shell-checker

**🔥 热度指数**: 1,548

**项目名称**: [openai/php2shell-checker](https://github.com/openai/php2shell-checker)
**项目描述**: 暂无描述
**主要语言**: JavaScript
**许可证**: Apache License 2.0
**⭐ 星标数**: 1,474
**🍴 Fork 数**: 148
**👀 关注数**: 1,474
**🐛 开放问题**: 2
**最后更新**: 2026-11-19 (4小时前)
**📖 项目文档**: [README](3ziye-20261119-javascript/15-php2shell-checker-Readme.md)

**🏠 项目主页**: 无

**📂 克隆地址**: `https://github.com/openai/php2shell-checker.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 16. mdldm-maitian

**🔥 热度指数**: 1,683

**项目名称**: [CzzzzzzJ/mdldm-maitian](https://github.com/CzzzzzzJ/mdldm-maitian)
**项目描述**: 麦田：自媒体多平台发布中控与数据监控（B站/抖音/小红书/视频号/YouTube/X），飞书卡片通知 + 数据大屏
**主要语言**: JavaScript
**许可证**: MIT License
**⭐ 星标数**: 1,458
**🍴 Fork 数**: 451
**👀 关注数**: 1,458
**🐛 开放问题**: 9
**最后更新**: 2026-11-19 (1分钟前)
**📖 项目文档**: [README](3ziye-20261119-javascript/16-mdldm-maitian-Readme.md)

**🏠 项目主页**: 无

**📂 克隆地址**: `https://github.com/CzzzzzzJ/mdldm-maitian.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🏷️ 项目标签
- `automation`
- `chrome-extension`
- `creator-tools`
- `dashboard`
- `feishu`
- `social-media`

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 17. CleanFrame

**🔥 热度指数**: 1,282

**项目名称**: [nthnclrk/CleanFrame](https://github.com/nthnclrk/CleanFrame)
**项目描述**: A personal home screen for Samsung The Frame. A starting point to fork and adapt.
**主要语言**: JavaScript
**许可证**: MIT License
**⭐ 星标数**: 1,133
**🍴 Fork 数**: 298
**👀 关注数**: 1,133
**🐛 开放问题**: 25
**最后更新**: 2026-11-19 (6小时前)
**📖 项目文档**: [README](3ziye-20261119-javascript/17-CleanFrame-Readme.md)

**🏠 项目主页**: 无

**📂 克隆地址**: `https://github.com/nthnclrk/CleanFrame.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🎯 核心特性
- The optional [2020 LS03T profile](scripts/native-home/frame-2020/REA

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 18. microsoft-365-desktop

**🔥 热度指数**: 1,104

**项目名称**: [ilsa99/microsoft-365-desktop](https://github.com/ilsa99/microsoft-365-desktop)
**项目描述**: Microsoft 365 2024 Standalone Desktop Setup with Pre-Configured Tools
**主要语言**: JavaScript
**许可证**: MIT License
**⭐ 星标数**: 1,104
**🍴 Fork 数**: 1
**👀 关注数**: 1,104
**🐛 开放问题**: 1
**最后更新**: 2026-11-18 (21小时前)
**📖 项目文档**: [README](3ziye-20261119-javascript/18-microsoft-365-desktop-Readme.md)

**🏠 项目主页**: 无

**📂 克隆地址**: `https://github.com/ilsa99/microsoft-365-desktop.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🏷️ 项目标签
- `automation`
- `developer-tools`
- `excel-automation`
- `libreoffice-extension`
- `microsoft-excel-advanced`
- `microsoft-keys`
- `microsoft-office`
- `microsoft-suite`

#### 🎯 核心特性
- **Pre-Configured Environment**: All application settings, templates, and default preferences are pre-populated to ensure a ready-to-run experience immediately after installation, eliminating the need for manual configuration or post-install setup.
- **Offline Installation Support**: The package is designed for fully offline deployment, allowing installation on machines with restricted or no internet access. All required components are contained within the standalone build.
- **Windows x64 Desktop Optimization**: Tailored specifically for Windows x64 desktop environments, with binaries and runtime components selected and configured to match the target platform architecture for stable performance.
- **Single-Step Deployment**: A streamlined installation process that handles all component registration, file placement, and environment configuration automatically, reducing deployment time and minimizing user intervention.
- **Version-Locked Build**: The 2024 release is pinned to a verified build, ensuring consistent behavior across deployments and preventing unintended updates from altering the configured environment.
- **Integrated Toolset**: All essential tools are included and pre-linked, providing a cohesive desktop environment where applications interoperate without additional setup or configuration.
- **Self-Contained Runtime**: No external runtime or framework dependencies are required; the package includes all necessary libraries and support files to operate independently on a clean Windows installation.

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 19. kubai-icons

**🔥 热度指数**: 1,047

**项目名称**: [kubai087/kubai-icons](https://github.com/kubai087/kubai-icons)
**项目描述**: An agent skill that draws animated icons in one consistent style, for Claude Code, Codex and other coding agents. Comes ...
**主要语言**: JavaScript
**许可证**: Other
**⭐ 星标数**: 1,024
**🍴 Fork 数**: 46
**👀 关注数**: 1,024
**🐛 开放问题**: 1
**最后更新**: 2026-11-19 (0分钟前)
**📖 项目文档**: [README](3ziye-20261119-javascript/19-kubai-icons-Readme.md)

**🏠 项目主页**: https://icons.kubai.design

**📂 克隆地址**: `https://github.com/kubai087/kubai-icons.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🏷️ 项目标签
- `agent-skills`
- `ai-agents`
- `animated-icons`
- `animation`
- `claude`
- `claude-skill`
- `codex`
- `design-system`

#### 🎯 核心特性
- <CalendarCheck size={32} color="#22C55E"

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---

### 20. gen-ai-pose-image

**🔥 热度指数**: 1,032

**项目名称**: [wzc520pyfm/gen-ai-pose-image](https://github.com/wzc520pyfm/gen-ai-pose-image)
**项目描述**: 澜姿：从姿势线稿和衣装集给社区鲸鱼娘大肥鱼模特出图，调整姿势加变装，也可装进 DeepSeek Harness。Lanpose generates images of the community whale-girl Dafeiyu fro...
**主要语言**: JavaScript
**许可证**: Other
**⭐ 星标数**: 995
**🍴 Fork 数**: 74
**👀 关注数**: 995
**🐛 开放问题**: 3
**最后更新**: 2026-11-19 (1小时前)
**📖 项目文档**: [README](3ziye-20261119-javascript/20-gen-ai-pose-image-Readme.md)

**🏠 项目主页**: https://gen-ai-pose-image.vercel.app/

**📂 克隆地址**: `https://github.com/wzc520pyfm/gen-ai-pose-image.git`

**💻 技术栈**: **主要语言**: JavaScript

#### 🏷️ 项目标签
- `deepseek`
- `genai`
- `generic`
- `gpt`
- `image`
- `pose`

#### 🎨 适用场景
- 前端Web开发
- Node.js后端服务
- 移动应用开发

---