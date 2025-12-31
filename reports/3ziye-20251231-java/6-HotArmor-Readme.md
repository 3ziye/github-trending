<div align="center">

[English](README.md) | [简体中文](README-ZH.md)

</div>

---

<div align="center">

# HotArmor 🛡️

**Intelligent Hotspot Data Protection Framework · Solving High-Concurrency Cache Penetration**

*One annotation, automatic promotion of hotspot data to local cache*

[![Java](https://img.shields.io/badge/Java-1.8+-orange.svg)](https://www.oracle.com/java/technologies/javase-downloads.html)
[![Spring Boot](https://img.shields.io/badge/Spring%20Boot-2.3.12-brightgreen.svg)](https://spring.io/projects/spring-boot)
[![Sentinel](https://img.shields.io/badge/Sentinel-1.8.6-blue.svg)](https://sentinelguard.io/)
[![License](https://img.shields.io/badge/license-Apache%202-blue.svg)](LICENSE)

</div>

---

## 💡 What Problem Does It Solve?

**HotArmor** is a hotspot data protection middleware designed for high-concurrency scenarios. In flash sales, trending events, and similar scenarios, a small number of hotspot data (such as popular products or trending topics) can cause serious performance issues:

| Problem | Typical Scenario | Technical Impact | HotArmor Solution |
|---------|-----------------|------------------|-------------------|
| ⚡ **Cache Breakdown** | Moment when hot key expires | Thousands of requests simultaneously bypass cache and hit database, overwhelming DB | L4 distributed lock + Double-Check ensures single-point source loading |
| 🔥 **Hotspot Overload** | Celebrity products frequently accessed | Redis connection pool exhausted, bandwidth saturated, slow response | L1-L3 intelligently identifies hotspots and promotes to local cache (microsecond level) |
| 🔄 **Distributed Cache Consistency** | Multi-node cluster deployment | Node A updates data, nodes B/C/D have stale local cache causing dirty reads | Pub/Sub invalidation broadcast + hotspot promotion broadcast, full-node synchronization |
| 🗑️ **DB-Cache Consistency** | High-concurrency read-write race conditions | After updating DB and deleting cache, concurrent queries write old data back to Redis | Delayed double-delete strategy eliminates write-after-read race window |

## 🚀 Core Features

```java
// Just one annotation, framework handles hotspot protection automatically
@HotArmorCache(resource = "product:detail", key = "#id")
public Product getProduct(Long id) {
    return productMapper.selectById(id);  // Hotspot data automatically promoted to local cache
}
```

- ✨ **Out-of-the-Box** - Declarative annotation usage, zero-intrusion integration
- 🧠 **Intelligent Recognition** - Based on Sentinel's hotspot parameter flow control, precise hotspot identification
- 🔄 **Four-Level Protection** - L1 Local Cache → L2 Noise Filter → L3 Hotspot Detection → L4 Safe Source Loading
- 📡 **Eventual Consistency** - Delayed double-delete + Redis Pub/Sub broadcast ensures cluster cache synchronization
- ⚡ **Ultimate Performance** - Hotspot data from Redis millisecond-level → Caffeine microsecond-level response

---

## 🏗️ Architecture Design

### System Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                        Application Layer                            │
│                                                                     │
│    @HotArmorCache(resource="...", key="...")  ← Query cache         │
│    @HotArmorEvict(resource="...", key="...")  ← Invalidate cache    │
└──────────────────────────┬──────────────────────────────────────────┘
                           │
                           │ AOP Interception
                           ↓
┌─────────────────────────────────────────────────────────────────────┐
│                      HotArmor Core Engine                            │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │                    Aspect Layer                                │ │
│  │  • HotArmorAspect - AOP interceptor                            │ │
│  │  • SpEL expression parser - Parse key/condition                │ │
│  │  • HotArmorContext - Request context object                    │ │
│  └─────────────────────────┬─────────────────────────────────────┘ │
│                            ↓                                        │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │                 Handler Layer                                  │ │
│  │  • DefaultHotArmorAspectHandler                                │ │
│  │    - handleCache() : Read flow four-level funnel               │ │
│  │    - handleEvict() : Write flow cache invalidation             │ │
│  └─────────────────────────┬─────────────────────────────────────┘ │
│                            ↓                                        │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │                  Data Plane                                    │ │
│  │                                                               │ │
│  │  ┌─────────────────────────────────────