# 基础脚手架后端 - zl-backend

## 项目简介

`zl-backend` 是一套企业级后端基础脚手架，基于 Spring Boot 构建。该项目采用模块化设计，旨在提供一个可扩展、易维护的后端开发基础架构，适用于快速搭建企业级应用系统。
项目提供了完整的安全认证、多模块管理、扩展功能支持等特性，可帮助开发团队快速启动新项目开发。

## 技术栈

### 核心技术
- **核心框架**：Spring Boot 3.4.5
- **持久层**：MyBatis 3.0.4、PageHelper 2.1.0
- **数据库**：MySQL 8.3.0
- **数据库连接池**：Druid 1.2.24
- **缓存**：Redis、Redisson 3.13.6
- **安全认证**：Spring Security、JWT 0.12.6
- **API文档**：Knife4j 4.5.0（基于OpenAPI 3）
- **构建工具**：Maven
- **Java 版本**：Java 17+
- **模块管理**：Maven 多模块项目结构

### 工具库
- **Hutool 5.8.0.M3**：Java工具库，提供丰富的工具方法
- **Fastjson2 2.0.53**：高性能JSON处理库
- **EasyExcel 3.3.2**：Excel导入导出工具
- **Lombok 1.18.20**：代码简化工具，减少样板代码
- **Jackson 2.18.0**：JSON序列化和反序列化
- **BouncyCastle 1.70**：加密算法实现
- **UserAgentUtils 1.21**：客户端信息解析
- **iTextPDF 5.5.13.3**：PDF导出功能
- **PDFBox 2.0.30**：PDF处理工具

### 扩展技术
- **Netty 4.1.79.Final**：高性能网络通信框架
- **MinIO 8.5.3**：对象存储服务
- **OSHI 6.6.6**：系统信息采集库
- **Spring AI 1.0.0-M6**：AI集成框架，支持多种大模型
- **LangChain4j 1.0.1-beta6**：大语言模型应用开发框架
- **XXL-JOB 3.2.0**：分布式任务调度平台
- **RabbitMQ**：消息队列中间件
- **EMQ MQTT**：物联网消息协议支持
- **WebFlux**：响应式编程支持
- **Jedis**：Redis客户端

## 项目结构

```bash
zl-backend/
├── .gitignore                    # Git忽略文件配置
├── README.md                     # 项目说明文档
├── pom.xml                       # 项目父POM文件
├── docs/                         # 文档目录
│   ├── 大文件处理方案/            # 大文件处理相关文档
│   ├── 权限认证设计/             # 权限认证相关文档
│   ├── 通用功能/                 # 通用功能文档
│   │   ├── 幂等控制方案/         # 幂等性控制设计文档
│   │   ├── 数据脱敏方案/         # 数据脱敏模块详解
│   │   ├── 日志方案/             # 日志系统使用指南
│   │   └── 异常处理设计/         # 全局异常处理设计文档
│   ├── 系统架构/                 # 系统架构文档
│   └── LLM应用/                   # 大语言模型应用文档
├── sql/                          # SQL脚本目录
│   ├── zl.sql                   # 初始化数据库脚本
│   └── test_learning_lesson_data.sql
├── zl-common/                    # 通用工具类和异常处理模块
├── zl-common-core/               # 通用核心功能模块
│   ├── zl-common-idempotent/     # 幂等性控制模块
│   └── zl-common-sensitive/      # 数据脱敏模块
├── zl-model/                     # 数据模型定义模块
├── zl-framework/                 # 框架核心模块，包含基础配置和通用组件
├── zl-security/                  # 安全认证与授权模块
├── zl-web/                       # Web 层模块，包含控制器和入口类
└── zl-extend/                    # 扩展功能模块
    ├── zl-file/                  # 文件处理相关模块
    │   ├── zl-file-starter       # 文件服务启动器
    │   └── zl-minio              # MinIO 文件存储实现
    ├── zl-netty/                 # Netty 网络通信模块
    ├── zl-oshi/                  # 系统信息采集模块（基于 OSHI）
    ├── zl-springai/              # Spring AI 集成模块
    ├── zl-langchain4j/           # LangChain4j 集成模块
    ├── zl-websocket/            # WebSocket 通信模块
    ├── zl-rabbitmq/             # RabbitMQ 消息队列集成模块
    ├── zl-emqx/                 # EMQ MQTT 物联网服务模块
    └── zl-xxl-job/              # XXL-JOB 分布式任务调度模块
```

