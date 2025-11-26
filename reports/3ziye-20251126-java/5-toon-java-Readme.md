# JToon – TOON Format for Java

[![Build](https://github.com/toon-format/toon-java/actions/workflows/build.yml/badge.svg)](https://github.com/toon-format/toon-java/actions/workflows/build.yml)
[![Release](https://github.com/toon-format/toon-java/actions/workflows/release.yml/badge.svg)](https://github.com/toon-format/toon-java/actions/workflows/release.yml)
[![Maven Central](https://img.shields.io/maven-central/v/dev.toonformat/jtoon.svg)](https://central.sonatype.com/artifact/dev.toonformat/jtoon)
![Coverage](.github/badges/jacoco.svg)

> **⚠️ Beta Status (v1.x.x):** This library is in active development and working towards spec compliance. Beta published to Maven Central. API may change before 2.0.0 release.

Compact, human-readable serialization format for LLM contexts with **30-60% token reduction** vs JSON. Combines YAML-like indentation with CSV-like tabular arrays. Working towards full compatibility with the [official TOON specification](https://github.com/toon-format/spec).

**Key Features:** Minimal syntax • TOON Encoding and Decoding • Tabular arrays for uniform data • Array length validation • Java 17 • Comprehensive test coverage.

## Installation

### Maven Central

JToon is available on Maven Central. Add it to your project using your preferred build tool:

**Gradle (Groovy DSL):**

```gradle
dependencies {
    implementation 'dev.toonformat:jtoon:1.0.5'
}
```

**Gradle (Kotlin DSL):**

```kotlin
dependencies {
    implementation("dev.toonformat:jtoon:1.0.5")
}
```

**Maven:**

```xml
<dependency>
    <groupId>dev.toonformat</groupId>
    <artifactId>jtoon</artifactId>
    <version>1.0.5</version>
</dependency>
```

> **Note:** See the [latest version](https://central.sonatype.com/artifact/dev.toonformat/jtoon) on Maven Central (also shown in the badge above).

### Alternative: Manual Installation

You can also download the JAR directly from the [GitHub Releases](https://github.com/toon-format/toon-java/releases) page and add it to your project's classpath.

## Quick Start

```java
import dev.toonformat.jtoon.JToon;
import java.util.*;

record User(int id, String name, List<String> tags, boolean active, List<?> preferences) {}
record Data(User user) {}

User user = new User(123, "Ada", List.of("reading", "gaming"), true, List.of());
Data data = new Data(user);

System.out.println(JToon.encode(data));
```

**Output:**

```
user:
  id: 123
  name: Ada
  tags[2]: reading,gaming
  active: true
  preferences[0]:
```

## Type Conversions

Some Java-specific types are automatically normalized for LLM-safe output:

| Input Type                  | Output                                                     |
| --------------------------- | ---------------------------------------------------------- |
| Number (finite)             | Decimal form; `-0` → `0`; whole numbers as integers        |
| Number (`NaN`, `±Infinity`) | `null`                                                     |
| `BigInteger`                | Integer if within Long range, otherwise string (no quotes) |
| `BigDecimal`                | Decimal number                                             |
| `LocalDateTime`             | ISO date-time string in quotes                             |
| `LocalDate`                 | ISO date string in quotes                                  |
| `LocalTime`                 | ISO time string in quotes                                  |
| `ZonedDateTime`             | ISO zoned date-time string in quotes                       |
| `OffsetDateTime`            | ISO offset date-time string in quotes                      |
| `Instant`                   | ISO instant string in quotes                               |
| `java.util.Date`            | ISO instant string in quotes                               |
| `Optional<T>`               | Unwrapped value or `null` if empty                         |
| `Stream<T>`                 | Materialized to array                                      |
| `Map`                       | Object with string keys                                    |
| `Collection`, arrays        | Arrays                                                     |

## API

### `JToon.encode(Object value): String`

### `JToon.encode(Object value, EncodeOptions options): String`

### `JToon.encodeJson(String json): String`

### `JToon.encodeJson(String json, EncodeOptions options): String`

Converts any Java object or JSON-string to TOON format.

**Parameters:**

- `value` – Any Java object (Map, List, primitive, or nested structure). Non-serializable values are converted to `null`. Java temporal types are converted to ISO strings, Optional is unwrapped, and Stream is materialized.
- `options` – Optional encoding options (`EncodeOptions` record):
  - `indent` – Number of spaces per indentation level (default: `2`)
  - `delimiter` – Delimiter enum for array values and tabular rows: `Delimiter.COMMA` (default), `Delimiter.TAB`, or `Delimiter.PIPE`
  - `lengthMarker` – Boolean to prefix array lengths with