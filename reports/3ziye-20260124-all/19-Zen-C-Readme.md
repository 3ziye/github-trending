
<div align="center">

# Zen C

**Modern Ergonomics. Zero Overhead. Pure C.**

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)]()
[![License](https://img.shields.io/badge/license-MIT-blue)]()
[![Version](https://img.shields.io/badge/version-0.1.0-orange)]()
[![Platform](https://img.shields.io/badge/platform-linux-lightgrey)]()

*Write like a high-level language, run like C.*

</div>

---

## Overview

**Zen C** is a modern systems programming language that compiles to human-readable `GNU C`/`C11`. It provides a rich feature set including type inference, pattern matching, generics, traits, async/await, and manual memory management with RAII capabilities, all while maintaining 100% C ABI compatibility.

## Community

Join the discussion, share demos, ask questions, or report bugs in the official Zen C Discord server!

- Discord: [Join here](https://discord.com/invite/q6wEsCmkJP)

---

## Index

- [Overview](#overview)
- [Community](#community)
- [Quick Start](#quick-start)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Environment Variables](#environment-variables)
- [Language Reference](#language-reference)
    - [1. Variables and Constants](#1-variables-and-constants)
    - [2. Primitive Types](#2-primitive-types)
    - [3. Aggregate Types](#3-aggregate-types)
        - [Arrays](#arrays)
        - [Tuples](#tuples)
        - [Structs](#structs)
        - [Enums](#enums)
        - [Unions](#unions)
        - [Type Aliases](#type-aliases)
    - [4. Functions & Lambdas](#4-functions--lambdas)
        - [Functions](#functions)
        - [Const Arguments](#const-arguments)
        - [Default Arguments](#default-arguments)
        - [Lambdas (Closures)](#lambdas-closures)
        - [Variadic Functions](#variadic-functions)
    - [5. Control Flow](#5-control-flow)
        - [Conditionals](#conditionals)
        - [Pattern Matching](#pattern-matching)
        - [Loops](#loops)
        - [Advanced Control](#advanced-control)
    - [6. Operators](#6-operators)
        - [Overloadable Operators](#overloadable-operators)
        - [Syntactic Sugar](#syntactic-sugar)
    - [7. Printing and String Interpolation](#7-printing-and-string-interpolation)
        - [Keywords](#keywords)
        - [Shorthands](#shorthands)
        - [String Interpolation (F-strings)](#string-interpolation-f-strings)
        - [Input Prompts (`?`)](#input-prompts-)
    - [8. Memory Management](#8-memory-management)
        - [Defer](#defer)
        - [Autofree](#autofree)
        - [Resource Semantics (Move by Default)](#resource-semantics-move-by-default)
        - [RAII / Drop Trait](#raii--drop-trait)
    - [9. Object Oriented Programming](#9-object-oriented-programming)
        - [Methods](#methods)
        - [Traits](#traits)
        - [Standard Traits](#standard-traits)
        - [Composition](#composition)
    - [10. Generics](#10-generics)
    - [11. Concurrency (Async/Await)](#11-concurrency-asyncawait)
    - [12. Metaprogramming](#12-metaprogramming)
        - [Comptime](#comptime)
        - [Embed](#embed)
        - [Plugins](#plugins)
        - [Generic C Macros](#generic-c-macros)
    - [13. Attributes](#13-attributes)
    - [14. Inline Assembly](#14-inline-assembly)
        - [Basic Usage](#basic-usage)
        - [Volatile](#volatile)
        - [Named Constraints](#named-constraints)
    - [15. Build Directives](#15-build-directives)
- [Standard Library](#standard-library)
- [Tooling](#tooling)
    - [Language Server (LSP)](#language-server-lsp)
    - [REPL](#repl)
- [Compiler Support & Compatibility](#compiler-support--compatibility)
    - [Test Suite Status](#test-suite-status)
    - [Building with Zig](#building-with-zig)
    - [C++ Interop](#c-interop)
    - [CUDA Interop](#cuda-interop)
- [Contributing](#contributing)
- [Attributions](#attributions)

---

## Quick Start

### Installation

```bash
git clone https://github.com/z-libs/Zen-C.git
cd Zen-C
make
sudo make install
```

### Usage

```bash
# Compile and run
zc run hello.zc

# Build executable
zc build hello.zc -o hello

# Interactive Shell
zc repl
```

### Environment Variables

You can set `ZC_ROOT` to specify the location of the Standard Library (standard imports like `import "std/vector.zc"`). This allows you to run `zc` from any directory.

```bash
export ZC_ROOT=/path/to/Zen-C
```

---

## Language Reference

### 1. Variables and Constants

Zen C distinguishes between compile-time constants and runtime variables.

#### Manifest Constants (`def`)
Values that exist only at compile-time (folded into code). Use these for array sizes, fixed configuration, and magic numbers.

```zc
def MAX_SIZE = 1024;
var buffer: char[MAX_SIZE]; // Valid array size
```

#### Variables (`var`)
Storage locations in memory. Can be mutable or read-only (`const`).

```zc
var x = 10;             // Mutable
x = 20;                 // OK

var y: const int = 10;  // Read-only (Type qualified)
// y = 20;              // Error: cannot assign to const
```
