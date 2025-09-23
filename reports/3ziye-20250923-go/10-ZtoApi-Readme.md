# OpenAI兼容API代理 for Z.ai GLM-4.5

这是一个为Z.ai GLM-4.5模型提供OpenAI兼容API接口的代理服务器。它允许你使用标准的OpenAI API格式与Z.ai的GLM-4.5模型进行交互，支持流式和非流式响应。

> **注意**: 本项目来自fork  [OpenAI-Compatible-API-Proxy-for-Z](https://github.com/kbykb/OpenAI-Compatible-API-Proxy-for-Z)二次开发


## ✨ 主要功能

- 🔄 **OpenAI API兼容**: 完全兼容OpenAI的API格式，无需修改客户端代码
- 🌊 **流式响应支持**: 支持实时流式输出，提供更好的用户体验
- 🔐 **身份验证**: 支持API密钥验证，确保服务安全
- 🛠️ **灵活配置**: 通过环境变量进行灵活配置
- 🐳 **Docker支持**: 提供Docker镜像，便于部署
- 🌍 **CORS支持**: 支持跨域请求，便于前端集成
- 📝 **思考过程展示**: 智能处理并展示模型的思考过程
- 📊 **实时监控仪表板**: 提供Web仪表板，实时显示API转发情况和统计信息

## 🚀 快速开始

### 环境要求

- Go 1.23 或更高版本
- Z.ai 的访问令牌

### 本地部署

1. **克隆仓库**
   ```bash
   git clone https://github.com/your-username/ZtoApi.git
   cd ZtoApi
   ```

2. **配置环境变量**
   ```bash
   cp config.env .env.local
   # 编辑 .env.local 文件，设置你的 ZAI_TOKEN
   ```

3. **启动服务**
   ```bash
   # 使用启动脚本（推荐）
   ./start.sh
   
   # 或直接运行
   go run main.go
   ```

4. **测试服务**
    ```bash
    curl http://localhost:9090/v1/models
    ```

5. **访问API文档**

   启动服务后，可以通过浏览器访问以下地址查看完整的API文档：
    ```
    http://localhost:9090/docs
    ```

   API文档提供了以下功能：
    - 详细的API端点说明
    - 请求参数和响应格式
    - 多种编程语言的使用示例（Python、cURL、JavaScript）
    - 错误处理说明

5. **访问Dashboard**

   启动服务后，可以通过浏览器访问以下地址查看实时监控仪表板：
   ```
   http://localhost:9090/dashboard
   ```

   Dashboard提供了以下功能：
    - 实时显示API请求统计信息（总请求数、成功请求数、失败请求数、平均响应时间）
    - 显示最近100条请求的详细信息（时间、方法、路径、状态码、耗时、客户端IP）
    - 数据每5秒自动刷新一次

### Docker部署

1. **构建镜像**
   ```bash
   docker build -t zto-api .
   ```

2. **运行容器**
   ```bash
   docker run -p 9090:9090 \
     -e ZAI_TOKEN=your_z_ai_token \
     -e DEFAULT_KEY=your_api_key \
     zto-api
   ```

## Render部署

1. Fork这个仓库到你的GitHub账户

2. 在Render上创建新的Web Service：
    - 连接你的GitHub仓库
    - 选择Docker作为环境
    - 设置以下环境变量：
    - `ZAI_TOKEN`: Z.ai 的访问令牌 (可选，不提供将自动获取随机匿名token)
    - `DEFAULT_KEY`: 客户端API密钥 (可选，默认: sk-your-key)
    - `MODEL_NAME`: 显示的模型名称 (可选，默认: GLM-4.5)
    - `PORT`: 服务监听端口 (Render会自动设置)

3. 部署完成后，使用Render提供的URL作为OpenAI API的base_url

## ⚙️ 环境变量配置

本项目支持通过环境变量进行配置，提供灵活的部署和运行选项。

### 🚀 快速开始

#### 1. 使用启动脚本（推荐）

**macOS/Linux:**
```bash
./start.sh
```

**Windows:**
```cmd
start.bat
```

#### 2. 手动设置环境变量

**macOS/Linux:**
```bash
export ZAI_TOKEN="your_z_ai_token_here"
export DEFAULT_KEY="sk-your-custom-key"
export PORT="9090"
go run main.go
```

**Windows:**
```cmd
set ZAI_TOKEN=your_z_ai_token_here
set DEFAULT_KEY=sk-your-custom-key
set PORT=9090
go run main.go
```

#### 3. Docker运行

```bash
docker run -p 9090:9090 \
  -e ZAI_TOKEN=your_z_ai_token_here \
  -e DEFAULT_KEY=sk-your-custom-key \
  -e PORT=9090 \
  zto-api
```

### 📋 环境变量列表

#### 🔑 必需配置

无必需配置。所有配置都有合理的默认值。

#### ⚙️ 可选配置

| 变量名 | 说明 | 默认值 | 示例 |
|--------|------|--------|------|
| `ZAI_TOKEN` | Z.ai 访问令牌 | 空（自动获取随机匿名token） | `eyJhbGciOiJFUzI1NiIs...` |

#### ⚙️ 可选配置

| 变量名 | 说明 | 默认值 | 示例 |
|--------|------|--------|------|
| `DEFAULT_KEY` | 客户端API密钥 | `sk-your-key` | `sk-my-api-key` |
| `MODEL_NAME` | 显示模型名称 | `GLM-4.5` | `GLM-4.5-Pro` |
| `PORT` | 服务监听端口 | `9090` | `9000` |
| `DEBUG_MODE` | 调试模式开关 | `true` | `false` |
| `DEFAULT_STREAM` | 默认流式响应 | `true` | `false` |
| `DASHBOARD_ENABLED` | Dashboard功能开关 | `true` | `false` |
| `ENABLE_THINKING` | 思考功能开关 | `false` | `true` |

#### 🔧 高级配置

| 变量名 | 说明 | 默认值 | 示例 |
|--------|------|--------|------|
| `UPSTREAM_URL` | 上游API地址 | `https://chat.z.ai/api/chat/completions` | 自定义URL |

### 📁 配置文件

#### 支持的配置文件（按优先级排序）

1. `.env.local` - 本地环境配置（推荐）
2. `.env` - 环境配置
3. `config.env` - 配置模板

#### 配置文件示例

```bash
# 复制配置文件
cp config.env .env.local

# 编辑配置文件
nano .env.local
```

### 🔐 获取 Z.ai Token

#### 方法1：浏览器开发者工具

1. 登录 [Z.ai](https://chat.z.ai)
2. 打开浏览器开发者工具（F12）
3. 切换到 Network 标签页
4. 发送一条消息
5. 在请求中找到 `Authorization` 头部的 Bearer token

#### 方法2：Cookie 方式

1. 登录 Z.ai 后，在开发者工具中查看 Cookies
2. 找到包含认证信息的 cookie

#### 方法3：匿名Token

本项目支持自动获取匿名token，无需手动配置。当 `ZAI_TOKEN` 环境变量未设置时，系统会自动为每次对话获取不同的随机匿名token，避免共享记忆。这种机制使得项目即使用户没有提供 Z.ai 的访问令牌也能正常工作。

### 🎯 使用示例

#### 基本配置

```bash
# .env.local
ZAI_TOKEN=eyJhbGciOiJFUzI1NiIs...
DEFAULT_KEY=sk-my-secret-key
MODEL_NAME=GLM-4.5-Pro
PORT=9000
DEBUG_MODE=false
```

#### 生产环境配置

```bash
# .env.production
ZAI_TOKEN=your_production_token
DEFAULT_KEY=sk-production-key
MODEL_NAME=GLM-4.5
PORT=9090
DEBUG_MODE=false
DEFAULT_STREAM=true
```

#### 开发环境配置

```bash
# .env.development
ZAI_TOKEN=your_dev_token
DEFAULT_KEY=sk-dev-key
MODEL_NAME=GLM-4.5-Dev
PORT=8080
DEBUG_MODE=true
DEFAULT_STREAM=true
DASHBOARD_ENABLED=true
```

### 📊 Dashboard功能

本项目提供了一个Web仪表板，用于实时监控API转发情况和统计信息。

#### 功能特点

- 实时显示API请求统计信息（总请求数、成功请求数、失败请求数、平均响应时间）
- 显示最近100条请求的详细信息（时间、方法、路径、状态码、耗时、客户端IP）
- 数据每5秒自动刷新一次
- 响应式设计，支持各种设备访问

#### 访问方式

启动服务后，通过浏览器访问以下地址：
```
http://localhost:9090/dashboard
```

#### 配置选项

通过 `DASHBOARD_ENABLED` 环境变量控制Dashboard功能的开启和关闭：

```bash
# 启用Dashboard（默认）
DASHBOARD_ENABLED=true

# 禁用Dashboard
DASHBOARD_ENABLED=false
```

#### 使用场景

- **开发调试**: 实时查看API请求情况，便于调试和问题排查
- **性能监控**: 监控API响应时间和成功率，评估系统性能
- **安全审计**: 查看请求来源和频率，发现异常访问模式

### 🔄 重启服务

修改环境变量后，需要重启服务使配置生效：

```bash
# 停止当前服务
