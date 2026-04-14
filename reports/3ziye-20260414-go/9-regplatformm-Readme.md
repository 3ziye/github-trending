# RegPlatform - 多平台账号批量注册系统

可运营的多平台账号批量注册平台，支持 OpenAI / Grok / Kiro / Gemini 等平台的全自动注册、OAuth Token 获取、积分系统与多用户管理。

# yyds mail 临时邮箱： https://vip.215.im

> 部署比较复杂，不可直接食用，需要进行配置你们自己的仓库以及 hf账号密钥，以及git仓库密钥，以及 cf 的密钥～ 在就是其他的参数配置～ 建议喂给 ai 进行适配～
> 小白不建议玩耍哦～


## 技术栈

| 层级 | 技术 |
|------|------|
| **后端** | Go 1.25 / Gin / GORM / PostgreSQL |
| **前端** | Vue 3 / Vite / Pinia / TailwindCSS |
| **CI/CD** | GitHub Actions → GHCR Docker 镜像 + GitHub Release |
| **部署** | Docker Compose（主服务器）+ HuggingFace Space（Worker 节点） |
| **负载均衡** | Cloudflare Worker（路径前缀路由 + 保活） |

## 架构概览

```
用户浏览器 ──→ Nginx (443) ──→ Vue SPA
                 │
                 └──→ Go 后端 (:8000)
                        │
                        ├── TaskEngine（任务调度，弹性 Worker 池）
                        │     │
                        │     └── POST → CF Worker
                        │           │ 路径前缀路由
                        │           ├── /openai/* → HFNP 节点池
                        │           ├── /grok/*   → HFGS 节点池
                        │           ├── /kiro/*   → HFKR 节点池
                        │           └── /ts/*     → HFTS 节点池
                        │
                        ├── HFSpaceService（弹性管理：健康检查、扩缩容、CF 同步）
                        ├── WebSocket（实时日志推送）
                        └── PostgreSQL（用户/任务/结果/积分/Space 状态）
```

## 项目结构

```
regplatform/
├── cmd/
│   ├── server/              # 主服务入口
│   ├── openai-worker/       # OpenAI Worker 二进制（部署到 HFNP）
│   ├── grok-worker/         # Grok Worker 二进制（部署到 HFGS）
│   └── grpctest/            # gRPC-web 调试工具
├── internal/
│   ├── config/              # 配置加载（Viper）
│   ├── model/               # GORM 数据模型
│   ├── service/             # 业务逻辑（TaskEngine、HFSpaceService 等）
│   ├── worker/              # 平台 Worker 实现（OpenAI/Grok/Kiro）
│   ├── handler/             # HTTP 路由处理器
│   ├── middleware/           # JWT 鉴权、CORS、限流
│   ├── dto/                 # 请求/响应数据结构
│   └── pkg/                 # 内部工具库
├── web/                     # Vue 3 前端
├── services/
│   ├── aws-builder-id-reg/  # Kiro 注册微服务（→ HFKR）
│   └── turnstile-solver/    # Turnstile 求解微服务（→ HFTS）
├── cloudflare/              # CF Worker 源码
├── HFNP/                    # OpenAI HF Space 模板
├── HFGS/                    # Grok HF Space 模板
├── HFKR/                    # Kiro HF Space 模板
├── HFTS/                    # Turnstile HF Space 模板
├── macmini/                 # Mac Mini 本地部署配置
├── scripts/                 # 部署脚本（HF Space 批量部署/弹性管理）
├── Dockerfile               # 主服务容器构建
├── docker-compose.yml       # 本地开发编排
└── docker-compose.prod.yml  # 生产部署编排
```

## 支持平台

