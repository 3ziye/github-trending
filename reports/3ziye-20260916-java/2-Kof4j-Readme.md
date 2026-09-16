[English](README.md) | [Português](README.pt_BR.md)

# Kof

<p align="center">
  <img src="kof.png" alt="Kof Logo" width="200">
</p>

### One language. One compiler. Many worlds.
pronounced coffe

**Less code. More intention. JVM, native, script and web. All starting from the same language.**

---

## Mascot

<p align="center">
  <img src="kof_mascot.png" alt="Kof mascot — a civetta" width="300">
</p>

Kof's mascot is a **civetta** — also known as the **musk cat**,
it is a feline that eats coffee. Nothing more fitting for a language
pronounced *coffe*.

---

## Disclaimer

The Kof language has no relationship whatsoever with the game The King of Fighters or its franchise.

The name Kof came about as a reference to the word "coffee" deliberately spelled incorrectly. The choice was made precisely in an attempt to create a short, unique and easily identifiable name for the language.

Koflang and Kof4J do not endorse the association of the name with the The King of Fighters franchise. Any similarity or association made in that sense is incidental and does not represent the origin, purpose or identity of the projects.

Our goal has always been to create a unique identity for the language and its components.

---

> Some people look at a problem and write a library.
>
> Others write a framework.
>
> Some create a tool.
>
> I apparently looked at the entire ecosystem and thought:
>
> **"This is all too complicated. I'm going to create a language."**
>
> And, apparently, a language alone wasn't enough either.

Welcome to **Kof**.

---

# What is Kof?

Kof is a **general-purpose, statically typed** programming language, built around one central idea:

> **A single language should not force you to choose a single world.**

> 📖 **The formal language specification** (grammar, type system,
> semantics, status of each feature) is in
> [`docs/language-reference/`](docs/language-reference/). The compiler
> architecture (implementation) is in
> [`docs/architecture/compiler-architecture.md`](docs/architecture/compiler-architecture.md). The
> distinction **language ≠ compiler ≠ target** is the axis of those documents.

Kof has its own compiler, lexer, parser, type system, semantic analysis and intermediate representation (Kof IR). From that IR, different backends turn the same program into different forms of execution:

```text
            Kof Language  (defined by the specification)
                          │
                    Kof Compiler  (one implementation)
                          │
                       Kof IR  (linear stack machine, 30 ops)
                          │
          ┌───────────────┼────────────────┐
          │               │                │
       JVM Backend    Native Backend    JS Backend
          │               │                │
          ▼               ▼                ▼
        JVM          Native Binary      ES Modules
       (.class)      (ELF x86_64,       (Node /
                      riscv64/aarch64)    browser)
```

**The language does not change. The target changes.** JVM, Native and JS are
*compilation targets* of the same Kof — not semantically different dialects.
**KofScript** (`.ks`, REPL) is a *direct execution target*: pure Kof consuming
the SAME frontend and executed by the IR interpreter, without compiling and
without a JVM fork — **it is not JavaScript** (`let`/`const`/`async`/`fn` do
not exist). KofC is a separate tool (C subset → ELF), it does not consume the
Kof IR — see
[docs/architecture/compiler-architecture.md](docs/architecture/compiler-architecture.md) §7.)

---

# Kof is not a transpiler

Kof does not work like this:

```text
Kof → Java → javac → JVM
```

It works like this:

```text
Kof → Kof Compiler → Kof IR → Backend → Target
```

The compiler has its own implementation of:

* lexer
* parser
* AST
* symbol resolution
* type system
* semantic analysis
* IR
* diagnostics
* code generation

Kof does not depend on Java as an intermediate language.

---

# Current State

Kof is in active development — **0.3.0-beta**.

The compiler has its own frontend, type system, Kof IR and **three backends
over the IR**, which produce **six targets**: JVM (V21 via ASM), Native x86_64
(ELF, no libc), `native.risc`/`native.arm` (real riscv64 + aarch64 via
ISA translator), KofJS (ES Modules) and Android (JVM variant + APK packaging).
**KofScript** (`.ks`, REPL) is a **direct execution target**: pure Kof
on the SAME frontend, executed by the IR interpreter (`KofInterpreter`) without
emitting bytecode or a JVM fork. **KofC** (C subset → native) is a separate
tool, it does not consume the Kof IR — see
[docs/architecture/compiler-architecture.md](docs/architecture/compiler-architecture.md) §7.

| Feature | JVM | Native | KofJS |
|---------|-----|--------|-------|
| println, variables, arithmetic | ✅ | ✅ | ✅ |
| if/else, if-expr, while, for, for-in, switch | ✅ | ✅ | ✅ |
| functions (without `fun`), lambdas with captures | ✅ | ✅ | ✅ |
| records, classes, inheritance, interfaces, virtual