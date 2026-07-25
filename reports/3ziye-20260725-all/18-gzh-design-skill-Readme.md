> 🤝 **本项目由 甲木 × [「摸鱼小李」](https://mp.weixin.qq.com/s/EMahAzgfAbRQrYukWE7_IQ) 联名共建** —— 排版组件、主题设计与质量标准凝聚了两人的公众号实践与共同打磨，特别感谢小李。

<div align="center">

# gzh-design-skill · 公众号排版技能

**把 Markdown 一键排成可直接粘贴进微信公众号编辑器的精致 HTML**

6 套精选主题 + 主题生成器 · 代码块/图片/GIF · 自动章节编号与关键词标记 · 双关卡质量校验

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-blue.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blue)](https://claude.ai/code)
[![Themes](https://img.shields.io/badge/themes-6%20+%20generator-059669)](references/theme-index.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Agents](https://img.shields.io/badge/Claude%20Code%20·%20Codex%20·%20Cursor-supported-8b5cf6.svg)](#-快速开始)

[English](README.en.md) ｜ 中文

</div>

---

一个给 AI Agent（Claude Code / Codex / Cursor 等）用的公众号排版 Skill。你写完 Markdown，它按你选的主题，生成**样式全内联、粘贴到公众号编辑器不掉格式**的 HTML——自动编章节号、标关键词下划线、配引言卡与目录、处理代码块和图片、合并作者签名，并用脚本确定性地兜住公众号平台的各种限制。

## ✨ 核心特性

- **6 套精选主题**：摸鱼绿（默认）· 红白 · 石墨极简 · 留白禅意 · 摸鱼票据 · 橄榄手记 —— 每套都是自成体系的厚组件库（设计变量 + 数十个精细组件 + 视觉层级表 + 文章类型配方表）。
- **主题生成器**：不满足现成主题？用一句话描述或一张参考图，生成一套全新组件库并保存本地复用（见 `references/theme-generator.md`）。
- **内容全兼容**：代码块（深/浅色，等宽不折行）、图片、GIF（带动图角标）、行内代码、引用、列表、产品徽章。
- **智能排版**：章节自动编号（末章 ∞ / ///）、每段主动标 1–3 个关键词下划线、从正文提炼引言卡与目录、作者签名去重合并。
- **中文全角标点**：正文自动规范全角，代码块内原样保留。
- **不掉格式**：所有样式内联、文字 `<span leaf="">` 包裹，规避 `<style>/<div>/class/grid/position` 等公众号会过滤的写法。
- **双关卡质量校验**：`component_lint.py`（组件库源头）+ `validate_gzh_html.py`（最终产物），构成可复现的「改→验→修」闭环。
- **一键复制**：生成带「复制」按钮的预览页，点一下把富文本复制到剪贴板，直接粘进公众号，免手动全选。

## 👀 效果预览

6 套主题各排同一篇长文（真实长图，含配图、引言卡、编号章节、金句、名词旁注等完整组件）：

<table>
<tr>
<td colspan="3" align="center"><img src="https://origin.picgo.net/2026/07/07/-40619312d679bc34.jpg" width="100%"><br><sub><b>摸鱼绿（默认）</b></sub></td>
</tr>
<tr>
<td colspan="3" align="center"><img src="https://origin.picgo.net/2026/07/07/-084eb2b9d6f8d5e2.jpg" width="100%"><br><sub><b>红白色系</b></sub></td>
</tr>
<tr>
<td colspan="3" align="center"><img src="https://origin.picgo.net/2026/07/07/-747b33f502544254.jpg" width="100%"><br><sub><b>橄榄手记</b></sub></td>
</tr>
<tr>
<td width="33%" align="center"><img src="https://github.com/isjiamu/gzh-design-skill/releases/download/assets-v1/lf-graphite-minimal.png?v=1" width="250"><br><sub><b>石墨极简风</b></sub></td>
<td width="33%" align="center"><img src="https://github.com/isjiamu/gzh-design-skill/releases/download/assets-v1/lf-zen-whitespace.png?v=1" width="250"><br><sub><b>留白禅意风</b></sub></td>
<td width="33%" align="center"><img src="https://github.com/isjiamu/gzh-design-skill/releases/download/assets-v1/lf-moyu-ticket.png?v=1" width="250"><br><sub><b>摸鱼票据风</b></sub></td>
</tr>
</table>

> 📚 **6 套完整长图 → [docs/all-themes.md](docs/all-themes.md)**　｜　克隆后浏览器打开 `docs/gallery/index.html` 可看可交互的完整 HTML。

## ✅ 适合 / ❌ 不适合

**✅ 适合**：观点/深度分析 · 教程/操作指南 · 测评/工具盘点 · 知识整理/方法论 · 访谈/人物特稿 · 数据复盘/报告 · 生活/情感随笔 · 案例实战 —— 把 Markdown / Word / PDF / 纯文本长文，一键排成可直接粘进公众号编辑器的 HTML；也能按描述或参考图生成自定义主题。

**❌ 不适合**：普通网页/落地页（用前端 skill）· PPT（用 PPT skill）· 纯图片海报/社交卡片（用社交卡片类 skill）· 非公众号平台的排版 · **代写文章**（本 skill 只排版、不写作——先有 Markdown 再用它）。

## 🗂 常见使用场景

| 你的内容 | 推荐怎么排 |
|---|---|
| 观点 / 深度长文 | 红白 或 石墨极简；关键词下划线 + 金句引用 + 居中金句 |
| 产品测评 / 工具盘点 | 摸鱼绿 或 摸鱼票据；step/tool-label + 卡片，按配方表走 |
| 教程 / 操作指南 | 摸鱼绿；step-label + 代码块 + 编号列表 |
| 数据复盘 / 年度报告 | 摸鱼绿 或 橄榄手记；数据卡 + 表格 |
| 禅意 / 极简随笔 | 留白禅意；大留白 + 居中衬线引用 |
| 内刊 / 深度评测 / 案例复盘 | 橄榄手记；编者按 + 分节 + 暗色摘要框 |
| Word / PDF 稿转公众号 | 先自动格式归一化 → 再按题材选主题 |
| 想要现成之外的风格 | 主题生成器：一句话或参考图现造一套 |

## 🎨 6 套精选主题

覆盖绝大多数公众号题材，每套都打磨到「拿来即用」：

| 主题 | 适合 |
|---|---|
| **摸鱼绿**（默认） | 教程、测评、清单、工具盘点（卡片丰富、信息密度高） |
| **红白色系** | 深度分析、观点、力量感话题（经典编辑风） |
| **石墨极简风** | 设计、科技评论、专业观点、高端品牌 |
| **留白禅意风** | 禅意、极简生活、深度随笔（呼吸感最强） |
| **摸鱼票据风** | 工具对比、创意评测（票据视觉隐喻） |
| **橄榄手记** | 内刊手记、深度评测、案例复盘（编辑部内刊质感） |

> 主色、下划线色值等**完整速查表见文末 [附录](#-完整主题速查表)**；不够用就让 AI [生成新主题](#-faq)。

## 🚀 快速开始

### 方式一：一行安装（推荐）

```bash
npx skills add https://github.com/isjiamu/gzh-design-skill
```

### 方式二：让 AI 自己装

对**任意 Agent**（Claude Code / Codex / Cursor 等）说一句：

> 请帮我查找并自动安装 https://github.com/isjiamu/gzh-design-skill 这个 skill

它会自行 clone 到对应的 skills 目录并接入。

### 方式三：手动 clone

```bash
git clone https://github.com/isjiamu/gzh-design-skill.git ~/.claude/skills/gzh-design
```

装好后，直接对 Agent 说：

> 用摸鱼绿把这篇文章排成公众号 HTML：`article.md`

## 💬 交流群

扫码加入**官方企业微信交流群**（活码自动邀请入群，一起交流公众号排版 & Agent Skills 玩法）：

<img src="https://github.com/isjiamu/gzh-design-skill/releases/download/assets-v1/group-qr.png" width="220" alt="企业微信交流群二维码">

> 扫码失效？加作者微信 **`zuiyn_soul`**（备注「gzh-design」）拉你进群。

## 📖 使用流程

1. **选主题** — 按题材自动推荐最契合的主题并请你一步确认（默认摸鱼绿）；也可直接指定，或让 AI 生成新主题。
2. **读组件库** — 读所选主题库 + 通用增量库（代码块/图片/小标签）。
3. **解析 Markdown** — 识别标题、章节、加粗、高亮、引用、图片、代码块、列表。
4. **装配 HTML** — 用组件库里的真实组件拼装，落实编号、下划线、全角、签名。
5. **校验** — 跑 `validate_gzh_html.py`，ERROR 清零才交付。
6. **输出** — 生成干净正文 + 带「复制」按钮的预览页；浏览器打开预览页点右上角「复制到公众号」，再去编辑器粘贴即可（免手动全选）。

## 🧩 公众号平台限制（已内置兜底）

生成的 HTML 严格遵守：禁 `<style>/<script>/<div>`、`class/id`、`position:fixed/absolute/sticky`、`float`、`@media/@keyframes`