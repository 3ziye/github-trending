# WebSSH（Spring Boot）

基于 Java Spring Boot + WebSocket 的浏览器 SSH 工具，支持多标签终端、会话保存、SFTP 文件管理、端口转发、主机指纹校验、移动端适配、国际化和登录鉴权。

## 功能

- **登录鉴权** — Spring Security 表单登录，内存用户存储（BCrypt 加密）
- **多标签 SSH 终端** — 每个标签独立 WebSocket + xterm.js，互不干扰
- **会话保存** — 按登录用户持久化到本地 JSON 文件
- **凭据加密保存** — AES-GCM 加密，主密钥可配置
- **主机指纹校验** — SHA-256，首次连接自动信任并回填
- **认证方式** — 密码认证、私钥认证（私钥口令可选）
- **终端尺寸同步** — 浏览器窗口变化自动同步到远端 PTY
- **SFTP 文件管理** — 目录浏览、上传（分片）、下载（分片 + ACK 流控）、创建目录
- **SSH 端口转发** — 本地转发（L）/ 远程转发（R）
- **Shell 工作目录追踪** — 注入 shell 钩子实时感知远端 `$PWD` 变化，SFTP 面板自动同步
- **终端主题** — 6 种配色方案（默认蓝、橙、绿、琥珀、紫、红）
- **国际化** — 支持 7 种语言（简体中文、English、日本語、한국어、Deutsch、Français、Русский）
- **全屏模式** — 终端可切换全屏显示
- **移动端适配** — 响应式 Web 设计，针对手机端优化布局、侧边栏滑动及文件管理交互
- **聊天机器人接入** — 支持 Telegram Bot、微信ClawBot 与 QQ 私聊机器人，可直接通过消息管理 SSH 与 AI 编程任务

## 技术栈

| 层级 | 技术 |
|------|------|
| 后端框架 | Java 17 + Spring Boot 3.3 |
| Web 通信 | Spring WebSocket（`/ws/ssh`） |
| 安全 | Spring Security（表单登录 + BCrypt） |
| SSH 客户端 | JSch（`com.github.mwiede:jsch:0.2.19`） |
| 前端终端 | xterm.js + xterm-addon-fit |
| 构建工具 | Maven |

前端终端依赖以静态资源方式内置：

- `/vendor/xterm/xterm.js` + `xterm.css`
- `/vendor/xterm-addon-fit/xterm-addon-fit.js`

## 项目结构

```
├── build.sh                          # 构建打包脚本
├── start.sh                          # 启动/停止/重启管理脚本
├── pom.xml                           # Maven 配置
└── src/main/
    ├── java/com/webssh/
    │   ├── WebSshApplication.java    # 启动入口
    │   ├── config/                   # 配置类（Security、WebSocket、属性绑定）
    │   ├── session/                  # 会话持久化与凭据加密
    │   ├── web/                      # REST 控制器（认证、会话 CRUD、页面路由）
    │   └── ws/                       # WebSocket 核心处理器（SSH/SFTP/端口转发）
    └── resources/
        ├── application.properties    # 应用配置
        └── static/                   # 前端静态资源
            ├── index.html            # 主页面（终端 UI）
            ├── login.html            # 登录页
            ├── app.js                # 前端主逻辑
            ├── i18n.js               # 国际化翻译
            ├── style.css             # 主样式
            └── login.css             # 登录页样式
```

## 默认配置

配置文件：[application.properties](src/main/resources/application.properties)

### 基础配置

| 配置项 | 默认值 | 说明 |
|--------|--------|------|
| `webssh.auth.username` | `admin` | 登录用户名 |
| `webssh.auth.password` | `admin123` | 登录密码 |
| `webssh.session-store.directory` | `./data/sessions` | 会话数据存储目录 |
| `webssh.crypto.master-key` | `change-this-master-key-in-production` | 凭据加密主密钥 |
| `webssh.ssh.allow-legacy-ssh-rsa` | `true` | 是否允许旧版 ssh-rsa 算法 |
| `webssh.ssh.server-alive-interval-ms` | `30000` | SSH Keepalive 间隔（毫秒） |
| `server.port` | `8080` | 服务端口 |

