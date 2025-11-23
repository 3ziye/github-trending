# MuMuAINovel 📚✨

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-green.svg)
![React](https://img.shields.io/badge/react-18.3.1-blue.svg)
![License](https://img.shields.io/badge/license-GPL%20v3-blue.svg)

**基于 AI 的智能小说创作助手**

[特性](#-特性) • [快速开始](#-快速开始) • [配置说明](#%EF%B8%8F-配置说明) • [项目结构](#-项目结构)

</div>

---

## ✨ 特性

- 🤖 **多 AI 模型** - 支持 OpenAI、Gemini、Claude 等主流模型
- 📝 **智能向导** - AI 自动生成大纲、角色和世界观
- 👥 **角色管理** - 人物关系、组织架构可视化管理
- 📖 **章节编辑** - 支持创建、编辑、重新生成和润色
- 🌐 **世界观设定** - 构建完整的故事背景
- 🔐 **多种登录** - LinuxDO OAuth 或本地账户登录
- 💾 **PostgreSQL** - 生产级数据库，多用户数据隔离
- 🐳 **Docker 部署** - 一键启动，开箱即用

## 📋 TODO List

- [x] **灵感模式** - 创作灵感和点子生成
- [x] **自定义写作风格** - 支持自定义 AI 写作风格
- [x] **数据导入导出** - 项目数据的导入导出
- [ ] **Prompt 调整界面** - 可视化编辑 Prompt 模板
- [x] **章节字数限制** - 用户可设置生成字数
- [ ] **设定追溯与矛盾检测** - 自动检测设定冲突
- [ ] **思维链与章节关系图谱** - 可视化章节逻辑关系
- [x] **根据分析一键重写** - 根据分析建议重新生成
- [x] **Linux DO 自动创建账号** - OAuth 登录自动生成账号

> 💡 欢迎提交 Issue 或 Pull Request！

## 🚀 快速开始

### 前置要求

- Docker 和 Docker Compose
- 至少一个 AI 服务的 API Key（OpenAI/Gemini/Claude）

### Docker Compose 部署（推荐）

```bash
# 1. 克隆项目
git clone https://github.com/xiamuceer-j/MuMuAINovel.git
cd MuMuAINovel

# 2. 配置环境变量（必需）
cp backend/.env.example .env
# 编辑 .env 文件，填入必要配置（API Key、数据库密码等）

# 3. 确保文件准备完整
# ⚠️ 重要：确保以下文件存在
# - .env（配置文件，必需挂载到容器）
# - backend/scripts/init_postgres.sql（数据库初始化脚本）

# 4. 启动服务
docker-compose up -d

# 5. 访问应用
# 打开浏览器访问 http://localhost:8000
```

> **📌 注意事项**
>
> 1. **`.env` 文件挂载**: `docker-compose.yml` 会自动将 `.env` 挂载到容器，确保文件存在
> 2. **数据库初始化**: `init_postgres.sql` 会在首次启动时自动执行，安装必要的PostgreSQL扩展
> 3. **自行构建**: 如需从源码构建，请先下载 embedding 模型文件（[加群获取](frontend/public/qq.jpg)）

### 使用 Docker Hub 镜像（推荐新手）

```bash
# 1. 拉取最新镜像（已包含模型文件）
docker pull mumujie/mumuainovel:latest

# 2. 配置 .env 文件
cp backend/.env.example .env
# 编辑 .env 填入配置

# 3. 启动服务
docker-compose up -d

# 4. 查看日志
docker-compose logs -f

# 5. 更新到最新版本
docker-compose pull
docker-compose up -d
```

> **💡 提示**: Docker Hub 镜像已包含所有依赖和模型文件，无需额外下载

### 本地开发 / 从源码构建

#### 前置准备

```bash
# ⚠️ 重要：如果从源码构建，需要先下载 embedding 模型文件
# 模型文件较大（约 400MB），需放置到以下目录：
# backend/embedding/models--sentence-transformers--paraphrase-multilingual-MiniLM-L12-v2/
#
# 📥 获取方式：
# - 加入项目 QQ 群或 Linux DO 讨论区获取下载链接
# - 群号：见项目主页
# - Linux DO：https://linux.do/t/topic/1100112
```

#### 后端

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 配置 .env 文件
cp .env.example .env
# 编辑 .env 填入必要配置

# 启动 PostgreSQL（可使用 Docker）
docker run -d --name postgres \
  -e POSTGRES_PASSWORD=your_password \
  -e POSTGRES_DB=mumuai_novel \
  -p 5432:5432 \
  postgres:18-alpine

# 启动后端
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

#### 前端

```bash
cd frontend
npm install
npm run dev  # 开发模式
npm run build  # 生产构建
```

## ⚙️ 配置说明

### 必需配置

创建 `.env` 文件：

```bash
# PostgreSQL 数据库（必需）
DATABASE_URL=postgresql+asyncpg://mumuai:your_password@postgres:5432/mumuai_novel
POSTGRES_PASSWORD=your_secure_password

# AI 服务（至少配置一个）
OPENAI_API_KEY=your_openai_key
OPENAI_BASE_URL=https://api.openai.com/v1
DEFAULT_AI_PROVIDER=openai
DEFAULT_MODEL=gpt-4o-mini

# 本地账户登录
LOCAL_AUTH_ENABLED=true
LOCAL_AUTH_USERNAME=admin
LOCAL_AUTH_PASSWORD=your_password
```

### 可选配置

```bash
# Gemini
GEMINI_API_KEY=your_gemini_key

# Claude
ANTHROPIC_API_KEY=your_claude_key

# LinuxDO OAuth
LINUXDO_CLIENT_ID=your_client_id
LINUXDO_CLIENT_SECRET=your_client_secret
LINUXDO_REDIRECT_URI=http://localhost:8000/api/auth/callback

# PostgreSQL 连接池（高并发优化）
DATABASE_POOL_SIZE=30
DATABASE_MAX_OVERFLOW=20
```

### 中转 API 配置

支持所有 OpenAI 兼容格式的中转服务：

```bash
# New API 示例
OPENAI_API_KEY=sk-xxxxxxxx
OPENAI_BASE_URL=https://api.new-api.com/v1

# 其他中转服务
OPENAI_BASE_URL=https://your-proxy-service.com/v1
```

## 🐳 Docker 部署详情

### 服务架构

- **postgres**: PostgreSQL 18 数据库
  - 端口: 5432
  - 数据持久化: `postgres_data` volume
  - 初始化脚本: `backend/scripts/init_postgres.sql`（自动挂载）
  - 优化配置: 支持 80-150 并发用户

- **mumuainovel**: 主应用服务
  - 端口: 8000
  - 日志目录: `./logs`
  - 配置挂载: `.env` 文件
  - 自动等待数据库就绪
  - 健康检查: 每 30 秒检测一次

### 重要文件说明

| 文件 | 说明 | 是否必需 |
|------|------|---------|
| `.env` | 环境配置（API Key、数据库密码等） | ✅ 必需 |
| `docker-compose.yml` | 服务编排配置 | ✅ 必需 |
| `backend/scripts/init_postgres.sql` | PostgreSQL 扩展安装脚本 | ✅ 自动挂载 |
| `backend/embedding/models--*/` | Embedding 模型文件 | ⚠️ 自建需要 |

> **注意**: 使用 Docker Hub 镜像时，模型文件已包含在镜像中，无需额外下载

### 常用命令

```bash
# 启动服务
docker-compose up -d

# 查看状态
docker-compose ps

# 查看日志
docker-compose logs -f

# 停止服务
docker-compose down

# 重启服务
docker-compose restart

# 查看资源使用
docker stats
```

### 数据持久化

- `./postgres_data` - PostgreSQL 数据库文件
- `./logs` - 应用日志文件

### 端口配置

修改 `docker-compose.yml` 中的端口映射：

```yaml
ports:
  - "8800:8000"  # 宿主机:容器
```

## 📁 项目结构

```
MuMuAINovel/
├── backend/                 # 后端服务
│   ├── app/
│   │   ├── api/            # API 路由
│   