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

---

## ✨ 特性亮点

| | 特性 | 说明 |
|---|---|---|
| 🌐 | **浏览器全流程操控** | 部署一次，任何设备的浏览器即可完成全流程操作 —— 权限审批、方案协商、任务管控，手机上也能用，无需安装客户端 |
| 🤖 | **多 Agent 协作** | Team（固定分工）/ Swarm（动态协商）/ SubAgent（主从委派）三种协作模式，复杂任务自动分工 |
| 🔒 | **深度安全架构** | 8 层 Bash 沙箱 + 14 步权限管道 + 289 项安全测试，命令执行前必过安全关卡 |
| 🇨🇳 | **国产大模型直连** | 千问 / DeepSeek / Moonshot 开箱即用，国内网络直连，无需科学上网 |
| 🐳 | **Docker 一键部署** | `docker compose up -d` 一条命令启动，数据存本地，完全私有 |

---

## 🎬 Demo

### 写入文件
![写入文件演示](docs/assets/demo-write-file.gif)

### iPad 浏览器全流程操控
![iPad浏览器操控演示](docs/assets/demo-ipad-browser.gif)

---

## ⚡ 快速开始

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

启动完成后，打开浏览器访问 **http://localhost:8080** 即可使用。

> **系统要求：** Docker 20.10+，Docker Compose V2，建议 4GB+ 内存。

### 方式二：本地开发

**前置条件：** JDK 21、Node.js 20+、Python 3.11+

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

在 `.env` 中配置 `LLM_BASE_URL` 和 `LLM_API_KEY` 即可切换：

| 服务商 | Base URL | 推荐模型 | 备注 |
|--------|----------|----------|------|
| **千问/DashScope** | `https://dashscope.aliyuncs.com/compatible-mode/v1` | qwen3.6-plus | **默认**，国内直连 |
| **DeepSeek** | `https://api.deepseek.com/v1` | deepseek-chat | 国内直连 |
| **Moonshot（Kimi）** | `https://api.moonshot.cn/v1` | moonshot-v1-auto | 国内直连 |
| **OpenAI** | `https://api.openai.com/v1` | gpt-4o | 需要外网访问 |
| **本地 Ollama** | `http://localhost:11434/v1` | qwen2.5:latest | 完全离线 |

> 任何兼容 OpenAI API 格式的服务商都可以接入，只需配置对应的 Base URL 和 API Key。

---

## 📊 竞品对比

### 功能对比

| 特性 | ZhikunCode | Aider | Cline | Cursor | Claude Code | Copilot |
|------|:---:|:---:|:---:|:---:|:---:|:---:|
| 开源免费 | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |
| Web UI | ✅ 全功能 | ⚠️ Streamlit | ❌ | ⚠️ Web版 | ✅ | ❌ |
| Docker 一键自托管 | ✅ 完整 Web 服务 | ⚠️ CLI 容器化 | ❌ | ⚠️ 企业付费 | ❌ | ❌ |
| 国产大模型直连 | ✅ 原生支持 | ⚠️ 需配置兼容 API | ⚠️ 需配置兼容 API | ❌ | ❌ | ❌ |
| 多 Agent 协作 | ✅ Team/Swarm/Sub | ❌ | ❌ | ✅ Multi-Agents | ✅ Sub-Agents | ✅ Agent Mode |
| 浏览器全流程操控¹ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 安全沙箱 | ✅ 8层 | ❌ | ❌ | ⚠️ 企业级 | ✅ OS级 | N/A |
| MCP 工具扩展 | ✅ | ⚠️ 第三方 | ✅ | ❌ | ✅ | ✅ |
| 无需安装客户端 | ✅ | ❌ | ❌ | ⚠️ | ✅ | ❌ |

> ¹ **浏览器全流程操控**：部署后任意设备浏览器（包括手机）即可完整操控编码全流程——权限审批、方案协商、任务管控。这与 Cline/Cursor 的"AI 控制浏览器做自动化测试"是不同的概念。

### 安全特性对比

| 安全特性 | ZhikunCode | Aider | Cline | Claude Code |
|---------|:---:|:---:|:---:|:---:|
| 命令执行沙箱 | 8 层检查 | ❌ 用户审批 | ❌ 用户审批 | ✅ gVisor/Firecracker |
| 权限管道 | 14 步管线 | ❌ | 简单确认 | 权限管理系统 |
| 安全测试覆盖 | 289 项 | 未公开 | 未公开 | 未公开 |
| 敏感路径拦截 | ✅ | ❌ | ❌ | ❌ |
| 危险命令阻断 | ✅ | ❌ | ❌ | ✅ 部分 |
| 环境变量白名单 | ✅ | ❌ | ❌ | ❌ |

> **说明：** 以上对比基于各项目公开文档（2025 Q2），如有不准确之处欢迎提 [Issue](https://github.com/zhikunqingtao/zhikuncode/issues) 指正。Cursor 2.0+ 和 GitHub Copilot Agent Mode 为较新特性，功能仍在快速迭代中。

---

## 🏗️ 架构概览

ZhikunCode 采用三端分离架构，Java 后端负责核心编排，React 前端提供交互界面，Python 服务处理代码分析：

```
┌──────────────────┐      WebSocket / HTTP      ┌──────────────────────┐
│    Frontend       │ ◄───────────────────────