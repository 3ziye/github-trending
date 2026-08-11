<p align="center">
  <img src="docs/logo.png" width="150" height="150" alt="one-api-pro logo">
</p>

<p align="center">
  One Api Pro · 基于Go语言的企业级 AI API Gateway
</p>
<p align="center">
  本项目基于 <a href="https://github.com/songquanpeng/one-api">one-api</a> (by <a href="https://github.com/songquanpeng">JustSong</a>) 深度重构开发，感谢原作者的开源贡献。
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="license"></a>
  <a href="https://go.dev/"><img src="https://img.shields.io/badge/language-Go-00ADD8.svg?logo=go&logoColor=white" alt="language"></a>
  <a href="https://gin-gonic.com/"><img src="https://img.shields.io/badge/framework-Gin-008080.svg?logo=go&logoColor=white" alt="framework"></a>
  <a href="https://vuejs.org/"><img src="https://img.shields.io/badge/frontend-Vue%203-42B883.svg?logo=vue.js&logoColor=white" alt="frontend"></a>
  <a href="https://arco.design/vue"><img src="https://img.shields.io/badge/ui-Arco%20Design-165DFF.svg" alt="ui"></a>
  <a href="https://vitejs.dev/"><img src="https://img.shields.io/badge/build-Vite-646CFF.svg?logo=vite&logoColor=white" alt="build"></a>
  <a href="https://gorm.io/"><img src="https://img.shields.io/badge/database-MySQL%20%7C%20PostgreSQL%20%7C%20SQLite-4479A1.svg?logo=mysql&logoColor=white" alt="database"></a>
  <a href="https://github.com/Leon-PanPan/one-api-pro"><img src="https://img.shields.io/badge/cluster-decentralized-FF6B6B.svg" alt="cluster"></a>
</p>

<p align="center">
  <a href="README.md">简体中文</a>
  &nbsp;·&nbsp;
  <a href="readme/README.en.md">English</a>
</p>

---

## 📑 目录