| 平台 | 注册方式 | HF Space | Release Tag |
|------|---------|----------|-------------|
| **OpenAI** | Go HTTP（Sentinel PoW + PKCE OAuth + Auth0） | HFNP | `inference-runtime-latest` |
| **Grok** | Go HTTP（gRPC-web + Turnstile + Server Actions） | HFGS | `stream-worker-latest` |
| **Kiro** | Python（AWS Cognito + Camoufox 浏览器自动化） | HFKR | `browser-agent-latest` |
| **Gemini** | Python（Camoufox 浏览器自动化） | HFGM | `gemini-agent-latest` |
| **Turnstile** | Python（Camoufox + Patchright 求解） | HFTS | `net-toolkit-latest` |

## 快速开始

### 环境要求

- Go 1.25+
- Node.js 18+
- PostgreSQL 16+
- Docker & Docker Compose（生产部署）

### 本地开发

```bash
# 1. 克隆项目
git clone https://github.com/your-username/regplatform.git
cd regplatform

# 2. 配置环境变量
cp .env.example .env
# 编辑 .env，配置数据库连接等

# 3. 启动后端
go mod tidy
go run cmd/server/main.go

# 4. 启动前端（另一个终端）
cd web && npm install && npm run dev
```

### Docker 部署

```bash
# 启动（含 PostgreSQL）
docker-compose -f docker-compose.prod.yml up -d
```

### 首次使用

1. 访问 `http://localhost:8000`，进入登录页面
2. 点击「注册」，创建第一个账号（**第一个注册的用户自动成为管理员**）
3. 进入后台管理面板，配置系统设置（邮箱服务、验证码求解等）

## 配置参数

### 环境变量（.env 文件）

| 变量 | 必填 | 默认值 | 说明 |
|------|------|--------|------|
| `DATABASE_URL` | 是 | - | PostgreSQL 连接串 |
| `JWT_SECRET` | 是（生产） | `change-me-in-production` | JWT 签名密钥（生产环境 ≥32 字符） |
| `PORT` | 否 | `8000` | 服务监听端口 |
| `GIN_MODE` | 否 | `release` | Gin 运行模式（`debug`/`release`） |
| `DEV_MODE` | 否 | `false` | 开发模式（启用 dev-login 端点） |
| `ADMIN_USERNAME` | 否 | 空 | 指定管理员用户名（该用户注册时自动成为管理员） |
| `SSO_SECRET` | 否 | 空 | SSO 对接密钥（可选，用于外部系统集成） |
| `REDIS_URL` | 否 | 空 | Redis 连接串（为空则使用内存缓存） |
| `JWT_EXPIRE_HOURS` | 否 | `72` | JWT 过期时间（小时） |
| `CORS_ORIGINS` | 否 | 空 | 允许的跨域来源（逗号分隔，如 `https://a.com,https://b.com`；开发模式下允许所有来源） |

### 管理后台系统设置（数据库持久化）

以下配置在管理后台「系统设置」中配置：

| 配置项 | 说明 |
|--------|------|
| `yydsmail_base_url` | YYDS Mail 临时邮箱 API 地址（用于接收注册验证码） |
| `gptmail_api_key` | GPTMail 邮箱服务 API Key |
| `gptmail_base_url` | GPTMail 服务地址 |
| `turnstile_solver_url` | Turnstile 验证码求解服务地址 |
| `cf_bypass_solver_url` | Cloudflare Bypass 求解服务地址 |
| `yescaptcha_key` | YesCaptcha API Key |
| `openai_reg_url` | OpenAI 注册服务 URL |
| `grok_reg_url` | Grok 注册服务 URL |
| `kiro_reg_url` | Kiro 注册服务 URL |
| `default_proxy` | 默认代理地址 |
| `new_user_bonus` | 新用户注册赠送积分数 |
| `max_threads_per_user` | 每用户最大并发线程数 |
| `max_target_per_task` | 每任务最大目标数 |

## 认证系统

### 注册 / 登录

- 用户通过用户名和密码注册、登录
- **密码要求**：至少 8 个字符，包含大写字母、小写字母和数字
- **接口限流**