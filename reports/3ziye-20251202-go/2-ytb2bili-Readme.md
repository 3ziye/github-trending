# YTB2BILI - YouTube 到 Bilibili 自动化转载系统

一个功能完整的视频自动化处理系统，支持从 YouTube 等平台下载视频，自动生成字幕、翻译内容、生成元数据，并定时上传到 Bilibili。

## ✨ 核心功能

### 🎬 智能视频处理链

**4步准备流程（实时处理）**：
1. **🎬 字幕生成** - 使用 Whisper AI 自动生成高质量字幕
2. **📷 封面下载** - 自动下载并上传高清封面到云存储
3. **🌐 字幕翻译** - 支持百度翻译和 DeepSeek AI 多语言翻译
4. **🤖 元数据生成** - AI 分析视频内容，生成符合 B站规范的标题、描述、标签

**定时上传策略（智能调度）**：
- **🎥 视频上传** - 每小时上传一个处理完成的视频
- **📝 字幕上传** - 视频上传成功后1小时自动上传字幕

### 📊 可视化管理面板
- **📋 视频列表** - 实时查看所有视频的处理状态
- **🔍 详细信息** - 完整的视频信息和处理步骤追踪  
- **🎯 单步重试** - 支持重新执行失败的任务步骤
- **📈 进度监控** - 实时进度百分比和处理时长统计
- **📁 文件管理** - 查看和下载所有生成的文件（视频、字幕、封面等）

### 🔐 B站账户集成
- **📱 扫码登录** - 支持 Bilibili TV 扫码快速登录
- **🖼️ 二维码生成** - 后端自动生成 PNG 格式登录二维码
- **🔄 自动检测** - 前端实时轮询检测登录状态
- **👤 用户信息** - 获取并展示用户名、头像等信息
- **💾 状态持久化** - 自动保存登录 Token 和 Cookie
- **⚡ 状态检查** - 智能检测账户登录状态

---

## 🏗️ 技术架构

### 🖥️ 后端技术栈
- **语言**: Go 1.24+ (支持最新语言特性)
- **Web 框架**: Gin (高性能HTTP框架)
- **ORM**: GORM v2 (支持多数据库)
- **数据库**: MySQL 8.0+ / PostgreSQL 15+ / SQLite (开发环境)
- **文件存储**: 腾讯云 COS (支持大文件分片上传)
- **依赖注入**: Uber FX (声明式依赖管理)
- **定时任务**: Robfig Cron v3 (精确到秒级调度)
- **日志**: Zap + Lumberjack (结构化日志和日志轮转)

### 🌐 前端技术栈 
- **框架**: Next.js 15+ (支持 App Router)
- **语言**: TypeScript 5.x (完全类型安全)
- **UI 库**: React 18 + Tailwind CSS 3.x
- **图标**: Lucide React (现代化图标库)
- **HTTP 客户端**: Axios (支持请求拦截和重试)
- **构建**: 静态导出 + 嵌入式部署

### 🔗 外部服务集成
- **🎤 yt-dlp** - 多平台视频下载 (YouTube, TikTok, 等)
- **🧠 Whisper AI** - 高精度语音识别和字幕生成
- **🌐 百度翻译 API** - 专业机器翻译服务
- **🤖 DeepSeek AI** - 先进的AI翻译和内容生成
- **📺 Bilibili SDK** - 官方视频上传和用户认证API
- **☁️ 腾讯云 COS** - 企业级对象存储服务
- **📊 数据分析** - 可选的用户行为分析和统计

---

## 📁 项目结构

