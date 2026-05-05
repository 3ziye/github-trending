# ChatGpt Image Studio

ChatGpt Image Studio 是一个单服务交付的图片工作流项目：

- `backend/`：Go 后端，负责图片接口、账号池、配置管理和静态资源托管
- `web/`：Vite + React 前端，构建后输出到 `web/dist`
- `scripts/`：本地开发、检查、构建脚本

项目当前交付方式是“一个二进制 + 一份静态前端 + 本地配置目录”：

- 前端不需要单独部署
- 后端运行时直接托管 `static/`
- 首次启动时自动生成 `data/config.toml`
- 首次生成配置后即可本地运行

## 核心功能

- 基于 `gpt-image-2` 的文本生图
- 参考图生成与连续编辑
- 选区涂抹式局部重绘
- 图片工作台支持会话历史、新建会话、失败重试、提示词复制与结果图下载
- 支持按比例选择分辨率与质量档位，并区分 `Free` / `Paid` 可用输出档
- 兼容图片场景的 `/v1/chat/completions` 与 `/v1/responses`
- 本地认证文件导入与账号池管理
- `Studio` 模式支持直接导入 `access_token`，并将 `Token` 账号与认证文件账号分开管理
- 支持单账号刷新、一键批量刷新额度与刷新进度展示
- 支持 `CPA / NewAPI / Sub2API` 多来源账号同步与推送
- 请求记录页可区分官方与 CPA 链路，并记录 `size / quality / promptLength`
- 配置管理页，可直接修改 `data/config.toml`

## 图片工作台

- 支持 `生成 / 编辑 / 选区编辑` 三种主流程
- 支持移动端单页工作流：会话历史与工作台可分别进入，历史记录支持回到指定会话
- 结果图支持：
  - 下载
  - 作为后续编辑源图继续改图
  - 打开选区编辑器进行局部重绘
- 用户消息支持一键复制，失败任务支持原位重试
- 历史记录支持浏览器本地存储或服务端持久化

## 数据存储

当前项目支持把不同类型的数据拆分存储：

- 账号池存储：`current / sqlite / redis`
- 配置文件存储：`file / redis`
- 图片会话记录：`browser / server`
- 图片数据：`browser / server`

说明：

- `current` 表示沿用当前本地文件目录方案
- `server` 表示由后端统一保存并对外提供图片 / 会话读取
- 设置页支持迁移账号池、配置文件与图片会话历史
- 无盘容器场景可配合 `redis` 保存配置与账号池

## 账号池与同步

- 支持导入本地认证文件
- 支持在 `Studio` 模式下直接导入 `access_token`
- `Token` 账号不会参与 `CPA / NewAPI / Sub2API` 的同步和推送
- 支持单账号额度刷新与一键批量刷新全部额度
- 批量刷新会限制并发，并在页面显示实时进度
- 支持：
  - 从 `CPA / NewAPI / Sub2API` 同步账号到本地
  - 推送本地账号到 `CPA / NewAPI / Sub2API`

## 界面预览

| 预览 1 | 预览 2 |
| --- | --- |
| ![界面预览 1](asset/21994c2f6f7ccdc2f5c6f5c472c1e7a7af4f1063.png) | ![界面预览 2](asset/665a23c2fc38a6c49d127f454b651854fcfa8e84.png) |
| ![界面预览 3](asset/9c47ac91270469513b769c30748f6d48f421ba9f.png) | ![界面预览 4](asset/a4f2e51c873e3066fb71fcab84fee8dee8ff9ea9.png) |
| ![界面预览 5](asset/bb2f570badfb194f8b16b07221df40bfac94ee05.png) | ![界面预览 6](asset/bf84c0b8a48d8cc28afec8a1980834887f8dd211.png) |

## 仓库结构

```text
.
├── backend/                  Go 后端
│   ├── api/                  HTTP 路由与处理器
│   ├── internal/             配置、账号、同步、中间件、版本信息
│   ├── data/                 默认模板与本地运行数据目录
│   ├── static/               本地开发时同步的前端静态资源（构建产物，不入库）
│   └── main.go
├── web/                      Vite 前端
│   ├── src/                  React 页面与组件
│   └── dist/                 构建产物（不入库）
├── scripts/                  build / dev / check 脚本
└── README.md
```

## 环境要求

- Go `1.25+`
- Node.js `24+`
- npm `10+`

## 获取项目

