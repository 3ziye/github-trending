<sub>🌐 <a href="README.en.md">English</a> · <b>中文</b></sub>

<div align="center">

# Huashu Design

> *「打字。回车。一份能交付的设计。」*
> *"Type. Hit enter. A finished design lands in your lap."*

[![License](https://img.shields.io/badge/License-Personal%20Use%20Only-orange.svg)](LICENSE)
[![Agent-Agnostic](https://img.shields.io/badge/Agent-Agnostic-blueviolet)](https://skills.sh)
[![Skills](https://img.shields.io/badge/skills.sh-Compatible-green)](https://skills.sh)

<br>

**在你的 agent 里打一句话，拿回一份能交付的设计。**

<br>

3 到 30 分钟，你能 ship 一段**产品发布动画**、一个能点击的 App 原型、一套能编辑的 PPT、一份印刷级的信息图。

不是「AI 做的还行」那种水平——是看起来像大厂设计团队做的。给 skill 你的品牌资产（logo、色板、UI 截图），它会读懂你的品牌气质；什么都不给，内置的 20 种设计语汇也能兜底到不出 AI slop。

**你看到这篇 README 里的每一个动画，都是 huashu-design 自己做的。** 不是 Figma，不是 AE，就是一句话 prompt + skill 跑通。下次产品发布要做宣传片？现在你也能做。

```
npx skills add alchaincyf/huashu-design
```

跨 agent 通用——Claude Code、Cursor、Codex、OpenClaw、Hermes 都能装。

[看效果](#demo-画廊) · [安装](#装上就能用) · [能做什么](#能做什么) · [核心机制](#核心机制) · [和 Claude Design 的关系](#和-claude-design-的关系)

</div>

---

<p align="center">
  <img src="https://github.com/alchaincyf/huashu-design/releases/download/v2.0/hero-animation-v10-en.gif" alt="huashu-design Hero · 打字 → 选方向 → 画廊展开 → 聚焦 → 品牌显形" width="100%">
</p>

<p align="center"><sub>
  ▲ 25 秒 · Terminal → 4 方向 → Gallery ripple → 4 次 Focus → Brand reveal<br>
  👉 <a href="https://www.huasheng.ai/huashu-design-hero/">访问带音效的 HTML 互动版</a> ·
  <a href="https://github.com/alchaincyf/huashu-design/releases/download/v2.0/hero-animation-v10-en.mp4">下载 MP4（含 BGM+SFX · 10MB）</a>
</sub></p>

---

## 装上就能用

```bash
npx skills add alchaincyf/huashu-design
```

然后在 Claude Code 里直接说话：

```
「做一份 AI 心理学的演讲 PPT，推荐 3 个风格方向让我选」
「做个 AI 番茄钟 iOS 原型，4 个核心屏幕要真能点击」
「把这段逻辑做成 60 秒动画，导出 MP4 和 GIF」
「帮我对这个设计做一个 5 维度评审」
```

没有按钮、没有面板、没有 Figma 插件。

---

## Star 趋势

<p align="center">
  <a href="https://star-history.com/#alchaincyf/huashu-design&Date">
    <img src="https://api.star-history.com/svg?repos=alchaincyf/huashu-design&type=Date" alt="huashu-design Star History" width="80%">
  </a>
</p>

---

## 能做什么

| 能力 | 交付物 | 典型耗时 |
|------|--------|----------|
| 交互原型（App / Web） | 单文件 HTML · 真 iPhone bezel · 可点击 · Playwright 验证 | 10–15 min |
| 演讲幻灯片 | HTML deck（浏览器演讲）+ 可编辑 PPTX（文本框保留） | 15–25 min |
| 时间轴动画 | MP4（25fps / 60fps 插帧）+ GIF（palette 优化）+ BGM | 8–12 min |
| 设计变体 | 3+ 并排对比 · Tweaks 实时调参 · 跨维度探索 | 10 min |
| 信息图 / 可视化 | 印刷级排版 · 可导 PDF/PNG/SVG | 10 min |
| 设计方向顾问 | 5 流派 × 20 种设计哲学 · 推荐 3 方向 · 并行生成 Demo | 5 min |
| 5 维度专家评审 | 雷达图 + Keep/Fix/Quick Wins · 可操作修复清单 | 3 min |

---

## Demo 画廊

### 设计方向顾问

模糊需求时的 fallback：从 5 流派 × 20 种设计哲学里挑 3 个差异化方向，并行生成 3 个 Demo 让你选。

<p align="center"><img src="https://github.com/alchaincyf/huashu-design/releases/download/v2.0/w3-fallback-advisor.gif" width="100%"></p>

### iOS App 原型

iPhone 15 Pro 精确机身（灵动岛 / 状态栏 / Home Indicator）· 状态驱动多屏切换 · 真图从 Wikimedia/Met/Unsplash 取 · Playwright 自动点击测试。

<p align="center"><img src="https://github.com/alchaincyf/huashu-design/releases/download/v2.0/c1-ios-prototype.gif" width="100%"></p>

### Motion Design 引擎

Stage + Sprite 时间片段模型 · `useTime` / `useSprite` / `interpolate` / `Easing` 四 API 覆盖所有动画需求 · 一条命令导出 MP4 / GIF / 60fps 插帧 / 带 BGM 的成片。

<p align="center"><img src="https://github.com/alchaincyf/huashu-design/releases/download/v2.0/c3-motion-design.gif" width="100%"></p>

### HTML Slides → 可编辑 PPTX

HTML deck 浏览器演讲 · `html2pptx.js` 读 DOM 的 computedStyle 逐元素翻译成 PowerPoint 对象 · 导出的是**真文本框**，PPT 里双击即可编辑。

<p align="center"><img src="https://github.com/alchaincyf/huashu-design/releases/download/v2.0/c2-slides-pptx.gif" width="100%"></p>

### Tweaks · 实时变体切换

配色 / 字型 / 信息密度等参数化 · 侧边面板切换 · 纯前端 + `localStorage` 持久化 · 刷新不丢。

<p align="center"><img src="https://github.com/alchaincyf/huashu-design/releases/download/v2.0/c4-tweaks.gif" width="100%"></p>

### 信息图 / 数据可视化

杂志级排版 · CSS Grid 精准分栏 · `text-wrap: pretty` 排印细节 · 真数据驱动 · 可导 PDF 矢量 / PNG 300dpi / SVG。

<p align="center"><img src="https://github.com/alchaincyf/huashu-design/releases/download/v2.0/c5-infographic.gif" width="100%"></p>

### 5 维度专家评审

哲学一致性 · 视觉层级 · 细节执行 · 功能性 · 创新性 各 0–10 分 · 雷达图可视化 · 输出 Keep / Fix / Quick Wins 清单。

<p align="center"><img src="https://github.com/alchaincyf/huashu-design/releases/download/v2.0/c6-expert-review.gif" width="100%"></p>

### Junior Designer 工作流

不闷头做大招：先写 assumptions + placeholders + reasoning，尽早 show 给你，再迭代。理解错了早改比晚改便宜 100 倍。

<p align="center"><img src="https://github.com/alchaincyf/huashu-design/releases/download/v2.0/w2-junior-designer.gif" width="100%"></p>

### 品牌资产协议 5 步硬流程

涉及具体品牌时强制执行：问 → 搜 → 下载（三条兜底）→ grep 色值 → 写 `brand-spec.md`。

<p align="center"><img src="https://github.com/alchaincyf/huashu-design/releases/download/v2.0/w1-brand-protocol.gif" width="100%"></p>

---

## Showcase · 真实案例

### 「聊聊 skill」 · PM after-party 演讲 deck

> **Live demo · [https://skill-huasheng.vercel.app](https://skill-huasheng.vercel.app)**

13 页 HTML deck，**全部用 huashu-design 完成**：

- 黑底极简衬线视觉系统（cover / about / hook / what / why / closing）
- 2 个带 BGM +