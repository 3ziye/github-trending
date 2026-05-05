<div align="center">

# gpt2api · KleinAI

**面向 GPT / GROK 双账号池的 OpenAI 兼容 AIGC 网关**

一站式覆盖文字、图片、视频生成，多账号池调度 · OpenAI 协议兼容 · 积分计费 · Docker 一键部署

[![Stars](https://img.shields.io/github/stars/432539/gpt2api?style=flat-square&logo=github&color=orange)](https://github.com/432539/gpt2api/stargazers)
[![Forks](https://img.shields.io/github/forks/432539/gpt2api?style=flat-square&logo=github&color=blue)](https://github.com/432539/gpt2api/network/members)
[![Issues](https://img.shields.io/github/issues/432539/gpt2api?style=flat-square&logo=github)](https://github.com/432539/gpt2api/issues)
[![Last Commit](https://img.shields.io/github/last-commit/432539/gpt2api?style=flat-square&logo=git&color=success)](https://github.com/432539/gpt2api/commits/main)
[![Release](https://img.shields.io/badge/release-v2.0.1-brightgreen?style=flat-square)](https://github.com/432539/gpt2api/releases)
[![Go](https://img.shields.io/badge/Go-1.24-00ADD8?style=flat-square&logo=go)](https://go.dev/)
[![React](https://img.shields.io/badge/React-18-61DAFB?style=flat-square&logo=react)](https://react.dev/)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=flat-square&logo=docker)](https://docs.docker.com/compose/)

[功能特性](#-功能特性) · [快速部署](#-快速部署) · [API 兼容性](#-openai-兼容-api) · [配置说明](#-配置说明) · [更新日志](#-更新日志) · [Star 趋势](#-star-趋势)

</div>

---

## 项目简介

`gpt2api`（项目代号 KleinAI）是一个生产级的 **AIGC 聚合网关**，把 GPT / GROK 这类账号 + Cookie 体系的能力，整体封装成 **OpenAI 兼容协议**，让任何按 OpenAI SDK 编写的程序都可以无缝接入。

平台同时提供：

- 一套面向终端用户的创作前台（图 / 文 / 视频）
- 一套面向运营的管理后台（账号池、代理、计费、CDK、日志）
- 一套对外暴露的 OpenAI 兼容 HTTP 接口

适用场景：私有化 AIGC 服务、白标 SaaS、多账号合规分发、内部团队调用聚合。

> 当前默认版本：`v2.0.1`，建议直接以 `v2.0.x` 演进；`v1.0.x` 保留为历史稳定基线。

## ✨ 功能特性

### 创作能力

| 能力 | OpenAI 兼容路由 | 说明 |
|------|----------------|------|
| 文字对话 | `POST /v1/chat/completions` | 支持流式 / 非流式输出 |
| 文生图 | `POST /v1/images/generations` | 支持批量出图、`gpt-image-2` 稳定通道 |
| 图生图 | `POST /v1/images/edits` | 支持参考图、Mask |
| 图片任务查询 | `GET /v1/images/generations/:task_id` | 异步任务进度 / 结果回查 |
| 文 / 图生视频 | `POST /v1/video/generations` | 支持 `quality=standard\|hd`，对应 720p / 1080p |
| 视频任务查询 | `GET /v1/video/generations/:task_id` | 异步任务进度 / 结果回查 |
| 模型列表 | `GET /v1/models` | 由后端模型表统一暴露，可在管理后台维护 |

### 调度与稳定性

- **多账号池**：GPT / GROK 账号批量导入、健康检测、自动刷新、熔断、轮换
- **代理池**：批量导入（`scheme://user:pass@host:port#name`）、批量删除、批量测试
- **代理策略**：账号级绑定优先，全局回落支持「固定代理」与「随机代理」两种模式
- **请求观测**：上游全链路日志可追踪，失败任务可看到完整 provider 报文
- **统一计费**：积分制，按模型 / 分辨率 / 时长可配置

### 运营能力（管理后台）

- 仪表盘、Token（账号）管理、代理管理、用户管理、充值消费
- 优惠码、CDK 兑换、模型价格、系统配置、请求日志、上游日志
- 所有配置尽量表单化，避免裸 JSON 手填

## 🏗️ 技术栈

| 层级 | 选型 |
|------|------|
| 后端 | Go 1.24 · Gin · GORM · MySQL · Redis |
| 前端 | React 18 · Vite · TypeScript · TailwindCSS · pnpm Workspace |
| 部署 | Docker · Docker Compose · Nginx · Caddy（可选） |
| 外部依赖 | FlareSolverr · 代理池 · 对象存储（可选） |

```
┌────────────┐    ┌────────────┐    ┌────────────────────┐
│  用户前台  │    │  管理后台  │    │ OpenAI 兼容 SDK 客户端 │
└─────┬──────┘    └─────┬──────┘    └──────────┬─────────┘
      │ :17080          │ :17088               │ :17200
      ▼                 ▼                      ▼
┌────────────────────────────────────────────────────────┐
│   Nginx / Caddy    （SSL · 反代 · 限流 · 静态资源）       │
└──────┬──────────────┬──────────────────┬───────────────┘
       │              │                  │
   ┌───▼────┐    ┌────▼────┐         ┌───▼─────┐
   │ user-api│    │admin-api│         │openai-api│   ← Go 多服务
   └───┬────┘    └────┬────┘         └───┬─────┘
       └──────┬───────┴──────┬───────────┘
              │              │
        ┌─────▼─────┐  ┌─────▼─────┐
        │   MySQL   │  │   Redis   │
        └───────────┘  └───────────┘
```

## 🚀 快速部署

### 环境要求

- Linux / macOS / Windows（推荐 Linux）
- Docker 24+ 与 Docker Compose v2
- 1 个域名或 3 个子域名（生产部署推荐）
- 80 / 443 端口可用

### 1. 拉取代码

```bash
git clone https://github.com/432539/gpt2api.git
cd gpt2api
```

### 2. 配置环境变量

```bash
cp deploy/env/.env.example deploy/env/.env.prod
# 编辑 .env.prod，重点检查：
#   - 数据库 / Redis 连接
#   - JWT_SECRET / AES_KEY（务必修改！）
#   - 域名 / CORS 来源
#   - GPT / GROK 上游基础地址
#   - 代理 / FlareSolverr 地址
```

### 3. 启动服务

```bash
cd deploy
docker compose -f docker-compose.server.yml up -d --build
```

### 4. 检查状态

```bash
docker compose -f docker-compose.server.yml ps
docker logs -f klein-api
docker logs -f klein-admin
docker logs -f klein-openai
docker logs -f klein-worker
```

### 5. 默认入口

| 入口 | 地址 |
|------|------|
| 用户前台 | `http(s)://your-domain:17080` |
| 管理后台 | `http(s)://your-domain:17088` |
| OpenAI 兼容 API | `http(s)://your-domain:17200/v1` |

## 🧩 OpenAI 兼容 API

直接把 OpenAI SDK 的 `base_url` 指向本服务即可：

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://your-domain:17200/v1",
    api_key="sk-xxxxxxxx",  # 在用户前台「密钥」页生成
)

# 文字对话
resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "你好"}],
)

# 图片生成
img = client.images.generate(
    model="gpt-image-2",
    prompt="一只在京都樱花树下的赛博狐狸，电影质感",
    size="1024x1024",
    n=4,
)

# 视频生成（v2