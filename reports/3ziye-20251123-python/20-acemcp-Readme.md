[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/qy527145-acemcp-badge.png)](https://mseep.ai/app/qy527145-acemcp)

简体中文 | [English](./README_EN.md)

# Acemcp

代码库索引和语义搜索的 MCP 服务器。

<a href="https://glama.ai/mcp/servers/@qy527145/acemcp">
  <img width="380" height="200" src="https://glama.ai/mcp/servers/@qy527145/acemcp/badge" alt="Acemcp MCP server" />
</a>

## 安装

### 作为工具安装（推荐）

```bash
# 安装到系统
uv tool install acemcp

# 或临时运行（无需安装）
uvx acemcp
```

### 开发安装

```bash
# 克隆仓库
git clone https://github.com/qy527145/acemcp.git
cd acemcp

# 安装依赖
uv sync

# 运行
uv run acemcp
```

## 配置

配置文件会在首次运行时自动创建在 `~/.acemcp/settings.toml`，包含默认值。

编辑 `~/.acemcp/settings.toml` 进行配置：
```toml
BATCH_SIZE = 10
MAX_LINES_PER_BLOB = 800
BASE_URL = "https://your-api-endpoint.com"
TOKEN = "your-bearer-token-here"
TEXT_EXTENSIONS = [".py", ".js", ".ts", ...]
EXCLUDE_PATTERNS = [".venv", "node_modules", ".git", "__pycache__", "*.pyc", ...]
```

**配置选项：**
- `BATCH_SIZE`: 每批上传的文件数量（默认：10）
- `MAX_LINES_PER_BLOB`: 大文件分割前的最大行数（默认：800）
- `BASE_URL`: API 端点 URL
- `TOKEN`: 认证令牌
- `TEXT_EXTENSIONS`: 要索引的文件扩展名列表
- `EXCLUDE_PATTERNS`: 要排除的模式列表（支持通配符如 `*.pyc`）

您还可以通过以下方式配置：
- **命令行参数**（最高优先级）：`--base-url`、`--token`
- **Web 管理界面**（更新用户配置文件）
- **环境变量**（使用 `ACEMCP_` 前缀）

## MCP 配置

将以下内容添加到您的 MCP 客户端配置中（例如 Claude Desktop）：

### 基础配置

```json
{
  "mcpServers": {
    "acemcp": {
      "command": "uvx",
      "args": [
        "acemcp"
      ]
    }
  }
}
```


**可用的命令行参数：**
- `--base-url`: 覆盖 BASE_URL 配置
- `--token`: 覆盖 TOKEN 配置
- `--web-port`: 在指定端口启用 Web 管理界面（例如 8080）

### 启用 Web 管理界面的配置

要启用 Web 管理界面，添加 `--web-port` 参数：

```json
{
  "mcpServers": {
    "acemcp": {
      "command": "uvx",
      "args": [
        "acemcp",
        "--web-port",
        "8888"
      ]
    }
  }
}
```

然后访问管理界面：`http://localhost:8888`

**Web 管理功能：**
- **配置管理**：查看和编辑服务器配置（BASE_URL、TOKEN、BATCH_SIZE、MAX_LINES_PER_BLOB、TEXT_EXTENSIONS）
- **实时日志**：通过 WebSocket 连接实时监控服务器日志，具有智能重连功能
  - 指数退避重连策略（1秒 → 1.5秒 → 2.25秒 ... 最大 30秒）
  - 最多 10 次重连尝试，防止无限循环
  - 网络故障时自动重连
  - 减少日志噪音（WebSocket 连接记录在 DEBUG 级别）
- **工具调试器**：直接从 Web 界面测试和调试 MCP 工具
  - 测试 `search_context` 工具，输入项目路径和查询
  - 查看格式化的结果和错误消息

## 工具

### search_context

基于查询搜索相关的代码上下文。此工具在搜索前**自动执行增量索引**，确保结果始终是最新的。它在您的代码库中执行**语义搜索**，并返回格式化的文本片段，显示相关代码的位置。

**核心特性：**
- **自动增量索引**：每次搜索前，工具自动仅索引新文件或修改过的文件，跳过未更改的文件以提高效率
- **无需手动索引**：您无需手动索引项目 - 只需搜索，工具会自动处理索引
- **始终保持最新**：搜索结果反映代码库的当前状态
- **多编码支持**：自动检测和处理多种文件编码（UTF-8、GBK、GB2312、Latin-1）
- **.gitignore 集成**：索引项目时自动遵守 `.gitignore` 模式

**参数：**
- `project_root_path`（字符串）：项目根目录的绝对路径
  - **重要**：即使在 Windows 上也使用正斜杠（`/`）作为路径分隔符
  - Windows 示例：`C:/Users/username/projects/myproject`
  - Linux/Mac 示例：`/home/username/projects/myproject`
- `query`（字符串）：用于查找相关代码上下文的自然语言搜索查询
  - 使用与您要查找的内容相关的描述性关键词
  - 工具执行语义匹配，而不仅仅是关键词搜索
  - 返回带有文件路径和行号的代码片段

**返回内容：**
- 与您的查询匹配的文件中的格式化文本片段
- 每个片段的文件路径和行号
- 相关代码部分周围的上下文
- 按相关性排序的多个结果

**查询示例：**

1. **查找配置代码：**
   ```json
   {
     "project_root_path": "C:/Users/username/projects/myproject",
     "query": "日志配置 设置 初始化 logger"
   }
   ```
   返回：与日志设置、logger 初始化和配置相关的代码

2. **查找认证逻辑：**
   ```json
   {
     "project_root_path": "C:/Users/username/projects/myproject",
     "query": "用户认证 登录 密码验证"
   }
   ```
   返回：认证处理器、登录函数、密码验证代码

3. **查找数据库代码：**
   ```json
   {
     "project_root_path": "C:/Users/username/projects/myproject",
     "query": "数据库连接池 初始化"
   }
   ```
   返回：数据库连接设置、连接池配置、初始化代码

4. **查找错误处理：**
   ```json
   {
     "project_root_path": "C:/Users/username/projects/myproject",
     "query": "错误处理 异常 try catch"
   }
   ```
   返回：错误处理模式、异常处理器、try-catch 块

5. **查找 API 端点：**
   ```json
   {
     "project_root_path": "C:/Users/username/projects/myproject",
     "query": "API 端点 路由 HTTP 处理器"
   }
   ```
   返回：API 路由定义、HTTP 处理器、端点实现

**获得更好结果的技巧：**
- 使用多个相关关键词（例如，"日志配置设置"而不仅仅是"日志"）
- 包含您要查找的特定技术术语
- 描述功能而不是确切的变量名
- 如果第一次查询没有返回您需要的内容，尝试不同的措辞

**索引特性：**
- **增量索引**：仅上传新文件或修改过的文件，跳过未更改的文件
- **基于哈希的去重**：通过路径 + 内容的 SHA-256 哈希识别文件
- **自动重试**：网络请求自动重试最多 3 次，采用指数退避（1秒、2秒、4秒）
- **批次弹性**：如果批次上传在重试后失败，工具会继续处理下一批次
- **文件分割**：大文件自动分割为多个块（默认：每块 800 行）
- **排除模式**：自动跳过虚拟环境、node_modules、.git、构建产物等
- **多编码支持**：自动检测文件编码（UTF-8、GBK、GB2312、Latin-1），并在失败时回退到 UTF-8 错误处理
- **.gitignore 集成**：自动从项目根目录加载并遵守 `.gitignore` 模式，与配置的排除模式结合使用

**搜索特性：**
- **自动重试**：搜索请求自动重试最多 3 次，采用指数退避（2秒、4秒、8秒）
- **优雅降级**：如果所有重试后搜索失败，返回清晰的错误消息
- **超时处理**：使用 60 秒超时来处理长时间运行的搜索
- **空结果处理**：如果未找到相关代码，返回有用的消息

**默认排除模式：**
```
.venv, venv, .env, env, node_modules, .git, .svn, .hg, __pycache__,
.pytest_cache, .mypy_cache, .tox, .eggs, *.egg-info, dist, build,
.idea, .vscode, .DS_Store, *.pyc, *.pyo, *.pyd, .Python,
pip-log.txt, pip-delete-this-directory.txt, .coverage, htmlcov,
.gradle, target, bin, obj
```
模式支持通配符（`*`、`?`），并匹配目录/文件名或路径。

**注意：** 如果项目根目录存在 `.gitignore` 文件，其模式将自动加载并与配置的排除模式结合使用。`.gitignore` 模式遵循 Git 的标准 wildmatch 语法。

## 高级特性

### 多编码文件支持

Acemcp 自动检测和处理不同字符编码的文件，适用于国际化项目：

- **自动检测**：按顺序尝试多种编码：UTF-8 → GBK → GB2312 → Latin-1
- **回退处理**：如果所有编码都失败，使用 UTF-8 错误处理以防止崩溃
- **日志记录**：记录每个文件成功使用的编码（DEBUG 级