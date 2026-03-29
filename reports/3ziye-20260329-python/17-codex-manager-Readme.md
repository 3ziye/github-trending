# OpenAI 账号管理系统 v2

管理 OpenAI 账号的 Web UI 系统，支持多种邮箱服务、并发批量注册、代理管理和账号管理。

# 官方拉闸了,改变了授权流程,各位自行研究吧  

> ⚠️ **免责声明**：本工具仅供学习和研究使用，使用本工具产生的一切后果由使用者自行承担。请遵守相关服务的使用条款，不要用于任何违法或不当用途。 如有侵权，请及时联系，会及时删除。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)

## 功能特性

- **多邮箱服务支持**
  - Tempmail.lol（临时邮箱，无需配置）
  - Outlook（IMAP + XOAUTH2，支持批量导入）
  - 自定义域名（两种子类型）
    - **MoeMail**：标准 REST API，配置 API 地址 + API 密钥
    - **TempMail**：自部署 Cloudflare Worker 临时邮箱，配置 Worker 地址 + Admin 密码
  - DuckMail
    - **DuckMail API**：兼容 DuckMail 接口，手动填写 API 地址、默认域名，可选 API Key

- **注册模式**
  - 单次注册
  - 批量注册（可配置数量和间隔时间）
  - Outlook 批量注册（指定账户逐一注册）

- **并发控制**
  - 流水线模式（Pipeline）：每隔 interval 秒启动新任务，限制最大并发数
  - 并行模式（Parallel）：所有任务同时提交，Semaphore 控制最大并发
  - 并发数可在 UI 自定义（1-50）
  - 日志混合显示，带 `[任务N]` 前缀区分

- **实时监控**
  - WebSocket 实时日志推送
  - 跨页面导航后自动重连
  - 降级轮询备用方案

- **代理管理**
  - 动态代理（通过 API 每次获取新 IP）
  - 代理列表（随机选取，支持设置默认代理，记录使用时间）

- **账号管理**
  - 查看、删除、批量操作
  - Token 刷新与验证
  - 订阅状态管理（手动标记 / 自动检测 plus/team/free）
  - 导出格式：JSON / CSV / CPA 格式 / Sub2API 格式
    - 单个账号导出为独立 `.json` 文件
    - 多个 CPA 账号打包为 `.zip`，每个账号一个独立文件
    - Sub2API 格式所有账号合并为单个 JSON
  - Codex Auth 格式需先在账号管理中手动执行 `Codex Auth 登录` 成功后才能导出
  - 上传目标（直连不走代理）：
    - **CPA**：支持多服务配置，上传时选择目标服务，可按服务开关将账号实际代理写入 auth file 的 `proxy_url`
    - **Sub2API**：支持多服务配置，标准 sub2api-data 格式
    - **Team Manager**：支持多服务配置

- **支付升级**
  - 为账号生成 ChatGPT Plus 或 Team 订阅支付链接
  - 后端命令行以无痕模式自动打开 Chrome/Edge
  - Team 套餐支持自定义工作区名称、座位数、计费周期

- **系统设置**
  - 代理配置（动态代理 + 代理列表，支持设默认）
  - CPA 服务列表管理（多服务，连接测试）
  - Sub2API 服务列表管理（多服务，连接测试）
  - Team Manager 服务列表管理（多服务，连接测试）
  - Outlook OAuth 参数
  - 注册参数（超时、重试、密码长度等）
  - 验证码等待配置（超时时间、轮询间隔、收件箱未找到时最多重发次数）
  - 数据库管理（备份、清理）
  - 支持远程 PostgreSQL

## 快速开始

### 环境要求

