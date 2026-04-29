<h1 align="center">Fund Analysis Agents</h1>

<p align="center">
  <strong>基于多智能体协作的中国基金市场智能分析系统</strong>
</p>

<p align="center">
  <a href="#核心特性">核心特性</a> •
  <a href="#系统架构">系统架构</a> •
  <a href="#快速开始">快速开始</a> •
  <a href="#配置说明">配置说明</a> •
  <a href="#开发指南">开发指南</a> •
  <a href="#路线图">路线图</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Java-21-orange?style=flat-square" alt="Java 21" />
  <img src="https://img.shields.io/badge/Spring%20Boot-3.4-green?style=flat-square" alt="Spring Boot" />
  <img src="https://img.shields.io/badge/Spring%20AI-1.0-blue?style=flat-square" alt="Spring AI" />
  <img src="https://img.shields.io/badge/Vue-3-brightgreen?style=flat-square" alt="Vue 3" />
  <img src="https://img.shields.io/badge/License-Apache%202.0-blue?style=flat-square" alt="License" />
</p>

---

## 项目简介

Fund Analysis Agents 是一个面向中国公募基金市场的 AI 智能分析系统。通过多个专业化 AI
Agent（分析师、研究员、交易员、风控经理）协作，模拟真实投研团队的工作流程，为个人投资者提供**严谨、理性、可追溯**的基金投资分析与建议。

> **免责声明**：本系统生成的所有分析报告仅供参考，不构成投资建议。投资有风险，入市需谨慎。

<p align="center">
  <img src="docs/images/dashboard.png" alt="管理后台仪表盘" width="80%" />
  <br/>
  <em>管理后台 — 自选基金、持仓管理、净值走势</em>
</p>

<p align="center">
  <img src="docs/images/agent-flow.png" alt="Agent 分析流程可视化" width="80%" />
  <br/>
  <em>Agent 分析流程 — 多智能体协作、辩论、决策全链路可视化</em>
</p>

## 核心特性

**多智能体协作分析**

- 6 个专业分析师 Agent 并行执行（基金、技术、行业、经理、情绪、新闻）
- 看多/看空研究员 3 轮结构化辩论，避免单一视角偏差
- 交易建议师 → 风控经理 → 组合顾问，逐层审核决策
- 基于 Spring AI Alibaba Graph 的 DAG 流程编排
- Agent 执行流程可视化，点击节点查看每个 Agent 的分析详情

**配置化管理后台**

- Vue 3 + Element Plus 响应式管理界面
- 自选基金、持仓管理、收益跟踪、净值走势图
- 多 LLM 模型配置（通义千问 / DeepSeek / OpenAI / 智谱），每个 Agent 可独立绑定模型
- 数据源动态配置与健康度监控
- 可视化定时任务管理（Cron 表达式）
- 系统架构实时状态图

**定时分析与智能推送**

- 盘中监控、盘后分析、每日/周/月报告
- 邮件（HTML 富文本）+ Bark 手机推送
- 中国交易日历适配，自动跳过非交易日

**证据可追溯**

- 每条结论标注证据层级：FACT（已披露事实）/ ESTIMATE（实时估算）/ INFERENCE（AI 推断）
- 完整的数据来源、采集时间、模型版本记录
- 分析批次管理，支持历史报告对比

**中国基金市场深度适配**

- 聚焦主动权益基金（股票型 + 偏股混合型）
- 基金经理变更预警、规模异动监控、限购状态跟踪
- 季报持仓变动分析、A/C 份额对比推荐
- 组合层风控规则（行业暴露、经理集中度、主题重复等）

**市场扫描与智能选基**

- 市场温度判断（危机/低迷/震荡/正常/过热），熊市自动抑制推荐
- 投资者适当性画像（风险等级、偏好行业、回撤容忍度等标签式配置）
- 量化初筛（规模、年限、业绩、回撤、夏普）+ 画像约束 + 交易可达性检查
- LLM 深度分析精选，结合现有持仓做组合适配，避免重复暴露
- A/C 份额自动推荐、申购费率展示、限购状态标注
- 时点快照留痕，每次推荐可完整复盘"为什么选了这几只"
- L1 数据不足时宁可不推荐，也不硬给名单

