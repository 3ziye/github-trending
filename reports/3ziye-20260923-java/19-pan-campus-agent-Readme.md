# pan-ai-agent


[![Java](https://img.shields.io/badge/Java-21-orange?logo=openjdk)](https://openjdk.org/)
[![Spring Boot](https://img.shields.io/badge/Spring%20Boot-3.4-brightgreen?logo=springboot)](https://spring.io/projects/spring-boot)
[![Spring AI](https://img.shields.io/badge/Spring%20AI-1.0-6DB33F?logo=spring)](https://docs.spring.io/spring-ai/reference/)
[![Vue](https://img.shields.io/badge/Vue-3-42b883?logo=vuedotjs)](https://vuejs.org/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](#许可证)

帮助新生与在校生完成校园知识问答、室内外寻路、设施检索、课表查询，以及报到入住等**多步任务的自主拆解与规划**。

---

## 目录

- [项目简介](#1-项目简介-overview)
- [核心特性](#2-核心特性-core-features)
- [技术栈](#3-技术栈-tech-stack)
- [快速启动指南](#4-快速启动指南-quick-start)
- [项目结构与维护说明](#5-项目结构与维护说明)
- [接口一览](#接口一览)
- [可选能力](#可选能力pgvector--mcp)

---

## 1. 项目简介 (Overview)

`pan-ai-agent` 系统面向虚构校园「星辰大学」，用大模型编排检索与工具，而不是把校规、路线硬编码进 Prompt。

| 能力 | 说明 | 产品入口 |
|------|------|----------|
| 校园问答 | 外置 Markdown 知识库 + 向量检索（RAG），回答门禁、食堂、报到流程等 | `/school-assistant` |
| 路线与生活工具 | 调用校园工具完成「从 A 到 B」「最近的打印店」「明天有没有课」 | 问答 / 规划均可 |
| 多步自主规划 | ReAct 循环拆解复杂指令（如新生报到全流程），逐步调用工具并汇总方案 | `/campus-agent` |

两条链路共用同一套窗口记忆与校园工具，前端通过 **SSE** 实时展示生成过程。

```
浏览器 (Vue 3 :3000)
        │  EventSource / SSE
        ▼
AiController  (:8123/api)
   ├─ /ai/campus/chat/sse      → SchoolAssistant（RAG Advisor + 工具）
   └─ /ai/campus-agent/chat    → CampusAgent（ReAct think → act → observe）
        │
        ├─ ConversationMemoryStore（按 chatId 保留最近 10 条）
        ├─ campus_knowledge.md → Header 切分 → Embedding → VectorStore
        └─ Campus Tools / MCP（路线、设施、课表、知识检索…）
```

核心开发与包名统一为 **`pan`**（`com.pan.panaiagent`）。

---

## 2. 核心特性 (Core Features)

### 动态层级 RAG

知识库外置为 Markdown，**不写进 Java 代码**。启动时 `CampusDocumentLoader` 优先读取 classpath 资源，若不存在则回退到运行目录下的 `data/campus_knowledge.md`。`MarkdownHeaderTextSplitter` 按 `###`、`##` 标题切块，并写入 `header` / `parent_header` / `header_level` 元数据，再交给 Spring AI `SimpleVectorStore`（可切换 PgVector）。

检索为空时走固定兜底话术（「该信息暂未收录，建议咨询辅导员」），降低幻觉。

### 多轮对话记忆

`ConversationMemoryStore` 基于 Spring AI `MessageWindowChatMemory`，以 **`chatId`（conversationId）** 隔离会话，窗口上限 **10 条消息**（约 5 轮）。支持「上一轮问博学楼，这一轮说怎么走过去」这类**指代消解**。问答助手通过 `MessageChatMemoryAdvisor` 自动注入；规划智能体在 `BaseAgent` 中手动 load / persist，避免单例 Agent 状态串扰。

### ReAct 思考链路追踪

规划智能体关闭框架内置自动 Tool Calling，自行实现 `think` → `act` → `observation`。控制台由 `ReActTraceLogger` 打印标准三行日志，便于调试且不干扰前端 Loading：

```text
[Thought]：星辰校园百事通 | 用户要从桃李苑去博学楼，应调用路线工具
[Action]：get_campus_route | {"startLocation":"桃李苑","endLocation":"博学楼"}
[Observation]：get_campus_route | 从 桃李苑 出发，沿紫藤长廊步行至喷泉广场...
```

### 校园 MCP / 工具调用

通过 `@Tool` 注册校园服务，模型按意图选择调用：

| 工具名 | 用途 |
|--------|------|
| `get_campus_route` | 校园路线规划（未知地点拒绝编造） |
| `find_nearest_facility` | 最近快递点 / 食堂 / 打印店 / 便利店 |
| `query_student_schedule` | 按日期查询课表 |
| `search_campus_knowledge` | Agent 主动检索知识库（Top-3） |
| `doTerminate` | 多步任务正常结束 |

另可选接入独立 MCP Server（图片搜索、高德地图等），与主进程解耦。

---

## 3. 技术栈 (Tech Stack)

| 层级 | 技术 | 说明 |
|------|------|------|
| 语言 | Java 21 | `pom.xml` 中 `java.version` |
| 后端 | Spring Boot 3.4.4 | Web、配置、测试 |
| LLM 主路径 | Spring AI 1.0 + Spring AI Alibaba DashScope | 默认模型 `qwen-plus` |
| LLM 对照 | LangChain4j DashScope | `demo/invoke` 示例 |
| 向量存储 | SimpleVectorStore（默认内存） / PgVector（可选） | Embedding 使用 DashScope |
| 实时传输 | SSE（`Flux` / `SseEmitter`） | 问答逐 token、规划按步骤推送 |
| 前端 | Vue 3 + Vite 4 + Vue Router 4 | 开发端口 `3000` |
| 协议 | Spring AI MCP Client / Server | 可选工具外置 |
| 文档 | Knife4j OpenAPI3 | `/api/swagger-ui.html` |

---

## 4. 快速启动指南 (Quick Start)

### 4.1 环境要求

- **JDK 21**（项目按 21 编译；生态兼容 JDK 17+，但请以本仓库 `pom.xml` 为准）
- **Maven 3.8+**（仓库已包含 Maven Wrapper：`mvnw` / `mvnw.cmd`，可无需全局安装 Maven）
- Node.js 18+（仅当前端开发时需要）
- 阿里云百炼 / DashScope API Key

### 4.2 环境变量配置（必须）

**必须设置 `DASHSCOPE_API_KEY`。严禁把真实密钥写入 `application.yml`、`application-local.yml` 或任何会提交到 Git 的文件。**

仓库配置已使用占位符：

```yaml
spring:
  ai:
    dashscope:
      api-key: ${DASHSCOPE_API_KEY}
```

按操作系统设置：

```powershell
# Windows PowerShell（当前会话）
$env:DASHSCOPE_API_KEY = "你的密钥"

# 可选：网页搜索工具
$env:SEARCH_API_KEY = "你的 SearchAPI 密钥"
```

```bash
# macOS / Linux（当前会话）
export DASHSCOPE_API_KEY="你的密钥"
export SEARCH_API_KEY="你的 SearchAPI 密钥"   # 可选
```

长期生效请写入用户环境变量或 CI Secret，不要提交 `.env` 到版本库。

> 本地 profile 为 `local`（见 `application.yml`）。`application-local.yml` 同样只引用环境变量，不会也不应出现明文 Key。

### 4.3 编译与运行（后端）

在**本仓库根目录**（含 `pom.xml` 与 `mvnw` 的目录）执行：

```bash
# 使用 Wrapper 启动（推荐）
./mvnw spring-boot:run          # macOS / Linux
.\mvnw.cmd spring-boot:run      # Windows
```

或先打包再运行：

```bash
./mvnw clean package -DskipTests
java -jar target/pan-ai-agent-0.0.1-SNAPSHOT.jar
```

启动成功后：

| 项目 | 地址 |
|------|------|
| 服务端口 | `http://localhost:8123` |
| Context Path | `/api` |
| 健康检查 | [http://localhost:8123/api/health](http://localhost:8123/api/health) |
| API 文档 | [http://localhost:8123/api/swagger-ui.html](http://localhost:8123/api/swagger-ui.html) |

无 PostgreSQL、无 MCP 进程即可启动：主应用已排除数据源自动配置，PgVector 与 MCP Client 在配置中默认注释。

### 4.4 启动前端（可选）

```bash
cd pan-ai-agent-frontend
n