- Python 3.10+
- [uv](https://github.com/astral-sh/uv)（推荐）或 pip

### 安装依赖

```bash
# 使用 uv（推荐）
uv sync

# 或使用 pip
pip install -r requirements.txt
```

### 环境变量配置（可选）

复制 `.env.example` 为 `.env`，按需填写：

```bash
cp .env.example .env
```

| 变量 | 说明 | 默认值 |
|------|------|--------|
| `APP_HOST` | 监听主机 | `0.0.0.0` |
| `APP_PORT` | 监听端口 | `15555` |
| `APP_ACCESS_PASSWORD` | Web UI 访问密钥 | `admin123` |
| `APP_DATABASE_URL` | 数据库连接字符串 | `data/database.db` |

> 优先级：命令行参数 > 环境变量（`.env`）> 数据库设置 > 默认值

### 修改端口

默认端口是 `15555`。现在已经收敛到少数几个固定入口：

- 本地临时启动改端口：直接用 `python webui.py --port 18080`
- 本地通过 `.env` 改端口：设置 `APP_PORT=18080`
- 源码里的默认端口：修改 `src/config/constants.py` 里的 `DEFAULT_WEBUI_PORT`
- Docker Compose 默认端口：修改 `docker-compose.yml` 顶部的 `x-webui-port`
- Docker 镜像构建默认端口：修改 `Dockerfile` 里的 `ARG DEFAULT_WEBUI_PORT`

补充说明：
- `src/config/constants.py` 的 `DEFAULT_WEBUI_PORT` 会同时影响默认 Web UI 端口、默认回调地址和 e2e 脚本默认地址。
- `docker-compose.yml` 里已经把端口映射、容器内 `WEBUI_PORT` 和健康检查统一绑到同一个 `x-webui-port`，改一处就够。

### 启动 Web UI

```bash
# 默认启动（0.0.0.0:15555）
python webui.py

# 指定地址和端口
python webui.py --host 0.0.0.0 --port 8080

# 调试模式（热重载）
python webui.py --debug

# 设置 Web UI 访问密钥
python webui.py --access-password mypassword

# 组合参数
python webui.py --host 0.0.0.0 --port 8080 --access-password mypassword
```

> `--access-password` 优先级高于数据库中保存的密钥设置，每次启动时生效。打包后的 exe 同样支持此参数：
> ```bash
> codex-register.exe --access-password mypassword
> ```

### Docker 部署

项目支持通过 Docker 进行容器化部署。Docker 镜像已托管至 GitHub Container Registry (GHCR)。

#### 使用 docker-compose (推荐)

在项目根目录下，直接使用 `docker-compose` 启动：

```bash
docker-compose up -d
```
你可以在 `docker-compose.yml` 中修改相关的环境变量，例如配置端口或者设置 `WEBUI_ACCESS_PASSWORD` 访问密码。

如果要修改 Docker Compose 对外端口，直接改文件顶部这一行即可：

```yaml
x-webui-port: &webui-port 15555
```

这一个值会同时同步到：

- 宿主机端口映射
- 容器内 `WEBUI_PORT`
- 健康检查访问地址

#### 直接使用 docker run

如果你不想使用 docker-compose，也可以直接拉取并运行镜像：

```bash
docker run -d \
  -p 15555:15555 \
  -e WEBUI_HOST=0.0.0.0 \
  -e WEBUI_PORT=15555 \
  -e WEBUI_ACCESS_PASSWORD=your_secure_password \
  -v $(pwd)/data:/app/data \
  --name codex-register \
  ghcr.io/yunxilyf/codex-register:latest
```

环境变量说明：
- `WEBUI_HOST`: 监听的主机地址 (默认 `0.0.0.0`)
- `WEBUI_PORT`: 监听的端口 (默认 `15555`)
- `WEBUI_ACCESS_PASSWORD`: 设置 Web UI 的访问密码
- `DEBUG`: 设为 `1` 或 `true` 开启调试模式
- `LOG_LEVEL`: 日志级别，如 `info`, `debug`

> **注意**：`-v $(pwd)/data:/app/data` 挂载参数非常重要，它确保了你的数据库文件和账户信息在容器重启或更新后不会丢失。

如果你要把容器端口改成 `18080`，`-p` 和 `WEBUI_PORT` 需要一起改：

```bash
docker run -d \
  -p 18080:18080 \
  -e WEBUI_HOST=0.0.0.0 \
  -e WEBUI_PORT=18080 \
  -e WEBUI_ACCESS_PASSWORD=your_secure_password \
  -v $(pwd)/data:/app/data \
  --name codex-register \
  ghcr.io/yunxilyf/codex-register:latest
```

### 使用远程 PostgreSQL

通过环境变量指定数据库连接字符串：

```bash
export APP_DATABASE_URL="postgresql://user:password@host:5432/dbname"
python webui.py
```

也支持 `DATABASE_URL`，优先级低于 `APP_DATABASE_URL`。

启动后访问 http://127.0.0.1:15555

## 打包为可执行文件

```bash
# Windows
build.bat

# Linux/macOS
bash build.sh
```

打包后生成 `codex-register.exe`（Windows）或 `codex-register`（Unix），双击或直接运行即可，无需安装 Python 环境。

## 项目结构

```
codex-register-v2/
├── webui.py            # Web UI 入口
├── build.bat          