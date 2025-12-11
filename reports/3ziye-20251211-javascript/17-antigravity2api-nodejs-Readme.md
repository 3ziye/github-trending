# Antigravity to OpenAI API 代理服务

将 Google Antigravity API 转换为 OpenAI 兼容格式的代理服务，支持流式响应、工具调用和多账号管理。

## 功能特性

- ✅ OpenAI API 兼容格式
- ✅ 流式和非流式响应
- ✅ 工具调用（Function Calling）支持
- ✅ 多账号自动轮换
- ✅ Token 自动刷新
- ✅ API Key 认证
- ✅ 思维链（Thinking）输出
- ✅ 图片输入支持（Base64 编码）
- ✅ 图片生成支持（大/小香蕉 模型）
- ✅ Pro 账号随机 ProjectId 支持

## 环境要求

- Node.js >= 18.0.0

## 快速开始

### 1. 安装依赖

```bash
npm install
```

### 2. 配置环境变量

复制 `.env.example` 为 `.env` 并编辑配置：

```bash
cp .env.example .env
```

编辑 `.env` 文件配置必要参数：

```env
# 必填配置
API_KEY=sk-text
ADMIN_USERNAME=admin
ADMIN_PASSWORD=admin123
JWT_SECRET=your-jwt-secret-key-change-this-in-production

# 可选配置
# PROXY=http://127.0.0.1:7897
# SYSTEM_INSTRUCTION=你是聊天机器人
# IMAGE_BASE_URL=http://your-domain.com
```

### 3. 登录获取 Token

```bash
npm run login
```

浏览器会自动打开 Google 授权页面，授权后 Token 会保存到 `data/accounts.json`。

### 4. 启动服务

```bash
npm start
```

服务将在 `http://localhost:8045` 启动。

## Web 管理界面

服务启动后，访问 `http://localhost:8045` 即可打开 Web 管理界面。

### 功能特性

- 🔐 **安全登录**：JWT Token 认证，保护管理接口
- 📊 **实时统计**：显示总 Token 数、启用/禁用状态统计
- ➕ **多种添加方式**：
  - OAuth 授权登录（推荐）：自动完成 Google 授权流程
  - 手动填入：直接输入 Access Token 和 Refresh Token
- 🎯 **Token 管理**：
  - 查看所有 Token 的详细信息（Access Token 后缀、Project ID、过期时间）
  - 📊 查看模型额度：按类型分组显示（Claude/Gemini/其他），实时查看剩余额度和重置时间
  - 一键启用/禁用 Token
  - 删除无效 Token
  - 实时刷新 Token 列表
- ⚙️ **配置管理**：
  - 在线编辑服务器配置（端口、监听地址）
  - 调整默认参数（温度、Top P/K、最大 Token 数）
  - 修改安全配置（API 密钥、请求大小限制）
  - 配置代理、系统提示词等可选项
  - 热重载配置（部分配置需重启生效）

### 使用流程

1. **登录系统**
   - 使用 `.env` 中配置的 `ADMIN_USERNAME` 和 `ADMIN_PASSWORD` 登录
   - 登录成功后会自动保存 JWT Token 到浏览器

2. **添加 Token**
   - **OAuth 方式**（推荐）：
     1. 点击「OAuth登录」按钮
     2. 在弹窗中点击「打开授权页面」
     3. 在新窗口完成 Google 授权
     4. 复制浏览器地址栏的完整回调 URL
     5. 粘贴到输入框并提交
   - **手动方式**：
     1. 点击「手动填入」按钮
     2. 填写 Access Token、Refresh Token 和过期时间
     3. 提交保存

3. **管理 Token**
   - 查看 Token 卡片显示的状态和信息
   - 点击「📊 查看额度」按钮查看该账号的模型额度信息
     - 自动按模型类型分组（Claude/Gemini/其他）
     - 显示剩余额度百分比和进度条
     - 显示额度重置时间（北京时间）
     - 支持「立即刷新」强制更新额度数据
   - 使用「启用/禁用」按钮控制 Token 状态
   - 使用「删除」按钮移除无效 Token
   - 点击「刷新」按钮更新列表

4. **修改配置**
   - 切换到「设置」标签页
   - 修改需要调整的配置项
   - 点击「保存配置」按钮应用更改
   - 注意：端口和监听地址修改需要重启服务

### 界面预览

- **Token 管理页面**：卡片式展示所有 Token，支持快速操作
- **设置页面**：分类展示所有配置项，支持在线编辑
- **响应式设计**：支持桌面和移动设备访问

## API 使用

### 获取模型列表

```bash
curl http://localhost:8045/v1/models \
  -H "Authorization: Bearer sk-text"
```

### 聊天补全（流式）

```bash
curl http://localhost:8045/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-text" \
  -d '{
    "model": "gemini-2.0-flash-exp",
    "messages": [{"role": "user", "content": "你好"}],
    "stream": true
  }'
```

### 聊天补全（非流式）

```bash
curl http://localhost:8045/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-text" \
  -d '{
    "model": "gemini-2.0-flash-exp",
    "messages": [{"role": "user", "content": "你好"}],
    "stream": false
  }'
```

### 工具调用示例

```bash
curl http://localhost:8045/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-text" \
  -d '{
    "model": "gemini-2.0-flash-exp",
    "messages": [{"role": "user", "content": "北京天气怎么样"}],
    "tools": [{
      "type": "function",
      "function": {
        "name": "get_weather",
        "description": "获取天气信息",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {"type": "string", "description": "城市名称"}
          }
        }
      }
    }]
  }'
```

### 图片输入示例

支持 Base64 编码的图片输入，兼容 OpenAI 的多模态格式：

```bash
curl http://localhost:8045/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-text" \
  -d '{
    "model": "gemini-2.0-flash-exp",
    "messages": [{
      "role": "user",
      "content": [
        {"type": "text", "text": "这张图片里有什么？"},
        {
          "type": "image_url",
          "image_url": {
            "url": "data:image/jpeg;base64,/9j/4AAQSkZJRg..."
          }
        }
      ]
    }],
    "stream": true
  }'
```

支持的图片格式：
- JPEG/JPG (`data:image/jpeg;base64,...`)
- PNG (`data:image/png;base64,...`)
- GIF (`data:image/gif;base64,...`)
- WebP (`data:image/webp;base64,...`)

### 图片生成示例

支持使用 大/小香蕉 模型生成图片，生成的图片会以 Markdown 格式返回：

```bash
curl http://localhost:8045/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-text" \
  -d '{
    "model": "gemimi-3.0-pro-image",
    "messages": [{"role": "user", "content": "画一只可爱的猫"}],
    "stream": false
  }'
```

## 多账号管理

`data/accounts.json` 支持多个账号，服务会自动轮换使用：

```json
[
  {
    "access_token": "ya29.xxx",
    "refresh_token": "1//xxx",
    "expires_in": 3599,
    "timestamp": 1234567890000,
    "enable": true
  },
  {
    "access_token": "ya29.yyy",
    "refresh_token": "1//yyy",
    "expires_in": 3599,
    "timestamp": 1234567890000,
    "enable": true
  }
]
```

- `enable: false` 可禁用某个账号
- Token 过期会自动刷新
- 刷新失败（403）会自动禁用并切换下一个账号

## 配置说明

项目配置分为两部分：

### 1. config.json（基础配置）

基础配置文件，包含服务器、API 和默认参数设置：
