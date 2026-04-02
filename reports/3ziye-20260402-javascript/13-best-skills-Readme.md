# best-skills

通用高质量 Skill 合集，可安装到 Cursor、Claude Code、Codex、OpenClaw 等 Agent 工具的 skills 目录使用。

**与 [best-prompts](https://github.com/xstongxue/best-prompts) 的区别**：best-prompts 是面向聊天框的 Prompt，需手动复制粘贴；best-skills 是面向 Agent 的 SKILL.md，Agent 会根据 `description` 中的关键词与触发场景**自动判断是否调用**，无需每次手动选择。

## 效果预览

**答辩 PPT（[pptgen-drawio](skills/pptgen-drawio/SKILL.md)）**

- **风格一 · 经典学术**：源文件  
  [paper-defense-style1-classic.drawio](preview/paper-defense.drawio) · [paper-defense-style1-classic.pptx](preview/paper-defense.pptx)
- **风格四 · 科技明快**：源文件  
  [paper-defense-style4-tech.drawio](preview/paper-defense.drawio) · [paper-defense-style4-tech.pptx](preview/paper-defense.pptx)

<table><tr>
<td><img src="preview/paper-defense1.jpg" alt="答辩PPT预览1"/></td>
<td><img src="preview/paper-defense2.jpg" alt="答辩PPT预览2"/></td>
</tr></table>

**公众号封面（[wechat-article-writer](skills/wechat-article-writer/SKILL.md)）** · 源文件：[wechat_cover.drawio](preview/wechat_cover.drawio)

![公众号封面预览](preview/wechat_cover.drawio.png)

**手绘图（[excalidraw-diagram](skills/excalidraw-diagram/SKILL.md)）** · 源文件：[excalidraw-transformer.excalidraw](preview/excalidraw-transformer.excalidraw.drawio)

![公众号封面预览](preview/excalidraw-transformer.png)

## 本科&硕士学位论文


| 用途                | Skill           | 示例 Prompt                                               |
| ----------------- | --------------- | ------------------------------------------------------- |
| 大纲审核（理工/文科）       | paper-write     | 「帮我审核一下这个论文大纲」（理工科 / 文科自动区分）                              |
| 结构仿写（理工 science）   | paper-write     | 「按这篇范文仿写我的实验章节」「帮我写绪论/摘要，参考 XX 论文」                         |
| 结构仿写（文科 liberal）   | paper-write     | 「文科仿写文献综述/理论章节」「文科仿写案例分析/对策建议」「写文科摘要」                        |
| 润色 / 去 AI 化       | paper-write     | 「这段读起来像 AI 写的，帮我润色」「实验章节润色」「文科章节润色」                        |
| 参考文献              | paper-write     | 「帮我找 RLHF 代表作并给 BibTeX」「cite Vaswani 的 attention」       |
| 结构化信息提取           | paper-write     | 「从这篇论文提取结构化信息，用于答辩 PPT」                                 |
| 系统章节生成            | codegen-doc     | 「根据当前项目生成系统总体设计章节」                                      |
| 答辩 PPT / 通用汇报 PPT | pptgen-drawio   | 「帮我做答辩 PPT，论文在 xxx」「根据这个大纲生成汇报 PPT」                     |
| 模型架构图 / 流程图       | drawio-diagram  | 「画一个 Transformer 架构图」「做一张算法流程图」                         |
| 图片风格迁移            | drawio-diagram  | 「按这张参考图的风格画」「参考图+描述：画一个三层系统，前端 Vue、后端 Spring、数据库 MySQL」 |
| 技术栈图              | codegen-diagram | 「根据当前项目画技术栈结构图」                                         |
| 系统架构图             | codegen-diagram | 「画我们系统的四层架构图」                                           |
| 数据结构图             | codegen-diagram | 「根据代码生成数据结构图」                                           |
| E-R 图             | codegen-diagram | 「根据数据库表结构画 E-R 图」                                       |


> **paper-write**：统一 Skill，**理工（science-*）与文科（liberal-*）命名区分**。支持大纲审核（理工/文科）、结构仿写（理工：绪论/摘要/实验；文科：绪论/摘要/文献综述/案例分析/对策）、参考文献、润色（通用/实验章节/文科章节）、扩写/缩写、防 AIGC、中英互译、结构化信息提取。  
> **codegen-diagram**：统一 Skill，根据用户表述自动匹配技术栈图、系统架构图、数据结构图、E-R 图。  
> **codegen-doc**：统一 Skill，匹配论文章节、项目梳理、重点问题、简历项目描述。  
> **pptgen-drawio**：支持论文答辩与通用汇报两种模式，输出 .drawio 后可用 drawio2pptx 导出 .pptx。

## 开发流程五步法


| 步骤     | Skill        | 示例 Prompt                           |
| ------ | ------------ | ----------------------------------- |
| 需求理解   | dev-workflow | 「我想做一个 XXX，帮我整理需求」                  |
| 方案设计   | dev-workflow | 「需求已整理好，帮我做技术方案」「架构设计：前后端分离」        |
| 代码实现   | dev-workflow | 「按方案开始写代码」「实现用户登录模块」                |
| 代码审查   | dev-workflow | 「帮我审查这段代码」「PR review，按团队规范检查」       |
| Bug 修复 | dev-workflow | 「这里报错了：xxx」「功能跑不通，帮我修」「测试挂了，看看怎么回事」 |


> **dev-workflow**：统一 Skill，根据用户表述自动匹配 requirement/design/implementation/review/bug-fix 五步之一。

## 自媒体创作


| 用途                   | Skill                 | 示例 Prompt                                         |
| -------------------- | --------------------- | ------------------------------------------------- |
| 公众号/技术博客（含配图）        | wechat-article-writer | 「写一篇关于 Cursor Skills 的公众号文章」「用高流量风格写 Vibe Coding」 |
| 公众号封面 / B站封面 / 小红书配图 | wechat-article-writer | 「生成这篇文章的封面，16:9」                                  |
| 正文插图                 | wechat-article-writer | 「生成 Cursor 启用四步骤的步骤图」「画 Prompt/Rules/Skills 对比图」  |
| 风格提取                 | wechat-article-writer | 「分析这篇公众号文章的写作风格」「提取可复用规则」「模仿这篇爆款文风」               |


> **wechat-article-writer**：统一 Skill，根据用户表述自动匹配撰写文章、封面图、正文插图、风格提取。支持 9 种写作风格（按序）：默认、高流量、清单体、资源盘点、个人实测、认知颠覆、身份共鸣、故事化、深度随笔。

## 周报 / 汇报 / 总结 / 介绍


| 用途      | Skill             | 示例 Prompt             |
| ------- | ----------------- | --------------------- |
| 周报      | md-report-summary | 「帮我写本周周报，结合websearch」 |
| 工作汇报    | md-report-summary | 「写一份 Q1 工作汇报」「整理汇报材料」 |
| 总结 / 复盘 | md-report-summary | 「写项目总结」「帮我复盘这次活动」     |
| 介绍      | md-report-summary | 「写一份项目介绍」「个人简介」       |


> **md-report-summary**：无草稿时从 Web 搜索并总结；有草稿时结合草稿整理、补充、润色。输出 Markdown。

## 项目文档与简历


| 用途     | Skill       | 示例 Prompt               |
| ------ | ----------- | -----