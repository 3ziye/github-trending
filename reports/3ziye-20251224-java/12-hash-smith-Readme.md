# HashSmith: Fast & memory efficient hash tables for Java

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Maven Central](https://img.shields.io/maven-central/v/io.github.bluuewhale/hashsmith.svg)](https://central.sonatype.com/artifact/io.github.bluuewhale/hashsmith)
[![javadoc](https://javadoc.io/badge2/io.github.bluuewhale/hashsmith/javadoc.svg)](https://javadoc.io/doc/io.github.bluuewhale/hashsmith)
[![Status: experimental](https://img.shields.io/badge/status-experimental-orange.svg)](#overview)

> ⚠️ This project is experimental and not ready for production use.

<p align="center">
  <img src="images/logo.png" alt="HashSmith logo" width="330">
</p>


## Overview
- HashSmith provides multiple high-performance hash table implementations optimized for speed and memory efficiency on modern JVMs.
- Focus areas: SWAR-probing (`SwissMap`), SIMD-probing (`SwissSimdMap`), predictable probe lengths (Robin Hood), and minimal per-entry overhead.
- Built for JDK 21+; `SwissSimdMap` uses the incubating Vector API for SIMD acceleration.
- More memory-efficient than the built-in JDK `HashMap`; performance depends on workload.

## Implementations
- **SwissMap**: SwissTable-inspired design using SWAR control-byte probing (no Vector API) with tombstone reuse. Default map.
- **SwissSimdMap**: SIMD (Vector API incubator) variant of SwissMap with vectorized control-byte probing. See `docs/SwissSimdMap.md` for details.
- **ConcurrentSwissMap**: sharded, thread-safe wrapper around `SwissMap` using per-shard `StampedLock` (null keys not supported).
- **SwissSet**: SwissTable-style hash set with SIMD control-byte probing, tombstone reuse, and null-element support 

### Why SWAR by default?
Vector API is still incubating, and profiling on my setup showed the SIMD path taking longer than expected, so the default `SwissMap` favors a SWAR probe. Numbers can differ significantly by hardware/JVM version; please run your own benchmarks if you plan to use `SwissSimdMap`.

## Blog / Write-up
- If you want a guided tour with design notes and benchmarks, see **[this write-up](https://bluuewhale.github.io/posts/building-a-fast-and-memory-efficient-hash-table-in-java-by-borrowing-the-best-ideas/)**.

## Quick Start
```java
import io.github.bluuewhale.hashsmith.SwissMap;      // SWAR
import io.github.bluuewhale.hashsmith.SwissSimdMap;  // Vector API
import io.github.bluuewhale.hashsmith.ConcurrentSwissMap;
import io.github.bluuewhale.hashsmith.RobinHoodMap;
import io.github.bluuewhale.hashsmith.SwissSet;

public class Demo {
    public static void main(String[] args) {
        // SwissMap (SWAR)
        var swiss = new SwissMap<String, Integer>();
        swiss.put("a", 1);
        swiss.put("b", 2);
        System.out.println(swiss.get("a")); // 1

        // SwissSimdMap (Vector API incubator)
        var swissSimd = new SwissSimdMap<String, Integer>();
        swissSimd.put("a", 1);
        swissSimd.put("b", 2);
        System.out.println(swissSimd.get("a")); // 1

        // ConcurrentSwissMap (sharded, thread-safe)
        var concurrentSwiss = new ConcurrentSwissMap<String, Integer>();
        concurrentSwiss.put("a", 1);
        concurrentSwiss.put("b", 2);
        System.out.println(concurrentSwiss.get("a")); // 1

        // SwissSet
        var swissSet = new SwissSet<String>();
        swissSet.add("k");
        swissSet.add(null); // nulls allowed
        System.out.println(swissSet.contains("k")); // true
    }
}
```

## Install
- Gradle (Kotlin DSL):
```kotlin
dependencies {
    implementation("io.github.bluuewhale:hashsmith:0.1.7")
}
```
- Gradle (Groovy):
```groovy
dependencies {
    implementation 'io.github.bluuewhale:hashsmith:0.1.7'
}
```
- Maven:
```xml
<dependency>
  <groupId>io.github.bluuewhale</groupId>
  <artifactId>hashsmith</artifactId>
  <version>0.1.7</version>
</dependency>
```

## Requirements
- JDK 21+ (`SwissSimdMap` needs `jdk.incubator.vector`)
- Gradle (wrapper provided)
- The JVM flag `--add-modules jdk.incubator.vector` is already configured for build, test, and JMH tasks that exercise `SwissSimdMap`.

## Build & Test
```bash
./gradlew build        # full build
./gradlew test         # JUnit 5 tests
```

## Memory Footprint 
- Compares retained heap for both maps (`HashMap` vs `SwissSimdMap` vs `SwissMap` vs fastutil `Object2ObjectOpenHashMap` vs Eclipse Collections `UnifiedMap`) and sets (`HashSet` vs `SwissSet` vs fastutil `ObjectOpenHashSet` vs Eclipse Collections `UnifiedSet`).
- Set benchmarks use UUID `String` keys (HashSet, SwissSet, ObjectOpenHashSet, UnifiedSet). Primitive-specialized collections (e.g., fastutil primitive sets) are excluded because their memory profile is driven by primitive storage, whereas these tests target general reference workloads.
### Results
- Maps: `SwissMap`/`SwissSimdMap` use open addressing to cut space; default load factor 0.875, up to 53.3% retained-heap reduction in payload-light cases vs `HashMap`.
- Sets: `SwissSet` (SwissHas