```bash
git clone https://github.com/peiyizhi0724/ChatGpt-Image-Studio.git
cd ChatGpt-Image-Studio
```

## 本地开发

### 启动开发环境

Windows：

```powershell
./scripts/dev.ps1
```

macOS / Linux：

```bash
chmod +x ./scripts/*.sh
./scripts/dev.sh
```

开发脚本会自动完成：

1. 安装前端依赖
2. 构建 `web/dist`
3. 同步前端资源到 `backend/static`
4. 启动 Go 后端

默认地址：

- `http://127.0.0.1:7000`

健康检查：

- `GET /health`

## Docker 部署

当前仓库支持通过 GitHub Container Registry 直接拉取镜像部署。

镜像发布规则：

- 推送到 `main` 分支后，GitHub Actions 会自动更新 `ghcr.io/peiyizhi0724/chatgpt-image-studio:latest`
- 推送版本标签 `v1.2.x` 后，会额外发布同名版本镜像标签
- Docker 镜像同时提供 `linux/amd64` 与 `linux/arm64`

### 首次启动

```bash
docker compose pull
docker compose up -d
```

默认会：

- 使用 `ghcr.io/peiyizhi0724/chatgpt-image-studio:latest`，也就是 `main` 分支当前最新镜像
- 将宿主机的 `./backend/data` 挂载到容器内 `/app/data`
- 对外暴露 `7000` 端口
- 额外注入 `host.docker.internal`，方便容器访问宿主机服务（如本机代理）

如需固定到某个版本，可先设置：

```bash
export IMAGE_TAG=v1.2.10
docker compose pull
docker compose up -d
```

Windows PowerShell：

```powershell
$env:IMAGE_TAG = "v1.2.10"
docker compose pull
docker compose up -d
```

### 无状态云部署（Redis 引导启动示例）

如果你的云平台是无状态容器，重启后不会保留本地磁盘，可以把：

- 账号池存到 Redis
- 配置存到 Redis
- 图片会话记录保留在浏览器
- 图片数据保留在浏览器

推荐启动方式：

```bash
docker run -d \
  --name chatgpt-image-studio \
  -p 7000:7000 \
  -e SERVER_HOST=0.0.0.0 \
  -e SERVER_PORT=7000 \
  -e STORAGE_BACKEND=redis \
  -e STORAGE_CONFIG_BACKEND=redis \
  -e REDIS_ADDR=your-redis-host:6379 \
  -e REDIS_PASSWORD=your-redis-password \
  -e REDIS_DB=0 \
  -e REDIS_PREFIX=chatgpt2api:studio \
  -e STORAGE_IMAGE_CONVERSATION_STORAGE=browser \
  -e STORAGE_IMAGE_DATA_STORAGE=browser \
  -e TZ=Asia/Shanghai \
  ghcr.io/peiyizhi0724/chatgpt-image-studio:latest
```

说明：

- 这组环境变量的作用是让程序每次启动时都能先从 Redis 读取配置引导。
- 启动成功后，其他配置仍可在页面“配置管理”中继续修改，并持久化到 Redis。
- 如果没有持久化磁盘，不建议把 `image_conversation_storage` 或 `image_data_storage` 设为 `server`，否则服务端图片历史和图片文件在容器重建后仍会丢失。

### 一键更新

Windows：

```powershell
./scripts/docker-update.ps1
```

macOS / Linux：

```bash
chmod +x ./scripts/docker-update.sh
./scripts/docker-update.sh
```

更新脚本会自动执行：

1. 检查 Docker / Docker Compose
2. 如果当前目录是 Git 仓库，则先 `git pull --ff-only origin main`
3. 从 GitHub Container Registry 拉取 `latest` 镜像
4. 重新创建并启动容器

### 配置文件

程序启动时会确保以下文件存在：

- `data/config.example.toml`
- `data/config.toml`

在仓库开发模式下，上述路径实际对应：

- `backend/data/config.example.toml`
- `backend/data/config.toml`

如果 `config.toml` 不存在，程序会自动按内置模板生成，无需手动复制。

最小配置示例：

```toml
[app]
auth_key = "chatgpt2api"
```

默认进入后台页面时使用的登录密码也是：

- `chatgpt2api`

如果你没有修改 `[app].auth_key`，首次进入时直接输入上面的默认密码即可。

如果需要接入 CPA 同步：

```toml
[sync]
enabled = true
base_url = "http://127.0.0.1:8317"
management_key = "