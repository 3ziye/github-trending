<div align="center">

<h1>🧠 Memoh-v2</h1>

## 推荐去用原项目,https://github.com/memohai/Memoh  
## 不维护了,去开发别的去了  

**真隔离 · 真记忆 · 真进化 · 真协作 —— 不妥协的 AI Agent 平台**

<p>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/license-AGPL--v3-blue.svg" alt="License" /></a>
  <a href="https://go.dev"><img src="https://img.shields.io/badge/Go-1.25-00ADD8?logo=go&logoColor=white" alt="Go" /></a>
  <a href="https://vuejs.org"><img src="https://img.shields.io/badge/Vue-3-4FC08D?logo=vuedotjs&logoColor=white" alt="Vue 3" /></a>
  <a href="https://docs.docker.com/compose/"><img src="https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white" alt="Docker" /></a>
  <a href="https://github.com/Kxiandaoyan/Memoh-v2/stargazers"><img src="https://img.shields.io/github/stars/Kxiandaoyan/Memoh-v2?style=social" alt="Stars" /></a>
</p>

<p>
  <a href="#-快速开始">快速开始</a> ·
  <a href="#-核心亮点">核心亮点</a> ·
  <a href="#-21-项内置技能">技能系统</a> ·
  <a href="#-团队协作多-bot-编排">团队协作</a> ·
  <a href="#-多平台频道接入">多平台接入</a> ·
  <a href="./README_EN.md">English</a>
</p>

<p>
  <a href="./doc/installation.md">🚀 安装与升级</a> ·
  <a href="./doc/features.md">📖 功能详解</a> ·
  <a href="./doc/concepts.md">💡 概念指南</a> ·
  <a href="./doc/README.md">📚 使用教程</a>
</p>
<p>
  <a href="./doc/screenshots.md">🖼️ 界面截图</a> ·
  <a href="./doc/comparison.md">⚖️ 与 OpenClaw 对比</a> ·
  <a href="./doc/known-limitations.md">⚠️ 已知局限性</a>
</p>
<p>
  <a href="./doc/FEATURE_AUDIT.md">📊 功能审计</a> ·
  <a href="./doc/PROMPTS_INVENTORY.md">📝 提示词清单</a> ·
  <a href="./doc/README.md#开发计划归档">🗂️ 开发计划归档</a>
</p>

<br/>

每个 Bot 一个 containerd 容器，不是共享运行时；<br/>
Qdrant + BM25 + LLM 三层记忆提取，不是 SQLite 向量搜索；<br/>
Bot 自己反思、实验、审查，持续进化，不是手动编辑记忆文件；<br/>
组建 AI 团队，大总管调度成员协作，不是单打独斗；<br/>
对接 Telegram / 飞书 / 个人微信 / Discord，一个 Bot 服务全平台。

</div>

---

<p align="center">
  <img src="./doc/1.png" width="100%" />
</p>

<p align="center">
  <a href="./doc/screenshots.md">👉 查看更多截图</a>
</p>

---

## 🚀 快速开始

**一键安装（需要 Docker）：**

```bash
curl -fsSL https://raw.githubusercontent.com/Kxiandaoyan/Memoh-v2/main/scripts/install.sh | sh
```

> 静默安装（跳过交互）：`curl -fsSL ... | sh -s -- -y`

或手动：

```bash
git clone --depth 1 https://github.com/Kxiandaoyan/Memoh-v2.git
cd Memoh-v2
docker compose up -d
```

访问 **http://localhost:8082**，默认登录：`admin` / `admin123`

**首次配置流程：**

```
1. 设置 → Provider      添加 API 服务商，填入 API Key 和 Base URL
       ↓
2. Provider → 模型       在 Provider 下添加模型（chat 或 embedding 类型）
       ↓
3. 新建 Bot              选择模板或空白创建，设置名称和类型
       ↓
4. Bot → 设置           选择 Chat 模型、Embedding 模型、语言等
       ↓
5. Bot → 频道           连接 Telegram / 飞书等消息平台（可选）
```

**升级：**

```bash
./scripts/upgrade.sh
```

> 自动备份数据库 → 拉取最新代码 → 重建服务 → 运行迁移 → 同步技能到所有 Bot

> 📖 详细安装、升级、卸载、数据迁移指南：[安装与升级](./doc/installation.md)

---

## ✨ 核心亮点

### 🔒 真隔离 — 每个 Bot 一个容器

