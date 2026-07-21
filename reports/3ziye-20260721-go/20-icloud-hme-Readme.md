# iCloud Hide My Email 本地管理工具

[English](#english) | 中文

通过逆向 iCloud Web 接口和 IMAP 邮件协议，实现 Apple iCloud 隐藏邮箱别名的创建、列出和邮件收取功能。

## 功能特性

- ✅ **创建 HME 别名** — 自动生成 iCloud 隐藏邮箱地址
- ✅ **列出所有别名** — 查看账号下的所有 HME 别名
- ✅ **收取邮件** — 通过 IMAP 或 Web API 读取发到 HME 别名的邮件
- ✅ **双路径读信** — 邮件读取优先走 IMAP (App Password),无 App Password 时回退 Web API (Cookie)
- ✅ **多账号管理** — 支持多个 iCloud 账号并行管理
- ✅ **双认证模式** — Cookie (创建别名 + 读邮件回退) 和 App Password (IMAP 优先)

## 快速开始

### 1. 安装

```bash
# 前置要求: Go 1.26+
go version  # 确认 Go 版本

# 克隆项目
git clone <your-repo-url>
cd icloud-hme

# 编译
go build -o icloud-hme.exe .
```

### 2. 配置账号

在项目根目录创建 `accounts.json`:

```json
{
  "accounts": [
    {
      "id": "acc_1",
      "name": "主号",
      "cookies": [
        {
          "domain": ".icloud.com",
          "name": "x-apple-session-token",
          "value": "YOUR_SESSION_TOKEN_HERE"
        }
      ],
      "app_passwords": [
        {
          "icloud_email": "your_email@icloud.com",
          "password": "YOUR_APP_PASSWORD_HERE"
        }
      ]
    }
  ]
}
```

### 3. 启动服务

```bash
./icloud-hme.exe

# 服务默认监听 :8080
# 可通过环境变量 PORT 修改端口
PORT=9090 ./icloud-hme.exe
```

## API 接口

### 核心接口

#### 创建 HME 别名

```bash
POST /api/create

# 请求体
{
  "account_id": "acc_1",      # 必填: 账号 ID
  "label": "注册某网站"        # 可选: 别名标签
}

# 响应
{
  "success": true,
  "data": {
    "email": "xyz123@icloud.com",
    "label": "注册某网站",
    "created_at": "2024-01-15T10:30:00Z",
    "account_id": "acc_1"
  }
}
```

#### 读取邮件

```bash
GET /api/inbox?account_id=acc_1&alias=xyz123@icloud.com&limit=20&days=7

# 参数说明:
#   account_id - 必填: 账号 ID
#   alias      - 可选: 只读取发到该别名的邮件
#   limit      - 可选: 返回邮件数量 (默认 20)
#   days       - 可选: 查找最近几天的邮件 (默认 7,仅 IMAP 模式)

# 响应
{
  "success": true,
  "data": {
    "account_id": "acc_1",
    "alias": "xyz123@icloud.com",
    "count": 2,
    "method": "imap",
    "messages": [
      {
        "id": "1042",
        "from": "noreply@example.com",
        "to": "xyz123@icloud.com",
        "subject": "欢迎注册",
        "preview": "感谢您的注册...",
        "date": "2026-07-09T14:32:10+08:00"
      }
    ]
  }
}

# 读取方式 (自动选择):
#   method: "imap"    — 通过 App Password 认证 (优先)
#   method: "web_api" — 通过 Cookie 认证,无需 App Password (回退)
```

### 账号管理接口

#### 列出所有账号

```bash
GET /api/accounts

# 响应
{
  "success": true,
  "data": [
    {"id": "acc_1", "name": "主号"},
    {"id": "acc_2", "name": "副号"}
  ]
}
```

#### 添加账号

**简化版（cookies 可选）:**

```bash
POST /api/accounts

# 请求体
{
  "name": "新账号",
  "host": "icloud.com",           # 可选
  "proxy": "http://..."           # 可选
}

# 响应 - 状态为 pending,需登录
{
  "success": true,
  "data": {
    "id": "acc_xxx",
    "name": "新账号",
    "status": "pending"
  }
}
```

**完整版（带 Cookie）:**

```bash
POST /api/accounts

# 请求体
{
  "name": "新账号",
  "cookies": "{\"x-apple-session-token\":\"token_value\"}",  # JSON 或 Header 格式
  "host": "icloud.com",           # 可选
  "proxy": "http://..."           # 可选
}

# 响应
{
  "success": true,
  "data": {
    "id": "acc_3",
    "name": "新账号",
    "status": "active"
  }
}
```

#### 账号登录（获取 Cookie）

```bash
POST /api/accounts/:id/login

# 请求体
{
  "password": "用户的常规iCloud密码",  # 不是 App Password
  "otp_code": "123456"                  # 可选,2FA 验证码
}

# 响应
{
  "success": true,
  "data": {
    "id": "acc_1",
    "cookies": {
      "x-apple-session-token": "...",
      "X-APPLE-WEBAUTH-TOKEN": "..."
    }
  }
}
```

#### 删除账号

```bash
DELETE /api/accounts/:id

# 响应
{
  "success": true,
  "data": {"id": "acc_3"}
}
```

#### 设置 App Password

```bash
POST /api/accounts/:id/password

# 请求体
{
  "icloud_email": "your_email@icloud.com",
  "app_password": "xxxx-xxxx-xxxx-xxxx"
}

# 响应
{
  "success": true,
  "data": {
    "id": "acc_1",
    "icloud_email": "your_email@icloud.com"
  }
}
```

### 别名管理接口

#### 列出所有别名

```bash
GET /api/aliases?account_id=acc_1

# 响应
{
  "success": true,
  "data": {
    "account_id": "acc_1",
    "count": 15,
    "aliases": [
      {
        "email": "xyz123@icloud.com",
        "label": "注册某网站",
        "created_at": "2024-01-15T10:30:00Z"
      }
    ]
  }
}
```

#### 停用别名

```bash
POST /api/aliases/:id/deactivate

# 请求体
{
  "account_id": "acc_1"
}

# 响应
{
  "success": true,
  "data": {
    "anonymous_id": "abc123",
    "success": true
  }
}
```

#### 激活别名

```bash
POST /api/aliases/:id/reactivate

# 请求体
{
  "account_id": "acc_1"
}

# 响应
{
  "success": true,
  "data": {
    "anonymous_id": "abc123",
    "success": true
  }
}
```

#### 删除别名

```bash
DELETE /api/aliases/:id

# 请求体
{
  "account_id": "acc_1"
}

# 响应
{
  "success": true,
  "data": {
    "anonymous_id": "abc123"
  }
}
```

## 认证方式

### 方式一: Cookie 认证 (推荐,功能最完整)

Cookie 认证可实现所有功能:创建别名、读取邮件、管理别名。

**适用范围:**
- 创建/停用/激活/删除 HME 别名 ✅
- 读取邮件 (通过 iCloud Web API,无需 App Password) ✅

**获取 Cookie:**

1. 使用浏览器登录 [icloud.com](https://www.icloud.com) 或 [icloud.com.cn](https://www.icloud.com.cn) (国区)
2. 打开浏览器开发者工具 (F12)
3. 进入 Application → Cookies
4. 导出全部 Cookie 为 `{"key":"value"}` 格式的 JSON

**关键 Cookie (必需):**
- `X-APPLE-WEBAUTH-TOKEN` — 