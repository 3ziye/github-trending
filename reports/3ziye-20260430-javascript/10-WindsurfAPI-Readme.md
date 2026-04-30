# 给我点 Star 和 Follow 我就不管你了

<p align="center">
  <a href="https://github.com/dwgx/WindsurfAPI/stargazers"><img src="https://img.shields.io/github/stars/dwgx/WindsurfAPI?style=for-the-badge&logo=github&color=f5c518" alt="Stars"></a>&nbsp;
  <a href="https://github.com/dwgx"><img src="https://img.shields.io/github/followers/dwgx?label=Follow&style=for-the-badge&logo=github&color=181717" alt="Follow"></a>
  &nbsp;·&nbsp;
  <a href="README.en.md">English</a>
</p>

# 声明

> **没点 Star 和 Follow 的**：严禁商业使用、转售、代部署、挂后台对外提供服务、包装成中转服务出售。
> **点了 Star 和 Follow 的**：随便用，我睁一只眼闭一只眼。
>
> 代码本体按 MIT License 开源（见 [LICENSE](LICENSE)），上面这段是作者个人态度。

---

把 [Windsurf](https://windsurf.com)（原 Codeium）的 AI 模型变成**两套标准 API 同时兼容**：

- `POST /v1/chat/completions` — **OpenAI 兼容** 任何 OpenAI SDK 直接用
- `POST /v1/messages` — **Anthropic 兼容** Claude Code / Cline / Cursor 直接连

**100+ 模型**：Claude 4.5/4.6/Opus 4.7 · GPT-5/5.1/5.2/5.4 全系 · Gemini 2.5/3.0/3.1 · Grok · Qwen · Kimi K2.x · GLM 4.7/5/5.1 · MiniMax · SWE 1.5/1.6 · Arena 等。零 npm 依赖 纯 Node.js。

## 它到底在干嘛

```
     ┌─────────────┐   /v1/chat/completions   ┌────────────┐
     │ OpenAI SDK  │ ──────────────────────→  │            │
     │ curl / 前端 │ ←──────────────────────  │            │
     └─────────────┘   OpenAI JSON + SSE      │ WindsurfAPI│
                                              │ Node.js    │      ┌──────────────┐       ┌─────────────────┐
     ┌─────────────┐   /v1/messages           │ (本服务)   │ gRPC │ Language     │ HTTPS │ Windsurf 云端   │
     │ Claude Code │ ──────────────────────→  │            │ ───→ │ Server (LS)  │ ────→ │ server.self-    │
     │ Cline       │ ←──────────────────────  │            │ ←─── │ (Windsurf    │ ←─── │ serve.windsurf  │
     │ Cursor      │   Anthropic SSE          │            │      │  binary)     │       │ .com            │
     └─────────────┘                          └────────────┘      └──────────────┘       └─────────────────┘
                                                    ↑
                                                账号池轮询
                                                速率限制隔离
                                                故障转移
```

**它做了什么**：
1. 一个 HTTP 服务（端口 3003）同时暴露 OpenAI 和 Anthropic 两套 API
2. 把请求翻译成 Windsurf 内部 gRPC 协议，通过本地 Language Server 发给 Windsurf 云
3. 维护账号池，自动轮询 + 速率限制 + 故障转移
4. 返回前把上游 Windsurf 身份剥掉，模型自称"我是 Claude Opus 4.6 由 Anthropic 开发"

## Claude Code / Cline / Cursor 怎么用

模型本身**不会**操作文件 — 文件操作是 IDE Agent 客户端（Claude Code / Cline 等）在本地执行的：

```
 你 "帮我改 bug"                Claude Code                    WindsurfAPI               Windsurf Cloud
   │                                │                               │                          │
   │────────────────────────────→  │                               │                          │
   │                                │  POST /v1/messages            │                          │
   │                                │  messages + tools + system    │                          │
   │                                │ ─────────────────────────────→│ 打包成 Cascade 请求      │
   │                                │                               │ ──────────────────────→  │
   │                                │                               │                          │
   │                                │                               │               模型思考 → 返回
   │                                │                               │               tool_use(edit_file)
   │                                │                               │ ←──────────────────────  │
   │                                │ ←── Anthropic SSE ────────────│                          │
   │                                │   content_block=tool_use      │                          │
   │                                │                               │                          │
   │                                │ 本地执行 edit_file()          │                          │
   │                                │ (读写本地文件)                │                          │
   │                                │                               │                          │
   │                                │ 带 tool_result 再发一轮       │                          │
   │                                │ ─────────────────────────────→│ ──────────────────────→  │
   │                                │                                             ... (循环) ...
   │                                │                               │                          │
   │  ← 最终答案                    │                               │                          │
```

**重点**：WindsurfAPI 只负责**传递** tool_use / tool_result，真正改文件的是客户端 CLI。

## 快速开始

### 一键部署

```bash
git clone https://github.com/dwgx/WindsurfAPI.git
cd WindsurfAPI
bash setup.sh          # 建目录 · 配权限 · 生成 .env
node src/index.js
```

Dashboard：`http://你的IP:3003/dashboard`

### Docker 部署

```bash
cp .env.example .env

# 可选：提前把 language_server_linux_x64 放到 .docker-data/opt/windsurf/ 下
# 不放也行，容器首次启动时会自