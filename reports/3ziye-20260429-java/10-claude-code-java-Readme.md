# Claude Code Java

<p align="center">
  <img src="https://img.shields.io/badge/Java-21+-ED8B00?style=flat-square&logo=openjdk&logoColor=white" alt="Java">
  <img src="https://img.shields.io/badge/Maven-3.9+-C71A36?style=flat-square&logo=apache-maven&logoColor=white" alt="Maven">
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="License">
</p>

> Claude Code 的 Java 版本实现，一比一复刻自 TypeScript/Bun 技术栈

## 项目概述

Claude Code Java 是 [Claude Code](https://docs.anthropic.com/zh-CN/docs/claude-code) 的纯 Java 实现，保持与原版功能完整性和行为一致性。该项目采用 Java 21 开发，充分利用现代 Java 特性（Virtual Threads、Records、Sealed Classes 等），通过 JLine3 构建终端 UI 层。

### 核心特性

- **完整的 AI 对话能力** — 与 Claude AI 进行多轮交互，支持工具调用、消息压缩、会话恢复
- **54 个内置工具** — 文件操作、Shell 命令、代码搜索、Web 访问、MCP 集成等
- **102 个斜杠命令** — 快速执行常用操作（commit、diff、review、compact 等）
- **MCP 协议支持** — 连接 MCP 服务器扩展 AI 能力
- **IDE 桥接** — 支持 VSCode、Neovim、JetBrains 等主流 IDE
- **LSP 集成** — Language Server Protocol 协议支持
- **终端 UI** — 完整的 Vim 模式、Markdown 渲染、代码高亮
- **会话持久化** — JSONL 格式，与 TypeScript 版本兼容

## 技术架构

```
┌─────────────────────────────────────────────────────────────┐
│                    claude-code-cli (Picocli)                │
│                      应用入口与 CLI 解析                      │
├─────────────────────────────────────────────────────────────┤
│                    claude-code-ui (JLine3)                  │
│           终端 UI：REPL、消息渲染、输入、Markdown              │
├──────────────────┬──────────────────┬───────────────────────┤
│  claude-code-    │  claude-code-    │  claude-code-         │
│  commands        │  tools           │  services             │
│  斜杠命令系统     │  工具系统         │  服务层                │
├──────────────────┴──────────────────┴───────────────────────┤
│                    claude-code-core                         │
│  QueryEngine │ Store │ Message │ Task │ Permission │ Config │
├──────────────────┬──────────────────┬───────────────────────┤
│  claude-code-api │  claude-code-mcp │  claude-code-bridge   │
│  Anthropic API   │  MCP 客户端       │  IDE 桥接             │
├──────────────────┴──────────────────┴───────────────────────┤
│  claude-code-session │ claude-code-permissions              │
│  会话持久化           │ 权限引擎                              │
├─────────────────────────────────────────────────────────────┤
│                    claude-code-utils                        │
│           通用工具：文件、Shell、Git、加密、格式化等            │
└─────────────────────────────────────────────────────────────┘
```

## 模块结构

| 模块 | 描述 | 文件数 |
|------|------|--------|
| `claude-code-utils` | 通用工具类：文件操作、Shell、Git、加密等 | ~50 |
| `claude-code-core` | 核心模型、QueryEngine、消息系统、状态管理 | ~80 |
| `claude-code-api` | Anthropic API 客户端（多 SDK 适配） | ~30 |
| `claude-code-permissions` | 权限系统（allow/deny/ask） | ~20 |
| `claude-code-tools` | 54 个内置工具实现 | ~150 |
| `claude-code-commands` | 102 个斜杠命令 | ~120 |
| `claude-code-mcp` | Model Context Protocol 集成 | ~50 |
| `claude-code-bridge` | IDE 桥接（VSCode、Neovim、JetBrains） | ~80 |
| `claude-code-session` | 会话管理（JSONL 持久化） | ~20 |
| `claude-code-services` | 服务层：compact、hooks、memory 等 | ~100 |
| `claude-code-ui` | 终端 UI：渲染器、对话框、菜单、Vim 模式 | ~200 |
| `claude-code-lsp` | Language Server Protocol 集成 | ~30 |
| `claude-code-cli` | CLI 入口（Picocli） | ~20 |
| `claude-code-app` | 应用打包与分发 | ~10 |

## 技术栈

| 类别 | 技术 |
|------|------|
| 语言 | Java 21+ (Records, Sealed Classes, Pattern Matching, Virtual Threads) |
| 构建 | Maven 3.9+ |
| JSON | Jackson 2.17.2 |
| 终端 UI | JLine3 3.26.3 |
| CLI | Picocli 4.7.6 |
| Markdown | commonmark-java 0.22.0 |
| 日志 | SLF4J 2.0.13 + Logback 1.5.8 |
| 工具库 | Guava 33.2.1, Commons Lang3 3.14.0, Commons IO 2.16.1 |
| LSP | Eclipse LSP4J 0.24.0 |
| 测试 | JUnit 5.10.3, jqwik 1.9.0 (属性测试) |

## 快速开始

### 环境要求

- **Java**: 21 或更高版本
- **Maven**: 3.9 或更高版本
- **API Key**: Anthropic API Key（设置 `ANTHROPIC_API_KEY` 环境变量）

### 安装 Java 21（如果需要）

```bash
# macOS with SDKMAN
sdk install java 21.0.2-tem

# Ubuntu/Debian
sudo apt install openjdk-21-jdk

# Windows (Chocolatey)
choco install openjdk21
```

### 构建项目

```bash
# 克隆项目
git clone https://github.com/your-username/claude-code-java.git
cd claude-code-java

# 全量构建
mvn clean install

# 跳过测试快速构建
mvn clean install -DskipTests

# 单模块构建
mvn -pl claude-code-core clean install
```

### 运行应用

```bash
# 使用 Maven 运行
mvn -pl claude-code-cli exec:java

# 或者运行打包后的 JAR
java -jar claude-code-app/target/claude-code-java-*-jar-with-dependencies.jar
```

### Docker 运行

```bash
# 构建镜像
docker build -t claude-code-java .

# 运行容器
docker run -it \
  -e ANTHROPIC_API_KEY=$ANTHROPIC_API_KEY \
  -v $(pwd):/workspace \
  claude-code-java
```

## 配置

### 环境变量

| 变量 | 描述 | 必需 |
|------|------|------|
| `ANTHROPIC_API_KEY` | Anthropic API 密钥 | 是 |
| `ANTHROPIC_BASE_URL` | API 基础 URL（可选，用于代理） | 否 |
| `CLAUDE_CONFIG_DIR` | 配置目录（默认 `~/.claude`） | 否 |

### 配置文件

```json
// ~/.claude/settings.json
{
  "model": "claude-sonnet-4",
  "maxTokens": 8192,
  "permissionMode": "ask",
  "disableBrowserTools": false
}
```

### 项目级配置

在项目根目录创建 `CLAUDE.md` 文件，