### 资源治理配置

这些配置用于限制系统资源消耗，防止单个用户或机器人任务占满系统资源。

| 配置项 | 默认值 | 说明 |
|--------|--------|------|
| `webssh.resource.shell-output.max-size` | `128` | 最大并发 Shell 输出任务数 |
| `webssh.resource.bot-command.max-size` | `16` | 最大并发机器人命令任务数 |
| `webssh.resource.ai-task.max-size` | `8` | 最大并发 AI 编程任务数 |
| `webssh.resource.ws-shell-per-user` | `6` | 每用户最大并发 SSH 标签页 |
| `webssh.resource.bot-command-per-user` | `2` | 每用户最大并发机器人指令 |
| `webssh.resource.ai-task-per-user` | `1` | 每用户最大并发 AI 任务 |
| `webssh.resource.bot-command-timeout` | `30s` | 机器人普通命令执行超时 |
| `webssh.resource.ai-task-timeout` | `15m` | AI 编程任务总执行超时 |

> ⚠️ 生产环境务必通过环境变量或外部配置覆盖默认账户密码和加密主密钥。

## 快速开始

### 开发模式

```bash
# 1. 克隆项目
git clone https://github.com/Jstrom2022/webSSH.git && cd webSSH

# 2. 启动应用（需要 Java 17+ 和 Maven）
mvn spring-boot:run

# 3. 打开浏览器访问
# http://localhost:8080
# 默认账户：admin / admin123
```

### 构建打包

```bash
./build.sh
```

执行后会在 `release/` 目录生成部署文件：

```
release/
├── webssh.jar                    # 可执行 JAR
├── start.sh                      # 启动管理脚本
└── config/application.properties # 外部配置（可修改）
```

### 服务器部署

将 `release/` 目录上传到服务器，使用启动脚本管理：

```bash
./start.sh start     # 启动
./start.sh stop      # 停止
./start.sh restart   # 重启
./start.sh status    # 查看状态
```

默认 JVM 参数：`-Xms128m -Xmx512m -XX:+UseG1GC -XX:MaxGCPauseMillis=200`

可通过 `JAVA_OPTS` 环境变量覆盖：

```bash
JAVA_OPTS="-Xms256m -Xmx1g" ./start.sh start
```

### Docker 部署

> 需要 Docker 20.10+ 以及 Docker Compose v2（`docker compose` 命令）。

**一键启动**

```bash
# 克隆项目
git clone https://github.com/Jstrom2022/webSSH.git && cd webSSH

# 后台构建并启动（首次构建需要几分钟）
docker compose up -d --build

# 访问 http://localhost:8080
```

**环境变量配置（推荐）**

在项目根目录创建 `.env` 文件，覆盖默认的敏感配置：

```env
WEBSSH_AUTH_USERNAME=admin
WEBSSH_AUTH_PASSWORD=your-strong-password
WEBSSH_CRYPTO_MASTER_KEY=your-random-secret-key
```

> ⚠️ 生产环境务必修改以上三项，`.env` 文件已在 `.gitignore` 中排除，不会提交到仓库。

**数据持久化**

会话数据挂载到宿主机的 `./data/` 目录，容器重建后数据不丢失。

**常用命令**

```bash
docker compose up -d          # 后台启动
docker compose down           # 停止并删除容器
docker compose logs -f        # 实时查看日志
docker compose restart        # 重启服务
docker compose ps             # 查看运行状态
```

## 兼容旧 SSH 服务器（ssh-rsa）

如果连接时报错：

> `Algorithm negotiation fail ... algorithmName="server_host_key" ... serverProposal="ssh-rsa"`

说明目标服务器只提供 `ssh-rsa` 主机密钥。当前默认已开启兼容：

```properties
webssh.ssh.allow-legacy-ssh-rsa=true
```

建议优先升级服务器到 `ss