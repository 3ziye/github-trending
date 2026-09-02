# FinSight Enterprise Backend

FinSight Enterprise Backend 是一个基于 Spring Boot 3 的企业级智能管理平台后端。项目围绕企业后台常见能力建设，提供用户、角色、菜单、部门、日志、监控、文件中心、工作流、即时通讯、AI 模型对话与 RAG 知识库能力，适合作为企业内部管理系统、智能办公平台、知识库问答平台的后端基础工程。

> 当前仓库是后端工程。前端工程位于 `../../1web/financial_intelligence_system/`，前端技术栈为 Vue 3、TypeScript、Element Plus。

## 目录

- [项目特性](#项目特性)
- [技术栈](#技术栈)
- [系统架构](#系统架构)
- [目录结构](#目录结构)
- [环境要求](#环境要求)
- [快速启动](#快速启动)
- [配置说明](#配置说明)
- [默认账号](#默认账号)
- [接口文档](#接口文档)
- [核心模块说明](#核心模块说明)
- [RAG 知识库说明](#rag-知识库说明)
- [数据库迁移](#数据库迁移)
- [常用接口](#常用接口)
- [开发规范](#开发规范)
- [安全建议](#安全建议)
- [常见问题](#常见问题)
- [开源说明](#开源说明)

## 项目特性

- 企业级 RBAC 权限体系：用户、角色、菜单、部门、按钮权限、二级/三级/多级菜单。
- JWT + Spring Security：无状态认证、接口权限校验、统一 401 响应。
- Redis 安全增强：登录失败限制、Token 黑名单、在线状态、普通用户单设备在线、管理员强制退出用户。
- 中文 Swagger/OpenAPI：接口分组清晰，支持 Bearer Token 调试。
- 登录日志、操作日志、模型对话日志：满足后台审计和运维追踪。
- 系统监控：服务器、JVM、磁盘、Redis、PostgreSQL 实时指标。
- 文件中心：本地存储和 MinIO/S3 存储可切换，支持上传、下载、在线预览、Office 转 PDF 预览。
- 工作流：基于 Flowable BPMN 2.0 的流程定义、部署、发起、审批、驳回、实例查询。
- 系统内即时通讯：用户单聊、群聊、未读消息、文件消息、撤回、搜索、WebSocket 实时推送。
- AI 模型管理：Chat 模型与 Embedding 模型分开配置，可在管理员后台维护和测试。
- 大模型对话：支持普通对话、SSE 流式输出、会话历史、Markdown 前端渲染。
- RAG 知识库：基于 PostgreSQL 16 + pgvector，支持文档解析、父子切片、向量检索、全文检索、RRF 融合召回、引用来源返回。

## 技术栈

| 类型 | 技术 |
| --- | --- |
| 基础框架 | Java 21、Spring Boot 3.5.4 |
| Web | Spring MVC、Spring Validation |
| 安全 | Spring Security、JWT、BCrypt |
| 数据库 | PostgreSQL 16、pgvector |
| 数据访问 | Spring JDBC `JdbcClient` |
| 数据迁移 | Flyway |
| 缓存/会话 | Redis、Spring Data Redis |
| 接口文档 | SpringDoc OpenAPI、Swagger UI |
| 文件存储 | 本地文件系统、MinIO/S3 |
| 工作流 | Flowable 7.2 |
| 文档解析 | PDFBox、Apache POI |
| Office 预览 | LibreOffice/soffice 转 PDF |
| 实时通信 | Spring WebSocket |

## 系统架构

```text
前端 Vue 3
  |
  | HTTP / SSE / WebSocket
  v
Spring Boot Backend
  |
  |-- Security Filter Chain
  |     |-- JWT 校验
  |     |-- Redis Token 黑名单
  |     |-- 普通用户单设备在线校验
  |
  |-- Controller
  |     |-- AuthController
  |     |-- SystemController
  |     |-- AiController
  |     |-- KnowledgeController
  |     |-- FileController
  |     |-- WorkflowController
  |     |-- ImController
  |     |-- LogController
  |     |-- MonitorController
  |
  |-- Service
  |     |-- AI 调用与流式响应
  |     |-- RAG 文档解析、切片、向量化、混合检索
  |     |-- 文件存储、本地/MinIO 切换
  |     |-- Redis 会话安全
  |     |-- 审计日志
  |
  |-- PostgreSQL 16 + pgvector
  |-- Redis
  |-- MinIO/S3 可选
  |-- 大模型服务 OpenAI Compatible API
```

## 目录结构

```text
Financial_Intelligence_System/
├── pom.xml
├── mvnw
├── README.md
├── HELP.md
├── data/
│   └── uploads/                  # 默认本地文件上传目录
└── src/
    ├── main/
    │   ├── java/com/rpa/financial_intelligence_system/
    │   │   ├── FinancialIntelligenceSystemApplication.java
    │   │   ├── common/            # 统一响应、全局异常处理
    │   │   ├── config/            # 安全、OpenAPI、异步、WebSocket 配置
    │   │   ├── controller/        # REST API 控制器
    │   │   ├── security/          # JWT、用户认证、操作日志过滤器
    │   │   └── service/           # 业务服务、AI、RAG、文件、Redis、IM
    │   └── resources/
    │       ├── application.yaml
    │       └── db/migration/      # Flyway 数据库迁移脚本
    └── test/
```

## 环境要求

- JDK 21+
- Maven 3.9+，也可以直接使用项目自带的 `./mvnw`
- PostgreSQL 16+
- PostgreSQL 扩展：pgvector
- Redis 6+
- 可选：MinIO 或兼容 S3 的对象存储
- 可选：LibreOffice，用于 Word、Excel、PPT 转 PDF 在线预览

## 快速启动

### 1. 创建数据库

请先确认 PostgreSQL 已安装 pgvector 扩展。macOS 可通过 Homebrew 安装：

```bash
brew install pgvector
```

创建数据库：

```bash
createdb -U postgres financial_ai
```

如果需要手动初始化扩展：

```sql
CREATE EXTENSION IF NOT EXISTS vector;
```

### 2. 启动 Redis

本地默认连接：

```text
host: localhost
port: 6379
password: 空
```

### 3. 修改配置

默认配置位于 `src/main/resources/application.yaml`，也可以通过环境变量覆盖。

本地默认数据库配置：

```yaml
spring:
  datasource:
    url: jdbc:postgresql://localhost:5432/financial_ai
    username: postgres
    password: 123456
```

### 4. 启动后端

```bash
./mvnw spring-boot:run
```

默认访问地址：

```text
http://localhost:8080
```

### 5. 编译检查

```bash
./mvnw -DskipTests compile
```

## 配置说明

项目支持通过环境变量覆盖核心配置，适合本地开发、测试环境和生产环境分别配置。

| 环境变量 | 默认值 | 说明 |
| --- | --- | --- |
| `SERVER_PORT` | `8080` | 后端服务端口 |
| `DB_URL` | `jdbc:postgresql://localhost:5432/financial_ai` | PostgreSQL JDBC 地址 |
| `DB_USERNAME` | `postgres` | 数据库用户名 |
| `DB_PASSWORD` | `123456` | 数据库密码 |
| `REDIS_HOST` | `localhost` | Redis 地址 |
| `REDIS_PORT` | `6379` | Redis 端口 |
| `REDIS_PASSWORD` | 空 | Redis 密码 |
| `JWT_SECRET` | 开发默认值 | JWT 签名密钥 |
| `JWT_EXPIRATION_HOURS` | `12` | Token 有效小时数 |
| `LIBREOFFICE_COMMAND` | `soffice` | LibreOffice 命令路径 |
| `OFFICE_PREVIEW_TIMEOUT_SECONDS` | `60` | Office 转 PDF 超时时间 |
| `AI_BASE_URL` | `https://api.openai.com/v1` | 默认 Chat API 基础地址 |
| `AI_API_KEY` | 空 | 默认模型 API Key |
| `AI_CHAT_MODEL` | `gpt-4.1-mini` | 默认 Chat 模型 |
| `AI_EMBEDDING_MODEL` | `text-embedding-3-small` | 默认 Embedding 模型 |
| `AI_EMBEDDING_DIMENSIONS` | `1536` | 默认 Embedding 维度 |

> 生产环境必须覆盖 `JWT_SECRET`，并且不要把任何真实 API Key、MinIO Secret、数据库密码提交到 GitHub。

## 默认账号

Flyway 初始化脚本会创建一个超级管理员账号：

```text
用户名：admin
密码：Admin@123
```

该账号拥有全部菜单和接口权限，建议首次部署后立即修改密码。

## 接口文档

启动后访问：

```t