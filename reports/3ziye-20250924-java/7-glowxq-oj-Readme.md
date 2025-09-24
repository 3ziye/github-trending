# Glowxq-OJ - 在线编程测评系统

<div align="center">

![GlowXQ Logo](docs/images/logo-icon.svg)



**面向信奥赛、少儿编程教学的在线测评平台**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Java](https://img.shields.io/badge/Java-21-orange.svg)](https://openjdk.java.net/projects/jdk/21/)
[![Spring Boot](https://img.shields.io/badge/Spring%20Boot-3.x-green.svg)](https://spring.io/projects/spring-boot)
[![Vue](https://img.shields.io/badge/Vue-3.x-brightgreen.svg)](https://vuejs.org/)
[![Docker](https://img.shields.io/badge/Docker-Supported-blue.svg)](https://www.docker.com/)

![GlowXQ Logo](docs/images/logo.svg)

[🚀 在线体验](http://42.192.87.184:7301/login) | [📖 完整文档](docs/) | [🐛 问题反馈](https://github.com/glowxq/glowxq-oj/issues)

</div>

## ✨ 项目简介

Glowxq-OJ 是一个专为信息学奥林匹克竞赛（信奥赛）和少儿编程教学设计的在线编程测评系统。本项目提供开源版本和商业版本，开源版本包含核心的在线测评功能，商业版本提供更完整的教学管理功能。

### 🎯 在线体验

- **商业版体验地址**: [http://42.192.87.184:7301](http://42.192.87.184:7301) (多租户版本记得**选择租户**)
- **开源版本**: 本仓库提供完整的开源实现，前后端已经整合，运行后访问http://localhost:7101访问

#### 🔑 默认测试账号

系统提供以下测试账号，密码统一为：**123456**

| 角色 | 账号 | 密码 | 说明 |
|------|------|------|------|
| 管理员 | 13667700000 | 123456 | 系统管理员，拥有所有权限 |
| 学生 | 13667700001 | 123456 | 普通学生账号，可提交代码 |
| 校长 | 13667700002 | 123456 | 校长账号，管理学校事务 |
| 老师 | 13667700003 | 123456 | 教师账号，管理班级和学生 |
| 系统管理员 | 13667700004 | 123456 | 超级管理员，系统维护 |

> 💡 **提示**: 生产环境请务必修改默认密码！

### 🌐 SaaS 云服务

**无需部署，开箱即用！** 我们提供专业的SaaS云服务，类似于 [Hydro](https://hydro.ac)、[洛谷](https://www.luogu.com.cn/) 等知名平台。

#### ✨ SaaS服务优势
- 🚀 **即开即用**: 无需复杂部署，注册账号即可使用
- 🎯 **完整功能**: 体验所有商业版功能，包括班级管理、多租户、GlowC、GlowGame等
- 🛠️ **技术支持**: 专业技术团队提供全方位支持
- 🔒 **数据安全**: 企业级数据安全保障
- 📈 **弹性扩容**: 根据使用量自动扩容，无需担心性能问题
- 💰 **成本优化**: 按需付费，相比自建节省70%以上成本

#### 📞 获取SaaS服务
想要体验完整的商业版功能？联系我们获取SaaS服务账号：
- **邮箱**: [glowxq@qq.com](mailto:glowxq@qq.com)
- **微信**: 扫描下方二维码添加作者微信

<div align="center">
<table>
<tr>
<td align="center">
<img src="docs/images/contact-qr.jpg" width="200" alt="联系二维码"/>
<br/>
<b>联系客服微信</b>
</td>
<td align="center">
<img src="docs/images/group-wechat.png" width="200" alt="微信技术交流群"/>
<br/>
<b>技术交流群</b>
</td>
</tr>
</table>
</div>

### 📋 版本对比

| 功能模块 | 开源版 | 商业版 |
|---------|--------|--------|
| 在线测评 | ✅ | ✅ |
| 题目管理 | ✅ | ✅ |
| 用户系统 | ✅ | ✅ |
| 代码编辑器 | ✅ | ✅ |
| 多语言支持 | ✅ | ✅ |
| 班级管理 | ❌ | ✅ |
| 多租户系统 | ❌ | ✅ |
| GlowC (C++画图) | ❌ | ✅ |
| GlowGame (编程游戏) | ❌ | ✅ |
| 部门管理 | ❌ | ✅ |
| 持续更新 | 社区驱动 | 商业支持 |

## 🏗️ 技术架构

### 后端技术栈
- **核心框架**: Spring Boot 3.x + Java 21
- **数据库**: MySQL 8.0 + Redis
- **ORM框架**: MyBatis-Flex
- **权限认证**: Sa-Token
- **API文档**: Knife4j (Swagger)
- **消息队列**: 内置队列系统
- **文件存储**: 本地存储 + OSS支持
- **容器化**: Docker + Docker Compose

### 前端技术栈
- **框架**: Vue 3.x + TypeScript
- **UI组件**: Element Plus
- **代码编辑器**: Monaco Editor
- **构建工具**: Vite
- **状态管理**: Pinia

### 判题系统
- **沙箱技术**: 安全沙箱
- **支持语言**: C/C++、Java、Python、JavaScript等
- **判题模式**: 普通判题、特殊判题、交互判题
- **性能优化**: 虚拟线程 + 异步处理

## 📚 文档导航

### 🚀 快速上手
- [📖 文档中心](docs/) - 完整的文档导航和索引
- [⚡ 快速部署](docs/deployment/quick-start.md) - 5分钟快速部署指南
- [🐳 Docker部署](docs/deployment/docker-deploy.md) - Docker一键部署方案

### 📖 详细文档
- [🛠️ 部署指南](docs/deployment/deployment-guide.md) - 完整的部署配置指南
- [💻 开发指南](docs/development/development-guide.md) - 开发环境搭建和规范
- [👤 用户指南](docs/user/user-guide.md) - 系统使用手册
- [🔧 管理指南](docs/admin/admin-guide.md) - 系统管理员操作指南

### 🎯 按角色查看
- **开发者**: [开发指南](docs/development/development-guide.md) → [API文档](docs/development/api-reference.md)
- **管理员**: [快速部署](docs/deployment/quick-start.md) → [管理指南](docs/admin/admin-guide.md)
- **教师**: [用户指南](docs/user/user-guide.md) → [功能介绍](docs/user/features.md)
- **学生**: [用户指南](docs/user/user-guide.md) → [常见问题](docs/user/faq.md)

## 🚀 快速开始

### 环境要求

- **Java**: JDK 21+
- **Node.js**: 16.x+
- **MySQL**: 8.0+
- **Redis**: 6.0+
- **Docker**: 20.x+ (可选)
- **Maven**: 3.8+

### 🐳 Docker 一键部署（推荐）

**全自动部署，包含MySQL、Redis、应用服务的完整解决方案！**

1. **克隆项目**
```bash
git clone https://github.com/glowxq/glowxq-oj.git
cd glowxq-oj
```

2. **一键启动**
```bash
# Linux/macOS
chmod +x start.sh
./start.sh

# Windows (使用Git Bash或WSL)
bash start.sh
```

3. **访问系统**
- 前端地址: http://localhost:7101
- API文档: http://localhost:7101/doc.html

**✨ 特性：**
- 🚀 一键部署，自动配置MySQL、Redis
- 📦 自动导入初始化SQL数据
- 🔄 服务健康检查和自动重启
- 💾 数据持久化存储
- 📊 完整的日志和监控

**🛠️ 管理命令：**
```bash
./start.sh          # 启动所有服务
./stop.sh           # 停止所有服务
./stop.sh --cleanup # 停止并清理资源
```

详细部署说明请参考：[Docker部署指南](docs/deployment/docker-deploy.md)

### 🛠️ 本地开发部署

#### 1. 数据库准备

**MySQL 配置**
```sql
-- 创建数据库
CREATE DATABASE glowxq_oj CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
CREATE DATABASE glowxq_system CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

-- 导入初始化数据
source init/初始化SQL.sql;
```

**Redis 配置**
```bash
# 启动 Redis 服务
redis-server
```

#### 2. 后端启动

```bash
# 安装依赖
mvn clean install -DskipTests

# 启动 OJ 服务
cd app/app-oj
mvn spring-boot:run

# 启动系统管理服务（可选）
cd app/app-system
mvn spring-boot:run
```

#### 3. 前端启动

前端已经集成到springboot中 springboot启动时会自动启动vue项目，所以不需要再启动前端项目。
直接访问 localhost:7101 即可访问前端页面。

## 📸 系统截图

### 🎨 特色功能 - C++画图 (GlowC)
<div a