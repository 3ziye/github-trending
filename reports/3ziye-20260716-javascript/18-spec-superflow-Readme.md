<h1 align="center">spec-superflow</h1>

<p align="center">
  <strong>源码级融合 OpenSpec 规划引擎 + Superpowers 执行纪律的 AI 编程工作流插件</strong>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT License"></a>
  <a href="https://github.com/MageByte-Zero/spec-superflow/stargazers"><img src="https://img.shields.io/github/stars/MageByte-Zero/spec-superflow" alt="GitHub Stars"></a>
  <a href="https://www.npmjs.com/package/spec-superflow"><img src="https://img.shields.io/npm/v/spec-superflow" alt="npm version"></a>
</p>

<p align="center">
  <a href="#快速开始">快速开始</a> |
  <a href="#安装">安装</a> |
  <a href="#为什么需要它">为什么</a> |
  <a href="#核心-skills">Skills</a> |
  <a href="#工作流">工作流</a> |
  <a href="docs/README_en.md">English</a> |
  <a href="docs/showcase.html">Showcase</a> |
  <a href="#常见问题">FAQ</a>
</p>

---

## 快速开始

安装后，告诉 Agent 一句话即可启动：

```
用 workflow-start 开始
```

Agent 会自动检查当前工件目录，**内容级判断**（不看文件时间戳，而是比较 proposal 范围 vs 契约意图锁）你处于哪个阶段，然后路由到正确的下一个 skill。

- 启动新的变更 → `用 workflow-start 开始`
- 恢复旧的变更 → `继续上次的工作流`
- 不确定当前状态 → `帮我看看现在该干什么`

## 安装

### Claude Code（Marketplace）

Claude Code 的主流方式是插件 marketplace：

```bash
/plugin marketplace add MageByte-Zero/spec-superflow
/plugin install spec-superflow@spec-superflow
/plugin update spec-superflow@spec-superflow
```

Marketplace 安装自动加载 hooks，每次新会话自动注入上下文。

### Cursor（Skills 目录 / GitHub 导入）

```bash
# 方式一：通过 ssf CLI
npx spec-superflow@latest install-cursor

# 方式二：直接运行脚本
curl -fsSL https://raw.githubusercontent.com/MageByte-Zero/spec-superflow/main/scripts/install-cursor.mjs | node -
```

> Cursor 原生发现 `.cursor/skills/`、`.agents/skills/`、`~/.cursor/skills/` 等目录，也可以在 Customize → Rules → Remote Rule (Github) 导入。脚本会自动部署 skills、scripts、docs 等运行时依赖。

### OpenAI Codex CLI / App

Codex 的主流方式是 Plugin Directory / marketplace。本仓库已提供 `.codex-plugin/plugin.json` 和 `.agents/plugins/marketplace.json`。

```bash
# 在 Codex CLI 中打开插件目录
codex
/plugins

# 或添加社区 marketplace 后安装
codex plugin marketplace add hashgraph-online/awesome-codex-plugins
codex plugin add spec-superflow@awesome-codex-plugins

# 直接从指定 release tag 安装（不等待社区镜像同步）
codex plugin marketplace add MageByte-Zero/spec-superflow --ref v0.9.0
codex plugin add spec-superflow@spec-superflow

# 升级并验证社区 marketplace 安装
codex plugin marketplace upgrade awesome-codex-plugins
codex plugin add spec-superflow@awesome-codex-plugins
codex plugin list | rg spec-superflow
```

Codex App 打开 **Plugins** 面板，安装或启用 `spec-superflow`。通过 CLI 安装或升级后，重启 Codex App 并新开会话；旧会话不会热加载 skills。

### GitHub Copilot CLI

```bash
copilot plugin marketplace add MageByte-Zero/spec-superflow
copilot plugin install spec-superflow@spec-superflow
```

### Gemini CLI

```bash
gemini extensions install https://github.com/MageByte-Zero/spec-superflow
gemini extensions update spec-superflow   # 升级
```

### 更多平台（Cline / Kiro / Windsurf / Qwen / Amazon Q / Roo Code / Continue / Pi / OpenCode / WorkBuddy / Trae）

| 平台 | 安装方式 | 状态 |
|------|---------|------|
| **Cline** | `npx spec-superflow@latest install-cline` | 已提供安装器 |
| **Kiro** | `npx spec-superflow@latest install-kiro` | 已提供安装器 |
| **Windsurf** | `npx spec-superflow@latest install-windsurf` | 已提供安装器 |
| **Qwen Code** | `npx spec-superflow@latest install-qwen` | 已提供安装器 |
| **Amazon Q Developer** | `npx spec-superflow@latest install-amazon-q` | 已提供安装器 |
| **Roo Code** | `npx spec-superflow@latest install-roocode` | 已提供安装器 |
| **Continue** | `npx spec-superflow@latest install-continue` | 已提供安装器 |
| **Pi** | `npx spec-superflow@latest install-pi` | 已提供安装器 |
| **OpenCode** | `.opencode/plugins/spec-superflow.js` 或 `.agents/skills -> skills/` | 已提供入口 |
| **WorkBuddy** | `npx spec-superflow@latest install-workbuddy` | 已提供安装器 |
| **Trae IDE / TRAE Work** | `.trae/skills/`、`~/.trae/skills/` 或上传 zip/.skill | 手动/导入 |

> 共支持 17 个平台，完整安装说明见 [INSTALL.md](INSTALL.md)，支持矩阵见 [docs/platform-matrix.md](docs/platform-matrix.md)。

### CLI 工具链

```bash
npm install -g spec-superflow    # 全局安装
npx spec-superflow list          # 或通过 npx 使用
```

| 命令 | 功能 |
|------|------|
| `ssf list` | 列出所有 changes 及状态 |
| `ssf validate <dir>` | 验证工件完整性 |
| `ssf doctor` | 健康检查（版本、hooks、skills、文档一致性） |
| `ssf version <semver>` | 一键同步版本号到所有 manifest |
| `ssf state <sub> <dir>` | 管理 `.spec-superflow.yaml` 状态文件 |
| `ssf inject <dir>` | 生成 phase-guard 产物；仅在检测到单一平台标记时可省略 `--platforms` |
| `ssf audit <dir>` | 生成决策点审计报告 |
| `ssf checkpoint save <dir> --task <id> --next <text>` | 保存任务级会话恢复点 |
| `ssf checkpoint list <dir>` | 列出 checkpoint 及 stale 状态 |
| `ssf checkpoint show <dir> <id>` | 查看单个恢复点 |
| `ssf handoff create <dir> --type <type> ...` | 创建 prototype/research/experiment handoff |
| `ssf handoff list <dir>` | 列出 handoff 生命周期状态 |
| `ssf handoff finish <dir> <id>` | 校验 handoff 结果 |
| `ssf handoff resolve <dir> <id> --decision <decision>` | 记录显式 handoff 决策 |
| `ssf execution recommend <dir> ...` | 基于任务量、wave 和工作流列出可用执行方式并给出推荐 |
| `ssf execution plan <dir> ...` | 在用户确认选择后，为 full/hotfix 保存受 guard 保护的执行计划 |
| `ssf execution s