# OtterLang 🦦

<p>
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://github.com/jonathanmagambo/otterlang/blob/main/image.png?raw=true" width="400">
      <img src="https://github.com/jonathanmagambo/otterlang/blob/main/image.png?raw=true" width="400" alt="OtterLang Logo" />
    </picture>
    <br>
    <strong>Simple syntax, native performance, transparent Rust FFI.</strong>
</p>

[![Build Status](https://github.com/jonathanmagambo/otterlang/workflows/CI/badge.svg)](https://github.com/jonathanmagambo/otterlang/actions)
[![Discord](https://img.shields.io/badge/Discord-Join%20Server-5865F2?style=flat&logo=discord&logoColor=white)](https://discord.gg/y3b4QuvyFk)

An indentation-sensitive programming language with an LLVM backend. OtterLang compiles to native binaries with a focus on simplicity and performance.

## Why OtterLang?

| Feature | OtterLang | Nim |
|---------|-----------|-----|
| **Transparent Rust FFI** | ✅ Auto-extracts entire public API | ❌ Manual bindings required |
| **Indentation-based Syntax** | ✅ Clean and readable | ✅ Similar |
| **LLVM Backend** | ✅ Native code generation | ✅ Also uses LLVM |
| **Memory Management** | ✅ Automatic GC + profiling | ✅ GC available |
| **Zero-cost Abstractions** | ✅ Direct LLVM compilation | ✅ Good |
| **Type Inference** | ✅ Full inference | ✅ Advanced |
| **Async/Await** | ✅ Built-in task system | ✅ Async/await |
| **Cross-compilation** | ✅ WASM, embedded targets | ✅ Good support |
| **REPL** | ✅ Interactive development | ❌ Limited |
| **Code Formatting** | ✅ Built-in formatter | ✅ Built-in |
| **Memory Profiling** | ✅ Built-in profiler | ❌ External tools |
| **Rust Ecosystem Access** | ✅ Transparent bridging | ❌ Manual bindings |
| **Compilation Speed** | ✅ Fast (LLVM) | ✅ Fast |
| **Runtime Performance** | ✅ Near C speed (1.28x) | ✅ Near C speed |

## Quick Start

```bash
git clone https://github.com/jonathanmagambo/otterlang.git
cd otterlang

# Option 1: Using Nix (recommended)
nix develop
cargo build --release

# Option 2: Using setup script
./setup.sh

# Create and run your first program
cat > hello.ot << 'EOF'
use otter:fmt

fn main():
    fmt.println("Hello from OtterLang!")
EOF

otter run hello.ot
```

## Installation

### Using Nix (Recommended)

```bash
nix develop
cargo build --release
```

The Nix flake automatically provides Rust nightly, LLVM 15, and all dependencies.

### Manual Setup

**Prerequisites:**
- Rust (via rustup) - nightly required for FFI features
- LLVM 15

**macOS:**
```bash
brew install llvm@15
export LLVM_SYS_150_PREFIX=$(brew --prefix llvm@15)
export PATH="$LLVM_SYS_150_PREFIX/bin:$PATH"
./setup.sh
```

**Ubuntu/Debian:**
```bash
sudo apt-get install -y llvm-15 llvm-15-dev clang-15
export LLVM_SYS_150_PREFIX=/usr/lib/llvm-15
./setup.sh
```

The setup script automatically installs Rust nightly and configures the project.

## Language Features

### Syntax

Clean indentation-based syntax with modern features:

```otter
use otter:fmt
use otter:math

fn greet(name: str) -> str:
    return "Hello, " + name + "!"

struct Point:
    x: float
    y: float

    fn distance(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y)

fn main():
    let message = greet("World")
    fmt.println(message)

    let p = Point(x=3.0, y=4.0)
    let dist = p.distance()
    fmt.println("Point: (" + stringify(p.x) + ", " + stringify(p.y) + "), distance: " + stringify(dist))

    if len(message) > 10:
        fmt.println("Long message")

    for i in 0..10:
        fmt.println(stringify(i))
```

### Transparent Rust FFI

Automatically use any Rust crate without manual configuration:

```otter
use rust:rand
use otter:fmt

fn main():
    let random = rand.random_f64()
    fmt.println("Random: " + stringify(random))
```

**Key advantages:**
- ✅ No manual bindings needed
- ✅ Automatic API extraction via rustdoc (requires Rust nightly)
- ✅ Memory management handled automatically
- ✅ Async/await support for Rust Futures
- ✅ Type checking integrated

See [docs/FFI_TRANSPARENT.md](docs/FFI_TRANSPARENT.md) for details.

### Standard Library

Built-in modules:
- `otter:math` - Mathematical functions
- `otter:io` - File I/O
- `otter:time` - Time utilities
- `otter:task` - Task-based concurrency
- `otter:rand` - Random numbers
- `otter:json` - JSON parsing
- `otter:net` - Networking
- `otter:http` - HTTP client/server

### Exception Handling

Modern exception handling with zero-cost success path:

```otter
use otter:fmt

fn divide(x: int, y: int) -> int:
    if y == 0:
        raise "Division by zero"
    return x / y

fn safe_operation():
    try:
        let result = divide(10, 0)
        fmt.println("Result: " + stringify(result))
    except Error as e:
        fmt.println("Caught error: " + stringify(e))
    else:
        fmt.println("No errors occurred")
    finally:
        fmt.println("Cleanup always runs")

fn nested_exceptions():
    try:
        try:
            raise "Inner error"
        except Error:
 