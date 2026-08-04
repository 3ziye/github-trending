# grokcli-2api【注册拉闸】

把 **Grok OIDC 登录态** 转成 **OpenAI / Anthropic 兼容 API**，并附带 Web 管理台：多 API Key、多账号轮询、设备码 / SSO / JSON 导入导出、协议注册。

**当前版本：v2.0.4** · 容器内热更新 · API Key 列表修复 · 注册资源/日志优化 · empty-output 治理 · Go 主进程

[![GHCR](https://img.shields.io/badge/ghcr.io-hm2899%2Fgrokcli--2api-blue)](https://github.com/users/HM2899/packages/container/package/grokcli-2api)
[![Release](https://img.shields.io/github/v/release/HM2899/grokcli-2api?display_name=tag)](https://github.com/HM2899/grokcli-2api/releases)

| 镜像（全小写） | 说明 |
|----------------|------|
| `ghcr.io/hm2899/grokcli-2api:2.0.4` | 当前版本 |
| `ghcr.io/hm2899/grokcli-2api:latest` | 最近 `v*` tag |
| `ghcr.io/hm2899/grokcli-2api:edge` | `main` 最新 |

> **分支**：默认 `main`（Go 2.x）。纯 Python 快照在次要分支 [`python`](https://github.com/HM2899/grokcli-2api/tree/python)，发布时不会覆盖。

- **独立运行**：不依赖本地 Grok CLI / 浏览器 OAuth
- **Hybrid 存储（默认强制）**：PostgreSQL 持久 + Redis 热状态 + 多 Worker
- **大账号池轮询**：`round_robin` / `least_used` / `random`；**没额度立即冷却踢出**；pick-time inflight 负载分散
- **会话粘性 / Prompt Cache**：`prompt_cache_key` / Claude session / messages hash；model 隔离绑定；TTL 可热改
- **协议注册**：内置 `grok-build-auth`（纯 HTTP，无需 Chromium）；**SSO 入库**；可选 **注册成功后自动推 sub2api / CLIProxyAPI**
- **中继友好**：兼容 new-api / sub2api / CLIProxyAPI / Claude Code / Codex；`Update`/`StrReplace` → `Edit`；**后到完整参数覆盖错误路径**
- **秒开流 + 可观测**：early SSE 信封；用量明细含 `ttft_ms` / `latency_ms` / **思考强度**；任务日志 + 终态帧

---

## 架构

```
客户端 (OpenAI / Anthropic SDK · new-api · Claude Code / sub2api)
        │  /v1/chat/completions  ·  /v1/responses  ·  /v1/messages
        ▼
  grokcli-2api  (Go 主进程 · multi-worker · TZ=Asia/Shanghai)
        │  管理台 /admin
        │  账号轮询 · 冷却/过期踢出 · inflight 分散 · Prompt Cache 会话粘性
        │  任务日志（注册 / SSO / JSON / 测活 / 续期）
        │  PostgreSQL（账号 / Key / 设置 / 冷却 / 任务日志）—— 容器内网
        │  Redis（粘性 / 计数 / 锁 / 会话 / 任务进度）—— 容器内网
        │
        ├─ Python sidecar（loopback）：注册机 / SSO 转换 / 过盾
        ▼
  cli-chat-proxy.grok.com
```

> `data/*.json` **仅作旧版迁移源与管理台导入导出**，运行时权威数据在 PostgreSQL / Redis，不再写本地 JSON 镜像。

---

## 功能一览

| 功能 | 说明 |
|------|------|
| OpenAI 兼容 | `/v1/models` · `/v1/chat/completions` · `/v1/responses` · SSE |
| Anthropic 兼容 | `/v1/messages` · tools / tool_use · `count_tokens` |
| Claude Code 工具 | Grok `Update`/`StrReplace` → 客户端 `Edit`；**后到完整参数覆盖错误路径（含 both-complete）**；`target_file` 等别名归一；残缺编辑不下发 |
| 注册机 | 批次自愈 + 孤儿回收；全局 inflight；Device Flow 重试；**SSO 入库 + 文件备份**；导出可走账号库；进度卡防连环 toast |
| 管理台 | 账号、Key、协议注册、测活、续期、任务日志、用量、**系统设置（维护/压缩/探测/sub2api · CLIProxyAPI · 版本与热更新）** |
| 多账号轮询 | `round_robin` / `least_used` / `random`；**pick-time inflight 分散**；可选**出站代理池** |
| 会话粘性 | `prompt_cache_key` / `previous_response_id` 粘同一账号；**TTL 可热改** |
| 冷却状态 | **没额度立即冷却踢出**（任意轮询策略）；live 硬排除；仅测活成功 / 手动解除才回池 |
| Token 过期 / 续期失败 | access token 过期立刻 `pool_status=expired` 移出轮询；连续 2 次 RT 失败 → 有 SSO 则重转，**无 SSO 则硬删账号** |
| 号池统计 | 总量 / 可轮询 / 冷却 / 过期 / 封禁 **互斥分类**（`pool_status` 权威） |
| Token 续期 | 后台 leader 维护；**维护间隔 / 提前刷新窗口可配置** |
| 模型探测 | 单账号 / 多选批量 / 全量；**探测模型列表 / 间隔 / 自动踢出可配置** |
| 协议注册 | MoeMail / YYDS / GPTMail / CF Temp Email / **TempMail.lol** + 内联过盾 / YesCaptcha；代理池；入池后延迟测活；**多邮箱 Key 独立槽位** |
| SSO / JSON / CPA | 后台任务 + 实时进度；JSON 多文件导入；**一键推送 sub2api**；**一键同步 CLIProxyAPI auth 目录**；CPA/auth 文件双向格式兼容 |
| 任务日志 | 注册、SSO、JSON、测活、续期等结果落 PG |
| 用量统计 | 代理侧 token / 请求：今日·近 N 天·累计；按 Key / 账号 / 模型；**首字 TTFT / 完成耗时 / 思考强度** |
| 流式可靠性 | early SSE 信封；**假阳性 client_gone 不再丢中间 tool/text 帧**；错误/断开仍发终态帧 |
| 容器时区 | 默认 `TZ=Asia/Shanghai`（日志与本地时间） |

---

## 本版本重点（v2.0.4）

| 能力 | 行为 |
|------|------|
| **容器内版本 / 热更新** | 管理台「系统设置 → 版本与热更新」：对照 GitHub Release；**在容器内** `docker pull` + `compose force-recreate`；**无需宿主机 watcher**（可选兼容 `request_file`） |
| **API Key 列表可见** | 新建 Key 后列表立即可见：最新在前；创建乐观插入；stats 失败不拖垮列表；NULL note 安全扫描 |
| **注册占用下降** | 默认并发更保守（`MAX_CONCURRENCY=3` / local captcha=1 / global inflight=2）；Redis 镜像节流；log 环形缓冲更短；终态 TTL 更快回收 |
| **注册日志更低延迟** | 健康路径约 **140ms** 轮询；Go 共享 HTTP 客户端 **750ms**；稳态只打 batch GET，避免全量 `/sessions` 扫描 |
| **注册资源释放** | stop 时立即 close receiver/client；worker finally 强制释放 + force 镜像 Redis |
| **空模型输出治理** | 继承 v2.0.3：空流换号 / 模型封禁（`GROK2API_EMPTY_OUTPUT_BLOCK_SEC`） |
| **TempMail.lol / 邮件槽位** | 继承 v2.0.3：独立 Key 槽位、防交叉污染 |

继承 v2.0.x：CPA prompt cache · 同会话粘号 · 流式 tool 可靠性 · 用量 TTFT / 思考强度。

---

## 快速开始

### 方式 A：Docker Compose（推荐）

```bash
git clone https://github.com/HM2899/grokcli-2api.git
cd grokcli-2api
cp .env.example .env
# 编辑 .env：至少改 GROK2API_ADMIN_PASSWORD；生产请改 Postgres 密码

docker compose up -d --build
curl -fsS http://127.0.0.1:3000/health
```

浏览器打开：`http://127.0.0.1:3000/admin`

#### 启动时指定打码线程数

主容器内联过盾线程数由 `TURNSTILE_THREAD` 控制（默认与注册并发一致，当前默认 **3**）：

```bash
# compose 启动时直接传参
TURNSTILE_THREAD=3 GROK2API_REG_CONCURRENCY=3 docker compose up -d --build

# 或写入 .env
# GROK2API_CAPTCHA_PROVIDER=local
# GROK2API_INLINE_SOLVER=1
# GROK2API_REG_CONCURRENCY=3
# TURNSTILE_THREAD=3
```

| 变量 | 默认 | 说明 |
|------|------|------|
| `GROK2API_CAPTCHA_PROVIDER` | `local` | `local`（容器内联）/ `yescaptcha` |
| `GROK2API_INLINE_SOLVE