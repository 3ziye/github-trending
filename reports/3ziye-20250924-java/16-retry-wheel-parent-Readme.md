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
### 5) 代码中投递任务
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

---

## 已实现/待完善/未实现

> ✅ 已实现或具备完整骨架；🟨 已实现核心功能但待完善；⬜️ 待实现.

### Starter 与自动装配
✅ Spring Boot 3.x Starter 形态，自动装配引擎、扫描器、定时轮、默认 SPI(支持覆盖).  
✅ RetryWheelProperties 配置映射（轮盘、扫描、执行器、回退、粘滞租约等）.  

### 调度与执行

✅ Netty HashedWheelTimer 初始化，tick 与槽数可配.  
✅ 扫描器：DB 拉取到期任务 → 抢占（或接管）→ 投递本地执行.  
✅ 执行器：业务线程池可配；采用CompletableFuture 链路 + Timeout机制，异步链路不吞异常.  
✅ 失败回退：固定/指数退避（含 jitter） + BackoffRegistry SPI（自定义）.  
⬜️ 优雅停机：释放本机持有任务 RUNNING→PENDING（next=now()）或允许自然到期接管.  

### 泛型与序列化/失败判定

✅ 提供默认PayloadSerializer（Jackson）实现, 可自定实现覆盖.  
✅ FailureDecider（默认需要重试）：业务基于异常类型与业务返回值判断是否需要重试.  

### 粘滞租约

✅ 表结构新增：owner_node_id、lease_expire_at、fence_token；索引 idx_retry_task_lease.    
✅ 首次抢占：PENDING→RUNNING 同步设置 owner/lease/fence 并挂入本地时间轮.    
✅ 本地重试：保持 RUNNING 与 owner 不变，仅回写 retry_count/next_trigger_time/last_error.   
✅ 接管：lease_expire_at<=now() 条件抢占，其他节点安全接手.   

### 可观测性与运维

🟨 Micrometer 指标：入队、成功、失败、DLQ、重试次数分布、执行时长等；空 MeterRegistry 使用默认/Noop 指标实现保障无侵入.  
⬜️ Actuator 端点：到期积压、线程池使用、各状态计数等.  
⬜️ 管理 REST：查询、暂停/恢复、取消、手动重试、DLQ 拉回（如已暴露基础接口）.  
⬜️ 审计日志：关键状态变更/接管/续约/异常栈保留与截断.  

### 告警通知

✅ 告警通知器 SPI：DLQ、接管失败、续约失败突增等触发器.  

### 多租户/分片

⬜️ 多租户/分片策略 SPI：tenant_id/shard_key 参与扫描与限流；提供路由器扩展点.  






# retry-notify (通知模块)

> 为重试框架提供 **可插拔、可路由、可限流、可观测** 的通知能力。支持单条通知，覆盖 DLQ、最大重试、不可重试失败、接管、续约失败、引擎异常、持久化异常等事件。

---

## 特性

- **SPI 可插拔**：`Notifier` 接口，内置 `LoggingNotifier`，支持自定义（如 飞书/钉钉/Slack）。
- **异步派发**：`AsyncNotifyingService` 独立线程池 + 指数退避重试，不阻塞主流程。
- **路由/过滤**：按事件/租户/业务/严重级别路由到不同通道；内置限流过滤器。
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
    private String 