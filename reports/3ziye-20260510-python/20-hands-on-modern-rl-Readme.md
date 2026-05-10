<div align="center">
  <img src="docs/public/readme/logo.png" alt="Hands-On Modern RL Logo" width="500" />
  <h1>Hands-On Modern RL</h1>
  <p><strong>现代强化学习实战课程</strong></p>
  <p><em>现代强化学习实战指南：涵盖经典控制、LLM 后训练、RLVR 与多模态智能体。</em></p>

  <p>
    <a href="https://walkinglabs.github.io/hands-on-modern-rl/"><img src="https://img.shields.io/badge/Course-Online-2563eb?style=flat-square" alt="Online Course" /></a>
    <a href="https://github.com/walkinglabs/hands-on-modern-rl/releases/latest"><img src="https://img.shields.io/badge/PDF-Download-e11d48?style=flat-square" alt="PDF Download" /></a>
    <a href="https://github.com/walkinglabs/hands-on-modern-rl/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-111827?style=flat-square" alt="CC BY-NC-SA 4.0 License" /></a>
    <img src="https://img.shields.io/badge/Node-%3E%3D18-16a34a?style=flat-square" alt="Node >= 18" />
    <img src="https://img.shields.io/badge/Docs-VitePress-646cff?style=flat-square" alt="VitePress" />
  </p>

  <p>
    <a href="README.md">中文</a> ·
    <a href="README.en.md">English</a>
  </p>

  <p>
    <a href="#wechat-group">💬 WeChat Group</a>
  </p>

  <p>
    <a href="#课程简介">课程简介</a> ·
    <a href="#简介">简介</a> ·
    <a href="#🔥-最新动态-news">最新动态</a> ·
    <a href="#目录">目录</a> ·
    <a href="#课程大纲">课程大纲</a> ·
    <a href="#实验代码">实验代码</a> ·
    <a href="#快速开始">快速开始</a> ·
    <a href="#参与贡献">参与贡献</a>
  </p>
</div>

## 课程简介

<table>
  <tr>
    <td width="50%" align="center">
      <img src="docs/public/readme/feature-learning-path.png" alt="课程学习地图截图" width="100%" />
      <br />
      <strong>一眼看懂的学习地图</strong>
      <br />
      <sub>从前言、基础导论到前沿专题，章节树和页内大纲帮助你快速定位。</sub>
    </td>
    <td width="50%" align="center">
      <img src="docs/public/readme/feature-code-focus.png" alt="PPO 代码聚焦截图" width="100%" />
      <br />
      <strong>代码逐行聚焦</strong>
      <br />
      <sub>PPO、DPO、GRPO 关键实现配有代码地图，把公式落到可读代码。</sub>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center">
      <img src="docs/public/readme/feature-training-metrics.png" alt="CartPole 训练指标截图" width="100%" />
      <br />
      <strong>训练指标可视化</strong>
      <br />
      <sub>真实曲线、指标解释和失败信号放在一起，方便边跑实验边诊断。</sub>
    </td>
    <td width="50%" align="center">
      <img src="docs/public/readme/feature-rlhf-pipeline.png" alt="RLHF 流水线截图" width="100%" />
      <br />
      <strong>LLM 后训练流水线</strong>
      <br />
      <sub>RLHF、DPO、GRPO、RLVR 等主题以流程、artifact 和案例串联起来。</sub>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center">
      <img src="docs/public/readme/feature-agentic-rl.png" alt="Agentic RL 项目截图" width="100%" />
      <br />
      <strong>Agentic RL 项目化</strong>
      <br />
      <sub>工具调用、轨迹合成、评测与多工具 Code Agent 走向完整工程练习。</sub>
    </td>
    <td width="50%" align="center">
      <img src="docs/public/readme/feature-vlm-rl.png" alt="VLM 强化学习截图" width="100%" />
      <br />
      <strong>多模态与前沿方向</strong>
      <br />
      <sub>VLM 强化学习、视觉生成 RL、具身智能和未来趋势延伸到前沿系统。</sub>
    </td>
  </tr>
</table>

---

> [!NOTE]
> 希望本开源教程能够让更多人拥有向智能上限发起攀登的勇气，解决更多通往 AGI 道路上的问题。
>
> 当前教程快速迭代中。建议只看非 🚧 状态的章节，🚧状态的章节很可能有错误，也欢迎修正和建议 。

