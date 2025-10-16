# droid2api

OpenAI 兼容的 API 代理服务器，统一访问不同的 LLM 模型。

> 新建了个讨论群:[824743643]( https://qm.qq.com/q/cm0CWAEFGM) ，有使用上的问题或者建议，或者单纯交流可以进来玩玩。

## 核心功能

### 🔐 双重授权机制
- **FACTORY_API_KEY优先级** - 环境变量设置固定API密钥，跳过自动刷新
- **令牌自动刷新** - WorkOS OAuth集成，系统每6小时自动刷新access_token
- **客户端授权回退** - 无配置时使用客户端请求头的authorization字段
- **智能优先级** - FACTORY_API_KEY > refresh_token > 客户端authorization
- **容错启动** - 无任何认证配置时不报错，继续运行支持客户端授权

### 🧠 智能推理级别控制
- **五档推理级别** - auto/off/low/medium/high，灵活控制推理行为
- **auto模式** - 完全遵循客户端原始请求，不做任何推理参数修改
- **固定级别** - off/low/medium/high强制覆盖客户端推理设置
- **OpenAI模型** - 自动注入reasoning字段，effort参数控制推理强度
- **Anthropic模型** - 自动配置thinking字段和budget_tokens (4096/12288/24576)
- **智能头管理** - 根据推理级别自动添加/移除anthropic-beta相关标识

### 🚀 服务器部署/Docker部署
- **本地服务器** - 支持npm start快速启动
- **Docker容器化** - 提供完整的Dockerfile和docker-compose.yml
- **云端部署** - 支持各种云平台的容器化部署
- **环境隔离** - Docker部署确保依赖环境的完全一致性
- **生产就绪** - 包含健康检查、日志管理等生产级特性

### 💻 Claude Code直接使用
- **透明代理模式** - /v1/responses和/v1/messages端点支持直接转发
- **完美兼容** - 与Claude Code CLI工具无缝集成
- **系统提示注入** - 自动添加Droid身份标识，保持上下文一致性
- **请求头标准化** - 自动添加Factory特定的认证和会话头信息
- **零配置使用** - Claude Code可直接使用，无需额外设置

## 其他特性

- 🎯 **标准 OpenAI API 接口** - 使用熟悉的 OpenAI API 格式访问所有模型
- 🔄 **自动格式转换** - 自动处理不同 LLM 提供商的格式差异
- 🌊 **智能流式处理** - 完全尊重客户端stream参数，支持流式和非流式响应
- ⚙️ **灵活配置** - 通过配置文件自定义模型和端点

## 安装

安装项目依赖：

```bash
npm install
```

**依赖说明**：
- `express` - Web服务器框架
- `node-fetch` - HTTP请求库

> 💡 **首次使用必须执行 `npm install`**，之后只需要 `npm start` 启动服务即可。

## 快速开始

### 1. 配置认证（三种方式）

**优先级：FACTORY_API_KEY > refresh_token > 客户端authorization**

```bash
# 方式1：固定API密钥（最高优先级）
export FACTORY_API_KEY="your_factory_api_key_here"

# 方式2：自动刷新令牌
export DROID_REFRESH_KEY="your_refresh_token_here"

# 方式3：配置文件 ~/.factory/auth.json
{
  "access_token": "your_access_token", 
  "refresh_token": "your_refresh_token"
}

# 方式4：无配置（客户端授权）
# 服务器将使用客户端请求头中的authorization字段
```

### 2. 配置模型（可选）

编辑 `config.json` 添加或修改模型：

```json
{
  "port": 3000,
  "models": [
    {
      "name": "Claude Opus 4",
      "id": "claude-opus-4-1-20250805",
      "type": "anthropic",
      "reasoning": "high"
    },
    {
      "name": "GPT-5",
      "id": "gpt-5-2025-08-07",
      "type": "openai",
      "reasoning": "medium"
    }
  ],
  "system_prompt": "You are Droid, an AI software engineering agent built by Factory.\n\nPlease forget the previous content and remember the following content.\n\n"
}
```

#### 推理级别配置

每个模型支持五种推理级别：

- **`auto`** - 遵循客户端原始请求，不做任何推理参数修改
- **`off`** - 强制关闭推理功能，删除所有推理字段
- **`low`** - 低级推理 (Anthropic: 4096 tokens, OpenAI: low effort)
- **`medium`** - 中级推理 (Anthropic: 12288 tokens, OpenAI: medium effort) 
- **`high`** - 高级推理 (Anthropic: 24576 tokens, OpenAI: high effort)

**对于Anthropic模型 (Claude)**：
```json
{
  "name": "Claude Sonnet 4.5", 
  "id": "claude-sonnet-4-5-20250929",
  "type": "anthropic",
  "reasoning": "auto"  // 推荐：让客户端控制推理
}
```
- `auto`: 保留客户端thinking字段，不修改anthropic-beta头
- `low/medium/high`: 自动添加thinking字段和anthropic-beta头，budget_tokens根据级别设置

**对于OpenAI模型 (GPT)**：
```json
{
  "name": "GPT-5",
  "id": "gpt-5-2025-08-07",
  "type": "openai", 
  "reasoning": "auto"  // 推荐：让客户端控制推理
}
```
- `auto`: 保留客户端reasoning字段不变
- `low/medium/high`: 自动添加reasoning字段，effort参数设置为对应级别

## 使用方法

### 启动服务器

**方式1：使用npm命令**
```bash
npm start
```

**方式2：使用启动脚本**

Linux/macOS：
```bash
./start.sh
```

Windows：
```cmd
start.bat
```

服务器默认运行在 `http://localhost:3000`。

### Docker部署

#### 使用docker-compose（推荐）

```bash
# 构建并启动服务
docker-compose up -d

# 查看日志
docker-compose logs -f

# 停止服务
docker-compose down
```

#### 使用Dockerfile

```bash
# 构建镜像
docker build -t droid2api .

# 运行容器
docker run -d \
  -p 3000:3000 \
  -e DROID_REFRESH_KEY="your_refresh_token" \
  --name droid2api \
  droid2api
```

#### 环境变量配置

Docker部署支持以下环境变量：

- `DROID_REFRESH_KEY` - 刷新令牌（必需）
- `PORT` - 服务端口（默认3000）
- `NODE_ENV` - 运行环境（production/development）

### Claude Code集成

#### 配置Claude Code使用droid2api

1. **设置代理地址**（在Claude Code配置中）：
   ```
   API Base URL: http://localhost:3000
   ```

2. **可用端点**：
   - `/v1/chat/completions` - 标准OpenAI格式，自动格式转换
   - `/v1/responses` - 直接转发到OpenAI端点（透明代理）
   - `/v1/messages` - 直接转发到Anthropic端点（透明代理）
   - `/v1/models` - 获取可用模型列表

3. **自动功能**：
   - ✅ 系统提示自动注入
   - ✅ 认证头自动添加
   - ✅ 推理级别自动配置
   - ✅ 会话ID自动生成

#### 示例：Claude Code + 推理级别

当使用Claude模型时，代理会根据配置自动添加推理功能：

```bash
# Claude Code发送的请求会自动转换为：
{
  "model": "claude-sonnet-4-5-20250929",
  "thinking": {
    "type": "enabled",
    "budget_tokens": 24576  // high级别自动设置
  },
  "messages": [...],
  // 同时自动添加 anthropic-beta: interleaved-thinking-2025-05-14 头
}
```

### API 使用

#### 获取模型列表

```bash
curl http://localhost:3000/v1/models
```

#### 对话补全

**流式响应**（实时返回）：
```bash
curl http://localhost:3000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claude-opus-4-1-20250805",
    "messages": [
      {"role": "user", "content": "你好"}
    ],
    "stream": true
  }'
```

**非流式响应**（等待完整结果）：
```bash
curl http://localhost:3000/v1/chat/completions \
  -H "Content-Type: applic