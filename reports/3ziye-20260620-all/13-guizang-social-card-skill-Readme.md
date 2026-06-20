# Guizang Social Card Skill · 小红书图文 / 公众号封面对

![GitHub stars](https://img.shields.io/github/stars/op7418/guizang-social-card-skill?style=flat-square)
![License](https://img.shields.io/github/license/op7418/guizang-social-card-skill?style=flat-square)
![Skill](https://img.shields.io/badge/Skill-Agent-111111?style=flat-square)
![Social Cards](https://img.shields.io/badge/Social-Cards-FF4D6D?style=flat-square)
![Claude Code](https://img.shields.io/badge/Claude%20Code-Supported-6B5B95?style=flat-square)
![Codex](https://img.shields.io/badge/Codex-Supported-222222?style=flat-square)

[English README](./README.en.md)

一个适配 Claude Code / Codex 等 Agent 环境的图文卡片技能,用于从文章、文案、截图、产品笔记、字幕或照片生成**小红书 / Rednote 图文组图**与**公众号 21:9 + 1:1 封面对**。

内置两套视觉系统,共用一份图文工作流:

- **电子杂志风(Editorial)**。像 *Monocle* / *Kinfolk* / *Cereal* 那样克制的版面,适合叙事、生活方式、旅行、阅读、影视、个人观察。
- **瑞士国际主义(Swiss)**。网格、单一锚点色、直角发丝线、极致字号对比,适合产品测评、数据、方法论、教程、AI 工具。

> 这个 Skill 是 [guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) 的姊妹项目,共享美学语言但独立维护。PPT 解决"横向翻页演讲",这里解决"静态信息流图文"。

![Guizang Social Card Skill 效果展示](https://github.com/user-attachments/assets/d370abcc-1fc4-4de1-903a-09020a6556ce)

## 30 秒开始

```bash
npx skills add https://github.com/op7418/guizang-social-card-skill --skill guizang-social-card-skill
```

也可以直接把这段话发给有 shell 权限的 AI Agent:

```text
帮我安装 guizang-social-card-skill。请把 https://github.com/op7418/guizang-social-card-skill 克隆到 ~/.claude/skills/guizang-social-card-skill,安装完成后检查 SKILL.md、assets/、references/ 是否存在。
```

已经安装过的话,用这段话更新:

```text
帮我更新 guizang-social-card-skill。请进入 ~/.claude/skills/guizang-social-card-skill 执行 git pull,然后告诉我当前最新 commit。
```

安装后直接对 Agent 说:

```text
帮我基于这篇文章做一套瑞士风小红书图文,5 张,IKB 蓝。
```

也可以试这些请求:

```text
基于这份产品测评做一套小红书 3:4,标题用电子杂志风。
帮我把这篇文章做成公众号封面对:21:9 头图 + 1:1 分享卡,视觉保持一致。
我有 3 张露营照片,帮我做一套全图风格的小红书图文。
把这段游戏攻略文案做成一套小红书图文,需要从 wallhaven 拿点游戏原画。
```

## 效果

- 🖋 **双视觉系统**:电子杂志风做氛围与叙事,瑞士风做事实与结构,两套共用同一份工作流
- 📐 **3 个画板尺寸**:`.poster.xhs` 1080×1440(小红书 3:4)、`.poster.wide` 2100×900(公众号 21:9)、`.poster.square` 1080×1080(公众号 1:1)
- 🧩 **28 个版式骨架**:Editorial 16 个(`M01-M16`,含 Image-Led Cover、Pipeline、Before/After 等)+ Swiss 12 个(`S01-S12`,含 KPI Tower、H-Bar Chart、Matrix + Hero 等)
- 🎨 **10 套主题预设**:Editorial 6 套(墨水经典、靛蓝瓷、森林墨、牛皮纸、沙丘、**Midnight Ink** 暗色)+ Swiss 4 套锚点色(IKB Klein Blue、柠檬黄、柠檬绿、安全橙)
- 🖼 **图源工作流**:用户图优先;无图时按 Unsplash → Pexels → Flickr CC → Wallhaven → 直接搜索的优先级取图,落本地 + 自动写 `SOURCES.md`
- 🌫 **WebGL 墨流背景**:杂志风 hero 页可挂动态墨流;低性能或截图时可禁用
- 🪧 **图片底图遮罩 + 人脸避让**:满铺图必须叠遮罩,文字落点要避开主体,`references/image-overlay.md` 给硬规则
- 🧰 **截图美化资产**:9 张 WebP 真实材质背景(Editorial 5 / Swiss 4),配套 `.frame-shot` / `.device-browser` / `.device-phone` 工具类
- 🗺 **地图组件**:MapLibre + OSM 真实瓦片,支持多 pin + 连线,适合旅行攻略
- ✅ **校验脚本**:`validate-social-deck.mjs` 自动检测溢出、字号上限、4 横带密度、footer 碰撞
- 📄 **单文件 HTML + Playwright 渲染**:不需要前端构建链,`node render.mjs` 直接出 PNG

## 适合 / 不适合

**✅ 合适**:小红书图文组图 / 公众号封面对 / 微信朋友圈封面 / 视频号封面 / 文章配图 / 教程拆页 / 数据回顾 / 旅行攻略 / 产品测评 / 截图说明

**❌ 不合适**:横向翻页 PPT(用 [guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill))/ 长视频生成 / 纯图片修图 / 无版式诉求的纯文字编辑

## 11 个小红书品类适配

按"能力圈"分三档,详见 [`references/category-cookbook.md`](./references/category-cookbook.md):

**端到端强势**(文 / 结构 / 图都在能力圈内):

- 旅行、职场、推荐(指定子类后)

**文与结构强势,图依赖用户或搜图源:**

- 游戏、影视、美食(食谱方向)、彩妆(教程方向)、健身、家居、穿搭(精选方向)

**能力圈外,主动说清**(不强行接):

- OOTD 实拍流 / 梦核 / 仿胶片调色 / 真实测肤美妆等强烈依赖摄影或后期的细分赛道

## 常见使用场景

| 任务 | 推荐方式 |
|------|---------|
| 长文章 → 小红书图文 | 抽核心观点,Editorial 走叙事节奏,Swiss 走拆条数据 |
| 产品测评 / 工具回顾 | Swiss + IKB 蓝,优先 `S09 KPI Tower` / `S10 H-Bar Chart` |
| 旅行 / 生活方式分享 | Editorial + Midnight Ink 或 Dune,`M16 Image-Led Cover` 满铺主图 |
| 公众号封面对 | 同一份内容渲两块:`.poster.wide` 21:9 + `.poster.square` 1:1,视觉一致 |
| 截图教程 / 工具说明 | `.frame-shot` + `.device-browser` 包壳,优先 Swiss 网格底 |
| 游戏攻略 / 影视回顾 | Editorial + Midnight Ink,从 Wallhaven 取游戏原画做满铺 |
| 数据回顾 / 年终总结 | Swiss + Lemon 或 Safety Orange,矩阵 + ledger 组合 |

## 为什么是单文件 HTML 渲 PNG

- **Agent 友好**:HTML + CSS 是文本,Agent 能直接写、读、改、验证
- **版式精确**:CSS Grid + 严格字号 / 留白 / 网格,远超 Markdown 排版能力
- **图源开放**:可以接 Unsplash / Pexels / Wallhaven / Mapbox / OSM 等任意网络资源
- **质量可校验**:`validate-social-deck.mjs` 用 Playwright 跑真实 DOM 测量,不是猜
- **交付简单**:`output/*.png` 直接发,不需要部署、不需要导出工具

## 平台支持

| 平台 | 状态 | 说明 |
|------|------|------|
| Claude Code | 支持 | 原生 Skill 工作流,适合生成 + 迭代图文 |
| Codex | 支持 | 适合长流程图文生成、调用图片源、做视觉检查 |
| Cursor / 其他本地 Agent | 可用 | 需要能读写文件 + 执行 shell |
| 普通 Chatbot | 不推荐 | 没有文件系统和渲染管线时无法稳定出图 |

## 安装

### 方式一:一行命令安装(推荐)

```bash
npx skills add https://github.com/op7418/guizang-social-card-skill --skill guizang-social-card-skill
```

### 方式二:把下面这段话直接发给 AI

> 帮我安装 `guizang-social-card-skill` 这个 Claude Code skill。请按下面步骤做:
>
> 1. 确保 `~/.claude/skills/` 目录存在(不存在就创建)
> 2. 执行 `git clone https://github.com/op7418/guizang-social-card-skill.git ~/.claude/skills/guizang-social-card-skill`
> 3. 验证:`ls ~/.claude/skills/guizang-social-card-skill/` 应该看到 `SKILL.md`、`assets/`、`references/` 三项
> 4. 告诉我装好了,之后我说"做一套小红书图文"之类的话就会触发这个 skill

把这段话复制粘贴给 Claude Code / Cursor / 任何有 shell 权限的 AI Agent,它会自动完成安装。

### 方式三:手动命令行

``