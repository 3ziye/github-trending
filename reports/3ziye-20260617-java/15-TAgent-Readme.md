# TAgent

TAgent 是一个基于 Java 17、Spring Boot、Spring AI 和 DDD 分层构建的 AI Agent 工程实践项目。

它不是只封装一次模型调用，而是覆盖了一次 Agent 请求从接入、路由、运行时装配、规划执行、RAG、记忆、MCP 工具治理、人工审批、执行中干预，到 SSE 流式输出和全链路观测的完整过程。

本仓库是脱敏后的公开版本，不包含真实密钥、运行日志、历史对话、临时报告、数据库备份和个人文件。

## 系统总览

![TAgent 端到端架构](docs/images/tagent-end-to-end-architecture-2026-06-v2.png)

主链路：

```text
用户请求
  -> Filter / SSE Controller
  -> UnifiedAgentRouter
  -> Fixed / Auto / Flow
  -> Advisor + LLM
  -> MCP 工具执行
  -> SSE 流式响应
```

主链之外还有几条关键控制链：

- 动态工具补充：路由判断缺失能力，PgVector 从工具目录中匹配真实 MCP 工具，再与 Agent 常驻工具合并。
- 执行中干预：用户可以发送 `steer` 重做当前步骤，发送 `answer_now` 跳过剩余步骤并进入 finalize，也可以通过 `cancel` 显式中断当前执行。
- 主动追问：模型缺少关键信息时可调用 `ask_user`，经 `user_input_required` SSE 事件向用户收集补充，再回填到模型上下文继续执行。

## 项目亮点

| 能力 | 实现 |
|---|---|
| 三种 Agent 模式 | Fixed 单步直答、Auto 分析执行闭环、Flow DAG 编排 |
| 数据库驱动装配 | Agent、Client、Model、Prompt、Advisor、RAG、MCP 关系由数据库配置 |
| 统一 Agent 路由 | 一次模型调用选择 Agent，并输出可能缺失的工具能力 |
| 动态 MCP 工具 | 工具目录中文化、意图扩写、PgVector 语义匹配、按请求临时补挂 |
| MCP 自愈 | 懒探活、失败重试、超时重连、dead-client 重建、冷却与熔断 |
| 工具治理 | 非执行步禁工具、未知工具纠正、参数提示、轮次预算、跨 MCP 并行 |
| Agentic RAG | SIMPLE、HyDE、FUSION、DECOMPOSE 四种查询策略 |
| 四层记忆 | Working、Chat、Long-Term、Episodic Memory |
| 流式干预 | Auto、Flow、Fixed 均支持立即回答、引导与取消执行 |
| 主动追问 | `ask_user` 通过 SSE 向用户请求补充信息，默认关闭、按 session 限次和超时 |
| 人机协同 | 高风险工具调用通过 SSE 请求人工批准或拒绝，主动追问与审批通道隔离 |
| 可解释输出 | 工具进度、RAG evidence、Memory evidence、步骤状态 |
| 全链路观测 | Prometheus、ELK、Jaeger、event_log、LLM 成本与 MCP 健康页 |

## 端到端请求流程

### 1. 接入与 SSE 建连

请求进入 `POST /api/v1/agent/auto_agent` 后依次经过：

1. `MdcTraceFilter`：写入 request、trace、user、tenant、session 等上下文。
2. `RateLimitFilter`：按用户、会话或 IP 进行限流。
3. `IdempotencyFilter`：同步请求支持幂等，SSE 长连接端点直接放行。
4. `AiAgentController`：创建 `ResponseBodyEmitter`、注册审批通道并立即发送 `ack`。
5. Controller 组装 `ExecuteCommandEntity`，交给 Dispatch 异步执行。

`ack` 会携带干预能力是否开启，前端据此决定是否显示执行中的操作栏。

### 2. 统一路由与懒装配

`AgentDispatchDispatchService` 负责：

- 用户未指定 Agent 时，调用 `UnifiedAgentRouter` 选择最合适的 `agent_id`。
- 用户已经指定 Agent 时，跳过 Agent 选择，但仍可推断缺失工具能力。
- 路由结果同时返回 `missing_tool_descs`，用于后续动态补工具。
- 首次使用 Agent 时通过 Armory 懒加载 ChatClient、Model、Advisor 和 MCP callback。
- 从数据库读取 Agent 的 `strategy`，分派到 Fixed、Auto 或 Flow。

运行时装配关系主要来自：

- `ai_agent`
- `ai_client`
- `ai_client_model`
- `ai_client_api`
- `ai_client_system_prompt`
- `ai_client_advisor`
- `ai_client_tool_mcp`
- `ai_client_rag_order`

数据库配置在 Armory 装配后会进入 Bean 缓存，修改核心模型、Prompt 或工具关系后建议重新装配或重启应用。

## 三种执行模式

### Fixed

适合直接问答或单轮工具任务：

```text
准备上下文 -> 注入 Advisor -> 合并工具 -> LLM 流式生成 -> 保存记忆 -> 输出
```

