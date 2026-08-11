# MCPX

MCPX 是运行在本地开发环境中的 MCP Runtime（网关）。它通过
Streamable HTTP 把本地 Workspace、源码、变更、命令、任务、环境和扩展能力
安全地提供给 ChatGPT、Claude、Cursor、Grok 等 MCP 客户端。

MCPX 的重点不是增加一个聊天界面，而是提供一套可审计、可恢复、对模型友好
的开发工具协议：客户端可以跨连接恢复同一个 Remote Session，模型可以用文件 SHA、
Edit ID、Task ID、discovery revision 和能力版本避免重复读取和无效重试。

## 能力概览

| 能力 | 说明 |
| --- | --- |
| Remote Session | 持久化 Workspace 会话、角色权限、事件、接力和跨客户端恢复 |
| Workspace | 注册多个项目，并在创建会话时显式绑定项目根目录 |
| Source | 文件窗口、批量读取、搜索、文件列表和有界上下文；返回 SHA-256 与编码/换行元数据 |
| Edit | 精确 replacement、批量变更、原子写、SHA 校验和格式保留 |
| Terminal | 执行命令或项目 Task；短命令内联返回，长命令持久化为 Task |
| Operation | 并行或有依赖地执行多个公开工具，并统一等待、分页、取消和恢复 |
| Project Task | 从项目配置中发现测试、构建和检查任务，并解析诊断信息 |
| Workspace State | 读取 Git 状态、快照、差异、监听结果和项目记忆 |
| Environment | 查看操作系统、架构、Shell、容器、资源、文件系统和工具链 |
| Extension | 发现并调用配置的 Skill 与上游 MCP Server |
| Artifact | 注册、列出和分页读取测试报告、构建产物、覆盖率和日志 |
| Screenshot | 截取显示器或屏幕区域，并通过 MCP ImageContent 返回 |
| Security | OAuth、Bearer、Remote Session ACL、命令/文件策略和语义确认 |
| Observation | 通过本机 Socket 观察工具调用、Task、Edit 和操作事件 |

## 架构

```mermaid
flowchart LR
    Client[ChatGPT / Claude / Cursor / Grok] -->|Streamable HTTP /mcp| Runtime[MCPX Runtime]
    Runtime --> Session[Remote Session / ACL]
    Runtime --> Tools[Core & Support Tools]
    Runtime --> Orchestration[Operation / Plan]
    Runtime --> Extension[Skill / Upstream MCP]
    Runtime --> Observe[Observation / Audit]

    Session --> Workspace[(Registered Workspace)]
    Tools --> Workspace
    Orchestration --> Tools
    Extension --> Skills[Local Skills]
    Extension --> Upstream[Upstream MCP Servers]

    Runtime --> State[(SQLite State)]
    Observe --> State
    Tools --> RuntimeData[Task Logs / Artifacts / Snapshots]
```

MCPX 把客户端连接、持久化 Remote Session、Workspace 能力、执行编排和扩展发现放在同一个
Runtime 边界内；所有有状态操作都绑定 `remote_session_id`，并通过 SQLite、Task 日志、Artifact
与 Observation 保留可恢复和可审计的执行状态。

## 公开工具

`tools/list` 是工具名称、描述、参数 Schema 和 Annotation 的唯一权威来源。
当前公开工具共 18 个，分为 11 个 core tools 和 7 个 support tools：

| 领域 | 工具 | 主要用途 |
| --- | --- | --- |
| Core | `session` | open、attach、close Remote Session |
| Core | `read` | 文件、搜索、列表、上下文和环境读取 |
| Core | `edit` | 精确 replacement、批量编辑、原子写和格式保留；不提供删除 |
| Core | `move_out` | `action=prepare` 只读冻结安全移出 manifest；用户确认后 `action=submit` 将目标移入系统回收站 |
| Core | `observe` | session、task、history、changes、logs、diff 观察 |
| Core | `execute` | 命令或项目 Task 执行，以及 attach、stop、stdin |
| Core | `plan` | create、read、advance、complete、block、replan、deliver |
| Core | `artifact` | 产物登记、列表和分片读取 |
| Core | `discover` | 显式发现 Skill 或上游 MCP，并签发 discovery lease |
| Core | `skill_call` | 调用已由 `discover` 返回的 Skill |
| Core | `mcp_call` | 调用已由 `discover` 返回的上游 MCP 工具 |
| Support | `operation_batch` | 并发或按依赖 DAG 执行多个工具 |
| Support | `operation_manage` | 查询、等待、读取结果、取消和恢复异步操作 |
| Support | `runtime_read` | 读取能力、项目摘要和适用指令 |
| Support | `environment_read` | 读取当前环境或比较环境快照 |
| Support | `environment` | 保存环境快照 |
| Support | `screenshot_capture` | 截取显示器或区域 |
| Support | `secret_provide` | 提供仅驻留内存的 Secret |

