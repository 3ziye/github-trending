<div align="center">

<img src="assets/readme-banner-cn.png" alt="Design Judge Skills 中文横幅" width="100%">

# Design Judge Skills

面向设计奖全流程的证据驱动 Agent Skills：从获奖案例检索、设计评价和奖项匹配，到申报文字准备与提交终检。

[![License](https://img.shields.io/badge/license-Apache--2.0-2ea44f)](LICENSE)
[![Install](https://img.shields.io/badge/install-Claude%20Code%20%7C%20Codex%20%7C%20OpenClaw%20%7C%20OpenCode%20%7C%20Hermes-111827)](#5-安装)
[![Skills](https://img.shields.io/badge/skills-6-0ea5e9)](#6-技能索引)
[![Observed Works](https://img.shields.io/badge/observed%20works-22%2C125-7c3aed)](docs/benchmark-coverage.md)
[![Validate repository](https://github.com/SeanJ1ang/design-judge-skills/actions/workflows/validate-repository.yml/badge.svg)](https://github.com/SeanJ1ang/design-judge-skills/actions/workflows/validate-repository.yml)
[![Language](https://img.shields.io/badge/language-中文%20%7C%20English-1f6feb)](README_EN.md)

[快速开始](#4-快速开始) · [获奖样本体量](docs/benchmark-coverage.md) · [安装](#5-安装) · [技能索引](#6-技能索引) · [贡献与开发](#7-贡献与开发) · [English](README_EN.md)

</div>

`design-judge-skills` 将设计奖申报拆解为边界清晰、可独立触发与验证的技能模块，围绕官方来源、证据定位与透明评分构建可追溯的辅助决策流程，并依据公开标准比较申报路径、解释适配度与确定申报优先级。

## 目录

- [1. 项目介绍](#1-项目介绍)
- [2. 工作流](#2-工作流)
- [3. 设计原则与边界](#3-设计原则与边界)
- [4. 快速开始](#4-快速开始)
- [5. 安装](#5-安装)
  - [5.1 npx skills 安装方式](#51-npx-skills-安装方式)
  - [5.2 Claude Code 安装方式](#52-claude-code-安装方式)
  - [5.3 Codex 安装方式](#53-codex-安装方式)
  - [5.4 其他 Agent 场景](#54-其他-agent-场景)
- [6. 技能索引](#6-技能索引)
- [7. 贡献与开发](#7-贡献与开发)

## 1. 项目介绍

Design Judge Skills 覆盖设计奖申报中的五类核心任务：

- 检索并核验同类别获奖案例；
- 用证据化量表评价设计本体与展示表达；
- 匹配奖项、项目路径和申报类别；
- 从用户材料中准备有来源约束的申报文字；
- 按当届官方规则检查提交包是否就绪。

当前配置覆盖 iF DESIGN AWARD、iF DESIGN STUDENT AWARD、Red Dot Product Design、Red Dot Design Concept、IDEA、DIA、K-Design、GOOD DESIGN AWARD Japan、Core77、James Dyson 和 EPDA。涉及截止日期、费用、资格、类别与提交规格时，技能要求在运行时重新核验官方页面。

评价模块内置来自 iF、iF Student、Red Dot 与 IDEA 的 **22,125 条获奖或入围作品聚合观察记录**。这些数据只提供描述性背景，不改变核心评分，也不能用于估计获奖概率。参见[覆盖范围、隐私与限制](docs/benchmark-coverage.md)。

## 2. 工作流

```text
设计材料 ── 不确定路线或需要完整流程 ──> design-award-pipeline
  │
  ├─ 寻找同类获奖案例 ──────────────> design-award-search
  ├─ 评价设计与展示表达 ────────────> design-evaluation
  └─ 选择奖项 / 赛道 / 类别 ───────> design-award-match
                                         │
                                         v
                                design-information-prep
                                         │
                                         v
                                design-submission-check
```

这些模块可以独立使用。完整申报流程通常从评价或匹配开始，在目标奖项确定后进入信息准备，最后执行提交终检。

## 3. 设计原则与边界

1. **优先使用一手来源。** 奖项规则和案例以官方页面为准，搜索摘要与第三方页面只能用于发现线索。
2. **事实与推断分离。** 用户材料中的事实、模型推断和待用户确认项必须分别标记。
3. **评分保持透明。** 适配度和评价分数用于辅助决策，不代表获奖概率。
4. **模块职责单一。** 检索、评价、奖项匹配、文字准备和提交检查不互相越界。
5. **不冒充官方判断。** 可对齐公开评审标准，但不模拟未公开的评委偏好或内部流程。

## 4. 快速开始

安装完成后，直接把设计图片、展板、说明书、项目 brief、研究材料或申报文件交给 Agent，并说明任务。下面的提示词可以直接复制。

| 想做什么 | 直接这样说 |
|---|---|
| 规划完整参奖流程 | `使用 $design-award-pipeline，根据现有材料规划完整参奖路线，并维护各阶段的交接记录。` |
| 查找同类获奖案例 | `使用 $design-award-search，为这个康复训练产品寻找经过官方页面核验的同类别获奖案例。` |
| 评价学生概念 | `使用 $design-evaluation 评价附件中的设计。成熟度由我确定为“学生概念”，请分别输出设计本体、展示表达、证据置信度和 Critical 问题。` |
| 比较目标奖项 | `使用 $design-award-match，比较 iF Student、Red Dot Design Concept、DIA、Core77 和 James Dyson 对这个项目的适配度。` |
| 准备申报文字 | `使用 $design-information-prep，基于附件准备 IDEA 申报文字。先列出缺失事实，再按字段输出英文草稿与字数校验。` |
| 提交前终检 | `使用 $design-submission-check，按照目标奖项当届官方规则检查这个提交包，并给出 go / conditional go / no-go 结论。` |

如果不确定该用哪个技能，使用 `design-award-pipeline`；它只选择必要模块，不会强制执行完整流水线。

## 5. 安装

仓库中的每个 `skills/<name>/` 目录都是一个可安装单元。`design-judge-shared` 是共享支持包；全量安装时会自动包含，单独安装 `design-award-search` 或 `design-award-match` 时请同时安装它。

### 5.1 `npx skills` 安装方式

需要 [Node.js 18 或更高版本](https://nodejs.org/)。无需全局安装 CLI。

先查看仓库中可安装的技能：

```bash
npx skills add SeanJ1ang/design-judge-skills --list
```

把全部技能全局安装到 Codex：

```bash
npx skills add SeanJ1ang/design-judge-skills --global --agent codex --skill '*' --yes --copy
```

只为当前项目安装一个独立技能：

```bash
npx skills add SeanJ1ang/design-judge-skills --agent codex --skill design-evaluation --yes --copy
```

单独安装依赖共享资料的技能：

```bash
npx skills add SeanJ1ang/design-judge-skills --global --agent codex \
  --skill design-award-search --skill design-judge-shared --yes --copy
```

安装到 CLI 支持的所有 Agent：

```bash
npx skills add SeanJ1ang/design-judge-skills --all
```

检查与更新：

```bash
npx skills list --global --agent codex
npx skills update --global --yes
```

### 5.2 Claude Code 安装方式

全量安装：

```bash
npx skills add SeanJ1ang/design-judge-skills --global --agent claude-code --skill '*' --yes --copy
```

安装后开启新的 Claude Code 会话，自然描述任务或明确指定技能名，例如：

```text
Use $design-award-match to compare the best award routes for this student concept.
```

### 5.3 Codex 安装方式

推荐使用 `npx skills` 安装到 Codex 的全局技能目录：

```bash
npx skills add SeanJ1ang/design-judge-skills --global --agent codex --skill '*' --yes --copy
```

也可以把仓库链接直接交给 Codex：

```text
请从 https://github.com/SeanJ1ang/design-judge-skills 安装全部 Codex skills。
请保留每个技能的完整目录，并同时安装 design-judge-shared。
安装完成后检查所有 SKILL.md 的 frontm