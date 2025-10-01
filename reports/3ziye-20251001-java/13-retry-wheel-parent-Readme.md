# ResilientWheel
一款基于 Netty HashedWheelTimer 的高可用分布式重试引擎，当前采用 MySQL 持久化 + 分布式抢占/粘滞租约，未来可无缝迁移至 Redis 等存储。

## 模块结构

```
retry-wheel-parent/
├─ retry-wheel-spring-boot3-starter/ # Starter：核心引擎、自动装配、SPI、Mapper 等
└─ sql/ # 初始化/清理 SQL（建表、索引）
```


---

## 快速开始

### 1) 引入依赖

```xml
<dependency>
  <groupId>com.fastretry</groupId>
  <artifactId>retry-wheel-spring-boot3-starter</artifactId>
  <version>${latest}</version>
</dependency>
```
### 2) 初始化数据库

执行 sql/schema.sql (建表、索引、枚举/注释；包含 retry_task 表及必要索引).

3) 启用与配置（application.yml）
```yml
retry:
  stick:
    enable: true
    lease-ttl: 30s
    renew-ahead: 10s
  tx:
    propagation: REQUIRED
    read-only: false
    isolation: DEFAULT
    timeout-seconds: 10
  wheel:
   tick-duration: 100ms
   ticks-per-wheel: 512
   max-pending-timeouts: 100000
  scan:
   initial-delay: 1000
   period: 2000
   batch: 200
  executor:
   core-pool-size: 8
   max-pool-size: 32
   queue-capacity: 1000
   keep-alive: 60s
   rejected-handler: CALLER_RUNS
  backoff:
   strategy: exponential
   base: 1s
   min: 500ms
   max: 300s
   jitter-ratio: 0.2
  default-max-retry: 5
  default-execute-timeout: 10s

```
### 4) 注册任务处理器示例
```JAVA
@Service(value = "test-biz")
public class CallHandler implements RetryTaskHandler<PayloadModel> {
    @Override
    public boolean supports(String bizType) {
        return "test-biz".equals(bizType);
    }

    @Override
    public boolean execute(RetryTaskContext ctx, PayloadModel payload) throws Exception {
        // 模拟失败
        if (payload.getSimulateStatus() == 500) {
            throw new RuntimeException("remote 500");
        }
        if (payload.getSimulateStatus() == 408) {
            Thread.sleep(5000);
        }
        return true;
    }

    @Override
    public TypeReference<PayloadModel> payloadType() {
        return new TypeReference<PayloadModel>() {};
    }
}
```
### 5) 投递任务
```JAVA
SubmitOptions opt = SubmitOptions.builder()
  .maxRetry(8)
  .priority(10)
  .executeTimeoutMs(4000)
  .backoffStrategy("exponential")
  .delay(Duration.ofSeconds(0))
  .deadline(Instant.now().plus(Duration.ofMinutes(10)))
  .build();
PayloadModel payload = new PayloadModel();
payload.setBody("hello world");
payload.setUrl("www.baidu.com");
payload.setSimulateStatus(408);
String taskId = engine.submit("test-biz", payload, opt);
return Map.of("taskId", taskId);
```



# 通知模块重构

> 为重试框架提供 **可插拔、可路由、可限流、可观测** 的通知能力。支持单条通知，覆盖 DLQ、最大重试、不可重试失败、接管、续约失败、引擎异常、持久化异常等事件。

---

## 特性

- **SPI 可插拔**：`Notifier` 接口，内置 `LoggingNotifier`，支持自定义（如 飞书/钉钉/kim）。
- **异步派发**：`AsyncNotifyingService` 独立线程池 + 指数退避重试，不阻塞主流程。
- **路由/过滤**：按事件/业务路由到不同通道；
- **可观测性**：Micrometer 指标 + 结构化日志。
- **开关友好**：通过`NotifyingFacade`封装`AsyncNotifyingService`, `retry.notify.enabled=false`时不装配异步实现, 由门面内部自动降级为NOOP，调用方零判空，无NPE风险。

---

## 快速开始

### 1) 引入（在 Starter 中已自动装配）

确保引入 `retry-wheel-spring-boot3-starter`，通知模块随 Starter 自动装配。

### 2) 配置

```yaml
retry:
  notify:
    enabled: true         
    async:
      core-pool-size: 2
      max-pool-size: 4
      queue-capacity: 2000
      keep-alive: 30s
    rate-limit:
      window: 30s                # 限流窗口
      threshold: 50                  # 限流阈值
```

### 3) 事件模型/严重级别
```JAVA
// 事件模型
public enum NotifyEventType {
  DEAD_LETTER,
  MAX_RETRY_REACHED,
  NON_RETRYABLE_FAILED,
  TAKEOVER,
  LEASE_RENEW_FAILED,
  PERSIST_FAILED,
  ENGINE_ERROR
}

// 事件严重级别
public enum Severity { INFO, WARNING, ERROR, CRITICAL }

```
### 4) 通知上下文
```JAVA
public class NotifyContext {
    private NotifyEventType type;
    private String nodeId;
    private String bizType;
    private String taskId;
    private String tenantId;
    private Integer retryCount;
    private Integer maxRetry;
    // 自定义分类码，如 TIMEOUT/NO_HANDLER/SERDE_ERROR
    private String reasonCode;
    // 可被截断/脱敏
    private String lastError;
    // 事件发生时间
    private Instant when;
    // 额外字段：shardKey、owner、fence、nextTriggerTime 等
    private Map<String, Object> attributes ;
}
```

### 5) 通知上下文构造工具类
```JAVA
public final class NotifyContexts {

    private static final int MAX_ERROR_LEN = 4000;

    private NotifyContexts() {}

    /* ========== 对外入口（使用系统UTC时钟） ========== */

    public static NotifyContext ctxForDlq(String nodeId, RetryTaskEntity t, Throwable e, String reasonCode) {
        return ctxForDlq(nodeId, t, e, reasonCode, Clock.systemUTC().withZone(ZoneOffset.ofHours(8)).withZone(ZoneOffset.ofHours(8)));
    }

    public static NotifyContext ctxForMaxRetry(String nodeId, RetryTaskEntity t, Throwable e) {
        return ctxForMaxRetry(nodeId, t, e, Clock.systemUTC().withZone(ZoneOffset.ofHours(8)));
    }

    public static NotifyContext ctxForNonRetryable(String nodeId, RetryTaskEntity t, Throwable e) {
        return ctxForNonRetryable(nodeId, t, e, Clock.systemUTC().withZone(ZoneOffset.ofHours(8)));
    }

    public static NotifyContext ctxForTakeover(
            String newOwnerNodeId, String taskId, String bizType, String tenantId,
            String oldOwnerNodeId, long oldFence, long newFence) {
 