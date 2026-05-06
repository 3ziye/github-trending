[🌐 English](docs/README_EN.md)

<div align="center">
  <img src="docs/assets/logo.svg" alt="ZhikunCode" width="120" />
  <h1>ZhikunCode</h1>
  <p><strong>开源 AI 编程助手 — 部署一次，浏览器全流程操控</strong></p>
  <p>多 Agent 协作 · Docker 自托管 · 国产大模型直连 · 深度安全架构</p>

  <p>
    <a href="#-快速开始">快速开始</a> ·
    <a href="#-特性亮点">核心特性</a> ·
    <a href="#-demo">在线演示</a> ·
    <a href="#-cli-工具">CLI 工具</a> ·
    <a href="#-skill技能系统">skill技能系统</a> ·
    <a href="#-插件系统">插件系统</a> ·
    <a href="#-可视化">可视化</a> ·
    <a href="#-记忆系统">记忆系统</a> ·
    <a href="#-竞品对比">竞品对比</a> ·
    <a href="docs/README_EN.md">English</a>
  </p>

  <p>
    <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT" /></a>
    <a href="https://github.com/zhikunqingtao/zhikuncode"><img src="https://img.shields.io/badge/Docker-Ready-blue?logo=docker" alt="Docker" /></a>
    <a href="https://github.com/zhikunqingtao/zhikuncode/stargazers"><img src="https://img.shields.io/github/stars/zhikunqingtao/zhikuncode?style=social" alt="GitHub Stars" /></a>
    <a href="https://github.com/zhikunqingtao/zhikuncode"><img src="https://img.shields.io/github/last-commit/zhikunqingtao/zhikuncode" alt="Last Commit" /></a>
    <a href="https://github.com/zhikunqingtao/zhikuncode"><img src="https://img.shields.io/github/languages/code-size/zhikunqingtao/zhikuncode" alt="Code Size" /></a>
  </p>
</div>

---

> **部署到服务器，打开浏览器就能用，手机上也行**

