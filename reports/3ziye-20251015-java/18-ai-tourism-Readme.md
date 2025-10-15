# AI 智能旅游规划助手（后端）

> **访问地址**：[https://www.aitrip.chat/](https://www.aitrip.chat/)  
> **欢迎体验智能旅游规划服务！**

## 📖 项目简介

**AI-Tourism** 是一个智能旅游规划系统，后端基于 **Spring Boot、LangChain4j、MySQL、MyBatis、Sa-Token** 等技术栈构建。

系统集成了多种 AI 能力（如 AI Service、MCP 工具等），为用户提供**个性化旅游路线推荐、多轮对话、权限控制**等功能。

### 🎯 核心特性
- **多轮对话与上下文记忆** - 智能理解用户需求，保持对话连贯性
- **地图路线可视化** - 实时展示旅游路线，直观易懂
- **MCP 灵活热插拔** - 工具可动态启用/禁用，支持热插拔
- **Tool 统一注册** - 所有工具统一管理，易于扩展
- **安全认证与权限管理** - 完善的用户权限体系

---

### 🖼️ AI 智能旅游规划 前端效果截图
![前端效果图](assets/界面图.png)

### 📹 视频效果
![演示视频](./assets/demo.gif)

**AI 智能旅游规划系统**，结合 `SpringBoot` 与 `LangChain4j`，在用户输入自然语言后，由 **AI Agent** 调用 **MCP 工具**与 **Function Call** 获取天气、景点等信息，由前端同时渲染文字版路线规划与结构化地图路线。

---

## 💡 核心特性与架构特点

![核心特性与架构特点](assets/核心特性与架构特点.png)

### 1. Agent 服务与地图路线渲染深度结合
- **图文结合**：提供图文结合的旅游攻略，并在前端地图中直观展示每日路线
- **流式传输**：使用 `SSE` 流式传输文字版攻略，并基于 `JSON Schema` 输出结构化数据，支持前端实时渲染

### 2. 基于 Langchain4j 的 Agent 服务
- **任务规划**：基于 `Prompt` 工程，设计角色定位 + 任务目标 + 约束限制
- **工具调用**：`MCP` 工具通过配置可灵活启用/禁用，支持热插拔；所有 `Tool` 工具均实现统一接口，注册到 `ToolManager`，支持运行时动态扩展与管理
- **多轮记忆**：实现 `ChatMemoryStore`，短期记忆优先存储于 `Redis`，未命中自动回退数据库，`AI Service` 实例以会话为单位缓存，支持多用户并发与上下文隔离
- **结构化输出路线**：基于 `JSON Schema` 输出结构化路线数据，用于前端地图渲染展示
- **安全防范**：`LangChain4j` 输入护轨机制，前置校验请求内容，防止敏感词与 `Prompt` 注入攻击，保障系统稳定性

### 3. 统一工具注册与高性能调用防抖
- **MCP 工具**：通过配置可灵活启用/禁用，支持热插拔
- **Function Call 工具**：通过 `ToolManager` 统一注册与调度，支持运行时扩展
- **性能优化**：引入 `Caffeine` 缓存，避免重复调用外部服务，**平均响应耗时从 5.20s 下降至 399μs**

### 4. 多轮对话记忆与实例隔离
- **记忆管理**：结合 `Redis` 与数据库实现短期记忆，使用数据库实现会话历史
- **实例缓存**：基于 `Caffeine` 缓存 `AI Service` 实例，支持会话隔离，提升服务响应性能并减少实例重复创建
- **性能提升**：实例平均创建时间由 **13.1ms 降低至 9.74ms，性能提升 28.4%**

### 5. AI 输入护轨与结构化输出
- **安全校验**：请求前置校验，自动过滤敏感词、恶意注入等风险内容，保障系统安全

### 6. Sa-Token 权限认证
- **令牌机制**：`JWT` 短期令牌 + `Refresh Token` 长期令牌结合
- **权限控制**：注解式权限控制，细粒度角色管理

### 7. SpringBoot 工程化与 RESTful 设计
- **分层架构**：标准的分层架构（`Controller` - `Service` - `Mapper`）
- **接口规范**：接口统一，符合 `RESTful` 规范，易于前后端协作

---

## 🏗️ 系统整体架构



- **前端（ai-tourism-frontend）**：`Vue` 应用，负责交互、地图渲染与对话展示；通过 `SSE` 调用 `POST /ai_assistant/chat-stream` 实时消费模型输出

- **接入层（Controller + 鉴权）**：基于 `Spring Boot REST`，使用 `Sa-Token` 进行登录与权限校验（如 `@SaCheckLogin`、`@SaCheckPermission`）

- **服务层（MemoryChatServiceImpl）**：统一处理请求校验、获取会话历史、获取会话列表、消息入库、`SSE` 流式返回

- **AI Service（MemoryAssistantServiceFactory）**：按会话构建隔离的 `AssistantService` 实例，整合 `OpenAI` 流式模型、`MessageWindowChatMemory`（基于 `ChatMemoryStore`）、输入护轨、工具调用；同时使用 `Caffeine` 按 `sessionId` 缓存实例，避免重复创建

- **记忆与历史（Redis + MySQL）**：
  - **短期对话记忆**：`CustomRedisChatMemoryStore` 基于 `Redis` 进行管理，同时支持 `MySQL` 消息填入
  - **长期历史与结构化数据**：通过 `MyBatis` 写入 `MySQL`（会话表、消息表、路线 JSON）

- **工具调用（Function Call + MCP）**：
  - **Function Call**：`ToolManager` 统一注册所有 `BaseTool`
  - **MCP**：基于 `LangChain4j MCP`，`McpClientService` 通过 `SSE` 创建 `ToolProvider`

- **缓存与防抖**：
  - **Caffeine**：缓存 `AssistantService` 实例
  - **Redis**：承载对话记忆，降低数据库读写压力

- **可观测性与监控**：`Micrometer`` 暴露 `Prometheus` 指标（管理端点已开放 `prometheus`）；`AiModelMonitorListener`/`AiModelMetricsCollector` 记录请求量、耗时、Token 使用、错误率、缓存命中等；Grafana 仪表盘见 `doc/Prometheus-Grafana.json`

---

## 🚀 快速开始

### 📂 目录结构

```
ai-tourism/
├── src/
│   ├── main/
│   │   ├── java/com/example/aitourism/
│   │   │   ├── ai/                  # AI Agent、工具、记忆、护轨等核心AI能力
│   │   │   ├── config/              # 配置类（如Sa-Token、CORS、Redis等）
│   │   │   ├── controller/          # REST API 控制器
│   │   │   ├── dto/                 # 数据传输对象
│   │   │   ├── entity/              # 实体类
│   │   │   ├── exception/           # 全局异常处理
│   │   │   ├── mapper/              # MyBatis 映射
│   │   │   ├── monitor/             # 监控与埋点
│   │   │   ├── service/             # 业务逻辑与AI集成
│   │   │   └── util/                # 工具类
│   │   └── resources/
│   │       ├── application.yml      # 主要配置文件
│   │       └── prompt/              # AI Prompt 模板
├── sql/
│   └── create_table.sql             # 数据库表结构
├── doc/
│   ├── API.md                       # 接口文档
│   └── Prometheus-Grafana.json      # 监控仪表盘配置
├── pom.xml                          # Maven 依赖
└── README.md
```

### 🛠️ 技术栈与依赖

| 技术分类 | 技术栈 | 版本/说明 |
|---------|--------|----------|
| **核心框架** | Java | `21` |
| | Spring Boot | `3.5.6` |
| **AI 能力** | LangChain4j | AI能力集成 |
| **数据库** | MySQL | `9.4` |
| **ORM** | MyBatis & MyBatis-Spring-Boot | 数据持久化 |
| **安全认证** | Sa-Token | JWT 认证与权限 |
| | BCrypt | 密码加密 |
| **工具库** | Lombok | 代码简化 |
| | OkHttp3 | HTTP 客户端 |
| | Hutool | 工具库 |
| **缓存** | Caffeine | 本地高性能缓存 |
| | Redis | 分布式缓存与对话记忆 |
| **监控** | Prometheus + Grafana | 监控与可视化 |
| | Micrometer | Spring Boot 监控埋点 |

> **详见** `pom.xml` 依赖配置

### 🗄️ 数据库结构

#### 主要表设计

| 表名 | 说明 | 主要字段 |
|------|------|----------|
| `t_user` | 用户表 | 手机号、加密密码、昵称、头像、状态等 |
| `t_role` | 角色表 | USER、ROOT 等角色 |
| `t_permission` | 权限表 | 权限标识、权限名称等 |
| `t_user_role` | 用户-角色关联表 | 用户ID、角色ID |
| `t_role_permission` | 角色-权限关联表 | 角色ID、权限ID |
| `t_refresh_token` | 刷新令牌表 | 用户ID、令牌值、过期时间等 |
| `t_ai_assistant_sessions` | 会话列表 | 会话ID、用户ID、会话标题等 |
| `t_ai_assistant_chat_messages` | AI助手消息表 | 消息ID、会话ID、消息内容、角色等 |

> **详细字段和约束**请参考 `