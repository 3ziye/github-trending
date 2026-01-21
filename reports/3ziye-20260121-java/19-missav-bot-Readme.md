# MissAV Bot

一个基于 Telegram 的视频推送机器人,自动抓取 MissAV 最新视频并推送给订阅用户。

## 功能特性

- 🤖 **自动抓取** - 定时抓取最新视频信息
- 📺 **预览播放** - 支持视频预览和封面图展示
- 🔔 **智能订阅** - 支持订阅全部/演员/标签
- 🚫 **自动去重** - 避免重复抓取和推送
- 🔍 **视频搜索** - 支持按演员、标签搜索
- 📊 **推送记录** - 完整的推送历史记录
- 🎯 **自动发现群组** - 启动时自动发现并订阅所有 Bot 所在的群组
- 🛡️ **防刷屏机制** - 智能去重，避免重启时重复推送
- 🎬 **手动爬取** - 支持按演员、番号、关键词手动爬取视频

## 技术栈

- Spring Boot 3.3.5
- MyBatis-Plus 3.5.9
- MySQL 8.0
- Telegram Bot API
- Jsoup (网页解析)
- Spring Boot Actuator (健康检查)

## 环境要求

- JDK 21+
- Maven 3.6+
- MySQL 8.0+
- Telegram Bot Token

## 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/your-username/missav-bot.git
cd missav-bot
```

### 2. 创建数据库

```sql
CREATE DATABASE missav_bot CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

执行数据库初始化脚本:

```sql
-- 视频表
CREATE TABLE videos (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    code VARCHAR(50) UNIQUE NOT NULL COMMENT '番号',
    title VARCHAR(500) COMMENT '标题',
    actresses VARCHAR(500) COMMENT '演员',
    tags VARCHAR(500) COMMENT '标签',
    duration INT COMMENT '时长(分钟)',
    release_date DATETIME COMMENT '发布日期',
    cover_url VARCHAR(500) COMMENT '封面URL',
    preview_url VARCHAR(500) COMMENT '预览视频URL',
    detail_url VARCHAR(500) COMMENT '详情页URL',
    pushed BOOLEAN DEFAULT FALSE COMMENT '是否已推送',
    created_id VARCHAR(50),
    created_name VARCHAR(100),
    created_time DATETIME,
    updated_id VARCHAR(50),
    updated_name VARCHAR(100),
    updated_time DATETIME,
    remark VARCHAR(500),
    INDEX idx_code (code),
    INDEX idx_pushed (pushed)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='视频表';

-- 订阅表
CREATE TABLE subscriptions (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    chat_id BIGINT NOT NULL COMMENT 'Telegram聊天ID',
    chat_type VARCHAR(20) COMMENT '聊天类型',
    type VARCHAR(20) NOT NULL COMMENT '订阅类型:ALL/ACTRESS/TAG',
    keyword VARCHAR(100) COMMENT '关键词',
    enabled BOOLEAN DEFAULT TRUE COMMENT '是否启用',
    created_id VARCHAR(50),
    created_name VARCHAR(100),
    created_time DATETIME,
    updated_id VARCHAR(50),
    updated_name VARCHAR(100),
    updated_time DATETIME,
    remark VARCHAR(500),
    INDEX idx_chat_id (chat_id),
    INDEX idx_type (type)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='订阅表';

-- 推送记录表
CREATE TABLE push_records (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    video_id BIGINT NOT NULL COMMENT '视频ID',
    chat_id BIGINT NOT NULL COMMENT '聊天ID',
    status VARCHAR(20) NOT NULL COMMENT '状态:SUCCESS/FAILED',
    fail_reason VARCHAR(500) COMMENT '失败原因',
    pushed_at DATETIME COMMENT '推送时间',
    message_id INT COMMENT '消息ID',
    created_id VARCHAR(50),
    created_name VARCHAR(100),
    created_time DATETIME,
    updated_id VARCHAR(50),
    updated_name VARCHAR(100),
    updated_time DATETIME,
    remark VARCHAR(500),
    INDEX idx_video_id (video_id),
    INDEX idx_chat_id (chat_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='推送记录表';
```

### 3. 配置文件

复制配置文件并修改:

```bash
cp src/main/resources/application-local.yaml.example src/main/resources/application-local.yaml
```

修改 `application-local.yaml`:

```yaml
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/missav_bot?useSSL=false&serverTimezone=Asia/Shanghai
    username: your_username
    password: your_password

telegram:
  bot:
    token: YOUR_BOT_TOKEN
    username: YOUR_BOT_USERNAME
    default-chat-id: YOUR_DEFAULT_CHAT_ID
```

### 4. 编译运行

```bash
# 编译
mvn clean package -DskipTests

# 运行
java -jar target/missav_bot_*.jar --spring.profiles.active=local
```

## 使用教程

### 创建 Telegram Bot

1. 在 Telegram 中搜索 [@BotFather](https://t.me/BotFather)
2. 发送 `/newbot` 创建新机器人
3. 按提示设置机器人名称和用户名
4. 获取 Bot Token 并配置到 `application-local.yaml`

### 获取 Chat ID

1. 将机器人添加到群组
2. 发送任意消息
3. 访问 `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
4. 在返回的 JSON 中找到 `chat.id`

### 机器人命令

#### 订阅管理

```
/subscribe              - 订阅全部新片
/subscribe 演员名       - 订阅指定演员
/subscribe #标签        - 订阅指定标签
/unsubscribe           - 取消全部订阅
/unsubscribe 演员名     - 取消演员订阅
/list                  - 查看我的订阅
```

#### 查询命令

```
/search 关键词          - 搜索视频
/latest                - 查看最新视频
/status                - 查看机器人状态
/help                  - 查看帮助信息
```

#### 手动爬取命令

```
/crawl actor 演员名 [数量]    - 爬取指定演员的作品
/crawl code 番号              - 爬取指定番号的作品
/crawl search 关键词 [数量]   - 按关键词搜索并爬取
```

**说明**：
- 手动爬取的视频会**立即推送给命令触发者**
- 支持指定爬取数量（可选参数）
- 所有用户都可以使用手动爬取功能

### 使用示例

1. **订阅全部新片**
   ```
   /subscribe
   ```

2. **订阅指定演员**
   ```
   /subscribe 三上悠亚
   ```

3. **订阅标签**
   ```
   /subscribe #中文字幕
   ```

4. **搜索视频**
   ```
   /search SSIS
   ```

5. **手动爬取演员作品**
   ```
   /crawl actor 三上悠亚 10
   ```

6. **手动爬取指定番号**
   ```
   /crawl code SSIS-001
   ```

7. **按关键词搜索爬取**
   ```
   /crawl search SSIS 20
   ```

## 配置说明

### 爬虫配置

```yaml
crawler:
  enabled: true              # 是否启用爬虫
  interval: 900000          # 抓取间隔(毫秒) 15分钟
  initial-pages: 2          # 初始抓取页数
  user-agent: Mozilla/5.0   # User-Agent
```

### 代理配置

如果你的服务器无法直接访问 Telegram API（如在中国大陆），可以配置代理：

```yaml
telegram:
  proxy:
    enabled: 