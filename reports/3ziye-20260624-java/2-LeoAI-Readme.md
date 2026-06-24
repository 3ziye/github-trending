[English](README_EN.md) | **中文**

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
| **多模型支持** | 兼容 OpenAI、通义千问、DeepSeek 及任何 OpenAI 兼容 API |
| **175 个 AI Tools** | AI Agent 可调用的原子能力，涵盖文件、进程、网络、凭据、扫描、HTTP 发包等全场景 |
| **8 个内置 AI Skills** | 预置的场景化任务提示词，一键启动完整攻击链（详见下方 Skills 列表） |
| **Skill 管理器** | 可视化管理 Skills：查看/编辑内容与描述、标签分类、启用/禁用、全文搜索、导入/导出，修改实时生效无需重启 |
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
- **应用管理**：Catalina 应用（Tomcat 5/6/7/8/9+、WebLogic）容器与 Spring Framework 运行时管理；支持 idle 部署 / puppet 注入全局 ClassLoader 等场景（线程扫描 + JMX MBean 双兜底），可即时卸载 Filter / Servlet / Valve / Listener / Controller / Interceptor

#### 安全与权限
- **凭据提取**：系统凭据、浏览器数据、WiFi 配置
- **SUID/Capability 检查**：快速发现 Linux 提权点
- **用户账户管理**：目标主机用户枚举和操作
- **网络连接查看**：查看活跃连接、网络共享、已安装软件

#### 其他工具
- **类字节码查看**：提取并反编译 JVM 中的已加载类
- **类与资源浏览**：按类名或路径读取 puppet 进程的 classpath 资源（jar 内 .class、`application.yml`、`META-INF/MANIFEST.MF` 等），自动识别二进制/文本/.class 类型并反编译为 Java 源码；当 puppet 注入 Tomcat 全局 ClassLoader 时，自动降级遍历所有 WebappClassLoader 兜底
- **剪贴板读取**：获取目标系统剪贴板内容
- **磁盘挂载管理**：查看和管理磁盘挂载点
- **HostId 切换**：单节点可管理多个内网主机

<img src="docs/images/screenshot-console.png" alt="操作控制台截图" width="800" />

*操作控制台：基础信息总览、AI 技能快捷面板与对话区*

### Shell 生成器

#### 内存马生成
- 支持类型：Filter、Servlet、Listener、Valve、Interceptor、Controller、WebSocket
- 支持中间件：Tomcat、Jetty、JBossAS、JBossEAP6、JBossEAP7、Wildfly、Undertow、Resin、Glassfish、Payara、WebLogic、WebSphere、SpringWebMVC、Apusic、BES、InforSuite、TongWeb、Struct2（共 18 种）
- 表达式注入 Packer：OGNL、SpEL、EL、Groovy、Freemarker、MVEL、BeanShell、Velocity、Thymeleaf、JEXL、Jinjava、JXPath、Rhino、Aviator、ScriptEngine、BCEL、Translet、XmlDecoder、H2、Base64、Hex 等（共 41 种）

#### WebShell 生成
- 支持格式：JSP、JSPX、Groovy

### 指纹与识别规则

- **内置规则库**：预置 10 条常见服务的 HTTP/TCP 指纹识别规则（Nginx、Tomcat、Redis、MySQL、Shiro、SSH、FTP、SMTP、Spring Boot Actuator、WordPress 等）
- **自定义规则**：通过「**识别规则**」页面新增、编辑、启用/禁用指纹规则
- **规则标签**：支持协议过滤和标签分组，便于在扫描时按需筛选
- **导入/导出**：支持单条或批量导出为 `.json` / `.zip`，可按冲突策略（跳过/覆盖/重命名）导入，方便团队间共享规则库

### 插件与脚本执行

- **统一执行控制台**：「脚本与插件」模块同时承载脚本编辑与字节码执行
  - **脚本编辑器**：支持 JavaScript / Groovy / Python，临时执行无需保存；可一键「保存为插件」
  - **Java Class 执行**：拖拽 `.class` 文件或直接粘贴 base64 字节码（自动清洗 URL-safe / 空白 / padding，自动校验 `cafebabe` magic），临时执行不持久化；可保存为 Java 插件
- **统一插件库**：Java 字节码与 js/groovy/python 脚本插件并存，按类型徽章区分；脚本插件可一键「载入编辑器」再编辑后执行
- **Java 插件热加载**：动态加载和执行自定义 Java 插件
- **AI Skills 内置插件**：脚本执行、命令执行、WebLogic 密码获取、堆转储分析等开箱即用
- **导入/导出**：单条 `.plugin` 或批量 `.zip`，导入时支持跳过/覆盖冲突策略

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
| **LLM 支持** | OpenAI、通义千问、DeepSeek 及所有 OpenAI 兼容接