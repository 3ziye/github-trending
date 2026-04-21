# Codex2API

Codex2API 是一个基于 **Go + Gin + React/Vite** 的 Codex 反向代理与管理后台项目，支持：

- 标准模式：**PostgreSQL + Redis**
- 轻量模式：**SQLite + 内存缓存**

它对外提供兼容 OpenAI 风格的接口，并在内部维护一套基于 **Refresh Token 账号池** 的调度、刷新、测试、限流恢复、用量观测与后台管理能力。

---

## 目录

- [快速部署](#快速部署)
- [完整文档](#完整文档)
- [环境配置](#环境配置)
- [对外接口](#对外接口)
  - [Token 上传与账号管理](#token-上传与账号管理)
- [管理后台](#管理后台)
- [核心能力](#核心能力)
- [目录结构](#目录结构)
- [常见注意事项](#常见注意事项)
- [免责声明](#免责声明与开源协议)

---

## 快速部署

> 详细部署指南请参考：[DEPLOYMENT.md](docs/DEPLOYMENT.md)

### 部署模式总览

| 模式 | 文件 | 适用场景 |
| --- | --- | --- |
| Docker 镜像部署 | `docker-compose.yml` | **推荐**，服务器 / 测试环境，直接拉取预构建镜像 |
| 本地源码容器构建 | `docker-compose.local.yml` | 本地改代码后做完整容器验证 |
| SQLite 轻量部署 | `docker-compose.sqlite.yml` | 单机轻量部署，不依赖 PostgreSQL / Redis |
| SQLite 本地源码构建 | `docker-compose.sqlite.local.yml` | 本地改代码后验证 SQLite 轻量模式 |
| 本地开发 | `go run .` + `npm run dev` | 前后端联调与调试 |

### 部署命令速查

标准镜像版：

```bash
git clone https://github.com/james-6-23/codex2api.git
cd codex2api
cp .env.example .env
docker compose pull
docker compose up -d
docker compose logs -f codex2api
```

标准本地构建版：

```bash
cp .env.example .env
docker compose -f docker-compose.local.yml up -d --build
docker compose -f docker-compose.local.yml logs -f codex2api
```

SQLite 镜像版：

```bash
cp .env.sqlite.example .env
docker compose -f docker-compose.sqlite.yml pull
docker compose -f docker-compose.sqlite.yml up -d
docker compose -f docker-compose.sqlite.yml logs -f codex2api
```

SQLite 本地构建版：

```bash
cp .env.sqlite.example .env
docker compose -f docker-compose.sqlite.local.yml up -d --build
docker compose -f docker-compose.sqlite.local.yml logs -f codex2api
```

补充说明：

- 标准版和 SQLite 版都读取 `.env`
- 切换部署模式前，需要先用对应的示例文件覆盖当前 `.env`
- 标准镜像版项目名固定为 `codex2api`，数据卷固定为 `codex2api_pgdata`、`codex2api_redisdata`
- 标准本地构建版项目名固定为 `codex2api-local`，数据卷固定为 `codex2api-local_pgdata`、`codex2api-local_redisdata`
- SQLite 镜像版项目名固定为 `codex2api-sqlite`，数据卷固定为 `codex2api-sqlite_sqlite-data`
- SQLite 本地构建版项目名固定为 `codex2api-sqlite-local`，数据卷固定为 `codex2api-sqlite-local_sqlite-data-local`
- 标准版容器名：`codex2api`
- SQLite 镜像版容器名：`codex2api-sqlite`
- SQLite 本地构建版容器名：`codex2api-sqlite-local`
- SQLite 轻量版只启动 `codex2api` 单容器，数据保存在 `/data/codex2api.db`
- `docker compose down` 默认不会删除命名卷；只有 `docker compose down -v`、`docker volume rm` 或 `docker volume prune` 才会删除持久化数据
- 不同部署模式的数据卷彼此隔离；切换 compose 文件后看到空数据，通常是切到了另一组卷，而不是原卷被自动删除

启动后访问：

- 管理台：`http://localhost:8080/admin/`
- 健康检查：`http://localhost:8080/health`

> 更多部署详情请参考：[DEPLOYMENT.md](docs/DEPLOYMENT.md)

---

## 完整文档

| 文档 | 说明 | 路径 |
|------|------|------|
| [API 文档](docs/API.md) | 所有 API 端点、请求/响应示例、错误码说明 | `docs/API.md` |
| [部署文档](docs/DEPLOYMENT.md) | 各种部署模式、升级指南、备份恢复 | `docs/DEPLOYMENT.md` |
| [配置文档](docs/CONFIGURATION.md) | 环境变量、系统设置、配置优先级 | `docs/CONFIGURATION.md` |
| [架构文档](docs/ARCHITECTURE.md) | 系统架构、调度算法、存储设计 | `docs/ARCHITECTURE.md` |
| [故障排查](docs/TROUBLESHOOTING.md) | 常见问题排查、诊断脚本、解决方案 | `docs/TROUBLESHOOTING.md` |
| [贡献指南](docs/CONTRIBUTING.md) | 开发规范、PR 流程、代码标准 | `docs/CONTRIBUTING.md` |

---

## 环境配置

```bash
git pull && docker compose pull && docker compose up -d && docker compose logs -f codex2api
```

> **⚠️ 重要：升级前请先备份数据库！**
>
> ```bash
> docker exec codex2api-postgres pg_dump -U codex2api codex2api > backup_$(date +%Y%m%d_%H%M%S).sql
> ```
>
> 如果升级后数据异常，可通过以下命令恢复：
>
> ```bash
> docker exec -i codex2api-postgres psql -U codex2api codex2api < backup_xxx.sql
> ```

如非必要，不建议在升级时执行 `docker compose down`；标准升级直接 `pull + up -d` 即可复用现有容器和命名卷。

### 本地开发模式

**后端：**

```bash
cp .env.example .env
cd frontend && npm ci && npm run build && cd ..
go run .
```

> 首次启动需要先构建前端，因为 Go 使用 `go:embed` 嵌入 `frontend/dist` 。

**前端开发服务器（联调）：**

```bash
cd frontend && npm ci && npm run dev
```

Vite 会自动代理 `/api` 和 `/health` 到后端，开发时访问 `http://localhost:5173/admin/`。

---

## 环境配置

### `.env` 环境变量

> 完整配置说明请参考：[CONFIGURATION.md](docs/CONFIGURATION.md)

| 变量 | 说明 |
| --- | --- |
| `CODEX_PORT` | HTTP 端口，默认 `8080` |
| `ADMIN_SECRET` | 管理后台登录密钥；设置后首次访问 `/admin` 会弹出密码输入框 |
| `DATABASE_DRIVER` | 数据库驱动，支持 `postgres` / `sqlite` |
| `DATABASE_PATH` | SQLite 数据文件路径，`DATABASE_DRIVER=sqlite` 时生效 |
| `DATABASE_HOST` | PostgreSQL 主机，`DATABASE_DRIVER=postgres` 时生效 |
| `DATABASE_PORT` | PostgreSQL 端口，默认 `5432` |
| `DATABASE_USER` | PostgreSQL 用户 |
| `DATABASE_PASSWORD` | PostgreSQL 密码 |
| `DATABASE_NAME` | PostgreSQL 数据库名 |
| `DATABASE_SSLMODE` | PostgreSQL SSL 模式，默认 `disable` |
| `CACHE_DRIVER` | 缓存驱动，支持 `redis` / `memory` |
| `REDIS_ADDR` | Redis 地址，例如 `redis:6379`，`CACHE_DRIVER=redis` 时生效 |
| `REDIS_PASSWORD` | Redis 密码 |
| `REDIS_DB` | Redis DB 库号 |
| `TZ` | 时区，例如 `Asia/Shanghai` |

标准版 `.env.example` 已显式声明 `DATABASE_DRIVER=postgres` 与 `CACHE_DRIVER=redis`；SQLite 轻量版请改用 `.env.sqlite.example`。

### 业务运行配置

以下参数**保存在数据库 `SystemSettings` 中**，通过管理台设置页面修改：

`MaxConcurrency`、`GlobalRPM`、`TestModel`、`TestConcurrency`、`ProxyURL`、`PgMaxConns`、`RedisPoolSize`、`AdminSecret`、自动清理开关等。

首次启动时程序会自动写入默认设置。

### API Key 与管理密钥

- **对外 API Key**：以数据库中的 API Keys 为准。如果没有配置任何 Key，则 `/v1/*` 跳过鉴权。
- **管