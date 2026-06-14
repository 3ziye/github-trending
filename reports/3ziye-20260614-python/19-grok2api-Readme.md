<div align="center">

<img alt="Grok2API" src="https://github.com/user-attachments/assets/037a0a6e-7986-41cc-b4af-04df612ee886" />

<h1>Grok Web 能力的 OpenAI 兼容网关</h1>

<h3>多账号池、智能选号、自动维护</h3>

<p>
将 grok.com 与 console.x.ai 的聊天、图像、视频能力，<br>
以 <strong>OpenAI / Anthropic 兼容 API</strong> 统一对外提供。
</p>

<p>
<a href="https://www.python.org/"><img alt="Python" src="https://img.shields.io/badge/python-3.13%2B-3776AB?logo=python&logoColor=white"></a>
<a href="https://fastapi.tiangolo.com/"><img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-0.119%2B-009688?logo=fastapi&logoColor=white"></a>
<a href="https://github.com/jiujiu532/grok2api/pkgs/container/grok2api"><img alt="Docker" src="https://img.shields.io/badge/ghcr.io-jiujiu532%2Fgrok2api-2496ED?logo=docker&logoColor=white"></a>
<a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/license-MIT-16a34a"></a>
</p>

<p>
<a href="#核心特性">核心特性</a> ·
<a href="#部署指南">部署指南</a> ·
<a href="#模型列表">模型列表</a> ·
<a href="#账号配置">账号配置</a> ·
<a href="#api-端点">API 端点</a> ·
<a href="#常见问题">常见问题</a>
</p>

</div>

> [!NOTE]
> 本项目仅供学习与研究交流。请务必遵守 Grok 的使用条款及当地法律法规，不得用于非法用途。