> [!WARNING]
> **当前 大模型 RL 以及 Agentic RL 部分尚未校对修正，请谨慎阅读 谢谢！**

> **寻求帮助**
>
> 由于资源稀缺问题，我们正在寻求显卡支持，如果您有显卡使用方式愿意支持非常欢迎联系 physicoada@gmail.com。

## 目录

- [课程简介](#课程简介)
- [目录](#目录)
- [简介](#简介)
  - [设计原则](#设计原则)
  - [目标受众](#目标受众)
  - [学习目标](#学习目标)
  - [当前状态](#当前状态)
- [🔥 最新动态 (News)](#-最新动态-news)
- [🗺️ 演进路线图 (Roadmap)](#️-演进路线图-roadmap)
- [课程大纲](#课程大纲)
  - [前言](#前言)
  - [第一部分：基础导论](#第一部分基础导论)
  - [第二部分：核心理论与方法](#第二部分核心理论与方法)
  - [第三部分：大模型 RL](#第三部分大模型-rl)
  - [第四部分：前沿与高级系统](#第四部分前沿与高级系统)
  - [附录](#附录)
- [实验代码](#实验代码)
- [推荐学习路径](#推荐学习路径)
- [快速开始](#快速开始)
  - [在线阅读](#在线阅读)
  - [本地运行文档网站](#本地运行文档网站)
  - [验证网站](#验证网站)
  - [运行课程代码](#运行课程代码)
- [仓库结构](#仓库结构)
- [开发命令](#开发命令)
- [参与贡献](#参与贡献)
- [Star History](#star-history)
- [其他课程](#其他课程)
- [WeChat Group](#wechat-group)
- [引用](#引用)
- [开源协议](#开源协议)

## 简介

**Hands-On Modern RL** 是一门面向现代强化学习实践的开放课程。与传统的“先讲公式，再给黑盒 API”不同，本课程采用 **“实践优先”** 的路径：从一行行可运行的代码和直观的训练现象出发，让学习者先看到智能体如何在环境中试错并从奖励中改进行为，再回头深入剖析其背后的状态、价值函数、策略梯度、奖励建模与信用分配等核心数学结构。

课程内容跨越经典控制理论，直接连接到当前最前沿的 AI 进展，包括大语言模型（LLM）后训练、偏好对齐（DPO/GRPO）、可验证奖励（RLVR）、多轮工具调用的 Agentic RL 以及视觉语言模型（VLM）强化学习等核心主题。

我们希望为你铺设一条坚实的阶梯——从解出 CartPole 的第一步，一直通往构建大模型后训练与智能体系统的前沿实践。

### 设计原则

课程围绕以下工程和教学原则组织：

1. **实践先于形式化。** 每个主要主题都从实验、指标、失败案例或实现细节开始，然后再引入数学抽象。
2. **理论用于解释行为。** MDP、贝尔曼方程、策略梯度、GAE、PPO 截断、DPO 目标和 GRPO 风格的组优势，都是作为解释代码行为的工具引入的。
3. **现代强化学习，不止于经典强化学习。** 课程涵盖经典控制和深度强化学习，然后进入 RLHF、偏好优化、RLVR、VLM 强化学习和多轮智能体训练。
4. **将调试能力视为一等公民。** 训练崩溃、奖励破解（Reward hacking）、KL 漂移、熵衰减、OOM 故障和评估盲区被视为核心内容，而不是补充说明。
5. **可读的系统优于黑盒。** 代码示例倾向于显式的实现、可检查的指标和清晰的实验边界，以便学习者可以修改和扩展它们。

### 目标受众

本课程专为希望通过构建和检查工作系统来理解强化学习的学习者而设计。

它特别适合：

- 从监督学习转向强化学习的机器学习工程师；
- 准备阅读现代强化学习和对齐论文的研究人员和学生；
- 希望了解 RLHF、DPO、GRPO、RLVR 和后训练系统的大语言模型（LLM）从业者；
- 工具使用智能体、Web 智能体、代码智能体和评估流水线的构建者；
- 喜欢在密集的公式推导前先看代码、实验和直观可视化的自主学习者。

推荐背景：

- Python 编程经验；
- 基础的 PyTorch 熟练度；
- 了解入门机器学习级别的线性代数、概率论和微积分；
- 能够阅读论文并追踪开源训练脚本。

课程附带了数学基础复