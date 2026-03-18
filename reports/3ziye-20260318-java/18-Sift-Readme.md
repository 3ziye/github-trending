# Sift
<img referrerpolicy="no-referrer-when-downgrade" src="https://static.scarf.sh/a.png?x-pxid=e931dfa9-02e9-406d-bde7-56f9e0000464" alt=""/>[![Java 8+](https://img.shields.io/badge/Java-8+-blue.svg)](https://adoptium.net/)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

[![Tests](https://github.com/mirkoddd/Sift/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/mirkoddd/Sift/actions)
[![Coverage](https://raw.githubusercontent.com/mirkoddd/Sift/main/.github/badges/jacoco.svg)](https://github.com/mirkoddd/Sift/actions)

**The Type-Safe Regex Builder for Java. If it compiles, it works.**

---

## The Problem

You've seen this before. Someone writes a regex, it works, and six months later nobody — including the author — can read it:

```java
// What does this even do?
Pattern p = Pattern.compile("^(?=[\\p{Lu}])[\\p{L}\\p{Nd}_]{3,15}+[0-9]?$");
```

You add a character class, break the balance of brackets, and find out at runtime. You copy a regex from Stack Overflow, miss an escape, and watch it fail silently in production. You duplicate the same validation pattern across DTOs and forget to update one of them.

**There is a better way.**

---

## The Solution

Sift is a fluent DSL that turns regex construction into readable, self-documenting Java code. Its state machine enforces grammatical correctness at **compile time** — if your pattern compiles, it is structurally valid.

```java
// The same pattern, written with Sift:
String regex = Sift.fromStart()
                .exactly(1).upperCaseLettersUnicode()   // Must start with an uppercase letter
                .then()
                .between(3, 15).wordCharactersUnicode().withoutBacktracking() // ReDoS-safe
                .then()
                .optional().digits()                    // May end with a digit
                .andNothingElse()
                .shake();

// Result: ^[\p{Lu}][\p{L}\p{Nd}_]{3,15}+[0-9]?$
```

Your IDE guides every step. Wrong transitions simply do not exist as methods.

---

## Installation
[![sift-core](https://img.shields.io/maven-central/v/com.mirkoddd/sift-core?label=sift-core)](https://central.sonatype.com/artifact/com.mirkoddd/sift-core)
[![sift-annotations](https://img.shields.io/maven-central/v/com.mirkoddd/sift-annotations?label=sift-annotations)](https://central.sonatype.com/artifact/com.mirkoddd/sift-annotations)

[![sift-engine-re2j](https://img.shields.io/maven-central/v/com.mirkoddd/sift-engine-re2j?label=sift-engine-re2j)](https://central.sonatype.com/artifact/com.mirkoddd/sift-engine-re2j)
[![sift-engine-graalvm](https://img.shields.io/maven-central/v/com.mirkoddd/sift-engine-graalvm?label=sift-engine-graalvm)](https://central.sonatype.com/artifact/com.mirkoddd/sift-engine-graalvm)

**Gradle:**
```groovy
// Core engine — zero external dependencies
implementation 'com.mirkoddd:sift-core:<latest>'

// Optional: Jakarta Validation / Hibernate Validator integration
implementation 'com.mirkoddd:sift-annotations:<latest>'


// Optional: Engine RE2J
implementation 'com.mirkoddd:sift-engine-re2j:<latest>'


// Optional: Engine GraalVM
implementation 'com.mirkoddd:sift-engine-graalvm:<latest>'
```

**Maven:**
```xml
<dependency>
    <groupId>com.mirkoddd</groupId>
    <artifactId>sift-core</artifactId>
    <version>latest</version>
</dependency>

<!-- Optional: Jakarta Validation / Hibernate Validator integration -->
<dependency>
    <groupId>com.mirkoddd</groupId>
    <artifactId>sift-annotations</artifactId>
    <version>latest</version>
</dependency>


<!-- Optional: Engine GraalVM -->
<dependency>
    <groupId>com.mirkoddd</groupId>
    <artifactId>sift-engine-graalvm</artifactId>
    <version>latest</version>
</dependency>


<!-- Optional: Engine RE2J -->
<dependency>
    <groupId>com.mirkoddd</groupId>
    <artifactId>sift-engine-re2j</artifactId>
    <version>latest</version>
</dependency>
```

> Sift targets **Java 8 bytecode** for maximum compatibility — including legacy Spring Boot 2.x and Android.

---

## Core Concepts

### Entry Points

| Method | Generates | Use when |
|---|---|---|
| `Sift.fromStart()` | `^...` | Validating an entire string |
| `Sift.fromAnywhere()` | `...` | Building reusable fragments or searching within text |
| `Sift.fromWordBoundary()` | `\b...` | Matching whole words |
| `Sift.fromPreviousMatchEnd()` | `\G...` | Iterative parsing |
| `Sift.filteringWith(flag)` | `(?i)...` | Global flags (case-insensitive, multiline, dotall) |

### Terminal Methods

| Method | Effect |
|---|---|
| `.shake()` | Returns the raw regex `String` |
| `.sieve()` | Compiles with the default JDK engine → `SiftCompiledPattern` |
| `.sieveWith(engine)` | Compiles with a custom engine → `SiftCompiledPattern` |
| `.andNothingElse()` | Appends `$` and seals the pattern |

---

## Examples

### 1. Modular Composition — The LEGO Brick Approach

The real power of Sift is the ability to name your building blocks and compose them. Every `Sift.fromAnywhere()` ca