## 模块说明

### 核心模块

- **zl-common**：提供通用工具类、异常处理、常量定义等基础功能
- **zl-common-core**：通用核心功能模块，包含幂等性控制、数据脱敏等核心功能
  - **zl-common-idempotent**：基于AOP的幂等性控制实现，支持注解式防重复提交
  - **zl-common-sensitive**：基于Jackson序列化的数据脱敏模块，支持多种脱敏策略
- **zl-model**：定义数据实体、DTO、VO等数据模型
- **zl-framework**：框架核心配置，包含异步任务管理、安全配置、全局异常处理等
- **zl-security**：认证授权机制，基于Spring Security和JWT实现，支持RBAC权限模型
- **zl-web**：Web层入口，包含控制器、启动类等

### 扩展模块

- **zl-file**：文件处理模块，提供基于MinIO的文件存储服务，支持大文件分片上传和断点续传
  - **zl-file-starter**：文件服务自动配置启动器
  - **zl-minio**：MinIO对象存储实现
- **zl-netty**：高性能网络通信模块，基于Netty框架实现，支持TCP/UDP协议和自定义心跳检测
- **zl-oshi**：系统信息采集模块，可获取服务器CPU、内存、磁盘等硬件信息，支持系统监控
- **zl-springai**：AI功能集成，基于Spring AI框架，支持多种大模型接入和向量数据库
- **zl-langchain4j**：LangChain4j集成，提供大语言模型应用能力，支持RAG和文档解析
- **zl-websocket**：WebSocket通信模块，支持实时消息推送和双向通信
- **zl-rabbitmq**：消息队列集成，支持异步消息处理和延迟消息
- **zl-emqx**：EMQ MQTT 物联网服务模块，支持设备连接和消息订阅发布
- **zl-xxl-job**：分布式任务调度模块，支持定时任务和分片广播任务

## 功能特性

### 安全认证
- 基于JWT的身份认证机制
- RBAC权限控制模型（用户-角色-资源）
- 细粒度的API权限控制
- 支持Token过期刷新机制
- 密码加密存储（BCrypt）
- 登录验证码支持
- ThreadLocal用户上下文管理
- 三组件协同认证流程（JwtAuthenticationFilter、UserTokenInterceptor、JwtAuthorizationManager）

### 数据访问
- 基于MyBatis的ORM映射
- 分页查询支持（PageHelper）
- 事务管理
- 数据源监控（Druid）
- Redis缓存支持
- Redisson分布式锁

### API文档
- 基于Knife4j的OpenAPI 3规范API文档
- 自动生成接口文档
- 在线接口测试
- 接口分组管理

### 系统功能
- **幂等性控制**：基于AOP的注解式防重复提交，支持自定义间隔时间和提示信息
- **数据脱敏**：基于Jackson序列化的数据脱敏功能，支持手机号、身份证、邮箱等多种脱敏策略
- **全局异常处理**：统一的异常处理机制，支持错误码管理和国际化
- **日志系统**：基于SLF4J+Logback的分级日志系统，支持按功能和级别分类输出
- **参数校验**：基于Spring Validation的参数校验框架
- **统一响应格式**：标准化的API响应格式，支持分页和错误信息

### 扩展能力
- 文件存储与管理（支持MinIO）
- 大文件分片上传和断点续传（基于MD5的文件命名冲突解决方案）
- 系统监控（CPU、内存、磁盘等信息）
- AI功能集成（支持通义千问等多种大模型）
  - Spring AI集成：支持Function Calling和向量数据库
  - LangChain4j集成：支持RAG和文档解析
  - MCP协议支持：标准化的AI模型与外部工具交互
- WebSocket实时通信
- 高性能网络通信（Netty）
- 消息队列支持（RabbitMQ）
- 物联网服务支持（EMQ MQTT）
- 分布式任务调度（XXL-JOB）
- PDF导出功能
- Excel导入导出

## 配置说明

### 主要配置文件
- **application.yml**：核心配置文件，包含服务器、安全、MyBatis等基础配置
- **application-dev.yml**：开发环境配置，包含数据库、Redis、AI服务等配置
- **application-file.yml**：文件服务配置，支持MinIO
- **application-extend.y