本仓库基于上游 [chenyme/grok2api](https://github.com/chenyme/grok2api) 二次开发，新增多账号池管理、Console 免费模型、配额轮换、防封部署等能力。欢迎 PR 和 Fork，二开请保留原作者与前端标识。

---

## 核心特性

| 能力 | 说明 |
| :-- | :-- |
| OpenAI 兼容 | `/v1/chat/completions`、`/v1/responses`、`/v1/images/generations`、`/v1/videos` |
| Anthropic 兼容 | `/v1/messages`（Claude SDK 直接对接） |
| 多账号池 | basic / super / heavy 三级池，自动负载均衡与配额同步 |
| 免费账号 | 支持 `console.x.ai` SSO Token，`*-console` 模型零成本使用 |
| 媒体生成 | 文生图、图像编辑、文生视频、图生视频，本地缓存与代理链接 |
| 防封内置 | `x-statsig-id` 兼容修复，WARP + FlareSolverr 一键部署 |
| 管理后台 | Admin 配置、账号管理、Web Chat、Masonry 画廊、ChatKit 语音 |

---

## 部署指南

本项目提供两种部署方式：

| 方式 | 说明 | 适用场景 |
| :-- | :-- | :-- |
| **标准版** | 仅 grok2api，直连 Grok | IP 干净、无 Cloudflare 拦截 |
| **防封版** | grok2api + WARP + Privoxy + FlareSolverr | IP 被 Cloudflare 拦截、需要稳定访问 |

> [!TIP]
> 当前版本已内置 403 兼容修复，标准版可直接验证。仍遇 403 时再切防封版。

---

### 标准版部署

**Docker Compose（推荐）：**

```bash
git clone https://github.com/jiujiu532/grok2api
cd grok2api/grok2api-main/grok2api-main
cp .env.example .env
docker compose up -d
```

查看日志：

```bash
docker compose logs -f grok2api
```

**Docker 单容器：**

```bash
docker run -d --name grok2api \
  -p 8000:8000 \
  -e TZ=Asia/Shanghai \
  -e LOG_LEVEL=INFO \
  -e ACCOUNT_STORAGE=local \
  -v $(pwd)/data:/app/data \
  -v $(pwd)/logs:/app/logs \
  --restart unless-stopped \
  ghcr.io/jiujiu532/grok2api:latest
```

Windows PowerShell：

```powershell
docker run -d `
  --name grok2api `
  -p 8000:8000 `
  -e TZ=Asia/Shanghai `
  -e LOG_LEVEL=INFO `
  -e ACCOUNT_STORAGE=local `
  -v ${PWD}/data:/app/data `
  -v ${PWD}/logs:/app/logs `
  --restart unless-stopped `
  ghcr.io/jiujiu532/grok2api:latest
```

---

### 防封版部署

> **前置要求**：服务器需支持 `NET_ADMIN` + `SYS_MODULE` 权限（KVM/XEN 虚拟化均支持，OpenVZ/LXC 不支持）。

```bash
git clone https://github.com/jiujiu532/grok2api
cd grok2api/grok2api-main/grok2api-main
docker compose -f docker-compose.warp.yml up -d
```

防封版自动启动以下服务：

| 服务 | 说明 |
| :-- | :-- |
| `warp-proxy` | Cloudflare WARP 出口代理，提供干净 IP |
| `privoxy` | HTTP 代理，将流量转发到 WARP |
| `flaresolverr` | 自动解 Cloudflare 挑战，获取 cf_clearance |
| `init-config` | 初始化容器，自动写入代理配置 |
| `grok2api` | 主服务 |

启动后代理配置已自动完成，进入 Admin 后台添加账号即可使用。

---

<details>
<summary><strong>升级 / 回滚 / 卸载 / 迁移</strong></summary>

### 升级

无论标准版还是防封版，升级时只需更新 `grok2api` 主镜像，防封组件不需要更新。

**标准版升级：**

```bash
docker pull ghcr.io/jiujiu532/grok2api:latest
docker compose up -d --no-deps grok2api
```

**防封版升级（只更新主服务，不动 WARP/FlareSolverr）：**

```bash
docker pull ghcr.io/jiujiu532/grok2api:latest
docker compose -f docker-compose.warp.yml up -d --no-deps grok2api
```

> `--no-deps` 确保只重启 grok2api，WARP/Privoxy/FlareSolverr 继续运行不中断。
> 
> `./data/` 中的配置（`config.toml`）和数据库（`accounts.db`）挂载在 volume 中，升级不会覆盖。

### 回滚

```bash
# 查看可用版本：https://github.com/jiujiu532/grok2api/pkgs/container/grok2api
docker pull ghcr.io/jiujiu532/grok2api:<tag>

# 标准版回滚
docker compose up -d --no-deps grok2api

# 防封版回滚
docker compose -f docker-compose.warp.yml up -d --no-deps grok2api
```

### 卸载

**标准版卸载：**

```bash
cd grok2api/grok2api-main/grok2api-main
docker compose down
# 如需删除数据（不可恢复）：
rm -rf ./data ./logs
```

**防封版卸载：**

```bash
cd grok2api/grok2api-main/grok2api-main
docker compose -f docker-compose.warp.yml down
# 如需删除数据（不可恢复）：
rm -rf ./data ./logs
```

### 从标准版迁移到防封版

数据完全保留，无需重新配置：

```bash
# 停止标准版
docker compose down

# 用防封版启动（自动检测已有配置，不覆盖）
docker compose -f docker-compose.warp.yml up -d
```

</details>

---

### 本地源码部署

前置：Python 3.13+、[uv](https://docs.astral.sh/uv/getting-started/installation/)

```bash
git clone https://github.com/jiujiu532/grok2api
cd grok2api/grok2api-main/grok2api-main
cp .env.example .env && uv sync
uv run granian --interface asgi --host 0.0.0.0 --port 8000 --workers 1 app.main:app
```

---

### 首次启动

访问 `http://localhost:8000/admin/login`，默认密码 `grok2api`，进入后设置：

1. `app.app_key` — Admin 密码
2. `app.api_key` — API 鉴权密钥（留空不鉴权）
3. `app.app_u