Fixed 也支持：

- MCP 工具调用
- RAG 与长期记忆
- `steer` 中断后重新生成
- `answer_now` 基于已有半截输出立即收尾

### Auto

适合目标明确但需要自主分析、执行和检查的任务：

| 步骤 | 职责 | 是否开放工具 |
|---|---|---|
| Step1 | 分析任务、判断完成度 | 否 |
| Step2 | 执行具体任务 | 是 |
| Step3 | 质量检查与 Reflexion | 否 |
| Step4 | 汇总最终结果 | 否 |

Auto 会循环执行，直到任务完成或达到 `maxStep`。当 Step3 判断失败时，可携带结构化 critique 返回 Step2 修正。

### Flow

适合可拆解、存在依赖关系的复杂任务：

| 步骤 | 职责 | 是否开放工具 |
|---|---|---|
| Step1 | 分析需要的工具能力 | 否 |
| Step2 | 生成带 `DEPENDS_ON` 的步骤计划 | 否 |
| Step3 | 将计划解析为 DAG | - |
| Step4 | 按依赖关系并行执行并最终整合 | 是 |

Flow 的并行边界不是无限并发：

- DAG 中依赖已经满足的步骤可以并行。
- 不同 MCP Server 的工具可以并行。
- 同一个 MCP Server 复用同一连接时保持串行，避免传输层并发损坏。

## 动态 MCP 工具补充

固定给每个 Agent 挂大量工具，会增加上下文、工具幻觉和选错工具的概率。TAgent 将工具拆成“常驻工具”和“按请求动态补充工具”。

流程如下：

```text
UnifiedAgentRouter
  -> missing_tool_descs
  -> 每条能力描述生成 embedding
  -> PgVector 查询 mcp_tool_vector
  -> 每类能力取 Top-K
  -> 相对距离阈值过滤
  -> 多类结果并集去重
  -> 懒创建或复用 MCP callback
  -> 常驻工具 + 动态工具
  -> 注入本次请求
```

工具资产由两部分组成：

- MySQL `ai_mcp_tool_catalog`：真实工具名、MCP、原始描述、中文描述和中文意图。
- PgVector `mcp_tool_vector`：用于语义检索的工具向量。

当前工具匹配采用 embedding-only，不回退 BM25 或 LLM rerank。向量服务不可用时宁可跳过动态补挂，也不盲目匹配无关工具。

相关迁移：

- `V041__create_mcp_tool_catalog.sql`
- `V042__add_mcp_tool_description_zh.sql`
- `V046__add_mcp_tool_intent_zh.sql`
- `V047__create_mcp_tool_vector_pg.sql`

## MCP 工具治理与自动重连

MCP 调用不是直接执行裸 callback，而是经过 `MeteredToolCallback`、`RobustToolCallingManager` 和 `McpClientRegistry` 三层治理。

### McpClientRegistry

Registry 维护 MCP Client、工具与 MCP 的映射、重建工厂、最近成功时间、连续失败次数和熔断状态。

自愈路径包括：

1. 工具调用前按需进行懒探活。
2. 首次调用失败后执行有限重试。
3. 超时后再次探活，判断连接仍存活还是已经死亡。
4. dead-client 或发送失败时重建 MCP Client。
5. 重建成功后刷新旧 `MeteredToolCallback` 内部 delegate。
6. 同一 MCP 设置 10 秒重连冷却，避免连续抖动和重连风暴。
7. 连续失败进入熔断状态时跳过无意义重连。

重连后对模型暴露的 ToolDefinition 保持稳定，因此工具参数提示不会因 callback 切换而丢失。

### MeteredToolCallback

每次真实工具调用会处理：

- 工具输入规范化与参数约束提示
- 首次失败、重试、恢复和最终失败统计
- 超时探活与重连
- 高风险工具审批
- 工具结果清洗与长度截断
- `tool_call_start`、`tool_call_end`、`tool_call_error` SSE 事件
- 同 MCP Server 的进程级发送锁

### RobustToolCallingManager

工具循环层负责：

- 非执行步骤不向模型暴露真实 tools schema
- 工具名大小写纠正
- 未知工具返回可用工具列表，让模型自我修正
- 单 Client 串行工具轮次上限
- 同轮不同 MCP Server 工具并行 fan-out
- 工具响应按原顺序合并

### MCP 观测

访问：

```text
http://localhost:8099/observe-mcp.html
```

可以查看：

- Client 状态：`alive`、`dead`、`reconnect_cooldown`、`circuit_open`
- 最近业务成功、探活成功和重连时间
- 首败、恢复、重试、重连失败和冷却命中
- 工具调用次数、延迟、错误率与最近错误样本

## Advisor 链

Advisor 由数据库配置，并按 order 参与请求：

| Advisor | 作用 |
|---|---|
| Semantic Cache | 相似问题命中后直接短路后续链路 |
| Long-Term Memory | 注入长期画像和语义记忆，结束后异步抽取新记忆 |
| Episodic Memory | 注入当前会话或跨会话摘要 |
| Pr