```
ytb2bili/
├── main.go                      # 🚀 应用程序入口和依赖注入配置
├── Makefile                     # 📦 自动化构建脚本 (前端+后端一键打包)
├── config.toml                  # ⚙️ 主配置文件
├── config.toml.example          # 📋 配置文件模板
├── go.mod                       # 📦 Go 模块依赖管理
└── README.md                    # 📖 项目文档

internal/                        # 🏠 内部业务逻辑
├── chain_task/                  # ⛓️ 任务链处理引擎
│   ├── chain_task_handler.go    # 任务链执行器 (准备阶段: 字幕生成→翻译→元数据)
│   ├── upload_scheduler.go      # 上传调度器 (定时上传: 视频→字幕)
│   ├── base/
│   │   └── base_task.go         # 任务基类
│   ├── handlers/                # 🔧 具体任务处理器
│   │   ├── generate_subtitles.go      # 字幕生成 (Whisper AI)
│   │   ├── translate_subtitle.go      # 字幕翻译 (百度/DeepSeek)
│   │   ├── generate_metadata.go       # 元数据生成 (AI标题描述)
│   │   ├── download_img_handler.go    # 封面下载处理
│   │   ├── upload_to_bilibili.go      # 视频上传到B站
│   │   ├── upload_subtitle_to_bilibili.go  # 字幕上传到B站
│   │   └── ...
│   └── manager/
│       ├── chain.go             # 任务链管理
│       └── state.go             # 状态管理
├── core/                        # 🎯 核心业务层
│   ├── app_server.go            # HTTP 服务器配置
│   ├── models/                  # 📊 数据模型
│   │   ├── tb_video.go          # 视频表模型
│   │   ├── tb_task_step.go      # 任务步骤模型
│   │   ├── tb_user.go           # 用户模型
│   │   └── ...
│   ├── services/                # 🔄 业务服务层
│   │   ├── tb_video_service.go  # 视频业务逻辑
│   │   ├── task_step_service.go # 任务步骤管理
│   │   └── saved_video_service.go
│   └── types/
│       ├── app_config.go        # 应用配置定义
│       └── task_interface.go    # 任务接口定义
├── handler/                     # 🌐 HTTP 请求处理器
│   ├── auth_handler.go          # 认证相关 API
│   ├── video_handler.go         # 视频管理 API
│   ├── upload_handler.go        # 上传相关 API
│   ├── subtitle_handler.go      # 字幕处理 API
│   └── ...
├── storage/                     # 💾 存储抽象层
│   ├── interfaces.go            # 存储接口定义
│   └── login_store.go           # 登录状态存储
└── web/                         # 🌟 内嵌前端资源
    ├── static.go                # 静态文件服务器
    └── bili-up-web/             # Next.js 编译后的静态文件
        ├── index.html           # 前端入口页面
        ├── _next/               # Next.js 静态资源
        └── ...

pkg/                             # 📚 可重用组件库
├── analytics/                   # 📊 数据分析客户端
│   ├── client.go
│   └── middleware.go
├── cos/                         # ☁️ 腾讯云COS存储客户端
│   ├── cos_client.go
│   ├── cos_handler.go
│   └── download_utils.go
├── logger/                      # 📝 日志组件
│   └── logger.go
├── services/                    # 🛠️ 通用服务
│   └── subtitle_service.go
├── store/                       # 🗃️ 数据库操作
│   ├── database.go              # 数据库连接
│   ├── migrate.go               # 数据库迁移
│   └── model/                   # 数据库模型
├── translator/                  # 🌐 翻译服务
│   ├── baidu_translator.go      # 百度翻译
│   ├── deepseek_translator.go   # DeepSeek翻译
│   ├── factory.go               # 翻译器工厂
│   └── manager.go               # 翻译管理器
└── utils/                       # 🧰 工具函数
    ├── crypto.go                # 加密工具
    ├── ffmpeg_utils.go          # 视频处理工具
    ├── youtube_utils.go         # YouTube工具
    ├── ytdlp_manager.go         # yt-dlp管理器
    └── ...
```

---

## 🚀 快速开始

### ⚡ 一键部署 (推荐)

```bash
# 克隆项目 (需要前端项目在同级目录)
git clone https://github.com/difyz9/ytb2bili.git
cd ytb2bili/bili-up-api

# 一键构建 (自动构建前端+后端并打包成单个可执行文件)
make build

# 启动服务
./bili-up-api-server
```

🎉 **就这么简单！** 访问 `http://localhost:8