---

## 系统架构

```
┌─────────────────────────────────────────────────────────────┐
│  Presentation    Vue3 Admin │ REST API │ Bark/Email/Webhook │
│                  OpenClaw Plugin Interface (预留)            │
├─────────────────────────────────────────────────────────────┤
│  Application     Portfolio Mgmt │ Orchestrator │ Scheduler  │
├─────────────────────────────────────────────────────────────┤
│  Agent Layer     Analysts(6) → Bull/Bear Debate → Decision  │
│                  确定性因子引擎 + LLM 解释层                  │
├─────────────────────────────────────────────────────────────┤
│  Data Layer      天天基金 │ 东方财富 │ Tushare │ 新闻爬取    │
├─────────────────────────────────────────────────────────────┤
│  Infrastructure  MySQL │ Redis │ Docker │ Spring Boot 3.4   │
└─────────────────────────────────────────────────────────────┘
```

**Maven 多模块结构**

```
fund-analysis-agents/
├── fund-common           # 公共模块：工具类、枚举、异常、安全
├── fund-datasource       # 数据源：天天基金/东方财富/Tushare 适配器
├── fund-agent-core       # Agent 核心：多智能体、辩论、决策、图编排
├── fund-service          # 业务服务：分析编排、组合管理、通知、调度
├── fund-administration   # 管理后台：REST API + Vue 3 前端
└── fund-application      # 启动模块：Spring Boot Application
```

---

## 快速开始

### 环境要求

| 组件             | 版本要求   | 说明               |
|----------------|--------|------------------|
| Docker         | 20.10+ | 用于运行 MySQL、Redis |
| Docker Compose | v2+    | 中间件编排            |
| JDK            | 21     | 项目编译运行           |
| Maven          | 3.9+   | 项目构建             |
| Node.js        | 18+    | 前端构建（可选，脚本自动处理）  |

### 一键部署

> **不想折腾？** 如果你不熟悉 Java/Maven/Docker 环境配置，可以直接将本项目 clone 到本地，然后把这份 README 和 `scripts/` 目录下的脚本交给 AI（如 Claude、ChatGPT），让它帮你完成环境安装和项目启动。

我们提供了跨平台的一键部署脚本，自动完成以下全部流程：

```
环境检查 → .env 配置校验 → MySQL/Redis 启动 → 后端编译 → 前端构建 → 应用启动
```

**macOS / Linux：**

```bash
# 1. 克隆项目
git clone https://github.com/liuyocom/fund-analysis-agents.git
cd fund-analysis-agents

# 2. 配置 API Key（至少填写一个 LLM Key，推荐通义千问）
cp .env.example .env
vim .env    # 或用任意编辑器打开

# 3. 一键启动（自动完成环境检查、中间件启动、编译、运行）
chmod +x scripts/setup.sh
./scripts/setup.sh
```

**Windows：**

```powershell
# 1. 克隆项目
git clone https://github.com/liuyocom/fund-analysis-agents.git
cd fund-analysis-agents

# 2. 配置 API Key（至少填写一个 LLM Key，推荐通义千问）
copy .env.example .env
notepad .env

# 3. 一键启动
scripts\setup.bat
```

启动成功后：
- 管理后台：http://localhost:8080
- API 文档：http://localhost:8080/swagger-ui.html
- 默认账号：`admin` / `admin2026`

> 脚本会自动检测缺失的依赖并给出安装提示。如果没有安装 Node.js，前端构建会被跳过（不影响后端功能）。

---

## 配置说明

### .env 配置项

项目通过 `.env` 文件管理所有外部配置，复制 `.env.example` 后按需填写即可。

| 配置项 | 必填 | 说明 |
|-------|------|------|
| `DASHSCOPE_API_KEY` | 三选一 | 通义千问 API Key（推荐，性价比高） |
| `OPENAI_API_KEY` | 三选一 | OpenAI API Key |
| `DEEPSEEK_API_KEY` | 三选一 | DeepSeek API Key |
| `SMTP_HOST` / `SMTP