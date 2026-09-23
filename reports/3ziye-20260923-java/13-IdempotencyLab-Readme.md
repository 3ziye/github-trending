# IdempotencyLab

一个面向 Java / Spring Boot 业务的幂等契约测试框架。

它不是帮你实现幂等，而是帮你验证：

- 同一请求重复提交时，系统会不会只生效一次
- 并发重放时，会不会写出脏状态
- 超时重试时，会不会产生重复副作用
- MQ 重复消费、回调乱序时，会不会破坏最终结果

## 这套框架做什么

IdempotencyLab 把“幂等”从代码习惯变成一份可验证的契约。

你在业务方法上声明幂等规则，框架会自动：

1. 读取契约
2. 生成重复、并发、超时、重放类攻击流量
3. 执行业务适配器
4. 收集执行快照
5. 对照契约做结果比对
6. 输出报告

## 真实执行链路

当前样例的完整链路是：

`SampleDemoController` -> `SampleVerificationService` -> `IdempotencyLabFacade` -> `DefaultIdempotencyTestEngine` -> `DefaultAttackGenerator` / `DefaultResultComparator` -> `ReportWriter`

对应源码：

- [SampleDemoController](idempotencylab-samples/src/main/java/com/idempotencylab/samples/SampleDemoController.java)
- [SampleVerificationService](idempotencylab-samples/src/main/java/com/idempotencylab/samples/SampleVerificationService.java)
- [IdempotencyLabFacade](idempotencylab-spring-boot-starter/src/main/java/com/idempotencylab/starter/IdempotencyLabFacade.java)
- [DefaultIdempotencyTestEngine](idempotencylab-core/src/main/java/com/idempotencylab/core/DefaultIdempotencyTestEngine.java)
- [DefaultAttackGenerator](idempotencylab-attack-generator/src/main/java/com/idempotencylab/attackgenerator/DefaultAttackGenerator.java)
- [DefaultResultComparator](idempotencylab-core/src/main/java/com/idempotencylab/core/DefaultResultComparator.java)
- [ConsoleReportWriter](idempotencylab-reporter/src/main/java/com/idempotencylab/reporter/ConsoleReportWriter.java)

## 模块

- `idempotencylab-contracts`：幂等契约注解和场景范围定义
- `idempotencylab-core`：核心模型、执行引擎、结果比对
- `idempotencylab-attack-generator`：攻击流量生成
- `idempotencylab-observer`：执行观察
- `idempotencylab-reporter`：报告输出
- `idempotencylab-spring-boot-starter`：Spring Boot 自动配置和门面
- `idempotencylab-samples`：可运行样例

## 快速开始

### 环境要求

- Java 17+
- Maven 3.9+

### 构建

```bash
mvn clean package
```

### 启动样例

```bash
mvn -pl idempotencylab-samples spring-boot:run
```

启动后访问：

```text
http://localhost:8080/demo/idempotency/report
```

## 一个最小示例

```java
@IdempotencyContract(
    name = "创建支付单",
    businessKey = "merchantOrderNo",
    scope = IdempotencyScope.API,
    repeatableInputs = {"merchantOrderNo", "amount"},
    oneTimeSideEffects = {"databaseWrite", "eventPublish"},
    description = "同一个 merchantOrderNo 在同一业务域内只能成功创建一次支付单。"
)
public ExecutionSnapshot execute(AttackScenario scenario) {
    ...
}
```

框架会根据这份契约，自动生成重复请求、并发重放、超时重试等场景，再把实际执行结果和契约要求做比对。

## 配置

`idempotencylab.enabled=true` 时启用 starter 自动配置，设为 `false` 可关闭整套自动装配。

常用配置项：

- `idempotencylab.sample-key`
- `idempotencylab.duplicate-requests`
- `idempotencylab.concurrent-requests`
- `idempotencylab.timeout-retries`
- `idempotencylab.message-duplicates`
- `idempotencylab.callback-replays`

## 文档

- [快速上手](docs/01-快速上手.md)
- [执行链路](docs/02-执行链路.md)
- [模块说明](docs/03-模块说明.md)
- [当前实现](docs/04-当前实现.md)

## 当前状态

这是一版已经打通样例链路的骨架实现，适合继续往下面扩：

- MQ 消费验证
- 回调乱序验证
- 超时重试验证
- 报告增强
- CI 集成

