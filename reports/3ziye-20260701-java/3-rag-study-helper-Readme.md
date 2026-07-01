
<p align="center">
  <img src="rag-comic.png" alt="RAG Study Helper" width="720">
</p>

<h1 align="center">RAG Study Helper</h1>

<p align="center">
  <strong>企业级 RAG（检索增强生成）问答系统</strong>
  <br>
  Spring Boot 2.6 · LangChain4j 0.35 · 多源知识库 · 分布式限流
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Java-8-%23ED8B00?logo=openjdk">
  <img src="https://img.shields.io/badge/Spring_Boot-2.6.13-%236DB33F?logo=spring">
  <img src="https://img.shields.io/badge/LangChain4j-0.35.0-blue">
  <img src="https://img.shields.io/badge/Redisson-4.5.0-%23DC382D?logo=redis">
  <img src="https://img.shields.io/badge/license-MIT-green">
</p>

> ⚠ **JDK 8 兼容说明：** LangChain4j 从 0.36.0 起要求 JDK 17，本项目使用最后支持 JDK 8 的 0.35.0。因此 Chroma 服务端锁定为 0.4.24（0.6.x+ API 不兼容），Milvus 使用 2.3.x。如需升级新版，需同时升级 JDK 17 + Spring Boot 3.x。

---

## 目录

- [系统架构](#系统架构)
- [快速开始](#快速开始)
- [LLM 配置](#llm-配置)
- [向量数据库](#向量数据库)
- [文档入库](#文档入库)
- [飞书知识库同步](#飞书知识库同步)
- [API 参考](#api-参考)
- [限流策略](#限流策略)
- [项目结构](#项目结构)
- [测试](#测试)
- [技术栈](#技术栈)

---

## 系统架构

![系统架构图](rag.png)

```
┌──────────────────────────────────────────────────────────────┐
│                     Web UI (index.html)                       │
│     SSE 流式渲染 · Markdown 解析 · 会话管理 · 知识库面板       │
│     深色/亮色主题 · 移动端适配 · 消息复制 · 自定义提示框       │
└───────────────────────┬──────────────────────────────────────┘
                        │ POST /api/chat {sessionId, question}
                        ▼
┌──────────────────────────────────────────────────────────────┐
│                    RateLimitAspect (@RateLimit)               │
│        Redisson 令牌桶（IP + 全局每日）                       │
│        429 → 统一 Results 格式返回                            │
└───────────────────────┬──────────────────────────────────────┘
                        ▼
┌──────────────────────────────────────────────────────────────┐
│                      ChatController                           │
│            SseEmitter (60s timeout) · Jackson 序列化          │
└───────────────────────┬──────────────────────────────────────┘
                        ▼
┌──────────────────────────────────────────────────────────────┐
│                       RAG Pipeline                            │
│                                                               │
│  ┌──────────────┐   ┌───────────────┐   ┌─────────────────┐  │
│  │  会话历史      │──▶│  Query        │──▶│  Embedding      │  │
│  │  Redis        │   │  Rewriting    │   │  BGE-large-zh   │  │
│  └──────────────┘   └───────────────┘   └───────┬─────────┘  │
│                                                  ▼            │
│                                           ┌────────────┐     │
│                                           │ Vector      │     │
│                                           │ Store       │     │
│                                           │ top 20      │     │
│                                           └─────┬──────┘     │
│                                                  ▼            │
│  ┌──────────────┐   ┌───────────────┐   ┌─────────────────┐  │
│  │ LLM 回答      │◀──│ Prompt 组装    │◀──│ Rerank          │  │
│  │ DeepSeek /    │   │ 引用 + 约束   │   │ BGE-reranker   │  │
│  │ OpenAI 兼容   │   │              │   │ top 5          │  │
│  └──────────────┘   └───────────────┘   └─────────────────┘  │
│                                                               │
│  ┌───────────────────────────────────────────────────────┐    │
│  │ 文档来源                                               │   │
│  │  ├─ Web 上传（Multipart, SHA256 去重）                 │   │
│  │  ├─ 目录扫描（data/docs/ 自动扫描）                    │   │
│  │  └─ 飞书知识库同步（Feishu Wiki Sync）                 │   │
│  └───────────────┬───────────────────────────────────────┘    │
│                  │ 元数据                                     │
│                  ▼                                            │
│  ┌──────────────────────────────────────────────────────┐    │
│  │              MySQL + MyBatis-Plus                     │    │
│  │  documents（文档元数据） · document_chunks（分块映射） │   │
│  └──────────────────────────────────────────────────────┘    │
└──────────────────────────────────────────────────────────────┘

                         ┌────────────┐
                         │   Redis    │ ← 多实例共享会话 + 分布式限流
                         └────────────┘
```

---

## 快速开始

### 前置条件

- Docker（推荐）或 JDK 8+（本地运行）
- API Key：Chat 模型 + Embedding 模型的密钥

> 默认使用 DeepSeek 作为对话模型、SiliconFlow 作为 Embedding/Rerank 服务商。
> 可通过环境变量切换任意 OpenAI 兼容 API，参考 [LLM 配置](#llm-配置)。

### Docker Compose（推荐）

```bash
# 1. 复制环境变量模板并填入密钥
cp .env.example .env

# 2. 选择向量库并启动
#    InMemory（零外部依赖，重启数据丢失）
docker compose up -d
#    或 Chroma（持久化，中型项目）
docker compose -f docker-compose-chroma.yml up -d
#    或 Milvus（分布式，生产级）
docker compose -f docker-compose-milvus.yml up -d

# 3. 查看日志
docker compose logs -f

# 4. 访问 http://localhost:8080
```

Docker Compose 会同时启动以下服务：

| 服务 | 镜像 | 说明 |
|------|------|------|
| app | 本地构建 | Spring Boot 应用，端口 8080 |
| mysql | mysql:8.0 | 文档元数据存储