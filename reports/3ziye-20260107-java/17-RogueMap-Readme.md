<div align="center">
  <img src="static/img/logo.svg" alt="RogueMap Logo" width="120" height="120">
  <h1>RogueMap</h1>
</div>

<div align="center">

[![License](https://img.shields.io/badge/license-Apache%202-blue.svg)](LICENSE)
[![Java](https://img.shields.io/badge/Java-8%2B-orange.svg)](https://www.oracle.com/java/)
[![Version](https://img.shields.io/badge/version-1.0.0--BETA1-green.svg)](https://github.com/bryan31/RogueMap)

</div>

**RogueMap** 是一个高性能的嵌入式键值存储引擎，突破 HashMap 的内存墙，提供堆外内存和持久化存储能力。

## 🎯 为什么选择 RogueMap？

### HashMap 的困境

在处理大规模数据时，传统的 HashMap 面临诸多限制：

- ❌ **内存瓶颈** - 所有数据必须存储在堆内存，受 JVM 堆大小限制
- ❌ **GC 压力** - 百万级对象导致 Full GC 频繁，影响应用稳定性
- ❌ **数据易失** - 进程重启后数据全部丢失，无持久化能力
- ❌ **容量受限** - 超大数据集（10GB+）无法处理，OutOfMemoryError 噩梦
- ❌ **冷启动慢** - 每次启动都需要重新加载数据，耗时数分钟甚至更久

### RogueMap 的突破

RogueMap 将数据存储在 **堆外内存** 或 **内存映射文件** 中，让你享受 HashMap 的简单 API，同时获得超越其限制的能力：

- ✅ **无限容量** - 突破 JVM 堆限制，轻松处理 100GB+ 数据集
- ✅ **零 GC 压力** - 堆内存占用减少 **84.7%**，告别 Full GC 噩梦
- ✅ **数据持久化** - 进程重启后数据自动恢复，零成本持久化
- ✅ **即开即用** - Mmap 模式秒级启动，无需预热加载
- ✅ **写入更快** - 写入性能提升 **1.45 倍**，仅写入索引，延迟序列化
- ✅ **临时存储** - 支持自动清理的临时文件模式，完美替代磁盘缓存

### 核心优势

| 特性 | HashMap | RogueMap |
|------|---------|----------|
| **数据容量** | 受限于堆大小（通常 < 10GB） | **无限制**，可达 TB 级 |
| **堆内存占用** | 100% | **仅 15.3%** |
| **GC 影响** | 严重（Full GC 秒级） | **几乎无影响** |
| **持久化** | ❌ 不支持 | ✅ 支持 |
| **进程重启** | 数据全部丢失 | **数据自动恢复** |
| **写性能** | 基准 | **1.45 倍提升** |
| **读性能** | 基准 | 约 1/4（反序列化开销） |
| **临时文件** | ❌ 不支持 | ✅ 自动清理 |

### 适用场景

**RogueMap 适合这些场景**：
- ✅ **写多读少** - 数据采集、日志聚合、指标统计
- ✅ **需要持久化** - 用户会话、应用状态、缓存数据
- ✅ **大数据集** - 数据量超过 JVM 堆大小限制
- ✅ **GC 敏感** - 对 Full GC 停顿零容忍的实时系统
- ✅ **临时数据处理** - 海量临时数据暂存，自动清理避免泄露

**RogueMap 不适合这些场景**：
- ❌ **读密集型** - 如果你的应用是读多写少，HashMap 或 Caffeine 更合适
- ❌ **微秒级延迟** - 如果需要极致的读取性能，纯内存方案更好
- ❌ **小数据集** - 数据量 < 1GB 时，HashMap 的简单性更有优势

## ✨ 特性

- ✅ **多种存储模式** - 支持 堆外内存、内存映射文件、内存映射临时文件 三种模式
- ✅ **持久化支持** - Mmap 模式支持数据持久化到磁盘，支持自动恢复
- ✅ **临时文件模式** - 支持自动清理的临时文件存储
- ✅ **零拷贝序列化** - 原始类型直接内存布局，无序列化开销
- ✅ **高并发支持** - 分段锁设计（64 个段），StampedLock 乐观锁优化
- ✅ **智能内存分配** - Slab Allocator 减少内存碎片
- ✅ **多种索引结构** - 支持 HashIndex、SegmentedHashIndex、LongPrimitiveIndex、IntPrimitiveIndex
- ✅ **类型安全** - 泛型支持，编译时类型检查
- ✅ **零依赖** - 核心库无第三方依赖

## 🚀 快速开始

### Maven 依赖

```xml
<dependency>
    <groupId>com.yomahub</groupId>
    <artifactId>roguemap</artifactId>
    <version>1.0.0-BETA2</version>
</dependency>
```

### 基本使用

#### OffHeap 模式（堆外内存）

```java
import com.yomahub.roguemap.RogueMap;
import com.yomahub.roguemap.serialization.PrimitiveCodecs;
import com.yomahub.roguemap.serialization.StringCodec;

// 创建一个 String -> Long 的堆外内存 Map
try (RogueMap<String, Long> map = RogueMap.<String, Long>offHeap()
        .keyCodec(StringCodec.INSTANCE)
        .valueCodec(PrimitiveCodecs.LONG)
        .maxMemory(100 * 1024 * 1024) // 100MB
        .build()) {

    // 存储数据
    map.put("user1", 1000L);
    map.put("user2", 2000L);

    // 读取数据
    Long score = map.get("user1");
    System.out.println("Score: " + score);

    // 更新数据
    map.put("user1", 1500L);

    // 删除数据
    map.remove("user2");

    // 检查存在
    boolean exists = map.containsKey("user1");

    // 获取大小
    int size = map.size();
}
```

#### Mmap 临时文件模式

```java
// 自动创建临时文件，JVM 关闭后自动删除
RogueMap<Long, Long> tempMap = RogueMap.<Long, Long>mmap()
    .temporary()
    .allocateSize(500 * 1024 * 1024L)
    .keyCodec(PrimitiveCodecs.LONG)
    .valueCodec(PrimitiveCodecs.LONG)
    .build();
```

#### Mmap 模式（持久化存储）

```java
// 第一次：创建并写入数据
RogueMap<String, Long> map1 = RogueMap.<String, Long>mmap()
    .persistent("data/scores.db")
    .allocateSize(1024 * 1024 * 1024L)  // 1GB
    .keyCodec(StringCodec.INSTANCE)
    .valueCodec(PrimitiveCodecs.LONG)
    .build();

map1.put("alice", 100L);
map1.put("bob", 200L);
map1.flush();  // 刷新到磁盘
map1.close();

// 第二次：重新打开并恢复数据
RogueMap<String, Long> map2 = RogueMap.<String, Long>mmap()
    .persistent("data/scores.db")
    .keyCodec(StringCodec.INSTANCE)
    .valueCodec(PrimitiveCodecs.LONG)
    .build();

long score = map2.get("alice");  // 100L（从磁盘恢复）
map2.close();
```

### 支持的数据类型

RogueMap 提供了零拷贝的原始类型编解码器：

```java
// Long 类型（高性能）
RogueMap<Long, Long> longMap = RogueMap.<Long, Long>offHeap()
    .keyCodec(PrimitiveCodecs.LONG)
    .valueCodec(PrimitiveCodecs.LONG)
    .build();

// Integer 类型
RogueMap<Integer, Integer> intMap = RogueMap.<Integer, Integer>offHeap()
    .keyCodec(PrimitiveCodecs.INTEGER)
    .valueCodec(PrimitiveCodecs.INTEGER)
    .build();

// String 类型
RogueMap<String, String> stringMap = RogueMap.<String, String>offHeap()
    .keyCodec(StringCodec.INSTANCE)
    .valueCodec(StringCodec.INSTANCE)
    .build();

// 混合类型
RogueMap<String, Double> mixedMap = RogueMap.<String, Double>offHeap()
    .keyCodec(StringCodec.INSTANCE)
    .valueCodec(PrimitiveCodecs.DOUBLE)
    .build();
```

**支持的原始类型**：`Long`, `Integer`, `Double`, `Float`, `Short`, `Byte`, `Boolean`

如果是对象类型，RogueMap也提供了对象的编码解析器：

```java
// 对象类型
RogueMap<Long, Long> longMap = RogueMap.<String, YourObject>offHeap(