不是共享进程，不是 Docker-in-Docker，是真正的 **containerd 容器隔离**。每个 Bot 拥有独立的文件系统、Shell、网络和浏览器环境。支持快照回滚，一键恢复到任意历史状态。

### 🧠 真记忆 — 三层记忆提取

| 层级 | 技术 | 作用 |
|------|------|------|
| 语义搜索 | Qdrant 向量数据库 | 理解"意思相近"的内容 |
| 关键词索引 | BM25 | 精确匹配专有名词和术语 |
| 智能提取 | LLM | 每次对话后自动提炼关键信息入库 |

24 小时短期记忆自动加载，长期记忆语义召回，Token 预算自动裁剪并用 LLM 摘要补偿。

**更多记忆特性：**
- 🧩 **事实自动提取** — 对话后自动提炼用户偏好、个人信息、计划意图等关键事实
- 🔧 **解决方案记忆** — 自动识别对话中的「问题→解决方案」对，下次遇到类似问题直接召回
- 🤝 **集体记忆** — 同一 Bot 的所有对话共享知识库，A 用户教会的知识，B 用户也能受益
- ⏳ **时间衰减** — 记忆按半衰期（30天）自动降权，越新的记忆权重越高
- 🗜️ **记忆压缩** — 当记忆条目过多时，LLM 自动合并冗余、去除矛盾，保持精简
- 🌍 **30+ 语言** — BM25 索引支持中日韩英法德等 30+ 语言的分词和检索

### 🧬 真进化 — 三阶段自我进化

Bot 不是静态的 prompt，而是会成长的智能体：

```
反思 (Reflection) → 实验 (Experiment) → 审查 (Review) → 循环
```

完整进化日志追踪，每一步改变都有据可查。

### 👥 真协作 — 多 Bot 团队编排

一键组建 AI 团队，自动生成"大总管"Bot 统一调度：

- 大总管通过 `call_agent` 工具调用团队成员
- 成员回复自动带 **【Bot名称】** 前缀，来源清晰
- 团队可直接对接 Telegram / 飞书等平台
- 支持心跳巡检，大总管定期检查团队任务状态

---

## 💰 零成本基础设施

不依赖任何付费第三方 API，核心能力全部自托管：

| 能力 | 方案 | 费用 |
|------|------|:----:|
| **联网搜索** | SearXNG 元搜索引擎（Docker 内置） | **免费** |
| **向量数据库** | Qdrant（Docker 内置） | **免费** |
| **关键词索引** | BM25 内置引擎（无需 Elasticsearch） | **免费** |
| **容器隔离** | Containerd（Docker 内置） | **免费** |
| **本地模型** | Ollama 支持（可选） | **免费** |

> 💡 搜索不花钱！SearXNG 聚合 Google、Bing、DuckDuckGo 等多个搜索引擎，无需任何 API Key。

---

## 🔌 10 种 AI 模型提供方

不绑定任何单一厂商，自由选择最适合的模型：

| 提供方 | 说明 |
|--------|------|
| OpenAI | GPT-4o、GPT-4、GPT-3.5 等 |
| Anthropic | Claude 3.5、Claude 3 等 |
| Google | Gemini 系列 |
| Azure OpenAI | 企业级 Azure 部署 |
| AWS Bedrock | AWS 托管模型 |
| Mistral AI | Mistral 系列 |
| xAI | Grok 系列 |
| Ollama | 🏠 **本地模型，零 API 费用** |
| 阿里云 DashScope | 通义千问系列 |
| OpenAI 兼容 | 任何兼容 OpenAI 格式的第三方 API |

> 每个 Bot 可独立配置对话模型、记忆模型、嵌入模型和视觉模型（VLM），灵活组合。

---

## 🛠 21 项内置技能

每个新建 Bot 自动获得全部技能，开箱即用。Bot 在对话中通过 `use_skill` 工具按需激活。

| 技能 | 用途 | 默认 |
|------|------|:----:|
| **web-search** | 联网搜索（SearXNG） | ✅ |
| **mcp-builder** | 构建自定义 MCP 服务器 | ✅ |
| **skill-creator** | 创建新技能 | ✅ |
| **webapp-testing** | Web 应用测试 | ✅ |
| **scheduled-task** | 定时任务调度 | ✅ |
| **web-artifacts-builder** | 构建 Web 制品 | ✅ |
| **develop-web-game** | 开发 Web 游戏 | ✅ |
| **playwright** | 浏览器自动化 | ✅ |
| **create-plan** | 任务规划 | ✅ |
| **canvas-design** | Canvas 画布设计 | ✅ |
