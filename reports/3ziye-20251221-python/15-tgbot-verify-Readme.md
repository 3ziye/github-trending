# SheerID 自动认证 Telegram 机器人

![Stars](https://img.shields.io/github/stars/PastKing/tgbot-verify?style=social)
![Forks](https://img.shields.io/github/forks/PastKing/tgbot-verify?style=social)
![Issues](https://img.shields.io/github/issues/PastKing/tgbot-verify)
![License](https://img.shields.io/github/license/PastKing/tgbot-verify)

> 🤖 自动完成 SheerID 学生/教师认证的 Telegram 机器人
> 
> 基于 [@auto_sheerid_bot](https://t.me/auto_sheerid_bot) GGBond 的旧版代码改进

---

## 📋 项目简介

这是一个基于 Python 的 Telegram 机器人，可以自动完成多个平台的 SheerID 学生/教师身份认证。机器人自动生成身份信息、创建认证文档并提交到 SheerID 平台，大大简化了认证流程。

### 🎯 支持的认证服务

| 命令 | 服务 | 类型 | 状态 | 说明 |
|------|------|------|------|------|
| `/verify` | Gemini One Pro | 教师认证 | ✅ 完整 | Google AI Studio 教育优惠 |
| `/verify2` | ChatGPT Teacher K12 | 教师认证 | ✅ 完整 | OpenAI ChatGPT 教育优惠 |
| `/verify3` | Spotify Student | 学生认证 | ✅ 完整 | Spotify 学生订阅优惠 |
| `/verify4` | Bolt.new Teacher | 教师认证 | ✅ 完整 | Bolt.new 教育优惠（自动获取 code）|
| `/verify5` | YouTube Premium Student | 学生认证 | ⚠️ 半成品 | YouTube Premium 学生优惠（见下方说明）|

> **⚠️ YouTube 认证特别说明**：
> 
> YouTube 认证功能目前为半成品状态，使用前请仔细阅读 [`youtube/HELP.MD`](youtube/HELP.MD) 文档。
> 
> **主要区别**：
> - YouTube 的原始链接格式与其他服务不同
> - 需要手动从浏览器网络日志中提取 `programId` 和 `verificationId`
> - 然后手动组成标准的 SheerID 链接格式
> 
> **使用步骤**：
> 1. 访问 YouTube Premium 学生认证页面
> 2. 打开浏览器开发者工具（F12）→ 网络（Network）标签
> 3. 开始认证流程，搜索 `https://services.sheerid.com/rest/v2/verification/`
> 4. 从请求载荷中获取 `programId`，从响应中获取 `verificationId`
> 5. 手动组成链接：`https://services.sheerid.com/verify/{programId}/?verificationId={verificationId}`
> 6. 使用 `/verify5` 命令提交该链接

### ✨ 核心功能

- 🚀 **自动化流程**：一键完成信息生成、文档创建、认证提交
- 🎨 **智能生成**：自动生成学生证/教师证 PNG 图片
- 💰 **积分系统**：签到、邀请、卡密兑换等多种获取方式
- 🔐 **安全可靠**：使用 MySQL 数据库，支持环境变量配置
- ⚡ **并发控制**：智能管理并发请求，确保稳定性
- 👥 **管理功能**：完善的用户管理和积分管理系统

---

## 🛠️ 技术栈

- **语言**：Python 3.11+
- **Bot框架**：python-telegram-bot 20.0+
- **数据库**：MySQL 5.7+
- **浏览器自动化**：Playwright
- **HTTP客户端**：httpx
- **图像处理**：Pillow, reportlab, xhtml2pdf
- **环境管理**：python-dotenv

---

## 🚀 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/PastKing/tgbot-verify.git
cd tgbot-verify
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
playwright install chromium
```

### 3. 配置环境变量

复制 `env.example` 为 `.env` 并填写配置：

```env
# Telegram Bot 配置
BOT_TOKEN=your_bot_token_here
CHANNEL_USERNAME=your_channel
CHANNEL_URL=https://t.me/your_channel
ADMIN_USER_ID=your_admin_id

# MySQL 数据库配置
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=tgbot_verify
```

### 4. 启动机器人

```bash
python bot.py
```

---

## 🐳 Docker 部署

### 使用 Docker Compose（推荐）

```bash
# 1. 修改 .env 文件配置
cp env.example .env
nano .env

# 2. 启动服务
docker-compose up -d

# 3. 查看日志
docker-compose logs -f
```

### 手动 Docker 部署

```bash
# 构建镜像
docker build -t tgbot-verify .

# 运行容器
docker run -d \
  --name tgbot-verify \
  --env-file .env \
  -v $(pwd)/logs:/app/logs \
  tgbot-verify
```

---

## 📖 使用说明

### 用户命令

```bash
/start              # 开始使用（注册）
/about              # 了解机器人功能
/balance            # 查看积分余额
/qd                 # 每日签到（+1积分）
/invite             # 生成邀请链接（+2积分/人）
/use <卡密>         # 使用卡密兑换积分
/verify <链接>      # Gemini One Pro 认证
/verify2 <链接>     # ChatGPT Teacher K12 认证
/verify3 <链接>     # Spotify Student 认证
/verify4 <链接>     # Bolt.new Teacher 认证
/verify5 <链接>     # YouTube Premium Student 认证
/getV4Code <id>     # 获取 Bolt.new 认证码
/help               # 查看帮助信息
```

### 管理员命令

```bash
/addbalance <用户ID> <积分>     # 增加用户积分
/block <用户ID>                 # 拉黑用户
/white <用户ID>                 # 取消拉黑
/blacklist                      # 查看黑名单
/genkey <卡密> <积分> [次数] [天数]  # 生成卡密
/listkeys                       # 查看卡密列表
/broadcast <文本>               # 群发通知
```

### 使用流程

1. **获取认证链接**
   - 访问对应服务的认证页面
   - 开始认证流程
   - 复制浏览器地址栏中的完整 URL（包含 `verificationId`）

2. **提交认证请求**
   ```
   /verify3 https://services.sheerid.com/verify/xxx/?verificationId=yyy
   ```

3. **等待处理**
   - 机器人自动生成身份信息
   - 创建学生证/教师证图片
   - 提交到 SheerID 平台

4. **获取结果**
   - 审核通常在几分钟内完成
   - 成功后会返回跳转链接

---

## 📁 项目结构

```
tgbot-verify/
├── bot.py                  # 机器人主程序
├── config.py               # 全局配置
├── database_mysql.py       # MySQL 数据库管理
├── .env                    # 环境变量配置（需自行创建）
├── env.example             # 环境变量模板
├── requirements.txt        # Python 依赖
├── Dockerfile              # Docker 镜像构建
├── docker-compose.yml      # Docker Compose 配置
├── handlers/               # 命令处理器
│   ├── user_commands.py    # 用户命令
│   ├── admin_commands.py   # 管理员命令
│   └── verify_commands.py  # 认证命令
├── one/                    # Gemini One Pro 认证模块
├── k12/                    # ChatGPT K12 认证模块
├── spotify/                # Spotify Student 认证模块
├── youtube/                # YouTube Premium 认证模块
├── Boltnew/                # Bolt.new 认证模块
└── utils/                  # 工具函数
    ├── messages.py         # 消息模板
    ├── concurrency.py      # 并发控制
    └── checks.py           # 权限检查
```

---

## ⚙️ 配置说明

### 环境变量

| 变量名 | 必填 | 说明 | 默认值 |
|--------|------|------|--------|
| `BOT_TOKEN` | ✅ | Telegram Bot