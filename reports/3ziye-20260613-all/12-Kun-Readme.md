<p align="center">
  <img src="src/asset/img/kun.png" width="104" alt="Kun 图标">
</p>

<h1 align="center">Kun</h1>

<p align="center">
  <strong>探索需求先行的下一代 coding 范式。</strong><br>
  用 DeepSeek、Xiaomi MiMo、MiniMax 的高性价比组合，把需求澄清、设计稿、计划和 Agent 编码串成完整闭环。
</p>

<p align="center">
  <a href="./README.en.md">English</a>
  &nbsp;·&nbsp;
  <strong>简体中文</strong>
  &nbsp;·&nbsp;
  <a href="https://github.com/KunAgent/Kun/releases">下载</a>
  &nbsp;·&nbsp;
  <a href="#文档地图">文档</a>
  &nbsp;·&nbsp;
  <a href="#从源码运行">源码运行</a>
</p>

<p align="center">
  <a href="https://github.com/KunAgent/Kun/releases"><img src="https://img.shields.io/github/v/release/KunAgent/Kun?label=release" alt="GitHub release"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/license-PolyForm%20Noncommercial%201.0.0-blue" alt="License: PolyForm Noncommercial 1.0.0"></a>
  <img src="https://img.shields.io/badge/platform-macOS%20%7C%20Windows%20%7C%20Linux-lightgrey" alt="Platform">
  <img src="https://img.shields.io/badge/Electron-34-47848F?logo=electron&logoColor=white" alt="Electron 34">
  <img src="https://img.shields.io/badge/React-19-61DAFB?logo=react&logoColor=black" alt="React 19">
</p>

Kun 是一次面向未来编程方式的产品实验：不再从“给 Agent 一句话，让它直接改代码”开始，而是从需求澄清开始，把需求文档、设计稿、交互原型、实施计划、Todo、Agent 编码和变更审查放到一条连续的 GUI 工作流里。

Kun 面向希望把 AI Agent 真正放进日常工作的用户。它不是只聊天的客户端，也不是只给程序员的 CLI 外壳：你可以把本地目录交给它处理代码、需求、计划和变更审查，也可以在独立的 Write 工作区里写作、润色和导出文档。

这也是 Kun 为什么把 DeepSeek、Xiaomi MiMo、MiniMax 作为默认的一线模型组合，而不是把它们当成普通的“可选 Provider”。需求先行的 coding 范式会带来更多轮澄清、调研、结构化、规划、执行和验证，如果模型成本太高，这条流程很难成为日常工作方式。Kun 选择三家来自中国的高性价比模型供应商，正是为了让完整流程跑得起、用得久、试得多。

Kun 内置同名本地运行时，通过 `kun serve` 连接桌面端。会话、日志、偏好设置和运行时配置默认保存在本机；模型请求使用你自己的模型服务凭据。对会读写文件和执行命令的流程，Kun 提供工具审批、权限模式、内联 diff 和变更审查面板。

---

<p align="center">
  <a href="src/asset/img/code.mp4">
    <img src="src/asset/img/code.gif" width="410" alt="Kun Code 模式演示">
  </a>
  <a href="src/asset/img/write.mp4">
    <img src="src/asset/img/write.gif" width="410" alt="Kun Write 模式演示">
  </a>
</p>

## 需求先行的 coding 范式

Kun 想探索的是“需求 -> 设计 -> 计划 -> 编码 -> 验证”的下一代编程工作流，而不是把一个聊天框简单贴到 IDE 上。

| 阶段 | Kun 的尝试 |
| --- | --- |
| **澄清需求** | 在 GUI 中新建需求草稿，让需求 AI 帮你补问题、做实现前调研、整理边界 |
| **沉淀文档** | 把草稿保存为 `.kunsdd/draft/.../requirement.md`，支持结构化需求块、验收标准和需求历史 |
| **生成设计** | 从需求片段生成 UI 设计稿、信息图或交互式 HTML 原型，让需求不只停留在文字里 |
| **形成计划** | 通过 `/plan` 和 `create_plan` 生成 GUI 管理的 `.kunsdd/plan/...` 实施计划，并把计划步骤和需求关联 |
| **Agent 编码** | 计划进入 Todo、文件编辑、命令执行和变更审查；需求变更后可以提示重规划，避免计划和需求脱节 |
| **回到验收** | 结合需求块、验收标准、计划状态和 `/review`，把“做完了吗”落回最初的需求 |

这条线是 Kun 最重要的产品方向：让 AI coding 从“即时问答”走向“需求驱动的软件生产流程”。模型、写作、计划、审查和自动化都围绕这条线服务。

## 核心模型组合

