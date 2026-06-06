# Agent Learning Hub

A curated AI Agent learning roadmap for people who want to build useful, reliable agents instead of collecting random links.

这个仓库只维护一个核心展示面：README。目标是把社区里优秀分享、官方博客、论文、开源项目和真实工程经验，整理成一份可以照着执行的 AI Agent 学习 todo list。

## Maintainer

Curated by [陈思州](https://github.com/jjyaoao) (Datawhale 成员) <a href="https://www.xiaohongshu.com/user/profile/67b9cc34000000000e013517" target="_blank"><img alt="Static Badge" src="https://img.shields.io/badge/Rednote-小红书-e93c49"></a>

## How To Use

- 如果你是新手：按「Learning Todo List」从上到下做，每完成一项就打勾。
- 如果你已经会 LLM 应用：从 Stage 2 或 Stage 3 开始，重点补 Agent loop、工具调用、评测和工程化。
- 如果你想做项目：直接看「Project Ladder」，每一档做一个可运行作品。
- 如果你只想找资料：看「Curated Resources」，优先读官方文档和经典论文。

## What To Learn Now

Agent 领域变化很快。当前更值得投入的不是老式“角色扮演多 agent 框架”，而是这些更贴近真实生产力的方向：

| Priority | Learn | Why |
| --- | --- | --- |
| 1 | Claude Code / Codex-style coding agents | 真实代码库、shell、文件编辑、测试、权限、上下文压缩，是最好的 agent 工程样本。 |
| 2 | Agent harness engineering | agent 的能力很大一部分来自 harness：工具协议、权限、状态、反馈、回放、CI、评测。 |
| 3 | OpenClaw / Hermes-style personal agents | 长运行、本地优先、跨应用、记忆、skills、消息入口，更像“个人操作系统”。 |
| 4 | Skills / MCP / A2A / ACP | skills 负责能力复用，MCP 连接工具，A2A 连接 agent，ACP 连接宿主应用。 |
| 5 | Evaluation and safety | 没有 eval、trace、权限边界的 agent 只能算 demo。 |

不建议把精力重押在已经泛化成模板的老式 crew/role-play 框架上。它们可以了解，但不应成为主线。

## Learning Todo List

### Stage 0: Understand What An Agent Is

- [ ] 区分 chatbot、workflow、agent、multi-agent。
- [ ] 理解 agent 的基本循环：observe -> think -> act -> observe。
- [ ] 明白什么时候不该用 agent：任务可预测、流程稳定、普通脚本能解决时，agent 反而增加不确定性。
- [ ] 读完 [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)。
- [ ] 读完 [OpenAI: A practical guide to building agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)。

产出：写一页短笔记，回答「我的场景为什么需要 agent，而不是普通 workflow？」

### Stage 1: Build A Minimal Agent Loop

- [ ] 会用一个 LLM API 完成普通对话。
- [ ] 会让模型输出结构化 JSON。
- [ ] 会定义一个工具函数，例如 search、calculator、read_file。
- [ ] 会解析模型的 tool call / function call。
- [ ] 会执行工具，并把工具结果喂回模型。
- [ ] 会给 agent loop 加最大步数、超时和错误处理。

推荐阅读：

- [OpenAI Function Calling](https://platform.openai.com/docs/guides/function-calling)
- [Gemini API Function Calling](https://ai.google.dev/gemini-api/docs/function-calling)
- [Claude Tool Use](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview)

产出：一个 50-150 行的最小 agent，可以选择工具、执行工具、返回最终答案。

### Stage 2: Learn Tool Use, RAG, And Memory

- [ ] 会做检索增强生成：chunk、embed、retrieve、answer with citations。
- [ ] 会把搜索、数据库、文件、浏览器、代码执行接成工具。
- [ ] 会区分短期上下文、会话记忆、长期记忆。
- [ ] 会处理工具失败、空结果、重复调用、幻觉引用。
- [ ] 会让 agent 在回答里给出来源或证据。

推荐阅读：

- [LlamaIndex Agents](https://docs.llamaindex.ai/en/stable/use_cases/agents/)
- [LangChain Docs](https://docs.langchain.com/)
- [Gemini API Code Execution](https://ai.google.dev/gemini-api/docs/code-execution)
- [Model Context Protocol](https://modelcontextprotocol.io/)

开源项目参考：

| Project | Why It Fits Stage 2 |
| --- | --- |
| [GPT Researcher](https://github.com/assafelovic/gpt-researcher) | 最接近“资料研究助手”的成品：搜索、抓取、筛选、引用、生成长报告。 |
| [Open Deep Research](https://github.com/langchain-ai/open_deep_research) | LangGraph 写的 deep research 示例，适合学多轮搜索、状态管理和引用输出。 |
| [STORM](https://github.com/stanford-oval/storm) | Stanford OVAL 的研究写作系统，适合学 outline、question asking、多视角资料综合。 |
| [Khoj](https://github.com/khoj-ai/khoj) | 个人 second brain，适合学本地文档、网页、语义搜索和长期记忆。 |
| [Onyx](https://github.com/onyx-dot-app/onyx) | 企业级 RAG/search assistant，适合学 connectors、hybrid search、权限和生产化。 |
| [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm) | 本地 RAG + agents 产品，适合初学者快速理解完整应用形态。 |
| [RAGFlow](https://github.com/infiniflow/ragflow) | 文档理解型 RAG 引擎，适合学 ingestion、chunking、retrieval、grounded answer。 |
| [mem0](https://github.com/mem0ai/mem0) | 记忆层组件，适合学如何给 agent 加长期 memory。 |
| [Letta](https://github.com/letta-ai/letta) | 面向 stateful agents 的 memory/context 平台，适合学上下文管理。 |

产出：一个资料研究助手，输入主题后自动搜索、筛选、总结并输出引用链接。

### Stage 3: Study One Modern Agent Harness

先选一个现代 agent 系统学深。这里的重点不是“框架 API 怎么调”，而是它如何组织工具、上下文、权限、状态、日志、子任务和反馈。

| System | Best For | Learn This If You Want To |
| --- | --- | --- |
| [Claude Code Docs](https://code.claude.com/docs/en/overview) | Coding agent product | 学真实 coding agent 的 CLI、工具、权限、hooks、subagents、MCP。 |
| [learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | From-scratch agent harness | 从 0 到 1 复刻 Claude Code-like harness。 |
| [claw0](https://github.com/shareAI-lab/claw0) | From-scratch OpenClaw gateway | 从 agent loop 一路构建 session、channel、gateway、memory、heartbeat、delivery、resilience、concurrency。 |
| [hello-agents](https://github.com/datawhalechina/hello-agents) | Chinese agent tutorial | 从零开始构建智能体，适合系统补 Agent 原理与实践。 |
| [OpenClaw](https://github.com/openclaw/openclaw) | Local-first personal agent | 学本地长运行 agent、skills、消息入口、系统工具和安全边界。 |
| [Hermes Agent](https://github.com/NousResearch/hermes-agent) | Self-hosted growing agent | 学长期记忆、skills、toolsets、多平台消息网关和迁移能力。 |
| [CyberClaw](https://github.com/ttguy0707/C