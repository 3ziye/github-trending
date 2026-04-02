<div align="center">

<img src="asset/logo.png" alt="Hello Claw Logo" width="400">

<p align="center"><em>一个不起眼的仓库里，龙虾诞生了。<br>选一只，送它上学堂；或动手写一只不被定义的龙虾。<br>它的梦想，从第一天起就很大。</em></p>

# 哈喽！龙虾 👋

<p align="center"><em>Hello Claw：领养你的 AI 龙虾助理，上龙虾大学学 Skills，从零构建属于你的智能助理</em></p>

<p align="center">
  📌 <a href="https://datawhalechina.github.io/hello-claw/">在线阅读</a> | 💬 <a href="#交流群">加入交流群</a> | 🚀 <a href="https://github.com/datawhalechina/easy-vibe">还想学 Vibe Coding</a>
</p>

<p align="center">
    <a href="https://github.com/datawhalechina/hello-claw/stargazers" target="_blank">
        <img src="https://img.shields.io/github/stars/datawhalechina/hello-claw?color=660874&style=for-the-badge&logo=star&logoColor=white&labelColor=1a1a2e" alt="Stars"></a>
    <a href="https://github.com/datawhalechina/hello-claw/network/members" target="_blank">
        <img src="https://img.shields.io/github/forks/datawhalechina/hello-claw?color=660874&style=for-the-badge&logo=git-fork&logoColor=white&labelColor=1a1a2e" alt="Forks"></a>
    <a href="LICENSE" target="_blank">
        <img src="https://img.shields.io/badge/License-CC_BY_NC_SA_4.0-4ecdc4?style=for-the-badge&logo=creative-commons&logoColor=white&labelColor=1a1a2e" alt="License"></a>
</p>

<p align="center">
  <a href="README.md"><img alt="简体中文" src="https://img.shields.io/badge/简体中文-d9d9d9"></a>
  <a href="README_EN.md"><img alt="English" src="https://img.shields.io/badge/English-d9d9d9"></a>
  <a href="README_JA.md"><img alt="日本語" src="https://img.shields.io/badge/日本語-d9d9d9"></a>
</p>

</div>

> [!WARNING]
> 🧪 Beta公测版本提示：教程主体已完成，正在优化细节，欢迎大家提Issue反馈问题或建议。

## 在线阅读

https://datawhalechina.github.io/hello-claw

## 项目简介

本项目是一个面向 OpenClaw 的完整学习教程，帮助你从零开始掌握这个强大的命令行 AI 助理系统。无论你是想快速上手使用 OpenClaw 提升效率，还是想深入理解其原理并构建自己的版本，本教程都能为你提供清晰的学习路径。

**本项目包含三大核心模块：**

1. **领养龙虾（使用篇）**：11 章 + 7 个附录，安装（Ch1-3）+ 核心配置（Ch4-6）+ 扩展运维（Ch7-9）+ 安全与客户端（Ch10-11），按需选读
2. **龙虾大学（场景实战篇）**：围绕 Skills 选型与典型工作流，给出可直接复用的实战案例
3. **构建龙虾（开发篇）**：11 章，先拆解 OpenClaw 源码与替代方案，再进入 Skills、渠道和完整定制

**谁适合学习：**

- 零基础用户：想要一个随时待命的 AI 助手，不需要任何编程经验
- 效率达人：希望通过 QQ / 飞书 / Telegram 远程控制 AI
- 技术爱好者：对 OpenClaw 的技能系统和自动化能力感兴趣
- 开发者：想深入理解 Agent 架构并构建自己的版本

**学习建议：**

- 零基础用户：从第一部分“领养龙虾”开始，先把安装与基础自动化跑通
- 想做场景闭环：直接进入“龙虾大学”，按场景挑 5~10 个 Skills 快速落地
- 开发者：进入“构建龙虾”，拆解底层实现原理并定制自己的 Claw

## 🔥 最新动态