Kun 追求的是“完整能力 + 极致性价比”。需求先行的流程比普通聊天更长，也更依赖反复调用模型；首启和设置页围绕三家中国模型供应商组织，让用户可以用更低的模型成本覆盖更多 Agent 场景。

| 供应商 | 在 Kun 中的角色 |
| --- | --- |
| **DeepSeek** | 默认文本与推理主模型，提供 `deepseek-v4-pro` / `deepseek-v4-flash`，支撑代码、计划、审查、长上下文会话和自动模型路由 |
| **Xiaomi MiMo** | 高性价比多模态与语音入口，覆盖长上下文文本模型、视觉输入、ASR 语音转写、TTS 语音生成和 Token Plan |
| **MiniMax** | 补齐完整媒体生成能力，覆盖 Anthropic Messages 文本模型、图片生成、语音生成、音乐生成、视频生成和 Token Plan |

这套组合让 Kun 可以把不同任务分配给更合适的能力：轻量澄清走高速模型，复杂代码和推理走更强模型，需求文档和 IM 场景接入语音，设计与创作场景接入图片、音乐和视频。你仍然可以添加 OpenAI 兼容、自托管或其他自定义 Provider，但 Kun 的默认体验会优先围绕这三家高性价比模型服务展开。

## 为什么选择 Kun

| 你想要 | Kun 提供 |
| --- | --- |
| 探索下一代 coding 范式 | 从需求澄清、需求文档、设计稿、实施计划一路走到 Agent 编码和验收 |
| 极致性价比的完整 Agent 能力 | 以 DeepSeek、Xiaomi MiMo、MiniMax 为核心组合，覆盖文本、推理、视觉、语音、图片、音乐和视频 |
| 让 AI 面向真实项目工作 | 绑定本地工作区，读写文件、搜索代码、执行命令、查看工具调用和结果 |
| 把需求推进到可执行计划 | 支持新建需求、`/plan`、Todo、`/goal`、旁支对话、会话压缩、分叉和归档 |
| 让改动保持可控 | 工具审批、文件系统权限模式、内联 diff、变更审查面板和 `/review` |
| 在同一个应用里写作 | Markdown 文件树、Live / Source / Split / Preview、多种导出格式、选区 inline agent |
| 离开电脑也能触发任务 | 飞书 / Lark / 微信连接、本地 webhook / relay、一次性或周期性定时任务 |
| 不被单一模型绑定 | 三家核心供应商之外，也支持自定义 Base URL、协议、模型列表和扩展能力 |

## 核心能力

- **需求先行 coding**：新建需求草稿，AI 澄清和结构化需求，生成设计稿或交互原型，再进入实施计划、Todo、Agent 编码和验收。
- **Code 工作台**：围绕真实代码库对话，读取项目上下文，执行 shell 命令，修改文件，并在提交前审查每一次变更。
- **需求、计划与审查**：从需求草稿进入计划，再到 Todo、执行、复盘和代码审查；长会话可以压缩、恢复、分叉或归档。
- **Write 写作模式**：独立 Markdown 工作区，支持文件树、预览模式切换、补全、选区改写、图片附件，以及 `HTML / PDF / DOC / DOCX` 导出。
- **自动化与远程入口**：把桌面会话接到飞书 / Lark / 微信等 IM，支持本地 webhook、relay 和定时任务，让后台任务也能回到同一套 Agent loop。
- **模型组合优先**：围绕 DeepSeek、Xiaomi MiMo、MiniMax 设计首启、Provider 预设和能力自动接线，用高性价比模型组合承担完整桌面 Agent 工作流。
- **多模态与媒体能力**：支持图片附件、视觉输入、语音转写、图片生成、语音生成、音乐生成和视频生成；相关能力随 Provider 配置启用。
- **MCP 与 Skills**：接入 Model Context Protocol 服务器，加载项目或全局 Skills，让 Kun 按任务获得更专门的工具和工作方式。
- **本地运行时**：`kun serve` 提供 HTTP/SSE 边界，采用 cache-first agent loop、追加式事件日志、用量统计和上下文压缩策略。

## 更多演示

<p align="center">
  <a href="src/asset/img/pdf-research.mp4">
    <img src="src/asset/img/pdf-research.gif" width="680" alt="PDF 研究演示">
  </a>
</p>
<p align="center"><em>PDF 研究与资料整理演示</em></p>

<p align="center">
  <a href="src/asset/img/sdd.mp4">
    <img src="src/asset/img/sdd.gif" width="680" alt="需求澄清、需求文档与计划演示">
  </a>
</p>
<p align="center"><em>需求澄清、需求文档与计划演示</em></p>

<p align="center">
  <a href="src/asset/img/ikun-ui-plugin.mp4">
    <img src="src/asset/img/ikun-ui-plugin.gif" width="680" alt="iKun UI 插件演示">
  </a>
</p>
<