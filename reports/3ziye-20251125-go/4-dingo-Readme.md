<div align="center">

# Dingo

<img src="docs/mascot.png" alt="Dingo mascot" width="200"/>

**Go that escaped.**

[![Go Version](https://img.shields.io/badge/Go-1.21+-00ADD8?style=flat&logo=go)](https://go.dev)
[![License](https://img.shields.io/badge/License-TBD-blue.svg)](LICENSE)
[![Development Status](https://img.shields.io/badge/Status-Active%20Development-orange)](https://github.com/MadAppGang/dingo)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg)](CONTRIBUTING.md)

[Features](#features-that-make-dingo-special) • [Quick Start](#quick-start) • [Examples](#real-working-examples-from-our-test-suite) • [Status](#implementation-status) • [Roadmap](#roadmap-the-realistic-version) • [Contributing](#can-i-help)

---

**At a Glance**

Sum Types: Working | Pattern Matching: Working | Error Propagation: Working | Functional Utils: Working | **Playground for Go's Future** | v1.0 Target: Late 2025

</div>

---

## Look, I love Go. But...

You know that feeling when you're writing Go and you type `if err != nil` for the 47th time in a single file?

Or when you forget to check for nil and your production server learns what a panic feels like?

Or when you're explaining to a Rust developer why Go doesn't have sum types and they look at you like you just said "we don't believe in seatbelts"?

Yeah. That's why Dingo exists.

## What's Dingo?

Think TypeScript, but for Go.

Dingo is a language that compiles to clean, idiomatic Go code. Not some franken-runtime or a whole new ecosystem. Just better syntax that becomes regular Go.

**The pitch:** Write code with Result types, pattern matching, and null safety. Get back perfect Go code that your team can read, your tools can process, and your production servers can run at exactly the same speed.

Zero runtime overhead. Zero new dependencies. Zero "what's this weird thing in my transpiled code?"

**Is this proven to work?** Yes. [Borgo](https://github.com/borgo-lang/borgo) (4.5k stars) already proved you can transpile to Go successfully. Dingo builds on that foundation with better IDE integration, source maps, and a pure Go implementation.

---

## Why "Dingo"?

Ever wonder what a dingo actually is?

Thousands of years ago, they were domesticated dogs. Well-behaved. Following commands. Controlled.

Then they escaped to the Australian wild and evolved into something science couldn't categorize. Not quite dog. Not quite wolf. **Ungovernable.**

The Go Gopher? Created at Google. Lives by the rules. Does what it's told.

**Dingo broke free.**

Here's the beautiful part: dingos are still canines. They didn't reject their DNA—they just refused to be controlled. Same with our language.

**Every Go feature still works.** Go 1.24 adds something? You get it in Dingo. Day one. Disable all plugins? You're running pure Go.

You're not losing anything. You're gaining **freedom without asking permission.**

Want pattern matching? Enable it. Want sum types? Already working. Think you can do it better? **Fork the plugin and prove it.**

**Your language. Your rules. No committee required.**

*See [MANIFESTO.md](MANIFESTO.md) for why this terrifies the establishment.*

---

## Quick Start

**Note:** Dingo is in active development. **Phase V Complete** - Infrastructure ready for v1.0 with comprehensive documentation, workspace builds, CI/CD enhancements, and 3/4 external model approval.

**Latest (2025-11-22)**: ✅ **LSP Integration Complete** - Post-AST source maps (100% accurate position mapping) + auto-rebuild on save. Edit → Save → IDE features work instantly! Hover, go-to-definition, and automatic transpilation fully functional. See [`CHANGELOG.md`](CHANGELOG.md) for details.

### Installation

```bash
# Clone the repository
git clone https://github.com/MadAppGang/dingo.git
cd dingo

# Build the compiler
go build -o dingo ./cmd/dingo

# Add to PATH (optional)
export PATH=$PATH:$(pwd)
```

### Your First Dingo Program

Create `hello.dingo`:

```go
package main

import "fmt"

func main() {
    let message = "Hello from Dingo!"
    fmt.Println(message)
}
```

Build and run:

```bash
# Transpile to Go
dingo build hello.dingo

# Or compile and run in one step
dingo run hello.dingo
```

### Try Working Features Now

**Sum Types with Pattern Matching:**

```go
enum Result {
    Ok(value: int),
    Error(message: string)
}

func divide(a: int, b: int) Result {
    if b == 0 {
        return Error("division by zero")
    }
    return Ok(a / b)
}

let result = divide(10, 2)
match result {
    Ok(value) => fmt.Printf("Success: %d\n", value),
    Error(msg) => fmt.Printf("Error: %s\n", msg)
}
```

**Safe Navigation and Null Coalescing (Phase 7 ✅):**

```go
// Property access with safe navigation
let city = user?.address?.city?.name ?? "Unknown"

// Method calls with safe navigation
let email = user?.getProfile()?.email ?? "noreply@example.com"

// Works with Go pointers too!
let timeout = config?.database?.timeout ?? 30

// Chained defaults
let theme = user?.theme ?? project?