所有有状态工具统一使用完整的 `remote_session_id`；`tools/list`、session
bootstrap、capability manifest 和 recovery action 使用同一组名称与 Schema。

## 设计边界

MCPX 同时处理两类 Session：

| 标识 | 生命周期 | 用途 |
| --- | --- | --- |
| `Mcp-Session-Id` | Streamable HTTP 传输层临时标识 | 连接和协议状态，重连或换客户端后可能变化 |
| `remote_session_id` | SQLite 持久化业务标识 | Workspace、角色、Edit、Task、Plan、操作、快照和产物的主键 |

客户端应始终原样保存并复用服务端返回的 `remote_session_id`、`edit_id`、`plan_id`、
`plan_task_id`、`execution_task_id`、`operation_id`、`artifact_id`、`discovery_id` 和
`discovery_revision`，不能自行缩写、猜测或从历史日志重建这些标识。Plan Task 与
执行 Task 是不同命名空间，不存在兼容的通用 `task_id` 字段。

MCPX 只提供 Streamable HTTP 的 `/mcp` 端点，不提供旧版 HTTP+SSE 的 `/sse`
或 `/message` 兼容端点。

## 快速开始

### 环境要求

- Go 1.26.1 或更高版本，具体版本以 `go.mod` 为准。
- 一个需要被 MCPX 管理的本地项目目录。
- 远程访问时需要 HTTPS 反向代理或其他受信任的网络入口。

### 从源码构建

```bash
git clone https://github.com/opentokenz/mcpx.git
cd mcpx
go build -o bin/mcpx ./cmd/mcpx-server
```

本地静态构建可以关闭 CGO：

```bash
CGO_ENABLED=0 go build -o bin/mcpx ./cmd/mcpx-server
```

普通 VCS 构建会从 Go build info 回填当前 Git revision（工作树有未提交变更时带 `-dirty`）；
正式发布仍以 GoReleaser 的 linker flags 为权威来源，同时注入版本、commit 和真实 build time。
CI 会构建带 provenance 的二进制并通过 `mcpx -version` 校验 commit/date 未丢失。

### 启动服务

```bash
./bin/mcpx
```

注册或更新一个 Workspace：

```bash
./bin/mcpx workspace register /path/to/your/project
```

然后启动服务：

```bash
./bin/mcpx
```

默认监听地址和 MCP 端点：

```text
http://127.0.0.1:9090/mcp
```

首次启动会在 `~/.mcpx/`（可用 `MCPX_HOME` 覆盖）初始化运行时目录：

| 路径 | 用途 |
| --- | --- |
| `config.yaml` | 全局监听、鉴权、安全策略和 Workspace 配置 |
| `.mcp.json` | 全局上游 MCP Server 配置 |
| `logs/` | JSONL 审计和运行日志 |
| `skills/` | 可选的本地 Skill 根目录 |
| `workspaces.example.yaml` | Workspace 配置示例 |
| `state/mcpx.db` | Remote Session、Edit、Task、Plan、操作、快照和产物索引 |
| `tasks/` | 持久终端 Task 的日志文件 |

查看版本和命令帮助：

```bash
./bin/mcpx -version
./bin/mcpx -h
```

服务端命令包括：

```text
mcpx [flags]                   启动 Streamable HTTP 服务
mcpx observe [flags] <name>    终端只读观测 Workspace 事件
mcpx workspace register <path> 注册或更新 Workspace
mcpx oauth-register [url]      动态注册 OAuth 客户端