
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

Zen C uses type inference by default.

```zc
var x = 42;                 // Inferred as int
const PI = 3.14159;         // Compile-time constant
var explicit: float = 1.0;  // Explicit type
```

#### Mutability
By default, variables are mutable. You can enable **Immutable by Default** mode using a directive.

```zc
//> immutable-by-default

var x = 10;
// x = 20; // Error: x is immutable

var mut y = 10;
y = 20;    // OK
```

### 2. Primitive Types

| Type | C Equivalent | Description |
|:---|:---|:---|
| `int`, `uint` | `int`, `unsigned int` | Platform standard integer |
| `I8` .. `I128` or `i8` .. `i128` | `int8_t` .. `__int128_t` | Signed fixed-width integers |
| `U8` .. `U128` or `u8` .. `u128` | `uint8_t` .. `__uint128_t` | Unsigned fixed-width integers |
| `isize`, `usize` | `ptrdiff_t`, `size_t` | Pointer-sized integers |
| `byte` | `uint8_t` | Alias for U8 |
| `F32`, `F64` or `f32`, `f64`  | `float`, `double` | Floating point numbers |
| `bool` | `bool` | `true` or `false` |
| `char` | `char` | Single character |
| `string` | `char*` | C-string (null-terminated) |
| `U0`, `u0`, `void` | `void` | Empty type |

### 3. Aggregate Types

#### Arrays
Fixed-size arrays with value semantics.
```zc
var ints: int[5] = {1, 2, 3, 4, 5};
var zeros: [int; 5]; // Zero-initialized
```

#### Tuples
Group multiple values together.
```zc
var pair = (1, "Hello");
var x = pair.0;
var s = pair.1;
```

#### Structs
Data structures with optional bitfields.
```zc
struct Point {
    x: int;
    y: int;
}

// Struct initialization
var p = Point { x: 10, y: 20 };

// Bitfields
struct Flags {
    valid: U8 : 1;
    mode:  U8 : 3;
}
```

#### Enums
Tagged unions (Sum types) capable of holding data.
```zc
enum Shape {
    Circle(float),      // Holds radius
    Rect(float, float), // Holds width, height
    Point               // No data
}
```

#### Unions
Standard C unions (unsafe access).
```zc
union Data {
    i: int;
    f: float;
}

#### Type Aliases
Create a new name for an existing type.
```zc
alias ID = int;
alias PointMap = Map<string, Point>;
```
```

### 4. Functions & Lambdas

#### Functions
```zc
fn add(a: int, b: int) -> int {
    return a + b;
}

// Named arguments supported in calls
add(a: 10, b: 20);
```

#### Lambdas (Closures)
Anonymous functions that can capture their environment.
```zc
var factor = 2;
var double = x -> x * factor;  // Arrow syntax
var full = fn(x: int) -> int { return x * factor; }; // Block syntax
```

### 5. Control Flow

#### Conditionals
```zc
if x > 10 {
    print("Large");
} else if x > 5 {
    print("Medium");
} else {
    print("Small");
}

// Ternary
var y = x > 10 ? 1 : 0;
```

#### Pattern Matching
Powerful alternative to `switch`.
```zc
match val {
    1 => print("One"),
    2 | 3 => print("Two or Three"),
    4..10 => print("Range"),
    _ => print("Other")
}

// Destructuring Enums
match shape {
    Circle(r) => print(f"Radius: {r}"),
    Rect(w, h) => print(f"Area: {w*h}"),
    Point => print("Point")
}
```

#### Loops
```zc
// Range
for i in 0..10 { ... }
for i in 0..10 step 2 { ... }

// Iterator/Collection
for item in vec { ... }

// While
while x < 10 { ... }

// Infinite with label
outer: loop {
    if done { break outer; }
}

// Repeat
repeat 5 { ... }
```

#### Advanced Control
```zc
// Guard: Execute else and return if condition is false
guard ptr != NULL else { return; }

// Unless: If not true
unless is_valid { return; }
```

### 6. Operators

| Operator | Description | Function Mapping |
|:---|:---|:---|
| `+`, `-`, 