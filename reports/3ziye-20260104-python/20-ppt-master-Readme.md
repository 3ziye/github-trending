# PPT Master - AI 驱动的多格式 SVG 内容生成系统

[![Version](https://img.shields.io/badge/version-v1.0.0-blue.svg)](./VERSION)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/hugohe3/ppt-master.svg)](https://github.com/hugohe3/ppt-master/stargazers)

[English](./README_EN.md) | 中文

一个基于 AI 的智能视觉内容生成系统，通过多角色协作，将源文档转化为高质量的 SVG 内容，**支持演示文稿、社交媒体、营销海报等多种格式**。

> 🎴 **在线示例**：[GitHub Pages 在线预览](https://hugohe3.github.io/ppt-master/) - 查看实际生成效果

> 🎬 **快速示例**：[YouTube](https://www.youtube.com/watch?v=jM2fHmvMwx0) | [Bilibili](https://www.bilibili.com/video/BV1iUmQBtEGH/) - 观看视频演示

---

## 🚀 快速使用指南

### 推荐工具

| 工具 | 推荐度 | 说明 |
|------|:------:|------|
| **[Antigravity](https://antigravity.dev/)** | ⭐⭐⭐ | **强烈推荐**！免费使用 Opus 4.5，集成 Banana 生图功能，可直接在仓库里生成配图 |
| [Cursor](https://cursor.sh/) | ⭐⭐ | 主流 AI 编辑器，支持多种模型 |
| [VS Code + Copilot](https://code.visualstudio.com/) | ⭐⭐ | 微软官方方案 |
| [Claude Code](https://claude.ai/) | ⭐⭐ | Anthropic 官方 CLI 工具 |

> 💡 **AI 生成图片建议**：如需 AI 生成配图，建议在 [Gemini](https://gemini.google.com/) 中生成后选择 **Download full size** 下载，分辨率比 Antigravity 直接生成的更高。Gemini 生成的图片右下角会有星星水印，可使用 [gemini-watermark-remover](https://github.com/journey-ad/gemini-watermark-remover) 或本项目的 `tools/gemini_watermark_remover.py` 去除。

### 三步开始

```
1️⃣ 克隆仓库
   打开编辑器 → Clone Repository → 输入本仓库地址
   git clone https://github.com/hugohe3/ppt-master.git

2️⃣ 打开聊天窗口
   在编辑器中打开 AI 聊天面板（Antigravity/Cursor/Copilot Chat）

3️⃣ 开始对话
   直接告诉 AI 你想创建什么内容，AI 会自动按照仓库中的角色定义工作
```

### 使用示例

```
用户：我有一份关于 Q3 季度业绩的报告，需要制作成 PPT

AI（Strategist 角色）：好的，在开始之前我需要完成八项确认...
   1. 画布格式：[建议] PPT 16:9
   2. 页数范围：[建议] 8-10 页
   ...
```

💡 **模型推荐**：Opus 4.5 效果最佳，Antigravity 目前可免费使用

---

## 🎴 精选示例

> 📁 **示例库**: [`examples/`](./examples/) · **15 个项目** · **229 页 SVG**

### 示例项目总览

| 类别 | 项目 | 页数 | 特色 |
|------|------|:----:|------|
| 🏢 **咨询风格** | [心理治疗中的依恋](./examples/ppt169_顶级咨询风_心理治疗中的依恋/) | 32 | 顶级咨询风格，最大规模示例 |
| | [构建有效AI代理](./examples/ppt169_顶级咨询风_构建有效AI代理_Anthropic/) | 15 | Anthropic 工程博客，AI Agent 架构 |
| | [重庆市区域报告](./examples/ppt169_顶级咨询风_重庆市区域报告_ppt169_20251213/) | 20 | 区域财政分析，企业预警通数据 🆕 |
| | [甘孜州经济财政分析](./examples/ppt169_顶级咨询风_甘孜州经济财政分析/) | 17 | 政务财政分析，藏区文化元素 |
| | [南欧江水电站战略评估](./examples/ppt169_高端咨询风_南欧江水电站战略评估/) | 20 | "流域危机"设计语言 |
| | [汽车认证五年战略规划](./examples/ppt169_高端咨询风_汽车认证五年战略规划/) | 20 | McKinsey/BCG 风格 |
| | [麦肯锡风客户忠诚度](./examples/ppt169_麦肯锡风_kimsoong_customer_loyalty/) | 8 | 麦肯锡经典 MECE 原则 |
| | [Google 年度工作汇报](./examples/ppt169_谷歌风_google_annual_report/) | 10 | Google 品牌设计语言 |
| 🎨 **通用灵活** | [Debug 六步法](./examples/ppt169_通用灵活+代码_debug六步法/) | 10 | 深色科技风格 |
| | [重庆大学论文格式](./examples/ppt169_通用灵活+学术_重庆大学论文格式标准/) | 11 | 学术规范指南 |
| | [AI 编程工具对比](./examples/ppt169_通过灵活+代码_三大AI编程神器横向对比/) | 11 | 技术评测风格 |
| ✨ **创意风格** | [地山谦卦深度研究](./examples/ppt169_易理风_地山谦卦深度研究/) | 20 | 易经本体美学，阴阳爻变设计 |
| | [金刚经第一品研究](./examples/ppt169_禅意风_金刚经第一品研究/) | 15 | 禅意学术，水墨留白 |
| | [Git 入门指南](./examples/ppt169_像素风_git_introduction/) | 10 | 像素复古游戏风 |
| | [PPT Master 介绍](./examples/demo_project_intro_ppt169_20251211/) | 10 | 清新科技风格 |

📖 [查看完整示例文档](./examples/README.md)

### 代表作品展示

#### 顶级咨询风格 · 心理治疗中的依恋（32 页）

> 最大规模示例项目，"安全基地"视觉隐喻

📁 [查看项目](./examples/ppt169_顶级咨询风_心理治疗中的依恋/) · 📄 [设计规范](./examples/ppt169_顶级咨询风_心理治疗中的依恋/设计规范与内容大纲.md)

#### 易理玄学风格 · 地山谦卦深度研究（20 页）

> 阴阳爻变设计语言，六爻层进结构

📁 [查看项目](./examples/ppt169_易理风_地山谦卦深度研究/) · 📄 [设计规范](./examples/ppt169_易理风_地山谦卦深度研究/设计规范与内容大纲.md)

#### 像素复古风格 · Git 入门指南（10 页）

> 霓虹色系，"存档点"隐喻版本控制

📁 [查看项目](./examples/ppt169_像素风_git_introduction/) · 📄 [设计规范](./examples/ppt169_像素风_git_introduction/设计规范与内容大纲.md)

---

<details>
<summary><b>📋 目录（点击展开）</b></summary>

| 章节 | 链接 |
|------|------|
| 🚀 快速使用指南 | [跳转](#-快速使用指南) |
| 🎴 精选示例 | [跳转](#-精选示例) |
| 项目简介 | [跳转](#项目简介) |
| 核心特性 | [跳转](#核心特性) |
| 系统架构 | [跳转](#系统架构) |
| 核心角色 | [跳转](#核心角色) |
| 快速开始 | [跳转](#快速开始) |
| 更多示例 | [跳转](#更多示例) |
| 设计风格 | [跳转](#设计风格) |
| 技术规范 | [跳转](#技术规范) |
| 项目结构 | [跳转](#项目结构) |
| 最佳实践 | [跳转](#最佳实践) |
| 常见问题 | [跳转](#常见问题) |
| 贡献指南 | [跳转](#贡献指南) |
| 路线图 | [跳转](#路线图) |
| 🛠️ 工具集 | [跳转](#️-工具集) |
| 📄 开源协议 | [跳转](#-开源协议) |
| 🙏 致谢 | [跳转](#-致谢) |
| 📮 联系方式 | [跳转](#-联系方式) |

</details>

## 📚 文档导航

- 🚀 **新手入门**: 阅读本 README
- 📖 **详细教程**: [工作流教程](./docs/workflow_tutorial.md)
- 🎨 **设计指南**: [设计规范详解](./docs/design_guidelines.md)
- 📐 **画布格式**: [支持的所有格式](./docs/canvas_formats.md)
- 🖼️ **图片嵌入**: [SVG 图片嵌入指南](./docs/svg_image_embedding.md)
- 📊 **图表模板**: [标准化图表模板库](./templates/charts/) - 13种常用图表 · [在线预览](./templates/charts/preview.html)
- ⚡ **快速查阅**: [快速参考指南](./docs/quick_reference.md)
- 🔧 **角色定义**: [查看所有角色](./roles/README.md)
- 🛠️ **工具集**: [工具使用指南](./tools/README.md)
- 💼 **示例索引**: [查看所有示例](./examples/README.md)

## 项目简介

PPT Master 是一个创新的 AI 辅助视觉内容创作系统，通过多角色协作（策略师、图片生成师、执行师、优化师），实现从内容策划到视觉优化的完整工作流。系统不仅支持生成符合顶尖咨询公司（如麦肯锡、波士顿咨询）标准的商业演示文稿，还支持小红书帖子、朋友圈海报、Instagram 等多种社交媒体和营销物料格式。

## 核心特性

✨ **智能内容解构** - 自动分析源文档并重组为清晰的页面序列
🎨 **三重设计风格** - 支持"通用灵活"、"一般咨询"和"顶级咨询（MBB 级）"
📐 **多格式支持** - 演示文稿 (16:9/4:3)、小红书 (3:4)、朋