<div align="center">

# claude-code-java

**可嵌入任何 Java 应用的 AI Agent 引擎 — CLI · REST API · Web Playground**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Java](https://img.shields.io/badge/Java-17+-orange.svg)](https://openjdk.org/)
[![Spring Boot](https://img.shields.io/badge/Spring%20Boot-3.2-green.svg)](https://spring.io/projects/spring-boot)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Stars](https://img.shields.io/github/stars/fluentlc/claude-code-java?style=social)](https://github.com/fluentlc/claude-code-java/stargazers)

[中文](#中文) | [English](#english)

</div>

---

## 中文

### 这是什么？

**claude-code-java** 是一个可嵌入任何 Java 应用的 AI Agent 引擎。它兼容 **OpenAI Chat Completions 协议**，可对接 OpenAI、Azure OpenAI、Ollama、DashScope 或任何兼容端点，同时也支持直接对接 Anthropic Messages API。

提供三种开箱即用的交互方式：
- **CLI 模式** — 终端 REPL，适合本地开发和调试
- **REST API 模式** — 标准 HTTP 接口（同步），适合集成到其他系统
- **Web Playground** — 内置实时流式对话界面，可视化 Agent 工作过程

所有能力都源自同一个核心循环：

```java
// AI Agent 的本质
while ("tool_calls".equals(finishReason)) {
    response = client.chat(messages, tools);
    executeTools(response);    // 执行工具调用
    appendResults(messages);   // 将结果追回对话
}
// 10 项核心能力只是往这个循环里注入新工具和新上下文
```

---

### Web Playground

启动服务后访问 `http://localhost:8080`，无需额外配置即可使用内置的对话界面。

```
┌─────────────────────────────────────────────────────────────────┐
│  claude-code-java                                    [新对话]      │
├──────────────────┬──────────────────────────────────────────────┤
│ 对话历史          │                                              │
│                  │  [Context Compressed]  第 1 次压缩  [查看 →]  │
│ > 帮我审查代码    │                                              │
│   创建 Agent 团队 │  ┌─ 🤖 assistant ──────────────────────┐    │
│                  │  │ 我将为你创建两个专家 Teammate...     │    │
│                  │  └─────────────────────────────────────┘    │
│                  │                                              │
│                  │  [reviewer · 正在执行 read_file ···]         │
│                  │  [tester   · 正在执行 write_file ···]        │
│                  │                                              │
│                  │  ┌ ── ── ── ── ── ── ── ── ── ── ── ── ┐    │
│                  │    ✦ reviewer 完成（12 个工具）[工作区 →]     │
│                  │  └ ── ── ── ── ── ── ── ── ── ── ── ── ┘    │
│                  │                                              │
│                  │  [输入消息...                    发送]        │
└──────────────────┴──────────────────────────────────────────────┘
                                                 ┌──── 工作空间 ────┐
                                                 │ 第1次  第2次      │
                                                 │ [压缩前完整历史]  │
                                                 │ [Teammate 工具流]│
                                                 └──────────────────┘
```

**核心交互特性：**

| 特性 | 说明 |
|------|------|
| **流式渲染** | 思考过程、工具调用、文字回复逐 token 实时呈现 |
| **思考卡片** | 执行中展开、完成自动折叠，显示耗时 |
| **工具卡片** | 展示 Input/Output，执行完自动折叠 |
| **压缩卡片** | 上下文压缩后不中断对话，卡片展示摘要 + 可进入历史抽屉 |
| **Teammate 悬浮条** | Agent Teams 工作时输入框上方实时显示各 Teammate 状态 |
| **工作空间抽屉** | 右侧滑入面板，按 Tab 区分各次压缩历史和各 Teammate 工作细节 |
| **压缩链导航** | 多次压缩形成链式历史，可逐层回溯查看每次压缩前的完整对话 |
| **会话侧边栏** | 历史会话持久化，点击即恢复完整对话流（含所有卡片） |
| **Markdown 渲染** | 所有 AI 回复、摘要均支持完整 Markdown 格式 |

---

### 架构

```
claude-code-java （父 pom）
├── claude-code-java-service  —— 纯 Java 17 库（无框架依赖）
│   ├── core/        OpenAiClient · AnthropicClient · ClientFactory
│   │                BaseTools · SecurityUtils · ShellUtils · ToolHandler
│   ├── capability/  TodoManager · ContextCompactor · BackgroundRunner
│   │                TaskStore · WorktreeManager · SkillLoader
│   │                MessageBus · TeammateRunner · SessionStore
│   │                TeamProtocol · TaskPoller
│   ├── tool/        8 个 ToolProvider
│   └── agent/       AgentLoop · TeammateLoop · AgentAssembler · SlashRouter
│
└── claude-code-java-start    —— Spring Boot 3.2 应用层
    ├── Application.java     统一入口
    ├── cli/CliRunner        @Profile("cli") REPL
    ├── web/controller/      ChatController（REST + SSE 流式端点）
    ├── web/service/         StreamService（AgentEventListener → SSE 事件）
    │                        ChatService（同步对话）
    ├── config/AgentBeans   Spring @Bean 配置
    └── resources/static/   index.html（Web Playground 单页应用）
```

---

### 10 项核心能力

| 能力 | 说明 |
|------|------|
| **TodoManager** | Agent 自我跟踪任务，每 3 轮未完成自动触发提醒 |
| **SkillLoader** | 从 `./skills/` 目录按需注入技能提示词，不污染主上下文 |
| **ContextCompactor** | 三层压缩管道（微压缩 → 自动压缩 40 条消息 → 手动 `/compact`），压缩历史持久化为 `.transcripts/` 文件 |
| **TaskStore** | JSON 文件持久化任务状态，含依赖图，重启后自动恢复 |
| **BackgroundRunner** | 线程池异步执行，fire-and-forget，完成后通知注入主循环 |
| **MessageBus** | JSONL 格式收件箱/发件箱，支持多 Agent 间消息传递 |
| **TeammateRunner** | Agent Teams 核心 — 动态 spawn Teammate，每个 Teammate 在独立线程中运行完整 LLM 循环，通过 MessageBus 通信、TaskStore 自主认领任务；会话实时持久化（每次工具调用后），Web Playground 可实时查看 |
| **Session