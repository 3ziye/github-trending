# AgentEval

A transparent HTTP proxy that captures Agent ↔ LLM API traffic, auto-splits sessions, builds structured conversation views, **grades** with multi-dimensional scoring, **diagnoses** behavioral issues via rule engine, and **probes** agent configuration for root causes — all with a built-in web dashboard.

*透明 HTTP 代理，捕获 Agent ↔ LLM 的 API 流量，自动切分 session、构建结构化视图、多维自动评分、规则诊断行为问题、探针审查配置根因 —— 内置 Web 评测面板。*

## How It Works / 工作原理

```
                         ┌──────────────────────────────┐
                         │   AgentEval (127.0.0.1:57633) │
                         └──────────────┬───────────────┘
                                        │
Agent ── HTTP ──► Proxy ── forward ──► Upstream LLM API
                    │
                    ├─ Raw traffic → logs/{stem}.jsonl
                    │  原始流量记录
                    ├─ Session detection (message rollback / idle timeout)
                    │  实时检测 session 边界
                    ├─ SessionView → logs/{session}.view.json
                    │  结构化会话视图
                    ├─ Auto-grade (rules + LLM judge) → logs/{session}.grade.json
                    │  自动评分（规则 + LLM 评审）
                    ├─ Diagnose (10 rule-based checks + LLM summary) → logs/{session}.diagnose.json
                    │  行为诊断（10条规则 + LLM 自然语言总结）
                    ├─ Probe (LLM agent reviews agent source config) → logs/{session}.probe.json
                    │  探针审查（LLM agent 审查被评测 agent 的 prompt/skills/tools 配置）
                    └─ Web Dashboard → http://127.0.0.1:57633/dashboard/
                       Web 评测面板
```

## Screenshots / 界面展示

### Dashboard / 面板列表

![Dashboard](src/assets/dashboard.png)

### Grader / 评分详情

![Grader](src/assets/grader.png)

### Diagnosis / 诊断结果

![Diagnosis](src/assets/diagnosis.png)

### Probe / 探针审查

![Probe](src/assets/probe.png)

## Quick Start / 快速开始

### 1. Configure `.env` / 配置

```bash
# Upstream LLM API / 上游 LLM 地址
AGENTEVAL_UPSTREAM=https://api.edgefn.net

# Proxy port / 代理监听端口
AGENTEVAL_PORT=57633

# Log directory / 日志目录
AGENTEVAL_LOG_DIR=./logs

# Judge LLM for grading, diagnosis summary, and probing / 评测 LLM（评分+诊断总结+探针共用）
AGENTEVAL_JUDGE_API_BASE=https://api.deepseek.com
AGENTEVAL_JUDGE_MODEL=deepseek-chat
AGENTEVAL_JUDGE_API_KEY=sk-xxx

# Source project directory for probe / 被探针审查的 agent 项目路径
PROBE_SOURCE_PROJECT_DIR=/path/to/your/agent/project
```

### 2. Start the proxy / 启动代理

```bash
cargo run
# listening http://127.0.0.1:57633 -> https://api.edgefn.net
# dashboard http://127.0.0.1:57633/dashboard/
```

### 3. Configure your Agent / 配置 Agent

Point your Agent's `BASE_URL` to the proxy.

*将 Agent 的 `BASE_URL` 指向代理地址。*

```bash
# Claude Code
export ANTHROPIC_BASE_URL=http://127.0.0.1:57633

# OpenAI SDK
export OPENAI_BASE_URL=http://127.0.0.1:57633/v1

# Generic
MODEL_BASE_URL=http://127.0.0.1:57633/v1 your-agent-command
```

### 4. View results / 查看结果

Open **http://127.0.0.1:57633/dashboard/** in your browser.

*浏览器打开上述地址查看评测面板。*

## Web Dashboard / Web 面板

### Session List / 会话列表

| Feature | Description |
|---------|-------------|
| Filter bar / 过滤 | 全部 / <6分 / 6-8分 / >8分，默认低分优先 |
| Pagination / 分页 | 超过 10 条自动分页，智能页码导航 |
| Score columns / 评分列 | Overall score + 4 dimension mini-bars / 总分 + 四维迷你进度条 |
| Grade button / 评分按钮 | Ungraded sessions show inline `[Grade]` button / 未评分会话可直接触發 |
| Diagnose badge / 诊断标记 | `⚠ N issues` / `✓ clean` / `[Diagnose]` button |
| Probe badge / 探针标记 | `🔍 N findings` / `✓ no findings` / `[Probe]` button |

### Detail View / 详情页

| Section | Description |
|---------|-------------|
| Grade / 评分 | Large overall score + 4 dimension cards with LLM judge reasons |
| Diagnose / 诊断 | **AI Summary** (LLM natural-language summary at top) + issue list (severity + category + detail + evidence) |
| Probe / 探针 | **AI Summary** (LLM overall assessment at top) + findings list (confidence + root cause + recommendation + evidence) |
| Conversation / 对话 | Expandable turns: user input + reasoning + text + tool calls + results |
| Scroll anchor / 锚点跳转 | Clicking diagnose/probe badge from list auto-scrolls to that panel |

## CLI / 命令行

```bash
# Run diagnosis on a session / 对某个 session 运行诊断
cargo run -- diagnose <session_id> [--format terminal|json]

# Run probe on a session (requires prior diagnosis) / 对某个 session 运行探针
cargo run -- probe <session_id>
```

## Session Splitting / Session 自动切分

| Trigger / 触发条件 | Behavior / 行为 |
|---|---|
| New conversation (message array rollback) / 用户开新对话 | Seal old session → background grade → start new session |
| 2-minute idle timeout / 2 分钟无新请求 | Same as above |
| Proxy shutdown / 进程退出 | Flush last session (synchronous grade) |

**Detection logic:** Normal conversations grow messages turn-by-turn. A new conversation "shrinks" back to just the system prompt + new question. When `common_prefix_len <= 1`, it's treated as a new session.

*正常对话 messages 逐轮增长，新对话 messages 会"回缩"。当 `common_prefix_len <= 1` 时判定为新 session。*

## Grading / 评分

Four weighted dimensions → overall 0–1 sc