> 🏗️ **[查看完整系统架构图 →](https://zhikunqingtao.github.io/zhikuncode/ZhikunCode-Architecture.html)**  
> 三端分离 · 660+ 文件 · 110,646 行代码 · 全景可视化

---

## ✨ 特性亮点

| | 特性 | 说明 |
|---|---|---|
| 🌐 | **浏览器全流程操控** | 部署一次，任何设备的浏览器即可完成全流程操作 —— 权限审批、方案协商、任务管控，手机上也能用，无需安装客户端 |
| 🤖 | **多 Agent 协作** | Team（固定分工）/ Swarm（动态协商）/ SubAgent（主从委派）三种协作模式，复杂任务自动分工 |
| 🔒 | **深度安全架构** | 8 层 Bash 沙箱 + 14 步权限管道 + 289 项安全测试，命令执行前必过安全关卡 |
| 🇨🇳 | **国产大模型直连** | 千问 / DeepSeek / Moonshot 开箱即用，国内网络直连，无需科学上网 |
| 🐳 | **Docker 一键部署** | `docker compose up -d` 一条命令启动，数据存本地，完全私有 |
| ⚡ | **智能上下文管理** | 五层压缩级联 + 增量折叠（每10轮自动压缩）+ 413三阶段恢复（激进压缩→反应式压缩→媒体剥离）+ Token三级告警，无缝应对超长对话 |

---

## 🎬 Demo

### 📱 手机开发前后端 TODO 应用完整演示

https://github.com/user-attachments/assets/bf1f1d3a-4a9b-4d91-af48-97a7d3dd7b8a

### 自动写代码下载小红书视频

https://github.com/user-attachments/assets/4b66261b-3258-44bd-82d3-6b2b3bbd4995

![自动写代码下载小红书视频](docs/assets/demo-auto-code-xiaohongshu.gif)

### 📱 项目分析和命令执行演示

https://github.com/user-attachments/assets/7b45c5d4-e540-4ffd-80d4-e11502477dba

### 文件操作
![文件操作演示](docs/assets/demo-file-operation.gif)

### 生成游戏
![生成游戏演示](docs/assets/demo-game-generation.gif)

### 优化代码
![优化代码演示](docs/assets/demo-code-optimization.gif)

### 多 Agent 协作开发前后端应用
![多 Agent 协作演示](docs/assets/demo-multi-agent-todo.gif)

### iPad 浏览器全流程操控
![iPad浏览器操控演示](docs/assets/demo-ipad-browser.gif)

---

## ⚡ 快速开始

### 前置准备：获取 LLM API Key

本项目需要 LLM（大语言模型）API Key 才能运行。默认使用**阿里云千问（DashScope）**，国内网络直连。

**获取千问 API Key：**
1. 访问 [阿里云百炼平台 API Key 管理](https://bailian.console.aliyun.com/cn-beijing/?tab=model#/api-key)
2. 注册或登录阿里云账号
3. 创建 API Key，复制完整密钥（以 `sk-` 开头）

> 千问提供免费额度，足够个人开发使用。也可以使用 [DeepSeek](https://platform.deepseek.com/)、[Moonshot/Kimi](https://platform.moonshot.cn/) 等国内服务商，详见下方"支持的 LLM 服务商"。

### 方式一：Docker 部署（推荐）

只需 3 步，从零到可用：

```bash
# 1. 克隆仓库
git clone https://github.com/zhikunqingtao/zhikuncode.git
cd zhikuncode

# 2. 配置 API Key
cp .env.example .env
# 编辑 .env，填入你的 LLM API Key（默认使用千问/DashScope，国内直连）

# 3. 启动
docker compose up -d
```

> **首次构建说明：** 第一次运行会自动构建 Docker 镜像，需要下载依赖并编译，预计耗时 **15-30 分钟**（取决于网络速度）。后续启动只需几秒。可通过 `docker compose logs -f` 查看构建进度。

启动完成后，打开浏览器访问 **http://localhost:8080** 即可使用。

> **系统要求：** Docker 20.10+，Docker Compose V2，建议 4GB+ 内存。

### 方式二：本地开发

**前置条件：** JDK 21、Node.js 22+、Python 3.11~3.12（不支持 3.13+）

```bash
git clone https://github.com/zhikunqingtao/zhikuncode.git
cd zhikuncode

# 配置环境变量
cp .env.example .env
# 编辑 .env，填入你的 LLM API Key

# 一键启动三端服务
./start.sh
```

三端服务会同时启动：

| 服务 | 地址 | 说明 |
|------|------|------|
| **Backend** | `http://localhost:8080` | Java Spring Boot 后端，核心 API |
| **Python Service** | `http://localhost:8000` | FastAPI 服务，代码分析 |
| **Frontend** | `http://localhost:5173` | React 开发服务器 |

<details>
<summary><b>手动分别启动各服务</b></summary>

```bash
# 后端
cd backend && ./mvnw spring-boot:run -DskipTests

# Python 服务
cd python-service
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
uvicorn src.main:app --host 0.0.0.0 --port 8000

# 前端
cd frontend && npm install && npm run dev
```

</details>

### 支持的 LLM 服务商

ZhikunCode 支持**多 Provider 同时配置**（推荐）和单 Provider 两种模式。多 Provider 模式下可在前端自由切换模型：

**方式一：多 Provider 配置（推荐）**

在 `.env` 中为每个服务商配置独立的 API Key，前端可自由切换：

```bash
# DashScope（千问系列）
LLM_PROVIDER_DASHSCOPE_API_KEY=your-dashscope-key

# DeepSeek
LLM_PROVIDER_DEEPSEEK_API_KEY=your-deepseek-key

# Moonshot (Kimi)
LLM_PROVIDER_MOONSHOT_API_KEY=your-moonshot-key
```

**方式二：单 Provider 配置（向后兼容）**

如未配置多 Provider，系统自动回退到单 Provider 模式。在 `.env` 中配置 `LLM_BASE_URL` 和 `LLM_API_KEY` 即可切换：

| 服务商 | Base U