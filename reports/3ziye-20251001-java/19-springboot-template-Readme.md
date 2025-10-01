<p align="center">
  <a href="https://github.com/AntonyCheng">
    <img alt="spring-boot-init-template logo" src="picture/logo/logo.png" title="logo"/>
  </a>
</p>

> **作者：[AntonyCheng](https://github.com/AntonyCheng)**
>
> **版本号：v2.2.1-jdk17-pre**
>
> **开源协议：[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0.html)**
> 
> **注意事项：该README跟随版本号的更新而更新，所有Git分支其实都是Pre预览分支，其中最新的内容并不能及时展现在该README中，所以想要使用稳定且具有对应说明的版本，推荐从Releases中下载。但是想要时刻跟进模板开发进度，也可以直接从各个Git分支拉取，查看每次提交的对应说明！**

# SpringBoot初始化模板

**基于 Java Web 项目的 SpringBoot 框架初始化模板**，该模板整合了常用的框架，广泛支持JDK11和JDK17，部分版本兼容JDK8，该模板适用于前后端分离项目启动开发，保证大家在此基础上能够快速开发自己的项目，同时也适合入门学习，本项目会由作者持续更新。

* [SpringBoot初始化模板](#springboot初始化模板)
  * [软件版本要求](#软件版本要求)
  * [模板特点](#模板特点)
    * [主流框架](#主流框架)
    * [业务特性](#业务特性)
  * [业务功能](#业务功能)
    * [示例业务](#示例业务)
    * [单元测试](#单元测试)
  * [快速上手](#快速上手)
    * [必须执行](#必须执行)
    * [可选执行](#可选执行)
      * [启动前端项目](#启动前端项目)
      * [整合Spring AI](#整合spring-ai)
      * [整合缓存服务](#整合缓存服务)
        * [整合系统缓存（Redis）](#整合系统缓存redis)
        * [整合业务缓存（Redisson）](#整合业务缓存redisson)
        * [整合本地缓存（Caffeine）](#整合本地缓存caffeine)
      * [整合消息队列](#整合消息队列)
        * [激活消息队列](#激活消息队列)
        * [自定义消息队列](#自定义消息队列)
      * [整合Elasticsearch](#整合elasticsearch)
      * [整合MongoDB](#整合mongodb)
      * [整合对象存储服务](#整合对象存储服务)
        * [整合腾讯云COS](#整合腾讯云cos)
        * [整合MinIO](#整合minio)
        * [整合阿里云OSS](#整合阿里云oss)
      * [整合验证码](#整合验证码)
      * [整合邮件](#整合邮件)
      * [整合离线IP库](#整合离线ip库)
      * [配置国际化](#配置国际化)
      * [配置SaToken](#配置satoken)
        * [开启鉴权认证功能](#开启鉴权认证功能)
          * [鉴权功能](#鉴权功能)
          * [认证功能](#认证功能)
        * [开启JWT](#开启jwt)
          * [整合Redis](#整合redis)
          * [整合JWT](#整合jwt)
          * [确认鉴权模式](#确认鉴权模式)
      * [配置定时任务](#配置定时任务)
        * [SpringBoot任务调度](#springboot任务调度)
        * [XxlJob任务调度](#xxljob任务调度)
        * [PowerJob任务调度](#powerjob任务调度)
      * [配置WebSocket](#配置websocket)
      * [配置SpringBootAdmin](#配置springbootadmin)
      * [配置Canal](#配置canal)
        * [Canal简介](#canal简介)
        * [搭建Deployer&Adapter系统](#搭建deployeradapter系统)
        * [搭建Deployer&Client系统](#搭建deployerclient系统)
  * [容器化部署](#容器化部署)
    * [准备工作](#准备工作)
    * [启动基础组件](#启动基础组件)
    * [启动前后端服务](#启动前后端服务)
  * [前端预览](#前端预览)
  * [申明&联系我](#申明联系我)
  * [项目历史](#项目历史)
  * [下一步开发计划](#下一步开发计划)

## 软件版本要求

MySQL 8.0.X（推荐）

Redis 7.X.X（强制）

Elasticsearch 7.X.X（强制，特别推荐7.14.0）

RaabbitMQ 3.X.X（推荐）

说明：其他没有提及到的软件版本均广泛支持

## 模板特点

### 主流框架

- **Java 17**
- **SpringBoot 3.2.5**
  - spring-boot-starter-web == 基于 Spring MVC 的 Web 应用依赖
  - spring-boot-starter-undertow == 轻量级、高性能 Servlet 容器
  - spring-boot-starter-aop == 提供面向切面编程功能
  - spring-boot-starter-validation == 参数校验依赖
  - spring-boot-starter-data-mongodb == Spring Data MongoDB 依赖
  - spring-boot-starter-email == Spring Data Email 依赖
  - spring-boot-starter-freemaker == 模板引擎依赖
  - spring-boot-starter-test == Spring Boot Test 依赖
  - spring-boot-configuration-processor == 生成配置元数据信息，辅助开发工具
- **前端模板**
  - vue-admin-template 4.4.0 == 这是一个极简的 vue admin 管理后台，只包含了 Vue 2 & Element UI & axios & iconfont & permission control & lint
- **Spring AI 1.1.0**
  - spring-ai-openai-spring-boot-starter == Spring AI OpenAI模型依赖
  - spring-ai-zhipuai-spring-boot-starter == Spring AI 智谱AI模型依赖
  - spring-ai-ollama-spring-boot-starter == Spring AI Ollama框架AI模型依赖
- **Netty**
  - netty-all 4.1.114.Final == Netty 框架
- **数据驱动层**
  - mysql-connector-j 8.0.33 == Java 连接 MySQL 依赖
  - mybatis-spring 3.0.4 == MyBatis Spring 依赖
  - mybatis-plus-boot-starter 3.5.8 == MyBatis-Plus 框架
  - mybatis-plus-annotation 3.5.7 == MyBatis-Plus 注解依赖
  - shardingsphere-jdbc 5.5.0 == 分布式数据库解决方案
  - druid-spring-boot-3-starter 1.2.23 == Druid 连接池
- **工具类**
  - lombok 1.18.34 == POJO 简化工具
  - hutool-all 5.8.32 == Hutool 工具类
  - commons-lang3 3.17.0 == Apache Commons Lang 工具类
  - commons-io 2.17.0 == Apache Commons IO 工具类
  - commons-codec 1.17.1 == Apache Commons Codec 工具类
  - commons-pool2 2.12.0 == Apache Commons Pool 工具类
  - commons-collections4 4.5.0-M2 == Apache Commons Collections 工具类
  - commons-math3 3.6.1 == Apache Commons Math 工具类
  - commons-compress 1.27.1 == Apache Commons Compress 工具类
  - okhttp 4.12.0 == OK Http 工具类
  - okio 3.9.0 == OK IO 工具类
  - fastjson2 2.0.53 == FastJSON 工具类
  - ip2region 2.7.0 == 离线 IP 地址定位库
- **权限校验**
  - sa-token-spring-boot3-starter 1.39.0 == SaToken 认证鉴权框架
  - sa-token-core 1.39.0 == SaToken 认证鉴权框架核心依赖
  - sa-token-jwt 1.39.0 == SaToken 认证鉴权框架 JWT 依赖
  - sa-token-redis-jackson 1.39.0 == SaToken 认证鉴权框架 Redis 依赖
- **缓存服务**
  - spring-boot-starter-data-redis == Spring Data Redis 依赖
  - spring-boot-starter-cache == Spring Cache 依赖
  - redisson 3.37.0 == Redis 的基础上实现的 Java 驻内存数据网格
- **本地缓存服务**
  - caffeine 3.1.8 == Caffeine 本地缓存依赖
- **消息队列**
  - spring-boot-starter-amqp == 支持 AMQP （高级消息队列协议）消息代理
  - spring-rabbit-test == Spring 支持对 RabbitMQ 消息队列的单元测试
- **搜索引擎**
  - easy-es-boot-starter 2.0.0 == 简化 Elasticsearch 搜索引擎，可以像 Mybatis-Plus 操作 MySQL 一样操作 Elasticsearch 的开源框架
  - elasticsearch 7.14.0 == Elasticsearch 依赖
  - elasticsearch-