- [🚀 快速开始](#-快速开始)
- [🔧 技术栈](#-技术栈)
  - [Go 后端](#go-后端)
  - [Vue 3 前端](#vue-3-前端)
- [✨ 功能亮点](#-功能亮点)
- [🔥 对比 one-api](#-对比-one-api)
- [📸 截图展示](#-截图展示)
- [⚙️ 配置](#%EF%B8%8F-配置)
  - [🔧 环境变量](#-环境变量)
  - [⌨️ 命令行参数](#%EF%B8%8F-命令行参数)
- [📖 接口文档](#-接口文档)
- [📦 部署](#-部署)
  - [🔨 手动部署](#-手动部署)
  - [🏢 多机部署](#-多机部署)
  - [🌐 集群部署（去中心化多活）](#-集群部署去中心化多活)
  - [🔌 部署第三方服务配合 One Api Pro 使用](#-部署第三方服务配合-one-api-pro-使用)
- [🗺️ 开发计划](#%EF%B8%8F-开发计划)
- [相关项目](#相关项目)
- [License](#license)

---

## 🚀 快速开始

### 1. 获取可执行文件

从 [GitHub Releases](https://github.com/Leon-PanPan/one-api-pro/releases/latest) 下载预编译版本，或从源码编译：

```bash
git clone https://github.com/Leon-PanPan/one-api-pro.git
cd one-api-pro
```

### 2.（源码构建）构建 Vue 3 前端

```bash
cd web
sh build.sh        # 按 web/THEMES 依次构建主题（默认 default-pro）
cd ..
```

### 3.（源码构建）构建后端

> 后端必须在前端构建完成之后再编译，以嵌入最新前端产物。

```bash
go build -ldflags "-s -w" -o one-api-pro
```

### 4. 启动

```bash
./one-api-pro --port 3000 --log-dir ./logs
```

访问 `http://localhost:3000`，使用初始账号 `root / 123456` 登录。

> 详细部署方式见 [📦 部署](#-部署)，接口文档见 [📖 接口文档](#-接口文档)。

---

## 🔧 技术栈

本项目基于以下开源技术构建，感谢所有开源项目作者。

### Go 后端

| 技术 | 用途 |
| --- | --- |
| [Gin](https://github.com/gin-gonic/gin) | HTTP Web 框架 |
| [GORM](https://gorm.io) | ORM 库，支持 SQLite / MySQL / PostgreSQL |
| [go-redis/redis](https://github.com/go-redis/redis) | Redis 客户端 |
| [golang-jwt/jwt](https://github.com/golang-jwt/jwt) | JWT 鉴权 |
| [AWS SDK for Go v2](https://github.com/aws/aws-sdk-go-v2) | AWS Bedrock 集成 |
| [Google API Go Client](https://github.com/googleapis/google-api-go-client) | Google Gemini / PaLM2 集成 |
| [pkoukk/tiktoken-go](https://github.com/pkoukk/tiktoken-go) | Token 计数 |
| [gorilla/websocket](https://github.com/gorilla/websocket) | WebSocket 支持（讯飞等渠道） |
| [joho/godotenv](https://github.com/joho/godotenv) | .env 配置文件解析 |

### Vue 3 前端

| 技术 | 用途 |
| --- | --- |
| [Vue 3](https://vuejs.org) | 前端框架（组合式 API） |
| [Vite](https://vitejs.dev) | 构建工具 |
| [Arco Design Vue](https://arco.design/vue) | UI 组件库 |
| [Pinia](https://pinia.vuejs.org) | 状态管理 |
| [Vue Router 4](https://router.vuejs.org) | 路由管理 |
| [Axios](https://axios-http.com) | HTTP 客户端 |
| [ECharts](https://echarts.apache.org) | 数据可视化图表 |
| [vue-i18n](https://vue-i18n.intlify.dev) | 国际化 |

---

## ✨ 功能亮点

One Api Pro 是一个**企业级 AI API 网关**，基于 Go 语言 + Vue 3 全新打造，在保留原版 one-api 全部功能的基础上，进行了架构级重构与企业级增强。

### 🖥️ 可视化仪表盘

全新的 Vue 3 + Arco Design 管理后台，提供数据可视化仪表盘，核心指标、使用趋势、模型用量分布一目了然。

| 核心指标卡 | 使用趋势图 |
|:---:|:---:|
| ![仪表盘首页](docs/Demo-Index.png) | ![仪表盘首页](docs/Demo-Index.png) |

### 🔑 精细的令牌管理

支持多维度令牌管控：可用模型白名单、IP 子网限制、额度上限、过期时间、无限额度，权限粒度细化到单个模型。

| 令牌管理 |
|:---:|
| ![令牌管理](docs/Demo-Token.png) |

### 📦 套餐订阅体系

内置完整的套餐与订阅体系：按 Token / 按请求计费，周期限频（小时 / 周 / 月），按模型精细管控，支持推荐套餐与价格配置。

| 套餐管理 | 订阅管理 |
|:---:|:---:|
| ![套餐管理](docs/Demo-Plan.png) | ![订阅管理](docs/Demo-Subscribe.png) |

### 🌐 去中心化多活集群

支持去中心化多活集群部署，每个节点独立 MySQL + Redis，通过应用层事件同步实现数据互信，无需共享数据库，天然支持全球多地域就近访问。

| 集群节点管理 |
|:---:|
| ![集群节点管理](docs/Demo-cluster.png) |

### 🧩 其他核心能力

- **30+ 模型平台接入**：OpenAI / Anthropic / Gemini / DeepSeek / 通义千问 / 文心一言 / 讯飞 / 智谱 等主流平台全覆盖，统一 OpenAI 兼容接口
- **精确成本核算**：按 Token 或按次计费，Prompt / Completion / Cached 独立定价，分组折扣叠加，周期用量追踪
- **渠道负载均衡**：按权重随机分配、自动故障切换、冷却 / 禁用策略、渠道并发与 RPM 限流
- **多级权限体系**：Guest / User / Admin / Root 四级权限，修复原版 API 权限漏洞，精细化管理员操作权限
- **企业级安全**：全链路 HTTPS、Token 鉴权、子网 IP 限制、审计日志实时追踪

---

## 🔥 对比 one-api

| 对比维度 | one-api | one-api-pro |
