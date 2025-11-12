![TOON logo with step‑by‑step guide](./.github/og.png)

# JToon - Token-Oriented Object Notation (TOON)

[![Build](https://github.com/felipestanzani/jtoon/actions/workflows/build.yml/badge.svg)](https://github.com/felipestanzani/jtoon/actions/workflows/build.yml)
[![Release](https://github.com/felipestanzani/jtoon/actions/workflows/release.yml/badge.svg)](https://github.com/felipestanzani/jtoon/actions/workflows/release.yml)
[![Maven Central](https://img.shields.io/maven-central/v/com.felipestanzani/jtoon.svg)](https://central.sonatype.com/artifact/com.felipestanzani/jtoon)

**Token-Oriented Object Notation** is a compact, human-readable format designed for passing structured data to Large Language Models with significantly reduced token usage.

TOON excels at **uniform complex objects** – multiple fields per row, same structure across items. It borrows YAML's indentation-based structure for nested objects and CSV's tabular format for uniform data rows, then optimizes both for token efficiency in LLM contexts.

## Why TOON?

AI is becoming cheaper and more accessible, but larger context windows allow for larger data inputs as well. **LLM tokens still cost money** – and standard JSON is verbose and token-expensive:

```json
{
  "users": [
    { "id": 1, "name": "Alice", "role": "admin" },
    { "id": 2, "name": "Bob", "role": "user" }
  ]
}
```

TOON conveys the same information with **fewer tokens**:

```
users[2]{id,name,role}:
  1,Alice,admin
  2,Bob,user
```

*Test the differences on [THIS online playground](https://www.curiouslychase.com/playground/format-tokenization-exploration)*

<details>
<summary>Another reason</summary>

[![xkcd: Standards](https://imgs.xkcd.com/comics/standards_2x.png)](https://xkcd.com/927/)

</details>

## Benchmarks

> **Learn more:** For complete format specification, rules, and additional benchmarks, see [TOON-SPECIFICATION.md](TOON-SPECIFICATION.md).

### Token Efficiency Example

TOON typically achieves **30–60% fewer tokens than JSON**. Here's a quick summary:

```
Total across 4 datasets        ████████████░░░░░░░░░░░░░  13,418 tokens
                               vs JSON: 26,379  💰 49.1% saved
                               vs XML:  30,494  💰 56.0% saved
```

**See [TOON-SPECIFICATION.md](TOON-SPECIFICATION.md#benchmarks) for detailed benchmark results and LLM retrieval accuracy tests.**

## Installation

### Maven Central

JToon is available on Maven Central. Add it to your project using your preferred build tool:

**Gradle (Groovy DSL):**

```gradle
dependencies {
    implementation 'com.felipestanzani:jtoon:0.1.2'
}
```

**Gradle (Kotlin DSL):**

```kotlin
dependencies {
    implementation("com.felipestanzani:jtoon:0.1.2")
}
```

**Maven:**

```xml
<dependency>
    <groupId>com.felipestanzani</groupId>
    <artifactId>jtoon</artifactId>
    <version>0.1.2</version>
</dependency>
```

> **Note:** See the [latest version](https://central.sonatype.com/artifact/com.felipestanzani/jtoon) on Maven Central (also shown in the badge above).

### Alternative: Manual Installation

You can also download the JAR directly from the [GitHub Releases](https://github.com/felipestanzani/jtoon/releases) page and add it to your project's classpath.

## Quick Start

```java
import com.felipestanzani.jtoon.JToon;
import java.util.*;

record User(int id, String name, List<String> tags, boolean active, List<?> preferences) {}
record Data(User user) {}

User user = new User(123, "Ada", List.of("reading", "gaming"), true, List.of());
Data data = new Data(user);

System.out.println(JToon.encode(data));
```

Output:

```
user:
  id: 123
  name: Ada
  tags[2]: reading,gaming
  active: true
  preferences[0]:
```

## TOON Format Basics

> **Complete specification:** For detailed formatting rules, quoting rules, and comprehensive examples, see [TOON-SPECIFICATION.md](TOON-SPECIFICATION.md).

TOON uses indentation-based structure (like YAML) combined with efficient tabular format for uniform arrays (like CSV):

**Simple objects:**

```
id: 123
name: Ada
```

**Nested objects:**

```
user:
  id: 123
  name: Ada
```

**Primitive arrays:**

```
tags[3]: admin,ops,dev
```

**Tabular arrays** (uniform objects with same fields):

```
items[2]{sku,qty,price}:
  A1,2,9.99
  B2,1,14.5
```

## Type Conversions

Some Java-specific types are automatically normalized for LLM-safe output:

| Input Type | Output |
|---|---|
| Number (finite) | Decimal form; `-0` → `0`; whole numbers as integers |
| Number (`NaN`, `±Infinity`) | `null` |
| `BigInteger` | Integer if within Long range, otherwise string (no quotes) |
| `BigDecimal` | Decimal number |
| `LocalDateTime` | ISO date-time string in quotes |
| `LocalDate` | ISO date string in quotes |
| `LocalTime` | ISO time string in quotes |
| `ZonedDateTime` | ISO zoned date-time string in quotes |
| `OffsetDateTime` | ISO offset date-time string in quotes |
| `Instant` | ISO instant string in quotes |
| `java.util.Date` | ISO instant string in quotes |
| `Optional<T>` 