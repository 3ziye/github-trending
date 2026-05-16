# Guizang PPT Skill · 网页 PPT / 配图 / 封面

![GitHub stars](https://img.shields.io/github/stars/op7418/guizang-ppt-skill?style=flat-square)
![License](https://img.shields.io/github/license/op7418/guizang-ppt-skill?style=flat-square)
![Skill](https://img.shields.io/badge/Skill-Agent-111111?style=flat-square)
![HTML Deck](https://img.shields.io/badge/HTML-Deck-0A7CFF?style=flat-square)
![Claude Code](https://img.shields.io/badge/Claude%20Code-Supported-6B5B95?style=flat-square)
![Codex](https://img.shields.io/badge/Codex-Supported-222222?style=flat-square)
[![由真格 Token Grant 资助](https://img.shields.io/static/v1?label=%E7%94%B1%E7%9C%9F%E6%A0%BC%20Token%20Grant&message=%E8%B5%84%E5%8A%A9&color=FF4D00&style=flat-square)](https://zhenfund.feishu.cn/share/base/form/shrcn1lAANF659o7EpWnxlR1VOh?sessionid=)

> 🌏 **English version: [README.en.md](./README.en.md)**

一个适配 Claude Code / Codex 等 Agent 环境的网页 PPT 技能,用于生成**单文件 HTML 横向翻页 PPT**、PPT 配图和多平台封面。

内置两套视觉系统:

- **Style A: 电子杂志 × 电子墨水**。像 *Monocle* 贴上了代码,适合叙事、观点、分享、个人风格表达。
- **Style B: 瑞士国际主义**。网格至上、单一高饱和锚点色、直角、发丝线、极致字号对比,适合事实、产品、分析、方法论表达。

> 由 [歸藏](https://x.com/op7418) 在"一人公司:被 AI 折叠的组织"、"一种新的工作方式"等线下分享中沉淀而成,踩过的每一个坑都写进了 `checklist.md`。

**旧主题 · Style A 电子杂志风**

![Style A 电子杂志风效果展示](https://github.com/user-attachments/assets/5dc316a2-401c-4e37-9123-ea081b6ae470)

**新主题 · Style B 瑞士国际主义**

![Style B 瑞士国际主义效果展示](https://github.com/user-attachments/assets/8960e78c-69bb-4b7e-aa95-6fad64b70314)

## 30 秒开始

```bash
npx skills add https://github.com/op7418/guizang-ppt-skill --skill guizang-ppt-skill
```

也可以直接把这段话发给有 shell 权限的 AI Agent:

```text
帮我安装 guizang-ppt-skill。请把 https://github.com/op7418/guizang-ppt-skill 克隆到 ~/.claude/skills/guizang-ppt-skill,安装完成后检查 SKILL.md、assets/、references/ 是否存在。
```

已经安装过的话,用这段话更新:

```text
帮我更新 guizang-ppt-skill。请进入 ~/.claude/skills/guizang-ppt-skill 执行 git pull,然后告诉我当前最新 commit。
```

安装后直接对 Agent 说:

```text
帮我基于这篇文章做一份瑞士风 PPT,控制在 7 页左右,需要 2-3 张配图。
```

也可以试这些请求:

```text
帮我把这份 Markdown 做成杂志风演讲 PPT。
基于这份 PPT 的核心观点,生成一张公众号 21:9 头图。
把这张产品截图重新设计成适合 PPT 的 16:10 配图。
```

## 效果

- 🖋 **双视觉系统**:电子杂志风负责叙事,瑞士风负责事实表达
- 📐 **横向左右翻页**:键盘 ← → / 滚轮 / 触屏滑动 / 底部圆点 / ESC 索引
- 🧩 **Style A 10 种布局**:封面、章节、数据大字报、图文、图片网格、Pipeline、对比等
- 🧱 **Style B 22 种锁定版式**:Cover、Statement、KPI Tower、Loop Diagram、Duo Compare、Image Hero、Closing Manifesto 等
- 🎨 **主题色预设**:Style A 5 套电子墨水主题,Style B 4 套瑞士高饱和锚点色
- 🖼 **Codex 可选配图流程**:可用 GPT-Image 2.0 / GPT-M 2.0 生成纪实照片、信息图、流程图、系统关系图、UI 情景图,并按模板比例插入
- 📰 **多平台封面**:可用同一套视觉规则生成公众号 21:9、公众号分享卡 1:1、小红书 3:4、视频号横版等封面
- 📴 **低性能静态模式**:按 `B` 可关闭 WebGL / canvas 动画,让动态内容退回静态背景
- 📄 **单文件 HTML**:不需要构建、不需要服务器,浏览器直接打开

## 适合 / 不适合

**✅ 合适**:线下分享 / 行业内部讲话 / 私享会 / AI 产品发布 / demo day / 带强烈个人风格的演讲

**❌ 不合适**:大段表格数据 / 培训课件(信息密度不够)/ 需要多人协作编辑(静态 HTML)

## 常见使用场景

| 任务 | 推荐方式 |
|------|---------|
| 长文章变演讲 PPT | 先抽核心观点,再按 6-10 页节奏生成 deck |
| 方法论 / 产品分析 | 用 Style B 瑞士风,优先使用锁定版式和 21:9 主图 |
| 个人分享 / 观点表达 | 用 Style A 电子杂志风,保留更强叙事感 |
| PPT 配图 | 在 Codex 中用 GPT-Image 2.0 / GPT-M 2.0 生成照片、信息图、流程图、UI 情景图 |
| 多平台封面 | 从同一份内容生成公众号 21:9、1:1 分享卡、小红书 3:4、视频号横版封面 |
| 截图统一风格 | 把原始截图重新生成到模板需要的比例,再插入 PPT |

## 为什么是 HTML PPT

- **更适合 Agent 生成和修改**:HTML / CSS 是文本,Agent 能直接读、改、验证。
- **表现力比 Markdown 更高**:可以做精细排版、空间定位、动画、交互和响应式封面。
- **交付更轻**:单文件 HTML 可以直接打开、演示、发送、截图。
- **更容易做质量控制**:瑞士风可以用脚本校验版式、图片槽位、标题对齐和危险 SVG。
- **更适合视觉内容链路**:同一套主题能覆盖 PPT、配图、封面和截图再设计。

## 平台支持

| 平台 | 状态 | 说明 |
|------|------|------|
| Claude Code | 支持 | 原生 Skill 工作流,适合生成和迭代 HTML deck |
| Codex | 支持 | 适合生成 PPT、调用图片生成能力、做浏览器视觉检查 |
| Cursor / 其他本地 Agent | 可用 | 需要能读写文件并执行 shell 命令 |
| WorkBuddy | 适配中 | 单独整理上架版本,去掉平台不需要的渠道差异 |
| 普通 Chatbot | 不推荐 | 没有文件系统和浏览器预览时,很难稳定生成完整 deck |

## 安装

### 方式一:一行命令安装(推荐)

```bash
npx skills add https://github.com/op7418/guizang-ppt-skill --skill guizang-ppt-skill
```

### 方式二:把下面这段话直接发给 AI

> 帮我安装 `guizang-ppt-skill` 这个 Claude Code skill。请按下面步骤做:
>
> 1. 确保 `~/.claude/skills/` 目录存在(不存在就创建)
> 2. 执行 `git clone https://github.com/op7418/guizang-ppt-skill.git ~/.claude/skills/guizang-ppt-skill`
> 3. 验证:`ls ~/.claude/skills/guizang-ppt-skill/` 应该看到 `SKILL.md`、`assets/`、`references/` 三项
> 4. 告诉我安装好了,之后我说"做一份杂志风 PPT"之类的话就会触发这个 skill

把这段话复制粘贴给 Claude Code / Cursor / 任何有 shell 权限的 AI Agent,它会自动完成安装。

### 方式三:手动命令行

```bash
git clone https://github.com/op7418/guizang-ppt-skill.git ~/.claude/skills/guizang-ppt-skill
```

### 触发方式

装好后,Claude Code 会在对话里自动发现并调用这个 skill。触发关键词:

- "帮我做一份杂志风 PPT"
- "帮我做一份瑞士风 PPT"
- "生成一个 horizontal swipe deck"
- "editorial magazine style presentation"
- "electronic ink 风格演讲 slides"
- "基于这篇文章做一张公众号 21:9 封面"
- "基于这份 PPT 生成一张 1:1 分享卡"

## 使用流程

Skill 本身是结构化工作流,Agent 会逐步引导:

1. **选择风格** — Style A 电子杂志风,或 Style B 瑞士国际主义
2. **需求澄清** — 7 问清单:风格、受众、时长、素材、图片/截图需求、主题色、硬约束
3. **拷贝模板** — Style A 用 `assets/template.html`,Style B 用 `assets/template-swiss.html`
4. **填充内容** — 先做主题节奏表,再从对应 layout 骨架里挑、粘、改文案
5. **可选配图** — 在 Codex 中询问是否用 GPT-Image 2.0 / GPT-M 2.0 生成配图,再按页面比例插入
6. **自检** — 对照 `references/checklist.md`,P0 级问题必须全过；瑞士风还要运行版式校验器
7. **预览** — 浏览器直接打开
8. **迭代** — inline style 改字号/高