- **[2026-03-25]** ✅ 龙虾大学完成一轮场景扩充与新手化重写，新增个人效率、编程开发、内容创作、商务销售、多智能体协作和更多场景共 11 篇可直接上手的实战案例，并同步按 README 分类整理
- **[2026-03-25]** 🔥 OpenClaw v2026.3.24：Gateway OpenAI 兼容端点（`/v1/models`、`/v1/embeddings`）、Microsoft Teams 官方 SDK 集成（流式回复/欢迎卡片/消息编辑删除）、Skills 一键安装配方与 Control UI 状态过滤、Slack 富回复恢复、CLI `--container` 容器内执行、Discord LLM 自动线程命名、`before_dispatch` 插件钩子、沙箱媒体安全修复，教程全章节同步
- **[2026-03-23]** 🔥 OpenClaw 3.22 大版本：插件 SDK 重构（旧 extension-api 废弃）、安全加固（SMB 凭证泄露/环境变量注入/Unicode 伪装等修复）、GPT-5.4 默认上位、飞书交互卡片/Telegram 话题自动命名、Agent 超时延长至 48h
- **[2026-03-12]** ✅ 完成构建 Claw 第1-10章：核心架构解析（提示词系统、工具系统、消息循环、多渠道接入）、替代方案探索（轻量化、安全加固、硬件方案）、站在山巅回望总结
- **[2026-03-10]** ✅ 完成构建 Claw 第13章：Skill 文件结构、Frontmatter、异步处理与调试
- **[2026-03-10]** ✅ 新增龙虾大学：菜单式 Skills 选修指南，让龙虾装上"战斗外挂"
- **[2026-03-08]** ✅ 完成领养 Claw 第1-11章：安装（AutoClaw + 手动安装 + 配置向导）、核心配置（聊天平台、模型、智能体）、扩展运维（工具与定时任务、网关、远程访问）、安全与客户端（安全防护、Web 界面）
- **[2026-03-04]** 🦞 项目启动，规划"领养 Claw"和"构建 Claw"两大核心模块

## 📖 目录

### 龙虾大学

<table align="center">
  <tr>
    <td valign="top" width="33%">
      <b>🌅 个人效率</b><br>
      • <a href="./docs/cn/university/email-assistant/index.md">邮箱助手实战（163）</a><br>
      • <a href="./docs/cn/university/local-health-assistant/index.md">Skill 开发实战：本地健康管理助手</a><br>
      • <a href="./docs/cn/university/daily-briefing/index.md">早间简报自动化</a><br>
      • <a href="./docs/cn/university/calendar-ops/index.md">智能日程管理</a>
    </td>
    <td valign="top" width="33%">
      <b>💻 编程开发</b><br>
      • <a href="./docs/cn/university/vibe-coding/index.md">Vibe Coding 实战</a><br>
      • <a href="./docs/cn/university/ci-cd-assistant/index.md">自动化测试与部署：CI/CD 助手实战</a><br>
      • <a href="./docs/cn/university/docs-automation/index.md">文档自动生成：从代码变更到可发布文档</a>
    </td>
    <td valign="top" width="33%">
      <b>📢 内容创作</b><br>
      • <a href="./docs/cn/university/vibe-research/index.md">自动化科研实战</a><br>
      • <a href="./docs/cn/university/content-studio/index.md">内容创作工作室：社媒运营、写作润色与多平台发布</a>
    </td>
  </tr>
  <tr>
    <td valign="top" width="33%">
      <b>🏢 商务销售</b><br>
      • <a href="./docs/cn/university/revops-assistant/index.md">商务销售实战：客户支持与 CRM 协同助手</a><br>
      • <a href="./docs/cn/university/meeting-ops/index.md">商务销售实战：会议预约与纪要自动化</a>
    </td>
    <td valign="top" width="33%">
      <b>🤖 多智能体协作</b><br>
      • <a href="./docs/cn/university/multi-claw-hiclaw/index.md">多智能体协作（Multi OpenClaw / HiClaw）</a><br>
      • <a href="./docs/cn/university/knowledge-base/index.md">多智能体协作实战：知识库共享与检索</a><br>
      • <a href="./docs/cn/university/one-person-company/index.md">一人公司实战（一个人，一支团队）</a>
    </td>
    <td valign="top" width="33%">
      <b>🔧 更多场景</b><br>
      • <a href="./docs/cn/university/security/index.md">安全防护清单</a><br>
      