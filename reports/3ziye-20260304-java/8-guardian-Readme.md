<p align="center">
  <a href="https://central.sonatype.com/artifact/io.github.biggg-guardian/guardian-repeat-submit-spring-boot-starter"><img src="https://img.shields.io/maven-central/v/io.github.biggg-guardian/guardian-repeat-submit-spring-boot-starter?label=Maven%20Central&color=orange" alt="Maven Central"></a>
  <img src="https://img.shields.io/badge/Java-1.8+-blue?logo=openjdk&logoColor=white" alt="Java">
  <img src="https://img.shields.io/badge/Spring%20Boot-2.7.x-6DB33F?logo=springboot&logoColor=white" alt="Spring Boot">
  <a href="https://github.com/BigGG-Guardian/guardian/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="License"></a>
  <a href="https://github.com/BigGG-Guardian/guardian/releases"><img src="https://img.shields.io/github/v/release/BigGG-Guardian/guardian?label=Release&color=green" alt="Release"></a>
  <a href="https://github.com/BigGG-Guardian/guardian/stargazers"><img src="https://img.shields.io/github/stars/BigGG-Guardian/guardian?style=flat&logo=github" alt="Stars"></a>
</p>

<h1 align="center">Guardian</h1>
<p align="center"><b>轻量级 Spring Boot API 请求层防护框架</b></p>
<p align="center">防重提交、接口限流、接口幂等、参数自动Trim、慢接口检测、请求链路追踪、IP黑白名单、防重放攻击、接口开关 —— 一个 Starter 搞定 API 请求防护。</p>

<p align="center">
  <a href="https://github.com/BigGG-Guardian/guardian">GitHub</a> ·
  <a href="https://gitee.com/BigGG-Guardian/guardian">Gitee</a> ·
  <a href="https://central.sonatype.com/artifact/io.github.biggg-guardian/guardian-repeat-submit-spring-boot-starter">Maven Central</a>
</p>

---

<p align="center">
  <img src="assets/guardian-mindmap.png" alt="Guardian 功能全景图" width="700">
</p>

---

## 功能一览

| 功能       | Starter                                      | 注解 | YAML | 说明                                           |
|----------|----------------------------------------------|------|------|----------------------------------------------|
| 防重复提交    | `guardian-repeat-submit-spring-boot-starter` | `@RepeatSubmit` | ✅ | 防止用户重复提交表单/请求                                |
| 接口限流     | `guardian-rate-limit-spring-boot-starter`    | `@RateLimit` | ✅ | 滑动窗口 + 令牌桶，双算法可选                             |
| 接口幂等     | `guardian-idempotent-spring-boot-starter`    | `@Idempotent` | — | Token 机制保证接口幂等性，支持结果缓存                       |
| 参数自动Trim | `guardian-auto-trim-spring-boot-starter`     | — | ✅ | 自动去除请求参数首尾空格 + 不可见字符替换                       |
| 慢接口检测    | `guardian-slow-api-spring-boot-starter`      | `@SlowApiThreshold` | ✅ | 慢接口检测 + Top N 统计 + Actuator 端点               |
| 请求链路追踪   | `guardian-trace-spring-boot-starter`         | — | ✅ | 自动生成/透传 TraceId，MDC 日志串联，支持跨线程传递、MQ 链路追踪     |
| IP黑白名单   | `guardian-ip-filter-spring-boot-starter`     | — | ✅ | 全局黑名单 + URL 绑定白名单，支持精确/通配符/CIDR              |
| 防重放攻击    | `guardian-anti-replay-spring-boot-starter`   | — | ✅ | Timestamp + Nonce 双重校验，nonce TTL 与 timestamp 窗口解耦 |
| 接口开关     | `guardian-api-switch-spring-boot-starter`    | — | ✅ | 动态关闭/开启接口                                    |
| 参数签名     | `guardian-sign-spring-boot-starter`          | `@SignVerify` | ✅ | 支持多种签名算法，请求参数签名验证 + 响应结果签名               |

每个功能独立模块、独立 Starter，**用哪个引哪个，互不依赖**。所有模块的 YAML 配置均支持**配置中心动态刷新**（Nacos / Apollo 等），无需重启即可生效。

---

## 快速开始

### 所有starter模块引用

```xml
<dependency>
    <groupId>io.github.biggg-guardian</groupId>
    <artifactId>guardian-starter-all</artifactId>
    <version>1.8.1</version>
</dependency>
```
><small>特别说明：`请求链路追踪模块`若开启RabbitMq/Kafka/RocketMq请求链路追踪，需额外引入对应的依赖(`guardian-trace-rabbitmq`/`guardian-trace-kafka`/`guardian-trace-rocketmq`)</small>

### 防重复提交

```xml
<dependency>
    <groupId>io.github.biggg-guardian</groupId>
    <artifactId>guardian-repeat-submit-spring-boot-starter</artifactId>
    <version>1.8.1</version>
</dependency>
```

```java
@PostMapping("/submit")
@RepeatSubmit(interval = 10, timeUnit = TimeUnit.SECONDS, message = "订单正在处理，请勿重复提交")
public Result submitOrder(@RequestBody OrderDTO order) {
    return orderService.submit(order);
}
```

### 接口限流

```xml
<dependency>
    <groupId>io.github.biggg-guardian</groupId>
    <artifactId>guardian-rate-limit-spring-boot-starter</artifactId>
    <version>1.8.1</version>
</dependency>
```

**滑动窗口（默认）：**

```java
@RateLimit(qps = 1, window = 60, windowUnit = TimeUnit.SECONDS, rateLimitScope = RateLimitKeyScope.IP)
```

**令牌桶：**

```java
@RateLimit(qps = 5, capacity = 20, algorithm = RateLimitAlgorithm.TOKEN_BUCKET)
```

或 YAML 批量配置：

```yaml
guardian:
  rate-limit:
    urls:
      # 滑动窗口
      - pattern: /api/sms/send
        qps: 1
        window: 60
        window-unit: seconds
        rate-limit-scope: ip
      # 令牌桶
      - pattern: /api/seckill/**
        qps: 10
        capacity: 50
        algorithm: token_bucket
        rate-limit-scope: global
```

### 接口幂等

```xml
<dependency>
    <groupId>io.github.biggg-guardian</groupId>
    <artifactId>guardian-idempotent-spring-boot-starter</artifactId>
    <version>1.8.1</version>
</dependency>
```

**1. 获取 Token：**

```
GET /guardian/i