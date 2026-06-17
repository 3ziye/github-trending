<div align="center">

<img src="docs/images/logo.png" alt="LeoAI Logo" width="120" />

# LeoAI

**AI 驱动的后渗透综合管理平台**

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)
[![Java](https://img.shields.io/badge/Java-17%2B-orange)](https://openjdk.org/)
[![Spring Boot](https://img.shields.io/badge/Spring%20Boot-3.5.13-brightgreen)](https://spring.io/projects/spring-boot)
[![LangChain4j](https://img.shields.io/badge/LangChain4j-1.16.1-purple)](https://github.com/langchain4j/langchain4j)

LeoAI 是一款专为红队操作人员设计的后渗透管理工具，深度集成大语言模型（LLM）Agent 能力，实现智能化、自动化的后渗透操作流程。相比传统 WebShell 管理工具，LeoAI 提供 AI 辅助决策、多协议通信、流量伪装、团队协作等企业级能力，内置 Web 管理界面，开箱即用。

<img src="docs/images/screenshot-dashboard.png" alt="主界面截图" width="800" />

*节点管理主界面：节点列表、详情面板、流量伪装策略配置*

</div>

---

## 目录

- [功能特性](#功能特性)
- [技术栈](#技术栈)
- [环境要求](#环境要求)
- [快速开始](#快速开始)
- [配置说明](#配置说明)
- [使用指南](#使用指南)
- [常见问题](#常见问题)
- [安全建议](#安全建议)
- [免责声明](#免责声明)
- [License](#license)

---

## 功能特性

### AI 与智能化

| 功能 | 描述 |
|------|------|
| **AI Agent 自动化** | 基于 LangChain4j，支持多轮工具调用，自动规划和执行后渗透操作 |
| **多模型支持** | 兼容 OpenAI、Anthropic、通义千问、DeepSeek 及任何 OpenAI 兼容 API |
| **175 个 AI Tools** | AI Agent 可调用的原子能力，涵盖文件、进程、网络、凭据、扫描、HTTP 发包等全场景 |
| **24 个内置 AI Skills** | 预置的场景化任务提示词，一键启动完整攻击链（详见下方 Skills 列表） |
| **Skill 管理器** | 可视化管理 Skills：查看/编辑内容与描述、标签分类、启用/禁用、全文搜索，修改实时生效无需重启 |
| **上下文积累** | 侦察摘要自动积累，AI 上下文随操作深入持续增强 |
| **操作报告生成** | AI 自动生成操作总结和风险分析报告 |

<img src="docs/images/screenshot-ai-assistant.png" alt="AI 助手演示" width="800" />

*AI 助手自动调用侦察工具、分析结果并生成侦察摘要*

### 节点管理

| 功能 | 描述 |
|------|------|
| **多协议通信** | HTTP、HTTP Chunked（大文件传输）、WebSocket（实时交互） |
| **流量隐蔽** | TLS 指纹伪装、Header 噪声注入、URL 随机化、请求/响应自定义编码 |
| **代理转发** | 支持 HTTP 代理、SOCKS5 代理、本地端口转发（ssh -L 风格）、反向隧道（ssh -R 风格） |
| **团队协作** | 节点可在团队成员间共享，权限可控 |
| **批量节点管理** | 支持节点分组、标签管理、批量操作 |

### 操作控制台工具集

#### 交互与命令执行
- **Web 终端**：交互式 Shell，支持命令补全、历史记录、实时流输出
- **后台任务**：异步执行长时间命令，支持输出轮询和任务取消

#### 文件与存储
- **文件管理器**：树形目录浏览、上传/下载、在线编辑、压缩/解压、预览（文本/图片/PDF）、大文件分片传输
- **用户文件空间**：每个用户独立的本地文件存储区域

#### 数据库与信息系统
- **数据库控制台**：支持 MySQL、PostgreSQL、Oracle、SQLite、SQL Server，提供 SQL 编辑器和表结构浏览
- **注册表管理**（Windows）：浏览和修改注册表键值
- **事件日志查看**：查询 Windows 系统事件日志
- **防火墙管理**：查看和修改防火墙规则

#### 网络与扫描
- **端口扫描**：TCP 端口扫描、主机存活探测（Ping Sweep）
- **指纹识别**：HTTP/TCP 服务指纹识别，内置规则库，支持自定义规则
- **侦察扫描**：多目标、多规则并发侦察，结果自动汇总至 AI 上下文
- **HTTP 发包器**：Repeater（单次发包）和 Fuzzer（批量模糊测试）
- **代理转发**：在目标节点上开启 HTTP 代理、SOCKS5 代理、本地端口转发（ssh -L）或反向隧道（ssh -R），支持连接数统计与流量监控

#### 系统管理
- **截屏**：实时获取目标桌面截图
- **进程管理**：列出、杀死、创建进程
- **计划任务**：Windows 计划任务管理
- **服务管理**：启动、停止、重启 Windows 服务
- **Docker 管理**：列出、启动、停止、查看容器和镜像
- **应用管理**：Catalina 应用（Tomcat/WebLogic）、Spring Framework 运行时管理

#### 安全与权限
- **凭据提取**：系统凭据、浏览器数据、WiFi 配置
- **SUID/Capability 检查**：快速发现 Linux 提权点
- **用户账户管理**：目标主机用户枚举和操作
- **网络连接查看**：查看活跃连接、网络共享、已安装软件

#### 其他工具
- **类字节码查看**：提取并反编译 JVM 中的已加载类
- **剪贴板读取**：获取目标系统剪贴板内容
- **磁盘挂载管理**：查看和管理磁盘挂载点
- **HostId 切换**：单节点可管理多个内网主机

<img src="docs/images/screenshot-console.png" alt="操作控制台截图" width="800" />

*操作控制台：基础信息总览、AI 技能快捷面板与对话区*

### Shell 生成器

#### 内存马生成
- 支持类型：Filter、Servlet、Listener、Valve、Interceptor、WebSocket
- 支持中间件：Tomcat、Jetty、JBoss、JBossAS、JBossEAP6、JBossEAP7、Wildfly、Undertow、Resin、Glassfish、Payara、WebLogic、WebSphere、SpringWebMVC、Apusic、BES、InforSuite、TongWeb、Struct2（共 19 种）
- 表达式注入 Packer：OGNL、SpEL、EL、Groovy、Freemarker、MVEL、BeanShell、Velocity、Thymeleaf、JEXL、Jinjava、JXPath、Rhino、Aviator、ScriptEngine、BCEL、Translet、XmlDecoder、H2、Base64、Hex 等（共 23 种）

#### WebShell 生成
- 支持格式：JSP、JSPX

### 指纹与识别规则

- **内置规则库**：预置 38 条常见服务的 HTTP/TCP 指纹识别规则（Nginx、Tomcat、Jenkins、Nacos、Redis、MySQL、Elasticsearch、GitLab 等）
- **自定义规则**：通过「**识别规则**」页面新增、编辑、启用/禁用指纹规则
- **规则标签**：支持协议过滤和标签分组，便于在扫描时按需筛选

### 插件系统

- **Java 插件热加载**：动态加载和执行自定义 Java 插件
- **内置插件**：脚本执行、命令执行、WebLogic 密码获取、堆转储分析
- **可扩展**：支持开发和集成自定义功能插件

### 管理功能

| 功能 | 描述 |
|------|------|
| **用户管理** | 创建用户、角色分配、权限控制 |
| **团队管理** | 创建团队、成员邀请、节点共享 |
| **AI 配置** | 多 LLM 通道配置、模型切换、API Key 管理 |
| **审计日志** | 操作审计（命令执行、文件操作等）、AI 对话审计 |
| **会话管理** | 会话记录、结果导出、操作报告生成 |

---

## 技术栈

| 层级 | 技术选型 |
|------|--------|
| **Web 框架** | Spring Boot 3.5 |
| **AI 框架** | LangChain4j 1.16 |
| **LLM 支持** | OpenAI、Anthropic、通义千问、DeepSeek 及所有 OpenAI 兼容接口 |
| **数据库** | SQLite（内嵌，无需额外部署）|
| **ORM** | MyBatis 3 |
| **HTTP 客户端** | OkHttp 4 |
| **字节码操作** | Javassist 3.30 |
| **构建工具** | Maven（多模块）|
| **运行环境** | Java 17+ |

---

## 环境要求

| 项目 | 要求 |
|------|------|
| **Java 版本** | 17 或更高（JDK/JRE 均可） |
| **操作系统** | Linux、macOS、Windows |
| **内存** | 建议 4 GB 以上 |
| **磁盘** | 至少 500 MB 可用空间 |
| **浏览器** | Chrome、Firefox、Edge 等现代浏览器 |

> 无需单独安装数据库：内置 SQLite，首次启动自动初始化。  
> 无需额外部署前端：Web 界面已打包至 JAR 文件中。

---

## 快速开始

### 第一步：获取 JAR

从 [Releases](https://github.com/cha0upup/LeoAI/releases) 页面下载最新版本：

```
LeoAi-0.0.3.jar
```

### 第二步：启动

```bash
java -jar --add-opens java.base/java.lang=ALL-UNNAMED LeoAi-0.0.3.jar
```

> `--add-opens java.base/java.lang=ALL-UNNAMED` 参数**不可省略**，用于开放 Java 模块系统内部访问权限。

### 第三步：访问

浏览器打开：

```
http://localhost:8082
```

### 第四步：初始化

首次启动时，系统自动